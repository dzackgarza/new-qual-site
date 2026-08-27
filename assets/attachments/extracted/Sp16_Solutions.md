Show that

$$
\int _ { 4 } ^ { 9 } { \sqrt { - 6 + 5 { \sqrt { - 6 + 5 { \sqrt { - 6 + 5 { \sqrt { - 6 + 5 { \sqrt { x } } } } } } } } } } d x
$$

is a rational number.

Solution: Let $f ( x )$ be the function in the integrand. Note that $f ( x )$ is defined on $[ 4 , 9 ]$ as $4 \leq - 6 + 5 \sqrt { x } \leq 9$ whenever $4 \leq x \leq 9$ . Also, $f ( x )$ is strictly increasing and $f ( 4 ) = 2$ and $f ( 9 ) = 3$ . So $f \colon [ 4 , 9 ]  [ 2 , 3 ]$ is invertible. Its inverse is

$$
f ^ { - 1 } ( y ) = \left( \frac { \frac { \Big ( \frac { \big ( \frac { y ^ { 2 } + 6 } { 5 } \big ) ^ { 2 } + 6 } { 5 } \Big ) ^ { 2 } + 6 } { 5 } \Big ) ^ { 2 } + 6 } { 5 } \right) ^ { 2 }
$$

which is a polynomial with rational coefficients.

The integral $\textstyle \int _ { 4 } ^ { 9 } f ( x ) d x$ is equal to the area of the region bounded by the graph $y = f ( x )$ the vertical lines $x = 4 , x = 9$ and the x-axis. The union of this region with the region bounded by the graph $y = f ( x )$ , the horizontal lines $y = 2 , y = 3$ and the y-axis is the difference between two rectangles: one bounded by the lines $x = 9 , y = 3$ and the x, y-axes and the other bounded by the lines $x = 4 , y = 2$ and the x, y-axes. Thus

$$
\int _ { 4 } ^ { 9 } f ( x ) d x + \int _ { 2 } ^ { 3 } f ^ { - 1 } ( y ) d y = 9 \cdot 3 - 4 \cdot 2 .
$$

The second integral is a rational number, since $f ^ { - 1 } ( y )$ is a polynomial with rational coefficients. So the first integral is also a rational number.

## Problem 2A.

Score:

Suppose that f and g are continuously differentiable real-valued functions on R with $f , g , f ^ { \prime } , g ^ { \prime } \in$ $L ^ { 2 } ( \mathbb { R } )$ . Show that

$$
\int _ { - \infty } ^ { \infty } f g ^ { \prime } d x = - \int _ { - \infty } ^ { \infty } f ^ { \prime } g d x .
$$

(Recall that $L ^ { 2 } ( \mathbb { R } )$ is the set of integrable functions h such that $\textstyle \int _ { - \infty } ^ { \infty } | h | ^ { 2 } \ d x < \infty . \textstyle )$

Solution: The condition $f , g , f ^ { \prime } , g ^ { \prime } \in L ^ { 2 } ( \mathbb { R } )$ implies that the two integrals exist. It also implies that $\begin{array} { r } { \int _ { - \infty } ^ { \infty } | f ( x ) | { \cdot } | g ( x ) | \ d x < \infty } \end{array}$ , and hence that there are sequences $\{ x _ { i } \} _ { i = 1 } ^ { \infty }$ and $\{ y _ { i } \} _ { i = 1 } ^ { \infty }$

such that lim $\begin{array} { r } { \mathsf { 1 } _ { i \to \infty } x _ { i } = - \infty , \operatorname* { l i m } _ { i \to \infty } y _ { i } = \infty } \end{array}$ and lim $\begin{array} { r } { \ O _ { 1 } { _ { \longrightarrow \infty } } f ( x _ { i } ) g ( x _ { i } ) = \operatorname* { l i m } _ { i \to \infty } f ( y _ { i } ) g ( y _ { i } ) = 0 . } \end{array}$ Then

$$
\int _ { - \infty } ^ { \infty } ( f g ^ { \prime } + f ^ { \prime } g ) d x = \operatorname* { l i m } _ { i \to \infty } \int _ { x _ { i } } ^ { y _ { i } } ( f g ^ { \prime } + f ^ { \prime } g ) d x = \operatorname* { l i m } _ { i \to \infty } ( f ( y _ { i } ) g ( y _ { i } ) - f ( x _ { i } ) g ( x _ { i } ) ) = 0 .
$$

## Problem 3A.

