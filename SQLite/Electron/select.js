const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('../DataBase/db/test-table.db', err => {
  if (err) {
    return console.error(err.message);
  }
  console.log('connected to db');
});

let sqlBuilder = (emotion, val) => {
  return `SELECT * FROM user_mood WHERE ${emotion} = ${val}`;
};

db.all(sqlBuilder('sad', 5), [], (err, rows) => {
  if (err) {
    throw err;
  }
  rows.forEach(row => {
    console.log(row);
  });
});

db.close(err => {
  if (err) {
    return console.error(err.message);
  }
  console.log('closed connection');
});
