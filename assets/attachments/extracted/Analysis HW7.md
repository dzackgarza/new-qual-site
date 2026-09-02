# Math 8100 Assignment 7 Hilbert Spaces

Due date: Thursday 14th of November 2019

1. (a) Prove that $\ell ^ { 2 } ( \mathbb { N } )$ is complete.

Recall that $\ell ^ { 2 } ( \mathbb { N } ) : = \{ x = \{ x _ { j } \} _ { j = 1 } ^ { \infty } : \| x \| _ { \ell ^ { 2 } } < \infty \}$ , where $\| x \| _ { \ell ^ { 2 } } : = \Big ( \sum _ { j = 1 } ^ { \infty } | x _ { j } | ^ { 2 } \Big ) ^ { 1 / 2 } .$

(b) Let H be a Hilbert space.
Prove the so-called polarization identity, namely that for any $x , y \in H$

$$
\langle x , y \rangle = { \frac { 1 } { 4 } } \left( \| x + y \| ^ { 2 } - \| x - y \| ^ { 2 } + i \| x + i y \| ^ { 2 } - i \| x - i y \| ^ { 2 } \right)
$$

and conclude that any invertible linear map from H to $\ell ^ { 2 } ( \mathbb { N } )$ is unitary if and only if it is isometric.

Recall that if $H _ { 1 }$ and $H _ { 2 }$ are Hilbert spaces with inner products $\langle \cdot , \cdot \rangle _ { 1 }$ and $\langle \cdot , \cdot \rangle _ { 2 }$ , then a mapping $U : H _ { 1 } \to H _ { 2 }$ is said to be unitary if it is an invertible linear map that preserves inner products, namely $\langle U x , U y \rangle _ { 2 } = \langle x , y \rangle _ { 1 }$ , and an isometry if it preserves “lengths”, namely $\| U x \| _ { 2 } = \| x \| _ { 1 }$

2. Let E be a subset of a Hilbert space H.

(a) Show that $E ^ { \perp } : = \{ x \in H : \langle x , y \rangle = 0$ for all $y \in E \}$ is a closed subspace of $H$

(b) Show that $( E ^ { \bot } ) ^ { \bot }$ is the smallest closed subspace of H that contains E.

3. In $L ^ { 2 } ( [ 0 , 1 ] )$ let $e _ { 0 } ( x ) = 1 , e _ { 1 } ( x ) = { \sqrt { 3 } } ( 2 x - 1 )$ for all $x \in ( 0 , 1 )$

(a) Show that $e _ { 0 } , e _ { 1 }$ is an orthonormal system in $L ^ { 2 } ( 0 , 1 )$

(b) Show that the polynomial of degree 1 which is closest with respect to the norm of $L ^ { 2 } ( 0 , 1 )$ to the function $f ( x ) = x ^ { 2 }$ is given by $g ( x ) = x - 1 / 6$ . What is $\| f - g \| _ { 2 } ?$

4. (a) Verify that the following systems are orthogonal in $L ^ { 2 } ( [ 0 , 1 ] )$

$$
\{ 1 / \sqrt { 2 } , \cos ( 2 \pi x ) , \sin ( 2 \pi x ) , \ldots , \cos ( 2 \pi k x ) , \sin ( 2 \pi k x ) , \ldots \}
$$

ii.
$\{ e ^ { 2 \pi i k x } \} _ { k = - \infty } ^ { \infty }$

(b) Let $f \in L ^ { 1 } ( [ 0 , 1 ] )$

i. Show that for any $\epsilon > 0$ we can write $f = g + h$ , where $g \in L ^ { 2 }$ and $\| h \| _ { 1 } < \epsilon$

ii.
Use this decomposition of f to prove the so-called Riemann-Lebesgue lemma:

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { 1 } f ( x ) \cos ( 2 \pi k x ) d x = \operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { 1 } f ( x ) \sin ( 2 \pi k x ) d x = 0
$$

5. (a) The first three Legendre polynomials are

$$
P _ { 0 } ( x ) = 1 , \quad P _ { 1 } ( x ) = x , \quad P _ { 2 } ( x ) = ( 3 x ^ { 2 } - 1 ) / 2 .
$$

Show that the orthonormal system in $L ^ { 2 } ( [ - 1 , 1 ] )$ obtained by applying the Gram-Schmidt process to $1 , x , x ^ { 2 }$ are scalar multiples of these.

(b) Compute

$$
\operatorname* { m i n } _ { a , b , c } \int _ { - 1 } ^ { 1 } | x ^ { 3 } - a - b x - c x ^ { 2 } | ^ { 2 } d x
$$

(c) Find

$$
\operatorname* { m a x } \int _ { - 1 } ^ { 1 } x ^ { 3 } g ( x ) d x
$$

where g is subject to the restrictions

$$
\int _ { - 1 } ^ { 1 } g ( x ) d x = \int _ { - 1 } ^ { 1 } x g ( x ) d x = \int _ { - 1 } ^ { 1 } x ^ { 2 } g ( x ) d x = 0 ; \ \int _ { - 1 } ^ { 1 } | g ( x ) | ^ { 2 } d x = 1 .
$$

6. Let

$$
{ \mathcal { C } } = \left\{ f \in L ^ { 2 } ( [ 0 , 1 ] ) : \int _ { 0 } ^ { 1 } f ( x ) d x = 1 \ { \mathrm { ~ a n d ~ } } \ \int _ { 0 } ^ { 1 } x f ( x ) d x = 2 \right\}
$$

(a) Let $g ( x ) = 1 8 x ^ { 2 } - 5$ . Show that $g \in { \mathcal { C } }$ and that

$$
\mathcal { C } = g + \mathcal { S } ^ { \perp }
$$

where $\mathcal { S } ^ { \perp }$ denotes the orthogonal complement of $S = \operatorname { S p a n } \left( \{ 1 , x \} \right)$

(b) Find the function $f _ { 0 } \in { \mathcal { C } }$ for which

$$
\int _ { 0 } ^ { 1 } | f _ { 0 } ( x ) | ^ { 2 } d x = \operatorname* { i n f } _ { f \in { \mathcal C } } \int _ { 0 } ^ { 1 } | f ( x ) | ^ { 2 } d x .
$$

## Extra Challenge Problems

Not to be handed in with the assignment

1. Prove that every closed convex set K in a Hilbert space has a unique element of minimal norm.

2. The Mean Ergodic Theorem: Let U be a unitary operator on a Hilbert space H.

Prove that if $M = \{ x \ : \ U x = x \}$ and $\begin{array} { r } { S _ { N } = \frac { 1 } { N } \sum _ { n = 0 } ^ { N - 1 } U ^ { n } } \end{array}$ , then lim $\| S _ { N } x - P x \| = 0$ N→∞ for all $x \in H$ , where P x denotes the orthogonal projection of x onto M.
