1A. Consider a sequence of functions $f _ { n } \colon [ a , b ] \to \mathbb { R }$ with the property that for each $x \in [ a , b ]$ there is an open interval $I _ { x }$ containing x such that $( f _ { n } ) _ { n \geq 1 }$ converges uniformly in $I _ { x } \cap [ a , b ]$ Show that $( f _ { n } ) _ { n \geq 1 }$ converges uniformly in $[ a , b ]$

Solution: For each $x \in [ a , b ]$ , the sequence $\left( f _ { n } \right)$ converges uniformly on $I _ { x }$ , and in particular converges pointwise at x. Let $f \colon [ a , b ]  \mathbb { R }$ be the pointwise limit of $\left( f _ { n } \right)$ . The compact set $[ a , b ]$ is covered by the collection of open intervals $I _ { x } ,$ , so there is a finite subcovering, say ${ \bar { [ } } a , b { \bar { ] } } \subset \bigcup _ { k = 1 } ^ { m } I _ { x _ { k } }$ . Given $\epsilon > 0$ , there exists $N _ { k }$ such that for $n \geq N _ { k }$ , the difference $\vert f _ { n } - f \vert$ is bounded by  on $I _ { x _ { k } }$ . Let $N : = \operatorname* { m a x } ( N _ { 1 } , \dots , N _ { m } )$ . Then for $n \geq N$ , the difference $\vert f _ { n } - f \vert$ is bounded by  on all of $[ a , b ]$ . Hence by definition, $\left( f _ { n } \right)$ converges to $f$ uniformly.

2A. Find a countable abelian group whose endomorphism ring has the same cardinality as the set of real numbers. Justify your answer.

Solution: Let G be a vector space of dimension $\aleph _ { 0 }$ over $\mathbb { F } _ { 2 }$ . Then G is countable, since it is a countable union of finite subspaces. Let $v _ { 1 } , v _ { 2 } , . . .$ . be a basis. For each $S \subseteq \{ 1 , 2 , 3 , \dots \}$ there is an endomorphism of $G$ mapping each $v _ { i }$ to $v _ { i }$ or 0 according to whether $i \in S$ Different subsets S give different endomorphisms, so # End $G \geq 2 ^ { \aleph _ { 0 } }$ . On the other hand,

$$
\# \operatorname { E n d } G \leq ( \# G ) ^ { \# G } = \aleph _ { 0 } ^ { \aleph _ { 0 } } \leq ( 2 ^ { \aleph _ { 0 } } ) ^ { \aleph _ { 0 } } = 2 ^ { \aleph _ { 0 } \aleph _ { 0 } } = 2 ^ { \aleph _ { 0 } } .
$$

Thus $\#$ End $G = 2 ^ { \aleph _ { 0 } } = \# \mathbb { R }$

3A. Let $a _ { 1 } , \ldots , a _ { n } , b _ { 1 } , \ldots , b _ { m }$ be distinct complex numbers, let $r _ { 1 } , \ldots , r _ { n }$ be nonnegative integers, and let $c _ { 1 } , \ldots , c _ { m }$ be complex numbers. Prove that if $m \leq r _ { 1 } + \cdot \cdot \cdot + r _ { n } + 1$ , then there exists a rational function $F ( z ) \in \mathbb { C } ( z )$ satisfying all of the following:

1. $F ( z )$ is holomorphic at ∞ and everywhere in C except possibly at $a _ { 1 } , \ldots , a _ { n }$

2. ${ \mathrm { o r d } } _ { z = a _ { i } } F ( z ) \geq - r _ { i }$

3. $F ( b _ { j } ) = c _ { j } { \mathrm { ~ f o r ~ } } j = 1 , \ldots , m .$

Solution: Write $\begin{array} { r } { F ( z ) = G ( z ) / \prod _ { i = 1 } ^ { n } ( z - a _ { i } ) ^ { r _ { i } } } \end{array}$ , where $G ( z ) \in \mathbb { C } ( z )$ is to be determined. The condition that F be holomorphic on C except for poles of order at most $r _ { i }$ at $a _ { i }$ corresponds to the condition that $G ( z )$ be holomorphic on $\mathbb { C } ,$ , hence a polynomial. The condition that $F ( z )$ be holomorphic at ∞ corresponds to the condition deg $G \leq r _ { 1 } + \cdots + r _ { n }$ . The m conditions $F ( b _ { j } ) = c _ { j }$ correspond to conditions $G ( b _ { j } ) = c _ { j } ^ { \prime }$ where $\begin{array} { r } { c _ { j } ^ { \prime } = c _ { j } \prod _ { i = 1 } ^ { n } ( b _ { j } - a _ { i } ) ^ { r _ { i } } } \end{array}$ . These m conditions can be satisfied by a polynomial of degree $m - 1$ (which is $\leq r _ { 1 } + \cdots + r _ { n } )$ , by the Lagrange interpolation formula. Alternatively,

