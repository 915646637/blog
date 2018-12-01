from django.contrib.auth import login
from rest_framework import serializers

from passport.models import User


class RegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(label="确认密码", max_length=20, write_only=True)
    token = serializers.CharField(label="token", read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'token', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("密码和确认密码不正确")
        if not attrs['email']:
            raise serializers.ValidationError("邮箱不能为空")

        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        user = super().create(validated_data)

        # 调用django的认证系统加密密码
        user.set_password(validated_data['password'])
        user.save()
        login(self.root.context['request'],user)
        return user


