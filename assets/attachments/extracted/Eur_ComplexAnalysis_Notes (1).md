# COMPLEX ANALYSIS NOTES

## CHRISTOPHER EUR

Notes taken while reviewing (but closer to relearning) complex analysis through [SSh03] and [Ahl79]. Some solutions to the exercises in [SSh03] are also written down. I do not claim that the notes or solutions written here are correct or elegant.

## 1. Preliminaries to complex analysis

The complex numbers is a field $\mathbb { C } : = \{ a + i b : a , b \in \mathbb { R } \}$ that is complete with respect to the modulus norm $| z | = z { \overline { { z } } }$ . Every $z \in \mathbb { C } , z \neq 0$ can be uniquely represented as $z \ = \ r e ^ { i \theta }$ for $r > 0 , \theta \in [ 0 , 2 \pi )$ . A region $\Omega \subset \mathbb { C }$ is a connected open subset; since C is locally-path connected, connected+open =⇒ path-connected (in fact, PL-path-connected). Denote the open unit disk by D.

Definition 1.1. A function $f : U \to \mathbb { C } \ f o r \ U \subset \mathbb { C }$ open is holomorphic/analytic/complexdifferentiable at $z _ { 0 } \in U$ if

$$
\operatorname* { l i m } _ { h \to 0 } { \frac { f ( z _ { 0 } + h ) - f ( z _ { 0 } ) } { h } }
$$

exists, and we denote the limit value by $f ^ { \prime } ( z _ { 0 } )$ . Equivalently, f is holomorphic at z0 iff there exists $a \in \mathbb { C }$ and such that $f ( z _ { 0 } + h ) - f ( z _ { 0 } ) - a h = h \psi ( h )$ and $\psi ( h ) \to 0$ as $h  0$ , in which case $a = f ^ { \prime } ( z _ { 0 } )$ . f is holomorphic if it is at z0 for all $z _ { 0 } \in U$

Proposition 1.2. Differentiation rules about $f + g , f g , f / g$ and $f \circ g$ (chain rule) holds.

Theorem 1.3. For $f : U \to \mathbb { C } ,$ , write $f = u + i v$ where $u , v : U \to \mathbb { R }$ . f is holomorphic at $z _ { 0 } \in U$ if and only if f as a map $\mathbb { R } ^ { 2 } \supset U  \mathbb { R } ^ { 2 }$ is differentiable at $z _ { \mathrm { 0 } }$ and satisfies

Cauchy-Riemann equations: $u _ { x } = v _ { y }$ and $u _ { y } = - v _ { x }$ at z0

Proof. First, note that $a + i b \in \mathbb { C }$ can identified with the real matrices of the form $\left[ { \begin{array} { l l } { a } & { - b } \\ { b } & { a } \end{array} } \right]$ . This also works well with $\mathbb { C } \simeq \mathbb { R } ^ { 2 }$ in that the vector in $\mathbb { R } ^ { 2 }$ for $( a + i b ) ( c + i d )$ is $\left[ \begin{array} { l l } { a } & { - b } \\ { b } & { a } \end{array} \right] \left[ \begin{array} { l } { c } \\ { d } \end{array} \right]$

Now, as a map in real variables, f is differentiable iff there exists a matrix A such that $\lvert f ( z _ { 0 } +$ $h ) - f ( z _ { 0 } ) - A h | = | h | | \psi ( h ) |$ with $| \psi ( h ) | \to 0$ as $h  0$ . Now, multiplication by A is complex number multiplication iff A of the form $\left[ \begin{array} { l l } { a } & { - b } \\ { b } & { a } \end{array} \right]$ . Thus, if f is differentiable in real sense and satisfies the Cauchy-Riemann equations, then $f ( z _ { 0 } + h ) - f ( z _ { 0 } ) - ( u _ { x } ( z _ { 0 } ) + i v _ { x } ( z _ { 0 } ) ) h = h \psi ( h )$ with $| \psi ( h ) |  0$ as $h  0$ , and hence holomorphic at $z _ { \mathrm { 0 } }$ . If $f$ is holomorphic, then letting A be the matrix of $f ^ { \prime } ( z _ { 0 } )$ works, and thus Cauchy-Riemann equation follows. 

Definition 1.4. Define two differential operators by:

$$
{ \frac { \partial } { \partial z } } = { \frac { 1 } { 2 } } \left( { \frac { \partial } { \partial x } } - i { \frac { \partial } { \partial y } } \right) \qquad { \frac { \partial } { \partial { \overline { { z } } } } } = { \frac { 1 } { 2 } } \left( { \frac { \partial } { \partial x } } + i { \frac { \partial } { \partial y } } \right)
$$

Proposition 1.5. f is holomorphic at z0 $i f f \frac { \partial f } { \partial \overline { { z } } } ( z _ { 0 } ) = 0$ . Moreover, if holomorphic,

$$
f ^ { \prime } ( z _ { 0 } ) = \frac { \partial f } { \partial z } ( z _ { 0 } ) = 2 \frac { \partial u } { \partial z } ( z _ { 0 } ) = 2 i \frac { \partial v } { \partial z } ( z _ { 0 } ) \ \mathrm { a n d } \ \operatorname* { d e t } [ D f ] _ { z _ { 0 } } = | f ( z _ { 0 } ) | ^ { 2 }
$$

Power series are good (and really the only) examples of holomorphic functions.

Theorem 1.6. Given a power series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ let $1 / R : = \operatorname* { l i m } \operatorname* { s u p } | a _ { n } | ^ { 1 / n }$ (with $1 / \infty = 0$ and $1 / 0 = \infty )$ . Then for $| z | < R$ , the series (uniformly) converges absolutely, and diverges $f o r \ | z | > R$ Moreover, $\textstyle f ( z ) : = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ is holomorphic on its disk of convergence with $\begin{array} { r } { f ^ { \prime } ( z ) = \sum _ { n = 0 } ^ { \infty } n a _ { n } z ^ { n } } \end{array}$ with the same radius of convergence.

Proof. Compare to geometric series (Weierstrass M-test), and do some computation.

It is useful to note the relationship between the root-test and the ratio-test; ratio-test is often the easier option, but root-test is more general. More precisely,

Proposition 1.7. For any sequence $\left\{ c _ { n } \right\}$ of positive numbers,

lim inf $\frac { c _ { n + 1 } } { c _ { n } } \leq$ lim inf $\sqrt [ n ] { c _ { n } }$ and lim sup $\sqrt [ n ] { c _ { n } } \leq \operatorname* { l i m } \operatorname* { s u p } \frac { c _ { n + 1 } } { c _ { n } }$

## 1.8. Exercises.

Exercise 1.A. [SSh03, 1.4] Show that there is no total ordering on C

Proof. Suppose there is a total ordering > on C, and $\mathrm { W L O G } \ i > 0$ . Then $- 1 = i ^ { 2 } > 0$ , and so $- 1 > 0$ , and so $1 = ( - 1 ) ^ { 2 } > 0 \mathrm { \ b u t \ } - 1 + \bar { 1 } > 1$ . Thus, $1 > 0$ and $1 < 0$ , which is a contradiction. 

Exercise 1.B. [SSh03, 1.7] For $z , w \in \mathbb { C }$ such that zw $\neq 1$ and $| z | \leq 1 , | w | \leq 1$ , show that

$$
\left| \frac { w - z } { 1 - \overline { { w } } z } \right| \leq 1
$$

where the equality occurs exactly when $| z | = 1 o r | w | = 1$ Moreover, for $w \in \mathbb { D }$ , the mapping $\begin{array} { r } { F : z \mapsto \frac { w - z } { 1 - \overline { { w } } z } } \end{array}$ is a bijective holomorphic map $F : \mathbb { D }  \mathbb { D }$ that interchanges 0 and w, and $| F ( z ) | = 1$ $i f \left| z \right| = 1$ . These mappings are called Blaschke factors

Proof. The inequality is equivalent to $| w - z | ^ { 2 } \leq | 1 - \overline { { w } } z | ^ { 2 }$ , which when written out is equivalent to $| z | ^ { 2 } + | w | ^ { 2 } \leq 1 + | w | ^ { 2 } | z | ^ { 2 }$ , and this inequality holds with equality exactly at $| z | = 1 \ \mathrm { o r } \ | w | = 1$ since $0 \leq ( 1 - | w | ^ { 2 } ) ( 1 - | z | ^ { 2 } )$ for $| z | , | w | \leq 1$ One computes that $F \circ F ( z ) = z$ and the rest of claims about F follows immediately from the inequality. 

Exercise 1.C. [SSh03, 1.9] Show that Cauchy-Riemann equations in polar coordinates is

$$
u _ { r } = { \frac { 1 } { r } } v _ { \theta } , \quad v _ { r } = - { \frac { 1 } { r } } u _ { \theta }
$$

Proof. With $x = r$ cos $\theta , y = r$ sin θ, computing du for $u : \mathbb { R } ^ { 2 }  \mathbb { R }$ in two coordinates $( x , y )$ and $( r , \theta )$ gives us (and likewise for dv):

$$
\left[ { \begin{array} { c c } { \cos \theta } & { \sin \theta } \\ { - r \sin \theta } & { r \cos \theta } \end{array} } \right] \left[ { \begin{array} { c } { u _ { x } } \\ { u _ { y } } \end{array} } \right] = \left[ { \begin{array} { c } { u _ { r } } \\ { u _ { \theta } } \end{array} } \right] , \quad \left[ { \begin{array} { c c } { \cos \theta } & { \sin \theta } \\ { - r \sin \theta } & { r \cos \theta } \end{array} } \right] \left[ { \begin{array} { c } { v _ { x } } \\ { v _ { y } } \end{array} } \right] = \left[ { \begin{array} { c } { v _ { r } } \\ { v _ { \theta } } \end{array} } \right]
$$

and thus we have

$$
\begin{array} { r } { \left[ r \cos \theta \quad - \sin \theta \right] \left[ u _ { r } \quad v _ { r } \right] = \left[ u _ { x } \quad v _ { x } \right] } \\ { r \sin \theta \quad \cos \theta \ \mathrm { ~ J ~ } \left[ u _ { \theta } \quad v _ { \theta } \right] = \left[ u _ { y } \quad v _ { y } \right] } \end{array}
$$

Now, $u _ { x } = v _ { y }$ and $u _ { y } = - v _ { x }$ becomes:

$$
( 1 ) : r \cos \theta u _ { r } - \sin \theta u _ { \theta } = r \sin \theta v _ { r } + \cos \theta v _ { \theta } , \quad ( 2 ) : r \sin \theta u _ { r } + \cos \theta u _ { \theta } = - r \cos \theta v _ { r } + \sin \theta v _ { \theta }
$$

And from here $( 1 ) \cdot \cos \theta + ( 2 )$ · sin θ gives us $r u _ { r } = v _ { \theta }$ , and −(1) · sin θ + (2) · cos θ gives us $r v _ { r } = - u _ { \theta } . $ as desired.

