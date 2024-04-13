// import  WebSocketServer  from 'ws';

const { WebSocketServer } = require('ws')

const wss = new WebSocketServer({ port: 8765 });

let clients = {}

let expected = {
  'Speed limit (30km/h)': {
    speed: 30
  },
  'Stop': {
    speed: 0
  },
  'No entry': {
    straight: false
  },
  'Bumpy road': {
    speed: 20
  },
  'Pedestrians': {
    speed: 20
  },
  'Turn right ahead': {
    left: false
  },
  'Turn left ahead': {
    right: false

  },
  'Ahead only': {
    straight: true
  },
  'Road work': {
    speed: 20
  }
}
wss.on('connection', function connection(ws) {
  ws.on('error', console.error);

  let i = 0

  ws.on('message', function message(data) {
    parsedData = JSON.parse(data)
    var nameValue = parsedData.name
    var message = parsedData.message
    clients[nameValue] = message
    // console.log("before remove",clients)
    if (nameValue == 'Model') {

      switch (clients.Model.result) {
        case 'Speed limit (30km/h)':
          if (clients.Vehicle.speed > expected[clients.Model.result].speed) {
            i = i + 1
            
          }
          break

        case 'Stop':
          if (clients.Vehicle.speed != expected[clients.Model.result].speed) {
            i = i + 1
          }
          break

        case 'No entry':
          if (clients.Vehicle.straight != expected[clients.Model.result].straight) {
            i = i + 1
          }
          break

        case 'Bumpy road':
          if (clients.Vehicle.speed > expected[clients.Model.result].speed) {
            i = i + 1
          }
          break

        case 'Pedestrians':
          if (clients.Vehicle.speed > expected[clients.Model.result].speed) {
            i = i + 1
          }
          break

        case 'Road work':
          if (clients.Vehicle.speed > expected[clients.Model.result].speed) {
            i = i + 1
          }
          break

        case 'Turn right ahead':
          if (clients.Vehicle.left == expected[clients.Model.result].left) {
            i = i + 1
          }
          break

        case 'Turn left ahead':
          if (clients.Vehicle.right == expected[clients.Model.result].right) {
            i = i + 1
          }
          break

        case 'Ahead only':
          if (clients.Vehicle.straight == expected[clients.Model.result].straight) {
            i = i + 1
          }
          break;
      }
      if(i>90){
       
        console.log(`Traffic signal ${parsedData.message.result} violated!!!`)
        i=0
      }

    }

    delete clients['Model']
  
    ws.send('OK');
});
});