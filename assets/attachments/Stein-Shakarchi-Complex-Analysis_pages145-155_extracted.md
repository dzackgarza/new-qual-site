and note that $F$ is bounded by 1 on the positive real and positive imaginary axes. Since we also have $| F ( z ) | \le C e ^ { c | z | }$ in the quadrant, we conclude by the Phragm´en-Lindel¨of theorem that $| F ( z ) | \le 1$ for ${ \mathrm { a l l ~ } } z { \mathrm { ~ i n ~ } } Q .$ which implies $| f ( z ) | \leq e ^ { 2 \pi M y }$ . A similar argument for the other quadrants concludes Step 3 as well as the proof of the Paley-Wiener theorem.

We conclude with another version of the idea behind the Paley-Wiener theorem, this time characterizing the functions whose Fourier transform vanishes for all negative ξ.

Theorem 3.5 Suppose f and $\hat { f }$ have moderate decrease. Then ${ \hat { f } } ( \xi ) =$ 0 for all $\xi < 0$ if and only if f can be extended to a continuous and bounded function in the closed upper half-plane $\left\{ z = x + i y : y \ge 0 \right\}$ with f holomorphic in the interior.

Proof. First assume ${ \hat { f } } ( \xi ) = 0$ for $\xi < 0$ . By the Fourier inversion formula

$$
f ( x ) = \int _ { 0 } ^ { \infty } { \hat { f } } ( \xi ) e ^ { 2 \pi i x \xi } d \xi ,
$$

and we can extend f when $z = x + i y$ with $y \geq 0$ by

$$
f ( z ) = \int _ { 0 } ^ { \infty } { \hat { f } } ( \xi ) e ^ { 2 \pi i z \xi } d \xi .
$$

Notice that the integral converges and that

$$
| f ( z ) | \leq A \int _ { 0 } ^ { \infty } \frac { d \xi } { 1 + \xi ^ { 2 } } < \infty ,
$$

which proves the boundedness of $f .$ The uniform convergence of

$$
f _ { n } ( z ) = \int _ { 0 } ^ { n } { \hat { f } } ( \xi ) e ^ { 2 \pi i x \xi } d \xi
$$

to $f ( z )$ in the closed half-plane establishes the continuity of $f$ there, and its holomorphicity in the interior.

For the converse, we argue in the spirit of the proof of Theorem 3.3. For ǫ and $\delta$ positive, we set

$$
f _ { \epsilon , \delta } ( z ) = \frac { f ( z + i \delta ) } { ( 1 - i \epsilon z ) ^ { 2 } } .
$$

Then $f _ { \epsilon , \delta }$ is holomorphic in a region containing the closed upper halfplane. One also shows as before, using Cauchy’s theorem, that $\widehat { f _ { \epsilon , \delta } } ( \xi ) = 0$ for all $\xi < 0$ . Then, passing to the limit successively, one has $\widehat { f _ { \epsilon , 0 } } ( \xi ) = 0$ for $\xi < 0$ , and finally ${ \hat { f } } ( \xi ) = { \widehat { f _ { 0 , 0 } } } ( \xi ) = 0$ for all $\xi < 0$

Remark. The reader should note a certain analogy between the above theorem and Theorem 7.1 in Chapter 3. Here we are dealing with a function holomorphic in the upper half-plane, and there with a function holomorphic in a disc. In the present case the Fourier transform vanishes when $\xi < 0$ , and in the earlier case, the Fourier coefficients vanish when $n < 0$

## 4 Exercises

1. Suppose f is continuous and of moderate decrease, and ${ \hat { f } } ( \xi ) = 0$ for all $\xi \in \mathbb { R }$ Show that $f = 0$ by completing the following outline:

(a) For each fixed real number t consider the two functions

$$
A ( z ) = \int _ { - \infty } ^ { t } f ( x ) e ^ { - 2 \pi i z ( x - t ) } d x \quad { \mathrm { ~ a n d ~ } } \quad B ( z ) = - \int _ { t } ^ { \infty } f ( x ) e ^ { - 2 \pi i z ( x - t ) } d x .
$$

Show that $A ( \xi ) = B ( \xi )$ for all $\xi \in \mathbb { R } .$

