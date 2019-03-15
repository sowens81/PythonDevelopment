new Mongo()
new Mongo(localhost:27107)

conn = new Mongo();
db = conn.getDB("mydb");

db.createCollection('customers')
db.customers.insert({username: "sowens81",address: {addressline1: "49 Campbell Road",addressline2: "",town: "Maidstone",county: "Kent",postcode: "ME15 6PY",country: "United Kingdom"},contact: {email: "stevejowens@icloud.com",mobile: "07427660903"}})
db.customers.insert({username: "hslee86",address: {addressline1: "49 Campbell Road",addressline2: "Tovil",town: "Maidstone",county: "Kent",postcode: "ME15 6PY",country: "United Kingdom"},contact: {email: "heather-21@live.com",mobile: "07908740375"}})
db.customers.find()