{ polynomials of degree $\leq m - 1 \}  \mathbb { C } ^ { m }$

$$
G ( z ) \mapsto ( G ( b _ { 1 } ) , \dots , G ( b _ { m } ) )
$$

is a linear map between C-vector spaces of the same finite dimension, and is injective (since a nonzero polynomial of degree $\leq m - 1$ has at most m − 1 zeros), so it is also surjective.

4A. For which positive integers n is it true that every invertible $2 \times 2$ matrix A with real entries can be expressed as the n-th power of another $2 \times 2$ matrix with real entries?

Solution: The answer is the odd positive integers. If n is even, then $\binom { - 1 } { 0 } \binom { 0 } { 1 }$ cannot be the n-th power of another $2 \times 2$ matrix with real entries, because its determinant is not an n-th power of a real number.

Now assume n is odd. Thus every real number is an n-th power of a real number. The question of whether A is an n-th power is not affected by conjugation. Thus if A has distinct real eigenvalues, then without loss of generality we may assume that A is diagonal, in which we take the n-th roots of the diagonal entries to find another diagonal matrix B with $B ^ { n } = A$

If A has equal real eigenvalues, then by conjugation, we may assume

$$
A = \lambda \left( { \begin{array} { l l } { 1 } & { c } \\ { 0 } & { 1 } \end{array} } \right)
$$

where $\lambda \in \mathbb { R } ^ { * }$ and $c \in \mathbb { R }$ . Then $A = B ^ { n }$ where

$$
B = \lambda ^ { 1 / n } \left( \begin{array} { c c } { { 1 } } & { { c / n } } \\ { { 0 } } & { { 1 } } \end{array} \right) .
$$

Finally if the eigenvalues of A are not real, then the minimal polynomial of A is a quadratic polynomial $f ( x )$ with no real roots, so the R-subalgebra $\mathbb { R } [ A ]$ of $M _ { 2 } ( \mathbb { R } )$ generated by A is isomorphic to $\mathbb { R } [ x ] / ( f ( x ) ) \simeq \mathbb { C }$ . Since every element of C has an n-th root, the matrix A has an n-th root in $\mathbb { R } [ A ]$

5A. Suppose $f \colon  { \mathbb { R } } \to  { \mathbb { C } }$ satisfies $f ^ { \prime } ( t ) + 2 i t f ( t ) = e ^ { 2 i t }$ and $f ( 0 ) = 0$ . Compute

$$
\operatorname* { l i m } _ { t \to + \infty } e ^ { i t ^ { 2 } } ( f ( t ) - f ( - t ) ) .
$$

You may assume $\textstyle \int _ { 0 } ^ { \infty } e ^ { - t ^ { 2 } } d t = { \sqrt { \pi } } / 2$

Solution: Multiply the ODE by the integrating factor $e ^ { i t ^ { 2 } }$ , and integrate to get

$$
e ^ { i t ^ { 2 } } f ( t ) = \int _ { 0 } ^ { t } e ^ { i x ^ { 2 } + 2 i x } d x
$$

(The hypothesis $f ( 0 ) = 0$ implies that there is no constant of integration.) Substituting −t for t and subtracting, we get

$$
\begin{array} { l } { { \displaystyle e ^ { i t ^ { 2 } } ( f ( t ) - f ( - t ) ) = \int _ { - t } ^ { t } e ^ { i x ^ { 2 } + 2 i x } d x } \ ~ } \\ { { \displaystyle ~ = e ^ { - i } \int _ { - t } ^ { t } e ^ { i ( x + 1 ) ^ { 2 } } d x } \ ~ } \\ { { \displaystyle ~ = e ^ { - i } \int _ { - t + 1 } ^ { t + 1 } e ^ { i z ^ { 2 } } d z } . } \end{array}
$$

Since $e ^ { i z ^ { 2 } }$ is an even function, the limit as $t \to + \infty$ equals $2 e ^ { - i } I$ , where $\begin{array} { r } { I : = \operatorname* { l i m } _ { R \to + \infty } \int _ { 0 } ^ { R } e ^ { i z ^ { 2 } } d z } \end{array}$ (assuming for now that the latter limit exists). Apply Cauchy’s Theorem to the triangular contour from 0 to R to $R + R i$ and back to 0. The vertical part contributes

$$
\int _ { R } ^ { R + R i } e ^ { i z ^ { 2 } } d z = \int _ { 2 } ^ { R } e ^ { i ( R + t i ) ^ { 2 } } i d t ,
$$

whose absolute value is bounded by

