# Fall 2023 Applied Algebra Qualifying Exam: Part A

# 1:00pm–4:00pm (PDT) Thursday September 7th

• Write your name and student PID at the top right corner of each page of your submission.

• Do all four problems. Show your work.

• This part of the exam will represent 40% of the total score.

• Notation:

$\mathcal { M } _ { m , n }$ denotes the set of $m \times n$ matrices with complex components.

$\mathcal { M } _ { n }$ denotes the set $\mathcal { M } _ { m , n }$ with $m = n$

– Cn is the set of column vectors with n complex components.

$x ^ { \mathrm { T } }$ is the transpose of a vector or matrix x.

$x ^ { \mathrm { H } }$ is the Hermitian transpose of a vector or matrix x.

– eig(A) is the set of eigenvalues of the matrix A (counting multiplicities).

– Re(α) is the real part of the complex scalar α.

– Im(α) is the imaginary part of the complex scalar α.

## Question 1.

(a) State, but do not prove, the Schur decomposition theorem for a matrix $A \in M _ { n }$

(b) Prove that for A, $B \in { \mathcal { M } } _ { n } , \operatorname { i f } x ^ { \mathrm { H } } A x = x ^ { \mathrm { H } }$ Bx for all $x \in \mathbb { C } ^ { n }$ , then $A = B$ . Give an example for which $x ^ { \mathrm { T } } A x = x ^ { \mathrm { T } } B x$ for all $x \in \mathbb { C } ^ { n }$ but $A \neq B$

## Question 2.

(a) Prove that every $A \in { \mathcal { M } } _ { n }$ may be written uniquely as $A = S + i T$ , where S and T are Hermitian.

(b) For any $A \in { \mathcal { M } } _ { n }$ , consider the unique expansion $A = S + i T$ , where S and T are Hermitian. Prove that for any $\lambda \in \mathrm { e i g } ( A )$ , it holds that

$$
\lambda _ { n } ( S ) \leq \operatorname { R e } ( \lambda ) \leq \lambda _ { 1 } ( S ) \quad { \mathrm { a n d } } \quad \lambda _ { n } ( T ) \leq \operatorname { I m } ( \lambda ) \leq \lambda _ { 1 } ( T ) ,
$$

where $\lambda _ { 1 } ( C )$ and $\lambda _ { n } ( C )$ denote the largest and smallest eigenvalues of a Hermitian matrix $C \in \mathcal { M } _ { n }$

Question 3. Consider any $A \in \mathcal { M } _ { m , n }$

(a) Define |A|, the modulus of A. Prove that the eigenvalues of $| A |$ are the singular values of A.

(b) Prove that if $m = n$ , then $| A |$ and $| A ^ { \mathrm { H } } |$ are similar.

## Question 4.

(a) Consider any Hermitian $A \in { \mathcal { M } } _ { n }$ with eigenvalues ordered so that $\lambda _ { n } ( A ) \leq$ $\dotsb \leq \lambda _ { 2 } ( A ) \leq \lambda _ { 1 } ( A )$ . Prove that

$$
\lambda _ { n } ( A ) \leq { \frac { x ^ { \mathrm { H } } A x } { x ^ { \mathrm { H } } x } } \leq \lambda _ { 1 } ( A ) ,
$$

for all nonzero $x \in \mathbb { C } ^ { n }$

(b) Suppose that $D \in \mathcal { M } _ { n }$ with $D = \mathrm { d i a g } ( d _ { 1 } , d _ { 2 } , \ldots , d _ { n } )$ . Prove that for all $1 \leq$ $p \leq \infty$ the p-norm of D is given by $\lVert D \rVert _ { p } = \operatorname* { m a x } _ { 1 \leq i \leq n } \left| d _ { i } \right|$

(c) Given $a \in \mathbb { C } ^ { n }$ , find $\| A \| _ { 2 }$ for the matrices

$$
A = a a ^ { \mathrm { H } } \quad { \mathrm { a n d } } \quad A = \left( { \begin{array} { c c } { 0 } & { a ^ { \mathrm { H } } } \\ { a } & { 0 } \end{array} } \right) .
$$

(Show your work. Simply writing down the answer will not be sufficient.)