(b) Prove that the function F equal to A in the closed upper half-plane, and B in the lower half-plane, is entire and bounded, thus constant. In fact, show that $F = 0$

(c) Deduce that

$$
\int _ { - \infty } ^ { t } f ( x ) d x = 0 ,
$$

for all t, and conclude that $f = 0$

2. If $f \in \mathfrak { F } _ { o }$ with $a > 0$ , then for any positive integer n one has $f ^ { ( n ) } \in \mathfrak { F } _ { b }$ whenever $0 \leq b < a$

[Hint: Modify the solution to Exercise 8 in Chapter 2.]

3. Show, by contour integration, that if $a > 0$ and $\xi \in \mathbb { R }$ then

$$
{ \frac { 1 } { \pi } } \int _ { - \infty } ^ { \infty } { \frac { a } { a ^ { 2 } + x ^ { 2 } } } e ^ { - 2 \pi i x \xi } d x = e ^ { - 2 \pi a | \xi | } ,
$$

and check that

$$
\int _ { - \infty } ^ { \infty } e ^ { - 2 \pi a | \xi | } e ^ { 2 \pi i \xi x } d \xi = \frac { 1 } { \pi } \frac { a } { a ^ { 2 } + x ^ { 2 } } .
$$

4. Suppose $Q$ is a polynomial of degree $\geq 2$ with distinct roots, none lying on the real axis. Calculate

$$
\int _ { - \infty } ^ { \infty } { \frac { e ^ { - 2 \pi i x \xi } } { Q ( x ) } } d x , \xi \in \mathbb { R }
$$

in terms of the roots of $Q$ . What happens when several roots coincide? [Hint: Consider separately the cases $\xi < 0 , \xi = 0$ , and $\xi > 0$ . Use residues.]

5. More generally, let $R ( x ) = P ( x ) / Q ( x )$ be a rational function with (degree $Q ) \geq$ (degreeP )+2 and $Q ( x ) \neq 0$ on the real axis.

(a) Prove that if $\alpha _ { 1 } , \ldots , \alpha _ { k }$ are the roots of R in the upper half-plane, then there exists polynomials $P _ { j } ( \boldsymbol { \xi } )$ of degree less than the multiplicity of $\alpha _ { j }$ so that

$$
\int _ { - \infty } ^ { \infty } R ( x ) e ^ { - 2 \pi i x \xi } d x = \sum _ { j = 1 } ^ { k } P _ { j } ( \xi ) e ^ { - 2 \pi i \alpha _ { j } \xi } , \qquad { \mathrm { w h e n ~ } } \xi < 0 .
$$

(b) In particular, if $Q ( z )$ has no zeros in the upper half-plane, then $\begin{array} { r } { \int _ { - \infty } ^ { \infty } R ( x ) e ^ { - 2 \pi i x \xi } \dot { d x } = 0 } \end{array}$ for $\xi < 0 .$

(c) Show that similar results hold in the case $\xi > 0$

(d) Show that

$$
\int _ { - \infty } ^ { \infty } R ( x ) e ^ { - 2 \pi i x \xi } d x = O ( e ^ { - a | \xi | } ) , \xi \in \mathbb { R }
$$

as $| \xi | \to \infty$ for some $a > 0$ . Determine the best possible $a \mathrm { { s } }$ in terms of the roots of R.

[Hint: For part (a), use residues. The powers of $\xi$ appear when one differentiates the function $f ( z ) = R ( z ) e ^ { - 2 \pi i z \xi }$ (as in the formula of Theorem 1.4 in the previous chapter). For part (c) argue in the lower half-plane.]

6. Prove that

$$
\frac { 1 } { \pi } \sum _ { n = - \infty } ^ { \infty } \frac { a } { a ^ { 2 } + n ^ { 2 } } = \sum _ { n = - \infty } ^ { \infty } e ^ { - 2 \pi a | n | }
$$

whenever $a > 0$ . Hence show that the sum equals coth $\pi a$

7. The Poisson summation formula applied to specific examples often provides interesting identities.

(a) Let $\tau$ be fixed with $\operatorname { I m } ( \tau ) > 0$ . Apply the Poisson summation formula to

$$
f ( z ) = ( \tau + z ) ^ { - k } ,
$$

where k is an integer $\geq 2 .$ , to obtain