Score:

Suppose g and $f _ { n }$ are nonnegative integrable functions such that $\textit { f f } _ { n } d x  0$ as $n $ ∞ and $f _ { n } ^ { 2 } \leq g$ for all n. Prove or find a counterexample to the statement that $\textit { f } f _ { n } ^ { 4 } d x  0$ a s $n \to \infty$

Solution: For a counterexample we can take the domain of the functions to be $( 0 , 1 )$ , take $f _ { n }$ to be the step function

$$
f _ { n } ( x ) = \left\{ { \begin{array} { l l } { n ^ { 1 / 4 } } & { 0 < x \leq 1 / n } \\ { 0 } & { 1 / n < x < 1 , } \end{array} } \right.
$$

and take $g ( x ) = x ^ { - 1 / 2 }$ . The condition $f _ { n } ^ { 2 } \leq g$ is satisfied, $g$ is integrable with $\textstyle { \int g d x = 2 , f _ { n } }$ is integrable with $\textstyle { \int f _ { n } d x = n ^ { - 3 / 4 } \to 0 }$ , and $\textstyle \int f _ { n } ^ { 4 } d x = 1$ for all n.

## Problem 4A.

Score:

Prove that a monic polynomial $p ( z )$ with real coefficients is real-rooted if and only if $\Im ( p ^ { \prime } ( z ) / p ( z ) ) < 0$ whenever $\Im ( z ) > 0$ . (=(z) denotes the imaginary part of z.)

Solution: (⇒) Let $\begin{array} { r } { p ( z ) = \prod _ { i = 1 } ^ { n } ( z - \lambda _ { i } ) } \end{array}$ and observe that

$$
{ \frac { p ^ { \prime } ( z ) } { p ( z ) } } = \sum _ { i = 1 } ^ { n } { \frac { 1 } { z - \lambda _ { i } } } = \sum _ { i = 1 } ^ { n } { \frac { { \overline { { z } } } - { \overline { { \lambda _ { i } } } } } { | z - \lambda _ { i } | ^ { 2 } } } .
$$

Since the $\lambda _ { i }$ are real all the numerators are in the lower half plane for z in the upper half plane, so any linear combination of them with nonnegative coefficients is also in the lower half plane.

(⇐) If $p$ is not real-rooted then it must have a zero in the upper half plane, since the zeros occur in conjugate pairs. Let λ be such a zero, occuring with multiplicity $m$ , and observe that

$$
\frac { p ^ { \prime } } { p } ( \lambda - \epsilon i ) = \frac { m } { - \epsilon i } + \frac { q ^ { \prime } } { q } ( \lambda - \epsilon i ) ,
$$

where $q ( z ) ~ = ~ p ( z ) / ( z ~ - ~ \lambda ) ^ { m }$ Since $q ( \lambda ) ~ \neq ~ 0$ we find that $q ^ { \prime } ( z ) / q ( z )$ is bounded in a neighborhood of λ, so

$$
\operatorname * { l i m } _ { \epsilon  0 } \frac { m } { - \epsilon i } + \frac { q ^ { \prime } } { q } ( \lambda - \epsilon i ) = i \infty ,
$$

in particular yielding $\mathrm { ~ a ~ } z$ for which $\Im ( z ) > 0$ and $\Im ( p ^ { \prime } ( z ) / p ( z ) ) > 0 .$

## Problem 5A.

Score:

Compute

$$
\int _ { 0 } ^ { 2 \pi } \frac { d \theta } { ( 3 + e ^ { - i \theta } ) ^ { 2 } } .
$$

Solution: Put $z = e ^ { i \theta }$ . Then

$$
\int _ { 0 } ^ { 2 \pi } \frac { d \theta } { ( 3 + e ^ { - i \theta } ) ^ { 2 } } = \int _ { | z | = 1 } \frac { 1 } { ( 3 + z ^ { - 1 } ) ^ { 2 } } \frac { d z } { i z } = 2 \pi \mathrm { R e s } _ { z = - \frac { 1 } { 3 } } \frac { z } { ( 3 z + 1 ) ^ { 2 } } = \frac { 2 \pi } { 9 } .
$$

## Problem 6A.

Score:

Prove or disprove: there exists an $\epsilon > 0$ and a real matrix A such that

$$
A ^ { 1 0 0 } = \left[ \begin{array} { c c } { { - 1 } } & { { 0 } } \\ { { 0 } } & { { - 1 - \epsilon } } \end{array} \right] .
$$

Solution: The eigenvalues $a , b \in \mathbb { C }$ of such a matrix A must satisfy

$$
a ^ { 1 0 0 } = - 1 b ^ { 1 0 0 } = ( - 1 - \epsilon ) .
$$

Note that a cannot be real since 100 is even. Moreover, since A is real its characteristic polynomial is real so we must have $a = { \bar { b } }$ . But this is impossible since $| a | ^ { 1 0 0 } = 1 \quad$ and $| b | ^ { 1 0 0 } = ( 1 + \epsilon ) ^ { 1 0 0 } \neq 1$ . So no such matrix can exist.

## Problem 7A.

Score:

Suppose A is a symmetric matrix with rational entries and $A = U D U ^ { T }$ , where U is orthogonal. Must D have rational entries? Prove or find a counterexample.

Solution: Since U is orthogonal the factorization $A = U D U ^ { T }$ diagonalizes A so the entries of D are the eigenvalues of A. These are the roots of its characteristic polynomial, which need not be rational. For instance, consider

$$
A = \left[ \begin{array} { r r } { { 1 } } & { { 1 } } \\ { { 1 } } & { { - 1 } } \end{array} \right] .
$$

The characteristic polynomial of this matrix is

$$
( x - 1 ) ( x + 1 ) - 1 = x ^ { 2 } - 2 ,
$$

which has roots $\pm { \sqrt { 2 } } .$

## Problem 8A.

Score:

Find a product of cyclic groups of prime power order isomorphic to the group of units in the ring of integers modulo 2016.

Solution: $2 0 1 6 = 2 ^ { 5 } \times 3 ^ { 2 } \times 7 .$ so the group of units is the product of the groups of units of the integers mod $2 ^ { 5 } , 3 ^ { 2 } , 7 .$ which are products of cyclic groups of orders 2, 8 and 2, 3 and 2, 3. So the solution is that the group is a product of cyclic groups of orders 2, 2, 2, 3, 3, 8.

## Problem 9A.

Score:

Compute the Galois group of the normal closure of the field

$$
K = \mathbb { Q } ( { \sqrt { 3 } } + { \sqrt { 5 } } )
$$

over $\mathbb { Q } .$

Solution: We first prove $K = \mathbb { Q } ( { \sqrt { 3 } } , { \sqrt { 5 } } )$ . For that, it suffices to prove ${ \sqrt { 3 } } , { \sqrt { 5 } } \in K$ . In fact, by

$$
( { \sqrt { 3 } } + { \sqrt { 5 } } ) ^ { 2 } = 8 + 2 { \sqrt { 1 5 } } ,
$$

we have ${ \sqrt { 1 5 } } \in K$ . Then

$$
( { \sqrt { 3 } } + { \sqrt { 5 } } ) { \sqrt { 1 5 } } = 5 { \sqrt { 3 } } + 3 { \sqrt { 5 } }
$$

is also in K. Its Q-linear combinations with ${ \sqrt { 3 } } + { \sqrt { 5 } }$ give ${ \sqrt { 3 } } , { \sqrt { 5 } } \in K$

As a consequence, K is Galois over Q, since it is the composite of two Galois extensions over Q. The normal closure of K over Q is still K.

We next prove $\mathbb { Q } ( { \sqrt { 3 } } ) \cap \mathbb { Q } ( { \sqrt { 5 } } ) = \mathbb { Q }$ . Otherwise, we would have $\mathbb { Q } ( { \sqrt { 3 } } ) = \mathbb { Q } ( { \sqrt { 5 } } )$ since both of them have degree 2 over Q. As a consequence, we have ${ \sqrt { 5 } } = a { \sqrt { 3 } } + b$ for some

$a , b \in \mathbb { Q }$ . Taking squares, we have√ $5 = 3 a ^ { 2 } + b ^ { 2 } + 2 a b { \sqrt { 3 } }$ . We must have $a b = 0$ , so $a = 0$ or $b = 0$ . If $a = 0 , { \sqrt { 5 } } = b \in \mathbb { Q }$ is a contradiction. If $b = 0 , \ { \sqrt { 5 / 3 } } = a \in \mathbb { Q }$ is still a contradiction.

Finally, the composite gives

$$
\operatorname { G a l } ( K / \mathbb { Q } ) = \operatorname { G a l } ( \mathbb { Q } ( { \sqrt { 3 } } ) / \mathbb { Q } ) \times \operatorname { G a l } ( \mathbb { Q } ( { \sqrt { 5 } } ) / \mathbb { Q } ) \simeq ( \mathbb { Z } / 2 \mathbb { Z } ) ^ { 2 } .
$$

An alternate approach is to start by by showing, as above, that ${ \sqrt { 5 } } \not \in \mathbb { Q } ( { \sqrt { 3 } } )$ , and define $L = \mathbb { Q } ( { \sqrt { 3 } } , { \sqrt { 5 } } )$ . Then L has degree 4 over $\mathbb { Q }$ and $\operatorname { A u t } _ { \mathbb { Q } } ( L )$ contains a group G isomorphic to $( \mathbb { Z } / 2 \mathbb { Z } ) ^ { 2 }$ , generated by $\sigma \colon \sqrt { 3 }  - \sqrt { 3 }$ and $\tau \colon \sqrt { 5 }  - \sqrt { 5 }$ . It follows that L is Galois over $\mathbb { Q }$ with Galois group $G .$ Since the stabilizer of ${ \sqrt { 3 } } + { \sqrt { 5 } }$ in G is trivial, $K = L$

Problem 1B.

Score:

Show that

$$
\int _ { 0 } ^ { \infty } { \frac { t e ^ { - t / 2 } } { 1 - e ^ { - t } } } d t = 4 \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { ( 2 n + 1 ) ^ { 2 } } }
$$

