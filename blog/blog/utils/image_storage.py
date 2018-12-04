from django.core.files.storage import Storage
from qiniu import Auth, put_data

from django.conf import settings

from blog.settings.dev import access_key, secret_key, bucket_name, qiniu_domainname


class QiniuStorage(Storage):

    def _save(self, name, content):
        try:
            q = Auth(access_key, secret_key)
            token = q.upload_token(bucket_name)
            ret, info = put_data(token, None, content.read())
        except Exception as e:
            raise e

        if info.status_code != 200:
            raise Exception("上传图片失败")
        return ret["key"]

    def url(self, name):

        return qiniu_domainname +name

    def exists(self, name):
        """
        判断文件是否存在，FastDFS可以自行解决文件的重名问题
        所以此处返回False，告诉Django上传的都是新文件
        :param name:  文件名
        :return: False
        """
        return False
