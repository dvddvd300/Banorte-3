import os

os.system('node mongo/mongo_connection.js')
""" 

uri = "mongodb+srv://juanpgtzg:ljIgvpQJzlYZJwfF@webdata.w6ffrza.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))


while True:
    documents = client.get_database("machine_learning").get_collection("json_files").find()

    # Convert documents to a list
    document_list = list(documents)

    # Save documents to a JSON file
    with open("output.json", "w") as file:
        json.dump(document_list, file)

    time.sleep(10)
client.close() """