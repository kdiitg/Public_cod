// Function to parse XML and find the innermost element based on coordinates
async function findInnermostElement(x, y) {
    try {
        const response = await fetch('zzzirctc1.xml'); // Ensure this path is correct
        const text = await response.text();
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(text, 'application/xml');

        // Check if the XML document has any parsing errors
        if (xmlDoc.getElementsByTagName('parsererror').length) {
            throw new Error('Error parsing XML');
        }

        // Find all node elements
        const nodes = Array.from(xmlDoc.getElementsByTagName('node'));
        let innermostNode = null;
        let maxDepth = -1;

        // Function to recursively find the innermost node
        function findNode(node, depth) {
            const boundsStr = node.getAttribute('bounds');
            if (boundsStr) {
                const bounds = parseBounds(boundsStr);
                if (isWithinBounds(x, y, bounds)) {
                    // Check if this node is deeper than the current innermost
                    if (depth > maxDepth) {
                        maxDepth = depth;
                        innermostNode = node;
                    }
                }
            }
            for (const child of Array.from(node.children)) {
                findNode(child, depth + 1);
            }
        }

        // Start searching from the root
        findNode(xmlDoc.documentElement, 0);

        // Return the innermost node or null if no node was found
        return innermostNode ? new XMLSerializer().serializeToString(innermostNode) : null;
    } catch (error) {
        console.error('Error fetching or parsing XML:', error);
        return null;
    }
}

function parseBounds(boundsStr) {
    // Parse bounds from string format '[x1,y1][x2,y2]'
    const matches = boundsStr.match(/\[(\d+),(\d+)\]\[(\d+),(\d+)\]/);
    if (matches) {
        return [parseInt(matches[1]), parseInt(matches[2]), parseInt(matches[3]), parseInt(matches[4])];
    }
    return [];
}

function isWithinBounds(x, y, bounds) {
    // Check if the point (x, y) is within the rectangle defined by bounds
    return bounds[0] <= x && x <= bounds[2] && bounds[1] <= y && y <= bounds[3];
}

// Handle image click events
document.getElementById('main-image').addEventListener('click', async (event) => {
    const rect = event.target.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    console.log(`Clicked coordinates: (${x}, ${y})`);

    const xmlElement = await findInnermostElement(x, y);
    if (xmlElement) {
        // Display the serialized XML string
        document.getElementById('xml-details').innerText = xmlElement;
    } else {
        document.getElementById('xml-details').innerText = 'No matching XML element found.';
    }
});

// Handle copy button click
document.getElementById('copy-button').addEventListener('click', () => {
    const attributesText = document.getElementById('xml-details').innerText;
    navigator.clipboard.writeText(attributesText).then(() => {
        document.getElementById('copy-button').innerText = 'Copied';
        setTimeout(() => {
            document.getElementById('copy-button').innerText = 'Copy to Clipboard';
        }, 2000);
    });
});