Exercise 1.D. [SSh03, 1.10,11] Show that $\begin{array} { r } { 4 \frac { \partial } { \partial z } \frac { \partial } { \partial \overline { { z } } } = 4 \frac { \partial } { \partial \overline { { z } } } \frac { \partial } { \partial z } = \Delta } \end{array}$ where ∆ is the Laplacian $\Delta =$ $\textstyle { \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } } + { \frac { \partial ^ { 2 } } { \partial y ^ { 2 } } }$ Moreover, show that if f is holomorphic on an open set Ω, then real and imaginary parts of f are harmonic, i.e. Laplacian is zero.

Proof. $4 \frac { 1 } { 2 } ( \partial _ { x } - i \partial _ { y } ) \frac { 1 } { 2 } ( \partial _ { x } + i \partial _ { y } ) = \Delta$ , and f holomorphic means $\begin{array} { r } { \frac { \partial f } { \partial \overline { { z } } } = 0 } \end{array}$ , and so $\Delta f = 0$

Exercise 1.E. [SSh03, 1.13] If f is holomorphic on an open set $\Omega ,$ and (i) Re(f ), or (ii) Im(f ), or $( i i i ) \mid f \mid$ is constant, then f is constant on Ω.

Proof. It suffices to show that $f ^ { \prime } = 0$ on Ω on any of the conditions given. For (i) or (ii), $\begin{array} { r } { { \frac { \partial f } { \partial z } } = } \end{array}$ $\begin{array} { r } { 2 { \frac { \partial u } { \partial z } } = i 2 { \frac { \partial v } { \partial z } } } \end{array}$ , so $f ^ { \prime } = 0$ . For (iii), $u ^ { 2 } + v ^ { 2 }$ is constant, and so applying $\partial _ { x x } , \partial _ { y y }$ to $( u ^ { 2 } + v ^ { 2 } ) = C$ gives us $\tilde { u } _ { x x } u + \tilde { v } _ { x x } v + ( u _ { x } ^ { 2 } + v _ { x } ^ { 2 } ) = 0 , u _ { y y } u + v _ { y y } v + ( u _ { y } ^ { 2 } + v _ { y } ^ { 2 } ) = 0$ . Adding the two and using the fact that $u , v$ are harmonic, we have that $u _ { x } = u _ { y } = v _ { x } = v _ { y } = 0$ 

Exercise 1.F. [SSh03, 1.14,15] Prove the summation by parts formula (defining $\begin{array} { r } { B _ { k } : = \sum _ { n = 1 } ^ { k } b _ { n } } \end{array}$ and $B _ { 0 } : = 0 )$ ),

$$
\sum _ { n = M } ^ { N } a _ { n } b _ { n } = a _ { N } B _ { N } - a _ { M } b _ { M - 1 } - \sum _ { n = M } ^ { N - 1 } ( a _ { n + 1 } - a _ { n } ) B _ { n }
$$

and use the formula to prove the Abel’s theorem: $I f \sum _ { n = 1 } ^ { \infty } a _ { n }$ converges, then

$$
\operatorname* { l i m } _ { r  1 ^ { - } } \sum _ { n = 1 } ^ { \infty } a _ { n } r ^ { n } = \sum _ { n = 1 } ^ { \infty } a _ { n }
$$

Proof. For the summation by parts formula, draw the $n \times n$ matrix $( a _ { i } b _ { j } ) _ { 1 \leq i , j \leq n }$ and consider what each terms in the summation mean. As for Abel’s theorem, something is weird since $f _ { N } ( r ) =$ $\textstyle \sum _ { n = 1 } ^ { N } a _ { n } r ^ { n }$ is continuous on $0 \leq r \leq 1$ and $f _ { N }  f$ uniformly (where $\textstyle f : = \sum _ { n = 1 } ^ { \infty } a _ { n } r ^ { n } )$ , we can commute the two limits. 

Exercise 1.G. [SSh03, 1.20] Show that: $( 1 ) \sum n z ^ { n }$ diverges for all points on the unit circle, (2) $\sum { \frac { 1 } { n ^ { 2 } } } z ^ { n }$ converges for all points on the unit circle, $( 3 ) \sum { \textstyle { \frac { 1 } { n } } } z ^ { n }$ converges for all points on the unit circle except $z = 1$

Proof. For (1), each terms don’t go to zero. For (2), absolute convergence. For (3), we need: Lemma: Suppose partial sums $A _ { n }$ of $\sum a _ { n }$ is a bounded sequence, and $b _ { 0 } \geq b _ { 1 } \geq b _ { 2 } \geq \cdot \cdot \cdot$ · with $\scriptstyle \operatorname* { l i m } _ { n \to \infty } b _ { n } = 0$ . Then $\sum a _ { n } b _ { n }$ is convergent. (Proof: use summation by parts formula).

This lemma also implies the Alternating Series Test with $a _ { n } = ( - 1 ) ^ { n }$ . For (3), we note that $a _ { n } = z ^ { n }$ satisfies the condition of the lemma for $| z | \leq 1 , z \neq 1$ 

## 2. Cauchy’s Theorem and Basic Applications

A curve $\gamma$ is assumed piecewise differentiable unless otherwise noted. A curve $\gamma$ is closed if the initial and end points are the same. A R-path is a curve entirely consisting of horizontal and vertical segments. Note that any region in C is R-path-connected.

A region Ω is simply-connected if $\pi _ { 1 } ( \Omega ) = 0$ , or equivalently, if any continuous map $S ^ { 1 } \to \Omega$ extends to $B ^ { 2 } \to \Omega$ , or equivalently, if complement of $\Omega$ in $\widehat { \mathbb { C } }$ is connected.

## 2.1. Cauchy’s Theorem.

Definition 2.2. For $f : \Omega \to \mathbb { C }$ and $\gamma : I  \Omega$ , we define the integral of f along $\gamma \ b y .$

$$
\int _ { \gamma } f d z : = \int _ { I } f ( \gamma ( t ) ) \gamma ^ { \prime } ( t ) d t
$$

Equivalently, the integral is the integration of a 1-form as follows: $\begin{array} { r } { \int _ { \gamma } ( u d x - v d y ) + i ( u d y + v d x ) } \end{array}$

Proposition 2.3. The defining length $\begin{array} { r } { . ( \gamma ) : = \int _ { \gamma } | d z | = \int _ { I } | \gamma ^ { \prime } ( t ) | d t } \end{array}$ , one has the following inequality:

$$
\left| \int _ { \gamma } f d z \right| \leq \int _ { \gamma } | f | | d z | \leq \left( \operatorname* { s u p } _ { \gamma } | f | \right) \cdot \operatorname { l e n g t h } ( \gamma )
$$

Theorem 2.4. For a 1-form $\omega = p d x + q d y$ on an open region Ω, $\textstyle { \int _ { \gamma } p d x + q d y = 0 }$ for any closed curve $\gamma$ in Ω if and only if ω is exact. Moreover, $i f \omega = d f$ , then for any $\gamma : [ a , b ] \to \Omega$ ,

$$
\int _ { \gamma } \omega = f ( \gamma ( b ) ) - f ( \gamma ( a ) )
$$

Proof. The second part is easy, and it implies one direction of the first part. For the converse, if the integral along any closed curve is zero, pick an arbitrary point $p \in \Omega$ and define $\begin{array} { r } { F ( z ) : = \int _ { \gamma } \omega } \end{array}$ for $z \in \Omega$ where $\gamma$ is a curve from p to z. By making γ an R-path, with last segment being horizontal or vertical, one recovers that $d F = \omega$ . 

Corollary 2.5. If $f : \Omega \to \mathbb { C }$ has a primitive, i.e. $F : \Omega  \mathbb { C }$ such that $F ^ { \prime } = f$ , then $\textstyle \int _ { \gamma } f = 0$ for all closed $\gamma \subset \Omega$

Proof. If $F = U + i V$ and $F ^ { \prime } = f = u + i v$ , then dF $ \phantom { + } = U _ { x } d x + U _ { y } d y + i ( V _ { x } d x + V _ { y } d y )$ and $u = U _ { x } = V _ { y } , v = V _ { x } = - U _ { y }$ , so that f as a 1-form equals dF . 

Theorem 2.6. [Goursat’s Theorem] If f is analytic on $R ,$ a rectangle with horizontal and vertical sides, then

$$
\int _ { \partial R } f d z = 0
$$

Proof. Keep subdividing rectangles into fours and pick ones with biggest integral and converge to $z _ { \mathrm { 0 } }$ . At each step, we have $| \eta ( R _ { n } ) | \geq 4 ^ { - n } | \eta ( R ) |$ |. Now, make n large enough $( R _ { n }$ small enough to z0) so that

$$
| f ( z ) - f ( z _ { 0 } ) - ( z - z _ { 0 } ) f ^ { \prime } ( z _ { 0 } ) | < \epsilon | z - z _ { 0 } |
$$

Note that $\textstyle \int _ { \partial R } d z \ = \ 0 \ = \ \int _ { \partial R } z d z$ , so integrating both sides of inequality above gives $| \eta ( R _ { n } ) | \ \leq$ $\begin{array} { r } { e \int _ { \partial R _ { n } } | z - z _ { 0 } | | d z | } \end{array}$ . Rest is computation. 

Proposition 2.7. Theorem 2.6 still holds if f is holomorphic on $R \backslash \{ z _ { 1 } , . . . , z _ { k } \} \ ( z _ { i } \in \operatorname { i n t } ( R ) )$ where

$$
\operatorname* { l i m } _ { z \to z _ { i } } ( z - z _ { i } ) f ( z ) = 0 \quad \forall i
$$

Proof. WLOG let $k = 1$ and use Theorem 2.6 to shrink the boundary of rectangle to a very small square centered at $z _ { 1 }$

Theorem 2.8. [Cauchy’s Theorem I] If f is holomorphic on an open disk D (or on D minus finite points satisfying the condition in Proposition 2.7), then for any closed $\gamma \subset D$ ,

$$
\int _ { \gamma } f d z = 0
$$

Proof. Construct the primitive of f as $\textstyle F ( z ) : = \int _ { \sigma } f d z$ where σ is an R-path from a pre-fixed point $p \ { \mathrm { t o } } \ z . \ F $ is well-defined due to Theorem 2.6 (Proposition 2.7). 

Theorem 2.9. Suppose f is holomorphic on open region Ω. Then $i f \gamma _ { 0 } , \gamma _ { 1 } \subset \Omega$ are homotopic (need be end-point homotopy), then

$$
\int _ { \gamma _ { 0 } } f d z = \int _ { \gamma _ { 1 } } f d z
$$

