## 13.4.13 Spring 20202 HW 3 # 3.8.9

Show that

$$
\int _ { 0 } ^ { 1 } \log ( \sin \pi x ) d x = - \log 2 .
$$

<!-- image-->  
Figure 9. Contour in Exercise 9

## 13.4.14 Spring 20202 HW 3 # 3.8.10

Show that if $a > 0$ , then

$$
\int _ { 0 } ^ { \infty } { \frac { \log x } { x ^ { 2 } + a ^ { 2 } } } d x = { \frac { \pi } { 2 a } } \log a .
$$

<!-- image-->

## 13.4.15 Spring 20202 HW 3 # 6

a. Show (without using 3.8.9 in the S&S) that

$$
\int _ { 0 } ^ { 2 \pi } \log \left| 1 - e ^ { i \theta } \right| d \theta = 0
$$

b. Show that this identity is equivalent to S&S 3.8.9:

$$
\int _ { 0 } ^ { 1 } \log ( \sin ( \pi x ) ) \ d x = - \log 2 .
$$

## 13.4.16 Spring 20202 HW 3 # 7

Let $0 < a <$ 4 and evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { \alpha - 1 } } { 1 + x ^ { 3 } } } d x
$$

## 13.4.17 Spring 20202 HW 3 # 10

For $a > 0$ , evaluate

$$
\int _ { 0 } ^ { \pi / 2 } { \frac { d \theta } { a + \sin ^ { 2 } \theta } }
$$

## 14 Conformal Maps (8155c)

Notation: D is the open unit disc, H is the open upper half-plane.

<!-- image-->

<!-- image-->

Find a conformal map from D to H.

<!-- image-->

## 14.2 2

<!-- image-->

Find a conformal map from the strip $\left\{ z \in \mathbb { C } \Big \vert 0 < \Im ( z ) < 1 \right\}$ to H.

## 14.3 3

Find a fractional linear transformation T which maps H to D, and explicitly describe the image of the first quadrant under T .

## 14.4 4

Find a conformal map from $\left\{ z \in \mathbb { C } \Big \vert | z - i | > 1 , \Re ( z ) > 0 \right\}$ to H.

## 14.5 5

Find a conformal map from $\{ z \in \mathbb { C } \ \middle \vert \ \vert z \vert < 1 , \middle \vert z - \frac { 1 } { 2 }  > \frac { 1 } { 2 } \}$ to D.

14.6 6

Find a conformal map from $\left\{ \left| z - 1 \right| < 2 \right\} \cap \left\{ \left| z + 1 \right| < 2 \right\}$ to H.

## 14.7 7

Let Ω be the region inside the unit circle |z| = 1 and outside the circle $\left| z - { \frac { 1 } { 4 } } \right| = { \frac { 1 } { 4 } } .$

Find an injective conformal map from Ω onto some annulus $\{ r < | z | < 1 \}$ for constant r.

## 14.8 8

Let D be the region obtained by deleting the real interval [0, 1) from D; find a conformal map from D to D.

## 14.9 9

Find a conformal map from $\mathbb { C } \setminus \left\{ x \in \mathbb { R } \ \middle | \ x \leq 0 \right\}$ to D.

14.10 10

Find a conformal map from $\mathbb { C } \setminus \left\{ x \in \mathbb { R } \ \middle | \ x \geq 1 \right\}$ to D.

<!-- image-->

## 14.11 11

Find a bijective conformal map from G to H, where

$$
G : = \left\{ z \in \mathbb { C } \Big \vert | z - 1 | < \sqrt { 2 } , | z + 1 | < \sqrt { 2 } \right\} \backslash [ 0 , i ) .
$$

## 14.12 12

Prove that TFAE for a Möbius transformation T given by $T ( z ) = { \frac { a z + b } { c z + d } } \vdots$

a. T maps $\mathbb { R } \cup \{ \infty \}$ to itself.

b. It is possible to choose $a , b , c , d$ to be real numbers.

c. ${ \overline { { T ( z ) } } } = T ( { \bar { z } } )$ for every $z \in \mathbb { C P } ^ { 1 }$

