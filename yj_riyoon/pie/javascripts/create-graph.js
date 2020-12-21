/*
 * Parse the data and create a graph with the data.
 */
function parseData(createGraph) {
	Papa.parse("../data/complete_data.csv", {
		download: true,
		complete: function(results) {
			// console.log(results.data);
			createGraph(results.data);
		}
	});
}

function createGraph(data) {
	var country = ["Countries"];

	for (var i = 1; i < data.length; i++) {
		country.push(data[i][3]);
	}

	console.log(country);

	var chart = c3.generate({
		bindto: '#chart',
    data: {
        columns: [
            ['data1', 10],
            ['data2', 120],
        ],
        type : 'pie',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    }
})}
parseData(createGraph);