$$
\begin{array} { l } { \displaystyle \int _ { 0 } ^ { R } { \lvert e ^ { i ( R + t i ) ^ { 2 } } \rvert d t } = \int _ { 0 } ^ { R } e ^ { - 2 R t } d t } \\ { \displaystyle \qquad = \frac { 1 } { 2 R } \int _ { 0 } ^ { 2 R ^ { 2 } } e ^ { - u } d u , } \end{array}
$$

which goes to 0 as $R \to \infty$ . Thus

$$
{ \begin{array} { r l r l } & { I = \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { 0 } ^ { R + R i } e ^ { i z ^ { 2 } } d z \qquad } & & { { \mathrm { ( i f ~ t h e ~ l i m i t ~ e x i s t s ) } } } \\ & { = \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { 0 } ^ { R } e ^ { i ( e ^ { i \pi / 4 } t ) ^ { 2 } } e ^ { i \pi / 4 } d t \qquad } & & { { \mathrm { ( i f ~ t h e ~ l i m i t ~ e x i s t s ) } } } \\ & { = e ^ { i \pi / 4 } \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { 0 } ^ { R } e ^ { - t ^ { 2 } } d t \qquad } & & { { \mathrm { ( i f ~ t h e ~ l i m i t ~ e x i s t s ) } } } \\ & { = e ^ { i \pi / 4 } { \frac { \sqrt { \pi } } { 2 } } . } \end{array} }
$$

Thus we now know that all the limits exist, and the answer is 2e $^ { - i } I = e ^ { - i + i \pi / 4 } \sqrt { \pi } .$

6A. For which pairs of integers $( a , b )$ is the quotient ring $\mathbb { Z } [ x ] / ( x ^ { 2 } + a x + b )$ isomorphic (as a ring) to the direct product of rings $\mathbb { Z } \times \mathbb { Z } ?$

Solution: Let $A = \mathbb { Z } [ x ] / ( x ^ { 2 } + a x + b )$ and $B = \mathbb { Z } \times \mathbb { Z }$ . If $x ^ { 2 } + a x + b$ is irreducible in the UFD $\mathbb { Z } [ x ]$ , then $( x ^ { 2 } + a x + b )$ is a prime ideal, so A is a domain. But B is not a domain. Thus we may assume $x ^ { 2 } + a x + b = ( x - c ) ( x - d )$ for some $c , d \in \mathbb { Z }$

Suppose p is a prime integer dividing $c - d .$ Then $A \simeq B$ implies $A / p A \simeq B / p B ;$ ; that is, $\mathbb { F } _ { p } [ x ] / ( x - \bar { c } ) ^ { 2 } \simeq \mathbb { F } _ { p } \times \mathbb { F } _ { p }$ , where $\bar { c } = \bar { d }$ is the image of c in $\mathbb { F } _ { p }$ . The ring on the left has a nonzero element with square 0, namely $x - { \bar { c } }$ , whereas the right hand side has no such element. This contradiction shows that $c - d$ is divisible by no primes, so $c - d = \pm 1$ 1.

Conversely, if $c - d = \pm 1$ , then the sum of the ideals $( x - c )$ and $( x - d )$ in $\mathbb { Z } [ x ]$ is the unit ideal, and their product equals their intersection (since they are generated by non-associate irreducible elements), so the Chinese Remainder Theorem gives

$$
{ \frac { \mathbb { Z } [ x ] } { ( ( x - c ) ( x - d ) ) } } \simeq { \frac { \mathbb { Z } [ x ] } { ( x - c ) } } \times { \frac { \mathbb { Z } [ x ] } { ( x - d ) } } .
$$

Each factor on the right is isomorphic to $\mathbb { Z } ,$ because each polynomial in $\mathbb { Z } [ x ]$ is uniquely expressible as $q ( x ) ( x - c ) + r$ with $q ( x ) \in \mathbb { Z } [ x ]$ and $r \in \mathbb { Z }$ . Thus $c - d = \pm 1$ implies $A \simeq B$ In other words, the answer is the set of $( a , b )$ such that $x ^ { 2 } + a x + b$ has the form $( x -$ $n ) ( x - ( n + 1 ) )$ ; that is,

$$
\{ ( - ( 2 n + 1 ) , n ( n + 1 ) ) : n \in \mathbb { Z } \} .
$$

7A. Evaluate $\int _ { 0 } ^ { \infty } { \frac { \sin { x } } { x } } d x .$

Solution: For $R > 1$ , let $\gamma _ { 1 }$ be the straight line path from $1 / R$ to $R _ { : }$ , let $\gamma _ { 2 }$ be the straight line path from R to $R + R i$ , let $\gamma _ { 3 }$ be the straight line path from $R + R i { \mathrm { ~ t o ~ } } { - R + R i }$ , let $\gamma _ { 4 }$ be the straight line path from $- R + R i$ to $- R ,$ , let $\gamma _ { 5 }$ be the straight line path from $- R$ to