d. There exist $\alpha \in \mathbb { R } , \beta \in \mathbb { C } \backslash$ R such that $T ( \alpha ) = \alpha \ { \mathrm { a n d } } \ T ( { \overline { { \beta } } } ) = { \overline { { T ( \beta ) } } }$

## 14.13 13

Find a conformal map from $D = \{ z : \ | z | < 1 , \ | z - 1 / 2 | > 1 / 2 \}$ to the unit disk $\Delta = \{ z : | z | < 1 \}$

## 14.13.1 Tie’s Extra Questions: Fall 2009

Find a conformal map from $D = \{ z : \ | z | < 1 , \ | z - 1 / 2 | > 1 / 2 \}$ to the unit disk $\Delta = \{ z : | z | < 1 \}$

## 15 Maps of the Disc

## 15.1 Spring 2020 HW 1 # 5

a. Let $z , w \in \mathbb { C }$ with $\bar { z } w \ne 1$ . Prove that

$$
\left| \frac { w - z } { 1 - \overline { { w } } z } \right| < 1 \mathrm { i f } \ | z | < 1 , \ | w | < 1
$$

with equality when $| z | = 1 \ \mathrm { o r } \ | w | = 1$

b. Prove that for a fixed $w \in \mathbb { D }$ , the mapping $F : z \mapsto { \frac { w - z } { 1 - { \overline { { w } } } z } }$ satisfies

• F maps D to itself and is holomorphic.

$F ( 0 ) = w$ and $F ( w ) = 0$

$| z | = 1$ implies $| F ( z ) | = 1$

## 16 Rouche’s Theorem (8155h)

## 16.1 1

<!-- image-->

Prove that for every $n \in \mathbb { Z } ^ { \geq 0 }$ the following polynomial has no roots in the open unit disc:

$$
f _ { n } ( x ) : = \sum _ { k = 0 } ^ { n } { \frac { z ^ { k } } { k ! } } .
$$

Hint: check $n = 1 , 2$ directly.

Solution omitted.

<!-- image-->

## 16.2 2

<!-- image-->

Assume that $| b | < 1$ and show that the following polynomial has exactly two roots (counting multiplicity) in $| z | < 1$ :

$$
f ( z ) : = z ^ { 3 } + 3 z ^ { 2 } + b z + b ^ { 2 } .
$$

Solution omitted.

## 16.3 3

Let $c \in \mathbb { C }$ with $| c | < { \frac { 1 } { 3 } } .$ Show that on the open set $\left\{ z \in \mathbb { C } \mid \Re ( z ) < 1 \right\}$ , the function $f ( z ) : = c e ^ { z }$ has exactly one fixed point.

## 16.4 4

How many roots does the following polynomial have in the open disc $| z | < 1 2$

$$
f ( z ) = z ^ { 7 } - 4 z ^ { 3 } - 1 .
$$

Solution omitted.

<!-- image-->

## 16.5 5

Let $n \in \mathbb { Z } ^ { \geq 0 }$ and show that the equation

$$
e ^ { z } = a z ^ { n }
$$

has n solutions in the open unit disc $\operatorname { i f } \left| a \right| > e ,$ and no solutions if $| a | < { \frac { 1 } { e } } .$

<!-- image-->

## 16.6 6

Let f be analytic in a domain D and fix $z _ { 0 } \in D$ with $w _ { 0 } : = f ( z _ { 0 } )$ . Suppose $z _ { \mathrm { 0 } }$ is a zero of $f ( z ) - w _ { 0 }$ with finite multiplicity m. Show that there exists $\delta > 0$ and $\varepsilon > 0$ such that for each w such that $0 < | w - w _ { 0 } | < \varepsilon ,$ the equation $f ( z ) - w = 0$ has exactly m distinct solutions inside the disc $| z - z _ { 0 } | < \delta .$

## 16.7 7

For $k = 1 , 2 , \cdots , n$ , suppose $| a _ { k } | < 1$ and

$$
f ( z ) : = \left( { \frac { z - a _ { 1 } } { 1 - { \bar { a } } _ { q } z } } \right) \left( { \frac { z - a _ { 2 } } { 1 - { \bar { a } } _ { 2 } z } } \right) \cdot \cdot \cdot \left( { \frac { z - a _ { n } } { 1 - { \bar { a } } _ { n } z } } \right) .
$$

