export default class Car {
  constructor(brand, motor, color) {
    if (typeof brand !== 'string' || typeof motor !== 'string' || typeof color !== 'string') {
      throw new TypeError('Must be a string');
    }
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    return new this.constructor(this.brand, this.motor, this.color);
  }
}