$- 1 / R$ , and let $\gamma _ { 6 }$ be the upper semicircle from $- 1 / R$ to $1 / R$ given by the parameterization $\gamma _ { 6 } ( t ) = e ^ { i t }$ for t running from $\pi$ to 0. Let $\gamma$ be the closed loop formed by concatenating these six paths. Cauchy’s Theorem implies that $\begin{array} { r } { \int _ { \gamma } \frac { e ^ { i z } } { z } d z = 0 } \end{array}$

We have

$$
| \int _ { \gamma _ { 2 } } { \frac { e ^ { i z } } { z } } d z | \leq \int _ { 0 } ^ { R } { \frac { e ^ { - t } } { R } } d t = { \frac { 1 - e ^ { - R } } { R } }  0
$$

as $R \to \infty$ . Similarly $\textstyle \int _ { \gamma _ { 4 } } { \frac { e ^ { i z } } { z } } d z \to 0$ , and

$$
| \int _ { \gamma _ { 3 } } { \frac { e ^ { i z } } { z } } d z | \leq \int _ { - R } ^ { R } { \frac { e ^ { - R } } { R } } d t = 2 e ^ { - R }  0 .
$$

On the other hand, $e ^ { i z } z$ differs from $1 / z \ \mathrm { b y }$ a holomorphic function, and $\gamma _ { 6 }$ is shrinking to a point, so

$$
\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { \gamma _ { 6 } } \frac { e ^ { i z } } { z } d z = \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { \gamma _ { 6 } } \frac { 1 } { z } d z } \\ { = \displaystyle \operatorname* { l i m } _ { R \to \infty } \int _ { \pi } ^ { 0 } \frac { 1 } { ( 1 / R ) e ^ { i t } } ( 1 / R ) i e ^ { i t } d t } \\ { = - \pi i . } \end{array}
$$

Thus

$$
\int _ { \gamma _ { 1 } } { \frac { e ^ { i z } } { z } } d z + \int _ { \gamma _ { 5 } } { \frac { e ^ { i z } } { z } } d z  \pi i
$$

as $R \to \infty$ . Taking imaginary parts and using the fact that $( \sin z ) / z$ is an even function, we find that

$$
2 \int _ { 1 / R } ^ { R } { \frac { \sin z } { z } } d z \to \pi
$$

as $R \to \infty$ . Since $( \sin z ) / z$ is holomorphic, it does not hurt to replace the lower limit $1 / R$ by 0, so $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sin x } { x } } d x = \pi / 2$

8A. Let V and W be finite-dimensional vector spaces over a field k. Let $f \colon V ^ { n } \to W$ be a function such that

(a) For each fixed $i \in \{ 1 , \ldots , n \}$ and fixed $v _ { 1 } , \dots , v _ { i - 1 } , v _ { i + 1 } , \dots , v _ { n } \in V$ , the map

$$
\begin{array} { l } { V \to W } \\ { x \mapsto f ( v _ { 1 } , \dots , v _ { i - 1 } , x , v _ { i + 1 } , \dots , v _ { n } ) } \end{array}
$$

is a k-linear transformation; and

(b) $f ( v _ { 1 } , \ldots , v _ { n } ) = 0$ whenever $v _ { i } = v _ { i + 1 }$ for some $i \in \{ 1 , \ldots , n - 1 \}$

Prove that either dim $V \geq n$ or f is identically zero.

Solution: Fix $i ,$ and $v _ { 1 } , \dots , v _ { i - 1 } , v _ { i + 2 } , \dots , v _ { n } \in V$ , and define $g ( x , y ) = f ( v _ { 1 } , \dots , v _ { i - 1 } , x , y , v _ { i + 2 } , \dots , v _ { n } )$ Then

$$
\begin{array} { l } { 0 = g ( x + y , x + y ) } \\ { \ } \\ { \displaystyle = g ( x + y , x ) + g ( x + y , y ) } \\ { \ } \\ { \displaystyle = g ( x , x ) + g ( y , x ) + g ( x , y ) + g ( y , y ) } \\ { \ } \\ { \displaystyle = g ( y , x ) + g ( x , y ) } \end{array}
$$

so interchanging adjacent arguments changes the sign of the value of $f .$ .

Suppose $v _ { 1 } , \ldots , v _ { n } \in V$ are such that $v _ { i } = v _ { j }$ for some $i < j$ Then we can interchange arguments repeatedly to move $v _ { j }$ to the $i + 1$ position, possibly changing the sign of the value of $f ( v _ { 1 } , \ldots , v _ { n } )$ as we go along. Since at the end the result is zero, we must have had $f ( v _ { 1 } , \ldots , v _ { n } ) = 0$ originally. Thus $f ( v _ { 1 } , \ldots , v _ { n } ) = 0$ whenever $v _ { i } = v _ { j }$ for some $i \neq j$

