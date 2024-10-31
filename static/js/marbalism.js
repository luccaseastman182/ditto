document.addEventListener('DOMContentLoaded', function() {
    var graphJSON = {{ graphJSON | safe }};
    Plotly.newPlot('chart', graphJSON.data, graphJSON.layout);
});
