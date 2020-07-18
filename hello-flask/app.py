from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import os

app = Flask(__name__)
# we are telling flask where our database is located, we aske the comoputer wher the application is created
basedir =  os.path.abspath(os.path.dirname(__file__))
# we want to create adatabase, , we need to pass in the basedir that we want it to go and we want to name it ssqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
# We are making posible to create a data base and now we are instantiating a database objectand a mrshmallow object
db = SQLAlchemy(app)
ma = Marshmallow(app)
# this db object allows us to create the database
# marshmallo allows us to create a Schema it gives us the srtuucture---
# no we create a Schemma -REMEBER THIS IS LIKE A LEARNING MANAGEMENT SYSTEM
# the rimary key allows t have built in function it will make the id unique, and erey new guide will have a new incrementing id
# it says it come from the dtabase column and then it states the kind of data structure,and the length of it, 
# for example the title column in the guide Scheema is not going to be unique , contrary to the uniqueness of the id, 
class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)
# now whenever a new guide is calles we need to have a basic constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content
        # we did not nee to do the same with id because that is automatic that why is a primary key
# now we create the Schemma class itself, using marshmallow because is what allows us to work with 
class GuideSchema(ma.Schema):
    class Meta:
        fields : ('title', 'content')

guide_schema= GuideSchema()
guides_schema = GuideSchema(many=True)
    
# Create a POST API Endpoint - to create a new guide programatically
# if you want to create a new guide you are going to point to this endpoint and use the http POST method at the /guide route- now we will create a method
@app.route('/guide', methods=['POST'])
def add_guide():
    title = request.json['title'] #so this is requesting from the database, and will be like a dictionay lookup , will parse it and store it in the variable(the Title obviously)
    content = request.json['content']#this means we will have acces to the totle and the content

    new_guide = Guide(title, content) #this is instabtiatin from the past lines, storing it in the new guide variable
# we are creating a new database session and is going to add that new guide onside of it,
    db.session.add(new_guide)
    # this commit thing is from the sqlachemy we are opening up a new conectiont to the database and we want to add info inside of it
    db.session.commit()

    #now lets make sure that it works, by queyngs, is a bad practice to create a guide without returning something
    # this wiil look up for the new guide id and will store it in the guide variable
    guide = Guide.query.get(new_guide.id)
    # this will return the ghide_schema but converted to a json file,(the guide variable.)
    return guide_schema.jsonify(guide)
# THIS IS A JSON API

# now we need a URL to get all the guide
# endpornt to query guides

@app.route('/guides', methods=['GET'])#GET is the http function that we want t use
def get_guides():
    all_guides = Guide.query.all()#this is goingt to get back all of the guide f the system
    result = guides_schema.dump(all_guides)#now we are using not the single guide but the one that allows us to work with ultible bacause many=True--dump is a function of marshmallow
#   return jsonify(result.data)#well get back the json data fro the result variable--
# # IMPORTANTE ok so in the version 3.0, no need to access .data attribute, dump already returns the data- data was deserialized in Marshmallow
    return jsonify(result)

# this all to create the crude option s for a very basic learning management system

# Endpoint for quering a single guide, not a collection but a single item
# now we need to tell th eapp.route our app the decotation what guide to brong back
@app.route('/guide/<id>', methods=['GET'])# this <id> thing is what allows us to later ask for a specific guide
def get_guide(id):#this time we do pass an argument : the id
    guide = Guide.query.get(id)#tells flask to look out for /guide/and the id that we are looking for, and it will get the id placing it in the new vaiable guide
    return guide_schema.jsonify(guide) #it turns it into a json and it structures it wth schema

# Endponit to Updating a guide #this |PUT| tells tfask what action
@app.route('/guide/<id>', methods=['PUT'])#we use <> because we need to know hwat guide are we oing to be updating
def guide_update(id):
    guide = Guide.query.get(id)
    title = request.json['title']
    content = request.json['content'] #we are perfonrmking a query i the database for the guide we are taking in the title and the content from that API request

    guide.title = title
    guide.content = content #we are now overwriting the content antitle that gpt back from the database and
    # staring a new database session to uodate those values(content and title)
    db.session.commit()#remeber this one doe not need the colon: is a ne session n the database db
    return guide_schema.jsonify(guide)

if __name__ == '__main__':
    app.run(debug=True)

