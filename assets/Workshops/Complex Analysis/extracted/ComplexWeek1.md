Complex Analysis Qual Prep Week 1: Preliminaries

D. Zack Garza

## Table of Contents

## Contents

Table of Contents 2\
1 Week 1: Preliminaries 3\
1.1 Topics 3\
1.2 Warmup 3\
1.3 Exercises 5\
1.4 Qual Problems 7

## Week 1: Preliminaries

<!-- image-->

## 1.1 Topics

<!-- image-->

• Complex arithmetic and geometry, conic section equations

• Uniform (continuity, differentiability, convergence)

• Inverse and implicit function theorems

• Green’s theorem, Stokes theorem

• Complex plane, Riemann sphere

<!-- image-->

## 1.2 Warmup

<!-- image-->

• State the Cauchy-Riemann equations.

• Define what it means for a function to be

– Holomorphic

– Meromorphic

– Analytic

– Harmonic

– Uniformly continuous

– Uniformly bounded

– Entire

• What does it mean for a sequence or series to uniformly converge?

• State the Laplace equation.

• What is the Dirichlet problem?

• Discuss how to carry out partial fraction decomposition

• Determine the radius of convergence of the power series for $\sqrt { z }$ expanded at $z _ { 0 } = 4 + 3 i$

• What is the logarithmic derivative?

• Find a function f such that $f ^ { 2 }$ is analytic on the open unit disc but $f$ is not.

Show that $f ( z ) = z ^ { 2 }$ is uniformly continuous in any open disk $| z | < R ,$ ,where $R > 0$ is fixed, but it is not uniformly continuous on C.

C 1

$$
3 . 3 . 3 \mathrm { ~ c ~ } \mathsf { Y }
$$

Identify $\mathbb { R } ^ { 2 }$ with C and give a necessary and sufficient condition for a real-differentiable function at $( a , b )$ to be complex differentiable at the point $a + i b$

## 3.4 4

Let $f = u + i v$ be complex-differentiable with continuous partial derivatives at a point $z = r e ^ { i \theta }$ with $r \neq 0 .$ Show that

$$
{ \frac { \partial u } { \partial r } } = { \frac { 1 } { r } } { \frac { \partial v } { \partial \theta } } \qquad { \frac { \partial v } { \partial r } } = - { \frac { 1 } { r } } { \frac { \partial u } { \partial \theta } } .
$$

$$
\mathbf { 9 . 1 \textit { 1 } } _ { \mathrm { ~ } } ^ { \mathrm { ~ } }
$$

Suppose f is analytic on a region Ω such that $\mathbb { D } \subseteq \Omega \subseteq \mathbb { C }$ and $f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ is a power series with radius of convergence exactly 1.

## 9.1.1 a

Give an example of such an f that converges at every point of $S ^ { 1 }$

## 9.1.2 b

Give an example of such an f which is analytic at 1 but $\sum _ { n = 0 } ^ { \infty } a _ { n }$ diverges.

$$
{ \mathfrak { s } } . 1 . 3 { \textbf { c } } ^ { \vdash }
$$

Prove that f can not be analytic at every point of $S ^ { 1 }$

$$
\mathbf { 1 . 3 3 } \cdots
$$

Find the Laurent expansion of

$$
f ( z ) = { \frac { z + 1 } { z ( z - 1 ) ^ { 2 } } }
$$

## 1.3 Exercises

3. Use n-th roots of unity (i.e. solutions of $z ^ { n } - 1 = 0 )$ to show that

$$
2 ^ { n - 1 } \sin { \frac { \pi } { n } } \sin { \frac { 2 \pi } { n } } \cdot \cdot \cdot \sin { \frac { ( n - 1 ) \pi } { n } } = n .
$$

$$
{ \mathrm { H i n t } } \colon 1 - \cos 2 \theta = 2 \sin ^ { 2 } \theta , \sin 2 \theta = 2 \sin \theta \cos \theta .
$$

2. Let $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ be analytic and one-to-one in $| z | < 1$ $0 < r _ { 0 } < 1$ $\overline { { D } } _ { r _ { 0 } }$ be the closed disk $| z | \leq r _ { 0 }$ . Show that the area A of $f ( \overline { { D } } _ { r _ { 0 } } )$ is finite and is given by

$$
A = \pi \sum _ { n = 1 } ^ { \infty } n | c _ { n } | ^ { 2 } r _ { 0 } ^ { 2 n } .
$$

[Hint: First find a formula in terms of polar coordinates in xy-plane for the area element dudv using complex analysis, where $f = u + i v$ Note that $d x d y = r d r d \theta . ]$

