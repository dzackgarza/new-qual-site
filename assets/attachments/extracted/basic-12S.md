# BASIC QUAL WINTER 2012

Instructions: Work any 10 problems and therefore at least 4 from Problems 1–6 and at least 4 from Problems 7–12. All problems are worth ten points.
You need to indicate clearly which are the 10 problems you want us to grade.
Full credit on one problem will be better than partial credit on two problems.

Problem 1. Let Ω denote the set of all closed subsets of [0, 1] and let $\rho \colon \Omega \times \Omega \to [ 0 , 1 ]$ be defined by

$$
\rho ( A , B ) : = \operatorname* { m a x } \Bigl \{ \operatorname* { s u p } _ { x \in A } \operatorname* { i n f } _ { y \in B } | x - y | , \operatorname* { s u p } _ { y \in B } \operatorname* { i n f } _ { x \in A } | x - y | \Bigr \}
$$

Show that $( \Omega , \rho )$ is a metric space.

Problem 2. Recall that $f \colon [ a , b ] \to \mathbb { R }$ is convex if for all $x , y \in [ a , b ]$ and $\alpha \in [ 0 , 1 ]$ , $f ( \alpha x + ( 1 - \alpha ) y ) \le \alpha f ( x ) + ( 1 - \alpha ) f ( y )$ . Let $f _ { n } \colon [ a , b ] \to \mathbb { R }$ be convex functions and suppose that $f ( x ) : = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ exists at all $x \in [ a , b ]$ and is continuous on $[ a , b ]$ . Prove that $f _ { n } \to f$ uniformly.

Problem 3. Prove the Bolzano Weierstrass theorem in the following form: Each sequence $( a _ { n } ) _ { n \in \mathbb { N } }$ of numbers $a _ { n }$ in the closed interval [0, 1] has a convergent subsequence.

Problem 4. For a sequence $\left\{ a _ { n } \right\}$ of non-negative numbers, let $\textstyle s _ { n } : = \sum _ { k = 1 } ^ { n } a _ { k }$ and suppose that $s _ { n }$ tends to a number $s \in \mathbb { R }$ in the Cesàro sense:

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { s _ { 1 } + \cdots + s _ { n } } { n } } = s .
$$

Show that $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k }$ exists and equals s.

Problem 5. Prove that there is a unique continuous function $y \colon [ 0 , 1 ] \to \mathbb { R }$ solving the equation

$$
y ( x ) = e ^ { x } + { \frac { y ( x ^ { 2 } ) } { 2 } } , \qquad x \in [ 0 , 1 ]
$$

Problem 6. Let $\gamma$ be a smooth curve from (1, 0) to (1, 0) in $\mathbb { R } ^ { 2 } \setminus \{ ( 0 , 0 ) \}$ winding once around the origin in the clockwise direction.
Compute the integral

$$
I ( \gamma ) : = \int _ { \gamma } \frac { y \mathrm { d } x - x \mathrm { d } y } { x ^ { 2 } + y ^ { 2 } } .
$$

Problem 7. Let F be the finite field of p elements, let V be a n-dimensional vector space over F , and let $0 \leq k \leq n$ . Compute the number of invertible linear maps $V \to V$ . It is acceptable if your solution is a lengthy algebraic expression, as long as you explain why it is correct.

Problem 8. Let A be a n×n complex matrix.
Prove that there are two sequences of matrices $\{ B _ { i } \}$ and $\{ L _ { i } \}$ , such that $L _ { i }$ are diagonal with distinct eigenvalues, and $B _ { i } L _ { i } B _ { i } ^ { - 1 } \to A$ as $i \to \infty$ Here by convergence of matrices we mean convergence in all entries.

Problem 9. Let $a _ { 1 } = 1 , a _ { 2 } = 4 , a _ { n + 2 } = 4 a _ { n + 1 } - 3 a _ { n }$ for all $n \geq 1$ . Find a $2 \times 2$ matrix A such that

$$
A ^ { n } \cdot { \binom { 1 } { 0 } } = { \binom { a _ { n + 1 } } { a _ { n } } }
$$

for all $n \geq 1$ . Compute the eigenvalues of A and use them to determine the limit

$$
\operatorname* { l i m } _ { n \to \infty } ( a _ { n } ) ^ { 1 / n } .
$$

Problem 10. Let A be a complex $n \times n$ matrix.
State and prove under which conditions on A, the following identity holds:

$$
\operatorname* { d e t } ( { \mathbf { e } } ^ { A } ) = \exp ( \operatorname { t r } A ) .
$$

Here the matrix exponentiation is defined via the Taylor series:

$$
\mathbf { e } ^ { A } = 1 + A + A ^ { 2 } / 2 ! + A ^ { 3 } / 3 ! + . . .
$$

You can assume known that this sum converges (entrywise) for all complex matrices A.

Problem 11. (a) Find a polynomial $P ( x )$ of degree 2, such that $P ( A ) = 0$ , for

$$
A = { \binom { 1 } { 4 } } \ 3 )
$$

(b) Prove that such $P ( x )$ is unique, up to multiplication by a constant.

Problem 12. Recall that the quadratic forms $Q _ { 1 } ( x , y )$ and $Q _ { 2 } ( x ^ { \prime } , y ^ { \prime } )$ are said to be equivalent if they are related by a non-singular change of coordinates $( x , y ) \mapsto ( x ^ { \prime } , y ^ { \prime } )$ . Decide whether $Q _ { 1 } = x y$ and $Q _ { 2 } = x ^ { 2 } + y ^ { 2 }$ are equivalent over C and whether they are equivalent over R. If not, give a proof.
If yes, find the matrix for change of coordinates.