Proof. Let $\gamma _ { s } ( t ) : I \times I  \Omega$ be the homotopy. Since Im $( \gamma _ { s } ( t ) ) \subset \Omega$ is compact, there exists $\epsilon > 0$ such that any 3-ball around a point in Im $( \gamma _ { s } ( t ) )$ is contained in Ω. Also, there exist $\delta > 0$ such that sup $| \gamma _ { s _ { 0 } } ( t ) - \gamma _ { s _ { 1 } } ( t ) | < \epsilon$ whenever $| s _ { 0 } - s _ { 1 } | < \delta$ . Use these to make disks $\{ D _ { 0 } , \ldots , D _ { n } \}$ of radius 2, $2 \epsilon$ and consecutive points $\{ z _ { 0 } , \ldots , z _ { n + 1 } \} \subset \gamma _ { s _ { 0 } } , \{ w _ { 0 } , \ldots , w _ { n + 1 } \} \subset \gamma _ { s _ { 1 } }$ with $z _ { 0 } = w _ { 0 } , \ z _ { n + 1 } = w _ { n + 1 }$ such that $z _ { i } , z _ { i + 1 } , w _ { i } , w _ { i + 1 } \in D _ { i }$ . Now Theorem 2.8 integrals implies that integrals along closed curves $z _ { i } \stackrel { \mathrm { s t r a i g h t } } {  } w _ { i } \stackrel { \gamma _ { s _ { 1 } } } {  } w _ { i + 1 } \stackrel { \mathrm { s t r a i g h t } } {  } z _ { i + 1 } \stackrel { - \gamma _ { s _ { 0 } } } {  } z _ { i }$ is zero, and adding these up we have $\textstyle \int _ { - \gamma _ { s _ { 0 } } + \gamma _ { s _ { 1 } } } f d z = 0$ . To finish the proof, divide interval I into many pieces all of length less than δ. 

Theorem 2.10 (Cauchy’s Theorem II). If f is holomorphic on an simply-connected region Ω, then for any closed $\gamma \subset \Omega$

$$
\int _ { \gamma } f = 0
$$

Proof. Homotope γ to a constant map and use Theorem 2.9

Proposition 2.11. Let $a \in \mathbb { C }$ and $\gamma \textit { a }$ closed curve not going through a. Then the index of a point a with respect to $\gamma \ ( o r _ { ; }$ , the winding number $o f \gamma$ around $a )$ , defined as

$$
n ( \gamma , a ) : = \frac { 1 } { 2 \pi i } \int _ { \gamma } \frac { 1 } { z - a } d z
$$

is an integer. In fact, if $C ( \mathbb { C } \backslash \{ a \} )$ is the group of chains of closed curves in $\mathbb { C } \backslash \{ a \}$ , then the map $C ( \mathbb { C } \backslash \{ a \} )  \mathbb { Z }$ given by $\gamma \mapsto n ( \gamma , a )$ is the map $C ( \mathbb { C } \backslash \{ a \} )  H _ { 1 } ( \mathbb { C } \backslash \{ a \} ) \stackrel { \sim } {  } \mathbb { Z }$

Proof. Homotope $\gamma$ to lie on a circle centered at a and compute. For the second statement, note that $H _ { 1 }$ is the abelianization of $\pi _ { 1 }$ 

Proposition 2.12. Given a closed curve $\gamma ,$ , define the regions determined by $\gamma$ as the connected open components $o f \mathbb { C } - \gamma$ . Then the number $n ( \gamma , a )$ only depends on the region determined by γ that a belongs to.

Proposition 2.13. Let $C ( \Omega )$ be the group of chains of closed curves on open region Ω. Given $\gamma \in C ( \Omega )$ , we have that $[ \gamma ] = 0 \in H _ { 1 } ( \Omega )$ if and only if $n ( \gamma , a ) = 0$ for any $a \in \mathbb { C } - \Omega$ •

Theorem 2.14 (General Cauchy’s Theorem). If f is holomorphic on an open region Ω, then

$$
\int _ { \gamma } f d z = 0
$$

for all $\gamma \in C ( \Omega )$ such that $[ \gamma ] = 0 \in H _ { 1 } ( \Omega )$

Proof. TODO

## 2.15. Basic Applications of Cauchy’s Theorem.

Remark 2.16. Even before touching upon calculus of residues, one can compute many real integrals using toy-contours and Cauchy’s Theorem. (Examples in the Exercises)

Theorem 2.17 (Cauchy integral formulas). Let f be holomorphic on a region Ω, and ${ \overline { { D } } } \subset \Omega$ be a closed disk and $\dot { C } : = \partial \overline { { D } }$ . Then for any $z \in D$ ,

$$
f ( z ) = \frac { 1 } { 2 \pi i } \int _ { C } \frac { f ( \zeta ) } { \zeta - z } d \zeta
$$

Furthermore, one has that

$$
f ^ { ( n ) } ( z ) = { \frac { n ! } { 2 \pi i } } \int _ { C } { \frac { f ( \zeta ) } { ( \zeta - z ) ^ { n + 1 } } } d \zeta
$$

Proof. Fix $z _ { 0 } \in D$ . By Theorem 2.8 on $\begin{array} { r } { \int _ { C } \frac { f ( \zeta ) - f ( z _ { 0 } ) } { \zeta - z _ { 0 } } d \zeta = 0 } \end{array}$ , and linearity of integral gives $\begin{array} { r } { \int _ { C } \frac { f ( \zeta ) } { \zeta - z _ { 0 } } d \zeta = } \end{array}$ $n ( C , z _ { 0 } ) \cdot f ( z _ { 0 } )$ . The second part of the theorem follows from the following more general lemma:

Lemma 2.18. [Ahl79, 4.2.3] If φ(ζ) is continuous on an arc γ, then $\begin{array} { r } { F _ { n } ( z ) : = \int _ { \gamma } \frac { \phi ( \zeta ) } { ( \zeta - z ) ^ { n } } d \zeta } \end{array}$ is holomorphic in each region determined by γ and $F _ { n } ^ { \prime } ( z ) = n F _ { n + 1 } ( z )$

Theorem 2.19 (General Cauchy’s formula). Let f be holomorphic on a region Ω, and γ be a cycle such that $\gamma \sim 0 \in H _ { 1 } ( \Omega )$ . Then for any $z \in \Omega$ not on γ, we have

$$
n ( \gamma , z ) f ( z ) = \frac { 1 } { 2 \pi i } \int _ { \gamma } \frac { f ( \zeta ) } { \zeta - z } d \zeta
$$

Corollary 2.20 (Cauchy’s inequality). If f holomorphic on open Ω and $\overline { { D } } _ { R } ( z _ { 0 } ) \subset \Omega$ , then

$$
\vert f ^ { ( n ) } ( z _ { 0 } ) \vert \leq { \frac { n ! \Vert f \Vert _ { C } } { R ^ { n } } }
$$

where $\| f \| _ { C } = \operatorname* { s u p } _ { z \in C } | f ( z ) |$

Theorem 2.21 (Morera’s Theorem). If f is continuous on open Ω and $\textstyle { \int _ { \gamma } f d z = 0 }$ for all closed $\gamma \subset \Omega$ , then f is holomorphic on Ω.

Proof. Can define a primitive of f by $\textstyle F ( z ) : = \int _ { \sigma } f d z$ , and Theorem 2.17 implies that $F ^ { \prime } = f$ is holomorphic as well. 

Remark 2.22. In the above statement, since any open set can be covered by open disks, it suffices to check $\begin{array} { r } { \int _ { \partial R } f d z = 0 } \end{array}$ for every rectangle $R \subset \Omega$

Theorem 2.23 (Taylor’s Theorem I). Suppose f is holomorphic on a region Ω, and $\overline { { D } } _ { R } ( z _ { 0 } ) \subset \Omega$ Then for all $z \in D$ , f has a power series expansion

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n } \quad { \mathrm { w h e r e ~ } } a _ { n } = { \frac { f ^ { ( n ) } ( z _ { 0 } ) } { n ! } }
$$

Proof. Let $C = \partial \overline { { D } }$ and by Theorem 2.17 write $\begin{array} { r } { f ( z ) ~ = ~ \frac { 1 } { 2 \pi i } \int _ { C } \frac { f ( \zeta ) } { \zeta - z } d \zeta } \end{array}$ . Now, note that for any $| z - z _ { 0 } | < r$ with $r < R$ , we have a uniformly convergence series

$$
\sum _ { n = 0 } ^ { \infty } \left( { \frac { z - z _ { 0 } } { \zeta - z _ { 0 } } } \right) ^ { n } = { \frac { 1 } { 1 - { \frac { z - z _ { 0 } } { \zeta - z _ { 0 } } } } } = ( \zeta - z _ { 0 } ) { \frac { 1 } { \zeta - z } }
$$

Uniform convergence means that we can interchange integral and the summation, and hence

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { f ( \zeta ) } { ( \zeta - z _ { 0 } ) ^ { n + 1 } } } d \zeta \cdot ( z - z _ { 0 } ) ^ { n } = \sum _ { n = 0 } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }
$$

Corollary 2.24. Suppose f is holomorphic on $D _ { R } ( z _ { 0 } )$ . Then in the power series expansion $\scriptstyle \sum _ { n = 0 } ^ { \infty } a _ { n } ( z -$ $z _ { 0 } ) ^ { n }$ of f at z0, the coefficients $a _ { n }$ are given by

$$
a _ { n } = \frac { 1 } { 2 \pi r ^ { n } } \int _ { 0 } ^ { 2 \pi } f ( z _ { 0 } + r e ^ { i \theta } ) e ^ { - i n \theta } d \theta
$$

for any $0 < r < R$

Proof. Combine Theorem 2.17 and Theorem 2.23.

Corollary 2.25 (Mean-value property). If f is holomorphic on $D _ { R } ( z _ { 0 } )$ , and $\operatorname { R e } ( f ) = u$ , then

