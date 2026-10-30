Students should solve four real analysis problems (numbered 1–6) and four complex analysis problems (numbered 7–12).

## Problem 1. Let

$$
K _ { t } ( x ) = ( 4 \pi t ) ^ { - 3 / 2 } e ^ { - | x | ^ { 2 } / 4 t } , \quad x \in \mathbf { R } ^ { 3 } , \ t > 0 ,
$$

where $| x |$ is the Euclidean norm of $\boldsymbol { x } \in \mathbf { R } ^ { 3 }$

• Show that the linear map

$$
L ^ { 3 } ( \mathbf { R } ^ { 3 } ) \ni f \mapsto t ^ { 1 / 2 } K _ { t } * f \in L ^ { \infty } ( \mathbf { R } ^ { 3 } )
$$

is bounded, uniformly in $t > 0$ . Here

$$
K _ { t } * f ( x ) = \int _ { \mathbf { R } ^ { 3 } } K _ { t } ( x - y ) f ( y ) d y
$$

is the convolution.

• Prove that $t ^ { 1 / 2 } | | K _ { t } * f | | _ { L ^ { \infty } } \to 0 { \mathrm { ~ a s ~ } } t \to 0 , { \mathrm { ~ f o r ~ } } f \in L ^ { 3 } ( \mathbf { R } ^ { 3 } ) .$

Problem 2. Let $f \in L ^ { 1 } ( \mathbf { R } )$ . Show that the series

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { \sqrt { n } } } f ( x - { \sqrt { n } } )
$$

converges absolutely for almost all $x \in \mathbf { R }$

Problem 3. Let $f \in L _ { \mathrm { l o c } } ^ { 1 } ( \mathbf { R } )$ be real valued and assume that for each integer $n > 0$ we have

$$
f \left( x + { \frac { 1 } { n } } \right) \geq f ( x ) ,
$$

for almost all $x \in \mathbf { R }$ . Show that for each real number $a \geq 0$ we have

$$
f ( x + a ) \geq f ( x ) ,
$$

for almost all $x \in \mathbf { R }$

Problem 4. Let $V _ { 1 }$ be a finite-dimensional subspace of the Banach space $V .$ Show that there exists a continuous projection $P : V  V _ { 1 }$ , i.e., a continuous linear map $P : V  V$ such that $P ^ { 2 } = P$ and the range of P is equal to $V _ { 1 }$

Problem 5. For $f \in C _ { 0 } ^ { \infty } ( \mathbf { R } ^ { 2 } )$ define $u ( x , t )$ by

$$
u ( x , t ) = \int _ { \mathbf { R } ^ { 2 } } e ^ { i x \cdot \xi } \frac { \sin ( t | \xi | ) } { | \xi | } f ( \xi ) d \xi , \quad x \in \mathbf { R } ^ { 2 } , \quad t > 0 .
$$

Show that lim $1 _ { t  \infty } | | u ( \cdot , t ) | | _ { L ^ { 2 } } = \infty$ for a set of f that is dense in $L ^ { 2 } ( \mathbf { R } ^ { 2 } )$

Problem 6. Suppose that $\left\{ \phi _ { n } \right\}$ is an orthonormal system of continuous functions in $L ^ { 2 } ( [ 0 , 1 ] )$ and let S be the closure of the span of $\left\{ \phi _ { n } \right\}$ . If $\operatorname* { s u p } _ { f \in S \setminus \{ 0 \} } { \frac { | | f | | _ { \infty } } { | | f | | _ { 2 } } }$ is finite, prove that S is finite dimensional.

Problem 7. Determine

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { x + z } } d x ,
$$

for $0 < a < 1$ and Re $z > 0$ . Justify all manipulations.

Problem 8. Let $\mathbf { C } _ { + } = \{ z \in \mathbf { C } ; \operatorname { I m } z > 0 \}$ and let $f _ { n } : \mathbf { C } _ { + } \to \mathbf { C } _ { + }$ be a sequence of holomorphic functions. Show that unless $| f _ { n } | \to \infty$ uniformly on compact subsets of $\mathbf { C } _ { + }$ , there exists a subsequence converging uniformly on compact subsets of $\mathbf { C } _ { + }$

Problem 9. Let $f : \mathbf { C }  \mathbf { C }$ be entire and assume that $| f ( z ) | = 1$ when $| z | = 1$ . Show that $f ( z ) = C z ^ { m }$ , for some integer $m \geq 0$ and $C \in \mathbf { C }$ with $| C | = 1$

Problem 10. Does there exist a function $f ( z )$ holomorphic in the disk $| z | < 1$ such that $\begin{array} { r } { \operatorname* { l i m } _ { | z | \to 1 } | f ( z ) | = \infty ? } \end{array}$ Either find one or prove that none exist.

Problem 11. Assume that $f ( z )$ is holomorphic on $| z | < 2$ . Show that

$$
\operatorname* { m a x } _ { | z | = 1 } \left| f ( z ) - { \frac { 1 } { z } } \right| \geq 1 .
$$

Problem 12. 1

• (a) Find a real-valued harmonic function v defined on the disk $| z | < 1$ such that $v ( z ) > 0$ and $\begin{array} { r } { \operatorname* { l i m } _ { z  1 } v ( z ) = \infty } \end{array}$

• (b) Let u be a real-valued harmonic function in the disk $| z | < 1$ such that $u ( z ) \leq$ $M < \infty$ and lim $\operatorname* { s u p } _ { r \to 1 } u ( r e ^ { i \theta } ) \leq 0$ for all $\theta \in ( 0 , 2 \pi )$ . Show that $u ( z ) \leq 0$ . The function in part $\mathrm { ( a ) }$ is useful here.