$$
\sum _ { n = - \infty } ^ { \infty } \frac { 1 } { ( \tau + n ) ^ { k } } = \frac { ( - 2 \pi i ) ^ { k } } { ( k - 1 ) ! } \sum _ { m = 1 } ^ { \infty } m ^ { k - 1 } e ^ { 2 \pi i m \tau } .
$$

(b) Set $k = 2$ in the above formula to show that if $\operatorname { I m } ( \tau ) > 0$ , then

$$
\sum _ { n = - \infty } ^ { \infty } \frac { 1 } { ( \tau + n ) ^ { 2 } } = \frac { \pi ^ { 2 } } { \sin ^ { 2 } ( \pi \tau ) } .
$$

(c) Can one conclude that the above formula holds true whenever $\tau$ is any complex number that is not an integer?

[Hint: For (a), use residues to prove that $\hat { f } ( \xi ) = 0 , \mathrm { i f } \ \xi < 0$ , and

$$
\hat { f } ( \xi ) = \frac { ( - 2 \pi i ) ^ { k } } { ( k - 1 ) ! } \xi ^ { k - 1 } e ^ { 2 \pi i \xi \tau } , ~ \mathrm { w h e n } ~ \xi > 0 . ]
$$

8. Suppose $\hat { f }$ has compact support contained in $[ - M , M ]$ and let $\begin{array} { r } { f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } } \end{array}$ Show that

$$
a _ { n } = { \frac { ( 2 \pi i ) ^ { n } } { n ! } } \int _ { - M } ^ { M } { \hat { f } } ( \xi ) \xi ^ { n } d \xi ,
$$

and as a result

$$
\operatorname* { l i m } _ { n \to \infty } ( n ! | a _ { n } | ) ^ { 1 / n } \leq 2 \pi M .
$$

In the converse direction, let f be any power series $\textstyle f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ with lim $\begin{array} { r } { \operatorname* { s u p } _ { n \to \infty } ( n ! | a _ { n } | ) ^ { 1 / n } \leq 2 \pi M } \end{array}$ Then, f is holomorphic in the complex plane, and for every $\epsilon > 0$ there exists $A _ { \epsilon } > 0$ such that

$$
\left. f ( z ) \right. \le A _ { \epsilon } e ^ { 2 \pi ( M + \epsilon ) \left. z \right. } .
$$

9. Here are further results similar to the Phragm´en-Lindel¨of theorem.

(a) Let F be a holomorphic function in the right half-plane that extends continuously to the boundary, that is, the imaginary axis. Suppose that $| F ( i y ) | \le 1$ for all $y \in \mathbb { R }$ , and

$$
| F ( z ) | \le C e ^ { c | z | ^ { \gamma } }
$$

for some $c , C > 0$ and $\gamma < 1$ . Prove that $| F ( z ) | \le 1$ for all z in the right half-plane.

(b) More generally, let S be a sector whose vertex is the origin, and forming an angle of $\pi / \beta$ . Let $F$ be a holomorphic function in S that is continuous on the closure of S, so that $| F ( z ) | \le 1$ on the boundary of S and

$$
| F ( z ) | \leq C e ^ { c | z | ^ { \alpha } } { \mathrm { f o r ~ a l l ~ } } z \in S
$$

for some $c , C > 0$ and $0 < \alpha < \beta$ . Prove that $| F ( z ) | \le 1$ for all $z \in S$

10. This exercise generalizes some of the properties of $e ^ { - \pi x ^ { 2 } }$ related to the fact that it is its own Fourier transform.

Suppose $f ( z )$ is an entire function that satisfies

$$
| f ( x + i y ) | \leq c e ^ { - a x ^ { 2 } + b y ^ { 2 } }
$$

for some $a , b , c > 0$ . Let

$$
{ \hat { f } } ( \zeta ) = \int _ { - \infty } ^ { \infty } f ( x ) e ^ { - 2 \pi i x \zeta } d x .
$$

Then, $\hat { f }$ is an entire function of ζ that satisfies

$$
| \hat { f } ( \xi + i \eta ) | \le c ^ { \prime } e ^ { - a ^ { \prime } \xi ^ { 2 } + b ^ { \prime } \eta ^ { 2 } }
$$

for some $a ^ { \prime } , b ^ { \prime } , c ^ { \prime } > 0$

