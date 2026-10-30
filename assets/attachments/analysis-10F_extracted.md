## ANALYSIS QUALIFYING EXAM, FALL 2010

Instructions: Work any 10 problems and therefore at least 4 from Problems 1-6 and at least 4 from Problems 7-12. All problems are worth ten points. Full credit on one problem will be better than part credit on two problems. If you attempt more than 10 problems, indicate which 10 are to be graded.

Notation: $\mathbb { D } = \{ z \in \mathbb { C } ; | z | < 1 \}$ is the open unit disk.

1: For this problem, consider just Lebesgue measurable functions $f : [ 0 , 1 ] \to \mathbb { R }$ together with the Lebesgue measure.

(a) State Fatou's lemma (no proof required).

(b) State and prove the Dominated Convergence Theorem.

(c) Give an example where $f _ { \mathscr { n } } ( x )  0 ~ \mathrm { a . e . }$ , but $\int f _ { \eta , } ( x ) d x \longrightarrow 1$

2: Prove the following form of Jensen's inequality:

If $f : [ 0 , 1 ]  \mathbb { R }$ is continuous then

$$
\int _ { 0 } ^ { 1 } e ^ { f ( x ) } d x \geq \exp { \left\{ \int _ { 0 } ^ { 1 } f ( x ) d x \right\} } .
$$

Moreover, if equality occurs then $f$ is a constant function.

3: Consider the following sequence of functions:

$$
f _ { n } : [ 0 , 1 ] \to \mathbb { R } \quad \mathrm { b y } \quad f _ { n } ( x ) = \exp \{ \sin ( 2 \pi n x ) \} .
$$

a) Prove that $f _ { n }$ converges weakly in $L ^ { 1 } \{ [ 0 , 1 ] \}$

(b) Prove that $f _ { \pi }$ converges weak-\* in $I ^ { \infty } ( [ 0 , 1 ] )$ , viewed as the dual of $L ^ { 1 } ( [ 0 , \frac { \gamma } { 2 } ] )$

4: Let $T$ be a linear transformation on $C _ { c } ^ { 0 } ( \Re )$ , the space of continuous functions of compact support, that has the following two properties:

$$
\| T f \| _ { L ^ { \infty } } \leq \| f \| _ { L ^ { \infty } } \quad { \mathrm { a n d } } \ . \ | \{ x \in \mathbb { R } : | T f ( x ) | > \lambda \} | \leq { \frac { \| f \| _ { L ^ { 1 } } } { \lambda } } .
$$

(Here $| A |$ denotes the Lebesgue measure of the set $A . )$ Prove that

$$
\int | T f ( x ) | ^ { 2 } d x \leq C \int | f ( x ) | ^ { 2 } d x
$$

for all $f \in C _ { c } ^ { 0 } ( \mathbb { R } )$ and some fixed number C.

5: Let $\mathbb { R } / \mathbb { Z }$ denote the torus (whose elements we will write as cosets) and fix an irrational number $\alpha > 0$

(a) Show that

$$
\operatorname* { l i m } _ { N  \infty } { \frac { 1 } { N } } \sum _ { n = 0 } ^ { N - 1 } f ( n \alpha + \mathbb { Z } ) = \int _ { 0 } ^ { 1 } f ( x + \mathbb { Z } ) d x
$$

for all continuous functions $f : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$ Hint: consider first $f ( x ) = e ^ { 2 \pi i k x } ]$ (b) Show that the conclusion is also true when $f$ is the characteristic function of a closed interval.

6: Let $\bar { \mathbb { D } } : = \{ z \in \mathbb { C } : | z | \leq 1 \}$ and consider the (complex) Hilbert space

$$
{ \mathcal { H } } : = \left\{ f : { \bar { \mathbb { B } } } \to \mathbb { C } \Big | f ( z ) = \sum _ { k = 0 } ^ { \infty } { \hat { f } } ( k ) z ^ { k } \quad { \mathrm { w i t h } } \quad | | f | | ^ { 2 } : = \sum _ { k = 0 } ^ { \infty } ( 1 + | k | ^ { 2 } ) | { \hat { f } } ( k ) | ^ { 2 } < \infty \right\}
$$

(a) Prove that the linear functional $L : f \mapsto f ( 1 )$ is bounded.

(b) Find the element $g \in H$ representing L.

c) Show that $f \mapsto \operatorname { R e } L ( f )$ achieves its maximal value on the set

$$
B : = \{ f \in { \mathcal { H } } : \| f \| \leq 1 \quad { \mathrm { a n d } } \quad f ( 0 ) = 0 \} ,
$$

that this maximum occurs at a unique point, and determine this maximal value.

7: Suppose that $f : \mathbb { C } \to \mathbb { C }$ is continuous on C and holomorphic on $\mathbb { C } \backslash \mathbb { R } = \{ z \in \mathbb { C } ; z \notin \mathbb { R } \}$ Prove that $f$ is entire.

8: Let $A ( \mathbb { D } )$ be the C-vector space of all holomorphic functions on D and suppose that $L : A ( { \mathfrak { P } } ) \to \mathbb { C }$ is a multiplicative linear functional, that is

$$
L ( a f + b g ) = a L ( f ) + b L ( g ) { \mathrm { ~ a n d ~ } } L ( f g ) = L ( f ) L ( g )
$$

for all $a , b \in \mathbb { C }$ and all $f , g \in A ( \mathbb { D } )$ . If L is not identically zero, show that there is ${ \mathfrak { a } } z _ { 0 } \in \mathbb { D }$ so that $L ( f ) = f ( z _ { 0 } )$ for all $f \in A ( \mathfrak { D } ) \}$ •

9: Let

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }
$$

be a holomorphic function in D. Show that if

$$
\sum _ { n = 2 } ^ { \infty } n | a _ { n } | \leq | a _ { 1 } |
$$

with $a _ { 1 } \neq 0$ then f is injective.

10: Prove that the punctured disc $\{ z \in \mathbb { C } ; 0 < | z | < 1 \}$ and the annulus given by $\{ z \in \mathbb { C } ; 1 < | z | < 2 \}$ are not conformally equivalent.

11: Let $\Omega \subset \mathbb { C }$ be a non-empty open connected set. If $f : \Omega  \mathbb { C }$ is harmonic and $f ^ { 2 }$ is also harmonic, show that either f or f is holomorphic on Ω.

12: Let $F$ be the family of functions f holomorphic on D with

$$
\int \int _ { x ^ { 2 } + y ^ { 2 } < 1 } | f ( x + i y ) | ^ { 2 } d x d y < 1 .
$$

Prove that for each compact subset $K \subset \mathbb { D }$ there is a constant A so that $| f ( z ) | < A$ for all $z \in K$ and all $f \in \mathcal F$ †