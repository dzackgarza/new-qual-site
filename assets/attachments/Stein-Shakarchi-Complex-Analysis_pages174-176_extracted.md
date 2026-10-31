(a) Show that if $\sum | a _ { n } | ^ { 2 }$ converges, then the product $\prod ( 1 + a _ { n } )$ converges to a non-zero limit if and only $\operatorname { i f } \sum a _ { n }$ converges.

(b) Find an example of a sequence of complex numbers $\left\{ a _ { n } \right\}$ such that $\sum a _ { n }$ converges but $\prod ( 1 + a _ { n } )$ diverges.

(c) Also find an example such that $\prod ( 1 + a _ { n } )$ converges and $\sum a _ { n }$ diverges.

8. Prove that for every z the product below converges, and

$$
\cos ( z / 2 ) \cos ( z / 4 ) \cos ( z / 8 ) \cdots = \prod _ { k = 1 } ^ { \infty } \cos ( z / 2 ^ { k } ) = { \frac { \sin z } { z } } .
$$

[Hint: Use the fact that sin $2 z = 2 \sin z \cos z . ]$

9. Prove that if $| z | < 1$ , then

$$
( 1 + z ) ( 1 + z ^ { 2 } ) ( 1 + z ^ { 4 } ) ( 1 + z ^ { 8 } ) \cdot \cdot \cdot = \prod _ { k = 0 } ^ { \infty } ( 1 + { z ^ { 2 } } ^ { k } ) = { \frac { 1 } { 1 - z } } .
$$

10. Find the Hadamard products for:

(a) $e ^ { z } - 1$

(b) cos πz.

[Hint: The answers are $\scriptstyle e ^ { z / 2 } z \prod _ { n = 1 } ^ { \infty } ( 1 + z ^ { 2 } / 4 n ^ { 2 } \pi ^ { 2 } )$ and $\scriptstyle \prod _ { n = 0 } ^ { \infty } ( 1 - 4 z ^ { 2 } / ( 2 n + 1 ) ^ { 2 } )$ respectively.]

11. Show that if f is an entire function of finite order that omits two values, then f is constant. This result remains true for any entire function and is known as Picard’s little theorem.

[Hint: If f misses a, then $f ( z ) - a$ is of the form $e ^ { p ( z ) }$ where p is a polynomial.]

12. Suppose f is entire and never vanishes, and that none of the higher derivatives of $f$ ever vanish. Prove that if f is also of finite order, then $f ( z ) = e ^ { a z + b }$ for some constants a and b.

13. Show that the equation $e ^ { z } - z = 0$ has infinitely many solutions in C.

[Hint: Apply Hadamard’s theorem.]

14. Deduce from Hadamard’s theorem that if $F$ is entire and of growth order $\rho$ that is non-integral, then F has infinitely many zeros.

15. Prove that every meromorphic function in C is the quotient of two entire functions. Also, if $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ are two disjoint sequences having no finite limit

points, then there exists a meromorphic function in the whole complex plane that vanishes exactly at $\left\{ a _ { n } \right\}$ and has poles exactly at $\left\{ b _ { n } \right\}$

## 16. Suppose that

$$
Q _ { n } ( z ) = \sum _ { k = 1 } ^ { N _ { n } } c _ { k } ^ { n } z ^ { k }
$$

are given polynomials for $n = 1 , 2 , \ldots$ Suppose also that we are given a sequence of complex numbers $\left\{ a _ { n } \right\}$ without limit points. Prove that there exists a meromorphic function $f ( z )$ whose only poles are at $\left\{ a _ { n } \right\}$ , and so that for each n, the difference

$$
f ( z ) - Q _ { n } \left( { \frac { 1 } { z - a _ { n } } } \right)
$$

is holomorphic near $a _ { n }$ . In other words, f has a prescribed poles and principal parts at each of these poles. This result is due to Mittag-Leffler.

17. Given two countably infinite sequences of complex numbers $\{ a _ { k } \} _ { k = 0 } ^ { \infty }$ and $\{ b _ { k } \} _ { k = 0 } ^ { \infty }$ , with lim $\operatorname { 1 } _ { k \to \infty } \left| a _ { k } \right| = \infty$ , it is always possible to find an entire function $F$ that satisfies $F ( a _ { k } ) = b _ { k }$ for all k.

(a) Given n distinct complex numbers $a _ { 1 } , \ldots , a _ { n }$ , and another n complex numbers $b _ { 1 } , \ldots , b _ { n }$ , construct a polynomial $P$ of degree $\leq n - 1$ with