[Hint: To prove $\hat { f } ( \xi ) = O ( e ^ { - a ^ { \prime } \xi ^ { 2 } } )$ , assume $\xi > 0$ and change the contour of integration to $x - i y$ for some $y > 0$ fixed, and $- \infty < x < \infty$ . Then

$$
\hat { f } ( \xi ) = O ( e ^ { - 2 \pi y \xi } e ^ { b y ^ { 2 } } ) .
$$

Finally, choose $y = d \xi$ where d is a small constant.]

11. One can give a neater formulation of the result in Exercise 10 by proving the following fact.

Suppose $f ( z )$ is an entire function of strict order 2, that is,

$$
f ( z ) = O ( e ^ { c _ { 1 } | z | ^ { 2 } } )
$$

for some $c _ { 1 } > 0$ . Suppose also that for x real,

$$
f ( x ) = O ( e ^ { - c _ { 2 } | x | ^ { 2 } } )
$$

for some $c _ { 2 } > 0$ . Then

$$
| f ( x + i y ) | = O ( e ^ { - a x ^ { 2 } + b y ^ { 2 } } )
$$

for some $a , b > 0$ . The converse is obviously true.

12. The principle that a function and its Fourier transform cannot both be too small at infinity is illustrated by the following theorem of Hardy.

If $f$ is a function on R that satisfies

$$
f ( x ) = O ( e ^ { - \pi x ^ { 2 } } ) \mathrm { a n d } \hat { f } ( \xi ) = O ( e ^ { - \pi \xi ^ { 2 } } ) ,
$$

then f is a constant multiple of $e ^ { - \pi x ^ { 2 } }$ . As a result, if $f ( x ) = O ( e ^ { - \pi A x ^ { 2 } } )$ , and $\hat { f } ( \xi ) = O ( e ^ { - \pi B \xi ^ { 2 } } )$ , with $A B > 1$ and $A , B > 0$ , then f is identically zero.

(a) If f is even, show that $\hat { f }$ extends to an even entire function. Moreover, if $g ( \dot { z } ) = \hat { f } ( z ^ { 1 / 2 } )$ , then g satisfies

$$
| g ( x ) | \leq c e ^ { - \pi x } \mathrm { a n d } | g ( z ) | \leq c e ^ { \pi R \sin ^ { 2 } ( \theta / 2 ) } \leq c e ^ { \pi | z | }
$$

when $x \in \mathbb { R }$ and $z = R e ^ { i \theta }$ with $R \geq 0$ and $\theta \in \mathbb { R }$

(b) Apply the Phragm´en-Lindel¨of principle to the function

$$
F ( z ) = g ( z ) e ^ { \gamma z } \quad { \mathrm { ~ w h e r e ~ } } \gamma = i \pi { \frac { e ^ { - i \pi / ( 2 \beta ) } } { \sin \pi / ( 2 \beta ) } }
$$

and the sector $0 \leq \theta \leq \pi / \beta < \pi$ , and let $\beta \to \pi$ to deduce that $e ^ { \pi z } g ( z )$ is bounded in the closed upper half-plane. The same result holds in the lower half-plane, so by Liouville’s theorem $e ^ { \pi z } g ( z )$ is constant, as desired.

(c) If f is odd, then ${ \hat { f } } ( 0 ) = 0$ , and apply the above argument to $\hat { f } ( z ) / z$ to deduce that $\boldsymbol { f } = \boldsymbol { \hat { f } } = 0$ . Finally, write an arbitrary $f$ as an appropriate sum of an even function and an odd function.

## 5 Problems

1. Suppose ${ \hat { f } } ( \xi ) = O ( e ^ { - a | \xi | ^ { p } } )$ as $| \xi | \to \infty$ , for some $p > 1$ . Then f is holomorphic for all z and satisfies the growth condition

$$
| f ( z ) | \leq A e ^ { a | z | ^ { q } }
$$

where $1 / p + 1 / q = 1$

Note that on the one hand, when $p \longrightarrow \infty$ then $q \to 1$ , and this limiting case can be interpreted as part of Theorem 3.3. On the other hand, when $p \to 1$ then $q \to \infty$ , and this limiting case in a sense brings us back to Theorem 2.1.

