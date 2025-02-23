const express = require('express');
const mysql = require('mysql');
const app = express();
const port = 5000;
//create a connection to the database
const db = mysql.createConnection({
    host: 'localhost',   
    user: 'root',
    password: 'password',
    database: 'open_heart'
}); 

// Connect to the database
db.connect((err) => {
    if(err){
        throw err;
    }
    console.log('Connected to database');
});
//create a simple route
app.get('/', (req, res) => {
    res.send('Hello from the server');
});

//start the server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});