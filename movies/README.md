# Movies

The **movies** microservice take account of the movie domain. Their APIs answer questions about movie details, genders of movies and searchs for movies. Its database is built by the [movie scraper](./movie-scraper) which reads our IMDB dataset and populate the movies' database.

## APIs
- GET /movies

List all available movies

**Request**

**Response**

200 - 
```json
[
	{
		"movieId": "integer",
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
	"movieId": "integer",
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
	"message": "string"
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
		"movieId": "integer",
		"name": "string",
		"gender": ["string"]
	}
]
```

- GET /movies/?q={query}

Search movies by keyword

**Request**

**Response**

200 - 
```json
[
	{
		"movieId": "integer",
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
	"movieId": "integer",
	"name": "string",
	"gender": ["string"],
	"director": "string",
	"description": "string"
}
```

**Response**

204

## Database

```json
[
	{
		"movieId": "integer",
		"name": "string",
		"gender": ["string"],
		"director": "string",
		"description": "string"
	}
]
```