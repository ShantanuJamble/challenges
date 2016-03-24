function start_countdown(milliseconds) {
    alert(new Date(milliseconds) + 'in start');
    $("#countdown").countdown({date: new Date(milliseconds)},
        function () {
            alert("Done");
        });
}

//Unix Timestramp