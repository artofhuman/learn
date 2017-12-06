#lang racket/base

(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

(define (square num)
  (* num num))

(define (sqrt-iter guess x)
  (if (good-enought? guess x)
    guess
    (sqrt-iter (improve guess x)
               x)))

(define (good-enought? guess x)
  (< (abs (- (square guess) x)) 0.001))

;---- solution
(define (better-good-enought? guess prev-guess)
  (< (abs (- guess prev-guess)) 0.001))

(define (better-sqrt-iter guess x)
  (if (better-good-enought? (improve guess x) guess)
    guess
    (better-sqrt-iter (improve guess x)
               x)))

(require rackunit)

(check-equal? (sqrt-iter 1.0 9) 3.00009155413138)
(check-equal? (better-sqrt-iter 1.0 9) 3.00009155413138)
