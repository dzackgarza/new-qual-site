1. Let $g \in C ( [ a , b ] )$, with $a \leq g ( x ) \leq b$ for all $x \in [ a , b ]$ .Prove the following:

(i) g has at least one fixed point p in the interval [a, b].

(ii) If there is a value $\gamma < 1$ such that

$$
| g ( x ) - g ( y ) | \leq \gamma | x - y |
$$

for all $x , y \in \left[ a , b \right]$ , then the fixed point p is unique, and the iteration

$$
x _ { n + 1 } = g ( x _ { n } )
$$

converges to p for any initial guess $x _ { 0 } \in [ a , b ]$

2. Let $\{ f _ { n } ( x ) \}$ be a sequence of continuous functions on the unit interval [0, 1] such that $f _ { n } ( x ) \geq 0$ for all n and x and such that for all $x \in [ 0 , 1 ]$

$$
\operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) = 0 .
$$

Prove or give a counterexample to the assertion:

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x = 0 .
$$

3. Assuming that $f \in C ^ { 4 } [ a , b ]$ is real, derive a formula for the error of approximation $E ( h )$ when the second derivative is replaced by the finite-difference formula

$$
f ^ { \prime \prime } ( x ) \sim { \frac { f ( x + h ) - 2 f ( x ) + f ( x - h ) } { h ^ { 2 } } } ,
$$

and h is the mesh size.
(Assume that $x , x + h , x - h \in ( a , b ) )$

4. Let X be a compact subset of $\mathbb { R } ^ { N }$ and let $\{ f _ { n } ( x ) \}$ be a sequence of continuous real functions on X such that

$$
0 \leq f _ { n + 1 } ( x ) \leq f _ { n } ( x )
$$

and

lim $f _ { n } ( x ) = 0$ for all $x \in X .$

Prove Dini's Theorem that $f _ { n } ( x )$ converges to 0 uniformly on X.

5. (a) Let $F ( x , y )$ be a continuous function on the plane such that for every square S having its sides parallel to the axes,

$$
\int \int _ { S } F ( x , y ) d x d y = 0 .
$$

Prove $F ( x , y ) = 0 $ for all $( x , y )$

( Assume $\begin{array} { r } { f ( x , y ) , \frac { \partial f ( x , y ) } { \partial x } , \frac { \partial f ( x , y ) } { \partial y } , \frac { \partial } { \partial y } \left( \frac { \partial f ( x , y ) } { \partial x } \right) } \end{array}$ and $\textstyle { \frac { \partial } { \partial x } } \left( { \frac { \partial f ( x , y ) } { \partial y } } \right)$ are all continuous in the plane.
Use part (a) to prove that

$$
\frac { \partial } { \partial y } \Big ( \frac { \partial f ( x , y ) } { \partial x } \Big ) = \frac { \partial } { \partial x } \Big ( \frac { \partial f ( x , y ) } { \partial y } \Big ) .
$$

Hint: You may assume the double integral in (a) equals the iterated integral $\textstyle \int ( \int F ( x , y ) d x ) d y$ and equals the iterated integral $\textstyle { \int ( \int F ( x , y ) d y ) d x }$

6. Let Y be a complete countable metric space.
   Prove there is $y \in Y$ such that $\{ y \}$ is open.

7. Let $a ( x )$ be a function on R such that

(i) $a ( x ) \geq 0$ for all x, and

(ii) There exists $M < \infty$ such that for all finite $F \subset \mathbb { R }$

$$
\sum _ { F } a ( x ) \leq M .
$$

Prove $\{ x : a ( x ) > 0 \}$ is countable.

8. Assume V is an n-dimensional vector space over the rationals Q, and T is a Q-linear tranformation $T : V \to V$ such that $T ^ { 2 } = T$ Prove that every vector $v \in V$ can be written uniquely as $\boldsymbol { v } = \boldsymbol { v } _ { 1 } + \boldsymbol { v } _ { 2 }$ such that $T ( v _ { 1 } ) = v _ { 1 }$ and $T ( v _ { 2 } ) = 0$

## 9. Let V be a vector space over R.

(a) Prove that if V is odd dimension, and if T is an R-linear transformation $T : V \to V$ of V, then T has a non-zero eigenvector $v \in V$

(b) Show that for every even positive integer n, there is a a vector space V over R of dimension n, and an R-linear transformation $T : V  V$ of V, such that there is no non-zero $v \in V$ satisfying $T ( v ) = \lambda v$ for some $\lambda \in \mathbb { R }$

10. Suppose A is an $n \times n$ complex matrix such that A has n distinct eigenvalues.
    Prove that if B is an $n \times n$ complex matrix such that $A B = B A$ , then B is diagonalizable.

11. Assume A is an n x n complex matrix such that for some positive integer m the power $A ^ { m } = I _ { n }$ where $I _ { n }$ is the $n \times n$ identity matrix.
    Prove that A is diagonalizable.

12. Let A be an $n \times n$ real symmetric $\left( a _ { i , j } = a _ { j , i } \right)$ matrix, and let $S = \{ x \in \mathbb { R } ^ { n } : \textstyle \sum x _ { j } ^ { 2 } = 1 \}$ be the unit sphere of $\mathbb { R } ^ { n }$.
    Let $x \in S$ be such that

$$
( A x , x ) = \operatorname* { s u p } _ { S } ( A y , y )
$$

where $\begin{array} { r } { ( z , y ) = \sum z _ { j } y _ { j } } \end{array}$ is the usual inner product on $\mathbb { R } ^ { n } .$ (By compactness such x exists.)

(a) Prove that $( x , y ) = 0 \Longrightarrow ( A x , y ) = 0 .$ Hint: Expand

$$
( A ( x + \epsilon y ) , x + \epsilon y ) .
$$

(b) Use (a) to prove x is an eigenvector for A.

(c) Use induction to prove $\mathbb { R } ^ { n }$ has an orthonormal basis of eigenvectors for A. Note: If you use part (c) to prove part (a) or part (b), then your solution should include a proof of part (c) that does not use part (a) or part (b).
