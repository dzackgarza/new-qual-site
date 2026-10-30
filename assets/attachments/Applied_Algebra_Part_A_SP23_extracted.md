# Spring 2023 Applied Algebra Qualifying Exam: Part A

# 1:00pm–4:00pm (PDT) Tuesday May 23rd

• Write your name and student PID at the top right corner of each page of your submission.

• Do all four problems. Show your work.

• This part of the exam will represent 40% of the total score.

• Notation:

$\mathcal { M } _ { m , n }$ denotes the set of $m \times n$ matrices with complex components.

$\mathcal { M } _ { n }$ denotes the set $\mathcal { M } _ { m , n }$ with $m = n$

$- \ \mathbb { C } ^ { n }$ is the set of column vectors with n complex components.

$- \mathbf { \nabla } x ^ { \mathrm { H } }$ is the Hermitian transpose of a vector or matrix x.

## Question 1.

(a) State, but do not prove, the Schur decomposition theorem.

(b) Let $( \lambda , x )$ be a simple eigenpair of $A \in \mathcal { M } _ { n }$ with $x ^ { \mathrm { H } } x = 1$

(i) Prove that there exists a nonsingular matrix $( \boldsymbol { x } \ \boldsymbol { X } )$ with inverse $( \boldsymbol { y } \ Y ) ^ { \mathrm { H } }$ such that

$$
\left( { \begin{array} { c } { y ^ { \mathrm { H } } } \\ { Y ^ { \mathrm { H } } } \end{array} } \right) A \left( x \quad X \right) = \left( { \begin{array} { c c } { \lambda } & { 0 } \\ { 0 } & { M } \end{array} } \right) , \ \mathrm { w i t h } \ M \in { \mathcal { M } } _ { n - 1 } .
$$

(ii) Hence prove that the angle θ between x and y satisfies sec $\theta = \| y \| _ { 2 }$

Question 2. Consider a Hermitian matrix $A \in \mathcal { M } _ { n }$

(a) Show that the eigenvalues of A are real.

(b) Assume that the eigenvalues of A are ordered so that $\lambda _ { n } \leq \lambda _ { n - 1 } \leq \cdot \cdot \cdot \leq \lambda _ { 2 } \leq$ $\lambda _ { 1 }$ . State, but do not prove, the Courant-Fischer theorem.

(c) Prove that

$$
\lambda _ { n } = \operatorname* { m i n } _ { x ^ { \mathrm { H } } x = 1 } \ x ^ { \mathrm { H } } A x , \quad { \mathrm { a n d } } \quad \lambda _ { 1 } = \operatorname* { m a x } _ { x ^ { \mathrm { H } } x = 1 } \ x ^ { \mathrm { H } } A x .
$$

## Question 3.

(a) Given a vector norm $\| \cdot \|$ , define the matrix norm subordinate to $\| \cdot \|$ . Prove that every subordinate matrix norm is consistent.

(b) Given $A \in \mathcal { M } _ { m , n }$ , let $\| A \|$ denote the matrix norm subordinate to the vector norm ∥ · ∥. Prove that $\| x y ^ { \mathrm { H } } \| = \| x \| \| y \| _ { D }$ for all $x , y \in \mathbb { C } ^ { n }$ , where $\| y \| _ { D }$ denotes the vector norm dual to $\| \cdot \|$

(c) Given $A \in \mathcal { M } _ { m , n } ,$ , prove that $\| A x \| _ { 2 } \leq \| A \| _ { F } \| x \| _ { 2 }$ for all $x \in \mathbb { C } ^ { n }$

(d) Find $\| x y ^ { \mathrm { H } } \|$ for the Frobenius norm.

## Question 4.

(a) State, but do not prove, the singular-value decomposition theorem.

(b) For a given $A \in \mathcal { M } _ { m , n }$ , prove that

$$
\sigma _ { 1 } ( A ) = \operatorname* { m a x } _ { \boldsymbol { x } , \boldsymbol { y } \neq \boldsymbol { 0 } } { \frac { | \boldsymbol { y } ^ { \mathrm { H } } \boldsymbol { A } \boldsymbol { x } | } { \| \boldsymbol { y } \| _ { 2 } \| \boldsymbol { x } \| _ { 2 } } } ,
$$

where $\sigma _ { 1 } ( A )$ is the largest singular value of A.

(c) For any $A \in { \mathcal { M } } _ { n }$ , define (i) the field of values ${ \mathcal { F } } ( A ) ; ( { \mathrm { i i } } )$ the spectral radius $\rho ( A )$ ; and (iii) the numerical radius $\omega ( A )$ . Prove that $\rho ( A ) \leq \omega ( A ) \leq \sigma _ { 1 } ( A )$