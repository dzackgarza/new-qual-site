# Complex Analysis Qual Prep Week 1: Things Named After Cauchy

D. Zack Garza

## Table of Contents

## Contents

Table of Contents 2   
1 Topics 3   
1.1 Review . 3   
1.1.1 Integrals and Residues 3   
1.1.2 Residues . 5   
1.1.3 Blaschke Factors 9   
1.1.4 Cauchy’s Integral Formula 10   
1.1.5 Misc . . 11   
2 Warmups 12   
3 Questions 13   
4 Qual Problems 14

## 1 Topics

• Blaschke factors

• Toy contours

• Cauchy’s integral formula

• Cauchy inequalities

• Computing integrals

– Residue formulas

– ML Inequality

– Jordan’s lemma

## 1.1 Review

proof of the theorem.

For example, in the slit plane $\Omega = \mathbb { C } - \{ ( - \infty , 0 ] \}$ we have the principal branch of the logarithm

$$
\log z = \log r + i \theta
$$

where $z = r e ^ { i \theta }$ with $\left| \theta \right| < \pi .$ (Here we drop the subscript Ω, and write ply lT ov  e a $\gamma$ shown in Figure 8.

Figure 1: Complex log

## 1.1.1 Integrals and Residues

For example, the function $f ( z ) = 1 / z \quad$ does not have a primitive in the open set $\mathbb { C } - \{ 0 \}$ , since if C is the unit circle parametrized by $z ( t ) = e ^ { i t }$ $0 \leq t \leq 2 \pi$ , we have

$$
\int _ { C } f ( z ) d z = \int _ { 0 } ^ { 2 \pi } { \frac { i e ^ { i t } } { e ^ { i t } } } d t = 2 \pi i \neq 0 .
$$

Figure 2: Integrating $1 / \mathrm { z }$ manually

<!-- image-->  
Figure 3: Goursat

## 1.1.2 Residues

<!-- image-->

Figure 4: Toy Contours

Corollary 2.2 Suppose that f is holomorphic in an open set containing a circle C and its interior, except for poles at the points z1, ..., zN inside

$$
\int _ { C } f ( z ) d z = 2 \pi i \sum _ { k = 1 } ^ { N } \mathrm { r e s } _ { z _ { k } } f .
$$

For the proof,consider a multiple keyhole which has a loop avoiding each one of the poles. Let the width of the corridors go to zero. In

Theorem 1.3 If f has a pole of order n at $z _ { 0 }$

$$
f ( z ) = { \frac { a _ { - n } } { ( z - z _ { 0 } ) ^ { n } } } + { \frac { a _ { - n + 1 } } { ( z - z _ { 0 } ) ^ { n - 1 } } } + \cdots + { \frac { a _ { - 1 } } { ( z - z _ { 0 } ) } } + G ( z ) ,\tag{}
$$

$G$ is a holomorphic function in a neighborhood of $z _ { 0 }$

Theorem 1.4 If f has a pole of order n at $z _ { 0 }$

$$
\mathrm { r e s } _ { z _ { 0 } } f = \operatorname * { l i m } _ { z  z _ { 0 } } { \frac { 1 } { ( n - 1 ) ! } } ( { \frac { d } { d z } } ) ^ { n - 1 } ( z - z _ { 0 } ) ^ { n } f ( z ) .
$$

The theorem is an immediate consequence of formula (1), which implies

$$
( z - z _ { 0 } ) ^ { n } f ( z ) = a _ { - n } + a _ { - n + 1 } ( z - z _ { 0 } ) + \cdots + a _ { - 1 } ( z - z _ { 0 } ) ^ { n - 1 } +
$$

$$
+ G ( z ) ( z - z _ { 0 } ) ^ { n } .
$$

The sum

$$
{ \frac { a _ { - n } } { ( z - z _ { 0 } ) ^ { n } } } + { \frac { a _ { - n + 1 } } { ( z - z _ { 0 } ) ^ { n - 1 } } } + \cdot \cdot \cdot + { \frac { a _ { - 1 } } { ( z - z _ { 0 } ) } }
$$

is called the principal part of f at the pole $z _ { 0 } .$ , and the coefficient $a _ { - 1 }$ is the residue of f at that pole. We write $\mathrm { r e s } _ { z _ { 0 } } f = a _ { - 1 }$ 'he i portance of he es1 nes the other terms in the principal

## Simple poles

At a simple pole c, the residue of f is given by:

$$
\operatorname { R e s } ( f , c ) = \operatorname* { l i m } _ { z \to c } ( z - c ) f ( z ) .
$$

## Residue at infinity

In general, the residue at infinity is defined as:

$$
\operatorname { R e s } ( f ( z ) , \infty ) = - \operatorname { R e s } \left( { \frac { 1 } { z ^ { 2 } } } f \left( { \frac { 1 } { z } } \right) , 0 \right) .
$$

If the following condition is met:

$$
\operatorname* { l i m } _ { | z | \to \infty } f ( z ) = 0 ,
$$

then the residue at infinity can be computed using the following formula:

$$
\operatorname { R e s } ( f , \infty ) = - \operatorname* { l i m } _ { | z | \to \infty } z \cdot f ( z ) .
$$

tmay be that the function f can be expressed as a quotient of two functions, $f ( z ) = { \frac { g ( z ) } { h ( z ) } } , \forall$ here g and h are holomorphic functions in a neighbourhood of $\dot { \mathbf { \rho } } _ { \mathrm { c } , \hdots }$ with h(c) = 0 and $h ^ { \prime } ( c ) \neq 0$ . In such a case, L'Hôpital's rule can be used to simplify the above formula to:

$$
{ \begin{array} { r l } & { { \mathrm { R e s } } ( f , c ) : = \displaystyle \operatorname* { l i m } _ { z  c } ( z - c ) f ( z ) = \displaystyle \operatorname* { l i m } _ { z  c } { \frac { z g ( z ) - c g ( z ) } { h ( z ) } } } \\ & { \qquad = \displaystyle \operatorname* { l i m } _ { z  c } { \frac { g ( z ) + z g ^ { \prime } ( z ) - c g ^ { \prime } ( z ) } { h ^ { \prime } ( z ) } } = { \frac { g ( c ) } { h ^ { \prime } ( c ) } } . } \end{array} }
$$

Bounds

Consider a complex-valued, continuous function $f ,$ defined on a semicircu contour

$$
C _ { R } = \lbrace R e ^ { i \theta } \ \vert \ \theta \in [ 0 , \pi ] \rbrace
$$

of positive radius R lying in the upper half-plane, centered at the origin. If function f is of the form

$$
f ( z ) = e ^ { i a z } g ( z ) , \quad z \in C _ { R } ,
$$

with a positive parameter a, then Jordan's lemma states the following uppe bound for the contour integral:

$$
\left| \int _ { C _ { R } } f ( z ) d z \right| \leq { \frac { \pi } { a } } M _ { R } \quad { \mathrm { w h e r e } } \quad M _ { R } : = \operatorname* { m a x } _ { \theta \in \left[ 0 , \pi \right] } \left| g \left( R e ^ { i \theta } \right) \right| .
$$

Jordan’s Lemma:

(iii) One has the inequality

## 1.1.3 Blaschke Factors

7. The family of mappings introduced here plays an important role in complex analysis. These mappings, sometimes called Blaschke factors, will reappear in various applications in later chapters.

(a) Let z, w be two complex numbers such that $\overline { { z } } w \ne 1$ . Prove that

$$
\left| { \frac { w - z } { 1 - { \overline { { w } } } z } } \right| < 1 \ \quad { \mathrm { ~ i f ~ } } | z | < 1 { \mathrm { ~ a n d ~ } } | w | < 1 ,
$$

and also that

$$
\left| { \frac { w - z } { 1 - { \overline { { w } } } z } } \right| = 1 \ \quad { \mathrm { i f } } \ | z | = 1 { \mathrm { ~ o r ~ } } | w | = 1 .
$$

[Hint: Why can one assume that z is real? It then suffices to prove that

$$
( r - w ) ( r - \overline { { w } } ) \leq ( 1 - r w ) ( 1 - r \overline { { w } } )
$$

with equality for appropriate r and |w|.]

$$
F : z \mapsto { \frac { w - z } { 1 - { \overline { { w } } } z } }
$$

satisfies the following conditions:

$F : \mathbb { D } \to \mathbb { D } )$ , and is holomorphic.

