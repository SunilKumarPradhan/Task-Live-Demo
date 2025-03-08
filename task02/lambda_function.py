import json

def lambda_handler(event, context):
    path = event.get("rawPath", "")
    method = event.get("requestContext", {}).get("http", {}).get("method", "")
    
    if path == "/hello" and method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Hello, World!"})
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Bad Request",
                "message": f"Invalid endpoint {path} with method {method}."
            })
        }
