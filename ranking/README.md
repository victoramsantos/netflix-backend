# Ranking

The **ranking** microservice take account of the votes and movies ranking. Their APIs collect users likes and compute the ranking. Here we also provide a ranking by gender and the top 10 overall movies.

## APIs

- POST /votes/{movie_id}/like

Provide a vote option to like movies

**Request**

**Response**

204

- GET /votes/{movie_id}

Retrieve votes of a movie

**Request**

**Response**

200 - 
```json
{
	"movieId": "integer",
	"votes": "integer"
}
```

404 - 
```json
{}
```

- GET /ranking/gender/{gender}

List ranked movies by gender

**Request**

**Response**

200 - 
```json
[
	{
		"movieId": "integer",
		"name": "string",
		"votes": "integer"
	}
]
```

## Database
```json
[
	{
		"movieId": "integer",
		"votes": "integer"
	}
]
```