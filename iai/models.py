from iai import db


# answer_voter = db.Table(
#     'answer_voter',
#     # db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
#     db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True),
#     db.Column('rates', db.Integer, nullable=True),
# )



class Prompt(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    component = db.Column("component", db.String(200), nullable=False)
    content = db.Column("content", db.Text(), nullable=False)
    create_date = db.Column("create_date", db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('prompt_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)


class Answer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    prompt_id = db.Column("prompt_id", db.Integer, db.ForeignKey('prompt.id', ondelete='CASCADE'))
    prompt = db.relationship('Prompt', backref=db.backref('answer_set'))
    content = db.Column("content", db.Text(), nullable=False)
    create_date = db.Column("create_date", db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    # voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))
    
class Rating(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    answer_id = db.Column("answer_id", db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'))
    answer = db.relationship('Answer', backref=db.backref('ratings'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('ratings'))
    rate = db.Column("rate", db.Integer, nullable=True)
    db.UniqueConstraint('answer_id', 'user_id', name='unique_rating')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# class Feedback(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'))
#     answer = db.relationship('Answer', backref=db.backref('feedback_set'))
#     content = db.Column(db.Text(), nullable=False)
#     create_dt = db.Column(db.DateTime(), nullable=False)