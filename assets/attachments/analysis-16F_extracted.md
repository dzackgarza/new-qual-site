# ANALYSIS QUALIFYING EXAM: FALL 2016

Ten of the twelve problems will be counted for the total score, at least four from Problems 1–6, and at least four from Problems 7–12. Please indicate on the front of your exam which ten problems you wish to have graded.

Problem 1. We consider the space $L ^ { 1 } ( \mu )$ of integrable functions on a measure space $( X , { \mathcal { M } } , \mu )$ . For $g \in L ^ { 1 } ( \mu )$ let

$$
\| g \| _ { 1 } = \int | g ( x ) | d \mu
$$

be the corresponding $L ^ { 1 } { \mathrm { - n o r m } }$ . Suppose that f and $f _ { n }$ for $n \in \mathbb N$ are functions in $L ^ { 1 } ( \mu )$ such that

(i) $f _ { n } ( x )  f ( x )$ for µ-almost every $x \in X$ and

(ii) $\| f _ { n } \| _ { 1 } \to \| f \| _ { 1 }$

Show that then $\vert \vert f _ { n } - f \vert \vert _ { 1 } \to 0 .$

Problem 2. Let $\mu$ be a finite positive Borel measure on R that is singular to Lebesgue measure. Show that

$$
\operatorname* { l i m } _ { r \to 0 ^ { + } } { \frac { \mu ( [ x - r , x + r ] ) } { 2 r } } = + \infty
$$

for µ-almost every $x \in \mathbb { R }$

Problem 3. If X is a compact metric space, we denote by ${ \mathcal { P } } ( X )$ be the set of positive Borel measures µ on X with $\mu ( X ) = 1$

(a) Let $\varphi \colon X  [ 0 , \infty ]$ be a lower-semicontinuous function on a compact metric space X. Show that if $\mu$ and $\mu _ { n }$ for $n \in \mathbb N$ are in ${ \mathcal { P } } ( X )$ and $\mu _ { n }  \mu$ with respect to the weak-star topology on ${ \mathcal { P } } ( X )$ , then

$$
\int \phi d \mu \leq \operatorname* { l i m } _ { n \to \infty } \int \phi d \mu _ { n } .
$$

(b) Let $K \subset \mathbb { R } ^ { d }$ be a compact set. For $\mu \in { \mathcal { P } } ( K )$ , we define

$$
E ( \mu ) = \int _ { K } \int _ { K } { \frac { 1 } { | x - y | } } d \mu ( x ) d \mu ( y ) .
$$

Here |z| denotes the Euclidean norm of $z \in \mathbb { R } ^ { d }$

Show that the function $E \colon { \mathcal { P } } ( K )  [ 0 , \infty ]$ attains its minimum on $\mathcal { P } ( K )$ (which could possibly be ∞).

Problem 4. Let $L ^ { 1 } = L ^ { 1 } ( [ 0 , 1 ] )$ be the space of integrable and $L ^ { 2 } = L ^ { 2 } ( [ 0 , 1 ] )$ b e the space of square-integrable functions on [0, 1]. Then $L ^ { 2 } \subset L ^ { 1 }$ . Show that $L ^ { \bar { 2 } }$ is a meager subset of $L ^ { 1 } , \mathrm { i . e . , } L ^ { 2 }$ can be written as a countable union of sets in $L ^ { 1 }$ that are closed and have empty interior in $L ^ { 1 }$

Problem 5. Let $X \ = \ C ( [ 0 , 1 ] )$ be the Banach space of real-valued continuous functions on [0, 1] equipped with the norm

$$
\| f \| = \operatorname* { m a x } _ { x \in [ 0 , 1 ] } | f ( x ) | .
$$

Let $\mathcal { A }$ be the Borel σ-algebra on $X .$

Show that A is the smallest σ-algebra on X that contains all sets of the form

$$
S ( t , B ) = \{ f \in X : f ( t ) \in B \} ,
$$

where $t \in [ 0 , 1 ]$ and $B \subset \mathbb { R }$ is a Borel set in R.

Problem 6. Consider the Banach space $\ell ^ { 1 }$ consisting of all sequences $u = \{ x _ { i } \}$ in R $( \mathrm { i . e . , } x _ { i } \in \mathbb { R }$ for $i \in \mathbb { N } )$ with

$$
\| u \| _ { 1 } = \sum _ { i = 1 } ^ { \infty } \left| x _ { i } \right| < \infty
$$

and the Banach space $\ell ^ { \infty }$ consisting of all sequences $v = \{ y _ { i } \}$ in R with

$$
\| v \| _ { \infty } = \operatorname* { s u p } _ { i \in \mathbb { N } } | y _ { i } | < \infty .
$$

There is a well-defined dual paring between $\ell ^ { 1 }$ and $\ell ^ { \infty }$ given by

$$
\langle u , v \rangle = \sum _ { i = 1 } ^ { \infty } x _ { i } y _ { i }
$$

for $u = \{ x _ { i } \} \in \ell ^ { 1 }$ and $v = \{ y _ { i } \} \in \ell ^ { \infty }$ . With this dual pairing, $\ell ^ { \infty } = ( \ell ^ { 1 } ) ^ { * }$ is the dual space of $\ell ^ { 1 }$

(a) Show that there exists no sequence $\{ u _ { n } \}$ in $\ell ^ { 1 }$ such that $\mathrm { ( i ) } \parallel u _ { n } \parallel _ { 1 } \geq 1$ for all $n \in \mathbb { N }$ and (ii) $\left. u _ { n } , v \right. \to 0$ for each $v \in \ell ^ { \infty }$

