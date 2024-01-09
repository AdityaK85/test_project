import {log, callAjax, sweetAlertMsg, showToastMsg} from '../../CommonJS/common.js';
log("----USED----")


window.JoinCustom = async function(room_id , user_id){
    if (user_id.trim() == 'None'  )
    {
        var checkUser = await sweetAlertMsg('User Not Login', 'Kindly access your account or initiate the account creation process.', 'question', 'cancel', 'Login', 'Back');
        if (checkUser) {
            $('#LoginModel').modal('show');
        } else {
            location.href = '/'
        }
    } else {
        data = {
            'room_id' : room_id, 
            'user_id': user_id,
        }
        var response =  await callAjax('/joinCustom', data);
        if (response.status == '1') {
            await sweetAlertMsg('Room Joined ' , response.msg, 'success').then(()=> {
                location.reload()
            })
        } else {
            showToastMsg('Failed to Join ', response.msg , 'error');
        }

    }
}