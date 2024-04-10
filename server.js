// import  WebSocketServer  from 'ws';

const {WebSocketServer} = require('ws')

const wss = new WebSocketServer({ port: 8765 });

wss.on('connection', function connection(ws) {
  ws.on('error', console.error);

  ws.on('message', function message(data) {
    console.log('received: %s', data);
    ws.send('something');
  });

  // ws.send('something');
});