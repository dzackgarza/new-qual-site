$\mathbf { 3 . ^ { * } }$ The Schwarz-Pick lemma (see Exercise 13) is the infinitesimal version of an important observation in complex analysis and geometry.

For complex numbers $w \in \mathbb { C }$ and $z \in \mathbb { D }$ we define the hyperbolic length of $w$ at z by

$$
\| w \| _ { z } = \frac { | w | } { 1 - | z | ^ { 2 } } ,
$$

where $| w |$ and $| z |$ denote the usual absolute values. This length is sometimes referred to as the Poincar´e metric, and as a Riemann metric it is written as

$$
d s ^ { 2 } = \frac { | d z | ^ { 2 } } { ( 1 - | z | ^ { 2 } ) ^ { 2 } } .
$$

The idea is to think of $w$ as a vector lying in the tangent space at $z .$ Observe that for a fixed $w ,$ its hyperbolic length grows to infinity as z approaches the boundary of the disc. We pass from the infinitesimal hyperbolic length of tangent vectors to the global hyperbolic distance between two points by integration.

(a) Given two complex numbers $z _ { 1 }$ and $z _ { 2 }$ in the disc, we define the hyperbolic distance between them by

$$
d ( z _ { 1 } , z _ { 2 } ) = \operatorname* { i n f } _ { \gamma } \int _ { 0 } ^ { 1 } \| { \gamma } ^ { \prime } ( t ) \| _ { \gamma ( t ) } d t ,
$$

where the infimum is taken over all smooth curves $\gamma : [ 0 , 1 ]  \mathbb { D }$ joining $z _ { 1 }$ and $z _ { 2 }$ . Use the Schwarz-Pick lemma to prove that if $f : \mathbb { D } \to \mathbb { D }$ is holomorphic, then

$$
d ( f ( z _ { 1 } ) , f ( z _ { 2 } ) ) \leq d ( z _ { 1 } , z _ { 2 } ) \quad \quad { \mathrm { f o r ~ a n y ~ } } z _ { 1 } , z _ { 2 } \in \mathbb { D } .
$$

In other words, holomorphic functions are distance-decreasing in the hyperbolic metric.

(b) Prove that automorphisms of the unit disc preserve the hyperbolic distance, namely

$$
d ( \varphi ( z _ { 1 } ) , \varphi ( z _ { 2 } ) ) = d ( z _ { 1 } , z _ { 2 } ) , \quad \mathrm { ~ f o r ~ a n y ~ } z _ { 1 } , z _ { 2 } \in \mathbb { D }
$$

and any automorphism $\varphi .$ Conversely, if $\varphi : \mathbb { D }  \mathbb { D }$ preserves the hyperbolic distance, then either $\varphi$ or $\overline { { \varphi } }$ is an automorphism of D.

(c) Given two points $z _ { 1 } , z _ { 2 } \in \mathbb { D }$ , show that there exists an automorphism $\varphi$ such that $\varphi ( z _ { 1 } ) = 0$ and $\varphi ( z _ { 2 } ) = s$ for some s on the segment $[ 0 , 1 )$ on the real line.

(d) Prove that the hyperbolic distance between 0 and $s \in [ 0 , 1 )$ is

$$
d ( 0 , s ) = { \frac { 1 } { 2 } } \log { \frac { 1 + s } { 1 - s } } .
$$

(e) Find a formula for the hyperbolic distance between any two points in the unit disc.

4.∗ Consider the group of matrices of the form

$$
M = \left( \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right) ,
$$

that satisfy the following conditions:

(i) $a , b , c ,$ and $d \in \mathbb { C } ,$

(ii) the determinant of M is equal to 1,

(iii) the matrix M preserves the following hermitian form on $\mathbb { C } ^ { 2 } \times \mathbb { C } ^ { 2 }$

$$
\langle Z , W \rangle = z _ { 1 } \overline { { w } } _ { 1 } - z _ { 2 } \overline { { w } } _ { 2 } ,
$$

where $Z = \left( z _ { 1 } , z _ { 2 } \right)$ and $W = ( w _ { 1 } , w _ { 2 } )$ . In other words, for all $Z , W \in \mathbb { C } ^ { 2 }$

$$
\langle M Z , M W \rangle = \langle Z , W \rangle .
$$

This group of matrices is denoted by SU(1, 1).

(a) Prove that all matrices in $\mathrm { S U } ( 1 , 1 )$ are of the form

