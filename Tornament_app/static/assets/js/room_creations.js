console.log('===========Room Creations========')


$("#create_room_header").addClass('active')

document.getElementById('set_password').style.display = 'none'
document.getElementById('custom_squad').style.display = 'none'
document.getElementById('game_room_type').style.display = 'none'
document.getElementById('custom_paid').style.display = 'none'


window.ChangeRoomType = function(select_field){
    if (select_field.value == 'public') {
        document.getElementById('set_password').style.display = 'none'
    } else {
        document.getElementById('set_password').style.display = 'block'
    }
}

window.Change_Team = function(select_field){
    if (select_field.value == 'custom') {
        document.getElementById('custom_squad').style.display = 'block'
    } else {
        document.getElementById('custom_squad').style.display = 'none'
    }
}

window.ChangeGameRoomType = function(select_field){
    if (select_field.value == 'private') {
        document.getElementById('game_room_type').style.display = 'block'
    } else {
        document.getElementById('game_room_type').style.display = 'none'
    }
}

window.paid_joining = function(select_field){
    if (select_field.value == 'paid_join') {
        document.getElementById('custom_paid').style.display = 'block'
    } else {
        document.getElementById('custom_paid').style.display = 'none'
    }
}



window.SetPrize = function(Value){
    if (Value.checked) {
        Swal.fire({
            title: 'Set Winning Prize?',
            text: 'Are you keeping the winning prize money or something ?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: 'Money',
            cancelButtonText: 'Something Special',
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    title: "Enter Winning Amount ",
                    input: "number",
                    inputAttributes: {
                      autocapitalize: "off"
                    },
                    showCancelButton: true,
                    confirmButtonText: "Set Prize Pool",
                    showLoaderOnConfirm: true,
                    preConfirm: async (login) => {
                    },
                    allowOutsideClick: () => !Swal.isLoading()
                  }).then((result) => {
                    if (result.isConfirmed) {
                      Swal.fire({
                        title: `${result.value.login}'s avatar`,
                        imageUrl: result.value.avatar_url
                      });
                    }else{
                        Value.checked = false;
                        
                    }
                });
            } else {
                Value.checked = false; 
                Swal.fire('Cancelled', 'You clicked No or closed the modal.', 'info');
            }
        });
    }
}

document.addEventListener("DOMContentLoaded", function () {
    var imageInput = document.getElementById('imageInput');
    var previewImage = document.getElementById('previewImage');

    imageInput.addEventListener('change', function (event) {
        var selectedFile = event.target.files[0];

        if (selectedFile) {
            var reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result;
            };
            reader.readAsDataURL(selectedFile);
        }
    });
});


