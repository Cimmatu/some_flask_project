from app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    exp = db.Column(db.Integer)

    #def __init__(self, *args, **kwargs):
        #uper(Employee, self).__init__(*args, **kwargs)

    def __init__(self, name, last_name, age, exp):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.exp = exp

    #def __repr__(self):
        #return '<Employee name: {}, last_name: {}, age: {}, exp: {}>'.format(
           # self.name, self.last_name, self.age, self.exp)
