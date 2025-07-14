# Guidance for Task: FastAPI Profile Upload API

## Requirements
- Implement a FastAPI API endpoint that allows authenticated users to create or update their profile, with optional avatar image upload.
- Only allow PNG/JPEG images up to 2MB. Images must be stored within a per-user folder (user identifier).
- Asynchronously generate a thumbnail of the uploaded image using FastAPI's BackgroundTasks.
- Use FastAPI routers, pydantic models, and dependency injection for authentication and logging.
- Log all actions (uploads and errors) using structured JSON logs (parseable for audit/security purposes).
- Ensure all API responses, including errors, have a consistent, informative structure.
- Document the endpoint(s), expected models, authentication flow, and result examples via OpenAPI (Swagger).
- Provide tests that cover both successful and invalid file upload scenarios.

## Task Expectations
- Review the provided code structure and files. You'll find partial implementations and basic structure in place, but some elements are incomplete or need enhancement (validation, thumbnailing, logging, etc).
- Implement all missing or incomplete logic for secure file validation, proper directory management, consistent error handling, and robust logging.
- Ensure each upload is validated for file type and file size before saving, and use BackgroundTasks to generate a thumbnail after upload.
- Make responses uniform and informative on success and all error cases, including validation and authentication errors.
- Be sure all logging is structured and parseable by log tools for audit purposes.
- Confirm that all endpoints and models are well-documented in the auto-generated docs.
- Authentication is simulated and you should support the sample token in the dependency for testing.

## Verifying Your Solution
- Check that you can upload a valid file and receive a correct response with avatar URL.
- Verify that uploads with bad type or size are rejected with the correct error format and logged appropriately.
- Ensure logs are output in structured JSON.
- Run the provided tests to check both success and failure scenarios.
- Consult the OpenAPI (Swagger UI) at /docs and confirm models and authentication workflow are well described.
