const fs = require('fs');
const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://juanpgtzg:ljIgvpQJzlYZJwfF@webdata.w6ffrza.mongodb.net/?retryWrites=true&w=majority";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
    serverApi: {
        version: ServerApiVersion.v1,
        strict: true,
        deprecationErrors: true,
    }
});

// Database and collection names
const dbName = 'machine_learning';
const collectionName = 'json_files';

// Read the JSON file
const jsonData = fs.readFileSync('mongo/coordinates.json');
const data = JSON.parse(jsonData);

/* Receives all data from the server and outputs it into a JSON file */
async function downloadJSON() {
    try {
        await client.connect();

        const db = client.db(dbName);
        const collection = db.collection(collectionName);

        const documents = await collection.find({}, { projection: { x: 1, y: 1, timestamps: 1 } }).toArray();

        // Convert documents to a JSON string
        const jsonContent = JSON.stringify(documents, null, 2);

        // Define the output JSON file path
        const outputFilePath = 'output.json';

        // Write documents to the JSON file
        fs.writeFileSync(outputFilePath, jsonContent);

        console.log(`Documents exported to ${outputFilePath}`);
    } catch (err) {
        console.error(err);
    } finally {
        // Close the MongoDB connection
        await client.close();
    }
}

function download() {
    downloadJSON().catch(console.error);
}

download();