$$
P ( a _ { i } ) = b _ { i } \qquad { \mathrm { f o r ~ } } i = 1 , \ldots , n .
$$

(b) Let $\{ a _ { k } \} _ { k = 0 } ^ { \infty }$ be a sequence of distinct complex numbers such that $a _ { 0 } = 0$ and lim $_ { k  \infty } | a _ { k } | = \infty$ , and let $E ( z )$ denote a Weierstrass product associated with $\{ a _ { k } \}$ . Given complex numbers $\{ b _ { k } \} _ { k = 0 } ^ { \infty }$ , show that there exist integers $m _ { k } \ge 1$ such that the series

$$
F ( z ) = \frac { b _ { 0 } } { E ^ { \prime } ( z ) } \frac { E ( z ) } { z } + \sum _ { k = 1 } ^ { \infty } \frac { b _ { k } } { E ^ { \prime } ( a _ { k } ) } \frac { E ( z ) } { z - a _ { k } } \left( \frac { z } { a _ { k } } \right) ^ { m _ { k } }
$$

defines an entire function that satisfies

$$
F ( a _ { k } ) = b _ { k } \qquad { \mathrm { f o r ~ a l l ~ } } k \geq 0 .
$$

This is known as the Pringsheim interpolation formula.

## 7 Problems

1. Prove that if f is holomorphic in the unit disc, bounded and not identically zero, and $z _ { 1 } , z _ { 2 } , . . . , z _ { n } , . . .$ . are its zeros $\left( \left| z _ { k } \right| < 1 \right)$ , then

$$
\sum _ { n } ( 1 - | z _ { n } | ) < \infty .
$$

[Hint: Use Jensen’s formula.]

2.∗ In this problem, we discuss Blaschke products, which are bounded analogues in the disc of the Weierstrass products for entire functions.

(a) Show that for $0 < | \alpha | < 1$ and $| z | \leq r < 1$ the inequality

$$
\left| \frac { \alpha + | \alpha | z } { ( 1 - \overline { { \alpha } } z ) \alpha } \right| \leq \frac { 1 + r } { 1 - r }
$$

holds.

(b) Let $\left\{ \alpha _ { n } \right\}$ be a sequence in the unit disc such that $\alpha _ { n } \neq 0$ for all n and

$$
\sum _ { n = 1 } ^ { \infty } ( 1 - | \alpha _ { n } | ) < \infty .
$$

Note that this will be the case if $\left\{ \alpha _ { n } \right\}$ are the zeros of a bounded holomorphic function on the unit disc (see Problem 1). Show that the product

$$
f ( z ) = \prod _ { n = 1 } ^ { \infty } { \frac { \alpha _ { n } - z } { 1 - { \overline { { \alpha } } } _ { n } z } } { \frac { | \alpha _ { n } | } { \alpha _ { n } } }
$$

converges uniformly for $| z | \leq r < 1$ , and defines a holomorphic function on the unit disc having precisely the zeros $\alpha _ { n }$ and no other zeros. Show that $| f ( z ) | \leq 1$

3.∗ Show that $\sum \frac { z ^ { n } } { ( n ! ) ^ { \alpha } }$ is an entire function of order $1 / \alpha$

$4 . ^ { * }$ Let $\begin{array} { r } { F ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } } \end{array}$ be an entire function of finite order. Then the growth order of F is intimately linked with the growth of the coefficients $a _ { n }$ as $n \to \infty$ In fact:

(a) Suppose $| F ( z ) | \leq A e ^ { a | z | ^ { \rho } }$ . Then

(8)

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } \left| a _ { n } \right| ^ { 1 / n } n ^ { 1 / \rho } < \infty .
$$

(b) Conversely, if (8) holds, then $| F ( z ) | \le A _ { \epsilon } e ^ { a _ { \epsilon } | z | ^ { \rho + \epsilon } }$ , for every $\epsilon > 0$

[Hint: To prove (a), use Cauchy’s inequality

$$
| a _ { n } | \leq { \frac { A } { r ^ { n } } } e ^ { a r ^ { \rho } } ,
$$

and the fact that the function $u ^ { - n } e ^ { u ^ { \rho } } , \ 0 < u < \rho _ { ; }$ , attains its minimum value $e ^ { n / \rho } ( \rho / n ) ^ { n / \rho }$ at $u = n ^ { 1 / \rho } / \rho ^ { 1 / \rho }$ . Then, choose r in terms of n to achieve this minimum.