We now solve the problem. If the conclusion fails, we have dim $V < n$ and there exist $v _ { 1 } , \ldots , v _ { n } \in V$ with $f ( v _ { 1 } , \ldots , v _ { n } ) \neq 0$ Since dim $V \ < \ n$ , the vectors $v _ { 1 } , \ldots , v _ { n }$ must be linearly dependent. Thus for some i, we can write $\begin{array} { r } { v _ { i } = \sum _ { j \neq i } c _ { j } v _ { j } } \end{array}$ for some constants $c _ { j } \in k$ for $j \neq i$ . By linearity of $f$ in the i-th argument,

$$
\begin{array} { l } { f ( v _ { 1 } , \dots , v _ { n } ) = \displaystyle \sum _ { j \neq i } c _ { j } f ( v _ { 1 } , \dots , v _ { i - 1 } , v _ { j } , v _ { i + 1 } , \dots , v _ { n } ) } \\ { = \displaystyle \sum _ { j \neq i } c _ { j } \cdot 0 } \end{array}
$$

by the previous paragraph, since in each term some $v _ { j }$ appears twice as an argument. Thus $f ( v _ { 1 } , \ldots , v _ { n } ) = 0$ , a contradiction.

9A. Let $f \colon  { \mathbb { R } } ^ { n } \to  { \mathbb { R } } ^ { n }$ be a differentiable function, and let L be a nonnegative real number. Prove that the following are equivalent:

(i) For every $x , y \in \mathbb { R } ^ { n }$

$$
( f ( x ) - f ( y ) ) . ( x - y ) \leq L | x - y | ^ { 2 }
$$

(ii) For every $x , v \in \mathbb { R } ^ { n }$

$$
D f ( x ) v . v \leq L | v | ^ { 2 } ,
$$

where $D f ( x )$ is the derivative of f at x, and . denotes the standard inner product of vectors in $\mathbb { R } ^ { n }$

Solution:

(i) =⇒ (ii): Let $x = y + t v$ . Then (i) says

$$
t ( f ( y + t v ) - f ( y ) ) . v \leq L t ^ { 2 } | v | ^ { 2 } .
$$

Divide by $t ^ { 2 }$ and take the limit as $t \longrightarrow 0$ to deduce $D f ( y ) v . v \leq L | v | ^ { 2 }$

(ii) =⇒ (i): Let $\phi ( t ) = f ( y + t ( x - y ) )$ for $t \in \mathbb { R }$ . Then

$$
{ \begin{array} { r l } { f ( x ) - f ( y ) = \phi ( 1 ) - \phi ( 0 ) \qquad } & { } \\ { \qquad = \displaystyle \int _ { 0 } ^ { 1 } \phi ^ { \prime } ( t ) d t } \\ { \qquad = \displaystyle \int _ { 0 } ^ { 1 } D f ( y + t ( x - y ) ) ( x - y ) d t \qquad } & { { \mathrm { ( b y ~ t h e ~ C h a i n ~ R u l e ) } } . } \end{array} }
$$

so

$$
\begin{array} { l l l } { ( f ( x ) - f ( y ) ) . ( x - y ) = \displaystyle \int _ { 0 } ^ { 1 } D f ( y + t ( x - y ) ) ( x - y ) . ( x - y ) d t } \\ { \displaystyle \qquad \leq \displaystyle \int _ { 0 } ^ { 1 } L | x - y | ^ { 2 } d t } \\ { \displaystyle \qquad = L | x - y | ^ { 2 } . } \end{array}\tag{by (ii)}
$$

1B. Let F be a field (of arbitrary characteristic). Suppose g is a nonnegative integer, and polynomials $a ( x ) , b ( x ) \in F [ x ]$ satisfy deg $a ( x ) \leq g$ and deg $b ( x ) = 2 g + 1$ . Prove that the polynomial $y ^ { 2 } + a ( x ) y + b ( x )$ is irreducible over $F ( x )$

Solution: If instead it factors in $F ( x ) [ y ]$ into polynomials of $y { \mathrm { - d e g r e e } } \geq 1$ , then by Gauss’s Lemma, it factors in $F [ x ] [ y ] = F [ x , y ]$ into polynomials of $y \mathrm { - d e g r e e } \geq 1$ . Thus we would have

$$
y ^ { 2 } + a ( x ) y + b ( x ) = ( y + p ( x ) ) ( y + q ( x ) )
$$

for some $p ( x ) , q ( x ) \in F [ x ]$ . Since $p ( x ) q ( x ) = b ( x )$ has odd degree, $p ( x )$ and $q ( x )$ have distinct degrees, so

