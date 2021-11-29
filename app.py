from flask import Flask, request, jsonify
app = Flask(__name__)
import json
import requests

# dict_names = { 'facility1': { 'd1' : { "PhysicianID":"1A" ,"Physician":"Doctor John", "Available_slots" : ['11 am -11:30 am','10 am -10:30 am','10 am -10:30 am','10 am -10:30 am'] , "Stars":"**" , "reviews":['good','good','good','excellent','neutral']},
#               'd2' : { "PhysicianID":"2A","Physician":"Doctor Radhika","Available_slots" : ['9 am -9:30 am','10 am -10:30 am'] , "Stars":"****" , "reviews":['good','excellent']}},
#                'facility2': { 'd1' : { "PhysicianID":"3A" ,"Physician":"Doctor Marry", "Available_slots" : ['06 am -06:30 am','11 am -11:30 am','10 am -10:30 am','10 am -10:30 am','10 am -10:30 am'] , "Stars":"**" , "reviews":['bad','bad','good','excellent','neutral']},
#               'd2' : { "PhysicianID":"4A","Physician":"Doctor Matt","Available_slots" : ['9 am -9:30 am','10 am -10:30 am'] , "Stars":"*" , "reviews":['Bad','V Bad']}},
# }

provider_service = { 'facility1': { 'd1' : { "PhysicianID":"1A" ,"Physician":"Doctor John", "Available_slots" : ['11 am -11:30 am','10 am -10:30 am','10 am -10:30 am','10 am -10:30 am'] },
              'd2' : { "PhysicianID":"2A","Physician":"Doctor Radhika","Available_slots" : ['9 am -9:30 am','10 am -10:30 am']}},
               'facility2': { 'd1' : { "PhysicianID":"3A" ,"Physician":"Doctor Marry", "Available_slots" : ['06 am -06:30 am','11 am -11:30 am','10 am -10:30 am','10 am -10:30 am','10 am -10:30 am'] },
              'd2' : { "PhysicianID":"4A","Physician":"Doctor Matt","Available_slots" : ['9 am -9:30 am','10 am -10:30 am'] }},
             }

# rating_service_v1 = { 'facility1': { 'd1' : { "PhysicianID":"1A" ,"Physician":"Doctor John",   "Stars":"" , "reviews":['good','good','good','excellent','neutral']},
#               'd2' : { "PhysicianID":"2A","Physician":"Doctor Radhika", "Stars":"" , "reviews":['good','excellent']}},
#                'facility2': { 'd1' : { "PhysicianID":"3A" ,"Physician":"Doctor Marry", "Stars":"" , "reviews":['bad','bad','good','excellent','neutral']},
#               'd2' : { "PhysicianID":"4A","Physician":"Doctor Matt","Stars":"" , "reviews":['Bad','V Bad']}},
#              }

# rating_service_v2 = { 'facility1': { 'd1' : { "PhysicianID":"1A" ,"Physician":"Doctor John",   "Stars":"**" , "reviews":['good','good','good','excellent','neutral']},
#               'd2' : { "PhysicianID":"2A","Physician":"Doctor Radhika", "Stars":"****" , "reviews":['good','excellent']}},
#                'facility2': { 'd1' : { "PhysicianID":"3A" ,"Physician":"Doctor Marry", "Stars":"**" , "reviews":['bad','bad','good','excellent','neutral']},
#               'd2' : { "PhysicianID":"4A","Physician":"Doctor Matt","Stars":"*" , "reviews":['Bad','V Bad']}},
#              }

# rating_service_v3 = { 'facility1': { 'd1' : { "PhysicianID":"1A" ,"Physician":"Doctor John",   "Stars":"**" , "Flag":"Flag for accepting new patients","reviews":['good','good','good','excellent','neutral']},
#               'd2' : { "PhysicianID":"2A","Physician":"Doctor Radhika", "Stars":"****" , "Flag":"Flag for accepting new patients" , "reviews":['good','excellent']}},
#                'facility2': { 'd1' : { "PhysicianID":"3A" ,"Physician":"Doctor Marry" , "Flag":"Flag for accepting new patients", "Stars":"**" , "reviews":['bad','bad','good','excellent','neutral']},
#               'd2' : { "PhysicianID":"4A","Physician":"Doctor Matt","Stars":"*" , "Flag":"Flag for accepting new patients" , "reviews":['Bad','V Bad']}},
#              }

def call_rating_service(obj, facilityID, docID):
    dict_names = obj[facilityID]
    docs = []
    for p_id, p_info in dict_names.items():
        for key in p_info:
            if p_info[key] == docID:
                return (p_info)




def get_data(obj,facilityID,docID):
    dict_names = obj[facilityID]
    docs = []
    for p_id, p_info in dict_names.items():

        for key in p_info:
            temp={}
            temp1={}
            temp['label'] = p_info['Physician']
            temp['value'] = p_info['PhysicianID']

            if p_info[key] == docID:

                #rating_results = call_rating_service(rating_service_v1,facilityID,docID)
                # Serializing json  
                json_object = json.dumps({"facilityID":facilityID , "docID":docID }, indent = 4) 
                
                res = requests.post('http://localhost:6003', json=json_object)
                rating_results = (res.json())

                temp1['PhysicianID'] = p_info['PhysicianID']
                temp1['Physician'] = p_info['Physician']
                temp1['Available_slots'] = p_info['Available_slots']
                temp1['Stars'] = rating_results['Stars']
                temp1['reviews'] = rating_results['reviews']
                
                if "Flag" in rating_results:
                    temp1['Flag'] = rating_results['Flag']
                return (temp1)

        docs.append(temp)   
    return docs
    


@app.route('/', methods=['POST'])
def add_message():
    print("YAHAN: \n\n\n\n")
    con = request.json
    content = json.loads(con)
    res = get_data(provider_service,content["facilityID"],content["docID"])
    print('\n\n\n\n')
    
    print(res)
    return json.dumps(res, indent = 2)



@app.route('/test')
def testing():
    return "API Working"


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=6000)