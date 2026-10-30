## Real Analysis Qualifying Exam, January, 2017

(1) Let $( \Omega , A , \mu )$ be a measure space. Prove directly from the definition of convergence almost everywhere that if for all $n _ { \mathrm { : } }$ $\mu \{ x \in \Omega : | f _ { n } ( x ) | > 1 / n \} < n ^ { - 3 / 2 }$ , then $f _ { n } \to 0 { \mathrm { ~ a . e . ~ } } ( \mu )$

(2) Find all f in $L ^ { 1 } ( 1 , 2 )$ such that for every natural number n we have $\textstyle \int _ { 1 } ^ { 2 } x ^ { 2 n } f ( x ) d x = 0$ . Give reasons for all assertions you make.

(3) A. Prove that there exists a sequence of measurable functions $g _ { n }$ on [0, 1] such that:

(a) $g _ { n } ( x ) \geq 0$ for any $x \in [ 0 , 1 ]$

(b) lim $g _ { n } ( x ) = 0 { \mathrm { ~ a . e . } } _ { }$ n→∞

(c) For any continuous function $f \in C [ 0 , 1 ]$

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f ( x ) g _ { n } ( x ) d x = \int _ { 0 } ^ { 1 } f ( x ) d x .
$$

B. If $g _ { n }$ is a sequence of measurable functions on $[ 0 , 1 ]$ such that $\mathrm { ( a ) }$ (b), and (c) are satisfied, what can you say about $\begin{array} { r } { \int _ { 0 } ^ { 1 } \operatorname* { s u p } _ { n } g _ { n } ( x ) d x ? } \end{array}$

(4) We say that a sequence $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ in $[ 0 , 1 ]$ is equidistributed (in [0, 1]) if and only if for all intervals $[ c , d ] \subset [ 0 , 1 ]$ 2

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { \left| \left\{ a _ { 1 } , \dots , a _ { n } \right\} \cap \left[ c , d \right] \right| } { n } } = d - c .
$$

(Here $| A |$ denotes the number of elements in the set $A . )$

Let $\dot { \mu _ { N } } \dot { = } \frac { 1 } { N } \sum _ { 1 \le n \le N } \delta _ { a _ { n } }$ with $\delta _ { a _ { n } }$ the point measure at $a _ { n }$ , that is, for

any subset $S \in [ 0 , 1 ] , \delta _ { a _ { n } } ( S ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } a _ { n } \in S } \\ { 0 } & { { \mathrm { i f ~ } } a _ { n } \not \in S } \end{array} \right. } .$

Show that $\{ a _ { n } \} \subset [ 0 , 1 ]$ is equidistributed if and only if

$$
\operatorname* { l i m } _ { N  \infty } \int _ { 0 } ^ { 1 } f d \mu _ { N } = \int _ { 0 } ^ { 1 } f d m ,
$$

for all continuous functions on [0, 1], where m is Lebesgue measure.

(5) Consider the space $C ( [ 0 , 1 ] )$ of real-valued continuous functions on the unit interval [0, 1]. We denote by $\| f \| _ { \infty } : = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | f ( x ) |$ the supremum norm of $f \in C ( [ 0 , 1 ] )$ and by $\begin{array} { r } { \| f \| _ { 2 } : = ( \int _ { 0 } ^ { 1 } | \dot { f } ( x ) | ^ { 2 } d x ) ^ { \frac { 1 } { 2 } } } \end{array}$ the $L ^ { 2 } \mathrm { - n o r m }$ of $f \in C ( [ 0 , 1 ] )$ . Let S be a closed linear subspace of $( C ( [ 0 , 1 ] ) , \parallel \cdot \parallel _ { \infty } )$ . Show that if S is complete in the norm $\| \cdot \| _ { 2 }$ , then S is finite-dimensional.

(6) Prove that if a function $f : [ 0 , 1 ] \to \mathbb { R }$ is Lipschitz, with

$$
| f ( x ) - f ( y ) | \leq M | x - y |
$$

for all $x , \ y \in [ 0 , 1 ]$ , then there is a sequence of continuously differentiable functions ${ \overline { { f _ { n } } } } : [ 0 , 1 ] \to \mathbb { R }$ such that

(i) $| f _ { n } ^ { \prime } ( x ) | \leq M$ for all $x \in [ 0 , 1 ] ;$

(ii) $f _ { n } ( x )  f ( x )$ for all $x \in [ 0 , 1 ]$

(7) Given $f : \mathbb { R } \to \mathbb { R }$ bounded and uniformly continuous and $K _ { n }$ with $K _ { n } \in L ^ { 1 } ( \mathbb { R } )$ for $n = 1 , 2 , 3 , \cdots$ such that

(i) $\| K _ { n } \| _ { 1 } \leq M < \infty , n = 1 , 2 , 3 , \cdot \cdot \cdot$

(ii) $\begin{array} { r } { \int _ { - \infty } ^ { \infty } K _ { n } ( x ) d x  1 \mathrm { ~ a s ~ } n  \infty . } \end{array}$

(iii) $\begin{array} { r } { \int _ { \{ x : | x | > \delta \} } | K _ { n } ( x ) |  0 \mathrm { ~ a s ~ } n  \infty } \end{array}$ for all $\delta > 0$

Show that ${ \dot { K } } _ { n } * f \to f$ uniformly, where

$$
K _ { n } * f ( x ) = \int _ { - \infty } ^ { \infty } K _ { n } ( y ) f ( x - y ) d y .
$$

(8) A. Construct a Lebesgue measurable subset A of of R so that for all reals $a < b , 0 < m ( A \cap [ a , b ] ) < b - a$ , where m is Lebesgue measure on R.

B. Suppose $A \subseteq \mathbb { R }$ is a Lebesgue measurable set and assume that

$$
m ( A \cap ( a , b ) ) \leq { \frac { b - a } { 2 } }
$$

for any $a , b \in \mathbb { R } , a < b$ . Prove that $\mu ( A ) = 0$

(9) Prove or disprove that the unit ball of $L ^ { 7 } ( 0 , 1 )$ is norm closed in $L ^ { 1 } ( 0 , 1 )$

(10) Let C be the Banach space of convergent sequences of real numbers under the supremum norm. Compute the extreme points of the closed unit ball, B, of C and determine whether B is the closed convex hull of its extreme points.

(11) Show that every convex continuous function defined on the closed unit ball of a reflexive Banach space achieves a minimum. (A convex function on a convex subset A of a normed space is a real valued function, f , on A s.t. for every $x , y \in A$ and every $0 < \lambda < 1$ we have $f ( \lambda x + ( 1 - \lambda ) y ) \leq \lambda f ( x ) + ( 1 - \lambda ) f ( y ) . )$