[Hint: To prove the result, use the inequality $- \xi ^ { p } + \xi u \le u ^ { q }$ , which is valid when ξ and u are non-negative. To establish this inequality, examine separately the cases $\xi ^ { p } \ge \xi u$ and $\xi ^ { p } < \xi u ;$ note also that the functions $\xi = u ^ { q - 1 }$ and $u = \xi ^ { p - 1 }$ are inverses of each other because $( p - 1 ) ( q - 1 ) = 1 . ]$

2. The problem is to solve the differential equation

$$
a _ { n } { \frac { d ^ { n } } { d t ^ { n } } } u ( t ) + a _ { n - 1 } { \frac { d ^ { n - 1 } } { d t ^ { n - 1 } } } u ( t ) + \cdot \cdot \cdot + a _ { 0 } u ( t ) = f ( t ) ,
$$

where $a _ { 0 } , a _ { 1 } , \ldots , a _ { n }$ are complex constants, and $f$ is a given function. Here we suppose that f has bounded support and is smooth (say of class $C ^ { 2 } )$

(a) Let

$$
{ \hat { f } } ( z ) = \int _ { - \infty } ^ { \infty } f ( t ) e ^ { - 2 \pi i z t } d t .
$$

Observe that $\hat { f }$ is an entire function, and using integration by parts show that

$$
| \hat { f } ( x + i y ) | \leq \frac { A } { 1 + x ^ { 2 } }
$$

if $| y | \le a$ for any fixed $a \geq 0$

(b) Write

$$
P ( z ) = a _ { n } ( 2 \pi i z ) ^ { n } + a _ { n - 1 } ( 2 \pi i z ) ^ { n - 1 } + \cdot \cdot \cdot + a _ { 0 } .
$$

Find a real number c so that $P ( z )$ does not vanish on the line

$$
L = \{ z : z = x + i c , x \in \mathbb { R } \} .
$$

(c) Set

$$
u ( t ) = \int _ { L } { \frac { e ^ { 2 \pi i z t } } { P ( z ) } } { \hat { f } } ( z ) d z .
$$

Check that

$$
\sum _ { j = 0 } ^ { n } a _ { j } \left( { \frac { d } { d t } } \right) ^ { j } u ( t ) = \int _ { L } e ^ { 2 \pi i z t } { \hat { f } } ( z ) d z
$$

and

$$
\int _ { L } e ^ { 2 \pi i z t } { \hat { f } } ( z ) d z = \int _ { - \infty } ^ { \infty } e ^ { 2 \pi i x t } { \hat { f } } ( x ) d x .
$$

Conclude by the Fourier inversion theorem that

$$
\sum _ { j = 0 } ^ { n } a _ { j } \left( { \frac { d } { d t } } \right) ^ { j } u ( t ) = f ( t ) .
$$

Note that the solution u depends on the choice $c .$

3.∗ In this problem, we investigate the behavior of certain bounded holomorphic functions in an infinite strip. The particular result described here is sometimes called the three-lines lemma.

(a) Suppose $F ( z )$ is holomorphic and bounded in the strip $0 < \mathrm { I m } ( z ) < 1$ and continuous on its closure. If $| F ( z ) | \le 1$ on the boundary lines, then $| F ( z ) | \le 1$ throughout the strip.

(b) For the more general $F ,$ , let $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathbb { R } } \ | F ( x ) | = M _ { 0 } } \end{array}$ and $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathbb { R } } \ | F ( x + i ) | = } \end{array}$ $M _ { 1 }$ . Then,

$$
\operatorname* { s u p } _ { x \in \mathbb { R } } | F ( x + i y ) | \leq M _ { 0 } ^ { 1 - y } M _ { 1 } ^ { y } , \quad \mathrm { ~ i f ~ } 0 \leq y \leq 1 .
$$

(c) As a consequence, prove that log $\textstyle \operatorname* { s u p } _ { x \in \mathbb { R } } \ | F ( x + i y ) |$ is a convex function of y when $0 \leq y \leq 1$

[Hint: For part (a), apply the maximum modulus principle to $F _ { \epsilon } ( z ) = F ( z ) e ^ { - \epsilon z ^ { 2 } }$ For part (b), consider $M _ { 0 } ^ { z - 1 } M _ { 1 } ^ { - z } F ( z ) . ]$

