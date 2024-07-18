(define (cddr s) (cdr (cdr s)))

(define (cadr s) ( car(cdr s) ))

(define (caddr s) ( car(cddr s) ))

(define (ascending? lst) ( if (not(null? (cdr lst)))
    (and (not(>(car lst)(cadr lst))) (ascending? (cdr lst)) )
    #t ))

(define (interleave lst1 lst2) (cond
((and(null? lst1)(null? lst2)) nil)
((null? lst1) lst2)
((null? lst2) lst1)
(else  (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)) ))  )
))

(define (my-filter func lst) (cond
( (null?  lst) nil)
((func (car lst)) (cons  (car lst)  (my-filter func (cdr lst))) )
(else (my-filter func (cdr lst)) )
))

(define (no-repeats lst) (if (null? lst) nil
(cons (car lst) (no-repeats (my-filter  (lambda (n) (not(= n (car lst))))   lst  )  ))
)) 