window.CreateRoom  = function(){
    var joining_fee = $('#joining_fee').val()
    var join_status = $('#join_status').val()
    var title = $('#title').val()
    var description = $('#room_description').val()
    var select_game = $('#select_game').val()
    var totalMembers = $('#total_members').val()
    var tornamentDt = $('#tornament_dt').val()
    var StartTm = $('#start_tm').val()
    var EndTm = $('#end_tm').val()
    var roomType = $('#roomType').val()
    var room_pwd = $('#room_pwd').val()
    var gameType = $('#game_type').val()
    var select_members = $('#select_members').val()
    var custom_team = $('#custom_team').val()
    var map = $('#map').val()
    var game_room_id = $('#game_room_id').val()
    var game_room_type = $('#game_room_select_type').val()
    var game_room_password = $('#game_room_password').val()
    var thambnail = document.getElementById("imageInput");
    var files = thambnail.files[0];
    var userPlayerStatus = document.getElementById('userPlayerStatus').checked

    if (title.trim() == '') {
       $("#title").focus()
       iziToast.show({
             title: 'Error',
             message: 'Please Enter Title'
          });
       }
       else if ( description == '') {
          $("#room_description").focus()
          iziToast.show({
                title: 'Error',
                message: 'Please Enter Description'
             });
          
       }
       else if ( select_game.trim() == '') {
          $('#select_game').focus()
          iziToast.show({
                title: 'Error',
                message: 'Please Select the game type.'
             });
          
       }
       else if ( totalMembers.trim() == '') {
          $('#total_members').focus()
          iziToast.show({
                title: 'Error',
                message: 'Please Enter Total Member in numbers'
             });
          
       }
       else if ( tornamentDt.trim() == '') {
          $('#tornament_dt').focus()
          iziToast.show({
                title: 'Error',
                message: 'Please Enter Tornament Date.'
             });
          
       }
       else if ( StartTm.trim() == '') {
          $('#start_tm').focus()
          iziToast.show({
                title: 'Error',
                message: 'Please Enter Start Time of Tornament.'
             });
          
       }
       else if ( roomType.trim() == '') {
          $('#roomType').focus()
          iziToast.show({
                title: 'Error',
                message: 'Please select room type.'
             });  
       }
       else if ( ($('#room_pwd').css('display') == 'block') && room_pwd.trim() == 'private' ) {
          $('#room_pwd').focus()
          iziToast.show({
             title: 'Error',
             message: 'Please enter Room Joing Password.'
          });  
       }
       else if ( gameType.trim() == '') {
          $('#game_type').focus()
          iziToast.show({
                title: 'Error',
                message: 'Please select Game type.'
             });  
       }
       else if ( select_members.trim() == '') {
          $('#select_members').focus()
          iziToast.show({
                title: 'Error',
                message: 'Please select the members.'
             });  
       }
       else if ( ($('#custom_team').css('display') == 'block') && (custom_team.trim() == 'custom')) {
           $('#custom_team').focus()
           iziToast.show({
               title: 'Error',
               message: 'Please enter custom members.'
            });  
        }
        else if ( join_status.trim() == '') {
            $('#join_status').focus()
            iziToast.show({
                title: 'Error',
                message: 'Please select the members.'
            });  
        }
        else if ( ($('#joining_fee').css('display') == 'block') && (joining_fee.trim() == 'paid_join')) {
            $('#joining_fee').focus()
            iziToast.show({
                title: 'Error',
                message: 'Please enter Joining Fee.'
             });  
         }
       else if (!files && thambnail.src == "") {
          iziToast.show({
                title: 'Error',
                message: 'Please select Thumbnail.'
             });
          }
       else if (files === undefined && thambnail.src == window.location.href) {
          iziToast.show({
                title: 'Error',
                message: 'Please select Thumbnail.'
             });
       }
       else{
          var formData = new FormData();
          formData.append('thumbnail', files);
          formData.append('title', title);
          formData.append('description', description);
          formData.append('select_game', select_game);
          formData.append('totalMembers', totalMembers);
          formData.append('tornamentDt', tornamentDt);
          formData.append('StartTm', StartTm);
          formData.append('EndTm', EndTm);
          formData.append('roomType', roomType);
          formData.append('room_pwd', room_pwd);
          formData.append('gameType', gameType);
          formData.append('select_members', select_members);
          formData.append('custom_team', custom_team);
          formData.append('map', map);
          formData.append('game_room_id', game_room_id);
          formData.append('game_room_type', game_room_type);
          formData.append('game_room_password', game_room_password);
          formData.append('join_status', join_status);
          formData.append('joining_fee', joining_fee);
          formData.append('userPlayerStatus', userPlayerStatus);
          $.ajax({
             type:"POST",
             url:"/SaveRoom",
             data : formData,
             contentType: false,
            processData: false,
             success: function (response){
                if (response.status === 1) {
                    Swal.fire('Room Created', response.msg, 'success').then(function(){
                        window.location.href = '/'
                    })
                }else {
                    Swal.fire('Room Creation Failed', response.msg, 'error');
                }
             }
          })
       }
    }