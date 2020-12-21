/*
 * Parse the data and create a graph with the data.
 */
function parseData(createGraph) {
	Papa.parse("static/data/top20countries.csv", {
		download: true,
		complete: function(results) {
			// console.log(results.data[1][1]);
			createGraph(results.data);
		}
	});
}

function createGraph(data) {
	var country = ["Countries"];
	var count = ["Count"];

	for (var i = 1; i < 6; i++) {
		country.push(data[i][1]);
		count.push(data[i][2])
	}

	console.log(country);
	console.log(count);
	
	var chart = c3.generate({
		bindto: '#chart',
	title:{
		text: "Top 5 Countries"
	},	
    data: {
        columns: [
			[country[1],count[1]],
			[country[2],count[2]],
			[country[3],count[3]],
			[country[4],count[4]],
			[country[5],count[5]],
    
        ],
        type : 'pie',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    }
})}
parseData(createGraph);