Show that $f ( z ) = b$ has n solutions in $| z | < 1$

## 16.8 8

For each $n \in \mathbb { Z } ^ { \geq 1 }$ , let

$$
P _ { n } ( z ) = 1 + z + { \frac { 1 } { 2 ! } } z ^ { 2 } + \cdots + { \frac { 1 } { n ! } } z ^ { n } .
$$

Show that for sufficiently large $n ,$ the polynomial $P _ { n }$ has no zeros in $| z | < 1 0$ , while the polynomial $P _ { n } ( z ) - 1$ has precisely 3 zeros there.

<!-- image-->

## 16.9 9

Prove that

$$
\operatorname* { m a x } _ { | z | = 1 } \left| a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { n - 1 } z ^ { n - 1 } + z ^ { n } \right| \ge 1 .
$$

Hint: the first part of the problem asks for a statement of Rouche’s theorem.

## 16.10 10

Use Rouche’s theorem to prove the Fundamental Theorem of Algebra.

## 17 Extras

<table><tr><td>17.1 ?</td><td></td></tr></table>

Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra:

If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree $n ,$ then it has n zeros in C.

<table><tr><td>17.2 ?</td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

Suppose f is entire and there exist A, $R > 0$ and natural number N such that

$$
| f ( z ) | \geq A | z | ^ { N } { \mathrm { ~ f o r ~ } } | z | \geq R .
$$

Show that (i) f is a polynomial and (ii) the degree of f is at least N .

## 17.2.1 Tie’s Extra Questions: Fall 2009

Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra: If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree n, then it has n zeros in C.

## 17.2.2 Spring 20202 HW 3 # 8

Prove the fundamental theorem of Algebra using

a. Rouche’s Theorem.

b. The maximum modulus principle.

## 17.2.3 Spring 20202 HW 3 # 11

Find the number of roots of $p ( z ) = 4 z ^ { 4 } - 6 z + 3$ in $| z | < 1$ and $1 < | z | < 2$ respectively.

## 17.2.4 Spring 20202 HW 3 # 12

Prove that $z ^ { 4 } + 2 z ^ { 3 } - 2 z + 1 0$ has exactly one root in each open quadrant.

## 17.2.5 Spring 20202 HW 3 # 13

Prove that for a > 0, z tan z − a has only real roots.

# 18 Schwarz Lemma and Reflection Principle(8155i)

Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic and admits a continuous extension $\widetilde { f } : \overline { { \mathbb { D } } } \to \overline { { \mathbb { D } } }$ such that $| z | = 1 \implies$ $| f ( z ) | = 1$

$$
\mathbf { 1 8 . 1 . 1 \textbf { a } } ^ { \flat }
$$

Prove that f is a rational function.

## 18.1.2 b

Suppose that z = 0 is the unique zero of f. Show that

$$
\exists n \in \mathbb { N } , \lambda \in S ^ { 1 } \quad { \mathrm { s u c h t h a t } } \quad f ( z ) = \lambda z ^ { n } .
$$

$$
\mathbf { 1 8 . 1 . 3 ~ c ~ } ^ { \flat }
$$

Suppose that $a _ { 1 } , \cdots , a _ { n } \in \mathbb { D }$ are the zeros of f and prove that

$$
\exists \lambda \in S ^ { 1 } \quad { \mathrm { s u c h t h a t } } \quad f ( z ) = \lambda \prod _ { j = 1 } ^ { n } { \frac { z - a _ { j } } { 1 - { \overline { { a _ { j } } } } z } } .
$$

## 18.2 2

Let $\overline { { B } } ( a , r )$ denote the closed disc of radius r about $a \in \mathbb { C }$ . Let $f$ be holomorphic on an open set containing $\textstyle { \overline { { B } } } ( a , r )$ and let

$$
M : = \operatorname* { s u p } _ { z \in \overline { { B } } ( a , r ) } | f ( z ) | .
$$

Prove that

$$
z \in \overline { { B } } \left( a , \frac { r } { 2 } \right) , z \neq a , \qquad \frac { | f ( z ) - f ( a ) | } { | z - a | } \leq \frac { 2 M } { r } .
$$

## 18.3 3

Define

