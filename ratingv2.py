from flask import Flask, request, jsonify
app = Flask(__name__)
import requests
import json


rating_service_v2 = { 'facility1': { 'd1' : { "PhysicianID":"1A" ,"Physician":"Doctor John",   "Stars":"**" , "reviews":['good','good','good','excellent','neutral']},
              'd2' : { "PhysicianID":"2A","Physician":"Doctor Radhika", "Stars":"****" , "reviews":['good','excellent']}},
               'facility2': { 'd1' : { "PhysicianID":"3A" ,"Physician":"Doctor Marry", "Stars":"**" , "reviews":['bad','bad','good','excellent','neutral']},
              'd2' : { "PhysicianID":"4A","Physician":"Doctor Matt","Stars":"*" , "reviews":['Bad','V Bad']}},
             }


def call_rating_service(facilityID, docID):
    dict_names = rating_service_v2[facilityID]
    docs = []
    for p_id, p_info in dict_names.items():
        for key in p_info:
            if p_info[key] == docID:
                return (p_info)




    


@app.route('/', methods=['POST'])
def add_message():
    con = request.json
    content = json.loads(con)
    res = call_rating_service(content["facilityID"],content["docID"])
    print(res)
    return json.dumps(res, indent = 2)




if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=6002)