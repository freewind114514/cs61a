(define (split-at lst n)
  (define (helper n-car n-cdr n) 
    (cond 
      ((null? n-cdr) (cons n-car n-cdr))
      ((equal? n 0) (cons n-car n-cdr))
      (else (helper (append n-car (list (car n-cdr))) (cdr n-cdr) (- n 1)) ) 
    )
  )
(helper nil lst n)
)

; Tree Abstraction
; Constructs tree given label and list of branches
(define (tree label branches)
  (cons label branches))

; Returns the label of the tree
(define (label t) (car t))

; Returns the list of branches of the given tree
(define (branches t) (cdr t))

; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t) (null? (branches t)))

(define (filter-odd t) 
  (cond 
    ((null? t) nil) 
    ((even? (label t)) (tree nil (map filter-odd (branches t))))
    (else (tree (label t) (map filter-odd (branches t))))
  )
)


(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (swap expr) 
  (let 
    (
      (first (cadr expr))
      (second (caddr expr))
      (other (cdr (cddr expr)))
    )
    (if (< (eval first) (eval second))
      (cons (car expr) (cons second (cons first other)))
      expr
    )
  )
)
