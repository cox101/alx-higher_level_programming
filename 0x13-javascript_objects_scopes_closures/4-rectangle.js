class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
            return {};
        }
        this.width = w;
        this.height = h;
    }

    print() {
        if (Object.keys(this).length === 0) {
            return;
        }
        const row = 'X'.repeat(this.width);
        for (let i = 0; i < this.height; i++) {
            console.log(row);
        }
    }

    rotate() {
        if (Object.keys(this).length === 0) {
            return;
        }
        const temp = this.width;
        this.width = this.height;
        this.height = temp;
    }

    double() {
        if (Object.keys(this).length === 0) {
            return;
        }
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;