(ii) F interchanges 0 and w, namely $F ( 0 ) = w$ and $F ( w ) = 0$

$| F ( z ) | = 1 { \mathrm { ~ i f ~ } } | z | = 1 .$

$F : \mathbb { D }  \mathbb { D }$ is bijective. [Hint: Calculate $F \circ F . ]$

## 1.1.4 Cauchy’s Integral Formula

toy contours.

The above ideas also lead us to a central result of this chapter, the Cauchy integral formula; this states that if f is holomorphic in an open set containing a circle C and its interior, then for all z inside $C ,$

$$
f ( z ) = { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { f ( \zeta ) } { \zeta - z } } d \zeta .
$$

D:Tr ( 1 as a consequence of the next theorem (see Exercises 11 and 12).

Theorem 4.1 Suppose f is holomorphic in an open set that contains the closure of a disc D. If C denotes the boundary circle of this disc with the positive orientation, then

$$
f ( z ) = \frac { 1 } { 2 \pi i } \int _ { C } \frac { f ( \zeta ) } { \zeta - z } d \zeta ~ f o r ~ a n y ~ p o i n t ~ z \in D .
$$

Corollary 4.2 If f is holomorphic in an open set $\Omega ,$ then f has infinitely many complex derivatives in Ω. Moreover, if $C \subset \Omega$ $a$ interior is also contained in Ω, then

$$
f ^ { ( n ) } ( z ) = { \frac { n ! } { 2 \pi i } } \int _ { C } { \frac { f ( \zeta ) } { ( \zeta - z ) ^ { n + 1 } } } d \zeta
$$

$a l l z i n$

From now on, we call the formulas of Theorem 4.1 and Corollary 4.2 the Cauchy integral formulas.

Corollary 4.3 (Cauchy inequalities) If f is holomorphic in an open set that contains the closure of a disc D centered at $z _ { 0 }$ and of radius R,

$$
\vert f ^ { ( n ) } ( z _ { 0 } ) \vert \leq { \frac { n ! \| f \| _ { C } } { R ^ { n } } } ,
$$

$\| f \| _ { C } = \operatorname* { s u p } _ { z \in C } | f ( z ) |$ $| f |$

## 1.1.5 Misc

Theorem 4.4 Suppose f is holomorphic in an open set Ω. If D is a disc centered at $z _ { 0 }$ and whose closure is contained in $\Omega ,$ power series expansion at $z _ { 0 }$

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }
$$

