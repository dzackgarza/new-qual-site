## Arranged by Topic

See http://www.math.uga.edu/qualifying-exams/Complex-Analysis for exams from previous years.

8155a - Compactness, connectedness & functions of one real variable

1. Take $x _ { 0 } = a , x _ { 1 } = b$ , and set $x _ { n } : = { \frac { x _ { n - 1 } + x _ { n - 2 } } { 2 } }$ for $n \geq 2$ . Prove that $( x _ { n } )$ i s a Cauchy sequence and find its limit in terms of a and b.

2. Suppose $f : \mathbb { R }  \mathbb { R }$ is continuous and $\begin{array} { r } { \operatorname* { l i m } _ { x \to \pm \infty } f ( x ) = 0 } \end{array}$ . Prove that f is uniformly continuous.

3. Give an example of a function $f : \mathbb { R } $ R such that f is everywhere differentiable, but $f ^ { \prime }$ is not continuous at 0.

4. Suppose $\left( g _ { n } \right)$ is a uniformly convergent sequence of functions from R to R, while $f : \mathbb { R } \to \mathbb { R }$ is uniformly continuous. Prove that the sequence $\left( f \circ g _ { n } \right)$ of composite functions is also uniformly convergent on R.

5. Let f be a differentiable function on $[ a , b ]$ . We say f is uniformly differentiable if for each $\epsilon > 0$ there exists a $\delta > 0$ such that

$$
\left| { \frac { f ( x ) - f ( y ) } { x - y } } - f ^ { \prime } ( y ) \right| < \epsilon
$$

whenever $| x - y | < \delta$ with $x , y \in [ a , b ]$ . Prove that f is uniformly differentiable on $[ a , b ]$ if and only if f  is continuous on [a, b].

6. Suppose A, B are disjoint non-empty compact subsets of $\mathbb { R } ^ { n }$ . Prove that there exist $a \in A$ and $b \in B$ satisfying $| | a - b | | = \operatorname* { i n f } \{ | | x - y | | : x \in A , y \in B \}$ •

7. Suppose A, B are connected subsets of $\mathbb { R } ^ { n }$ which are not disjoint. Prove that their union $A \cup B$ is also connected.

8. Suppose $( f _ { n } ) _ { n \in \mathbb { N } }$ is a sequence of continuous functions : $[ 0 , 1 ]  \mathbb { R }$ satisfying $f _ { n } ( x ) \geq f _ { n + 1 } ( x ) \geq 0$ for each $n \in \mathbb { N }$ and $x \in [ 0 , 1 ]$ . Prove that if the sequence $\left( f _ { n } \right)$ converges pointwise to 0 on [0, 1], then $\left( f _ { n } \right)$ converges uniformly to 0 on [0, 1].

9. Show that if $E \subset [ 0 , 1 ]$ is uncountable, then there is some $t \in \mathbb { R }$ such that both $E \cap ( - \infty , t )$ and $E \cap ( t , \infty )$ are uncountable.

1. Discuss continuity and differentiability of the function $f : \mathbb { R } ^ { 2 } \to \mathbb { R }$ defined by

$$
f ( x , y ) = \left\{ \begin{array} { l l } { \frac { x y } { \sqrt { x ^ { 2 } + y ^ { 2 } } } , \qquad } & { ( x , y ) \neq ( 0 , 0 ) } \\ { 0 , } & { ( x , y ) = ( 0 , 0 ) } \end{array} . \right.
$$

2. Include brief justification for your answers to Parts b) and c) of this problem. a) Complete the definition: $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is (real) differentiable at a point $a \in \mathbb { R } ^ { n }$ if there is a linear transformation . . .

b) Give an example of a function $g : \mathbb { R } ^ { 2 } $ R whose first order partial derivatives exist everywhere, such that $g$ is not differentiable at $( 0 , 0 )$

c) Give an example of a function $h : \mathbb { R } ^ { 2 }  \mathbb { R } ^ { 2 }$ which is (real) differentiable everywhere, but not complex differentiable anywhere.

