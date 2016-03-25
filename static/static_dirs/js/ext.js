function start_countdown(milliseconds,quiz) {
    alert(new Date(milliseconds) + 'in start');
    $("#countdown").countdown({date: new Date(milliseconds)},
        function () {
            alert(quiz);
            window.location.replace("/end/"+quiz)
        });
}

//Unix Timestramp