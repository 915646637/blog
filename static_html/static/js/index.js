var vm = new Vue({
    el: '#app',
    // 声明vue变量使用[[语法
    delimiters: ['[[', ']]'],
    data: {
        host:"http://127.0.0.1:8000/",
        username: sessionStorage.username || localStorage.username,
        user_id: sessionStorage.user_id || localStorage.user_id,
        login_username:'',
        login_password:'',
        error_username: false,
        error_pwd: false,
        error_login:false,
        error_msg:"",

        register_username:'',
        register_password:'',
        register_password2:'',
        register_email:'',
        error_register:false,
        error_register_msg:"",

        navs:"",
        articleList:"",
        hostarticleList:"",
        carouselLIst:"",

        total_page:"",
        page:1,
        next:"",
        previous:"",

    },
    mounted:function(){
        this.get_navs();
        this.get_articleList();
        this.get_hostarticleList();
        this.get_carouselLIstList();
    },

    methods: {
        get_next_page:function () {
            axios.get(this.next, {}, {
                responseType: 'json',
                withCredentials: true
            })
            .then(response => {
                this.articleList = response.data
                this.page += 1
                this.next = response.data.next
                this.previous = response.data.previous
                document.documentElement.scrollTop = document.body.scrollTop = 0;
            })
            .catch(error => {
                alert("服务器内部错误")
            })
        },
        get_previous_page:function () {
            axios.get(this.previous, {}, {
                responseType: 'json',
                withCredentials: true
            })
            .then(response => {
                this.articleList = response.data
                this.page -= 1
                this.next = response.data.next
                this.previous = response.data.previous
                document.documentElement.scrollTop = document.body.scrollTop = 0;
            })
            .catch(error => {
                alert("服务器内部错误")
            })
        },

        get_carouselLIstList:function () {
            axios.get(this.host + "carouselLIstList/", {}, {
                responseType: 'json',
                withCredentials: true
            })
            .then(response => {
                this.carouselLIst = response.data
            })
            .catch(error => {
                alert("服务器内部错误")
            })

        },
        get_hostarticleList:function () {
            axios.get(this.host + "hostArticleLists/", {

            }, {
                responseType: 'json',
                withCredentials: true
            })
            .then(response => {
                this.hostarticleList = response.data
            })
            .catch(error => {
                alert("服务器内部错误")
            })

        },
        get_articleList:function () {
            axios.get(this.host + "articleLists/", {
                params:{
                    category:'all',
                }
            }, {
                responseType: 'json',
                withCredentials: true
            })
            .then(response => {
                this.articleList = response.data
                this.total_page = Math.ceil(response.data.count/5)
                this.page = 1
                this.next = response.data.next
                this.previous = response.data.previous
            })
            .catch(error => {
                alert("服务器内部错误")
            })

        },
        get_navs:function () {
            axios.get(this.host+'navs/', {
                }, {
                    responseType: 'json',
                    withCredentials: true
                })
                .then(response => {
                    this.navs = response.data
                })
                .catch(error => {
                    alert("服务器内部错误")
                })
        },

        get_csrf_token:function () {
          csrf_cookie = document.cookie.split("=")
          return csrf_cookie[1]
        },

        check_username: function(){
            if (!this.login_username) {
                this.error_username = true;
            } else {
                this.error_username = false;
                this.error_login = false;
            }
        },
        check_pwd: function(){
            if (!this.login_password) {
                this.error_pwd_message = '请填写密码';
                this.error_pwd = true;
            } else {
                this.error_pwd = false;
                this.error_login = false;
            }
        },

        on_submit: function(){
            this.check_username();
            this.check_pwd();

            if (this.error_username == false && this.error_pwd == false) {
                axios.post(this.host+'user/login/', {
                        username: this.login_username,
                        password: this.login_password,
                    }, {
                        responseType: 'json',
                        withCredentials: true
                    })
                    .then(response => {
                        localStorage.username = response.data.username;
                        // 跳转页面
                        return_url = '/index.html';
                        location.href = return_url;
                    })
                    .catch(error => {
                        this.error_login=true
                        this.error_msg = error.response.data.error
                    })
            }
        },
        register: function () {

            axios.post(this.host+'user/register/', {
                    username: this.register_username,
                    password: this.register_password,
                    password2: this.register_password2,
                    email: this.register_email,
                }, {
                    responseType: 'json',
                    withCredentials: true
                })
                .then(response => {
                    // 使用浏览器本地存储保存token
                    localStorage.username = response.data.username;
                    // 跳转页面
                    return_url = '/index.html';
                    location.href = return_url;
                })
                .catch(error => {
                    this.error_register = true;
                    this.error_register_msg = "数据错误"
                })
            // }
        },
        logout: function(){
            axios.post(this.host+'user/logout/', {
                },
                {
                    responseType: 'json',
                    withCredentials: true,
                    headers: {
                        'X-CSRFToken': this.get_csrf_token()
                    }
                })
                .then(response => {
                    localStorage.clear();
                    // 跳转页面
                    return_url = '/index.html';
                    location.href = return_url;
                })
                .catch(error => {
                    alert("服务器内部错误")
                })
        },
    }
});