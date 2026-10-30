## ANALYSIS QUALIFYING EXAM

September 14, 2011

Answer at most 10 questions. All problems are worth ten points; parts of a problem do not carry equal weight. On the front of your paper indicate which 10 problems you wish to have graded. You must demonstrate adequate knowledge of both real analysis (problems 16) and complex analysis (problems 7-12).

Problem 1. Prove Egorov's theorem, that is:   
Consider a sequence of measurable functions $f _ { \mathscr { n } } : [ 0 , 1 ] \to { \mathbb R }$ that converge (Lebesgue) almost everywhere to a measurable function $f : [ 0 , 1 ] \to \mathbb { R }$ . Then for any $\varepsilon > ^ { \ i } 0$ there exists a measurable set $E \subset \{ 0 , 1 \}$ with measure $| \overrightarrow { E } | <$ ε such that $f _ { \pi }$ converge uniformly on $[ 0 , 1 ] \backslash E$

Hint: You may want to consider the sets $\begin{array} { r } { \dot { E } _ { n } ( k ) = \cap _ { m \ge n } \{ x : | f _ { m } ( x ) - f ( x ) | < \frac { 1 } { k } \} } \end{array}$

Problem 2. (a) Let do denote surface measure on the unit sphere $\mathbb { S } ^ { 2 } \subset \mathbb { R } ^ { 3 }$ Note $\textstyle \int d \sigma ( x ) = 4 \pi$ .For $\xi \in \mathbb { R } ^ { 3 }$ , compute

$$
\int _ { { \mathbb S } ^ { 2 } } e ^ { i x \cdot \xi } d \sigma ( x ) ,
$$

where · denotes the usual inner product on $\mathbb { R } ^ { 3 }$

(b) Using this, or otherwise, show that the mapping

$$
f \mapsto \int _ { { \mathbb S } ^ { 2 } } \int _ { { \mathbb S } ^ { 2 } } f ( x + y ) d \sigma ( x ) d \sigma ( y )
$$

extends uniquely from the space of all $C ^ { \infty }$ functions on $\mathbb { R } ^ { 3 }$ with compact support to a bounded linear functional on $I ^ { 2 } ( \mathbb { R } ^ { 3 } )$

Problem 3. Let $1 < p , q <$ ∞ satisfying $\textstyle { \frac { 1 } { p } } + { \frac { 1 } { q } } = 1$ . Fix $f \in L ^ { p } ( \mathbb { R } ^ { 3 } )$ and ${ \mathfrak { g } } \in L ^ { \mathfrak { q } } ( \mathbb { R } ^ { 3 } ) .$ (a) Show that

$$
[ f * g ] ( x ) : = \int _ { \mathbb { R } ^ { 3 } } f ( x - y ) g ( y ) d y
$$

defines a continuous function on $\mathbb { R } ^ { 3 }$

(b) Moreover, show that $[ f * g ] ( x ) \to 0 { \mathrm { ~ a s ~ } } | x | \to \infty$

Problem 4. Let $f \in C ^ { \infty } ( [ 0 , \infty ) \times [ 0 , 1 \} )$ such that

$$
\int _ { 0 } ^ { \infty } \int _ { 0 } ^ { 1 } { \big | } \partial _ { t } f ( t , x ) { \big | } ^ { 2 } ( 1 + t ^ { 2 } ) d x d t < \infty .
$$

Prove that there exists a function $g \in L ^ { 2 } ( [ 0 , 1 ] )$ such that $f ^ { \prime } ( t , \cdot )$ converges to $g ( \cdot )$ in $L ^ { 2 } ( [ 0 , 1 ] )$ as $t \to \infty$

Problem 5. For a function $f : \mathbb { R } \to$ R belonging to $L ^ { 1 } ( \mathbb { R } )$ , we define the Hardy-Littlewood maximal function as follows:

