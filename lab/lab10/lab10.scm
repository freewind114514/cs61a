(define (over-or-under num1 num2) ( cond ((< num1 num2)-1) ((= num1 num2)0) (else 1)  ) )

(define (make-adder num) (lambda(inc)(+ num inc)))

(define (composed f g) (lambda(x)(f (g x))))

(define (square n) (* n n))

(define (pow base exp) 
(
cond ((= exp 1)base)
((even? exp)(square (pow base (quotient exp 2))))

(else (*(square (pow base (quotient exp 2))) base))
))