4.∗ There is a relation between the Paley-Wiener theorem and an earlier representation due to E. Borel.

(a) A function $f ( z )$ , holomorphic for all z, satisfies $| f ( z ) | \leq A _ { \epsilon } e ^ { 2 \pi ( M + \epsilon ) | z | }$ for all ǫ if and only if it is representable in the form

$$
f ( z ) = \int _ { C } e ^ { 2 \pi i z w } g ( w ) d w
$$

where $g$ is holomorphic outside the circle of radius M centered at the origin, and g vanishes at infinity. Here C is any circle centered at the origin of radius larger than M . In fact, if $f ( z ) = \sum a _ { n } z ^ { n }$ , then $\begin{array} { r } { g ( w ) = \sum _ { n = 0 } ^ { \infty } A _ { n } w ^ { - n - 1 } } \end{array}$ with $a _ { n } = A _ { n } ( 2 \pi i ) ^ { n + 1 } / n !$

(b) The connection with Theorem 3.3 is as follows. For these functions $f$ (for which in addition f and ˆf are of moderate decrease on the real axis), one can assert that the g above is holomorphic in the larger region, which consists of the slit plane $\mathbb { C } - [ - M , M ]$ . Moreover, the relation between g and the Fourier transform $\hat { f }$ is

$$
g ( z ) = { \frac { 1 } { 2 \pi i } } \int _ { - M } ^ { M } { \frac { { \hat { f } } ( \xi ) } { \xi - z } } d \xi
$$

so that $\hat { f }$ represents the jump of g across the segment $[ - M , M ]$ ; that is,

$$
\hat { f } ( x ) = \operatorname * { l i m } _ { \epsilon  0 , \epsilon > 0 } g ( x + i \epsilon ) - g ( x - i \epsilon ) .
$$

See Problem 5 in Chapter 3.

...but after the $1 5 ^ { \mathrm { t h } }$ of October I felt myself a free man, with such longing for mathematical work, that the last two months flew by quickly, and that only today I found the letter of the $1 9 ^ { \mathrm { t h } }$ of October that I had not answered. The result of my work, with which I am not entirely satisfied, I want to share with you.

Firstly, in looking back at my lectures, a gap in function theory needed to be filled. As you know, up to now the following question had been unresolved. Given an arbitrary sequence of complex numbers, $a _ { 1 } , a _ { 2 } , \dotsc$ , can one construct an entire (transcendental) function that vanishes at these values, with prescribed multiplicities, and nowhere else?...

K. Weierstrass, 1874

In this chapter, we will study functions that are holomorphic in the whole complex plane; these are called entire functions. Our presentation will be organized around the following three questions:

1. Where can such functions vanish? We shall see that the obvious necessary condition is also sufficient: if $\left\{ z _ { n } \right\}$ is any sequence of complex numbers having no limit point in C, then there exists an entire function vanishing exactly at the points of this sequence. The construction of the desired function is inspired by Euler’s product formula for sin $\pi z$ (the prototypical case when $\left\{ z _ { n } \right\}$ is $\mathbb { Z } )$ , but requires an additional refinement: the Weierstrass canonical factors.

2. How do these functions grow at infinity? Here, matters are controlled by an important principle: the larger a function is, the more zeros it can have. This principle already manifests itself in the simple case of polynomials. By the fundamental theorem of algebra, the number of zeros of a polynomial P of degree d is precisely d, which is also the exponent in the order of (polynomial) growth of $P ,$ , namely

$$
\operatorname* { s u p } _ { | z | = R } | P ( z ) | \approx R ^ { d } \quad { \mathrm { ~ a s ~ } } R \to \infty .
$$

A precise version of this general principle is contained in Jensen’s formula, which we prove in the first section. This formula, central to much of the theory developed in this chapter, exhibits a deep connection between the number of zeros of a function in a disc and the (logarithmic) average of the function over the circle. In fact, Jensen’s formula not only constitutes a natural starting point for us, but also leads to the fruitful theory of value distributions, also called Nevanlinna theory (which, however, we do not take up here).

3. To what extent are these functions determined by their zeros? It turns out that if an entire function has a finite (exponential) order of growth, then it can be specified by its zeros up to multiplication by a simple factor. The precise version of this assertion is the Hadamard factorization theorem. It may be viewed as another instance of the general rule that was formulated in Chapter 3, that is, that under appropriate conditions, a holomorphic function is essentially determined by its zeros.