$$
( M f ) ( x ) : = \operatorname* { s u p } _ { h > 0 } { \frac { 1 } { 2 h } } \int _ { x - h } ^ { x + h } | f ( y ) | d y .
$$

Prove that it has the following property: There is a constant A such that for any $\lambda > 0$ p

$$
| \{ x \in \mathbb { R } : ( M f ) ( x ) > \lambda \} | \leq { \frac { A } { \lambda } } \| f \| _ { L ^ { 1 } }
$$

where $| E |$ denotes the Lebesgue measure of E. If you use a covering lemma, you should prove it.

Problem 6. Let $( X , d )$ be a compact metric space. Let $\mu _ { \pi }$ be a sequence of positive Borel measures on X that converge in the weak-\* topology to a finite positive Borel measure $\mu ,$ that is,

$$
\int _ { X } f d \mu _ { n } \to \int _ { X } f d \mu \qquad { \mathrm { f o r ~ a l l } } \quad f \in C ( X ) .
$$

Here, $C ( X )$ denotes the space of bounded continuous functions on X. Show that

$$
\mu ( K ) \geq \operatorname* { l i m } _ { n  \infty } \operatorname* { s u p } \mu _ { n } ( K ) \qquad { \mathrm { f o r ~ a l l ~ c o m p a c t ~ s e t s } } \quad K \subseteq X .
$$

Problem 7. Compute $\int _ { 0 } ^ { \infty } \frac { \cos { x } } { ( 1 + x ^ { 2 } ) ^ { 2 } }$ dx. Justify all your steps!

Problem 8. Determine the number of solutions to

$$
z - 2 - e ^ { - z } = 0
$$

with z in the right half-plane $H = \{ z \in \mathbb { C } : \mathrm { R e } ( z ) > 0 \}$

Problem 9. Let $\mathbb { D } = \{ z \in \mathbb { C } : | z | < 1 \}$ , and suppose that $f$ is a holomorphic function in the punctured open unit disk $\mathbf { \hat { \mathbb { D } } ^ { * } } = \mathbb { D } \ : \backslash \ : \{ 0 \}$ such that

$$
\int _ { { \bar { \mathbb { D } } } ^ { + } } | f ( z ) | ^ { 2 } d \lambda ( z ) < \infty ,
$$

where integration is with respect to 2-dimensional Lebesgue measure λ. Show that f has a holomorphic extension to the unit disk D.

Problem 10. Let $\Omega \subseteq \mathbb { C }$ be a simply connected domain with $\Omega \neq \mathbb { C }$ , and $j ^ { 2 } \colon \Omega  \Omega$ be a holomorphic mapping. Suppose that there exist points $z _ { 1 } , z _ { 2 } \in \Omega , \ z _ { 1 } \ne z _ { 2 } ,$ with $f ( z _ { 1 } ) = z _ { 1 }$ and $f ^ { * } ( z _ { 2 } ) = z _ { 2 }$ Show that $f$ is the identity on $\Omega , \mathrm { i } . \mathrm { e } , \boldsymbol { \mathscr { f } } ( z ) = z$ for all $z \in \Omega$

Problem 11. Let $f : \mathbb { C } \to \mathbb { C }$ be a holomorphic function with $f ( z ) \neq 0$ for all $z \in \mathbb { C } .$ Define $U = \{ z \in \mathbb { C } : | f ( z ) | < 1 \}$ . Show that all connected components of U are unbounded.

Problem 12. A holomorphic function $f : \mathbb { C } \to \mathbb { C }$ is said $\ddagger 0$ be of exponential type if there are constants $c _ { 1 } , c _ { 2 } > 0$ such that

$$
| f ( z ) | \leq c _ { 1 } e ^ { c _ { 2 } | z | } \quad { \mathrm { f o r ~ a l l ~ } } z \in \mathbb { C } .
$$

Show that $f$ $0 \mathrm { f }$ exponential type if and only if $f ^ { t }$ B $\scriptscriptstyle \mathcal { O } \mathbf { f }$ exponential type.