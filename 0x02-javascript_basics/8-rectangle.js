#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w <= 0 || h <= 0 || !w || !h) {
    this.width;
    this.height;
  } else {
    this.width = w;
    this.height = h;
  }
};
