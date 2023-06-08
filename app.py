from flask import Flask,jsonify,request
from tinydb import TinyDB,Query
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_bcrypt import Bcrypt
from slugify import slugify
import uuid

# Initialize TinyDB databases
user_db = TinyDB('users.json')
post_db = TinyDB('posts.json')

# Initialize Query objects for database queries
User = Query()
Post = Query()

# Initialize Flask application
app = Flask(__name__)

# Configure JWT secret key
app.config['JWT_SECRET_KEY'] = 'AST5arGrxz'

# Initialize Bcrypt and JWTManager
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@app.route('/', methods=['GET', 'POST'])
@jwt_required()
def posts():
    if request.method == 'POST':

        # Create a new post
        if not 'title' in request.json:
            return jsonify({'error': 'title is required'})
        if not 'content' in request.json:
            return jsonify({'error': 'content is required'})
        title = request.json['title']
        content = request.json['content']
        slug = slugify(title)
        id = str(uuid.uuid4())
        post_db.insert({'id':id,'title': title, 'content': content, 'slug':slug})
        return jsonify({'success':'Post successfully created'})
    
    # Retrieve all posts
    posts = post_db.all()
    return jsonify(posts)

@app.route("/<string:slug>", methods=['GET'])
@jwt_required()
def get_single_post(slug):
    # Retrieve a specific post based on the slug
    post = post_db.search(Post.slug==slug)
    return jsonify(post)

@app.route("/<string:id>",methods=['PATCH'])
@jwt_required()
def update_post(id):
    # Update a post based on its ID
    title = request.json.get('title')
    content = request.json.get('content')
    data = {}
    if title:
        data['title'] = title
    if content:
        data['content'] = content
    post = post_db.update(data,Post.id==id)
    return jsonify({'success': 'Post successfully updated'})

@app.route("/<string:id>",methods=['DELETE'])
@jwt_required()
def delete_post(id):
    # Delete a post based on its ID
    post = post_db.remove(Post.id==id)
    return jsonify({'success': 'Post successfully deleted'})

@app.route("/register",methods=['POST'])
def register():
    # User registration
    email = request.json['email']
    password = request.json['password']
    user_exists = user_db.search(User.email==email)
    if not user_exists:
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user_db.insert({'email': email,'password': hashed_password})
        return jsonify({'success':'user registration successful'}),201
    return jsonify({'error':'user already exists'}),400

@app.route("/login", methods=['POST'])
def login():
    # User login
    if not 'email' in request.json:
        return jsonify({'error': 'email is required'})
    if not 'password' in request.json:
        return jsonify({'error': 'password is required'})
    email = request.json['email']
    password = request.json['password']
    user = user_db.get(User.email==email)
    if not user:
        return jsonify({'error':'user not found'})
    if bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=user['email'])
        return jsonify({'access_token':access_token}),200
    return jsonify({'error':'invalid password'}),400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)