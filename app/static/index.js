var socket = io.connect('http://' + document.domain + ':' + location.port);
var i_name = document.querySelector('#i_name');
var i_message = document.querySelector('#i_message');
var sec_home = document.querySelector('#sec_home');
var frm_home = document.querySelector('#frm_home');
var sec_chat = document.querySelector('#sec_chat');
var frm_chat = document.querySelector('#frm_chat');
var d_message = document.querySelector('#d_message');

frm_home.addEventListener('submit', function(ev){
    sec_home.style.display = 'none';
    sec_chat.style.display = 'grid';
    socket.emit('enter', i_name.value);
    ev.preventDefault();
});

frm_chat.addEventListener('submit', function(ev){
    socket.emit('message', {
        name: i_name.value,
        message: i_message.value
    });
    ev.preventDefault();
    i_message.value = '';
});

socket.on('message', function(data) {
    d_message.innerHTML += '<p><strong>' + data.name + ': </strong>' + data.message + '</p>';
});

socket.on('notification', function(data) {
    d_message.innerHTML += '<p><strong>' + data + '</strong></p>';
});