Solution:

Expand e $^ { - t / 2 } / ( 1 - e ^ { - t } )$ in a geometric series and integrate

$$
\int _ { 0 } ^ { \infty } \sum _ { n = 0 } ^ { \infty } t e ^ { - ( n + 1 / 2 ) t } d t .
$$

term by term, using the formula

$$
\int _ { 0 } ^ { \infty } e ^ { - \alpha t } t d t = { \frac { 1 } { \alpha ^ { 2 } } } ,
$$

valid for any $\alpha > 0$ . This formula can be obtained using integration by parts.

(It is also possible, but more difficult, to evaluate both sides of the required identity explicitly, obtaining the value $\pi ^ { 2 } / 2 . )$

Since this is meant to be a calculus problem rather than a real analysis problem, graders should not demand justification for the interchange of summation and integration.

## Problem 2B.

Score:

Let $( f _ { i } ) _ { i = 1 } ^ { \infty }$ and $g$ be twice-differentiable real-valued functions on R, with $f _ { i } ^ { \prime \prime } \geq 0$ . Suppose that

$$
\operatorname * { l i m } _ { i \to \infty } f _ { i } ( x ) = g ( x )
$$

for all $x \in \mathbb { R }$ . Show that $g ^ { \prime \prime } \geq 0$

Solution: Since each $f _ { i }$ is concave upward, we have