$$
f ( z _ { 0 } ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( z _ { 0 } + r e ^ { i \theta } ) d \theta \quad \mathrm { a n d } \quad u ( z _ { 0 } ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } u ( z _ { 0 } + r e ^ { i \theta } ) d \theta
$$

Theorem 2.26 (Analytic continuation). $I f f , g$ are analytic on a region Ω and agrees on a set with a limit point in Ω, then $f \equiv g . \ ( I f f = g$ on some open subset of Ω, then $f \equiv g )$

Proof. One shows that zeroes of non-zero analytic functions are isolated by using Theorem 2.23 as follows: let $E _ { 1 }$ be points where all derivatives vanish, and $E _ { 2 }$ be points where at least one derivative is nonzero; both are open. 

Theorem 2.27 (Liouville’s Theorem). If f is entire and bounded, then f is constant.

Proof. Show $f ^ { \prime } = 0$ on any $z _ { 0 } \in \mathbb { C }$ by Cauchy’s inequality.

Corollary 2.28 (Fundamental Theorem of Algebra). A polynomial $P ( z )$ has a root in C.

Theorem 2.29. If $\left\{ f _ { n } \right\}$ is holomorphic on a region Ω and $f _ { n }  f$ uniformly on every compact subset $o f \Omega$ , then f is holomorphic on Ω. Moreover, $f _ { n } ^ { \prime }  f ^ { \prime }$ uniformly on every compact subset of Ω.

Proof. Use uniform convergence to interchange limit and integral to find that f satisfies Morera’s Theorem. For the second part, prove for every closed disk. 

Often a holomorphic function is thus built as $\scriptstyle \sum _ { n = 0 } ^ { \infty } f _ { n } ( z )$ . (e.g. Zeta function). The following is the continuous version:

Proposition 2.30. For an open Ω, suppose $F : \Omega \times [ 0 , 1 ] \to \mathbb { C }$ be continuous and $F ( z , s )$ is holomorphic for each $s \in [ 0 , 1 ]$ . Then $f ( z ) : = \int _ { 0 } ^ { 1 } F ( z , s ) d s$ is holomorphic.

Let Ω be a symmetric open subset, in the sense that $z \in \Omega \Leftrightarrow \overline { { z } } \in \Omega$ (i.e. symmetric across the real-axis). In this case Ω partitions into $\Omega ^ { + } , \Omega ^ { - } , I$ , the upper, lower, real-line parts of Ω. The next two theorems are in this setting.

Theorem 2.31 (Symmetry principle). If f+ and $f ^ { - }$ are holomorphic on $\Omega ^ { + } , \Omega ^ { - }$ , and extends continuously to I with $f ^ { + } ( x ) = f ^ { - } ( x )$ for all $x \in I$ , then f defined piecewise accordingly on Ω is holomorphic.

Proof. At each open disk in Ω centered on a point on I, use Morera with -shifting and partitions of rectangles under consideration. 

Theorem 2.32 (Schwarz reflection principle). Suppose f is holomorphic on $\Omega ^ { + }$ and extends continuously to I with $f ( I ) \subset \mathbb { R }$ . Then there exist F holomorphic on Ω such that $F = f$ on $\Omega ^ { + }$

Proof. Define the lower half to be $F ( z ) = { \overline { { f ( { \overline { { z } } } ) } } }$ , and use the symmetry principle.

## 2.33. Exercises.

Exercise 2.A. [SSh03, 2.1,2] Evaluate the following integrals:

Fresnel integrals : $\int _ { 0 } ^ { \infty } \sin ( x ^ { 2 } ) d x = \int _ { 0 } ^ { \infty } \cos ( x ^ { 2 } ) d x = { \frac { \sqrt { 2 \pi } } { 4 } }$

$$
\int _ { 0 } ^ { \infty } { \frac { \sin { x } } { x } } d x = \frac { \pi } { 2 }
$$

Proof. Follow the hint.

Exercise 2.B. [SSh03, 2.7] Suppose $f : \mathbb { D }  \mathbb { C }$ is holomorphic, and let $d : = \dim ( f ( \mathbb { D } ) ) \ =$ $\operatorname* { s u p } _ { z , w \in \mathbb { D } } | f ( z ) - f ( w ) |$ . Then

$$
2 | f ^ { \prime } ( 0 ) | \leq d
$$

and equality holds precisely when $f$ is linear.

Proof. For any $0 ~ < ~ r ~ < ~ 1$ , we have that $\begin{array} { r } { 2 f ^ { \prime } ( 0 ) \ = \ \frac 1 { 2 \pi i } \int _ { \partial D _ { r } } \frac { f ( \zeta ) - f ( - \zeta ) } { \zeta ^ { 2 } } d \zeta } \end{array}$ , and thus $2 | f ^ { \prime } ( 0 ) | \ \leq$ $\textstyle { \frac { 1 } { 2 \pi } } { \frac { d } { r ^ { 2 } } } ( 2 \pi r ) = d / r$ for any $0 < r < 1$ . Hence, $2 | f ^ { \prime } ( 0 ) | \leq d ,$ as desired. That equality holds when $f$ is linear is clear. For converse, we first consider the following lemma:

Lemma: If f is holomorphic on D and non-constant, then $\exists z \in \mathbb { D }$ such that $| f ( 0 ) | < | f ( z ) |$ . (Proof: $\mathrm { I f } \ f ( 0 ) = 0$ where is nothing to prove. So assume not can let $R > 0$ be such that $f ( z ) \neq 0 \mathrm { o n } | z | < R .$ . Note that for by Cauchy integral formula we have $\begin{array} { r } { | f ( 0 ) | \le \frac { 1 } { 2 \pi } \int _ { \partial D _ { r } } \frac { | f ( \zeta ) | } { r } | d \zeta | } \end{array}$ for any $0 < r < R$ . If $| f ( 0 ) | = \operatorname* { s u p } _ { | \zeta | = r } | f ( \zeta ) |$ , then $| f ( \zeta ) | = | f ( 0 ) |$ constant, so that f is constant by [SSh03, 2.15]. Thus, $\| f ( 0 ) \vert < \mathrm { s u p } _ { | \zeta | = r } | f ( \zeta ) |$

Back to the main proof: now, use power series expansion and consider $f ( z ) - f ( - z )$ to conclude that if reserved for later. turns out this is a hard problem 

Exercise 2.C. [SSh03, 2.12] Let $u : \mathbb { D }  \mathbb { R }$ be $C ^ { 2 }$ and harmonic (i.e. $\Delta u = 0 )$ . Then show that there exists holomorphic $f$ on D such that $\operatorname { R e } ( f ) = u$ . Moreover, the imaginary part of $f$ is unique upto a (real) additive constant.

Proof. First, let $\begin{array} { r } { g ( z ) : = 2 \frac { \partial u } { \partial z } } \end{array}$ . Note that g is holomorphic on D since $\begin{array} { r } { \frac { \partial g } { \partial \overline { { z } } } = 2 \frac { \partial } { \partial \overline { { z } } } \frac { \partial } { \partial z } u = \frac { 1 } { 2 } \Delta u = 0 } \end{array}$ . By Cauchy’s Theorem there exists $F _ { ; }$ , unique upto (complex) additive constant, such that $F ^ { \prime } = g .$ . So, writing $F = U + i V + c$ (where $c \in \mathbb { C } )$ , that $( F - u ) ^ { \prime } = 0$ implies that $( U - u ) _ { x } = ( U _ { u } ) _ { y } = 0$ , and thus $U - u = \alpha$ for some $\alpha \in \mathbb { R }$ . Absorbing this into $c ,$ we have constructed $f = F = u + i V + c$ where c is imaginary. 

Exercise 2.D. [SSh03, 2.13] If f is holomorphic on a region Ω and for each $z _ { 0 } \in \Omega$ at least one coefficient in the power series expansion $\begin{array} { r } { f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } ( z - z _ { 0 } ) ^ { n } } \end{array}$ is zero. Then show that $f$ is a polynomial.

Proof. Define $S _ { n } : = \{ z \in \Omega : f ^ { ( n ) } ( z ) = 0 \}$ Since $\textstyle \bigcup _ { n \in \mathbb { N } } S _ { n } \ = \ \Omega$ , there is N such that $S _ { N }$ is uncountable. Thus, $f ^ { ( N ) } ( z )$ has zeroes that accumulate, and hence is identically zero. 

Exercise 2.E. [SSh03, 2.15] Suppose f is continuous and non-zero on $\overline { { \mathbb { D } } }$ and holomorphic on D such that $| f ( z ) | \overset { } { = } 1 f o r a l l | z | = 1$ . Show that f is then constant.

Proof. Note that for any g holomorphic on $U \subset \mathbb { C }$ open, if $\phi : \mathbb { C } \to \mathbb { C }$ is the conjugation map, then $\widetilde { g } ( z ) : = \overline { { f ( \overline { { z } } ) } }$ is holomorphic on $\phi ^ { - 1 } ( U )$ . Thus, we can extend $f$ to $| z | > 1$ by defining $\begin{array} { r } { f ( z ) : = \frac { 1 } { f ( \frac { 1 } { \overline { { z } } } ) } } \end{array}$ (that $| f | = 1 \mathrm { a t } | z | = 1$ condition implies that the two $f \mathrm { ^ { \prime } s }$ match at $| z | = 1 )$ . Now, using Morera’s theorem with rectangles (and continuity of $f )$ , we have that $f$ is entire, and since $f$ was non-zero on $\overline { { \mathbb { D } } } , f$ is bounded. By Liouville’s theorem, $f$ is thus constant. 

## 3. Meromorphic Functions and the Logarithm

## 3.1. Zeroes, singularities, meromorphic functions.

Definition 3.2. A point $z _ { 0 } \in \mathbb { C }$ is a (point/isolated singularity of f if f is defined in a neighborhood $o f z _ { 0 }$ but not at $z _ { \mathrm { 0 } }$ .

There are three types of point singularities: removable, poles, and essential singularities.

Theorem 3.3. Suppose f is analytic on $\Omega \backslash \{ z _ { 0 } \}$ Then $f$ can be extended to analytic function on Ω if and only $i f \operatorname * { l i m } _ { z \to z _ { 0 } } ( z - z _ { 0 } ) f ( z ) = 0 \ ( i . e . \ ,$ f is bounded on a neighborhood $o f z _ { 0 } )$ , and the extension is unique.

Proof. By Proposition 2.7, we have that $\begin{array} { r } { f ( z ) = \frac { 1 } { 2 \pi i } \int _ { C } \frac { f ( \zeta ) } { \zeta - z } d \zeta } \end{array}$ is valid for $z \neq z _ { 0 }$ for a circle $C \subset \Omega$ centered at $z _ { \mathrm { 0 } }$ , but the RHS expression is analytic inside the circle by Lemma 2.18, so extend $f$ as the integral formula expresses. 

As a result of this theorem, isolated singularities that satisfy the condition in Theorem 3.3 are called removable singularities.

Theorem 3.4 (Taylor’s Theorem II). If f is analytic on a region $\Omega \ni z _ { 0 }$ , then it is possible to write

$$
f ( z ) = \left( \sum _ { k = 0 } ^ { n - 1 } \frac { f ^ { ( k ) } ( z _ { 0 } ) } { k ! } ( z - z _ { 0 } ) ^ { k } \right) + f _ { n } ( z ) ( z - z _ { 0 } ) ^ { n }
$$

where $f _ { n }$ is analytic on Ω.

Proof. Apply Theorem 3.3 to $\begin{array} { r } { F ( z ) = \frac { f ( z ) - f ( z _ { 0 } ) } { z - z _ { 0 } } } \end{array}$ for case $n = 1$ , and induct using the same idea. 

Theorem 3.5. If f is analytic on a region Ω, does not vanish identically on $\Omega ,$ and $f ( z _ { 0 } ) = 0$ , then there exists $g ( z )$ analytic on Ω and nonzero in a neighborhood of $z _ { \mathrm { 0 } }$ , and a unique n, such that

$$
f ( z ) = ( z - z _ { 0 } ) ^ { n } g ( z )
$$

(in which case, we say $z _ { \mathrm { 0 } }$ is a zero of order n).

Definition 3.6. A function f has a pole at z0 $i f 1 / f$ , defined to be 0 at $z _ { \mathrm { 0 } }$ , is analytic in a neighborhood of z0. Equivalently, z0 is a pole of f if $\begin{array} { r } { \operatorname* { l i m } _ { z \to z _ { 0 } } f ( z ) = \infty } \end{array}$

Theorem 3.7. If f has a pole at $z _ { \mathrm { 0 } }$ , then there exists h holomorphic and nonzero on a neighborhood $o f z _ { 0 } .$ , and a unique $n ,$ such that

$$
f ( z ) = ( z - z _ { 0 } ) ^ { - n } h ( z )
$$

(in which case, $z _ { \mathrm { 0 } }$ is a pole of order/multiplicity n).

Corollary 3.8. If f has a pole of order n at $z _ { 0 }$ , then

$$
f ( z ) = { \frac { a _ { - n } } { ( z - z _ { 0 } ) ^ { n } } } + \cdot \cdot \cdot + { \frac { a _ { - 1 } } { z - z _ { 0 } } } + G ( z )
$$

where $G ( z )$ is holomorphic on a neighborhood of $z _ { \mathrm { 0 } }$

Theorem 3.9 (Casorati-Weierstrass). Suppose f is holomorphic on a neighborhood of $z _ { \mathrm { 0 } }$ but not on $z _ { \mathrm { 0 } }$ , which is an essential singularity (point singularity that is neither removable or a pole). Then the image of any (punctured) neighborhood of $z _ { \mathrm { 0 } }$ under f is dense in $\mathbb { C } .$

Proof. Let D be a small disk around $z _ { 0 } .$ and suppose there exists w with $r > 0$ such that $D _ { r } ( w ) \cap$ $f ( D ) = \varnothing$ . Now, consider the function $\begin{array} { r } { g ( z ) : = \frac { 1 } { f ( z ) - w } } \end{array}$ . Note that $g ( z )$ is bounded on $D _ { : }$ , and hence has a removable singularity at $z _ { \mathrm { 0 } }$ . If $g ( z _ { 0 } ) \neq 0$ , then f has removable singularity at $z _ { \mathrm { 0 } }$ , and if $g ( z _ { 0 } ) = 0$ , then $f ( z ) - w$ has a pole at $z _ { \mathrm { 0 } }$ , which means $f ( z )$ has a pole at $z _ { \mathrm { 0 } }$ . Either case, we get a contradiction. 

Definition 3.10. If f is holomorphic on an unbounded region, we say that f has a removable/pole/essential singularity at ∞ if $F ( z ) : = f ( 1 / z )$ has the corresponding singularity at $z = 0$

Definition 3.11. A function f is meromorphic on an open set Ω if it is holomorphic on Ω except for a discrete set of points which are poles of f .

Theorem 3.12. The meromorphic functions on $\widehat { \mathbb { C } }$ are the rational functions.

Proof. Given f meromorphic on ${ \widehat { \mathbb { C } } } ,$ subtract off principal part of f at each poles to get a bounded holomorphic function on C, which must be constant. 

## 3.13. The calculus of residues.

Definition 3.14. Suppose f has a pole of order n at $z _ { 0 . }$ , so that by Corollary $3 . 8$ we can write $f ( z ) = { \frac { a _ { - n } } { ( z - z _ { 0 } ) ^ { n } } } + \cdots + { \frac { a _ { - 1 } } { z - z _ { 0 } } } + { \bar { G ( z ) } }$ . We call the $\textstyle { \frac { a _ { - n } } { ( z - z _ { 0 } ) ^ { n } } } + \cdots + { \frac { a _ { - 1 } } { z - z _ { 0 } } }$ part the principal part of f at pole $z _ { 0 } ,$ and define the residue of f at pole z0 as $\mathrm { R e s } _ { z _ { 0 } } f : = a _ { - 1 }$

Proposition 3.15. If f has a pole of order n at $z _ { \mathrm { 0 } }$ , then

$$
{ \mathrm { R e s } } _ { z _ { 0 } } f = \operatorname* { l i m } _ { z  z _ { 0 } } { \frac { 1 } { ( n - 1 ) ! } } ( { \frac { \partial } { \partial z } } ) ^ { n - 1 } ( z - z _ { 0 } ) ^ { n } f ( z )
$$

Theorem 3.16 (Residue formula). Let f be analytic on a region Ω except for poles $z _ { 1 } , \dotsc , z _ { N } \in \Omega$ Then, for any cycle $\gamma \sim 0 \in H _ { 1 } ( \Omega )$ and not passing through any of $z _ { j } \ { } ^ { \prime } s _ { \mathrm { : } }$ we have

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } f d z = \sum _ { j = 1 } ^ { N } n ( \gamma , z _ { j } ) \operatorname { R e s } _ { z _ { j } } f
$$

In particular, $i f \gamma$ is a toy-contour in Ω containing $z _ { 1 } , \dots , z _ { N }$ , then we have

$$
\int _ { \gamma } f d z = 2 \pi i \sum _ { j = 1 } ^ { N } \mathrm { R e s } _ { z _ { j } } f
$$

Proof. Note that $\gamma \sim 0$ in Ω implies that $\begin{array} { r } { \gamma \sim \sum _ { j = 1 } ^ { N } n ( \gamma , z _ { j } ) C _ { j } } \end{array}$ in $\Omega \backslash z _ { 1 } , \ldots , z _ { N }$ for some circles $C _ { j }$ centered at $z _ { j }$ . For each $C _ { j }$ use Corollary 3.8. 

Example 3.17. [Ahl79, 4.5.3] One can show (in increasing generalities) that for a rational function $R ( x )$ such that $R ( \infty ) = 0$ and poles on the real line are simple, we get

$$
\int _ { - \infty } ^ { \infty } R ( x ) e ^ { i x } = 2 \pi i \sum _ { y > 0 } \mathrm { R e s } _ { y } R ( z ) e ^ { i z } + \pi i \sum _ { y = 0 } \mathrm { R e s } _ { y } R ( z ) e ^ { i z }
$$

## 3.18. The argument principle & applications.

Theorem 3.19 (Argument principle). Suppose f is meromorphic on an open Ω with zeroes $\{ a _ { j } \}$ and poles $\{ b _ { k } \}$ (repeated to each order), and $\gamma$ is a cycle such that $\gamma \sim 0 \in H _ { 1 } ( \Omega )$ and does not go through zeroes or poles of f. Then

$$
\frac { 1 } { 2 \pi i } \int _ { \gamma } \frac { f ^ { \prime } ( z ) } { f ( z ) } d z = \sum _ { j } n ( \gamma , a _ { j } ) - \sum _ { k } n ( \gamma , b _ { k } )
$$

Proof. Apply the residue formula (Theorem 3.16) to $f ^ { \prime } / f$

Corollary 3.20. If f is meromorphic on an open set containing a circle C and its interior, and f has no zeroes or poles on C, then

$$
{ \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z = ( { \mathrm { n u m b e r ~ o f ~ z e r o e s ~ i n s i d e ~ } } C ) - ( { \mathrm { n u m b e r ~ o f ~ p o l e s ~ i n s i d e ~ } } C )
$$

where the zeros and poles are counted with multiplicity.

Theorem 3.21 (Rouche’s theorem). If f and g are holomorphic on an open set containing a circle C and its interior, and $| f ( z ) | > | g ( z ) |$ for all $z \in C$ , then f and $f + g$ have the same number of zeros in C.

Proof. Define $f _ { t } ( z ) = f ( z ) + t g ( z )$ for $t \in [ 0 , 1 ]$ , which is continuous jointly in $t , z$ . Note that $| f ( z ) | > | g ( z ) |$ implies that $f _ { t } ( z ) \neq 0$ for all t in a neighborhood of C. Thus, we can define

$$
n _ { t } : = \frac { 1 } { 2 \pi i } \int _ { C } \frac { f _ { t } ^ { \prime } ( z ) } { f _ { t } ( z ) } d z
$$

Since $n _ { t }$ is continuous in t, it must be constant, and hence $n _ { 0 } = n _ { 1 }$ , as desired.

Theorem 3.22 (open mapping theorem). If f is holomorphic and non-constant on Ω, then f is open.

Proof. Fix arbitrary $z _ { \mathrm { 0 } }$ and let $w _ { 0 } : = f ( z _ { 0 } )$ . Choose $\delta > 0$ such that $B _ { \delta } ( z _ { 0 } ) \subset \Omega$ and $f ( z ) \neq w _ { 0 }$ on $\left. z - z _ { 0 } \right. = \delta _ { \mathrm { { \ t } } }$ δ, and $\epsilon > 0$ such that $| f ( z ) - w _ { 0 } | \geq \epsilon \mathrm { ~ o n ~ } | z - z _ { 0 } | = \delta$ . Now, note that for any w such that $| w - w _ { 0 } | < \epsilon .$ by Rouche’s theorem we have that $g ( z ) : = f ( z ) - w = ( f ( z ) - w _ { 0 } ) + ( w _ { 0 } - w ) =$ $F ( z ) + G ( z )$ has a root in $| z - z _ { 0 } | < \delta$ . 

Theorem 3.23 (maximum modulus principle). If f is holomorphic and non-constant on a region Ω, then f cannot attain a maximum (i.e. maximum in modulus $| f ( z ) | )$ in Ω.

Proof. $\mathrm { I f } \mid f ( z _ { 0 } ) \mid$ is max, then consider $f ( D )$ where D is a small disk around $z _ { 0 } .$ , which is open. 

Corollary 3.24. Suppose Ω is a region with compact closure Ω. If f is holomorphic on Ω and continuous on Ω, then

$$
\displaystyle \operatorname* { s u p } _ { z \in \Omega } | f ( z ) | \leq \operatorname* { s u p } _ { \overline { { \Omega } } - \Omega } | f ( z ) |
$$

## 3.25. Complex logarithm.

Proposition 3.26. Suppose Ω is simply connected with $1 \in \Omega$ and $0 \not \in \Omega$ . Then in Ω there is a branch of the logarithm $F ( z ) = \log z $ such that F is holomorphic on $\Omega , \dot { e } ^ { F ( z ) } = z f o r \ a l l \ z \in \Omega$ , and $F ( r ) = \log r$ whenever r is real number near 1.

Example 3.27. In the split plane $\Omega = \mathbb { C } - \{ ( - \infty , 0 ] \}$ , we have the principal branch log $z =$ log $r + i \theta$ where $| \theta | < \pi$ . For $\alpha \in \mathbb { C } , z ^ { \alpha }$ is defined as $z ^ { \alpha } : = e ^ { \alpha \log z }$ on Ω

Theorem 3.28. If f is nowhere vanishing holomorphic on simply connected region Ω, then there exists g holomorphic on Ω such that

$$
f ( z ) = e ^ { g ( z ) }
$$

$$
( i . e . ~ g ( z ) = \log f ( z ) ) .
$$

Proof. Fixing $z _ { 0 } \in \Omega$ , define $\begin{array} { r } { g ( z ) = \int _ { \gamma } \frac { f ^ { \prime } ( \zeta ) } { f ( \zeta ) } d \zeta + c _ { 0 } } \end{array}$ for γ path from $z _ { \mathrm { 0 } }$ to z and $e ^ { c _ { 0 } } = f ( z _ { 0 } )$

## 3.29. Exercises.

Exercise 3.A. [SSh03, 3.1] Show that the complex zeros of sin πz are exactly at the integers, and are each of order 1. Calculate the residue of 1/ sin πx are $z = n \in \mathbb { Z }$

Solution. Since sin $\begin{array} { r } { \pi z = \frac { e ^ { i \pi z } - e ^ { - i \pi z } } { 2 i } } \end{array}$ , we have that sin πx $: = 0 \implies e ^ { i 2 \pi z } = 1$ , and writing $z = x + i y .$ one obtains $e ^ { i 2 \pi x } e ^ { - 2 \pi y } = 1$ , so that $y = 0$ and $x = n \in \mathbb { Z }$ . Power series expanding sin πz at $n \in \mathbb { Z }$ gives $\begin{array} { r } { \sum _ { k = 1 } ^ { \infty } \pi ( z - n ) - \frac { \pi ^ { 3 } } { 3 ! } ( z - n ) ^ { 3 } + \cdot \cdot \cdot } \end{array}$ if n is even, and the opposite if n is odd. Hence, the zeros are of order 1, and the residues for 1/ sin πz are $1 / \pi$ for n even and $- 1 / \pi$ for n odd. 

Exercise 3.B. [SSh03, 3.6] Show that for $n \geq 1$

$$
\int _ { - \infty } ^ { \infty } { \frac { d x } { ( 1 + x ^ { 2 } ) ^ { n + 1 } } } = { \frac { ( 2 n ) ! } { 4 ^ { n } ( n ! ) ^ { 2 } } } \pi
$$

Proof. Note that $\textstyle f ( z ) : = { \frac { 1 } { ( 1 + z ^ { 2 } ) ^ { n + 1 } } }$ has poles i and −i of order $n + 1$ . So, [above integral equals $\begin{array} { r } { 2 \pi i \operatorname { R e s } _ { i } f = \operatorname* { l i m } _ { z  i } \frac { 1 } { n ! } ( \frac { \partial } { \partial z } ) ^ { n } \frac { ( z - i ) ^ { n + 1 } } { ( 1 + z ^ { 2 } ) ^ { n + 1 } } = 2 \pi i \frac { ( 2 n ) ! } { ( n ! ) ^ { 2 } } \frac { ( - 1 ) ^ { n } } { ( 2 i ) ^ { 2 n + 1 } } = \frac { ( 2 n ) ! } { 4 ^ { n } ( n ! ) ^ { 2 } } \pi . } \end{array}$ 

Exercise 3.C. [SSh03, 3.8] Prove that

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { a + b \cos \theta } } = { \frac { 2 \pi } { \sqrt { a ^ { 2 } - b ^ { 2 } } } }
$$

Proof. Letting $z = e ^ { i \theta }$ , we can rewrite the integral as (where C is unit circle)

$$
\int _ { C } { \frac { 1 } { a + b \cdot { \frac { 1 } { 2 } } ( z + { \frac { 1 } { z } } ) } } { \frac { d z } { i z } } = 2 \pi i \operatorname { R e s } _ { z _ { 0 } \in \mathbb { D } } f
$$

which gives us the desired result.

Exercise 3.D. [SSh03, 3.10] Show that for $a > 0$

$$
\int _ { 0 } ^ { \infty } { \frac { \log x } { x ^ { 2 } + a ^ { 2 } } } d x = { \frac { \pi } { 2 a } } \log a
$$

Proof. Define log z on $\mathbb { C } - \left\{ ( 0 , y ) : y \leq 0 \right\}$ by log $z = \log | z | + i \theta$ where $\theta \in \left( { - \pi / 2 , 3 \pi / 2 } \right)$ . Using the dented semicircle γ as the contour, and noting that ${ \frac { r \log r } { r ^ { 2 } + a ^ { 2 } } } \to 0$ as $r  0$ or $r  \infty$ , one computes that

$$
2 \pi i \cdot { \frac { \log ( i a ) } { 2 i a } } = \int _ { \gamma } { \frac { \log z } { z ^ { 2 } + a ^ { 2 } } } d z = \int _ { - \infty } ^ { 0 } { \frac { \log ( - x ) + i \pi } { x ^ { 2 } + a ^ { 2 } } } d x + \int _ { 0 } ^ { \infty } { \frac { \log x } { x ^ { 2 } + a ^ { 2 } } } d x
$$

and thus we have $\begin{array} { r } { \frac { \pi \log a } { a } + \frac { i \pi ^ { 2 } } { 2 a } = 2 \int _ { 0 } ^ { \infty } \frac { \log x } { x ^ { 2 } + a ^ { 2 } } + \frac { i \pi ^ { 2 } } { 2 a } } \end{array}$ , and the desired equality follows.

Exercise 3.E. [SSh03, 3.14] Prove that all entire functions that are also injective take the form $ f ( z ) = a z + b$ with $a , b \in \mathbb { C }$ and $a \neq 0$ .

Proof. If f is meromorphic on $\widehat { \mathbb { C } } .$ then f is a rational function, but since f entire, it is a polynomial and injectivity implies that $f$ is then linear. If f has essential singularity at infinity, then $f ( \mathbb { C } \backslash \mathbb { D } )$ must be dense in C, but then since $f$ is an open map, $f ( \mathbb { C } \backslash \mathbb { D } ) \cap f ( \mathbb { D } ) \neq \emptyset$ , and hence injectivity implies that f cannot have essential singularity at infinity. 

Exercise 3.F. [SSh03, 3.15] Prove the following statements:

(1) If f is an entire function satisfying $\begin{array} { r } { \operatorname* { s u p } _ { | z | = R } | f ( z ) | \leq A R ^ { k } + B } \end{array}$ for some A, $B \geq 0$ and $k \in \mathbb N$ then f is polynomial of $d e g r e e \le k$

(2) If f is holomorphic on D, is bounded, and converges uniformly to zero in the sector $\theta \ <$ $\arg z < \phi \ a s \ | z |  1$ , then $f = 0$

(3) Let $w _ { 1 } , \ldots , w _ { n }$ be on the unit circle C. Then $\exists z \in C$ such that $| z - w _ { 1 } | \cdot \cdot \cdot | z - w _ { n } | = 1$

(4) If the real part of an entire function f is bounded, then f is constant.

(1) Cauchy inequality implies that $f ^ { ( n ) } ( 0 ) = 0$ for all $n > k$

(2) ASK

(3) Note that $C $ R given by $z \mapsto | z - w _ { 1 } | \cdot \cdot \cdot | z - w _ { n } |$ is continuous, so it suffices to show that for some $z \in C , | z - w _ { 1 } | \cdot \cdot \cdot | z - w _ { n } | \geq 1$ . Well, $( z - w _ { 1 } ) \cdot \cdot \cdot ( z - w _ { n } )$ is holomorphic on D, then achieves modulus 1 when $z = 0 ,$ , so the maximum principle gives us the desired $z \in C$

(4) If f has essential singularity at infinity, then the real part is not bounded by Casorati-Weierstrass. But if f is meromorphic, then f is a polynomial and hence is constant.

Exercise 3.G. [SSh03, 3.16] Suppose f and g are holomorphic on a region containing ${ \overline { { \mathbb { D } } } } ,$ and suppose f has a simple zero at $z = 0$ with no other zeroes on D. Then $f _ { \epsilon } ( z ) = f ( z ) + \epsilon g ( z )$ has a unique zero in D for  sufficiently small, and $i f z _ { \epsilon }$ is the zero of f, then $\epsilon \mapsto z _ { \epsilon }$ is continuous.

Proof. For a small enough $\epsilon > 0$ , we have inf $\dot { | z | } = 1 \left| f \right| > \epsilon \operatorname { s u p } _ { | z | = 1 } \left| g \right|$ , so that by Rouche’s theorem $f _ { \epsilon }$ has a unique zero in ${ \overline { { \mathbb { D } } } } .$ Moreover, let $\{ \delta _ { n } \}$ sequence of numbers converging to $\delta < \epsilon$ . We need show that $z _ { \delta _ { n } }  z _ { \delta }$ Well, if $\{ z _ { \delta _ { n } } \} \subset \overline { { \mathbb { D } } }$ does not converge to $z _ { \delta }$ then it has a subsequence that converges to some w $\neq z _ { \delta }$ . But since $F : \overline { { \mathbb { D } } } \times \mathbb { R }  \mathbb { C }$ defined as $F ( z , \epsilon ) : = f _ { \epsilon } ( z )$ is continuous, and $( \delta _ { n } , z _ { \delta _ { n } } )  ( \delta , w )$ , we have $f _ { \delta } ( w ) = F ( w , \delta ) = 0$ , which contradicts uniqueness of the zero of $f _ { \delta }$ . 

Exercise 3.H. [SSh03, 3.17] Let f be non-constant and holomorphic on an open set containing D. $I f f \left| f ( z ) \right| = 1 \ o n \ | z | = 1 , \ o r \ i f \left| f ( z ) \right| \geq 1 \ o n \ | z | = 1$ and there exists $z _ { \in } \mathbb { D }$ such that $| f ( z _ { 0 } ) | < 1$ , then the image of f contains the unit disk.

Proof. In both cases, by Rouche’s theorem $f ( z ) = w$ has a root for every $w \in \mathbb { D } \mathrm { ~ i f ~ } f ( z ) = 0$ has a root. But if $f ( z ) = 0$ has no root, then $1 / f$ defined on D achieves its maximum in the interior D (by maximum principle for the first case, obvious in the second case). 

Exercise 3.I. [SSh03, 3.19] Prove the maximum principle for harmonic functions.

Proof. Suppose an harmonic function u defined on an open set Ω achieves a local maximum M at $z _ { 0 } \in \Omega$ . We know that there exists a holomorphic function f on Ω such that $\operatorname { R e } ( f ) = u$ . Then f is not open since $f ( z _ { 0 } ) = M + i b$ , and no neighborhood of $M + i b$ is contained in the image $f ( D )$ where D is a small neighborhood of $z _ { \mathrm { 0 } }$ 

Exercise 3.J (Laurent Series Expansion). [SSh03, Problem 3.3] Suppose f is analytic on a region containing the annulus $\{ r _ { 1 } \le | z - z _ { 0 } | \le r _ { 2 } \}$ . Then, we can write (uniquely)

$$
f ( z ) = \sum _ { n = - \infty } ^ { \infty } a _ { n } ( z - z _ { 0 } ) ^ { n }
$$

where the series converges absolutely in the interior of the annulus.

Proof. By Theorem 2.14, one can write

$$
f ( z ) = { \frac { 1 } { 2 \pi i } } \int _ { C _ { r _ { 1 } } } { \frac { f ( \zeta ) } { \zeta - z } } d \zeta - { \frac { 1 } { 2 \pi i } } \int _ { C _ { r _ { 2 } } } { \frac { f ( \zeta ) } { \zeta - z } } d \zeta
$$

and use the series expansion of $1 / ( \zeta - z ) = \frac { 1 } { ( \zeta - z _ { 0 } ) - ( z - z _ { 0 } ) }$ appropriately in each case.

## 4. Conformal Maps

## 4.1. Conformal equivalence and examples.

Proposition 4.2. If $f : U \to V$ for $U , V \subset \mathbb { C }$ open is holomorphic and injective, then $f ^ { \prime } ( z _ { 0 } ) \neq 0$ for all $z _ { 0 } \in U$ . Moreover, as a result the inverse of f defined on its image is holomorphic.

Proof. Write $f ( z ) - f ( z _ { 0 } ) = a _ { k } ( z - z _ { 0 } ) ^ { k } + [ ( z - z _ { 0 } ) ^ { k + 1 } ]$ and use Rouche’s theorem to conclude that $f ( z ) - f ( z _ { 0 } )$ is not injective. Second part follows: $\begin{array} { r } { ( f ^ { - 1 } ) ^ { \prime } ( f ( z _ { 0 } ) ) = \frac { 1 } { f ^ { \prime } ( z _ { 0 } ) } } \end{array}$ 

Definition 4.3. A map holomorphic map $f : U \to V$ with $f ^ { \prime } ( z _ { 0 } ) \neq 0 \forall z _ { 0 } \in U$ is called conformal map. If f is bijective, then it is called a biholomorphism (note that its inverse is also holomorphic), in which we say U, V are conformally equivalent.

Example 4.4. Translations $z \mapsto z + a$ and rotation+dilation given by $z \mapsto c z , ~ ( c \in \mathbb { C } )$ are conformal equivalences $\mathbb { C } \overset { \sim } { \to } \mathbb { C }$ .

Example 4.5. Let $\mathbb { H } : = \{ z \in \mathbb { C } : \operatorname { I m } ( z ) > 0 \}$ be the upper half-plane. H and the unit disk D are conformally equivalent. One equivalence is given by $F : \mathbb { H }  \mathbb { D } , G : \mathbb { D }  \mathbb { H }$ where

$$
F ( z ) = { \frac { i - z } { i + z } } , \quad G ( w ) = i { \frac { 1 - w } { 1 + w } }
$$

Example 4.6. For $0 < \alpha < 2$ , the map $f ( z ) = z ^ { \alpha }$ defined in terms of the principal branch is a biholomorphic map from H to the sector $S = \{ w \in \mathbb { C } : 0 < \arg ( w ) < \alpha \pi \}$

Example 4.7. The map $f ( z ) = \log { z }$ is a biholomorphism from H to a region $\{ a + b i : a \in \mathbb { R } , 0 <$ $b < \pi \}$ . It also biholomorphically maps upper unit disk to $\{ a + b i : a < 0 , 0 < b < \pi \}$

## 4.8. The Mobius transformations.

Definition 4.9. We call maps of the following form a Mobius transformation / (fractional) linear map:

$$
f ( z ) = { \frac { a z + b } { c z + d } }
$$

for $a , b , c , d \in \mathbb { C }$ such that $a d - b c \neq 0$

Remark 4.10. Noting the identification $\mathbb { C P } ^ { 1 } \simeq \widehat { \mathbb { C } }$ , we see that a Mobius map computed in $\mathbb { C P } ^ { 1 }$ is $[ z _ { 1 } : z _ { 2 } ]  [ a z _ { 1 } + b z _ { 2 } : c z _ { 1 } + d z _ { 2 } ]$ . In other words, it really is a linear transformation in homogeneous coordinates made by multiplying matrix $M = { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] } { \mathrm { ~ t o ~ } } { \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \end{array} \right] }$ . In this view, one sees that matrices of $P S L _ { 2 } ( \mathbb { C } )$ correspond exactly to different Mobius maps, and so a Mobius map is determined by image of three distinct points. Moreover, composition of Mobius maps corresponds to matrix multiplication. Indeed, it is thus a biholomorphic map $\widehat { \mathbb { C } } \ \overset { \sim } {  } \widehat { \mathbb { C } }$ . Moreover,

