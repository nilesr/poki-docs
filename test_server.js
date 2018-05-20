const file = "brl.1"
const WebSocket = require('ws');
const fs = require('fs')
const { exec } = require("child_process")

const wss = new WebSocket.Server({ port: 8080 });
var wssl = null;

var send = function send() {
  if (wssl == null) return;
  exec("env BROWSER=cat man -H -l " + file, function(_, stdout) {
	wssl.send(stdout);
  });
}

wss.on('connection', function connection(ws) {
  console.log('new connection');
  wssl = ws;
  send();
});

fs.watch(file, {}, function(e, _) {
  //if (e != "change") return;
  console.log("Got event")
  send();
});

console.log('running')