3. Let $f : \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$

a) Define in terms of linear transformations, what it means for f to be differentiable at a point $( a , b ) \in \mathbb { R } ^ { 2 }$

b) State a version of the inverse function theorem in this setting.

c) Identifying C with $\mathbb { R } ^ { 2 }$ in the usual way, give, with proof, a necessary and sufficient condition for a function satisfying the definition of real differentiability in Part a) to be complex differentiable at the point $a + i b$

4. Let $f = u + i v$ be differentiable (i.e. $f ^ { \prime } ( z )$ exists) with continuous partial derivatives at a point $z = r \mathrm { e } ^ { i \theta } , \ r \neq 0$ . Show that

$$
\frac { \partial u } { \partial r } = \frac { 1 } { r } \frac { \partial v } { \partial \theta } , \quad \frac { \partial v } { \partial r } = - \frac { 1 } { r } \frac { \partial u } { \partial \theta } .
$$

5. Consider the polynomial function $f ( s , t ) = 9 s ^ { 3 } - 6 s t + t ^ { 2 }$ . Let $P = ( 1 , 3 )$

a) Carefully state the conclusion of the implicit function theorem concerning the equation $f ( s , t ) = 0$ when $f$ is considered as a function from $\mathbb { R } ^ { 2 }$ to R.

b) Carefully state the conclusion of the implicit function theorem concerning the equation $f ( s , t ) = 0$ when f is considered as a function from $\mathbb { C } ^ { 2 }$ to C.

c) Use the implicit function theorem for functions from $\mathbb { R } ^ { \times } \mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ to prove b). (There are various approaches to this, including the definition of complex derivative, the Cauchy-Riemann equations, and consideration of total derivatives.)

6. Let $F : \mathbb { R } ^ { 2 }  \mathbb { R }$ be a continuously differentiable map satisfying $F ( 0 , 0 ) = 0$ and $| | \bigtriangledown F \big | _ { ( 0 , 0 ) } | | < 1$ . Prove that there is some real number $r > 0$ such that $| F ( x , y ) | < r$ whenever $| | ( x , y ) | | < r$ $( \# 2$ on the January 2003 Analysis Qual is a more general version of this problem.)

7. State the most general (real) version of the implicit theorem you know and outline how it can be proved from the corresponding version of the (real) inverse function theorem.

## 8155c - Conformal Mapping

1. Find a conformal map of the unit disk onto the upper half plane.

2. Exhibit a conformal map from the strip $\{ z \in \mathbb { C } : 0 < \operatorname { I m } ( z ) < 1 \}$ onto the open unit disk.

3. Find a linear fractional transformation T which maps the open upper half plane onto the open unit disk. Then explicitly describe the image of the first quadrant of the unit disk under T .

4. Find a conformal map from $D : = \left\{ z \in \mathbb { C } : | z - i | > 1 , \mathrm { R e } ( z ) > 0 \right\}$ onto the open upper half plane.

5. Find a conformal map from $D : = \{ z \in \mathbb { C } : | z | < 1 , | z - { \frac { 1 } { 2 } } | > { \frac { 1 } { 2 } } \}$ onto the open unit disk.

6. Find a conformal map from the intersection of $| z - 1 | < 2$ and $| z + 1 | < 2$ t o the open upper half plane.

7. Let $\Omega \subset \mathbb { C }$ be the region inside the unit circle $| z | = 1$ and outside the circle $\begin{array} { r } { | z - \frac { 1 } { 4 } | = \frac { 1 } { 4 } } \end{array}$ . Find a cone-to-one conformal map of Ω onto an annulus $r < | \boldsymbol { z } | < 1$ for an appropriate value of r.

8. Let D be the region obtained by removing the interval [0, 1) from the unit disk $| z | < 1$ . Find a conformal map from D onto the open unit disk.

9. Find a conformal map from $\mathbb { C } \backslash \{ x \in \mathbb { R } : x \leq 0 \}$ onto the open unit disk.

10. Find a conformal map from $\mathbb { C } \backslash \{ x \in \mathbb { R } : | x | \geq 1 \}$ onto the open unit disk.

11. Find a bijective conformal map from

$$
G : = \{ z \in \mathbb { C } : | z - 1 | < { \sqrt { 2 } } , ~ | z + 1 | < { \sqrt { 2 } } \} ~ \backslash ~ [ 0 , i )
$$

onto the open upper half plane.

12. (Can omit; related to the discussion of symmetry) Prove that the following are equivalent for a Mobius transformation T given by $\begin{array} { r } { T z = \frac { a z + b } { c z + d } } \end{array}$

a) T maps $\mathbb { R } \cup \{ \infty \}$ onto itself.

