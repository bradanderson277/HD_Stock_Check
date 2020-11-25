from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URLI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    data_posted = db.Column(db.DateTime, nullable=False, default=DateTime.estnow)

    def __repr__(self):
        return 'Blog Post' + str(self.id)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'Much content'
    },
     {
        'title': 'Post 2',
        'content': 'Much content again'
    }
]

@app.route('/home')
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


def hello():
    return "hello World"

@app.route('/onlyget', methods=['GET'])
def get_req(): 
    return 'you can only get this webpage'







if __name__ == '__main__':
    app.run(debug=True)
