# Support

The **support** microservice posts the user message to a Kafka topic in order to notify the _technical support_ team.

## APIs

- POST /support/{user_id}

Open a technical support for problems

**Request**

```json
{
	"message": "string"
}
```

**Response**

204