4. Prove that $| z _ { 1 } + z _ { 2 } | ^ { 2 } + | z _ { 1 } - z _ { 2 } | ^ { 2 } = 2 ( | z _ { 1 } | ^ { 2 } + | z _ { 2 } | ^ { 2 } )$ for any two complex numbers $z _ { 1 } , z _ { 2 } ,$ ,and explain the geometric meaning of this identity.

$$
\mathbf { 1 . 1 1 } \mathrm { ~ \# ~ } _ { + \mathrm { \# } } ^ { + }
$$

Find the Laurent expansion of

$$
f ( z ) = { \frac { z + 1 } { z ( z - 1 ) } }
$$

about z = 0 and $z = 1$ respectively.

5. Prove the following:

(a) The power series $\sum _ { n = 1 } ^ { \infty } n z ^ { n }$ does not converge at any point of the unit circle.

(b) The power series $\sum _ { n = 1 } ^ { \infty } { \frac { z ^ { n } } { n ^ { 2 } } }$ converges at every point of the unit circle.

(c) The power series $\sum _ { n = 1 } ^ { \infty } { \frac { z ^ { n } } { n } }$ converges at every point of the unit circle except at $z = 1$

6. (Cauchy's formula for "exterior" region) Let γ be piecewise smooth simple closed curve with interior $\Omega _ { 1 }$ and exterior $\Omega _ { 2 }$ . Assume $f ^ { \prime } ( z )$ exists in an open set containing γ and $\Omega _ { 2 }$ and lim ${ \mathfrak { i } } _ { z \to \infty } f ( z ) = A$ . Show that

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \xi ) } { \xi - z } } d \xi = { \left\{ \begin{array} { l l } { A , } & { { \mathrm { i f ~ } } z \in \Omega _ { 1 } , } \\ { - f ( z ) + A , } & { { \mathrm { i f ~ } } z \in \Omega _ { 2 } } \end{array} \right. }
$$

## UUMTLEA ANALIDID NAUIIUE I NUDLEMD Z.V

## Complex 2.0 #9.2

Let D be a domain which contains in its interior the closed unit disk $| z | \leq 1$ . Let f (z) be analytic in D except at a finite number of points $z _ { 1 } , \ldots , z _ { k }$ on the unit circle $| z | = 1$ where f (z) has first order poles with residues $s _ { 1 } , \ldots , s _ { k }$ . Let the Taylor series of f(z) at the origin be $\begin{array} { r } { \dot { f } ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } } \end{array}$ Prove that there exists a positive constant M such that $| a _ { n } | \leq M$

## Additional Problem

Let $f : \mathbb { R } \to \mathbb { R }$ satisfy

(1) f is continuous on $[ 0 , \infty )$

(2) $f ^ { \prime } \left( x \right)$ exists for all $x \geq 0$

(3) $f \left( 0 \right) = 0$

′ is increasing.

For $x > 0$ , define $\begin{array} { r } { g \left( x \right) = \frac { f ( x ) } { x } } \end{array}$ . Prove that g is increasing.

Problem: Prove or disprove that there is a sequence of analytic polynomials $\{ p _ { n } ( z ) \} , n \in \mathbb { N }$ , so that $p _ { n } ( z ) \to \bar { z } ^ { 4 }$ $n \to \infty$ uniformly for $z \in \partial D ( 0 , 1 )$

Problem: Show that for $R > 0$ $N _ { R }$ such that when $n > N _ { R }$ , the function

$$
P _ { n } ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + \cdots + { \frac { z ^ { n } } { n ! } } \neq 0 , \quad \forall \ | z | \leq R .
$$

Problem: Let f (z) be analytic in the disk $U = \{ | z | < 1 \}$ $f ( 0 ) = f ^ { \prime } ( 0 ) = 0 \quad$ Show that $g ( z ) = \sum _ { n = 1 } ^ { \infty } f \left( { \frac { z } { n } } \right)$ defines an analytic function on U. Moreover, show that the above function $g ( z )$ satisfies

$$
g ( z ) = f ( z ) \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } }
$$

if and only $\mathrm { i f } \ f ( z ) = c z ^ { 2 }$

## 1.4 Qual Problems

1. Find the Laurent series expansion of $f ( z ) = { \frac { 1 } { ( z - 1 ) ( z - 2 ) } }$ valid in the annulus $1 <$ $| z | < 2$

2. Prove that the distinct complex numbers $z _ { 1 } ,$ , z2 and $z _ { 3 }$ are the vertices of an equilateral triangle if and only if