$$
G : = \left\{ z \in \mathbb { C } \Big \vert \ \Re ( z ) > 0 , | z - 1 | > 1 \right\} .
$$

Find all of the injective conformal maps $G  \mathbb { D }$ . These may be expressed as compositions of maps, but explain why this list is complete.

## 18.4 4

Suppose $f : \mathbb { H } \cup \mathbb { R }  \mathbb { C }$ satisfies the following:

$f ( i ) = i$

• f is continuous

• f is analytic on H

$f ( z ) \in \mathbb { R } \iff z \in \mathbb { R } .$

Show that f (H) is a dense subset of H.

## 18.5 5

Suppose $f : \mathbb { D } \to \mathbb { H }$ is analytic and satisfies $f ( 0 ) = 2$ . Find a sharp upper bound for $\left| f ^ { \prime } ( 0 ) \right|$ , and prove it is sharp by example.

## 18.6 6

Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic, has a single zero of order k at $z = 0 ,$ and satsifies $\operatorname* { l i m } _ { | z | \to 1 } | f ( z ) | = 1$ Give with proof a formula for $f ( z )$

<!-- image-->

## 18.7 7

<!-- image-->

## 18.7.1 a

State the standard Schwarz reflection principle involving reflection across the real axis.

## 18.7.2 b

Give a linear fractional transformation T mapping D to H. Let $g ( z ) = { \bar { z } } .$ , and show

$$
( T ^ { - 1 } \circ g \circ T ) ( z ) = 1 / { \bar { z } } .
$$

18.7.3 c

Suppose that f is holomorphic on D, continuous on ${ \overline { { \mathbb { D } } } } ,$ and real on $S ^ { 1 }$ . Show that f must be constant.

<!-- image-->

## 18.8 8

<!-- image-->

Suppose $f , g : \mathbb { D } \to \Omega$ are holomorphic with f injective and $f ( 0 ) = g ( 0 )$

Show that

$$
\forall 0 < r < 1 , \qquad g \left( \left\{ | z | < r \right\} \right) \subseteq f \left( \left\{ | z | < r \right\} \right) .
$$

## 18.9 9

Let $S : = \left\{ z \in \mathbb { D } \Big | \mathbb { S } ( z ) \geq 0 \right\}$ . Suppose $f : S  \mathbb { C }$ is continuous on $S ,$ real on $S \cap \mathbb { R }$ , and holomorphic on $S ^ { \circ }$

Prove that f is the restriction of a holomorphic function on D.

## 18.10 10

Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic. Prove that

$$
\forall a \in \mathbb { D } , \qquad { \frac { | f ^ { \prime } ( a ) | } { 1 - | f ( a ) | ^ { 2 } } } \leq { \frac { 1 } { 1 - | a | ^ { 2 } } } .
$$

## 18.10.1 Tie’s Extra Questions: Fall 2009

Let g be analytic for $| z | \le 1$ and $| g ( z ) | < 1$ for $| z | = 1$

1. Show that g has a unique fixed point in $| z | < 1$

2. What happens if we replace $| g ( z ) | < 1$ with $| g ( z ) | \leq 1$ for $| z | = 1 2$ Give an example if (a) is not true or give an proof if (a) is still true.

3. What happens if we simply assume that f is analytic for $| z | < 1$ and $| f ( z ) | < 1$ for $| z | < 1 2$ Suppose that $f ( z ) \not \equiv z$ . Can f have more than one fixed point in $| z | < 1 2$

$$
H i n t : \ T h e \ m a p \ \psi _ { \alpha } ( z ) = \frac { \alpha - z } { 1 - \bar { \alpha } z } \ m a y \ b e \ u s e f u l .
$$

## 18.10.2 Spring 20202 HW 2 # 2.6.15

Suppose f is continuous and nonvanishing on D, and holomorphic in D. Prove that if $| z | = 1 \implies$ $| f ( z ) | = 1$ , then f is constant.

Hint: Extend f to all $o f \mathbb { C }$ by $f ( z ) = 1 / \overline { { f ( 1 / \bar { z } ) } }$ for any $| z | > 1$ and argue as in the Schwarz reflection principle.

# 19 Riemann Mapping andCasorati-Weierstrass

## 19.0.1 Spring 20202 HW 3 # 4

