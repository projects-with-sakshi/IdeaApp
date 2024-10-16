from flask import Flask,request

app = Flask(__name__)

# create the idea repository where ideas will be stored
ideas={
    1:{
        "id":1,
        "idea_name":"ONDC",
        "idea_description":"Details about ONDC",
        "idea_author":"Adeeb"
    },
    2:{
        "id":2,
        "idea_name":"Save Soil",
        "idea_description":"Details about Saving Soil",
        "idea_author":"Ankit Sharma"
    }
}

'''
create an RESTful endpoint for fetching all the ideas
'''
@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    # logic to fetch all the ideas
    return ideas

'''
create a restful end point for creating a new idea
'''
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    # logic to create a new ideas
    try:
        # first read the request body
        request_body = request.get_json()  # (request) represent the body passed by user


        # check if the idea id is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return "idea with the same id already present",400    # 400 is HTTP status code or Bad request 
        
        #Insert the passed idea in the ideas dictionary
        ideas[request_body["id"]] = request_body
        
        # return the response saying idea got saved
        return "idea created and saved successfully",201
    except KeyError:
        return "id is missing",400
    except:
        return "some internal server error",500

if __name__=='__main__':
    app.run(port=8080)