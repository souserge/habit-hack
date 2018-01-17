(function () {
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    Date.prototype.getMonthName = function () {
        return months[this.getMonth()];
    };
    Date.prototype.getDayName = function () {
        return days[this.getDay()];
    };
})();


// Define helper functions
function pad(str, max) {
    return str.length < max ? pad('0' + str, max) : str;
}

function dateToHash(date) {
    let y = date.getYear();
    let m = date.getMonth();
    let d = date.getDate();
    return pad(y.toString(), 4) + '-' + pad(m.toString(), 2) + '-' + pad(d.toString(), 2);
}

function hashToDate(hash) {
    return new Date(hash);
}

function getDate(dayOffset, date) {
    let newDate = date!=null ? date : new Date();
    newDate.setDate(newDate.getDate() - dayOffset);
    return newDate;
}




// Define sample data
let pushups = new Habit(0, "Pushups", new Set([0, 1, 2, 3, 4, 5, 6]), 30);
let guitar = new Habit(1, "Guitar", new Set([0, 4, 5, 2]), 3);
let swimming = new Habit(2, "Swimming", new Set([1, 3, 6]), 1);
habits = [pushups, guitar, swimming];

$(() => {
    console.log('jQuery works!');
    let $table = $('#habits-table');
    createHeader($table);

    for (let habit of habits) {
        createHabitRow(habit, $table)
    }

    $('.habit-cell-btn_active').on('click', function (ev) {
        let dayOffset = parseInt($(this).closest('.habit-cell').attr('value'));
        let habitId = parseInt($(this).closest('.habit-row').attr('value'));
        let habit = habits.find((h) => h.id == habitId);

        let date = getDate(dayOffset);
        let rec = habit.incrementRecord(date);

        drawSector(rec.counter / habit.numRepeats, $(this));
    });
});

function createHeader($table, date) {
    let appendStrMonth = '<tr class="days-row">';
    let appendStr = '<tr class="days-row">';
    let monthName = date!=null ? date : new Date();
    let button = document.createElement("button");
    let button1 = document.createElement("button");
    button.textContent = "Previous Week";
    button1.textContent = "Next Week";
    appendStrMonth += '<th>' + monthName.getMonthName() + '</th>';
    button.onclick = function () {
        let newDate = getDate(7);
        monthName = newDate;
        alert("New Date:" + newDate);
    }
    button1.onclick = function () {
        let newDate = getDate(-7, monthName);
        createHeader($table, newDate);
        alert("New Date:" + newDate);
    }
    for (let i = 6; i >= 0; i--) {
        let d = getDate(i);
        appendStr += '<th class="day-cell">';
        appendStr += d.getDayName().substring(0, 3);
        appendStr += '</th>';
    }
    appendStr += '</tr>';
    $table.append(appendStrMonth);
    $table.append(appendStr);
    $table.append(button);
    $table.append(button1);
}

function createHabitRow(habit, $table) {
    let appendStr = '<tr class="habit-row" value="' + habit.id + '">';

    for (let i = 6; i >= 0; i--) {
        let date = getDate(i);

        appendStr += '<td class="habit-cell" value="' + i + '">';
        appendStr += createDayCell(habit.isActiveWeekday(date.getDay()), date.getDate());
        appendStr += '</td>';
    }

    appendStr += '<td class="habit-cell-name">' + habit.name + '</td>';

    appendStr += '</tr>';
    $table.append(appendStr);
}


function createDayCell(isActive, dayOfMonth) {
    let state = isActive ? 'active' : 'inactive';
    return '<div class="habit-cell-btn habit-cell-btn_' + state + '">'
        + '<div class="habit-cell-btn-circle habit-cell-btn-circle_' + state + '">'
        + '<span class="habit-cell-btn-text">' + dayOfMonth + '</span>'
        + '</div></div>';
}

function drawSector(prec, $border) {
    if (prec >= 1)
        prec = 1;
    let deg = prec * 360;
    if (deg <= 180) {
        $border.css('background-image', 'linear-gradient(' + (90 + deg) + 'deg, transparent 50%, #A2ECFB 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)');
    }
    else {
        $border.css('background-image', 'linear-gradient(' + (deg - 90) + 'deg, transparent 50%, #559bb3 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)');
    }

    let startDeg = 90;
    $border.css('transform', 'rotate(' + startDeg + 'deg)');
    $border.find(".habit-cell-btn-circle").first().css('transform', 'rotate(' + (-startDeg) + 'deg)');
}