$$
\deg ( p ( x ) + q ( x ) ) = \operatorname* { m a x } ( \deg p ( x ) , \deg q ( x ) ) \geq ( \deg p ( x ) + \deg q ( x ) ) / 2 = ( 2 g + 1 ) / 2 > g .
$$

This contradictions deg $a ( x ) = g$

2B. Find the maximum possible value of $\vert f ^ { \prime } ( 1 ) \vert$ given that f is holomorphic on an open neighborhood of $\{ z \in \mathbb { C } : | z | \leq 2 \}$ and satisfies $| f ( z ) | \leq 1$ when $| z | = 2$ .

Solution: We will use a fractional linear transformation to change the problem to one where the derivative is evaluated at the center of a disk.

The function $z \mapsto { \frac { 2 } { z } } \left( { \frac { z - 1 } { { \bar { z } } - 1 } } \right)$ on $| z | = 2$ has absolute value 1, and it extends to a fractional linear transformation $\begin{array} { r } { g ( z ) = 2 \left( \frac { z - 1 } { 4 - z } \right) } \end{array}$ Since it also maps $z = 1$ to the interior of the unit disk, it must map the region $| z | \le 2$ bijectively onto the unit disk. We calculate $| g ^ { \prime } ( 1 ) | = 2 / 3$

Now, for any other f mapping the circle $| z | = 2$ into $| z | \leq 1$ , the composition $h : = f \circ g ^ { - 1 }$ is holomorphic on a neighborhood of $| z | \le 1$ , and maps $| z | = 1$ into $| z | \leq 1$ . Taking absolute values in

$$
h ^ { \prime } ( 0 ) = \frac { 1 } { 2 \pi i } \int _ { | z | = 1 } \frac { h ( z ) } { z ^ { 2 } } d z
$$

gives $| h ^ { \prime } ( 0 ) | \ \leq \ 1$ Since $g ^ { - 1 } ( 0 ) = 1$ , the Chain Rule gives $h ^ { \prime } ( 0 ) ~ = ~ f ^ { \prime } ( 1 ) g ^ { \prime } ( 1 ) ^ { - 1 }$ Thus $| f ^ { \prime } ( 1 ) | = | h ^ { \prime } ( 0 ) | | g ^ { \prime } ( 1 ) | \leq | g ^ { \prime } ( 1 ) | = 2 / 3$ . Thus $2 / 3$ is the maximum possible value of $\vert f ^ { \prime } ( 1 ) \vert$ .

3B. Let A be ${ \mathrm { ~ a ~ } } d \times d$ matrix with complex entries. Assume that every eigenvalue of A has absolute value 1. Prove that there exists a constant $c \in \mathbb { R }$ independent of n such that

$$
\| A ^ { n } x \| \leq c n ^ { d - 1 } \| x \|
$$

for all $n \geq 1$ and $\boldsymbol { x } \in \mathbb { C } ^ { d }$ . Here $\| x \| : = ( | x _ { 1 } | ^ { 2 } + \cdot \cdot \cdot + | x _ { d } | ^ { 2 } ) ^ { 1 / 2 }$ for all $( x _ { 1 } , \ldots , x _ { d } ) \in \mathbb { C } ^ { d } .$

Solution: We may use $| x | _ { \infty } : = \operatorname* { m a x } \{ | x _ { 1 } | , \ldots , | x _ { n } | \}$ instead of $\lVert x \rVert$ , since different norms on a finite-dimensional vector space are bounded by positive constants times each other. Then it suffices to show that the entries of $A ^ { n }$ are $O ( n ^ { d - 1 } )$ as $n \to \infty$ . This property is unchanged if we conjugate all the $A ^ { n }$ by a fixed invertible matrix. Thus we may assume that A is in Jordan canonical form. Thus $A = D + N$ where D is diagonal, N is nilpotent, and $D$ and $N$ commute. By the Cayley-Hamilton theorem, $N ^ { d } = 0$ . Thus the binomial theorem gives

$$
A ^ { n } = D ^ { n } + { \binom { n } { 1 } } D ^ { n - 1 } N + { \binom { n } { 2 } } D ^ { n - 2 } N ^ { 2 } + \cdots + { \binom { n } { d - 1 } } D ^ { n - d + 1 } N ^ { d - 1 } .
$$

The diagonal entries of $D$ are the eigenvalues of A, which have absolute value 1, so the entries of $D ^ { m }$ are $O ( 1 )$ for any m. The entries of $N , \dot { N } ^ { 2 } , \dots , N ^ { d - 1 }$ do not depend on n. The binomial coefficients are $O ( n ^ { \dot { d } - 1 } )$ . Thus the entries of $A ^ { n }$ are $O ( n ^ { d - 1 } )$ , as desired.