b) It is possible to choose $a , b , c , d \in \mathbb { R }$

c) ${ \overline { { T z } } } = T ( { \overline { { z } } } )$ for every $z \in \mathbb { C } \cup \infty$

d) There exist $\alpha \in \mathbb { R }$ and $\beta \in \mathbb { C } \backslash \mathbb { R }$ satisfying T (α) = α and $T ( \overline { { \beta } } ) = \overline { { T \beta } }$

1. Suppose $f , g : [ 0 , 1 ] \to \mathbb { R }$ with f Riemann integrable and

$$
| g ( x ) - g ( y ) | \leq | f ( x ) - f ( y ) | , \qquad x , y \in [ 0 , 1 ] .
$$

Prove that g is also Riemann integrable.

2. State and prove Green’s Theorem for rectangles. Then use it to prove Cauchy’s Theorem for functions analytic in a rectangle.

3. Suppose $( f _ { n } ) _ { n \in \mathbb { N } }$ is a sequence of analytic functions on $\mathbb { D } : = \{ z \in \mathbb { C } : | z | < 1 \}$ Show that if $\left( f _ { n } \right)$ converges to a function $g : \mathbb { D }  \mathbb { C }$ uniformly on each compact subset of D, then g is analytic on D

4. Suppose $\left( f _ { n } \right)$ is a sequence of functions which are entire (=analytic throughout the complex plane). Suppose $\left( f _ { n } \right)$ converges pointwise to a function $g : \mathbb { C } \to \mathbb { C }$ and the convergence is uniform on each line segment in C. Show that $g$ is entire and that $f _ { n }  g$ uniformly on each compact subset of $\mathbb { C }$

5. Prove that there is no sequence of polynomials that converge uniformly to the function $\textstyle f ( z ) = { \frac { 1 } { z } }$ on the unit circle.

6. Suppose that $f$ is a continuous function on R which vanishes outside some finite interval and for each $z \subset \mathbb { C }$ define

$$
g ( z ) = \int _ { - \infty } ^ { \infty } f ( t ) \exp ( - i z t ) d t .
$$

Show that $g$ is entire.

7. Suppose $f : \mathbb { C } \to \mathbb { C }$ is entire and $| f ( z ) | \leq | z | ^ { \frac { 1 } { 2 } }$ whenever $| z | > 1 0$ . Prove that $f$ is the zero function.

8. Let $\gamma$ be a smooth curve joining two distinct points $a , b \in \mathbb { C }$ . Prove that the function defined by the formula

$$
f ( z ) = \int _ { \gamma } \frac { g ( w ) d w } { w - z }
$$

is analytic off the range of $\gamma$ . Justify every step.

9. Suppose $f : \mathbb { C } \to \mathbb { C }$ is continuous everywhere and analytic off the real axis.   
Prove that f is entire.

10. Suppose $f : \mathbb { C } \to \mathbb { C }$ is entire and bounded. Use Cauchy’s formula to prove that $f ^ { \prime }$ is identically zero and hence that f is constant. This is Liouville’s Theorem.

# 8155e - Liouville, FTA, and Power Series