Let f be non-constant, analytic in $| z | > 0$ , where $f ( z _ { n } ) = 0$ for infinitely many points $z _ { n }$ with $\operatorname* { l i m } _ { n \to \infty } z _ { n } = 0$ J.

Show that $z = 0$ is an essential singularity for $f .$

Example: f(z) = sin(1/z).

## 19.1 10.

Let $f : \mathbb { C } \to \mathbb { C }$ be an injective analytic (also called univalent) function. Show that there exist complex numbers $a \neq 0$ and b such that $ f ( z ) = a z + b . $

## 19.1.1 Tie’s Extra Questions: Fall 2009

Let $f : \mathbb { C } \to \mathbb { C }$ be an injective analytic (also called univalent) function. Show that there exist complex numbers $a \neq 0$ and b such that $ f ( z ) = a z + b . $

## 19.1.2 Spring 20202 HW 3 # 3.8.14

Prove that all entire functions that are injective are of the form $ f ( z ) = a z + b$ with $a , b \in \mathbb { C }$ and $a \neq 0$

Hint: Apply the Casorati-Weierstrass theorem to $f ( 1 / z )$

## 19.1.3 Spring 20202 HW 3 # 3.8.15

Use the Cauchy inequalities or the maximum modulus principle to solve the following problems:

a. Prove that if f is an entire function that satisfies

$$
\operatorname* { s u p } _ { | z | = R } | f ( z ) | \leq A R ^ { k } + B
$$

for all $R > 0$ , some integer $k \geq 0$ , and some constants $A , B > 0$ , then $f$ is a polynomial of degree $\leq k$

b. Show that if f is holomorphic in the unit disc, is bounded, and converges uniformly to zero in the sector $\theta < \arg ( z ) < \varphi$ as $| z | \to 0$ , then $f \equiv 0$

c. Let $w _ { 1 } , \cdots w _ { n }$ be points on $S ^ { 1 } \subset \mathbb { C }$ . Prove that there exists a point $z \in S ^ { 1 }$ such that the product of the distances from z to the points $w _ { j }$ is at least 1.

Conclude that there exists a point $w \in S ^ { 1 }$ such that the product of the above distances is exactly 1.

d. Show that if the real part of an entire function is bounded, then f is constant.

## 19.1.4 Spring 20202 HW 3 # 3.8.17

Let f be non-constant and holomorphic in an open set containing the closed unit disc.

a. Show that if $| f ( z ) | = 1$ whenever $| z | = 1$ , then the image of f contains the unit disc.

Hint: Show that $f ( z ) ~ = ~ w _ { 0 }$ has a root for every   
$w _ { 0 } \in \mathbb { D } .$ , for which it suffices to show that $f ( z ) = 0$   
has a root. Conclude using the maximum modulus   
principle.

b. If $| f ( z ) | \geq 1$ whenever $| z | = 1$ and there exists a $z _ { 0 } \in \mathbb { D }$ such that $| f ( z _ { 0 } ) | < 1$ , then the image of f contains the unit disc.

## 19.1.5 Spring 20202 HW 3 # 3.8.19

Prove that maximum principle for harmonic functions, i.e.

a. If u is a non-constant real-valued harmonic function in a region $\Omega ,$ then u can not attain a maximum or a minimum in Ω.

b. Suppose Ω is a region with compact closure $\overline { { \Omega } } .$ . If u is harmonic in Ω and continuous in ${ \overline { { \Omega } } } ,$ then

$$
\operatorname* { s u p } _ { z \in \Omega } | u ( z ) | \leq \operatorname* { s u p } _ { z \in \overline { { \Omega } } - \Omega } | u ( z ) | .
$$

Hint: to prove $( a ) ,$ assume u attains a local maximum at $z _ { 0 }$ Let f be holomorphic near $z _ { \mathrm { 0 } }$ with $\Re ( f ) = u ,$ and show that f is not an open map. Then (a) implies (b).

## 19.1.6 Spring 20202 HW 3 # 9

Let f be analytic in a region D and $\gamma \mathrm { ~ a ~ }$ rectifiable curve in D with interior in $D$ .

Prove that if f (z) is real for all $z \in \gamma$ , then f is constant.

## 19.1.7 Spring 20202 HW 3 # 14

