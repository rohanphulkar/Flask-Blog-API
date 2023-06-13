# Flask Blog API

The Flask Blog API is a lightweight Flask-based API that provides essential functionality for managing posts or blogs. It allows users to register, log in, create, update, and delete posts. The API utilizes JSON Web Token (JWT) authentication, password hashing with Bcrypt, and a JSON database powered by TinyDB.

## Features

- User Registration: Users can register by providing their email and password.
- User Login: Registered users can log in using their credentials to obtain an access token.
- Create Post: Authenticated users can create a new post by providing a title and content.
- Update Post: Authenticated users can update the title and content of an existing post.
- Delete Post: Authenticated users can delete a post based on its ID.
- Retrieve Single Post: Authenticated users can retrieve a specific post based on its slug.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/rohanphulkar/Flask-Blog-API.git
   cd Flask-Blog-API
   ```

2. Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Run the application:

```
python app.py
```

5. The Flask API will be accessible at `http://localhost:5000`

## API Endpoints

- `POST /register`: Register a new user by providing an email and password in the request body.
- `POST /login`: Authenticate and obtain an access token by providing the email and password in the request body.
- `GET, POST /`: Retrieve all posts or create a new post. Requires a valid access token.
- `GET /<string:slug>`: Retrieve a specific post based on the slug. Requires a valid access token.
- `PATCH /<string:id>`: Update a post by providing the post ID and new title/content in the request body. Requires a valid access token.
- `DELETE /<string:id>`: Delete a post by providing the post ID in the request body. Requires a valid access token.