1. Suppose f is analytic on a region Ω in C containing the open unit disk D and we have $f ( z ) = \sum a _ { n } z ^ { n }$ with this power series having radius of convergence 1.

a) Give an example of such an f so that the series converges at every point on the unit circle T.

b) Give an example of such an f which is analytic at 1, but $\sum a _ { n }$ diverges.

c) Prove that f cannot be analytic at each point of T.

2. Suppose f is entire and has Taylor series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ about 0.

a) (No proof required) Express $a _ { n }$ as a contour integral along the circle $| z | = R$ b) Apply Part a) to verify that the power series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ converges uniformly on each bounded subset of C.

c) Determine, with proof, those functions f for which the power series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ converges uniformly on all of C.

3. Suppose D is a domain and f and g are analytic functions on D. Prove that if the product $f g = 0$ throughout D, then either f or g must vanish identically on D.

4. Suppose f is analytic on the open unit disk. Determine, with proof, which of the following are possible.

a) $\textstyle f ( { \frac { 1 } { n } } ) = ( - 1 ) ^ { n }$ for each integer $n > 1$

b) $\begin{array} { r } { f ( \frac { 1 } { n } ) = \exp ( - n ) } \end{array}$ for each even integer $n > 1$ while $\begin{array} { r } { f ( \frac { 1 } { n } ) = 0 } \end{array}$ for each odd integer $n > 1$

c) $\begin{array} { r } { f ( \frac { 1 } { n ^ { 2 } } ) = \frac { 1 } { n } } \end{array}$ for each integer $n > 1$

d) $\begin{array} { r } { f ( \frac { 1 } { n } ) = \frac { n - 2 } { n - 1 } } \end{array}$ for each integer $n > 1$

5. Use complex analysis to prove the Fundamental Theorem of Algebra.

6. Find all entire functions f which satisfy $| f ( z ) | \geq | z |$ for all $z \in \mathbb { C }$ . Be sure to prove your list is complete.

7. Suppose the complex power series $\textstyle \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ converges for some $z _ { 0 } \neq 0$

a) Prove that the series converges absolutely for each z with $| z | < | z _ { 0 } |$

b) Suppose $0 < r < | z _ { 0 } |$ . Show that the series converges uniformly on $| z | \leq r$

8. Suppose f is entire and assume that lim ${ \frac { f ( z ) } { z ^ { n } } } = 0$ for some integer $n \geq 1$ z→∞   
Prove that f is a polynomial of degree at most $n - 1$

9. Find, with proof, all entire functions satisfying $| f ( z ) | \leq \sqrt { | z | } \mathrm { ~ f o r ~ } | z | > 1 0$

10. Prove that the series $\scriptstyle \sum _ { n = 1 } ^ { \infty } { \frac { \sin ( n z ) } { 2 ^ { n } } }$ converges uniformly on $\{ z : \operatorname { I m } z < \ln 2 \}$

## 8155f - Laurent Expansions, Singularities

1. Find the Laurent expansions of $\textstyle { \frac { z + 1 } { z ( z - 1 ) } }$ about

a) $z = 0$

b) $\mathbf { Z } { = } 1$

2. Find the Laurent expansions of $\exp ( \textstyle { \frac { 1 } { z } } )$ and $\cos { \left( { \frac { 1 } { z } } \right) }$ about the origin.

3. Find the Laurent expansions of $\frac { z + 1 } { z ( z - 1 ) ^ { 2 } }$ about

a) $z = 0$

b) $\mathbf { Z } { = } 1$

Hint: Recall that power series can be differentiated.

4. Find the Laurent series for the following functions about 0 and classify their singularities there.

a) $\frac { \sin ^ { 2 } z } { z }$

b) $\scriptstyle z \exp ( { \frac { 1 } { z ^ { 2 } } } )$

c) $\frac { 1 } { z ( 4 - z ) }$

5. Find all entire functions which have poles at $\infty$