Let $f$ be nonzero, analytic on a bounded region Ω and continuous on its closure $\overline { { \Omega } } .$

Show that if $| f ( z ) | \equiv M$ is constant for $z \in \partial \Omega$ , then $f ( z ) \equiv M e ^ { i \theta }$ for some real constant $\theta .$

## 20 Extra Questions from Jingzhi Tie

## 20.1 16

Let $f ( z )$ be analytic in an open set Ω except possibly at a point $z _ { \mathrm { 0 } }$ inside $\Omega .$

Show that if $f ( z )$ is bounded in near $z _ { \mathrm { 0 } }$ , then $\int _ { \Delta } f ( z ) d z = 0$ for all triangles $\Delta$ in Ω.

## 20.1.1 Tie’s Extra Questions: Fall 2009

For $s > 0$ , the gamma function is defined by $\Gamma ( s ) = \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { s - 1 } d t .$

1. Show that the gamma function is analytic in the half-plane $\Re ( s ) > 0$ , and is still given there by the integral formula above.

2. Apply the formula in the previous question to show that

$$
\Gamma ( s ) \Gamma ( 1 - s ) = \frac { \pi } { \sin \pi s } .
$$

Hint: You may need $\Gamma ( 1 - s ) = t \int _ { 0 } ^ { \infty } e ^ { - v t } ( v t ) ^ { - s } d v$ for t > 0.

## 20.2 Fall 2009

## 20.2.1 Tie’s Extra Questions: Fall 2009

Let $f ( z )$ be analytic in an open set Ω except possibly at a point $z _ { \mathrm { 0 } }$ inside Ω. Show that if $f ( z )$ is bounded in near $z _ { \mathrm { 0 } }$ , then $\int _ { \Delta } f ( z ) d z = 0$ for all triangles $\Delta$ in Ω.

## 20.2.2 Tie’s Extra Questions: Fall 2009

Assume f is continuous in the region: $0 < | z - a | \leq R , \ 0 \leq \arg ( z - a ) \leq \beta _ { 0 } \ ( 0 < \beta _ { 0 } \leq 2 \pi )$ and the limit $\operatorname* { l i m } _ { z \to a } ( z - a ) f ( z ) = A $ exists. Show that

$$
\operatorname * { l i m } _ { r  0 } \int _ { \gamma _ { r } } f ( z ) d z = i A \beta _ { 0 } \ ,
$$

where $\gamma _ { r } : = \lbrace z \mid z = a + r e ^ { i t } , 0 \leq t \leq \beta _ { 0 } \rbrace$

## 20.2.3 Tie’s Extra Questions: Fall 2009

Show that $f ( z ) = z ^ { 2 }$ is uniformly continuous in any open disk $| z | < R$ where $R > 0$ is fixed, but it is not uniformly continuous on C.

## 20.2.4 Tie’s Extra Questions: Fall 2009

(1) Show that the function $u = u ( x , y )$ given by

$$
u ( x , y ) = { \frac { e ^ { n y } - e ^ { - n y } } { 2 n ^ { 2 } } } \sin n x \quad { \mathrm { f o r ~ } } n \in \mathbf { N }
$$

is the solution on $D = \{ ( x , y ) ~ | x ^ { 2 } + y ^ { 2 } < 1 \}$ of the Cauchy problem for the Laplace equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 0 , \quad u ( x , 0 ) = 0 , \quad \frac { \partial u } { \partial y } ( x , 0 ) = \frac { \sin n x } { n } .
$$

(2) Show that there exist points $( x , y ) \in D$ such that lim n $_ { \stackrel { \mathrm { 1 S u p } } {  \infty } } | u ( x , y ) | = \infty$

## 20.3 Fall 2011

## 20.3.1 Tie’s Extra Questions: Fall 2011

Let f be a continuous function in the region

$$
D = \{ z \ | | z | > R , 0 \leq \arg Z \leq \theta \} \quad \mathrm { w h e r e } \quad 0 \leq \theta \leq 2 \pi .
$$

If there exists k such that $\operatorname* { l i m } _ { z \to \infty } z f ( z ) = k$ for z in the region D. Show that

