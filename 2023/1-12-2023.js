const fs = require('fs');  // Import the fs module

// Specify the file path (update with your actual file location)
const filePath = './2023/1-12-2023.txt'; // Update this path with your file location
let numberTotal = 0;

// Function to process each line
const processLine = (line) => {
    // Remove all letters from a to z (case-insensitive)
    let modifiedLine = line.replace(/[a-zA-Z]/g, '');
    
    // Check if the line has numeric characters to process
    if (modifiedLine.length > 0) {
        // Take the first and last characters
        const firstChar = modifiedLine[0];
        const lastChar = modifiedLine[modifiedLine.length - 1];
        
        // Parse numbers and avoid NaN errors
        const firstNum = parseInt(firstChar, 10);
        const lastNum = parseInt(lastChar, 10);
        
        // Check if both characters are valid numbers before summing them
        if (!isNaN(firstNum) && !isNaN(lastNum)) {
            let number = firstNum + lastNum;
            console.log(number);
            numberTotal += number;
        }
    }
};

// Read the file
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        // Log an error if the file cannot be read
        console.error('Error reading file:', err);
    } else {
        // Split the data into lines (assuming the file has multiple lines)
        const lines = data.split('\n');
        console.log(lines)
        
        // Iterate through each line and process it
        for (let line in lines){
            processLine(line);
        }
        
        // Print the total after processing all lines
        console.log('Total sum:', numberTotal);
    }
});
