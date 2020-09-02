# Reminder

The **reminder** microsservice collect the reminder and watch later movies list. Their APIs collect users desire for reminder a movie and to set movies as watched.

## APIs

- POST /reminder/{user_id}/{movie_id}

Add a reminder for a movie

**Request**

**Response**

204


- GET /reminder/{user_id}

Provide a reminder list of movies

**Request**

**Response**

200 - 
```json
[
	{
		"movieId": "string"
	}
]
```

- POST /watched/{user_id}/{movie_id}

Set a movie as watched 

**Request**

**Response**

204

- GET /watched/{user_id}

List watched movies for an user

**Request**

**Response**

200 - 
```json
[
	{
		"movieId": "string"
	}
]
```