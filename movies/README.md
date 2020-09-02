# Movies

The **movies** microservice take account of the movie domain. Their APIs answer questions about movie details, genders of movies and searchs for movies.

## APIs
- GET /movies

List all available movies

**Request**

**Response**

200 - 
```json
[
	{
		"movieId": "string",
		"name": "string",
		"gender": ["string"]
	}
]
```

- GET /movies/{movie_id}

Visualize movie details by {movie_id}

**Request**

**Response**

200 - 
```json
{
	"movieId": "string",
	"name": "string",
	"gender": ["string"],
	"director": "string",
	"description": "string",
	"votes": "integer"
}
```

404 - 
```json
{
	"message": "string",
}
```

- GET /movies/gender/{gender}

List movies by gender

**Request**

**Response**

200 - 
```json
[
	{
		"movieId": "string",
		"name": "string",
		"gender": ["string"]
	}
]
```

- GET /movies/?={query}

Search movies by keyword

**Request**

**Response**

200 - 
```json
[
	{
		"movieId": "string",
		"name": "string",
		"gender": ["string"]
	}
]
```

- POST /movies

Add a movie

**Request**


```json
{
	"movieId": "string",
	"name": "string",
	"gender": ["string"],
	"director": "string",
	"description": "string",
}
```

**Response**

204

## Database

```json
[
	{
		"movieId": "string",
		"name": "string",
		"gender": ["string"],
		"director": "string",
		"description": "string"
	}
]
```