from twitoff import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    # tweets = db.relationship('Tweet', backref=db.backref('author', lazy=True))

    def __repr__(self):
        return '<User {}>'.format(self.name)
    
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.Unicode(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.tweet)