Proposition 4.11. Given three distinct points $z _ { 2 } , z _ { 3 } , z _ { 4 } \in \widehat { \mathbb { C } }$ , the Mobius map T that maps z2, z3, z4 to 1, 0, ∞, respectively, is given by

$$
f ( z ) = { \frac { ( z - z _ { 3 } ) ( z _ { 2 } - z _ { 4 } ) } { ( z - z _ { 4 } ) ( z _ { 2 } - z _ { 3 } ) } }
$$

$( i f z _ { 2 } , z _ { 3 } , o r z _ { 4 } = \infty$ , just cancel the terms with it). We denote the above f (z) by $( z , z _ { 2 } , z _ { 3 } , z _ { 4 } )$ called the cross ratio.

Theorem 4.12. For distinct points $z _ { 1 } , z _ { 2 } , z _ { 3 } , z _ { 4 } \in \widehat { \mathbb { C } }$ and T a Mobius map, $( T z _ { 1 } , T z _ { 2 } , T z _ { 3 } , T z _ { 4 } ) =$ $( z _ { 1 } , z _ { 2 } , z _ { 3 } , z _ { 4 } )$ . And hence, T that maps $z _ { 2 } , z _ { 3 } , z _ { 4 } )$ to $w _ { 2 } , w _ { 3 } , w _ { 3 }$ is obtained by writing $( w , w _ { 2 } , w _ { 3 } , w _ { 4 } ) =$ $( z , z _ { 2 } , z _ { 3 } , z _ { 4 } )$ and solving for w.

