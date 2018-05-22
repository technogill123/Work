var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var mongodb = require('mongodb');
var cors = require('cors');
//var Joi = require('joi');
//var expressJoi = require('express-joi-validator');
//var HttpStatus = require('http-status-codes');

var dbConn = mongodb.MongoClient.connect('mongodb://localhost:27017');

var app = express();

app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.resolve(__dirname, 'public')));


//var jsonParser = bodyParser.json();
app.use(bodyParser.json())

//app.post('/', function (req, res) {
    
    //res.status(404).send('DATA NOT')
//});



app.post('/pd', function (req, res) {
    dbConn.then(function(db) {
	var dbo = db.db("mydbs")
	var reqbody = req.body
	console.log(reqbody) 

	/*var schema = Joi.reqbody().keys({
	_id: Joi.string().required(),
        src: Joi.string().required(),
        status: Joi.string().min(2).max(5).required(),
        name: Joi.string().required(),
        description: Joi.string().required(),
        path: Joi.string().required(),
        number: Joi.string().required(),
        error: Joi.string().required()
       
  	});

	Joi.validate(reqbody, schema )*/


        //console.log(reqbody) 
        dbo.collection('vmdetails').insertOne(req.body);
    });    
    res.send('Data received:\n' + JSON.stringify(req.body));
});

app.get('/vd',  function(req, res) {
    dbConn.then(function(db) {
	var dbo = db.db("mydbs");
        dbo.collection('vmdetails').find({}).toArray().then(function(collection) {
            res.status(200).json(collection);
        });
    });

});

app.delete('/dd/:_id', function (req, res) {
    dbConn.then(function(db) {
	var ID = req.params._id;
	//console.log(req.params)
	console.log("tagId is set to " + ID)
	var dbo = db.db("mydbs") 
	//var myquery = req.body['status'];  
        //dbo.collection('vmdetails').deleteOne({ _id: ID });
 	dbo.collection('vmdetails').remove({_id: mongodb.ObjectID( req.params._id)})
    });    
    //res.send('Data deleted:\n' + JSON.stringify(req.body));
});

app.listen(process.env.PORT || 8083, process.env.IP || '192.168.106.141' );
