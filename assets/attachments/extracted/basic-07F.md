# BASIC 2007 FALL

1. Let S be a subset of $\mathbb { R } ^ { n }$ with the distance function $d ( x , y ) = ( ( x _ { 1 } - y _ { 1 } ) ^ { 2 } + \cdot \cdot \cdot +$ $( x _ { n } - y _ { n } ) ^ { 2 } ) ^ { 1 / 2 }$ so that $( S , d \vert _ { S \times S } )$ is a metric space.

a)Given $y \in S ,$ is $E = \{ x \in S : d ( x , y ) \geq r \}$ a closed set in S?

b) Is the set E in part a) contained in the closure of $\{ x \in S : d ( x , y ) > r \}$ in $S ?$

Prove your answers.

2. Let $f : ( a , b ) \to \mathbb { R }$ be continuous and differentiable in $\left( a , b \right) \backslash \left\{ c \right\}$ . If $\lim _ { x \to c } f ^ { \prime } ( x ) = d \in \mathbb { R }$ , show that f is differentiable at $c$ and ${ f ^ { \prime } } ( c ) = d .$

3. Let T be a linear transformation of the vector space V into itself.
   If $T v$ and v are linearly dependent for each $v \in V$ , show that $T$ must be a scalar multiple of the identity.

4. Suppose that $f : \mathbb { R } \to \mathbb { R }$ is twice differentiable and its second derivative, $f ^ { \prime \prime }$ satisfies $| f ^ { \prime \prime } ( x ) | \le B$

a)Prove that

$$
| 2 A f ( 0 ) - \int _ { - A } ^ { A } f ( x ) d x | \le { \frac { A ^ { 3 } } { 3 } } B
$$

b) Use the result of part a) to justify the following estimate:

$$
\Big | \int _ { a } ^ { b } f ( x ) d x - \frac { b - a } { n } \sum _ { k = 1 } ^ { n } f ( a + \frac { 2 k - 1 } { 2 n } ( b - a ) ) \big | \le C n ^ { - 2 } ,
$$

where C is a constant that does not depend on n.

5. a) Show that, given a continuous function, $f : [ 0 , 1 ] \to \mathbb { R } .$ ,which vanishes at $x = 1$ , there is a sequence of polynomials vanishing at $x = 1$ which converges uniformly to f on [0, 1].

b) If f is continuous on [0, 1], and

$$
\int _ { 0 } ^ { 1 } f ( x ) ( x - 1 ) ^ { k } d x = 0 { \mathrm { ~ f o r ~ e a c h ~ } } k = 1 , 2 , . . . ,
$$

show that $f ( x ) \equiv 0 .$

6. Let T be a linear transformation from a finite dimensional vector space V into a finite dimensional vector space W. Compute (with proof)

$$
\mathrm { d i m } \ ( \mathrm { N u l l } \ T ) + \mathrm { d i m } \ ( \mathrm { R a n g e } \ T )
$$

and

$$
\mathrm { d i m } \ ( \mathrm { N u l l } \ T ^ { * } ) + \mathrm { d i m } \ ( \mathrm { R a n g e } \ T )
$$

in terms of the dimensions of V and W. Here $T ^ { * }$ denotes the adjoint of T.

7. Let $A ( x )$ be a function on $\mathbb { R }$ whose values are $n \times n$ matrices.
   Starting from the definition that the derivative $A ^ { \prime } ( x )$ is the matrix you get by differentiating the entries in $A ( x )$ , show that when $A ( x )$ is invertible and differentiable for all $x ,$ $A ^ { - 1 } ( x )$ is differentiable, and

$$
( A ^ { - 1 } ) ^ { \prime } ( x ) = - A ^ { - 1 } ( x ) A ^ { \prime } ( x ) A ^ { - 1 } ( x ) .
$$

8. Suppose $a _ { n } \geq 0$ and $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n } = \infty$ . Does it follow that

$$
\sum _ { n = 1 } ^ { \infty } { \frac { a _ { n } } { 1 + a _ { n } } } = \infty ?
$$

Prove your answer.

9. Suppose $u _ { n } : \mathbb { R } \to \mathbb { R }$ is differentiable and solves

$$
u _ { n } ^ { \prime } ( x ) = F ( u _ { n } ( x ) , x ) ,
$$

where F is continuous and bounded.

a) Suppose $u _ { n } \to u$ uniformly.
Show that u is differentiable and solves

$$
u ^ { \prime } ( x ) = F ( u ( x ) , x ) .
$$

Suppose

$$
u ^ { \prime } ( x ) = F ( u ( x ) , x ) , u ( x _ { 0 } ) = y _ { 0 }
$$

has a unique solution $u : \mathbb { R } \to \mathbb { R }$ and $u _ { n } ( x _ { 0 } )$ converges to yo as $n \to \infty$ . Show that $u _ { n }$ uniformly converges to u.

10. Suppose that $\{ \vec { v } _ { j } \} _ { j = 1 } ^ { n }$ is a basis for the complex vector space $\mathbb { C } ^ { n }$

a) Show that there is a basis $\{ \vec { w } _ { j } \} _ { j = 1 } ^ { n }$ such that $( \vec { w } _ { j } , \vec { v } _ { k } ) = \delta _ { j k }$ . Here $( \cdot , \cdot )$ is the standard inner product, $( { \vec { w } } , { \vec { v } } ) = { \overline { { w } } } _ { 1 } { v _ { 1 } } + { \overline { { w } } } _ { 2 } { v _ { 2 } } + \cdot \cdot \cdot + { \overline { { w } } } _ { n } { v _ { n } } ,$ and $\delta _ { j k } = 1$ when $j = k$ and 0 otherwise.

If the $\vec { v } _ { j } \mathrm { : }$ s are eigenvectors for a linear transformation $_ T$ of $\mathbb { C } ^ { n }$ , show that the $\vec { w } _ { j }$ 's are eigenvectors for $T ^ { * }$ , the adjoint of T with respect to ( ,).

11. Let $f$ be bounded real function on [0,1]. Show that f is Riemann integrable if and only if $f ^ { 3 }$ is Riemann integrable.

12. a) Suppose that $x _ { 0 } < x _ { 1 } < \cdots < x _ { n }$ are points in $[ \mathrm { a } , \mathrm { b } ]$ Define linear functions on $\mathbb P ^ { n }$ , the vector space of polynomials of degree less than or equal $n ,$ by setting

$$
l _ { j } ( p ) = p ( x _ { j } ) \quad j = 0 , \ldots , n
$$

Show that the set $\{ l _ { j } \} _ { j = 0 } ^ { n }$ is linearly independent.

b) Show that there are unique coefficients $c _ { j }$ such that

$$
\int _ { a } ^ { b } p ( x ) d x = \sum _ { j = 0 } ^ { n } c _ { j } l _ { j } ( p )
$$

for all $p \in \mathbb { P } ^ { n }$