Example 4.13. Fractional linear map gives us abundance of biholomorphism, especially when we use them to rotate the Riemann sphere. The map $\begin{array} { r } { z \mapsto ( z , i , 1 , - 1 ) = \frac { ( z - 1 ) ( i + 1 ) } { ( z + 1 ) ( i - 1 ) } = i \frac { 1 - z } { 1 + z } } \end{array}$ is the map $G : \mathbb { D }  \mathbb { H }$ in Example 4.5. In another case, $\begin{array} { r } { z \mapsto ( z , 0 , - 1 , 1 ) = \frac { ( z + 1 ) ( - 1 ) } { ( z - 1 ) ( 1 ) } = \frac { 1 + z } { z - 1 } } \end{array}$ maps upper half-disk to the first quadrant.

## 4.14. The Schwarz lemma and Aut(D), Aut(H).

Proposition 4.15 (Schwarz Lemma). Let $f : \mathbb { D } \to \mathbb { D }$ be holomorphic with $f ( 0 ) = 0$ . Then $| f ( z ) | \leq$ |z| for all $z \in \mathbb { D }$ , and if equality occurs at $z _ { 0 } \in \mathbb { D }$ , then f is a rotation. Moreover, $| f ^ { \prime } ( 0 ) | \le 1$ 1, and if equal then f is a rotation.

