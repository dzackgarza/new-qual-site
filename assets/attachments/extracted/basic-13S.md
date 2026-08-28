## Basic Examination – Spring 2013

You may only submit solutions to 10 of the following 12 problems.
Please indicate clearly which ones you want to submit.

1. (a) Define what it means for a function on [0,1] to be Riemann integrable.

(b) Show that every monotone increasing function on [0,1] is Riemann integrable.

(c) Use part (b) to give an example of a Riemann integrable function on [0,1] which has infinitely many discontinuities.

2. The approximation from “Simpson’s Rule” for $\textstyle \int _ { a } ^ { b } f ( x ) d x$ is

$$
S _ { [ a , b ] } f = [ \frac { 2 } { 3 } f ( \frac { a + b } { 2 } ) + \frac { 1 } { 3 } ( \frac { f ( a ) + f ( b ) } { 2 } ) ] ( b - a ) .
$$

If f has continuous derivatives up to order three, prove that $\begin{array} { r } { | \int _ { a } ^ { b } f ( x ) d x - S _ { [ a , b ] } f | \leq } \end{array}$ $C ( b - a ) ^ { 4 } \operatorname* { m a x } _ { [ a , b ] } | f ^ { ( 3 ) } ( x ) |$ , where C does not depend on $f$

3. Prove that a metric space is sequentially compact if and only if it is complete and totally bounded.
   A metric space is totally bounded when for every $\epsilon > 0$ it can be covered by a finite number of balls of radius $\epsilon$.

4. Denote by $h _ { n }$ the n-th harmonic number:

$$
h _ { n } = 1 + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + . . . + { \frac { 1 } { n } }
$$

Prove that there is a limit

$$
\gamma = \operatorname* { l i m } _ { n \to \infty } ( h _ { n } - \ln n )
$$

5. Define polynomials $U _ { n } ( x ) , n = 0 , 1 , 2 , \ldots$ as follows:

$$
U _ { 1 } ( x ) = 1 , U _ { 2 } ( x ) = 2 x , U _ { n + 1 } ( x ) = 2 x U _ { n } ( x ) - U _ { n - 1 } ( x )
$$

(a) Prove that

$$
U _ { n } ( \cos \theta ) = { \frac { \sin ( ( n + 1 ) \theta ) } { \sin ( \theta ) } } .
$$

(b) Prove that the polynomials $U _ { n } ( x )$ satisfy:

$$
\int _ { - 1 } ^ { 1 } U _ { m } ( x ) U _ { n } ( x ) { \sqrt { 1 - x ^ { 2 } } } d x = { \left\{ \begin{array} { l l } { 0 \quad \text { when } m \neq n } \\ { \pi / 2 \quad \text { when } m = n } \end{array} \right. }
$$

6. (a) Prove that diagonalizable matrices are dense in the set of all $n \times n$ matrices with complex entries.

(b) Are diagonalizable matrices with real entries dense in the set of all $n \times n$ matrices with real entries?

7. (a) Define the operator norm of a real $n \times n$ matrix (considered as a linear transformation from $\mathbb { R } ^ { n }$ to $\mathbb { R } ^ { n }$ ).

(b) Denote the $n \times n$ identity matrix by I. Show that the series $\exp ( A ) = I + A + A ^ { 2 } / 2 ! + A ^ { 3 } / 3 ! + \cdots$ converges to a limit in the usual sense of convergence of matrices (convergence entry by entry).

(c) Show that the series $\ln ( I + A ) = A - A ^ { 2 } / 2 + A ^ { 3 } / 3 + \cdot \cdot \cdot + ( - 1 ) ^ { n + 1 } A ^ { n } / n + \cdot \cdot \cdot$ converges if the operator norm of A is less than one.

(d) Show that $\exp ( \ln ( I + A ) ) = I + A$ if the operator norm of A is less than 1.

8. Let T be a linear transformation from a finite-dimensional vector space V with an inner product to a finite dimensional vector space W also with an inner product (the dimension of W can be different from the dimension of V here).

(a) Define the adjoint $T ^ { * } : W \to V$

(b) Show that if matrices are written relative to orthonormal bases of V and W then the matrix of $T ^ { * }$ is the transpose of the matrix of T .

(c) Show that the kernel (null space) of $T ^ { * }$ is the orthogonal complement of the range of T .

(d) Use (b) and (c) to show that the row rank of a matrix is the same as the column rank of that same matrix.

9. Suppose A is a real $n \times n$ orthogonal matrix, i.e. the transpose of A is its inverse.

(a) Show that A is similar to a matrix which consists of $2 \times 2$ blocks down the diagonal along with some diagonal elements that are +1 or -1 with the $2 \times 2$ blocks being rotation matrices of the form

$$
\left( \begin{array} { c c } { { \cos \theta } } & { { \sin \theta } } \\ { { - \sin \theta } } & { { \cos \theta } } \end{array} \right) .
$$

(b) Use part (a) to show that if n is odd, then there is a nonzero vector v such that $A ^ { 2 } v = v$

10. Denote by G the set of real $4 \times 4$ upper triangular matrices with 1’s on the diagonal.
    Fix

$$
M = { \left( \begin{array} { l l l l } { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right) }
$$

Denote by C the set of matrices in G commuting with M .

(a) Prove that C is an affine subspace in the space $\mathbb { R } ^ { 16 }$ of all $4 \times 4$ real matrices.
S is an “affine subspace” of a vector space V if there is a vector $w \in V$ such that $S ^ { 0 } = \{ v - w : v \in S \}$ is a subspace of V . The dimension of S is defined to be the dimension of $S ^ { 0 }$

(b) Find the dimension of C.

11. Define the Fibonacci sequence $F _ { n }$ by $F _ { 0 } = 0 , F _ { 1 } = 1$ , and recursively $F _ { n } =$ $F _ { n - 1 } + F _ { n - 2 }$ for $n = 2 , 3 , 4 , . . .$

(a) Show that the limit as n goes to infinity of $F _ { n } / F _ { n - 1 }$ exists and find its value.

(b) Prove that $F _ { 2 n + 1 } F _ { 2 n - 1 } - F _ { 2 n } ^ { 2 } = 1$ for all $n \geq 1$

12. Define $\begin{array} { r } { \pi = 4 \int _ { 0 } ^ { 1 } \frac { d x } { 1 + x ^ { 2 } } } \end{array}$ . Prove that $\pi = 4 ( 1 - 1 / 3 + 1 / 5 - 1 / 7 + \cdot \cdot \cdot$ . Be careful to give a complete proof.
