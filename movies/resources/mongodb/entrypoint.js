db.createCollection("movies");
db.movies.insertMany([
	{
		"movieId": NumberInt(1001),
		"name": "Matrix",
		"gender": ["Adventure","Sci-Fi"],
		"director": "Wachowski Brothers",
		"description": "Neo starts saving the world, the real one"
	}
]);