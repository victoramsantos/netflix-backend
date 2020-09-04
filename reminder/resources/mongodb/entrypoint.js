db.createCollection("reminder");
db.reminder.insertMany([
	{
		"userId": NumberInt(1),
		"movies": [
			NumberInt(1001)
		]
	}
]);

db.createCollection("watched");
db.watched.insertMany([
	{
		"userId": NumberInt(1),
		"movies": [
			NumberInt(1001)
		]
	}
]);
