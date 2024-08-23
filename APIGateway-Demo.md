API Gateway Demo

API Gateway mapping template: https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html

API Gateway model:

{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"title": "Note",
	"type": "object",
	"properties": {
		"UserId": {"type": "string"},
		"NoteId": {"type": "number"},
		"Note": {"type": "string"}
	},
	"required": ["UserId","NoteId","Note"]
}

API Gateway mapping for DynamoDB:

{
	"TableName": "Notes",
	"Item": {
		"UserId": {
			"S": "$input.path('$.UserId')"
		},
		"NoteId": {
			"N": "$input.path('$.NoteId')"
		},
		"Note": {
			"S": "$input.path('$.Note')"
		}
	}
}

API Gateway test payload:

Invalid payload: {"cuma":"test"}
Valid payload: {"UserId":"StudentX","NoteId":22,"Note":"Demo API Gateway"}