$$
\left( \begin{array} { c c } { { a } } & { { b } } \\ { { \overline { { { b } } } } } & { { \overline { { { a } } } } } \end{array} \right) ,
$$

where $| a | ^ { 2 } - | b | ^ { 2 } = 1$ . To do so, consider the matrix

$$
J = \left( \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } \end{array} \right) ,
$$

and observe that $\langle Z , W \rangle = { } ^ { t } W J Z$ , where tW denotes the conjugate transpose of W .

(b) To every matrix in SU(1, 1) we can associate a fractional linear transformation

$$
{ \frac { a z + b } { c z + d } } .
$$

Prove that the group SU(1, 1)/{±1} is isomorphic to the group of automorphisms of the disc. [Hint: Use the following association.]

$$
e ^ { 2 i \theta } \frac { z - \alpha } { 1 - \overline { { { \alpha } } } z } \longrightarrow \left( \begin{array} { c c } { { \frac { e ^ { i \theta } } { \sqrt { 1 - | \alpha | ^ { 2 } } } } } & { { - \frac { \alpha e ^ { i \theta } } { \sqrt { 1 - | \alpha | ^ { 2 } } } } } \\ { { - \frac { \overline { { { \alpha } } } e ^ { - i \theta } } { \sqrt { 1 - | \alpha | ^ { 2 } } } } } & { { \frac { e ^ { - i \theta } } { \sqrt { 1 - | \alpha | ^ { 2 } } } } } \end{array} \right) .
$$

5. The following result is relevant to Problem 4 in Chapter 10 which treats modular functions.

(a) Suppose that $F : \mathbb { H }  \mathbb { C }$ is holomorphic and bounded. Also, suppose that $F ( z )$ vanishes when $z = i r _ { n } , n = 1 , 2 , 3 , . . . ,$ where $\{ r _ { n } \}$ is a bounded sequence of positive numbers. Prove that if $\textstyle \sum _ { n = 1 } ^ { \infty } r _ { n } = \infty$ , then $F = 0$

(b) If $\textstyle \sum r _ { n } < \infty$ , it is possible to construct a bounded function on the upper half-plane with zeros precisely at the points $i r _ { n }$

For related results in the unit disc, see Problems 1 and 2 in Chapter 5.]

${ \bf 6 . ^ { * } }$ The results of Exercise 18 extend to the case when $\gamma$ is assumed merely to be closed, simple, and continuous. The proof, however, requires further ideas.

7.∗ Applying ideas of Carath´eodory, Koebe gave a proof of the Riemann mapping theorem by constructing (more explicitly) a sequence of functions that converges to the desired conformal map.

Starting with a Koebe domain, that is, a simply connected domain $\kappa _ { 0 } \subset \mathbb { D }$ that is not all of D, and which contains the origin, the strategy is to find an injective function $f _ { 0 }$ such that $f _ { 0 } ( \mathcal { K } _ { 0 } ) = \mathcal { K } _ { 1 }$ is a Koebe domain “larger” than $\kappa _ { 0 }$ . Then, one iterates this process, finally obtaining functions $F _ { n } = f _ { n } \circ \cdot \cdot \cdot \circ f _ { 0 } : \mathcal { K } _ { 0 } \to \mathbb { D }$ such that $F _ { n } ( { \cal K } _ { 0 } ) = { \cal K } _ { n + 1 }$ and lim $F _ { n } = F$ is a conformal map from $\kappa _ { 0 }$ to D.

The inner radius of a region $\kappa \subset \mathbb { D }$ that contains the origin is defined by $r _ { \mathcal { K } } = \operatorname* { s u p } \{ \rho \ge 0 : D ( 0 , \rho ) \subset \mathcal { K } \}$ . Also, a holomorphic injection $f : \mathcal { K }  \mathbb { D }$ is said to be an expansion if $f ( 0 ) = 0$ and $| f ( z ) | > | z |$ for all $z \in \mathcal { K } - \{ 0 \}$

(a) Prove that if $f$ is an expansion, then $r _ { f ( \mathcal { K } ) } \ge r _ { \mathcal { K } }$ and $\left| f ^ { \prime } ( 0 ) \right| > 1$ [Hint: Write $f ( z ) = z g ( z )$ and use the maximum principle to prove that $\left| f ^ { \prime } ( 0 ) \right| =$ $| g ( 0 ) | > 1 . ]$

