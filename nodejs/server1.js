var express = require('express');
var cors = require('cors');
var path = require('path');
var bodyParser = require('body-parser');
var app = express();
var mongodb = require('mongodb');
var dbConn = mongodb.MongoClient.connect('mongodb://localhost:27017');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.resolve(__dirname, 'public')));

app.post('/pd', function (req, res) {
    dbConn.then(function(db) {
        delete req.body._id; // for safety reasons
        db.collection('feedbacks').insertOne(req.body);
    });    
    res.send('Data received:\n' + JSON.stringify(req.body));
});

app.get('/vd',  function(req, res) {
    dbConn.then(function(db) {
        db.mydbs('collection').find({}).toArray().then(function(collection) {
            res.status(200).json(collection);
        });
    });
});

var server = app.listen(8083, function () {
   var host = '192.168.106.141'
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})