Proof. Consider the holomorphic function $\textstyle { \frac { f ( z ) } { z } }$ and use the maximum principle.

Definition 4.16. For a open set $\Omega \subset \mathbb { C }$ , an automorphism of Ω is a biholomorphic map $f : \Omega $ Ω. Automorphisms of Ω forms a group $\operatorname { A u t } ( \Omega )$

Example 4.17. In [SSh03, Exercise 3.14], we proved that ${ \mathrm { A u t } } ( \mathbb { C } ) = \{ z \mapsto a z + b : a , b \in \mathbb { C } , \ a \neq 0 \}$

Theorem 4.18. Automorphisms of D are exactly the maps

$$
f ( z ) = e ^ { i \theta } { \frac { \alpha - z } { 1 - { \overline { { \alpha } } } z } }
$$

where $\theta \in \mathbb { R }$ and $\alpha \in \mathbb { D }$

Proof. Note that the map $\begin{array} { r } { \varphi _ { \alpha } ( z ) : = \frac { \alpha - z } { 1 - \overline { { \alpha } } z } } \end{array}$ is a biholomorphism $\mathbb { D }  \mathbb { D }$ that exchanges 0 and $\alpha ,$ and $\varphi _ { \alpha }$ is its own inverse. Now, suppose $f \in \operatorname { A u t } ( \mathbb { D } )$ and $f ( 0 ) = \alpha$ Consider $g = f \circ \varphi _ { \alpha }$ , which biholomorphically maps $\mathbb { D }  \mathbb { D }$ and $g ( 0 ) = 0$ . By Schwarz lemma on both g and $g ^ { - 1 }$ , we get $| g ( z ) | = | z |$ for $z \in \mathbb { D }$ , and hence g is a rotation $g = e ^ { i \theta }$ . But then $f = g \circ \varphi _ { \alpha }$ . 

Corollary 4.19. Automorphisms of D that fix the origin are the rotations.

Theorem 4.20. Automorphisms of H are exactly of the form

$$
z \mapsto { \frac { a z + b } { c z + d } }
$$

where $a , b , c , d \in \mathbb { R }$ such that ad $- b c = 1$ . In other words, we have an isomorphism

$$
\mathrm { A u t } ( \mathbb { H } ) \simeq P S L _ { 2 } ( \mathbb { R } )
$$

Proof. Let $F : \mathbb { H }  \mathbb { D }$ be a biholomorphism. Note the isomorphism $\operatorname { A u t } ( \mathbb { D } ) \ { \stackrel { \sim } { \to } } \ \operatorname { A u t } ( \mathbb { H } )$ via $f \mapsto$ $F ^ { - 1 } \circ f \circ F$ . Then, the previous theorem and computation yields the desired result. 

Remark 4.21. Note that $\operatorname { A u t } ( \mathbb { D } ) , \operatorname { A u t } ( \mathbb { H } )$ act transitively on D, H (respectively), but not faithfully.

## 4.22. The Riemann mapping theorem.

Before stating and proving the Riemann mapping theorem and its proof, we consider some metric topological matters.

Given a metric space $( X , d )$ , X is totally bounded if X can be covered by finitely many -balls for any given $\epsilon > 0 .$ . It is well-known that

A metric space X is compact iff it is complete and totally bounded

Given a metric space $( Y , d )$ and X a set, we can define a metric on $Y ^ { X }$ by