6. Find all functions on the Riemann sphere $\mathbb { C } \cup \{ \infty \}$ that have a simple pole at the point 2 and a double pole at ∞, but are analytic elsewhere.

7. Let f be entire. Discuss, with proofs and examples, the types of singularities f might have (removable, pole, or essential) at ∞ in each of the following cases.

a) f has at most finitely zeros in C.

b) f has infinitely many zeros in C.

8. Take $\begin{array} { r } { f ( z ) = \frac { \pi ^ { 2 } } { \sin ^ { 2 } \pi z } } \end{array}$ and $\begin{array} { r } { g ( z ) = \sum _ { n = - \infty } ^ { \infty } \frac { 1 } { ( z - n ) ^ { 2 } } } \end{array}$

a) Show these functions have the same singularities in $\mathbb { C }$

b) Show that f and g have the same singular parts at each of their singularities.

c) Note that f and g each have period one and that both approach zero uniformly on $0 \leq x \leq 1$ as $| y | \to \infty$ .

d) Conclude that $f = g$

## 8155g - Residues

Use complex variable methods and justify your work.

1. Calculate $\textstyle \int _ { 0 } ^ { \infty } { \frac { d x } { ( 1 + x ^ { 2 } ) ( 1 + 9 x ^ { 2 } ) } }$

2. Let $a > 0$ . Evaluate $\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x$

3. Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sqrt { x } } { ( x + 1 ) ^ { 2 } } } d x$

4. Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \cos x - \cos 4 x } { x ^ { 2 } } } d x$

5. Let $a > 0$ . Evaluate $\begin{array} { r } { \int _ { 0 } ^ { \infty } \frac { x ^ { 2 } } { ( x ^ { 2 } + a ^ { 2 } ) ^ { 2 } } d x } \end{array}$

6. Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sin { x } } { x } } d x$

7. Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sin x } { x ( x ^ { 2 } + 1 ) } } d x$

8. Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sqrt { x } } { 1 + x ^ { 2 } } } d x$

9. Evaluate $\textstyle \int _ { - \infty } ^ { \infty } { \frac { 1 + x ^ { 2 } } { 1 + x ^ { 4 } } } d x$

10. Let $a > 0$ . Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \cos x } { ( x ^ { 2 } + a ^ { 2 } ) ^ { 2 } } } d x$

11. Evaluate $\int _ { 0 } ^ { \infty } { \frac { \sin ^ { 3 } x } { x ^ { 3 } } } d x$

12. Let n be a positive integer and $0 < \theta < \pi$ . Prove that

$$
{ \frac { 1 } { 2 \pi i } } \int _ { | z | = 2 } { \frac { z ^ { n } } { 1 - 2 z \cos \theta + z ^ { 2 } } } d z = { \frac { \sin n \theta } { \sin \theta } } .
$$

13. Suppose $a > b > 0$ . Evaluate $\begin{array} { r } { \int _ { 0 } ^ { 2 \pi } \frac { d \theta } { ( a + b \cos \theta ) ^ { 2 } } } \end{array}$

## 8155h - Rouch´e’s Theorem

1. Prove that for every nonnegative integer n, the polynomial $\textstyle f _ { n } ( x ) = \sum _ { k = 0 } ^ { n }$ zkk! has no roots in the open unit disk. (Hint: Check $n = 1$ and $n = 2$ directly.)

2. Assuming that $| b | < 1$ , show that $f ( z ) = z ^ { 3 } + 3 z ^ { 2 } + b z + b ^ { 2 }$ has exactly two roots (counting multiplicity) in $| z | < 1$

3. Let c be a complex number such that $| c | < { \frac { 1 } { 3 } }$ . Show that on the open set $\mathrm { R e } ( z ) < 1$ , the function $f ( z ) = c \exp ( z )$ has exactly one fixed point, i.e., a point z0 such that $f ( z _ { 0 } ) = z _ { 0 }$