$$
\operatorname* { l i m } _ { R ^ { \prime } \to \infty } \int _ { L } f ( z ) d z = i \theta k ,
$$

where L is the part of the circle $| z | = R ^ { \prime }$ which lies in the region D.

## 20.3.2 Tie’s Extra Questions: Fall 2011

Suppose that f is an analytic function in the region D which contains the point a. Let

$$
F ( z ) = z - a - q f ( z ) , \quad { \mathrm { w h e r e } } \quad q { \mathrm { ~ i s ~ a ~ c o m p l e x ~ p a r a m e t e r . } }
$$

(1) Let $K \subset D$ be a circle with the center at point a and also we assume that $f ( z ) \neq 0$ for $z \in K$ Prove that the function F has one and only one zero $z = w$ on the closed disc $\overline { { K } }$ whose boundary is the circle K ${ \mathrm { i f ~ } } | q | < \operatorname* { m i n } _ { z \in K } { \frac { | z - a | } { | f ( z ) | } }$

(2) Let $G ( z )$ be an analytic function on the disk $\overline { { K } } .$ Apply the residue theorem to prove that $\frac { G ( w ) } { F ^ { \prime } ( w ) } = \frac { 1 } { 2 \pi i } \int _ { K } \frac { G ( z ) } { F ( z ) } d z$ , where w is the zero from (1).

(3) If $z \in K$ , prove that the function $\frac { 1 } { F ( z ) }$ can be represented as a convergent series with respect to q: ${ \frac { 1 } { F ( z ) } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( q f ( z ) ) ^ { n } } { ( z - a ) ^ { n + 1 } } }$

## 20.3.3 Tie’s Extra Questions: Fall 2011

Evaluate $\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x$

## 20.3.4 Tie’s Extra Questions: Fall 2011

Let $f = u + i v$ be differentiable $\mathrm { ( i . e . ~ } f ^ { \prime } ( z )$ exists) with continuous partial derivatives at a point $z = r e ^ { i \theta } , r \neq 0$ . Show that

$$
\frac { \partial u } { \partial r } = \frac { 1 } { r } \frac { \partial v } { \partial \theta } , \quad \frac { \partial v } { \partial r } = - \frac { 1 } { r } \frac { \partial u } { \partial \theta } .
$$

## 20.3.5 Tie’s Extra Questions: Fall 2011

Show that $\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x = { \frac { \pi } { n \sin { \frac { a \pi } { n } } } }$ using complex analysis, $0 \textless a \textless n$ . Here n is a positive integer.

## 20.3.6 Tie’s Extra Questions: Fall 2011

For $s > 0$ , the gamma function is defined by $\Gamma ( s ) = \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { s - 1 } d t .$

1. Show that the gamma function is analytic in the half-plane $\Re ( s ) > 0$ , and is still given there by the integral formula above.

2. Apply the formula in the previous question to show that

$$
\Gamma ( s ) \Gamma ( 1 - s ) = \frac { \pi } { \sin \pi s } .
$$

Hint: You may need $\Gamma ( 1 - s ) = t \int _ { 0 } ^ { \infty } e ^ { - v t } ( v t ) ^ { - s } d v$ for t > 0.

## 20.3.7 Tie’s Extra Questions: Fall 2011

Apply Rouché’s Theorem to prove the Fundamental Theorem of Algebra: If

$$
P _ { n } ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { n - 1 } z ^ { n - 1 } + a _ { n } z ^ { n } \quad ( a _ { n } \neq 0 )
$$

is a polynomial of degree n, then it has n zeros in C.

## 20.3.8 Tie’s Extra Questions: Fall 2011

Let g be analytic for $| z | \le 1$ and $| g ( z ) | < 1 \mathrm { f o r } | z | = 1$

• Show that g has a unique fixed point in $| z | < 1$

• What happens if we replace $| g ( z ) | < 1$ with $| g ( z ) | \leq 1$ for $| z | = 1 2$ Give an example if (a) is not true or give an proof if (a) is still true.

• What happens if we simply assume that f is analytic for $| z | < 1$ and $| f ( z ) | < 1$ for $| z | < 1 2$ Suppose that $f ( z ) \not \equiv z$ . Can f have more than one fixed point in $| z | < 1 2$