$$
f _ { i } ( z ) \leq { \frac { f _ { i } ( z + h ) + f _ { i } ( z - h ) } { 2 } }
$$

for all $z , h \in \mathbb { R }$ . It follows that g satisfies the same inequality. Then

$$
g ^ { \prime \prime } ( z ) = \operatorname* { l i m } _ { h \to 0 } { \frac { g ( z + h ) + g ( z - h ) - 2 g ( z ) } { h ^ { 2 } } } \geq 0
$$

for all $z \in \mathbb { R }$

## Problem 3B.

Score:

Show that the series

$$
\sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } } { k + | x | } }
$$

converges pointwise to a Lipschitz function $f ( x )$ . Is the convergence uniform on $\mathbb { R } ?$

Solution: Since the series is alternating for every x, it converges pointwise to some limiting function $f ( x )$ . For the Lipschitz condition, we can assume without loss of generality that $x \geq 0$ and compute

$$
\sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } } { k + x } } - \sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } } { k + x + \epsilon } } = \sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } \epsilon } { ( k + x ) ( k + x + \epsilon ) } } .
$$

The last sum is again an alternating series, bounded in absolute value by its first term $\epsilon / ( ( 1 + x ) ( 1 + x + \epsilon ) ) \leq \epsilon .$ . Hence $f ( x )$ is Lipschitz with constant 1.

Using again the fact the series is alternating, its $N ^ { \mathrm { t h } }$ tail has

$$
\left| f ( x ) - \sum _ { k = 1 } ^ { N - 1 } { \frac { ( - 1 ) ^ { k } } { k + | x | } } \right| = \left| \sum _ { k = N } ^ { \infty } { \frac { ( - 1 ) ^ { k } } { k + | x | } } \right| \leq { \frac { 1 } { N + | x | } } \leq { \frac { 1 } { N } } ,
$$