4. How many roots does the equation $z ^ { 7 } - 4 z ^ { 3 } - 1 = 0$ have in the open disk $| z | < 1 \ \mathrm { ? }$

5. Let $n \in \mathbb { N }$ . Prove that the equation $\exp ( z ) = a z ^ { n }$ has n solutions in the open unit disk D $\mathrm { i f } \ | a | > \mathrm { e }$ and none $\begin{array} { r } { \mathrm { i f ~ } | a | < \frac { 1 } { \mathrm { e } } } \end{array}$

6. Let f be analytic in a domain D. Fix $z _ { 0 } \in D$ and let $w _ { 0 } = f ( z _ { 0 } )$ . Suppose $z _ { 0 }$ is a zero of finite multiplicity m for $\begin{array} { r } { f ( z ) - w _ { 0 } = 0 } \end{array}$ . Show that there exist $\delta > 0$ and $\epsilon > 0$ such that for each w with $0 < | w - w _ { 0 } | < \epsilon .$ , the equation $f ( z ) - w = 0$ has exactly m distinct solutions inside the disk $| z - z _ { 0 } | < \delta$

7. Let $| a _ { k } | < 1 ( k = 1 , 2 , \ldots , n ) , | b | < 1$ and

$$
f ( z ) = { \frac { z - a _ { 1 } } { 1 - { \overline { { a } } } _ { 1 } z } } { \frac { z - a _ { 2 } } { 1 - { \overline { { a } } } _ { 2 } z } } \cdots { \frac { z - a _ { n } } { 1 - { \overline { { a } } } _ { n } z } } .
$$

Show that $f ( z ) = b$ has n solutions in $| z | < 1$

8. For each integer $n \geq 1$ , let $\begin{array} { r } { P _ { n } ( z ) = 1 + z + \frac { 1 } { 2 ! } z ^ { 2 } + \frac { 1 } { 3 ! } z ^ { 3 } + \cdot \cdot \cdot + \frac { 1 } { n ! } z ^ { n } } \end{array}$ . Show that all sufficiently large n, the polynomial $P _ { n }$ has no zeros in $| z | < 1 \ddot { 0 }$ , while the polynomial $P _ { n } ( z ) - 1$ has exactly 3 zeros there.

## 9. Prove that

$$
\operatorname* { m a x } _ { | z | = 1 } | a _ { 0 } + a _ { 1 } z + \cdot \cdot \cdot + a _ { n - 1 } z ^ { n - 1 } + z ^ { n } | \geq 1 .
$$

Hint: The first part of the problem asks for a statement of Rouch´e’s Theorem.

10. Use Rouch´e’s Theorem to prove the Fundamental Theorem of Algebra.

# 8155i - Schwarz Lemma and Reflection Principle

Problem 2 is best approached with Cauchy’s formula.

1. [Fall 2012, Problem $\# 7 ]$ Write $\mathbb { D } : = \{ z \in \mathbb { C } : | z | < 1 \}$ for the open unit disk. Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic, and admits a continuous extension $\widetilde { f } : \overline { { \mathbb { D } } } \to \overline { { \mathbb { D } } }$ such that $| f ( z ) | = 1$ whenever $| z | = 1$ .

a) Prove that $f$ is a rational function.

b) Suppose that $z = 0$ is the unique zero of $f .$ . Prove that $f ( z ) = \lambda z ^ { n }$ . for some $\lambda \in \mathbb { C }$ of absolute value 1 and some natural number $n$ .

c) More generally, suppose that $a _ { 1 } , \dots , a _ { n } \in \mathbb { D }$ are the zeros of $f _ { ; }$ , listed with multiplicity. Prove that

$$
f ( z ) = \lambda \prod _ { j = 1 } ^ { n } { \frac { z - a _ { j } } { 1 - { \overline { { a } } } _ { j } z } } , \quad | \lambda | = 1 .
$$

