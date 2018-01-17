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

function pad(str, max) {
    return str.length < max ? pad('0' + str, max) : str;
}

function dateToHash(date) {
    let y = date.getUTCFullYear();
    let m = date.getUTCMonth() + 1;
    let d = date.getUTCDate();
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