so it converges uniformly.

## Problem 4B.

Score:

Compute

$$
\int _ { C } { \frac { 6 z ^ { 5 } + 1 } { z ^ { 6 } + z + 1 } } d z ,
$$

where C is the circle centered at the origin with radius 2, oriented counterclockwise.

Solution: If $| z | > 3 / 2$ then $| z + 1 | \le | z | + 1 < | z | ^ { 6 } = | z ^ { 6 } |$ , so $\frac { 6 z ^ { 5 } + 1 } { z ^ { 6 } + z + 1 }$ is analytic on $\{ z \colon | z | > 3 / 2 \}$ . Then

$$
\int _ { C } { \frac { 6 z ^ { 5 } + 1 } { z ^ { 6 } + z + 1 } } d z = - 2 \pi i { \mathrm { ~ R e s } } _ { z = \infty } { \frac { 6 z ^ { 5 } + 1 } { z ^ { 6 } + z + 1 } } = 1 2 \pi i .
$$

Alternate solution: the integrand is the derivative of $\log ( z ^ { 6 } + z + 1 )$ . Hence the integral is i times the change in arg $\cdot ( z ^ { 6 } + z + 1 )$ along C, or 2πi times the number of zeroes of $z ^ { 6 } + z + 1$ inside C. The same argument as above shows that all six zeroes are inside C.

Problem 5B.

Score:

Let $f ( z ) = \sum f _ { n } z ^ { n }$ and $g ( z ) = \sum g _ { n } z ^ { n }$ define holomorphic functions on a neighborhood of the closed unit disk $D = \{ z : | z | \leq 1 \}$ Prove that $h ( z ) = \textstyle \sum f _ { n } g _ { n } z ^ { n }$ also defines a holomorphic function on a neighborhood of D.

Solution: The series for $f ( z )$ and $g ( z )$ must have radius of convergence greater than 1. Hence there is a $\rho > 1$ such that $f _ { n } / \rho ^ { n } \to 0$ and $g _ { n } / \rho ^ { n } \to 0 { \mathrm { ~ a s ~ } } n \to \infty$ . Then $f _ { n } g _ { n } / \rho ^ { 2 n } \to 0$ implies that the series for $h ( z )$ has radius of convergence at least $\rho ^ { 2 }$ , which is again greater than 1.

Problem 6B.

Score:

Let A be an $m \times n$ real matrix and $y \in \mathbb { R } ^ { m }$ . Let $x \in \mathbb { R } ^ { n }$ be a vector with nonnegative entries that minimizes the Euclidean distance $\| y - A x \|$ (among all nonnegative vectors x). Show that the vector $v = A ^ { T } ( y - A x )$ has nonnegative entries.

Solution: Suppose $v _ { j } = a _ { j } ^ { T } ( A x - y ) < 0$ , where $a _ { j } = A e _ { j }$ is the j-th column of A. Then for sufficiently small $\epsilon > 0$ 7

$$
\| y - A ( x + \epsilon e _ { j } ) \| ^ { 2 } = \| y - A x - \epsilon a _ { j } \| ^ { 2 } = \| y - A x \| ^ { 2 } + 2 \epsilon a _ { j } ^ { T } ( A x - y ) + \epsilon ^ { 2 } \| a _ { j } \| ^ { 2 } < \| y - A x \| ^ { 2 } ,
$$

contrary to the hypothesis on x.

Score:

Let A be a real square matrix and let $\rho$ be the maximum of the absolute values of its eigenvalues $( i . e .$ , its spectral radius). (1) Show that if A is symmetric then $\| A x \| \leq \rho \| x \|$ for all $x \in \mathbb { R } ^ { n }$ , where k·k denotes the Euclidean norm. (2) Is this true when A is not symmetric? Prove or give a counterexample.

Solution: (1) Assume A is $n \times n .$ . Since A is symmetric it has real eigenvalues $\lambda _ { 1 } \ldots \lambda _ { n }$ and orthogonal eigenvectors $u _ { 1 } , \ldots , u _ { n }$ . Thus, by the spectral theorem:

$$
A ^ { 2 } = \sum _ { i = 1 } ^ { n } \lambda _ { i } ^ { 2 } u _ { i } u _ { i } ^ { T } .
$$

This implies that for any x:

