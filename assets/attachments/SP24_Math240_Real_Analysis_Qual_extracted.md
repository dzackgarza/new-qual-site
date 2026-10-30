## MATH 240 Qualifying Exam

May 14, 2024

Instructions: 3 hours, open book/notes (only Folland or personal lecture notes; no HW or other solutions). You may use without proofs results proved in Folland Chapters 1-8. Present your solutions clearly, with appropriate detail.

1. (25 pts) Let $\{ r _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence with $r _ { n } \in [ 0 , 1 ]$ and define the function

$$
f ( x ) : = \sum _ { r _ { n } < x } { \frac { 1 } { 2 ^ { n } } } .
$$

Show that f is Borel measurable, find all its points of discontinuity, and find $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ( x ) d x . } \end{array}$

2. (40 pts) (a) Let $( X , { \mathcal { M } } , \mu )$ be a measure space and let $f _ { n } , f \in L ^ { 1 } ( \mu ) \ ( n \in \mathbb { N } )$ be nonnegative functions. If $f _ { n } \to f$ almost everywhere and $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \int _ { X } f _ { n } d \mu = \int _ { X } f d \mu . } \end{array}$ , show that $f _ { n } \to f$ in $L ^ { 1 } ( \mu )$

(b) Does the conclusion in (a) continue to hold when we drop the hypothesis that $f _ { n } , f$ are non-negative? Either prove this or find a counter-example.

3. (40 pts) Let $0 ~ < ~ \alpha ~ \leq ~ 1$ and let $\Lambda _ { \alpha } ( [ 0 , 1 ] )$ denote the space of H¨older continuous functions of exponent α on [0, 1]. Specifically, $\Lambda _ { \alpha } ( [ 0 , 1 ] ) = \{ f \in C ( [ 0 , 1 ] ) : \| f \| _ { \Lambda _ { \alpha } } < \infty \}$ where

$$
\| f \| _ { \Lambda _ { \alpha } } = | f ( 0 ) | + \operatorname* { s u p } _ { x \neq y \in [ 0 , 1 ] } { \frac { | f ( x ) - f ( y ) | } { | x - y | ^ { \alpha } } } .
$$

(a) Show that $\Vert \cdot \Vert _ { \Lambda _ { \alpha } }$ is a norm on $\Lambda _ { \alpha } ( [ 0 , 1 ] )$ and that with this norm $\Lambda _ { \alpha } ( [ 0 , 1 ] )$ is a Banach space.

(b) Let $B = \{ f \in \Lambda _ { \alpha } ( [ 0 , 1 ] ) : \| f \| _ { \Lambda _ { \alpha } } \leq 1 \}$ be the closed unit ball in $\Lambda _ { \alpha } ( [ 0 , 1 ] )$ . Show that B is compact with respect to the uniform norm.

4. (35 pts) Let A be a set and $1 < p < \infty$ . Prove that a sequence $f _ { n } \in \ell ^ { p } ( A )$ converges weakly to $f \in \ell ^ { p } ( A )$ if and only if $\left( f _ { n } \right)$ converges to $f$ pointwise and $\operatorname* { s u p } _ { n } \| f _ { n } \| _ { p } < \infty$

5. (25 pts) Let X be a set equipped with the discrete topology, and let $X ^ { * } = X \cup \{ \infty \}$ be the one-point compactification of X. Let $\mu$ be a Radon measure on $X ^ { \ast }$ and define the support of $\mu$ as

$$
\operatorname { s u p p } ( \mu ) = \bigcap \{ N : N \subseteq X ^ { * } { \mathrm { ~ i s ~ c l o s e d ~ a n d ~ } } \mu ( N ^ { c } ) = 0 \} .
$$

Prove that supp(µ) is countable.

6. (35 pts) Let $f \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ be such that $f ( x ) = 0$ for a.e. $x \in \mathbb { R } ^ { n } \setminus A$ , where $m ( A ) < \infty$ Show that, for any measurable $E \subset \mathbb { R } ^ { n }$

$$
\int _ { E } | { \hat { f } } ( \xi ) | ^ { 2 } d \xi \leq m ( A ) m ( E ) \| f \| _ { L ^ { 2 } } ^ { 2 } .
$$