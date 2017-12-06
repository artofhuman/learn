#lang racket/base

(define (square num)
  (* num num))

(define (solution a b c)
  (if (> a b)
    (if (> b c)
      (+ (square a) (square b))
      (+ (square a) (square c)))
    (+ (square b) (square c)))
)

(require rackunit)

(check-equal? (solution 1 2 3) 13)
(check-equal? (solution 4 1 2) 20)
(check-equal? (solution 1 1 2) 5)
