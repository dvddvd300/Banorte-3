function mostVisitedCoordinates(data) {
    // Create a map to store the number of times each coordinate has been visited.
    const visitedCoordinates = new Map();

    // Iterate over the data.
    for (const coordinate of data) {
        // Get the x and y coordinates.
        const x = coordinate.x;
        const y = coordinate.y;

        // Increment the count for the coordinate in the map.
        visitedCoordinates.set(x, visitedCoordinates.get(x) || 0) + 1;
    }

    // Get the coordinates with the highest counts.
    const mostVisitedCoordinates = Array.from(visitedCoordinates.entries())
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);

    // Return the most visited coordinates.
    return mostVisitedCoordinates;
}
const fs = require('fs');
const jsonData = fs.readFileSync('machinejs/coordinates.json');
const data = JSON.parse(jsonData);

// Extract x and y coordinates from the JSON data
const coordinates = data.map(entry => [entry.x, entry.y]);


const most = mostVisitedCoordinates(coordinates);

console.log(most);