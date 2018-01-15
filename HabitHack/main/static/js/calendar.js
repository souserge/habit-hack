// Define classes
class Habit {
    constructor(id, name, weekdays, numRepeats) {
        this.id = id;
        this.name = name;
        this.weekdays = weekdays;
        this.numRepeats = numRepeats > 0 ? numRepeats : 1;
        this.history = new Map();
    }

    incrementRecord(date) {
        let dateHash = dateToHash(date);
        let rec = this.history.get(dateHash);
        if (!rec) {
            if (this.isActiveWeekday(date.getDay())) {
                rec = new Record();
                this.history.set(dateHash, rec);
            }
        } else if (rec.isLowerThan(this.numRepeats)) {
            rec.incr();
        }
        return rec;
    }

    decrementRecord(date) {
        let rec = this.history.get(dateHash);
        if (rec && rec.isHigherThan(0)) {
            rec.decr();
        }
        return rec;
    }

    isActiveWeekday(weekday) {
        return this.weekdays.has(weekday);
    }
}

class Record {
    constructor() {
        this.counter = 1;
    }

    incr() {
        this.counter++;
    }

    decr() {
        this.counter--;
    }

    isLowerThan(val) {
        return this.counter < val;
    }

    isHigherThan(val) {
        return this.counter > val;
    }
}






// Define helper functions
function pad (str, max) {
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

function getDate(dayOffset) {
    let date = new Date();
    date.setDate(date.getDate() - dayOffset);
    return date;
}




// Define sample data
let pushups  = new Habit(0, "Pushups", new Set([0, 1, 2, 3, 4, 5, 6]), 30);
let guitar   = new Habit(1, "Guitar", new Set([0, 4, 5, 2]), 3);
let swimming = new Habit(2, "Swimming", new Set([1, 3, 6]), 1);
habits = [ pushups, guitar, swimming ];

$(() => {
    alert('It works!');
    let $table = $('#habits-table');
    createHeader($table);

    for (let habit of habits) {
        createHabitRow(habit, $table)
    }

   $('.habit-cell-btn_active').on('click', function(ev) {
        let dayOffset = parseInt($(this).closest('.habit-cell').attr('value'));
        let habitId = parseInt($(this).closest('.habit-row').attr('value'));
        let habit = habits.find((h) => h.id == habitId);
        console.log("Offset: " + dayOffset + "; habitId: " + habitId);
        let date = getDate(dayOffset);
        let rec = habit.incrementRecord(date);

        drawSector(rec.counter / habit.numRepeats, $(this));
   });
});


function createHeader($table) {
    let appendStr = '<tr class="days-row">';
    

    for (let i = 6; i >= 0; i--) {
        let d = getDate(i);
        appendStr += '<th class="day-cell">';
        appendStr += d.toDateString();
        appendStr += '</th>';
    }
    appendStr += '</tr>';
    $table.append(appendStr);
}

function createHabitRow(habit, $table) {
    let appendStr = '<tr class="habit-row" value="' + habit.id + '">';

    for (let i = 6; i >= 0; i--) {
        let dow = getDate(i).getDay();

        appendStr += '<td class="habit-cell" value="' + i + '">';
        appendStr += habit.isActiveWeekday(dow) ? createDayCell(habit.numRepeats) : createDayCell(0);
        appendStr += '</td>';
    }

    appendStr += '<td class="habit-cell-name">' + habit.name + '</td>';

    appendStr += '</tr>';
    $table.append(appendStr);
}


function createDayCell(goalNum) {
    return goalNum > 0 
            ?   '<div class="habit-cell-btn habit-cell-btn_active">'
                + '<div class="habit-cell-btn-circle habit-cell-btn-circle_active">'
                + '<span class="habit-cell-btn-day">' + goalNum + '</span>'
                + '</div></div>'
            :   '<div class="habit-cell-btn habit-cell-btn_inactive">'
                + '<div class="habit-cell-btn-circle habit-cell-btn-circle_inactive">'
                + '</div></div>';
}

function drawSector(prec, $border) {
    if (prec >= 1)
        prec = 1;
    let deg = prec*360;
    if (deg <= 180){
        $border.css('background-image','linear-gradient(' + (90+deg) + 'deg, transparent 50%, #A2ECFB 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)');
    }
    else {
        $border.css('background-image','linear-gradient(' + (deg-90) + 'deg, transparent 50%, #39B4CC 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)');
    }
    
    let startDeg = 90;
    $border.css('transform','rotate(' + startDeg + 'deg)');
    $border.find(".habit-cell-btn-circle").first().css('transform','rotate(' + (-startDeg) + 'deg)');
}