Suppose we begin with a Koebe domain $\kappa _ { 0 }$ and a sequence of expansions $\{ f _ { 0 } , f _ { 1 } , \dotsc , f _ { n } , \dotsc \}$ , so that ${ \boldsymbol { \mathcal { K } } } _ { n + 1 } = f _ { n } ( { \boldsymbol { \mathcal { K } } } _ { n } )$ are also Koebe domains. We then define holomorphic maps $F _ { n } : { \mathcal { K } } _ { 0 } \to \mathbb { D } { \mathrm { ~ b y ~ } } F _ { n } = f _ { n } \circ \cdot \cdot \cdot \circ f _ { 0 }$

(b) Prove that for each n, the function $F _ { n }$ is an expansion. Moreover, $\begin{array} { r } { F _ { n } ^ { \prime } ( 0 ) = \prod _ { k = 0 } ^ { n } f _ { k } ^ { \prime } ( 0 ) } \end{array}$ , and conclude that lim $_ { 1 n \longrightarrow \infty } | f _ { n } ^ { \prime } ( 0 ) | = 1$ . [Hint: Prove that the sequence $\{ | F _ { n } ^ { \prime } ( 0 ) | \}$ has a limit by showing that it is bounded above and monotone increasing. Use the Schwarz lemma.]

(c) Show that if the sequence is osculating, that is, $r \kappa _ { n }  1$ as $n \to \infty$ , then $\{ F _ { n } \}$ converges uniformly on compact subsets of $\kappa _ { 0 }$ to a conformal map $F : { \mathcal { K } } _ { 0 } \to \mathbb { D } .$ [Hint: If $r _ { F ( \mathcal { K } _ { 0 } ) } \ge 1$ then $F$ is surjective.]

To construct the desired osculating sequence we shall use the automorphisms $\psi _ { \alpha } = ( \alpha - z ) / ( 1 - \overline { { \alpha } } z )$

(d) Given a Koebe domain $\kappa ,$ , choose a point $\alpha \in \mathbb { D }$ on the boundary of $\kappa$ such that $| \alpha | = r \kappa$ , and also choose ${ \boldsymbol { \beta } } \in \mathbb { D }$ such that $\beta ^ { 2 } = \alpha$ . Let $S$ denote the square root of $\psi _ { \alpha }$ on $\kappa$ such that $S ( 0 ) = 0$ . Why is such a function well defined? Prove that the function $f : \mathcal { K }  \mathbb { D }$ defined by $f ( z ) = \psi _ { \beta } \circ S \circ \psi _ { \alpha }$ is an expansion. Moreover, show that $| f ^ { \prime } ( 0 ) | = ( 1 + r \kappa ) / 2 \sqrt { r \kappa } .$ . [Hint: To prove that $| f ( z ) | > | z |$ on $\kappa - \{ 0 \}$ apply the Schwarz lemma to the inverse function, namely $\psi _ { \alpha } \circ g \circ \psi _ { \beta }$ where $g ( z ) = z ^ { 2 } . ]$

(e) Use part (d) to construct the desired sequence.

8.∗ Let f be an injective holomorphic function in the unit disc, with $f ( 0 ) = 0$ and $f ^ { \prime } ( 0 ) = 1$ . If we write $f ( z ) = z + a _ { 2 } z ^ { 2 } + a _ { 3 } z ^ { 3 } \cdot \cdot \cdot$ , then Problem 1 in Chapter 3 shows that $| a _ { 2 } | \le 2$ Bieberbach conjectured that in fact $\left. a _ { n } \right. \leq n$ for all $n \geq 2$ ; this was proved by deBranges. This problem outlines an argument to prove the conjecture under the additional assumption that the coefficients $a _ { n }$ are real.

(a) Let $z = r e ^ { i \theta }$ with $0 < r < 1$ , and show that if $v ( r , \theta )$ denotes the imaginary part of $f ( r e ^ { i \theta } )$ , then

$$
a _ { n } r ^ { n } = { \frac { 2 } { \pi } } \int _ { 0 } ^ { \pi } v ( r , \theta ) \sin n \theta d \theta .
$$

(b) Show that for $0 \leq \theta \leq \pi$ and $n = 1 , 2 , \ldots$ . we have $| \sin n \theta | \leq n$ sin θ.

(c) Use the fact that $a _ { n } \in \mathbb { R }$ to show that $f ( \mathbb { D } )$ is symmetric with respect to the real axis, and use this fact to show that f maps the upper half-disc into either the upper or lower part of $f ( \mathbb { D } )$

(d) Show that for r small,

$$
v ( r , \theta ) = r \sin \theta [ 1 + O ( r ) ] ,
$$