$$
H i n t : \ T h e \ m a p \ \psi _ { \alpha } ( z ) = \frac { \alpha - z } { 1 - \bar { \alpha } z } \ m a y \ b e \ u s e f u l .
$$

## 20.3.9 Tie’s Extra Questions: Fall 2011

Find a conformal map from $D = \{ z : \ | z | < 1 , \ | z - 1 / 2 | > 1 / 2 \}$ to the unit disk $\Delta = \{ z : | z | < 1 \}$

## 20.3.10 Tie’s Extra Questions: Fall 2011

Let $f ( z )$ be entire and assume that $f ( z ) \leq M | z | ^ { 2 }$ outside some disk for some constant M. Show that f (z) is a polynomial in z of degree $\leq 2$

## 20.3.11 Tie’s Extra Questions: Fall 2011

Let $f ( z )$ be analytic in an open set Ω except possibly at a point $z _ { \mathrm { 0 } }$ inside Ω. Show that if $f ( z )$ is bounded in near $z _ { \mathrm { 0 } }$ , then $\int _ { \Delta } f ( z ) d z = 0$ for all triangles $\Delta$ in Ω.

## 20.3.12 Tie’s Extra Questions: Fall 2011

Assume f is continuous in the region: $0 < | z - a | \leq R , \ 0 \leq \arg ( z - a ) \leq \beta _ { 0 } \ ( 0 < \beta _ { 0 } \leq 2 \pi )$ and the limit $\operatorname* { l i m } _ { z \to a } ( z - a ) f ( z ) = A $ exists. Show that

$$
\operatorname * { l i m } _ { r  0 } \int _ { \gamma _ { r } } f ( z ) d z = i A \beta _ { 0 } \ ,
$$

where $\gamma _ { r } : = \lbrace z \mid z = a + r e ^ { i t } , 0 \leq t \leq \beta _ { 0 } \rbrace$

## 20.3.13 Tie’s Extra Questions: Fall 2011

Show that $f ( z ) = z ^ { 2 }$ is uniformly continuous in any open disk $| z | < R$ where $R > 0$ is fixed, but it is not uniformly continuous on C.

(1) Show that the function $u = u ( x , y )$ given by

$$
u ( x , y ) = { \frac { e ^ { n y } - e ^ { - n y } } { 2 n ^ { 2 } } } \sin n x \quad { \mathrm { f o r ~ } } n \in \mathbf { N }
$$

is the solution on $D = \{ ( x , y ) ~ | x ^ { 2 } + y ^ { 2 } < 1 \}$ of the Cauchy problem for the Laplace equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 0 , \quad u ( x , 0 ) = 0 , \quad \frac { \partial u } { \partial y } ( x , 0 ) = \frac { \sin n x } { n } .
$$

(2) Show that there exist points $( x , y ) \in D$ such that $\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } | u ( x , y ) | = \infty .$

## 20.4 Spring 2014

## 20.4.1 Tie’s Extra Questions: Spring 2014

The question provides some insight into Cauchy’s theorem. Solve the problem without using the Cauchy theorem.

1. Evaluate the integral $\int _ { \gamma } z ^ { n } d z$ for all integers n. Here $\gamma$ is any circle centered at the origin with the positive (counterclockwise) orientation.

2. Same question as (a), but with $\gamma$ any circle not containing the origin.

3. Show that if $\vert a \vert < r < \vert b \vert$ , then $\int _ { \gamma } { \frac { d z } { ( z - a ) ( z - b ) } } d z = { \frac { 2 \pi i } { a - b } }$ . Here $\gamma$ denotes the circle centered at the origin, of radius r, with the positive orientation.

## 20.4.2 Tie’s Extra Questions: Spring 2014

Evaluate $\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x .$

## 20.4.3 Tie’s Extra Questions: Spring 2014

Let $f = u +$ iv be differentiable (i.e. $f ^ { \prime } ( z )$ exists) with continuous partial derivatives at a point $z = r e ^ { i \theta } , r \neq 0$ . Show that

$$
\frac { \partial u } { \partial r } = \frac { 1 } { r } \frac { \partial v } { \partial \theta } , \quad \frac { \partial v } { \partial r } = - \frac { 1 } { r } \frac { \partial u } { \partial \theta } .
$$