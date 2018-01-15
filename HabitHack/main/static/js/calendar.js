// Define classes
class Habit {
    constructor(name, weekdays, numRepeats) {
        this.name = name;
        this.weekdays = weekdays;
        this.numRepeats = numRepeats > 0 ? numRepeats : 1;
        this.history = new Map();
    }

    incrementRecord(dateHash) {
        let rec = this.history.get(dateHash);
        if (!rec && this.isActiveWeekday(hashToDate(dateHash).getDay())) {
            this.history.set(new Record());
        } else if (rec.isLowerThan(this.numRepeats)) {
            rec.incr();
        }
    }

    decrementRecord(date) {
        let rec = this.history.get(dateHash);
        if (rec && rec.isHigherThan(0)) {
            rec.decr();
        }
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





// Define sample data
let pushups  = new Habit("Pushups", new Set([0, 1, 2, 3, 4, 5, 6]), 30);
let guitar   = new Habit("Guitar", new Set([0, 4, 5, 2]), 3);
let swimming = new Habit("Swimming", new Set([1, 3, 6]), 1);
habits = [ pushups, guitar, swimming ];

$(() => {
    alert('It works!');
    let $table = $('#habits-table');
    for (let habit of habits) {
        let appendStr = '<tr class="habit-row">';
        appendStr += '<td class="habit-cell-name">' + habit.name + '</td>';

        for (let i = 0; i < 7; i++) {
            appendStr += '<td class="habit-cell">';
            appendStr += habit.isActiveWeekday(i) ? createDayCell(habit.numRepeats) : createDayCell(0);
            appendStr += '</td>';
        }

        appendStr += '</tr>';
        $table.append(appendStr);
   }

   $('.habit-cell-btn').on('click', () => {
        // percent += 100/times;
        // drawSector(percent);
   });
});


function createDayCell(goalNum) {
    return '<div class="habit-cell-btn">'
            + '<div class="habit-cell-btn-circle">'
            + '<span class="habit-cell-btn-day">' + goalNum + '</span>'
            + '</div>'
            + '</div>';
}

function drawSector(prec) {
    let activeBorder = $("#activeBorder");
    if (prec >= 1)
        prec = 1;
    let deg = prec*360;
    if (deg <= 180){
        activeBorder.css('background-image','linear-gradient(' + (90+deg) + 'deg, transparent 50%, #A2ECFB 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)');
    }
    else {
        activeBorder.css('background-image','linear-gradient(' + (deg-90) + 'deg, transparent 50%, #39B4CC 50%),linear-gradient(90deg, #A2ECFB 50%, transparent 50%)');
    }
    
    let startDeg = 90;
    activeBorder.css('transform','rotate(' + startDeg + 'deg)');
    $("#circle").css('transform','rotate(' + (-startDeg) + 'deg)');
}