and use the previous part to conclude that $v ( r , \theta )$ sin $\theta \ge 0$ for all $0 < r < 1$ and $0 \leq \theta \leq \pi$

(e) Prove that $| a _ { n } r ^ { n } | \leq n r$ , and let $r \to 1$ to conclude that $\left. a _ { n } \right. \leq n$

(f) Check that the function $f ( z ) = z / ( 1 - z ) ^ { 2 }$ satisfies all the hypotheses and that $\left. a _ { n } \right. = n$ for all n.

9.∗ Gauss found a connection between elliptic integrals and the familiar operations of forming arithmetic and geometric means.

We start with any pair $( a , b )$ of numbers that satisfy $a \geq b > 0$ , and form the arithmetic and geometric means of a and $b ,$ that is,

$$
a _ { 1 } = \frac { a + b } { 2 } \mathrm { a n d } b _ { 1 } = ( a b ) ^ { 1 / 2 } .
$$

We then repeat these operations with a and b replaced by $a _ { 1 }$ and $b _ { 1 }$ . Iterating this process provides two sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ where $a _ { n + 1 }$ and $b _ { n + 1 }$ are the arithmetic and geometric means of $a _ { n }$ and $b _ { n }$ , respectively.

(a) Prove that the two sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ have a common limit. This limit, which we denote by $M ( a , b )$ , is called the arithmetic-geometric mean of a and b. [Hint: Show that $a \geq a _ { 1 } \geq a _ { 2 } \geq \cdot \cdot \cdot \geq a _ { n } \geq b _ { n } \geq \cdot \cdot \cdot \geq$ $b _ { 1 } \geq b$ and $a _ { n } - b _ { n } \leq ( a - b ) / 2 ^ { n } . ]$

(b) Gauss’s identity states that

$$
\frac { 1 } { M ( a , b ) } = \frac { 2 } { \pi } \int _ { 0 } ^ { \pi / 2 } \frac { d \theta } { ( a ^ { 2 } \cos ^ { 2 } \theta + b ^ { 2 } \sin ^ { 2 } \theta ) ^ { 1 / 2 } } .
$$

To prove this relation, show that if $I ( a , b )$ denotes the integral on the righthand side, then it suffices to establish the invariance of $I ,$ namely

$$
I ( a , b ) = I \left( { \frac { a + b } { 2 } } , ( a b ) ^ { 1 / 2 } \right) .\tag{6}
$$

Then, observe that the connection with elliptic integrals takes the form

$$
I ( a , b ) = { \frac { 1 } { a } } K ( k ) = { \frac { 1 } { a } } \int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { ( 1 - x ^ { 2 } ) ( 1 - k ^ { 2 } x ^ { 2 } ) } } } \mathrm { ~ w h e r e ~ } k ^ { 2 } = 1 - b ^ { 2 } / a ^ { 2 } ,
$$

and that the relation (6) is a consequence of the identity in (b) of Exercise 24.

# 9 An Introduction to Elliptic Functions

The form that Jacobi had given to the theory of elliptic functions was far from perfection; its flaws are obvious. At the base we find three fundamental functions sn, cn and dn. These functions do not have the same periods...

In Weierstrass’ system, instead of three fundamental functions, there is only one, ℘(u), and it is the simplest of all having the same periods. It has only one double infinity; and finally its definition is so that it does not change when one replaces one system of periods by another equivalent system.

H. Poincar´e, 1899

The theory of elliptic functions, which is of interest in several parts of mathematics, initially grew out of the study of elliptic integrals. These can be described generally as integrals of the form  $R ( x , { \sqrt { P ( x ) } } )$ dx, where R is a rational function and P a polynomial of degree three or four.1 These integrals arose in computing the arc-length of an ellipse, or of a lemniscate, and in a variety of other problems. Their early study was centered on their special transformation properties and on the discovery of an inherent double-periodicity. We have seen an example of this latter phenomenon in the mapping function of the half-plane to a rectangle taken up in Section 4.5 of the previous chapter.

It was Jacobi who transformed the subject by initiating the systematic study of doubly-periodic functions (called elliptic functions). In this theory, the theta functions he introduced played a decisive role. Weierstrass after him developed another approach, which in its initial steps is simpler and more elegant. It is based on his ℘ function, and in this chapter we shall sketch the beginnings of that theory. We will go as far as to glimpse a possible connection with number theory, by considering the Eisenstein series and their expression involving divisor functions. A number of more direct links with combinatorics and number theory arise from the theta