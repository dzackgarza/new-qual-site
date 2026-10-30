## MATH 220; Complex Analysis Qualifying exam. May 24, 2004

General instructions: 3 hours. No books or notes. Be sure to motivate all (nontrivial) claims and statements (and be careful in your estimates). You may use without proof any result proved in the text (i.e. Chap. I-IX.1 in Conway; if you are not sure, ask!). You need to reprove any result given as an exercise. The notation $B ( a , r ) : = \{ z \colon | z - a | < r \}$ and $\mathbb { D } : = B ( 0 , 1 )$ will be used. Moreover, G denotes an open region of the complex plane and O(G) the space of analytic functions in G.

Specific instructions: Do problem 1 (true or false) and choose 4 of the remaining 5 problems (26). Indicate clearly on the front page which 4 problems you want graded!

1. For each of the following, determine if the statement is true or false. If true, give a proof. If false, disprove it (e.g. by giving a counterexample). (Hint: each problem has a short solution.)

(a) (10p) There is a Möbius (linear fractional) transformation sending the triangle with vertices at $\{ 0 , i , 1 \}$ to that with vertices at $\{ 0 , i , 2 \}$ •

(b) (10p) Let $( X , d )$ be a metric space. If a Cauchy sequence $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ in X has a convergent subsequence, then $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ is convergent.

c) (10p) Let $\gamma _ { + } ( t ) = e ^ { i \pi t }$ and $\gamma _ { - } ( t ) = e ^ { - i \pi t }$ , for $t \in \{ 0 , 1 \}$ .Then, we have

$$
\int _ { \gamma _ { + } } { \frac { 2 } { ( 2 z - 1 ) ^ { 2 } } } d z = \int _ { \gamma _ { - } } { \frac { 2 } { ( 2 z - 1 ) ^ { 2 } } } d z .
$$

(d) (10p) Let $f _ { n } \in { \mathcal { O } } ( G )$ be a sequence such that $f _ { n } ( G ) \subset \mathbb { D } \backslash \{ 0 \}$ , for $n = 1 , 2 , . . . ,$ and assume that $f _ { n } \to f$ in ${ \mathcal { O } } ( G )$ (as a metric space). Then, either f is constant or $f ( G ) \subset \mathbb { D } \setminus \{ 0 \}$

(e) (10p) There is a sequence of complex numbers $\{ a _ { n } \} _ { n = 0 } ^ { \infty }$ and strictly increasing sequence of integers $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ with $p _ { n } \geq n$ such that the radius of convergence of

$$
\sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }
$$

is one but that of

$$
\sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { p _ { n } }
$$

is less than one.

<!-- image-->

2. (25p) Let $f \in { \mathcal { O } } ( { \mathfrak { D } } )$ and assume that $| f ( z ) | \leq 1$ in D. Show that

$$
{ \frac { | f ( 0 ) | - | z | } { 1 + | f ( 0 ) | | z | } } \leq | f ( z ) | \leq { \frac { | f ( 0 ) | + | z | } { 1 - | f ( 0 ) | | z | } } .
$$

3. (25p) Let f and g be meromorphic functions in C. Assume that

$$
| f ( z ) + g ( z ) | \leq | g ( z ) |
$$

for every $z \in \mathbb { C }$ which is not a pole of either f or g. Show that there is a constant c with $| c + 1 | \leq 1$ such that $f ( z ) = c g ( z )$

4. (25p) Let G be an open connected and bounded subset of the plane $\mathbb { C } ,$ and $f \colon G \to \mathbb { C }$ an analytic function with $f ( G ) \subset G$ Let $f ^ { n }$ denote the nth iterate of f, i.e.

$$
f ^ { n } ( z ) = \underbrace { f \circ f \circ . . . \circ f } _ { n { \mathrm { ~ t i m e s } } } ( z ) .
$$

Suppose that $a \in G$ is a fixed point of $f \ ( { \mathrm { i . e . } } \ f ( a ) = a )$ and $\left| f ^ { \prime } ( a ) \right| < 1$ . Define the basin of attraction of $z = a$ to be the set

$$
\Omega : = \{ z \in G \colon \operatorname* { l i m } _ { n  \infty } f ^ { n } ( z ) = a \} .
$$

<!-- image-->

(a) Show that there is a $\delta > 0$ such that $\{ z \colon | z - a | < \delta \} \subset \Omega$

(b) Show, using part (a), that in fact $\Omega = G$

5. (25p) Let K be a compact subset of the plane C and $\hat { K }$ its polynomial hull, i.e.

$$
\hat { K } : = \{ z \in \mathbb { C } : | p ( z ) | \leq \operatorname* { s u p } _ { w \in K } | p ( w ) | , \mathrm { ~ f o r ~ e v e r y ~ p o l y n o m i a l ~ } p \} .
$$

Show that if $z \in \mathbb { C } \backslash K$ and there is a curve $\gamma \subset \mathbb { C } _ { \infty } \backslash K$ connecting z to ∞, then $z \not \in { \hat { K } }$

6. (25p) Let $G$ be an open region in C and $\left\{ z _ { n } \right\}$ a sequence of distinct points in G without limit points in G. Suppose that for each n, you are given an integer $m _ { n }$ and a sequence of complex numbers $\{ w _ { n , k } \} _ { k = 0 } ^ { m _ { n } }$ Show that there is $f \in H ( G )$ such that, for every $n ,$

$$
f ^ { ( k ) } ( z _ { n } ) = w _ { n , k } , \ k = 0 , 1 , \ldots , m _ { n } .
$$

Hint: First show that, given an integer m, complex numbers $w _ { k }$ for $k = 1 , \ldots , m$ a point $z = a ,$ , and an analytic function g which vanishes to order $m + 1$ at $z = a$ then one can find a rational function

$$
S ( z ) = \sum _ { k = 1 } ^ { m + 1 } { \frac { b _ { k } } { ( z - a ) ^ { k } } }
$$

<!-- image-->

such that the product $f ( z ) = S ( z ) g ( z )$ has a removable singularity at $z = a$ and

$$
\begin{array} { r } { f ^ { ( k ) } ( a ) = w _ { k } , \ k = 0 , 1 , \dots , m . } \end{array}
$$