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

    getDateCounter(date) {
        let rec = this.history.get(dateToHash(date));
        return rec ? rec.counter : undefined;
    }
}