$$
\rho ( f , g ) : = { \left\{ \begin{array} { l l } { \operatorname* { s u p } _ { x \in X } d ( f ( x ) , g ( x ) ) } \\ { 1 { \mathrm { ~ i f ~ } } \operatorname* { s u p } > 1 } \end{array} \right. }
$$

This is the uniform topology on $Y ^ { X }$ ; convergence in this metric is exactly uniform convergence of functions. Hence, we know that $C ( X , Y ) \subset Y ^ { X }$ is closed. Moreover, note the fact that $\bar { Y } ^ { X }$ is complete if Y is complete. Note that unit-ball in $C ( X , Y )$ is not compact; e.g. $\{ x ^ { n } \} _ { n } \subset C ( [ 0 , 1 ] )$ is not sequentially compact. For K a compact metric space, a family of functions ${ \mathcal { F } } \in C ( K )$ is uniformly bounded if there exists M such that $| f | \leq M \forall f \in { \mathcal { F } }$ , and $\mathcal { F }$ is equicontinuous if for any $\epsilon > 0$ there exists $\delta > 0$ such that $| f ( x ) - f ( y ) | < \epsilon$ whenever $x , y \in K , \ d ( x , y ) < \delta$ and $f \in \mathcal F$

Theorem 4.23 (Arzela-Ascoli). Let K is a compact metric space. If a family of functions $\mathcal F \subset$ $C ( K )$ is equicontinuous and uniformly bounded, then $\overline { \mathcal { F } }$ is compact.

In complex analysis, a related notion to a family of functions being compact is the following:

Definition 4.24. Let $\Omega \subset \mathbb { C }$ be open, and $\mathcal { F }$ be a family of holomorphic functions on Ω. $\mathcal { F }$ is normal if every sequence in $\mathcal { F }$ has a subsequence that converges uniformly on every compact subset of Ω (limit need not be in $\mathcal { F } )$

Theorem 4.25 (Montel’s theorem). Let $\mathcal { F }$ be a family of holomorphic functions on Ω. $I f \mathcal { F }$ is uniformly bounded on every compact subset of Ω, then $\mathcal { F }$ is equicontinuous on every compact subset of Ω, and hence $\mathcal { F }$ is a normal family.

Proof. Note that if $| f ^ { \prime } |$ is bounded, then f is Lipschitz cotninuous, so use Cauchy integral formula and that $\mathcal { F }$ is uniformly bounded to show that $| f ^ { \prime } ( z ) | \leq M$ for all $f \in \mathcal F$ and $z \in \Omega$ . This show $\mathcal { F }$ equicontinuous. Then use Arzela-Ascoli theorem with exhaustion of Ω by compact sets to show normal. 

Proposition 4.26. If Ω is a region and $\left\{ f _ { n } \right\}$ a sequence of injective holomorphic functions on Ω that converges uniformly to a holomorphic function f on every compact subset of Ω, then f is either injective or constant.

Proof. If $f ( z _ { 1 } ) = f ( z _ { 2 } )$ , then consider the sequence $g _ { n } ( z ) : = f _ { n } ( z ) - f ( z _ { 1 } )$ Note that $g _ { n }  g : =$ $f ( z ) - f ( z _ { 1 } )$ uniformly on all compact subsets and so does $g _ { n } ^ { \prime }  g ^ { \prime }$ . Thus, for a small circle around $z _ { 2 }$ , we must have $\begin{array} { r } { 0 = { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { g _ { n } ^ { \prime } ( z ) } { g _ { n } ( z ) } } d z = { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { g ^ { \prime } ( z ) } { g ( z ) } } d z = 1 } \end{array}$ , which is a contradiction. 

Theorem 4.27 (Riemann mapping theorem). $I f \Omega \subset \mathbb { C }$ is proper and simply-connected region, then $f o r \ z _ { 0 } \in \Omega$ , there exists a unique biholomorphism $F : \Omega  \mathbb { D }$ such that $F ( z _ { 0 } ) = 0$ and $F ^ { \prime } ( z _ { 0 } ) > 0$

Proof. TODO

## 4.28. Exercises.

Exercise 4.A. [SSh03, 8.10] Let $F : \mathbb { H }  \mathbb { C }$ be a holomorphic function satisfying $| F ( z ) | \le 1$ and $F ( i ) = 0$ . Then show that $\begin{array} { r } { | F ( z ) | \le | \frac { i - z } { i + z } | } \end{array}$

Proof. Note that $G : \mathbb { H }  \cdot$ D defined by $\begin{array} { r } { G ( z ) : = \frac { i - z } { i + z } } \end{array}$ and $\begin{array} { r } { G ^ { - 1 } ( w ) = i \frac { 1 - w } { 1 + w } } \end{array}$ is a conformal equivalence. Define $H : \mathbb { D }  \mathbb { D }$ by $H : = F \circ G ^ { - 1 } : \mathbb { D } \to \mathbb { C }$ . Since H maps $\mathbb { D }  \mathbb { D }$ and $H ( 0 ) = 0$ , by the Schwarz lemma we have $| H ( w ) | \leq | w |$ for all $w \in \mathbb { D }$ . In other words, $| F ( G ^ { - 1 } ( w ) ) | \leq | G ( G ^ { - 1 } ( w ) |$ , and thus $| F ( z ) | \le | z |$ for $z \in \mathbb { H }$ 

Exercise 4.B. [SSh03, 8.12] $I f f : \mathbb { D } \to \mathbb { D }$ is analytic and has two distinct fixed points, then $f$ is the identity $( i . e . \ f ( z ) = z )$

Proof. Suppose $\alpha , \beta \in \mathbb { D }$ are two distinct fixed points. Consider the biholomorphism $\begin{array} { r } { \phi _ { \alpha } ( z ) : = \frac { \alpha - z } { 1 - \overline { { \alpha } } z } . } \end{array}$ which satisfies $\phi _ { \alpha } ( 0 ) = \alpha$ and $\phi _ { \alpha } ( \beta ) = \beta ^ { \prime }$ (note $\phi _ { \alpha } ( \beta ^ { \prime } ) = \beta )$ . Now, consider the map $g : = \phi _ { \alpha } \circ f \circ \phi _ { \alpha }$ : $\mathbb { D }  \mathbb { D } .$ , which has fixed points 0 and $\beta ^ { \prime }$ . By the Schwarz lemma, $g$ is a rotation that fixes a nonzero point, and hence identity, and thus $f$ is also identity. 

Exercise 4.C. [SSh03, 8.14] Show that all biholomorphic maps $\mathbb { H } \to \mathbb { D }$ take the form

$$
z \mapsto e ^ { i \theta } { \frac { z - \beta } { z - { \overline { { \beta } } } } } , \quad \theta \in \mathbb { R } , \ \beta \in \mathbb { H }
$$

Proof. Any biholomorphism $f : \mathbb { H } \to \mathbb { D }$ factors through as $f = ( f \circ F ^ { - 1 } ) \circ F$ where $F : \mathbb { H }  \mathbb { D }$ is a biholomorphism $z \mapsto { \textstyle { \frac { i - z } { i + z } } }$ and $f \circ F ^ { - 1 } \in \operatorname { A u t } ( { \mathbb { D } } )$ is of the form $z \mapsto e ^ { i \theta } { \frac { \alpha - z } { 1 - { \overline { { \alpha } } } z } }$ for $\theta \in \mathbb { R } , \ \alpha \in \mathbb { D }$ . Now, computing the composition of the Mobius transformation

$$
e ^ { i \theta } \left[ { \frac { - 1 \quad \alpha } { - \alpha } } \right] \left[ { \frac { - 1 \quad i } { 1 } } \right] = e ^ { i \theta } \left[ { \frac { \alpha + 1 \quad i ( \alpha - 1 ) } { \alpha + 1 } } \right]
$$

which factors as

$$
e ^ { i \theta } \left[ { \begin{array} { c c } { \alpha + 1 } & { 0 } \\ { 0 } & { { \overline { { { \alpha } } } } + 1 } \end{array} } \right] \left[ { \begin{array} { c c } { 1 } & { - \beta } \\ { 1 } & { - { \overline { { \beta } } } } \end{array} } \right]
$$

where $\begin{array} { r } { \beta = i \frac { 1 - \alpha } { 1 + \alpha } = F ^ { - 1 } ( \alpha ) } \end{array}$ . Since $| \alpha + 1 | = | \overline { { \alpha } } + 1 |$ , the left matrix also rotation Mobius map. Hence, for some $\theta ^ { \prime }$ and $\beta \in \mathbb { H }$ as defined, $\begin{array} { r } { f ( z ) = e ^ { i \theta ^ { \prime } } \frac { z - \beta } { z - \overline { { \beta } } } . } \end{array}$ , as desired. 

Exercise 4.D. [SSh03, 8.15] Suppose $\Phi \in \operatorname { A u t } ( \mathbb { H } )$ that fixes three distinct points on the real axis, then Φ is identity. $I f \left( x , y , z \right)$ and $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ are two pairs of three distinct points on the real axis with $z _ { 1 } < z _ { 2 } < z _ { 3 } , \ w _ { 1 } < w _ { 2 } < w _ { 3 }$ , then there exists a unique automorphism $\Phi \in \operatorname { A u t } ( \mathbb { H } )$ such that $\Phi ( x _ { i } ) = w _ { i }$ . Same holds if $w _ { 2 } < w _ { 3 } < w _ { 1 }$ or $w _ { 3 } < w _ { 1 } < w _ { 2 }$

Proof. $\operatorname { A u t } ( \mathbb { H } ) \subset \operatorname { A u t } ( { \widehat { \mathbb { C } } } )$ as $P S L _ { 2 } ( \mathbb { R } ) \subset P S L _ { 2 } ( \mathbb { C } )$ . Thus, since a Mobius transformation is determined by images of three distinct points, the first statement follows. Now, for the second statement, writing $( z , z _ { 1 } , z _ { 2 } , z _ { 3 } ) = ( w , w _ { 1 } , w _ { 2 } , w _ { 3 } )$ and solving for w gives a Mobius transformation $\frac { a z + b } { c z + d }$ for some $a , b , c , d \in \mathbb { R }$ mapping $z _ { 1 } , z _ { 2 } , z _ { 3 }$ to $w _ { 1 } , w _ { 2 } , w _ { 3 }$ , and with (a lot of) computation, one checks that ad − bc > 0 (so that $\left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] \in P S L _ { 2 } ( \mathbb { R } ) )$ exactly when $w _ { i } \mathrm { ^ s }$ are ordered as given. 

Exercise 4.E. [SSh03, Problem 8.2] The oriented angle $o f z , w \in \mathbb { C }$ is determined by two quantities

$$
{ \frac { \langle z , w \rangle } { | z | | w | } } { \mathrm { ~ a n d ~ } } { \frac { \langle z , - i w \rangle } { | z | | w | } } , { \mathrm { ~ w h e r e ~ } } \langle z , w \rangle = \operatorname { R e } ( w { \overline { { z } } } )
$$

An oriented angle of two intersecting curves at the intersection is defined as the angle of two tangent vectors at the intersection. A map $f : \Omega \to \mathbb { C }$ is angle-preserving at $z _ { 0 } \in \Omega$ if for any two curves $\gamma , \eta \subset \Omega$ intersecting at $z _ { 0 } ,$ the (oriented) angle $o f \gamma , \eta$ at z0 and the angle of $f \circ \gamma , f \circ \eta$ at $f ( z _ { 0 } )$ are the same. Show that:

(1) $\begin{array} { r } { I f f : \Omega \to \mathbb { C } } \end{array}$ is holomorphic with $f ( z _ { 0 } ) \neq 0$ , then f is angle-preserving at $z _ { \mathrm { 0 } }$ .

(2) Conversely, if $f : \Omega \to \mathbb { C }$ is real-differentiable at $z _ { \mathrm { 0 } }$ with $J _ { f } ( z _ { 0 } ) \ne 0$ and is angle-preserving, then f is holomorphic at $z _ { \mathrm { 0 } }$ .

Proof. (1) is easy, for if $\gamma ( t _ { 0 } ) = z _ { 0 }$ and $\eta ( s _ { 0 } ) = z _ { 0 }$ , then $( f \circ \gamma ) ^ { \prime } ( t _ { 0 } ) = f ^ { \prime } ( z _ { 0 } ) \gamma ^ { \prime } ( t _ { 0 } ) , ( f \circ \eta ) ^ { \prime } ( t _ { 0 } ) =$ $f ^ { \prime } ( z _ { 0 } ) \eta ^ { \prime } ( t _ { 0 } )$ . For the converse, by chain rule, if γ is a curve through z0 at $t _ { 0 }$ , then $[ D f ] _ { z _ { 0 } } \gamma ^ { \prime } ( t _ { 0 } ) = ( f \circ$ $\gamma ) ^ { \prime } ( t _ { 0 } )$ . Since the matrix $M : = [ D f ] _ { z _ { 0 } }$ is such that $\langle u , v \rangle = \langle M u , M v \rangle$ and $\langle u , - i v \rangle = \langle M u , M ( - i v ) \rangle$ for any $| u | = | v | = 1$ , it is of the form $\left[ { \begin{array} { l l } { a } & { - b } \\ { b } & { a } \end{array} } \right]$ , which means that f satisfies the Cauchy-Riemann equation at $z _ { \mathrm { 0 } }$ 

## References

[Ahl79] Ahlfors. Complex Analysis. 3rd ed. Mc-Graw Hill. 1979.

[SSh03] Stein & Shakarchi. Complex Analysis. Princeton Lectures in Analysis II. 2003.

[Lee13] Lee. Introduction to Smooth Manifolds. Springer. 2013.