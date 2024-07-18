(define (curry-cook formals body) 'YOUR-CODE-HERE)

(define (curry-consume curry args)
  'YOUR-CODE-HERE)

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons `cond
        (map (lambda (option)
               (cons `(equal? ,(car (cdr switch-expr)) ,(car option))  (cdr option)))
             (car (cdr (cdr switch-expr))))))
