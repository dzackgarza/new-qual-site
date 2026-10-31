(c) Let $L ( z ) = - \sigma ^ { \prime } ( z ) / \sigma ( z )$ . Then

$$
L ^ { \prime } ( z ) = { \frac { ( \sigma ^ { \prime } ( z ) ) ^ { 2 } - \sigma ( z ) \sigma ^ { \prime \prime } ( z ) } { ( \sigma ( z ) ) ^ { 2 } } } = \wp ( z ) .
$$

6. Prove that $\wp ^ { \prime \prime }$ is a quadratic polynomial in $\wp$ .

7. Setting $\tau = 1 / 2$ in the expression

$$
\sum _ { m = - \infty } ^ { \infty } \frac { 1 } { ( m + \tau ) ^ { 2 } } = \frac { \pi ^ { 2 } } { \sin ^ { 2 } ( \pi \tau ) } ,
$$

deduce that

$$
\sum _ { m \geq 1 , \ m { \mathrm { ~ o d d } } } { \frac { 1 } { m ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 8 } } \ a \mathrm { n d } \ \sum _ { m \geq 1 } { \frac { 1 } { m ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 6 } } = \zeta ( 2 ) .
$$

Similarly, using $\textstyle \sum { 1 / ( m + \tau ) ^ { 4 } }$ deduce that

$$
\sum _ { m \geq 1 , \ m { \mathrm { ~ o d d } } } { \frac { 1 } { m ^ { 4 } } } = { \frac { \pi ^ { 4 } } { 9 6 } } \ a \mathrm { n d } \ \sum _ { m \geq 1 } { \frac { 1 } { m ^ { 4 } } } = { \frac { \pi ^ { 4 } } { 9 0 } } = \zeta ( 4 ) .
$$

These results were already obtained using Fourier series in the exercises at the end of Chapters 2 and 3 in Book I.

8. Let

$$
E _ { 4 } ( \tau ) = \sum _ { ( n , m ) \neq ( 0 , 0 ) } \frac { 1 } { ( n + m \tau ) ^ { 4 } }
$$

be the Eisenstein series of order 4.

(a) Show that $E _ { 4 } ( \tau ) \to \pi ^ { 4 } / 4 5 { \mathrm { ~ a s ~ I m } } ( \tau ) \to \infty$

(b) More precisely,

$$
\left| E _ { 4 } ( \tau ) - { \frac { \pi ^ { 4 } } { 4 5 } } \right| \leq c e ^ { - 2 \pi t } \quad { \mathrm { ~ i f ~ } } \tau = x + i t { \mathrm { ~ a n d ~ } } t \geq 1 .
$$

(c) Deduce that

$$
\Bigl | E _ { 4 } ( \tau ) - \tau ^ { - 4 } { \frac { \pi ^ { 4 } } { 4 5 } } \Bigr | \le c t ^ { - 4 } e ^ { - 2 \pi / t } ~ \mathrm { i f } ~ \tau = i t ~ \mathrm { a n d } ~ 0 < t \le 1 .
$$

## 4 Problems

1. Besides the approach in Section 1.2, there are several alternate ways of dealing with the sum $\textstyle \sum { 1 } / ( z + \omega ) ^ { 2 }$ , where $\omega = n + m \tau$ . For example, one may sum either (a) circularly, (b) first in n then in m, (c) or first in m then in n.

(a) Prove that ${ \mathrm { i f ~ } } z \notin \Lambda$ , then

$$
\operatorname * { l i m } _ { R  \infty } \sum _ { n ^ { 2 } + m ^ { 2 } \leq R ^ { 2 } } \frac { 1 } { ( z + n + m \tau ) ^ { 2 } } = S _ { 1 } ( z )
$$

exists and $S _ { 1 } ( z ) = \wp ( z ) + c _ { 1 }$

(b) Similarly,

$$
\sum _ { m } \left( \sum _ { n } { \frac { 1 } { ( z + n + m \tau ) ^ { 2 } } } \right) = S _ { 2 } ( z )
$$

exists and $S _ { 2 } ( z ) = \wp ( z ) + c _ { 2 } , { \mathrm { w h e r e ~ } } c _ { 2 } = F ( \tau )$ , and F is the forbidden Eisenstein series.

(c) Also

$$
\sum _ { n } \left( \sum _ { m } { \frac { 1 } { ( z + n + m \tau ) ^ { 2 } } } \right) = S _ { 3 } ( z )
$$

exists with $S _ { 3 } ( z ) = \wp ( z ) + c _ { 3 }$ , and $c _ { 3 } = \tilde { F } ( \tau )$ , the reverse of $F ,$

[Hint: To prove (a), it suffices to show that lim $. R { \longrightarrow } \infty$ $\sum { \begin{array} { r l } \end{array} } \quad 1 / ( n + m \tau ) ^ { 2 } = c _ { 1 }$ $1 \leq n ^ { 2 } + m ^ { 2 } \leq R ^ { 2 }$ exists. This is proved by a comparision with $\begin{array} { r } { \int _ { 1 \leq x ^ { 2 } + y ^ { 2 } \leq R ^ { 2 } } \frac { d x } { ( x + y \tau ) ^ { 2 } } = I ( R ) } \end{array}$ . It can be shown that $I ( R ) = 0$ , which follows because $( \overline { { x } } + y \tau ) ^ { - 2 } = - ( \partial / \partial x ) ( x + y \tau ) ^ { - 1 } . ]$

## 2. Show that

$$
\wp ( z ) = c + \pi ^ { 2 } \sum _ { m = - \infty } ^ { \infty } { \frac { 1 } { \sin ^ { 2 } ( ( z + m \tau ) \pi ) } }
$$

where c is an appropriate constant. In fact, by part (b) of the previous problem $c = - F ( \tau )$

3.∗ Suppose Ω is a simply connected domain that excludes the three roots of the polynomial $4 z ^ { 3 } - g _ { 2 } z - g _ { 3 }$ . For $\omega _ { 0 } \in \Omega$ and $\omega _ { 0 }$ fixed, define the function I on Ω by

$$
I ( \omega ) = \int _ { \omega _ { 0 } } ^ { \omega } \frac { d z } { \sqrt { 4 z ^ { 3 } - g _ { 2 } z - g _ { 3 } } } ~ \omega \in \Omega .
$$

Then the function I has an inverse given by $\wp ( z + \alpha )$ for some constant $\alpha ;$ that is,

$$
I ( \wp ( z + \alpha ) ) = z
$$

for appropriate $\alpha .$

[Hint: Prove that $( I ( \wp ( z + \alpha ) ) ) ^ { \prime } = \pm 1$ , and use the fact that $\wp$ is even.]

$^ { 4 , { ^ * } }$ Suppose $\tau$ is purely imaginary, say $\tau = i t$ with $t > 0$ Consider the division of the complex plane into congruent rectangles obtained by considering the lines $x = n / 2 , y = t m / 2$ as n and m range over the integers. (An example is the rectangle whose vertices are $0 , 1 / 2 , 1 / 2 + \tau / 2$ , and $\tau / 2 . )$

(a) Show that $\wp$ is real-valued on all these lines, and hence on the boundaries of all these rectangles.

(b) Prove that ℘ maps the interior of each rectangle conformally to the upper (or lower) half-plane.