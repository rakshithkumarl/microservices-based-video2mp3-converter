# Microservices-Based Application with Python and Flask: Technical Overview

## Architecture and Functionalities

The application has distinct microservices, each of them serving a specific functionality:

- **API Gateway**: Acts as the entry point for the incoming requests to enable communication between client and server.
- **User Authentication**: Offers strong authentication mechanisms to ensure secure access to the API.
- **Video to MP3 Converter**: A service to convert video files into MP3.
- **Client Notification**: Facilitates sending the notifications to clients.

## Technologies Used

To achieve our objectives, we leverage a suite of cutting-edge technologies:

- **Python**: Primary programming language for the overall development.
- **Flask**: Web framework for developing RESTful APIs.
- **MySQL**: Relational database for storing user authentication data.
- **MongoDB**: NoSQL database for efficient media storage.
- **RabbitMQ**: Message broker that facilitates asynchronous communication between microservices.
- **Docker**: Containerization tool to containerize the microservices.
- **Kubernetes**: Container orchestration tool used for the deployment and management of containerized applications.

<!--
## Deployment Instructions

To deploy the application, follow these steps:

1. Clone the repository to your local environment.
2. Ensure Docker and Kubernetes are installed and configured properly.
3. Deploy the microservices using the provided Kubernetes manifests.
4. Customize environment variables and service configurations as necessary.

## Usage Guidelines

Upon deployment, users can interact with the application as follows:

1. Access the API gateway to initiate requests and interact with the various microservices.
2. Utilize JWT tokens for secure authentication and access control mechanisms.
3. Leverage the video to MP3 conversion service to process multimedia files efficiently.
4. Employ the client notification service to disseminate messages or notifications seamlessly.
5. Utilize MongoDB for storing and retrieving media files, ensuring scalability and performance.

## Testing Screenshots

Here you can find screenshots demonstrating the testing of our application:

- [Screenshot 1](screenshots/screenshot1.png): Describe the context of this screenshot.
- [Screenshot 2](screenshots/screenshot2.png): Describe the context of this screenshot.
- [Screenshot 3](screenshots/screenshot3.png): Describe the context of this screenshot.
-->