4B. Let $a _ { 1 } , \ldots , a _ { n }$ be positive real numbers. Let $\Delta$ be the set of points $\mathbf { x } \in \mathbb { R } ^ { n }$ satisfying the conditions

$$
\sum _ { i = 1 } ^ { n } a _ { i } x _ { i } = 1 , \quad x _ { i } > 0 { \mathrm { ~ f o r ~ a l l ~ } } i .
$$

Prove that the function $\scriptstyle \log ( \prod _ { i = 1 } ^ { n } x _ { i } )$ has a unique maximum on $\Delta$ and find the point where it occurs.

Solution: The given function is continuous and approaches −∞ at every point on the boundary of $\Delta$ (since each $x _ { i }$ is bounded above, and at least one of them approaches zero at every point on the boundary). Hence a maximum exists. By Lagrange multipliers, at a maximum we must have d log $\begin{array} { r } { ( \prod _ { i = 1 } ^ { n } x _ { i } ) \ : = \ : \lambda d \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } } \end{array}$ for some $\lambda ,$ or $\textstyle \sum _ { i } d x _ { i } / x _ { i } =$ $\lambda \sum _ { i } a _ { i } d x _ { i }$ . Hence $( x _ { 1 } , \ldots , x _ { n } ) = ( 1 / \lambda ) ( 1 / a _ { 1 } , \ldots , 1 / a _ { n } )$ . Combining this with the equation $\textstyle \sum _ { i } a _ { i } x _ { i } = 1$ shows that $\lambda = n$ and $( x _ { 1 } , \ldots , x _ { n } ) = ( 1 / n ) ( 1 / a _ { 1 } , \ldots , 1 / a _ { n } )$ . This locates the maximum and proves that it is unique.

Alternative solution: The arithmetic-mean–geometric-mean inequality gives

$$
{ \frac { \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } } { n } } \geq \left( \prod _ { i = 1 } ^ { n } ( a _ { i } x _ { i } ) \right) ^ { 1 / n } ,
$$

with equality if and only if $a _ { 1 } x _ { 1 } = \cdots = a _ { n } x _ { n }$ . On $\Delta$ , the left hand side is constant, so we get an upper bound on $\textstyle \prod _ { i = 1 } ^ { n } x _ { i } ,$ attained exactly when $a _ { 1 } x _ { 1 } = \cdots = a _ { n } x _ { n }$ . It follows that there is a unique maximum where $a _ { i } x _ { i } = 1 / n$ for all $i ;$ that is, $x _ { i } = 1 / ( n a _ { i } )$ for all i.

5B. Let $n _ { 1 } , \ldots , n _ { r }$ be integers $\geq 2$ . Prove that there is a finite group G containing elements $g _ { 1 } , \ldots , g _ { r }$ such that $g _ { i }$ has exact order $n _ { i }$ for each $i ,$ and $g _ { i } g _ { j } \neq g _ { j } g _ { i }$ for $i \neq j$

Solution: Let $T _ { 1 } , \ldots , T _ { r }$ be disjoint sets with $\# T _ { i } = n _ { i } - 1$ . Let S be the union of the $T _ { i }$ together with one more element x outside all the $T _ { i }$ . Let G be the set of permutations of S.

Choose $g _ { i } \in G$ such that $g _ { i }$ acts as an $n _ { i } { \mathrm { - } } \mathrm { C y }$ cle on $T _ { i } \cup \{ x \}$ , and acts as the identity on the complement. Then $g _ { i }$ has order $n _ { i }$ . If $i \neq j$ , then $( g _ { i } g _ { j } ) ( x ) = g _ { i } ( g _ { j } ( x ) ) \in g _ { i } ( T _ { j } ) = T _ { j }$ , and similarly $( g _ { j } g _ { i } ) ( x ) \in T _ { i }$ , so $g _ { i } g _ { j } \neq g _ { j } g _ { i }$ .

6B. Let $( u _ { n } ( x , y ) ) _ { n \geq 1 }$ be a sequence of functions that are defined and harmonic for $( x , y )$ in an open neighborhood of the upper half plane $\mathbb { R } \times \mathbb { R } _ { \geq 0 }$ . Suppose that $\begin{array} { r } { \frac { \partial u _ { n } } { \partial y } ( x , 0 ) = \dot { 0 } } \end{array}$ for all $x \in \mathbb { R }$ , and $u _ { n } ( x , 0 )$ converges to 0 as $n \to \infty$ uniformly for $x \in \mathbb { R }$ . Must $u _ { n } ( x , y )  0$ as $n \to \infty$ for every $( x , y ) \in \mathbb { R } \times \mathbb { R } _ { > 0 } ?$