(b) Show that every weakly convergent sequence $\{ u _ { n } \}$ in $\ell ^ { 1 }$ converges in the norm topology of $\ell ^ { 1 }$ .

Problem 7. Let H be space of holomorphic functions $f$ on the unit disc $\mathbb { D } = \left\{ z \in \right.$ $\mathbb { C } : | z | < 1 \}$ such that

$$
\int _ { \mathbb { D } } | f ( z ) | ^ { 2 } d A ( z ) < \infty .
$$

Here integration is with respect to Lebesgue measure A on D. The vector space H is a Hilbert space if equipped with the inner product

$$
\langle f , g \rangle = \int _ { \mathbb { D } } f ( z ) { \overline { { g ( z ) } } } d A ( z )
$$

for $f , g \in { \mathcal { H } }$ . Fix $z _ { 0 } \in \mathbb { D }$ and define $L _ { z _ { 0 } } ( f ) = f ( z _ { 0 } )$ for $f \in \mathcal H$

(a) Show that $L _ { z _ { 0 } } \colon \mathcal { H } \to \mathbb { C }$ is a bounded linear functional on $\mathcal { H } .$

(b) Find an explicit function $g _ { z _ { 0 } } \in \mathcal { H }$ such that

$$
L _ { z _ { 0 } } ( f ) = f ( z _ { 0 } ) = \langle f , g _ { z _ { 0 } } \rangle
$$

for all $f \in \mathcal { H }$

Problem 8. Let f be a continuous complex-valued function on the closed unit disk D such that f is holomorphic on the open disk $\mathbb { D } = \left\{ z \in \mathbb { C } : | z | < 1 \right\}$ and $f ( 0 ) \neq 0$

(a) Show that if $0 < r < 1$ and if $\textstyle \operatorname* { i n f } _ { | z | = r } | f ( z ) | > 0$ , then

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log | f ( r e ^ { i \theta } ) | d \theta \geq \log | f ( 0 ) | .
$$

(b) Show that $\left| \left\{ \theta \in [ 0 , 2 \pi ] : f ( e ^ { i \theta } ) = 0 \right\} \right| = 0$ , where $| E |$ denotes the Lebesgue measure of $E \subset [ 0 , \dot { 2 } \pi ]$

Problem 9. Let µ be a positive Borel measure on [0, 1] with $\mu ( [ 0 , 1 ] ) = 1$

(a) Show that the function f defined as

$$
f ( z ) = \int _ { [ 0 , 1 ] } e ^ { i z t } d \mu ( t )
$$

for $z \in \mathbb { C }$ is holomorphic on C.

(b) Suppose that there exists $n \in \mathbb { N }$ such that

$$
\operatorname* { l i m } _ { | z | \to \infty } | f ( z ) | / | z | ^ { n } < \infty .
$$

Show that then $\mu$ is equal to the Dirac measure $\delta _ { 0 }$ at 0.

Problem 10. Consider the quadratic polynomial $f ( z ) = z ^ { 2 } - 1$ on C. We are interested in the iterates $f ^ { n }$ of f defined to be $f ^ { 0 } = \operatorname { i d } _ { \mathbb { C } }$ the identity on C for $n = 0$ and as

$$
f ^ { n } = \underbrace { f \circ \cdot \cdot \cdot \circ f } _ { n { \mathrm { ~ f a c t o r s } } }
$$

for $n \in \mathbb { N } .$

(a) Find an explicit constant $M > 0$ such that the following dichotomy holds for each point $z \in \mathbb { C } \mathrm { : }$ : either ${ \mathrm { ( i ) ~ } } | f ^ { n } ( z ) |  \infty$ as $n \to \infty$ or (ii) $| f ^ { n } ( z ) | \leq M$ for all $n \in  { \mathbb { N } } _ { 0 }$ .

(b) Let U be the set of all $z \in \mathbb { C }$ for which the first alternative (i) holds and K be the set of all $z \in \mathbb { C }$ for which the second alternative (ii) holds.

Show that U is an open set and K is a compact set without “holes”, i.e., $\mathbb { C } \setminus K$ has no bounded connected components.

Problem 11. Suppose $f \colon \mathbb { C } \to \mathbb { C }$ is a holomorphic function such that the function $z \mapsto g ( z ) = f ( z ) f ( 1 / z )$ is bounded on $\mathbb { C } \setminus \{ 0 \}$ .

(a) Show that if $f ( 0 ) \neq 0$ , then f is constant.

(b) Show that if $f ( 0 ) = 0$ , then there exist $n \in \mathbb { N }$ and $a \in \mathbb { C }$ such that $f ( z ) = a z ^ { n }$ for all $z \in \mathbb { C }$

Problem 12. Let $U \subset \mathbb { C }$ be an open set and $K \subset U$ be a compact subset of U.

(a) Prove that there exists a bounded open set V with $K \subset V \subset { \overline { { V } } } \subset U$ such that ∂V consists of finitely many closed line segments. Hint: Consider a fine square grid.

(b) Let f be a holomorphic function on U. Show that there exists a sequence $\{ R _ { n } \}$ of rational functions such that $\operatorname { ( i ) } \ R _ { n } \to f$ uniformly on K and (ii) none of the functions $R _ { n }$ has a pole in K. Hint: First represent $f ( z )$ for $z \in K$ as a suitable integral over the set $\partial V$ and then notice that the integrand is equicontinuous in z.