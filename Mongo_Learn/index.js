var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/testingMongo', { useNewUrlParser: true, useUnifiedTopology: true });
var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function () {
    // we're connected!
    console.log("We are connected bro/sis ..")
});