Solution: No. Let $u _ { n } = \cosh ( n y ) \cos ( n x ) / n$ Since $u _ { n }$ is the real part of the holomorphic function $\cos ( n z ) / n$ , it is harmonic on the entire plane. Then $\begin{array} { r } { \frac { \partial u _ { n } } { \partial y } ( x , 0 ) = - \sinh ( 0 ) \cos ( n x ) = } \end{array}$ 0, and $u _ { n } ( x , 0 ) = \cos ( n x ) / n \to 0 { \mathrm { ~ a s ~ } } n \to \infty$ uniformly for $x \in R$ . But $u _ { n } ( 0 , 1 ) = \cosh ( n ) / n$ does not tend to 0 as $n \to \infty$

7B. Let A and B be $n \times n$ matrices with complex entries, such that $A B - B A$ is a linear combination of A and B. Prove that there exists a nonzero vector v that is an eigenvector of both A and B.

Solution: Let $A B - B A = C = \alpha A + \beta B$ . If $\alpha = \beta = 0$ , then A and B commute. By a theorem of linear algebra, commuting complex matrices have a common eigenvector. Otherwise, assume without loss of generality that $\beta \neq 0$ . Then B is a linear combination of A and C, so it suffices to prove that A and C have a common eigenvector. Note that $A C - C A = \beta C$ . Since A has finitely many eigenvalues, it must have one, call it λ, such that $\lambda + \beta$ is not an eigenvalue of A. Let v be a nonzero vector with $A v \ = \ \lambda v$ Then $A C v = C A v + \beta C v = ( \lambda + \beta ) C v , \mathrm { s o } C v = 0$ . Hence v is a common eigenvector of A and C.

8B. For each real number x, compute

$$
\operatorname* { l i m } _ { n \to \infty } n \left( \left( 1 + { \frac { x } { n } } \right) ^ { n } - e ^ { x } \right) .
$$

Solution: We have

$$
\begin{array} { c } { { n \left( \left( 1 + \displaystyle \frac { x } { n } \right) ^ { n } - e ^ { x } \right) = n \left( e ^ { n \log ( 1 + x / n ) } - e ^ { x } \right) } } \\ { { = n e ^ { x } \left( e ^ { n \log ( 1 + x / n ) - x } - 1 \right) . } } \end{array}
$$

Taylor’s Theorem with Remainder gives

$$
\log \left( 1 + { \frac { x } { n } } \right) = { \frac { x } { n } } - { \frac { 1 } { 2 } } \left( { \frac { x ^ { 2 } } { n ^ { 2 } } } \right) + O \left( { \frac { 1 } { n ^ { 3 } } } \right)
$$

where the constant in the big-O depends on x, but not on n. Substituting, we get

$$
n e ^ { x } \left( e ^ { - \frac { x ^ { 2 } } { 2 n } + O \left( \frac { 1 } { n ^ { 2 } } \right) } - 1 \right) .
$$

Since $e ^ { y } = 1 + y + O ( y ^ { 2 } )$ as $y  0$ , this becomes

$$
n e ^ { x } \left( - \frac { x ^ { 2 } } { 2 n } + O \left( \frac { 1 } { n ^ { 2 } } \right) \right) = - \frac { 1 } { 2 } x ^ { 2 } e ^ { x } + O \left( \frac { 1 } { n } \right) ,
$$

so the limit is $- { \textstyle \frac { 1 } { 2 } } x ^ { 2 } e ^ { x }$

9B. Let $S _ { 4 }$ be the group of permutations of {1, 2, 3, 4}. Determine the order of the automorphism group $\mathrm { A u t } ( S _ { 4 } )$ . Justify your answer.

Solution: The center of $S _ { 4 }$ is trivial, so $S _ { 4 }$ acts faithfully on itself by inner automorphisms. We will then have $| \mathrm { A u t } ( S _ { 4 } ) | = | S _ { 4 } | = 2 4 $ , if we can show that every automorphism of $S _ { 4 }$ is inner.

Let $\sigma \in \mathrm { A u t } ( S _ { 4 } )$ The group $S _ { 4 }$ has exactly four subgroups $H _ { 1 } , ~ H _ { 2 } , ~ H _ { 3 } , ~ H _ { 4 }$ of order 3, where $H _ { i }$ contains the identity and the two 3-cycles that fix i. The automorphism σ must permute these subgroups. Since inner automorphisms permute them arbitrarily, we can assume after multiplying $\sigma$ by an inner automorphism that $\sigma$ fixes each $H _ { i }$ . The set of transpositions is characterized as the unique conjugacy class consisting of 6 elements of order $2 ,$ so $\sigma$ stabilizes it. Among the transpositions, each one $\tau = ( i j )$ is characterized by the property that $\tau$ and $H _ { k }$ generate S4 $S _ { 4 }$ if and only if $k \in \{ i , j \}$ . Therefore $\sigma$ fixes every transposition. Since the transpositions generate S4, σ must be the identity.