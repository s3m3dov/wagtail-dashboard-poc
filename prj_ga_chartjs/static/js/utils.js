function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function createListOfRandomColors(length) {
    colorList = [];
    for (var i = 0; i < length; i++) {
        colorList.push(getRandomColor())
    }
    return colorList;
}

function isItPieOrDoughnut(type) {
    if (type === 'pie' || type === 'doughnut') {
        return true;
    } else {
        return false;
    }
}

function drawSegmentValues() {
    for(var i=0; i < myChart.segments.length; i++) {
        // Default properties for text (size is scaled)
        ctx.fillStyle="#212121";
        var textSize = canvas.width / 10;
        ctx.font = textSize + "px Verdana";

        // Get needed variables
        var value = myChart.segments[i].value;
        var startAngle = myChart.segments[i].startAngle;
        var endAngle = myChart.segments[i].endAngle;
        var middleAngle = startAngle + ((endAngle - startAngle)/2);

        // Compute text location
        var posX = (radius/2) * Math.cos(middleAngle) + midX;
        var posY = (radius/2) * Math.sin(middleAngle) + midY;

        // Text offside to middle of text
        var w_offset = ctx.measureText(value).width/2;
        var h_offset = textSize/4;

        ctx.fillText(value, posX - w_offset, posY + h_offset);
    }
}