#lang racket/base

(define (improve guess x)
  (/ (+ (/ x (* guess guess)) (* 2 guess)) 3))

(define (better-good-enought? guess prev-guess)
  (< (abs (- guess prev-guess)) 0.001))

(define (solution guess x)
  (if (better-good-enought? (improve guess x) guess)
    guess
    (solution (improve guess x)
               x)))

(require rackunit)

(check-equal? (solution 1.0 27) 3.0000005410641766)
(check-equal? (solution 1.0 8) 2.000004911675504)