$$
\| A x \| ^ { 2 } = x ^ { T } A ^ { 2 } x = \sum _ { i = 1 } ^ { n } \lambda _ { i } ^ { 2 } \langle x , u _ { i } \rangle ^ { 2 } \leq \left( \operatorname* { m a x } _ { i } \lambda _ { i } ^ { 2 } \right) \| x \| ^ { 2 } ,
$$

since $\textstyle \sum _ { i = 1 } ^ { n } \langle x , u _ { i } \rangle ^ { 2 } = \| x \| ^ { 2 }$ . Taking square roots proves the claim.

(2) This is not true. Consider the matrix

$$
A = { \bigg [ } 0 \ { \begin{array} { l } { 1 } \\ { 0 } \end{array} } { \bigg ] }
$$

which has both eigenvalues equal to zero, but

$$
A e _ { 2 } = e _ { 1 } ,
$$

for elementary basis vectors $e _ { 1 } , e _ { 2 }$

## Problem 8B.

Score:

Factor the polynomial

$$
f ( x ) = 6 x ^ { 5 } + 3 x ^ { 4 } - 9 x ^ { 3 } + 1 5 x ^ { 2 } - 1 3 x - 2
$$

into a product of irreducible polynomials in the ring $\mathbb { Q } [ x ]$

Solution: Since $f ( 1 ) = 0$ , the polynomial has a factor $x - 1$ . Then we obtain

$$
f ( x ) = ( x - 1 ) ( 6 x ^ { 4 } + 9 x ^ { 3 } + 1 5 x + 2 ) .
$$

We claim that this is a final form of the factorization, for which we need to prove that

$$
g ( x ) = 6 x ^ { 4 } + 9 x ^ { 3 } + 1 5 x + 2
$$

is irreducible.

First, the polynomial

$$
h ( x ) = 2 x ^ { 4 } + 1 5 x ^ { 3 } + 9 x + 6
$$

is irreducible. This follows from the Eisenstein criterion by the prime number $p = 3$

Second, for any polynomial

$$
\phi ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { 0 }
$$

of degree n, denote

$$
{ \tilde { \phi } } ( x ) = x ^ { n } \phi ( x ^ { - 1 } ) = a _ { 0 } x ^ { n } + \cdot \cdot \cdot + a _ { n - 1 } x + a _ { n } .
$$

Then $g ( x ) = \tilde { h } ( x )$ , and a decomposition $g ( x ) = g _ { 1 } ( x ) g _ { 2 } ( x )$ would give a decomposition

$$
h ( x ) = \tilde { g } _ { 1 } ( x ) \tilde { g } _ { 2 } ( x ) .
$$

Hence, $g$ is irreducible.

## Problem 9B.

Score:

Let p be a prime number. Prove that every group G of order $p ^ { 2 }$ is commutative.

Solution: Let G act on itself by conjugation, $g ( x ) = g x g ^ { - 1 }$ Under the action, $G$ is a disjoint union of orbits $O _ { 0 } , O _ { 1 } , . . . , O _ { r }$ , where ${ \cal O } _ { 0 } = \{ e \}$ is the orbit of the identity element. The length $| O _ { i } |$ of each orbit is a divisor of $| G | = p ^ { 2 }$ , so is equal to 1, $p ,$ or $p ^ { 2 }$ . We have the sum

$$
| O _ { 0 } | + | O _ { 1 } | + \cdots + | O _ { r } | = | G | = p ^ { 2 } .
$$

Since $| O _ { 0 } | = 1$ , at least $p - 1$ other orbits $O _ { i }$ must have length 1. Let $O _ { i _ { 0 } } = \{ x _ { 0 } \}$ be such an orbit. By definition, $g x _ { 0 } g ^ { - 1 } = x _ { 0 }$ for all $g \in G$ . Then $x _ { 0 }$ is in the center of $G$ , and it is not the identity.

If $x _ { 0 }$ generates $G ,$ then $G \cong \mathbb { Z } / p ^ { 2 } \mathbb { Z }$ is commutative. If $x _ { 0 }$ does not generate $G ,$ then it generates a subgroup $\langle x _ { 0 } \rangle$ of order $p .$ . Let $x _ { 1 }$ be any element of $G - \langle x _ { 0 } \rangle$ . Then the subgroup $\left. x _ { 0 } , x _ { 1 } \right.$ has order greater than $p ,$ thus it is equal to $G .$ . Since $x _ { 0 }$ and $x _ { 1 }$ commute, we see that G is still commutative.