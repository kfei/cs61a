; CS 61A Fall 2014
; Name:
; Login:

(define (assert-equal value expression)
  (if (equal? value (eval expression))
    (print 'ok)
    (print (list 'for expression ':
                 'expected value
                 'but 'got (eval expression)))))

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))

(define (caddr s)
  (car (cddr s)))

(define (test-car-cadr)
  (assert-equal (list 3 4) '(cddr '(1 2 3 4)))
  (assert-equal 2          '(cadr '(1 2 3 4)))
  (assert-equal 3          '(caddr '(1 2 3 4))))

(test-car-cadr)

(define (sign x)
  (cond
    ((zero? x) 0)
    ((< x 0) (- 1))
    (else 1)))

(define (test-sign)
  (assert-equal -1 '(sign -42))
  (assert-equal 0  '(sign 0))
  (assert-equal 1  '(sign 42)))

(test-sign)

(define (gcd m n)
  (cond
    ((= m n) n)
    ((> m n) (gcd (- m n) n))
    ((< m n) (gcd (- n m) m))))

(define (test-gcd)
  (assert-equal 4 '(gcd 12 8))
  (assert-equal 4 '(gcd 12 16))
  (assert-equal 8 '(gcd 16 8))
  (assert-equal 6 '(gcd 24 42))
  (assert-equal 5 '(gcd 5 5)))

(test-gcd)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((zero? n) 1)
    ((even? n) (square (pow b (/ n 2))))
    ((odd? n) (* b (pow b (- n 1))))))

(define (test-pow)
  (assert-equal 1024 '(pow 2 10))
  (assert-equal 1000 '(pow 10 3))
  (assert-equal 243  '(pow 3 5)))

(test-pow)

(define (ordered? lst)
  (cond
    ((null? lst) true)
    ((null? (cdr lst)) true)
    ((< (car lst) (cadr lst)) (ordered? (cdr lst)))
    (else false)))

(define (test-ordered?)
  (assert-equal true  '(ordered? '(1 2 3 4 5)))
  (assert-equal false '(ordered? '(1 5 2 4 3))))

(test-ordered?)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
  (cond ((empty? s) false)
    ((> (car s) v) false)
    ((< (car s) v) (contains? (cdr s) v))
    (else true)))

(define odds (list 3 5 7 9))

(define (test-contains)
  (assert-equal true '(contains? odds 3))
  (assert-equal true '(contains? odds 9))
  (assert-equal false '(contains? odds 6)))

(test-contains)

(define (append s v)
  (cond ((empty? s) (list v))
    ((contains? s v) s)
    ((< v (car s)) (cons v s))
    (else (cons (car s) (append (cdr s) v)))))

(define (test-append)
  (assert-equal '(2 3 5 7 9)  '(append odds 2))
  (assert-equal '(3 5 7 9)    '(append odds 5))
  (assert-equal '(3 5 6 7 9)  '(append odds 6))
  (assert-equal '(3 5 7 9 10) '(append odds 10)))

(test-append)

(define (intersect s t)
  (cond ((or (empty? s) (empty? t)) nil)
    ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
    ((< (car s) (car t)) (intersect (cdr s) t))
    ((> (car s) (car t)) (intersect s (cdr t)))))

(define eight (list 1 2 3 4 5 6 7 8))

(define (test-intersect)
  (assert-equal '(3 5) '(intersect odds (list 2 3 4 5)))
  (assert-equal '()    '(intersect odds (list 2 4 6 8)))
  (assert-equal '(3 5 7)   '(intersect odds eight)))

(define (union s t)
  (cond ((empty? s) t)
    ((empty? t) s)
    (else (union (append s (car t)) (cdr t)))))

(define (test-union)
  (assert-equal '(2 3 4 5 7 9)       '(union odds (list 2 3 4 5)))
  (assert-equal '(2 3 4 5 6 7 8 9)   '(union odds (list 2 4 6 8)))
  (assert-equal '(1 2 3 4 5 6 7 8 9) '(union odds eight)))

(test-intersect)
(test-union)

; Binary search trees

; A data abstraction for binary trees where nil represents the empty tree
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf entry) (tree entry nil nil))

(define (in? t v)
  (cond ((empty? t) false)
    ((= v (entry t)) true)
    ((< v (entry t)) (in? (left t) v))
    (else (in? (right t) v))))

(define odd-tree (tree 3 (leaf 1)
                         (tree 7 (leaf 5)
                                 (tree 9 nil (leaf 11)))))

(define (test-in?)
  (assert-equal true  '(in? odd-tree 1))
  (assert-equal false '(in? odd-tree 2))
  (assert-equal true  '(in? odd-tree 3))
  (assert-equal false '(in? odd-tree 4))
  (assert-equal true  '(in? odd-tree 5)))

(test-in?)

(define (as-list t)
  (define (flatten t e)
    (if (empty? t)
      e
      (flatten (left t) (cons (entry t) (flatten (right t) s)))
  (flatten t nil))))

(define (test-as-list)
  (assert-equal '(5 7 9 11) '(as-list (right odd-tree)))
  (assert-equal '(1 3 5 7 9 11) '(as-list odd-tree)))

(test-as-list)
