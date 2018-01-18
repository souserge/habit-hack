$(() => {
    updateTable();

    $('#prev-week').on('click', function (ev) {
        weekOffset += 1;
        
        updateTable();
    });

    $('#next-week').on('click', function (ev) {
        if (weekOffset > 0) weekOffset -= 1;
        updateTable();
    });
});

let weekOffset = 0;

function updateTable() {
    let date = getDate(weekOffset*7)
    $('#month-name').text(date.getMonthName());

    console.log('jQuery works!');
    createHabitTable();

    $('.habit-cell-btn_active').on('click', function (ev) {
        ev.preventDefault();
        let habit = findHabit($(this));
        let date  = findHabitDate($(this));
        $.ajax({
            url: '/increment_counter/',
            type: 'POST',
            data: { 'habit_id': habit.id, 'datehash': dateToHash(date) },
            success: (response) => {
                console.log('database updated');
                habit.incrementRecord(date);
                drawSector(habit.percentDone(date), $(this));
            }
        });
    });
}

function createHabitTable() {
    let $table = $('#habits-table');
    $table.children().remove();
    createHabitHeader($table);

    for (let habit of habits) {
        createHabitRow(habit, $table);
    }

    $('.habit-cell-btn_active').each(function() {
        refreshSlider($(this));
    });
}

function refreshSlider($habitCell) {
    let habit = findHabit($habitCell);
    let date  = findHabitDate($habitCell);
    drawSector(habit.percentDone(date), $habitCell);
}

function findHabit($habitCell) {
    let habitId = parseInt($habitCell.closest('.habit-row').attr('value'));
    return habits.find((h) => h.id == habitId);
}

function findHabitDate($habitCell) {
    let dayOffset = parseInt($habitCell.closest('.habit-cell').attr('value'));
    return getDate(dayOffset + weekOffset*7);
}

function createHabitHeader($table) {
    let appendStr = '<tr class="days-row">';
    for (let i = 6; i >= 0; i--) {
        let d = getDate(i + weekOffset*7);
        appendStr += '<th class="day-cell">';
        appendStr += d.getDayName().substring(0, 3);
        appendStr += '</th>';
    }
    appendStr += '</tr>';
    $table.append(appendStr);
}

function createHabitRow(habit, $table) {
    let appendStr = '<tr class="habit-row" value="' + habit.id + '">';

    for (let i = 6; i >= 0; i--) {
        let date = getDate(i + weekOffset*7);

        appendStr += '<td class="habit-cell" value="' + i + '">';
        appendStr += createDayCell(habit.isActiveWeekday(date.getDay()), date.getDate());
        appendStr += '</td>';     
    }

    appendStr += '<td class="habit-cell-name"><a href="/habits/' + habit.id + '/">' + habit.name + '</a></td>';

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
    if (prec >= 1) {
        console.log("heey");
        $border.find(".habit-cell-btn-circle").first().css('background-color', '#559bb3');
        $border.find(".habit-cell-btn-circle").first().css('color', '#fff');        
        prec = 1;
    }
    
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