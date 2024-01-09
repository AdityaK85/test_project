// import {log, callAjax, sweetAlertMsg, showToastMsg} from '../../CommonJS/common';

$('a.flipper').click(function(){
  $('.flip').toggleClass('flipped');
});

window.LoginModelshow = function() {
    var modal = new bootstrap.Modal(document.getElementById('LoginModel'));
    modal.show();
}

window.close_model = function() {
    $('#LoginModel').modal('hide');
}

$('#LoginModel').on('shown.bs.modal',async function () {

}).on('hidden.bs.modal', function () {
    $( "#close_modal" ).trigger( "click" );
    location.reload()
    
});


window.LoginSignup = function (status) {
    
    var username;
    var pwd;
    var email;
    var send_data = false
    var emailfilter = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i;
    
    if (status == 'login') {

        username = $('#login_username').val()
        pwd = $('#login_pwd').val()

        if (username.trim()  == '') {
            $('#login_username').focus()
                iziToast.show({
                        title: 'Error',
                        message: 'Please select Display Name.'
                    }); 
                } 
        else if ( pwd.trim() == '' ) {
            $('#login_pwd').focus()
                iziToast.show({
                        title: 'Error',
                        message: 'Please type your Password.'
                    }); 
            
        }
        else {
            send_data = true
        }
    }
    else if (status == 'signup') {

        username = $("#sign_username").val()
        email = $("#sign_email").val()
        pwd = $("#sign_pwd").val()


        if (username.trim()  == '') {
            $('#sign_username').focus()
                iziToast.show({
                        title: 'Error',
                        message: 'Please select Display Name.'
                    }); 
                } 
        else if ( pwd.trim() == '' ) {
            $('#sign_pwd').focus()
                iziToast.show({
                        title: 'Error',
                        message: 'Please type your Password.'
                    }); 
            
        }
        else if ( email.trim() == '' ) {
            $('#sign_email').focus()
                iziToast.show({
                        title: 'Error',
                        message: 'Please type your email address.'
                    }); 
            
        }

        else if (!emailfilter.test(email) ) {
            $('#sign_email').focus()
            iziToast.show({
                    title: 'Error',
                    message: 'Please enter valid email address.'
                }); 
        }

        else {
            send_data = true
        }
    } 

    if (send_data == true) {

        var data = {
            'username' : username,
            'email' : email,
            'pwd' : pwd,
        }

        console.log("-----datat", data)
        $.ajax({
            method:"POST",
            url:"/SaveUser",
            data:data,
            success:function(response){
                if (response.status == 1){
                    Swal.fire('Login Successfully', response.msg, 'success').then(function(){
                        location.reload()
                    })
                } else if (response.status == 2 ) {
                    Swal.fire('Congratulations ,welcome ', response.msg, 'success').then(function(){
                        location.reload()
                    })
                } else {
                    Swal.fire('Nope !!', response.msg, 'error')
                }
            }
        })
    }
}