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