## 1 Jensen’s formula

In this section, we denote by $D _ { R }$ and $C _ { R }$ the open disc and circle of radius R centered at the origin. We shall also, in the rest of this chapter, exclude the trivial case of the function that vanishes identically.

Theorem 1.1 Let Ω be an open set that contains the closure of a disc $D _ { R }$ and suppose that f is holomorphic in Ω, $f ( 0 ) \neq 0$ , and f vanishes nowhere on the circle $C _ { R }$ $I f z _ { 1 } , \dots , z _ { N }$ denote the zeros of f inside the disc (counted with multiplicities),1 then

$$
\log | f ( 0 ) | = \sum _ { k = 1 } ^ { N } \log \left( \frac { | z _ { k } | } { R } \right) + \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log | f ( R e ^ { i \theta } ) | d \theta .\tag{1}
$$

The proof of the theorem consists of several steps.

Step 1. First, we observe that if $f _ { 1 }$ and $f _ { 2 }$ are two functions satisfying the hypotheses and the conclusion of the theorem, then the product $f _ { 1 } f _ { 2 }$ also satisfies the hypothesis of the theorem and formula (1). This observation is a simple consequence of the fact that log xy = log x + log y whenever x and $y$ are positive numbers, and that the set of zeros of $f _ { 1 } f _ { 2 }$ is the union of the sets of zeros of $f _ { 1 }$ and $f _ { 2 }$

Step 2. The function

$$
g ( z ) = { \frac { f ( z ) } { ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { N } ) } }
$$

initially defined on $\Omega - \{ z _ { 1 } , \dots , z _ { N } \}$ , is bounded near each $z _ { j }$ . Therefore each $z _ { j }$ is a removable singularity, and hence we can write

$$
f ( z ) = ( z - z _ { 1 } ) \cdot \cdot \cdot ( z - z _ { N } ) g ( z )
$$

where $g$ is holomorphic in Ω and nowhere vanishing in the closure of $D _ { R }$ By Step 1, it suffices to prove Jensen’s formula for functions like $g$ that vanish nowhere, and for functions of the form $z - z _ { j }$

Step 3. We first prove (1) for a function g that vanishes nowhere in the closure of $D _ { R }$ . More precisely, we must establish the following identity:

$$
\log | g ( 0 ) | = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log | g ( R e ^ { i \theta } ) | d \theta .
$$

In a slightly larger disc, we can write $g ( z ) = e ^ { h ( z ) }$ where h is holomorphic in that disc. This is possible since discs are simply connected, and we can define $h = \log g$ (see Theorem 6.2 in Chapter 3). Now we observe that

$$
| g ( z ) | = | e ^ { h ( z ) } | = | e ^ { \mathrm { R e } ( h ( z ) ) + i \mathrm { I m } ( h ( z ) ) } | = e ^ { \mathrm { R e } ( h ( z ) ) } ,
$$

so that log $| g ( z ) | = \operatorname { R e } ( h ( z ) )$ . The mean value property (Corollary 7.3 in Chapter 3) then immediately implies the desired formula for g.

Step 4. The last step is to prove the formula for functions of the form $f ( z ) = z - w$ , where $w \in D _ { R }$ . That is, we must show that

$$
\log | w | = \log \left( { \frac { | w | } { R } } \right) + { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log | R e ^ { i \theta } - w | d \theta .
$$

Since log $( | w | / R ) { = } \log | w | { - } \log R$ and log $\left| R e ^ { i \theta } - w \right| { = } \log R { + } \log \left| e ^ { i \theta } - w / R \right|$ it suffices to prove that

$$
\int _ { 0 } ^ { 2 \pi } \log \left| e ^ { i \theta } - a \right| d \theta = 0 , \quad { \mathrm { ~ w h e n e v e r ~ } } | a | < 1 .
$$

This in turn is equivalent (after the change of variables $\theta \mapsto - \theta )$ to

$$
\int _ { 0 } ^ { 2 \pi } \log | 1 - a e ^ { i \theta } | d \theta = 0 , ~ \mathrm { w h e n e v e r } ~ | a | < 1 .
$$