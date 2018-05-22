var express = require('express');
var cors = require('cors');
var app = express();
var MongoClient = require('mongodb').MongoClient;
var database = undefined;

var dbUrl = 'mongodb://127.0.0.1:27017/security';
MongoClient.connect(dbUrl, function(err, db) {
  if (err) {
    throw err;
  } else {
    database = db;
    console.log('MongoDB connection successful');
}
});

app.use(cors());
app.get('/', function (req, res) {
   res.send('Hello World');
})

app.get('/user', function (req, res) {
  res.json([
    {"src":"http://images.all-free-download.com/images/graphicthumb/green_globe_ok_tic_584.jpg","status":"OK","name":"First VM","description":"Bussiness VMs" , "path":"/tintri/first_VM", "number":10, "error":0},
    {"src":"https://cdn1.iconfinder.com/data/icons/color-bold-style/21/08-512.png","status":"ERROR","name":"Second VM","description":"Virtual VMs" , "path":"/tintri/second_VM", "number":15, "error":6},
    {"src":"http://images.all-free-download.com/images/graphicthumb/green_globe_ok_tic_584.jpg","status":"OK","name":"Third VM","description":"Critical VMs" , "path":"/tintri/third_VM", "number":8, "error":0},
    {"src":"http://images.all-free-download.com/images/graphicthumb/green_globe_ok_tic_584.jpg","status":"OK","name":"Fourth VM","description":"Logical VMs" , "path":"/tintri/fourth_VM", "number":20, "error":0},
    {"src":"http://images.all-free-download.com/images/graphicthumb/green_globe_ok_tic_584.jpg","status":"OK","name":"Fifth VM","description":"Physical VMs" , "path":"/tintri/fifth_VM", "number":20, "error":0},{"src":"http://images.all-free-download.com/images/graphicthumb/green_globe_ok_tic_584.jpg","status":"OK","name":"Sixth VM","description":"Logical VMs" , "path":"/tintri/sixth_VM", "number":21, "error":0}
  ]);
})

var server = app.listen(8083, function () {
   var host = '192.168.106.141'
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})

