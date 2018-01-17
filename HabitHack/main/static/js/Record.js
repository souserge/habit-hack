class Record {
    constructor(value) {
        this.counter = value || 0;
    }

    incr() {
        this.counter++;
    }

    decr() {
        this.counter--;
    }

    set(num) {
        this.counter = num;
    }

    isLowerThan(val) {
        return this.counter < val;
    }

    isHigherThan(val) {
        return this.counter > val;
    }
}