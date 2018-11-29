var vm = new Vue({
    el: '#app',
    // 声明vue变量使用[[语法
    delimiters: ['[[', ']]'],
    data: {
        host:"127.0.0.1",
        username: sessionStorage.username || localStorage.username,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        loginusername:'',
        password:'',
        error_username: false,
        error_pwd: false,
    },
    // mounted: function(){
    //     this.get_cart();
    // },
    methods: {
        // 退出
        check_username: function(){
            if (!this.loginusername) {
                this.error_username = true;
            } else {
                this.error_username = false;
            }
        },
        check_pwd: function(){
            if (!this.password) {
                this.error_pwd_message = '请填写密码';
                this.error_pwd = true;
            } else {
                this.error_pwd = false;
            }
        },
        on_submit: function(){
            this.check_username();
            this.check_pwd();

            if (this.error_username == false && this.error_pwd == false) {
                axios.post(this.host+'/authorizations/', {
                        username: this.loginusername,
                        password: this.password
                    }, {
                        responseType: 'json',
                        withCredentials: true
                    })
                    .then(response => {
                        // 使用浏览器本地存储保存token
                            // 记住登录
                        sessionStorage.clear();
                        localStorage.token = response.data.token;
                        localStorage.user_id = response.data.user_id;
                        localStorage.username = response.data.username;
                        // 跳转页面
                        var return_url = this.get_query_string('next');
                        if (!return_url) {
                            return_url = '/index.html';
                        }
                        location.href = return_url;
                    })
                    .catch(error => {
                        this.error_pwd = true;
                    })
            }
        },
        logout: function(){
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },
        // 获取购物车数据
        // get_cart: function(){

        // }
    }
});