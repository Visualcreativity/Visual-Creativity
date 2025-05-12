# API Reference

## Overview

The Visual Creativity API provides programmatic access to our AI-powered visual generation platform. This reference documentation covers all available endpoints, parameters, and response formats.

## Authentication

### API Keys

All API requests require authentication using an API key. Include your API key in the request header:

```http
Authorization: Bearer your_api_key
```

## Base URL

```
https://api.visualcreativity.com/v1
```

## Endpoints

### Generation API

#### Create Image

```http
POST /generate/image
```

**Parameters**

```json
{
  "scene": {
    "subjects": [{
      "type": "string",
      "style": "string",
      "pose": "string"
    }],
    "background": {
      "type": "string",
      "style": "string"
    },
    "resolution": "string",
    "format": "string"
  }
}
```

**Response**

```json
{
  "id": "string",
  "status": "string",
  "url": "string",
  "metadata": {
    "resolution": "string",
    "format": "string",
    "generation_time": "number"
  }
}
```

#### Get Generation Status

```http
GET /generate/status/{id}
```

**Response**

```json
{
  "id": "string",
  "status": "string",
  "progress": "number",
  "eta": "number"
}
```

### Style API

#### List Styles

```http
GET /styles
```

**Response**

```json
{
  "styles": [{
    "id": "string",
    "name": "string",
    "description": "string",
    "preview_url": "string"
  }]
}
```

#### Get Style Details

```http
GET /styles/{id}
```

**Response**

```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "parameters": {
    "artistic_style": "string",
    "color_scheme": "string",
    "lighting": "string"
  },
  "preview_url": "string"
}
```

### Model API

#### List Models

```http
GET /models
```

**Response**

```json
{
  "models": [{
    "id": "string",
    "name": "string",
    "version": "string",
    "capabilities": ["string"]
  }]
}
```

#### Get Model Details

```http
GET /models/{id}
```

**Response**

```json
{
  "id": "string",
  "name": "string",
  "version": "string",
  "capabilities": ["string"],
  "parameters": {
    "resolution_range": {
      "min": "string",
      "max": "string"
    },
    "supported_formats": ["string"]
  }
}
```

## WebSocket API

### Real-time Generation

```javascript
// Connect to WebSocket
const ws = new WebSocket('wss://api.visualcreativity.com/v1/ws');

// Authentication
ws.send(JSON.stringify({
  type: 'auth',
  api_key: 'your_api_key'
}));

// Start generation
ws.send(JSON.stringify({
  type: 'generate',
  scene: {
    // Scene parameters
  }
}));

// Receive updates
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Generation progress:', data.progress);
};
```

## Error Handling

### Error Codes

| Code | Description |
|------|-------------|
| 400  | Bad Request |
| 401  | Unauthorized |
| 403  | Forbidden |
| 404  | Not Found |
| 429  | Too Many Requests |
| 500  | Internal Server Error |

### Error Response Format

```json
{
  "error": {
    "code": "number",
    "message": "string",
    "details": {
      "field": "string",
      "reason": "string"
    }
  }
}
```

## Rate Limits

- Standard tier: 100 requests per minute
- Professional tier: 1000 requests per minute
- Enterprise tier: Custom limits

## SDK Support

### Official SDKs

- [Python SDK](https://github.com/visualcreativity/python-sdk)
- [Node.js SDK](https://github.com/visualcreativity/node-sdk)
- [Java SDK](https://github.com/visualcreativity/java-sdk)

## Webhooks

### Configuration

```http
POST /webhooks
```

**Parameters**

```json
{
  "url": "string",
  "events": ["string"],
  "secret": "string"
}
```

### Event Types

- `generation.completed`
- `generation.failed`
- `model.updated`
- `style.added`

## Best Practices

1. **Error Handling**
   - Implement proper error handling
   - Use exponential backoff for retries
   - Monitor API response times

2. **Performance**
   - Use batch operations when possible
   - Implement caching strategies
   - Monitor rate limits

3. **Security**
   - Secure API keys
   - Validate webhook signatures
   - Use HTTPS for all requests

## Support

For API support and updates:

1. Join our [Developer Community](../community/developers.md)
2. Check our [Status Page](https://status.visualcreativity.com)
3. Contact API support team