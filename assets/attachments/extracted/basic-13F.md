## Basic Exam, Fall 2013

Instructions: Write your UCLA student number on each page of your solutions. Do not write your name. Work 10 of the 12 problems, at least 4 of the first 6 and at least 4 of the last 6, and indicate here which 10 problems you want to have graded: (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12). Each problem is worth 10 points, but different parts of a problem may have different values.

1. When $\left\{ a _ { n } \right\}$ is a sequence of positive real numbers, $a _ { n } > 0$ , define $P _ { n } = \Pi _ { j = 1 } ^ { n } \big ( 1 + a _ { j } \big )$ . Prove that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } P _ { n }$ exists and is a non-zero real number if and only if $\textstyle \sum _ { n } a _ { n } < \infty$

2. Let $f : \mathbb { R } \to \mathbb { R }$ be a nondecreasing real-valued function, i.e. if $x < y$ then $f \left( x \right) \leq f \left( y \right)$

(a) Prove that $\{ x \in \mathbb { R } : f$ is not continuous at x} is countable.

(b) Let $S \subset \mathbb { R }$ be a countable set. Prove there exists nondecreasing $f : \mathbb { R } \to \mathbb { R }$ such that for all $x \in \mathbb { R } , f$ is not continuous at x if and only ${ \mathrm { i f ~ } } x \in S .$

3. Let $\gamma : [ 0 , 1 ] \to \mathbb { R } ^ { 2 }$ be a continuous one-to-one function. By definition the length of the range $\gamma ( [ 0 , 1 ] )$ is

$$
L ( \gamma ) = \operatorname* { s u p } \{ \sum _ { j = 1 } ^ { n - 1 } | \gamma ( t _ { j + 1 } ) - \gamma ( t _ { j } ) | : 0 \leq t _ { 1 } < t _ { 2 } < . . . < t _ { n } \leq 1 , \ n < \infty \}
$$

where $| ( x , y ) | = { \sqrt { x ^ { 2 } + y ^ { 2 } } }$ when $( x , y ) \in \mathbb { R } ^ { 2 }$

(a) Suppose $f ( t )$ is continuous and nondecreasing on [0, 1], and let $\gamma ( t ) = ( t , f ( t ) )$ (so that the range of γ is the graph of f ). Prove

$$
L ( \gamma ) \leq 1 + ( f ( 1 ) - f ( 0 ) ) .
$$

(b) Show there exists continuous nondecreasing f(t) on [0, 1] such that $f ( 0 ) = 0 { \mathrm { ~ a n d ~ } } f ( 1 ) = 1$ and such that $L ( \gamma ) = 2$ when $\gamma ( t ) = ( t , f ( t ) )$ ,

4. Let $f ( x , y )$ be a continuous real-valued function on the plane $\mathbb { R } ^ { 2 }$ . Assume that for every square $\begin{array} { r } { S = \{ a < x < a + \frac { 1 } { n } , b < y < b + \frac { 1 } { n } \} } \end{array}$ , where a and b are rational numbers and $n = 1 , 2 , \ldots ,$

$$
\int \int _ { S } f ( x , y ) d x d y = 0 .
$$

Prove $f ( x , y ) = 0$ for all $( x , y )$

5. A function $f : \mathbb { R } ^ { d }  \mathbb { R }$ is said to be convex if

$$
f ( t x + ( 1 - t ) y ) \leq t f ( x ) + ( 1 - t ) f ( y ) , { \mathrm { ~ f o r ~ a l l ~ } } x , y \in \mathbb { R } ^ { d } , 0 \leq t \leq 1 .
$$

Assume that f is continuously differentiable such that

$$
( \nabla f ( x ) - \nabla f ( y ) ) \cdot ( x - y ) \geq 0 , \quad x , y \in \mathbb { R } ^ { d }
$$

where $\nabla f$ is the gradient of f and · is the inner product on $\mathbb { R } ^ { d }$ . Prove that f is convex.

6. Let X be a compact metric space, let $\{ x _ { n } \}$ be a sequence in X and let $x \in X$ . Assume that for every subsequence $\left\{ y _ { n } \right\}$ of $\{ x _ { n } \}$ there is a subsequence $\left\{ z _ { n } \right\}$ of $\left\{ y _ { n } \right\}$ such that $\left\{ z _ { n } \right\}$ converges to x. Prove $\{ x _ { n } \}$ converges to x.

7. Let $z _ { 1 } , z _ { 2 } , . . . , z _ { n }$ be distinct complex numbers and for $1 \leq j \leq n _ { \cdot }$ , let $m _ { j }$ be a non-negative integer. Write $\begin{array} { r } { N + 1 = \sum _ { j = 0 } ^ { n } ( 1 + m _ { j } ) } \end{array}$ . Prove that given any array of $N + 1$ complex numbers

$$
\begin{array} { r } { c _ { j , k } , 1 \le j \le n , 0 \le k \le m _ { j } , } \end{array}
$$

there is a unique polynomial $P ( z )$ of degree at most N such that for all $j , k$

$$
P ^ { ( k ) } ( z _ { j } ) = c _ { j , k }
$$

where $P ^ { ( k ) }$ denotes the k−th derivative, i.e. $( z ^ { n } ) ^ { ( 2 ) } = n ( n - 1 ) z ^ { n - 2 } , n \geq 2 .$

8. An orthogonal projection on a finite dimensional inner product space V is an endomorphism P that satisfies $P ^ { 2 } = P$ and $i m ( P ) = k e r ( P ) ^ { \perp }$ . Suppose $V = \mathbb { R } ^ { 3 }$ and P is an orthogonal projection with diagonal matrix entries $p _ { 1 , 1 } = 2 / 3 , p _ { 2 , 2 } = 1 / 2 , p _ { 3 , 3 } = 5 / 6$ . Find all matrices that P could be. (Hint: it’s a very small finite set!).

9. Let A be an endomorphism of a vector space V of dimension d over a field F . Show, from first principles (i.e. do not use Jordan form or the Cayley-Hamilton theorem) that A satisfies a polynomial $P ( X ) \in F [ X ]$ of degree at most d.

10. Let A be an n by n Hermitian matrix and let, for $j \in [ 1 , n ] , A _ { j }$ be the submatrix consisting of the entries of A in the first j row and columns of A. Suppose that $d e t ( A _ { j } ) \neq 0$ and $d e t ( A _ { 1 } ) > 0$ Give and prove a rule in terms of the signs of the $d e t ( A _ { j } )$ to determine the signature of the Hermitian form defined by A.

11. Define a normal linear transformation N on a finite dimensional complex inner product space V . Supposing that N is normal, show that there exists an orthogonal basis of V consisting of eigenvectors of N .

12. Suppose A is an endomorphism of a complex vector space with characteristic polynomial $C _ { A } ( X ) = X ^ { 4 } - 6 X ^ { 3 } + 1 3 X ^ { 2 } - 1 2 X + 4$ . How many similarity (i.e. conjugacy) classes of elements can have this characteristic polynomial? Suppose also that the minimal polynomial $M _ { A } ( X )$ of A is equal to $C _ { A } ( { \cal { X } } )$ . How many classes satisfy this additional condition? Prove your answers, quoting any general theorems you need.