$$
z _ { 1 } ^ { 2 } + z _ { 2 } ^ { 2 } + z _ { 3 } ^ { 2 } = z _ { 1 } z _ { 2 } + z _ { 2 } z _ { 3 } + z _ { 3 } z _ { 1 } .
$$

.(a) Prove that $\mathrm { i f } \ | w _ { 1 } | = c | w _ { 2 } |$ where $c > 0$ , then $| w _ { 1 } - c ^ { 2 } w _ { 2 } | = c | w _ { 1 } - w _ { 2 } |$

(b) Prove that if $c > 0 , c \neq 1$ and $z _ { 1 } \neq z _ { 2 }$ , then $\left| { \frac { z - z _ { 1 } } { z - z _ { 2 } } } \right| = c$ represents a circle.
Find its center and radius.

2. Expand $\frac { 1 } { 1 - z ^ { 2 } } + \frac { 1 } { z - 3 }$ in a series of t he form $\sum _ { - \infty } ^ { \infty } a _ { n } z ^ { n }$ so it converges for $| z | < 1$ $1 < | z | < 3 ;$ $| z | > 3$

3. Let $z _ { 1 }$ and $z _ { 2 }$ be two complex numbers.

(a)Show that $| z _ { 1 } - \bar { z } _ { 1 } z _ { 2 } | ^ { 2 } - | z _ { 1 } - z _ { 2 } | ^ { 2 } = ( 1 - | z _ { 1 } | ^ { 2 } ) ( 1 - | z _ { 2 } | )$

(b) Show that if $| z _ { 1 } | < 1$ and $| z _ { 2 } | < 1$ , then $\left| \frac { z _ { 1 } - z _ { 2 } } { 1 - \bar { z } _ { 1 } z _ { 2 } } \right| < 1 .$

(c) Assume that $z _ { 1 } \neq z _ { 2 } .$ .Show that $\left| { \frac { z _ { 1 } - z _ { 2 } } { 1 - { \bar { z } } _ { 1 } z _ { 2 } } } \right| = 1$ ${ \mathrm { i f ~ } } | z _ { 1 } | = 1 { \mathrm { ~ o r ~ } } | z _ { 2 } | = 1$

6.Suppose $\{ f _ { n } ( z ) \} _ { n = 1 } ^ { \infty }$ is a sequence of holomorphic functions on the unit disk D, and $f ( z )$ is a holomorphic function on the unit disk D. Show that the following are equivalent.

$\{ f _ { n } ( z ) \}$ converges to $f ( z )$ uniformly on compact subsets in D.

$\begin{array} { r } { \int _ { | z | = r } | f _ { n } ( z ) - f ( z ) | | d z | } \end{array}$ converges to 0 if $0 < r < 1$

$n \geq 2$ be an integer.
Show that $2 ^ { n - 1 } \prod _ { k = 1 } ^ { n - 1 } \sin { \frac { k \pi } { n } } = n$

[Hint: Use n-th roots of unity i.e., solutions of $z ^ { n } - 1 = 0 ]$

2. Let $u ( x , y )$ be a harmonic functions defined in an open disk of radius $R > 0$ Suppose that $u ( x , y )$ has continuous partial derivatives of order two in its domain.

a) Let two points $( a , b ) , ( x , y )$ in this disk be given.
Show that the following integral is independent of the path in this disk joining these points:

$$
v ( x , y ) = \int _ { ( a , b ) } ^ { ( x , y ) } ( - \frac { \partial u } { \partial y } d x + \frac { \partial u } { \partial x } d y ) .
$$

) (i) Prove that $u ( x , y ) + i v ( x , y )$ is an analytic function in this disk.

(ii) Prove that $v ( x , y )$ is harmonic in this disk.

$f : D \to \mathbb { C }$ be a continuous function, where $D \subset \mathbb { C }$ is a domain.
Let $\alpha : [ a , b ] \to D$ be a smooth curve.

a) Define the complex line integral $\textstyle \int _ { \alpha } f .$

b) Assume that there exists a constant M such that $| f ( \tau ) | \leq M$ for all $\tau \in { \mathrm { I m a g e } } ( \alpha )$ Prove that

$$
\big | \int _ { \alpha } f \big | \leq M \times \mathrm { l e n g t h } ( \alpha ) .
$$

$C _ { R }$ be the circle $| z | = R ,$ described in the counterclockwise direction, where $R > 1$ . Provide an upper bound for $\big | \int _ { C _ { R } } \frac { \log { ( z ) } } { z ^ { 2 } } \big |$ , which depends only on R and (possibly) other constants.