2. [August 2011, Problem $\# 3 ]$ Let $\overline { { B } } ( a , r )$ denote the closed disk of radius $r > 0$ about a point $a \in \mathbb { C }$ . Let $f$ be a holomorphic function an an open set containing $\overline { { B } } ( a , r )$ and let $M : = \mathrm { s u p } _ { z \in \overline { { B } } ( a , r ) } | f ( z ) |$ . Prove that for $\textstyle z \in { \overline { { B } } } ( a , { \frac { r } { 2 } } ) , z \neq a$ , we have

$$
{ \frac { | f ( z ) - f ( a ) | } { | z - a | } } \leq { \frac { 2 M } { r } } .
$$

3. [January 2011, Problem $\# 3 ]$ Write D for the open unit disk and set $G : = \{ z \in \mathbb { C } : \operatorname { R e } ( z ) > 0$ and $| z - 1 | > 1 \}$ . Find all conformal one-to-one maps of G onto D. You may express the maps as compositions, but should explain why your list is complete.

4. [January 2011, Problem $\# 6 ]$ Set $H _ { + } : = \{ z \in \mathbb { C } : \operatorname { I m } ( z ) > 0 \}$ Suppose $f : H _ { + } \cup \mathbb { R } \to \mathbb { C }$ satisfies the following:

(i) $f ( i ) = i$

(ii) f is continuous

(iii) f is analytic on $H _ { + }$

(iv) $f ( z )$ is real if and only z is real.

Show that $f ( H _ { + } )$ is a dense subset of $H _ { + }$

5. [Fall 2010, Problem $\# 5 ]$ Let $H : = \{ z \in \mathbb { C } : \operatorname { R e } ( z ) > 0 \}$ . Suppose f is an analytic function which maps the open unit disk D into H and satisfies $f ( 0 ) = 2$ . Find a sharp upper bound for $\left| f ^ { \prime } ( 0 ) \right|$ |, justifying your bound by a proof and its sharpness by an example.

6. [January 2008, Problem $\# 5 \mathrm { b } ]$ Suppose $f : \mathbb { D }  \mathbb { D }$ is analytic, has a zero of order k at the origin, has no other zeros, and satisfies $\begin{array} { r } { \operatorname* { l i m } _ { | z | \to 1 } | f ( z ) | = 1 } \end{array}$ . Give, with proof, a formula for f (z).

7. [August 2007, Problem $\# 4]$

a) State the standard Schwarz reflection principle involving reflection across the real axis.

b) Give, with justification, a linear fractional transformation T mapping D to H. Let $g ( z ) = { \overline { { z } } } ;$ show that $\begin{array} { r } { T ^ { - 1 } \circ g \circ T ( z ) = \frac { 1 } { \overline { { z } } } } \end{array}$

c) Suppose f is holomorphic on D, continuous on ${ \overline { { \mathbb { D } } } } _ { : }$ , and real on the unit circle. Prove that f must be constant.

8. [Fall 2002 Problem #8] Suppose f and g are holomorphic mappings of the unit disc D into an open domain Ω, f is one-to-one, and $f ( 0 ) = g ( 0 )$ . Show that $g ( | z | < r ) \subset f ( | z | < r )$ for each $0 < r < 1$ . (The first part of the problem asks for a statement of the Schwarz Lemma.)

9. [April 1999 Problem $\# 7 ]$ Let $S : = \{ z \in \mathbb { D } : \operatorname { I m } ( z ) \geq 0 \}$ . Suppose $f : S  \mathbb { C }$ is continuous on S, real on $S \cap \mathbb { R }$ , and holomorphic on the interior of S. Prove that f is the restriction of a holomorphic function on the open unit disk.

10. [Fall 1998, Problem #5] Suppose $f : \mathbb { D }  \mathbb { D }$ is analytic. Prove that for any $a \in \mathbb { D }$

$$
{ \frac { | f ^ { \prime } ( a ) | } { 1 - | f ( a ) | ^ { 2 } } } \leq { \frac { 1 } { 1 - | a | ^ { 2 } } } .
$$