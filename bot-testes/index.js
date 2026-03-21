const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client();

const sofiaMensagens = new Array['sofia linda', 'sofia maravilhosa', 'ian lindo', 'ian maravilhoso']


client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('message_create', message => {

	if (message.body !== sofiaMensagens) {
		// send back "pong" to the chat the message was sent in
		client.sendMessage(message.from, 'cu');
	}

    if(message.body === sofiaMensagens){
        client.sendMessage(message.from, 'concordo');
    }
});


client.initialize();
