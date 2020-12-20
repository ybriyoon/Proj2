/*
 * Parse the data and create a graph with the data.
 */
function parseData(createGraph) {
	Papa.parse("../data/complete_data.csv", {
		complete: function(results) {
			console.log("Finished:", results.data);
		}
	});
}

function createGraph(data) {
	
}
