# ANALYSIS QUAL: FALL 2013

Each problem is worth ten points and at most ten problems will count towards your total score. Indicate on the front page of your paper which ten problems you want to have graded. You must demonstrate adequate knowledge of both complex analysis (Problems 1-6) and real analysis (Problems 7-12).

Problem 1. Let U and V be open and connected sets in the complex plane $\mathbb { C } ,$ and $f : U  \mathbb { C }$ be a holomorphic function with $f ( U ) \subseteq V$ Suppose that $f$ is a proper map from U into $V , \mathrm { i . e . , } \ f ^ { - 1 } ( K ) \subseteq U$ is compact, whenever $K \subseteq V$ is compact. Show that then f is surjective.

Problem 2. Show that there is no function f that is holomorphic near $0 \in \mathbb { C }$ and satisfies

$$
f ( 1 / n ^ { 2 } ) = { \frac { n ^ { 2 } - 1 } { n ^ { 5 } } }
$$

for all large $n \in \mathbb { N } .$

Problem 3. Does there exist a holomorphic function $f \colon \mathbb { D } : = \{ z \in \mathbb { C } : | z | < 1 \} $ C such that

$$
\operatorname* { l i m } _ { n \to \infty } | f ( z _ { n } ) | = + \infty
$$

for all sequences $\{ z _ { n } \}$ in D with $\scriptstyle \operatorname* { l i m } _ { n \to \infty } | z _ { n } | = 1 ?$ Justify your answer!

Problem 4. Let u be a non-negative continuous function on ${ \overline { { \mathbb { D } } } } \setminus \{ 0 \} = \{ z \in \mathbb { C }$ $0 < | z | \leq 1 \}$ that is subharmonic on $\mathbb { D } \backslash \{ 0 \}$ . Suppose that $u | \partial \mathbb { D } \equiv 0$ and

$$
\operatorname* { l i m } _ { \tau \to 0 ^ { + } } \frac { 1 } { r ^ { 2 } \log ( 1 / r ) } \int _ { \{ z \in \mathbb { C } : 0 < | z | < r \} } u ( z ) d \lambda ( z ) = 0 ,
$$

where integration is with respect to Lebesgue measure λ on C. Show that then $u \equiv 0$

Problem 5. Let $\{ f _ { n } \}$ be a sequence of holomorphic functions on D and suppose that

$$
\int _ { \mathbb { D } } \left. f _ { n } ( z ) \right. d \lambda ( z ) \le 1
$$

for all $n \in \mathbb { N } ,$ where dλ denotes integration with respect to Lebesgue measure λ on C. Show that then there exists a subsequence $\{ f _ { n _ { k } } \}$ that converges uniformly on all compact subsets of $\mathfrak { D } .$ .

Problem 6. Let $U \subseteq \mathbb { C }$ be a bounded open set with $0 \in U ,$ and $f : U  \mathbb { C }$ be holomorphic function with $f ( U ) \subseteq U$ and ${ f } ( 0 ) = 0 .$ Show that $| f ^ { \prime } ( 0 ) \} | \leq 1$ . Hint: Consider the iterates $f ^ { n } : = \underline { { f } } \circ \cdots \circ f$ of $f .$

n times

Problem 7. Show that there is a dense set of functions $f \in L ^ { 2 } \langle [ 0 , 1 ] \rangle$ such that $x \mapsto x ^ { - 1 / 2 } f ( x ) \in L ^ { 1 } ( [ 0 , 1 ] )$ and $\textstyle \int _ { 0 } ^ { 1 } x ^ { - 1 / 2 } f ( x ) d x = 0$

Problem 8. Compute the following limits and justify your calculations!

a lim $\cdot \int _ { 0 } ^ { k } x ^ { n } { \biggl ( } 1 - { \frac { x } { k } } { \biggr ) } ^ { k }$ dx, where n  N. k→o0

$$
{ \mathfrak { b } } ) \operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { \infty } \left( 1 + { \frac { x } { k } } \right) ^ { - k } \cos ( x / k ) d x .
$$

Problem 9. Let X be a Banach space, $Y$ be a normed linear space, and $B \colon X \times$ $Y  \mathbb { R }$ be a bilinear function. Suppose that for each ${ \mathfrak { x } } \in X$ there exists a constant $C _ { x } \geq 0$ such that $| B ( x , y ) | \leq C _ { x } \| y \|$ for all $y \in Y$ , and for each $y \in Y$ there exists a constant $C _ { y } \geq 0$ such that $| B ( x , y ) \} \leq C _ { y } \| x \|$ for all $x \in X .$

Show that then there exists a constant $C \geq 0$ such that $| B ( x , y ) | \leq C \| x \| \cdot \| y \|$ for all $x \in X$ and all $y \in Y$ •

Problem 10. a) Let $f \in L ^ { 2 } ( \mathbb { R } )$ and define $\begin{array} { r } { h ( x ) = \int _ { \mathbb { R } } f ( x - y ) f ( y ) } \end{array}$ dy for ${ \mathfrak { x } } \in \mathbb { R }$ Show that then there exists a function $g \in L ^ { 1 } ( \mathbb { R } )$ such

$$
h ( \xi ) = \int _ { \mathbb R } e ^ { - i \xi x } g ( x ) d x
$$

for $\xi \in \mathbb { R } , \mathrm { i . e . , }$ h is the Fourier transform of a function in $L ^ { 1 } ( \mathbb { R } )$

Conversely, show that if $g \in L ^ { 1 } \{ \mathbb { R } \}$ ,then there is a function $f \in L ^ { 2 } ( \mathbb { R } )$ such that the Fourier transform of $g$ is given by $\begin{array} { r } { x \mapsto h ( x ) : = \int _ { \mathbb { R } } f ( \dot { x } - y ) f ( y ) d y } \end{array}$

Problem 11. Consider the space $C ( [ 0 , 1 ] )$ of real-valued continuous functions on the unit interval [0, 1]. We denote by $\| \bar { \boldsymbol { f } } \| _ { \infty } : = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | \boldsymbol { f } ( x ) |$ the supremum norm and by $\begin{array} { r } { \| f \| _ { 2 } : = \left( \int _ { 0 } ^ { 1 } | \dot { f } ( x ) | ^ { 2 } d x \right) ^ { 1 / 2 } } \end{array}$ the $L ^ { 2 }$ -norm of a function $f \in { \cal C } ( [ 0 , 1 ] )$

Let S be a subspace of $C ( [ 0 , 1 ] )$ . Show that if there exists a constant $K \geq 0$ such that $\| f \| _ { \infty } \leq K \| f \| _ { 2 }$ for all $f \in S$ ,then $S$ is finite-dimensional.

Problem 12. Let $f = [ 0 , 1 ] $ R be a continuous function that is absolutely continuous on each interval $\{ \epsilon , \mathfrak { z } \}$ with $0 < \epsilon \leq 1$ •

Show that $f$ is not necessarily absolutely continuous on [0, 1].

b) Show that if f is of bounded variation on [0, 1], then $f$ is absolutely continuous on [0, 1].