db.createCollection("ranking");
db.ranking.insertMany([
	{
		"movieId": NumberInt(1001),
		"votes": NumberInt(1)
	}
]);