$z \in D$ , and the coefficients are given $b y$

$$
a _ { n } = \frac { f ^ { ( n ) } ( z _ { 0 } ) } { n ! } f o r a l l n \geq 0 .
$$

expansion around 0, say $\textstyle f ( z ) = \sum _ { n = 0 } ^ { } a _ { n } z ^ { n }$ , that converges in all of C.

Corollary 4.5 (Liouville's theorem) If f is entire and bounded, then

Proof. It suffices to prove that $f ^ { \prime } = 0 ,$ , since C is connected.and we

## 2 Warmups

• Do any example from here

## 1.4 5

$\begin{array} { r } { f ( z ) = \frac { 1 } { z } \ : \mathrm { o n } \ : S ^ { 1 } } \end{array}$

• Anything from the homeworks

• Show that $f ^ { \prime } = 0 \implies f$ is constant using integrals and primitives (i.e. antiderivatives).

See S&S Corollary 3.4.

5. Suppose f is continuously complex differentiable on $\Omega ,$ and $T \subset \Omega$ whose interior is also contained in Ω. Apply Green's theorem to show that

$$
\int _ { T } f ( z ) d z = 0 .
$$

This provides a proof of Goursat's theorem under the additional assumption that $f ^ { \prime }$ is continuous.

$( F , G )$ field, then

$$
\int _ { T } F d x + G d y = \int _ { \mathrm { I n t e r i o r ~ o f ~ } T } \left( { \frac { \partial G } { \partial x } } - { \frac { \partial F } { \partial y } } \right) d x d y .
$$

ExAMPLE 2. An integral that will play an important role in Chapter 6

$$
\int _ { - \infty } ^ { \infty } { \frac { e ^ { a x } } { 1 + e ^ { x } } } d x = { \frac { \pi } { \sin \pi a } } , 0 < a < 1 .
$$

## 3 Questions

• Can every continuous function on $\overline { { \mathbb { D } } }$ be uniformly approximated by polynomials in the variable $z ?$

Hint: compare to Weierstrass for the real interval.

• Suppose $f$ is analytic, defined on all of C, and for each $z _ { 0 } \in \mathbb { C }$ there is at least one coefficient in the expansion $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } ( z - z _ { 0 } ) ^ { n }$ is zero. Prove that f is a polynomial.

