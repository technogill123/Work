var express = require('express');
var cors = require('cors');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
var app = express();
app.use(cors());


  MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydbs");
  dbo.collection("collection").find({}).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
  });
}); 

var server = app.listen(8083, function () {
   var host = '192.168.106.141'
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})