Hint: use the fact that $c _ { n } n ! = f ^ { ( n ) } ( z _ { 0 } )$ and use a countability argument.

11. Show that if $| \alpha | < r < | \beta |$ , then

$$
\int _ { \gamma } { \frac { 1 } { ( z - \alpha ) ( z - \beta ) } } = { \frac { 2 \pi i } { \alpha - \beta } }
$$

where $\gamma$ denotes the circle centered at the origin, of radius r, with positive orientation.

12. Assume f is continuous in the region: $x \ge x _ { 0 } , 0 \le y \le b$ and the limit

$$
\operatorname* { l i m } _ { x \to + \infty } f ( x + i y ) = A
$$

exists uniformly with respect to y (independent of y). Show that

$$
\operatorname* { l i m } _ { x  + \infty } \int _ { \gamma _ { x } } f ( z ) d z = i A b ,
$$

where $\gamma _ { x } : = \{ z \mid z = x + i t , 0 \leq t \leq b \}$

9. Let $f ( z )$ be analytic. Show that $f ( \overline { { 2 } } )$ is also analytic.

## 4 Qual Problems

2. Expand $\frac { 1 } { 1 - z ^ { 2 } } + \frac { 1 } { z - 3 }$ in a series of the form $\sum _ { - \infty } ^ { \infty } a _ { n } z ^ { n }$ so it converges for $| z | < 1$ $1 < | z | < 3 ;$ and $\mathrm { ( c ) } \ | z | > 3$

Figure 5: Fall 2020 $\# 2$

3. Let $a \in \mathbb { R }$ with $0 < a < 3$ . Evaluate $\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { 3 } } } d x$

Figure 6: Fall 2020 #3

1. Let $z _ { 1 }$ and $z _ { 2 }$ be two complex numbers.

(a) Show that $| z _ { 1 } - \bar { z } _ { 1 } z _ { 2 } | ^ { 2 } - | z _ { 1 } - z _ { 2 } | ^ { 2 } = ( 1 - | z _ { 1 } | ^ { 2 } ) ( 1 - | z _ { 2 } | )$

(b) Show that $\mathrm { i f ~ } | z _ { 1 } | < 1$ and $| z _ { 2 } | < 1$ , then $\left| \frac { z _ { 1 } - z _ { 2 } } { 1 - \bar { z } _ { 1 } z _ { 2 } } \right| < 1$

(c) Assume that $z _ { 1 } \neq z _ { 2 }$ Show that $\left| { \frac { z _ { 1 } - z _ { 2 } } { 1 - { \bar { z } } _ { 1 } z _ { 2 } } } \right| = 1$ if only ${ \mathrm { i f ~ } } | z _ { 1 } | = 1 { \mathrm { ~ o r ~ } } | z _ { 2 } | = 1$

Figure 7: Spring 2021 #1

2. Evaluate the integral $\int _ { - \infty } ^ { \infty } { \frac { e ^ { i \xi x } } { \cosh ( x ) } }$ dx where $\cosh ( x ) = { \frac { e ^ { x } + e ^ { - x } } { 2 } }$ and ξ is real.

Hint: Use an appropriate rectangular contour containing $[ - R , R ]$ as one side.

Figure 8: Spring 2021 #2

3. Let γ be piecewise smooth simple closed curve with interior $\Omega _ { 1 }$ and exterior $\Omega _ { 2 }$ . Assume $f ^ { \prime } ( z )$ exists in an open set containing $\gamma$ and $\Omega _ { 2 }$ and $\begin{array} { r } { \operatorname* { l i m } _ { z \to \infty } f ( z ) = A } \end{array}$ .Show that

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \xi ) } { \xi - z } } d \xi = { \left\{ \begin{array} { l l } { A , } & { { \mathrm { i f ~ } } z \in \Omega _ { 1 } , } \\ { - f ( z ) + A , } & { { \mathrm { i f ~ } } z \in \Omega _ { 2 } } \end{array} \right. }
$$

Figure 9: Fall 2019 #3