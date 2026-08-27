1A. Show that there is a unique piecewise continuous function $y ( x )$ on R satisfying the two conditions

$$
\begin{array} { l l l } { { y ( x ) = \displaystyle \int _ { 0 } ^ { \infty } e ^ { - 2 s } y ( x - s ) d s ~ } } & { { \qquad } } & { { \mathrm { f o r ~ } x > 0 , \mathrm { a n d ~ } } } \\ { { y ( x ) = e ^ { x } , ~ } } & { { \qquad } } & { { \mathrm { f o r ~ } x \le 0 , } } \end{array}
$$

and find an explicit formula for $y ( x )$ for $x > 0$

Solution: Suppose that $y ( x )$ is a solution. For $x > 0$ , the substitution $s = x - t$ yields

$$
\begin{array} { c } { { y ( x ) = \displaystyle \int _ { - \infty } ^ { x } e ^ { - 2 ( x - t ) } y ( t ) d t } } \\ { { e ^ { 2 x } y ( x ) = \displaystyle \int _ { - \infty } ^ { x } e ^ { 2 t } y ( t ) d t . } } \end{array}\tag{1}
$$

The right hand side is continuous as a function of x, so $e ^ { 2 x } y ( x )$ is continuous on $\mathbb { R } _ { > 0 }$ , and multiplying by $e ^ { - 2 x }$ shows that $y ( x )$ is continuous on $\mathbb { R } _ { > 0 }$ . This in turn implies that the right hand side is differentiable, and the same argument now shows that $y ( x )$ is differentiable on ${ \mathbb R } _ { > 0 }$ . Differentiating both sides for $x > 0$ yields

$$
\begin{array} { c } { { e ^ { 2 x } ( y ^ { \prime } + 2 y ) = e ^ { 2 x } y } } \\ { { y ^ { \prime } + 2 y = y } } \\ { { y ^ { \prime } = - y } } \\ { { y = c e ^ { - x } } } \end{array}
$$

for some $c \in \mathbb { R }$ . Substituting this back into (1) yields, for $x > 0$

$$
\begin{array} { c } { { c e ^ { x } = \displaystyle \int _ { - \infty } ^ { 0 } e ^ { 3 t } d t + \int _ { 0 } ^ { x } c e ^ { t } d t } } \\ { { } } \\ { { c e ^ { x } = \displaystyle \frac { 1 } { 3 } + c ( e ^ { x } - 1 ) } } \\ { { } } \\ { { c = \displaystyle \frac { 1 } { 3 } } } \\ { { } } \\ { { y ( x ) = \displaystyle \frac { 1 } { 3 } e ^ { - x } . } } \end{array}
$$

Thus if there is a solution, it must be

$$
y ( x ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { 3 } } e ^ { - x } } & { { \mathrm { i f ~ } } x > 0 } \\ { e ^ { x } } & { { \mathrm { i f ~ } } x \leq 0 } \end{array} \right. }
$$

Because (1) is equivalent to the integral equation in the original problem, this function indeed satisfies the conditions of the problem.

2A. For $c \in \mathbb { Q }$ , define $R _ { c } : = \mathbb { Q } [ x ] / ( x ^ { 3 } - c x )$ . Let $a , b \in \mathbb { Q }$ . Show that the rings $R _ { a }$ and $R _ { b }$ are isomorphic if and only if there exists a nonzero $r \in \mathbb { Q }$ such that $b = r ^ { 2 } a$

Solution: If $r \neq 0$ and $b = r ^ { 2 } a$ , then the ring automorphism $\mathbb { Q } [ x ]  \mathbb { Q } [ x ]$ sending x to rx maps $x ^ { 3 } - b x$ to $r ^ { 3 } x ^ { 3 } - b r x = r ^ { 3 } ( x ^ { 3 } - a x )$ , so it induces an isomorphism between the quotient rings

$$
{ \cal R } _ { b } = \frac { \mathbb { Q } [ x ] } { ( x ^ { 3 } - b x ) } \simeq \frac { \mathbb { Q } [ x ] } { ( r ^ { 3 } ( x ^ { 3 } - a x ) ) } = \frac { \mathbb { Q } [ x ] } { ( x ^ { 3 } - a x ) } = { \cal R } _ { a } .
$$

Conversely, suppose $R _ { a } \simeq R _ { b }$ . The maximal ideals of $R _ { a }$ correspond bijectively to maximal ideals of $\mathbb { Q } [ x ]$ containing $x ^ { 3 } - a x$ , which in turn correspond bijectively to distinct irreducible factors of $x ^ { 3 } - a x$ . Thus $R _ { a }$ has 1, 3, or 2 maximal ideals according as $a = 0$ , a is a nonzero square, or a is not a square. Since $R _ { b }$ must have the same number of maximal ideals, we immediately deduce that $b = r ^ { 2 } a$ for some r, except possibly in the case where neither a nor b is a square. We now assume we are in this remaining case. The quotient fields of $R _ { a }$ (the quotients of $R _ { a }$ by its two maximal ideals) are $\mathbb { Q }$ and $\mathbb { Q } [ x ] / ( x ^ { 2 } - a ) \simeq \mathbb { Q } [ { \sqrt { a } } ]$ . These must be the same as the quotient fields Q and $\mathbb { Q } [ { \sqrt { b } } ]$ of $R _ { b }$ , in some order. Since b is a square in $\mathbb { Q } [ { \sqrt { b } } ]$ but not in $\mathbb { Q } .$ , it must be a square in $\mathbb { Q } [ { \sqrt { a } } ]$ . Write

$$
( r { \sqrt { a } } + s ) ^ { 2 } = b .
$$

Expanding, we get $2 r s = 0$ . If $r = 0$ , we contradict the assumption that b is not a square. Thus $s = 0$ , and $b = r ^ { 2 } a$

3A. Let $f$ and $g$ be functions that are holomorphic on all of $\mathbb { C } .$ except that g has an essential singularity at the complex number c. Prove that either $f$ is constant, or the composition $f \circ g$ has an essential singularity at c. (Hint: you may assume the Casorati-Weierstrass Theorem, which states that if a function $f$ has an essential singularity at ${ \mathit { c } } ,$ then for any punctured neighborhood N of c on which f is holomorphic, the image $f ( N )$ is dense in C.)

Solution: Suppose that f is not constant. Choose a, $b \in \mathbb { C }$ such that $f ( a ) \neq f ( b )$ . If N is any punctured neighborhood of $c ,$ then $g ( N )$ is dense in C, by the Casorati-Weierstrass Theorem. In particular, the closure of $g ( N )$ contains a and $b ,$ so the closure of $f ( g ( N ) )$ ) contains $f ( a )$ and $f ( b )$ . Since this holds for every N , the limit $\scriptstyle \operatorname* { l i m } _ { z \to c } f ( g ( z ) )$ is not ∞, and does not exist as a complex number either. Thus $f \circ g$ has neither a pole nor a removable singularity at ${ \mathit { c } } ,$ so it has an essential singularity at c.

4A. Let A be an $n \times n$ matrix with complex entries. Prove that A is diagonalizable if and only if the following is true: Whenever f is a polynomial with complex coefficients such that $f ( A )$ is nilpotent, we have $f ( A ) = 0$ . (A matrix A is nilpotent if $A ^ { m } = 0$ for some $m \geq 1 . )$ )

Solution: First suppose that A is diagonalizable. If C is an invertible $n \times n$ matrix, then $f ( C A C ^ { - 1 } ) = C f ( A ) { \bar { C } } ^ { - 1 }$ , so both sides of the “if and only $\mathrm { i f } ^ { \dag }$ are unchanged by conjugation. Thus we may assume A is diagonal. Then $f ( A )$ is diagonal for any $f .$ Hence if $f ( A )$ is nilpotent, then $f ( A ) = 0$

Now suppose, conversely, that A is such that $f ( A ) = 0$ whenever $f ( A )$ is nilpotent. Let $f ( x )$ be the product of $( x - \lambda )$ where λ runs through the distinct eigenvalues of A. Then the characteristic polynomial $c ( x )$ of A divides some power of $f ( x )$ , but $c ( A ) = 0$ (Cayley-Hamilton Theorem), so some power of $f ( A )$ is 0. By hypothesis, $f ( A ) = 0$ . Thus the minimal polynomial of A has distinct zeros, so A is diagonalizable.

5A. Let $( a _ { m } ) _ { m \geq 1 }$ be a sequence of real numbers satisfying $a _ { n + m } \leq a _ { n } + a _ { m }$ . Prove that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n } } { n } } = \operatorname* { i n f } _ { n } { \frac { a _ { n } } { n } }
$$

as an element of $[ - \infty , \infty )$

Solution: If $n = \ell m + r$ for integers $m , \ell \geq 1$ and $r \in [ 0 , m )$ , then $a _ { n } = a _ { \ell m + r } \leq a _ { \ell m } + a _ { r } \leq$ $\ell a _ { m } + a _ { r }$ , and dividing by n yields

$$
\frac { a _ { n } } { n } \leq \frac { \ell m } { n } \frac { a _ { m } } { m } + \frac { a _ { r } } { n } .
$$

After sending $n \to \infty$ (for fixed m, so \` and r vary with n), we obtain

$$
\operatorname* { l i m } \operatorname* { s u p } { \frac { a _ { n } } { n } } \leq { \frac { a _ { m } } { m } } .
$$

This holds for each m, so

$$
\operatorname* { l i m } \operatorname* { s u p } { \frac { a _ { n } } { n } } \leq \operatorname* { i n f } { \frac { a _ { m } } { m } } .
$$

On the other hand,

$$
\operatorname* { l i m } \operatorname* { i n f } { \frac { a _ { n } } { n } } \geq \operatorname* { i n f } { \frac { a _ { m } } { m } }
$$

holds by definition. Thus

$$
\operatorname* { l i m } { \frac { a _ { n } } { n } } = \operatorname* { i n f } { \frac { a _ { m } } { m } } .
$$

6A. Let n be a square-free positive integer $( i . e . , n = 1 \mathrm { o r } n$ is prime or n is a product of distinct primes). Assume that for every product of primes $p q _ { 1 } \cdots q _ { r }$ dividing n, with $r > 0$ , we have $q _ { 1 } \cdots q _ { r } \not \equiv 1$ (mod p). Prove that every group G of order n is abelian.

Solution: Suppose p|n and let P be a Sylow p-subgroup of G. Let N be the normalizer of P . By Sylow’s theorems, the number of Sylow p-subgroups is $[ G : N ] \equiv 1 { \pmod { p } }$ Since N contains P , we have $[ G : N ] = q _ { 1 } \cdot \cdot \cdot q _ { r }$ , where $p q _ { 1 } \cdots q _ { r } | n$ . Our hypothesis implies that $r = 0$ , hence $N = G$ , so P is normal. Now let $n = p _ { 1 } \cdots p _ { k }$ and let $P _ { 1 } , \ldots , P _ { k }$ be the corresponding normal Sylow subgroups. Let $Q _ { i } \subseteq G$ be the product of the $P _ { j } \mathrm { ^ { * } s }$ , omitting $P _ { i }$ Then $Q _ { i }$ is normal and $G / Q _ { i }$ is cyclic of order $p _ { i }$ . Thus we have a surjective homomorphism $\phi _ { i } \colon G \to \mathbb { Z } / p _ { i } \mathbb { Z }$ for each $i ,$ and combining these, we get a homomorphism $\begin{array} { r } { \phi \colon G \to \prod _ { i } \mathbb { Z } / p _ { i } \mathbb { Z } } \end{array}$ Let $K = \ker ( \phi )$ . Since each $\phi _ { i }$ factors through $G / K$ , every $p _ { i }$ divides $| G / K |$ . This implies $K = 0$ . Then φ is an injective homomorphism between two groups of equal order, hence an isomorphism.

7A. Let D be the open unit disk in C, and $f \colon D \to D$ a holomorphic function. Suppose that $f ( - \frac { 1 } { 2 } ) = 0$ and $\begin{array} { r } { f ( 0 ) = \frac { 1 } { 2 } } \end{array}$ . Prove that there is only one possible value for $f ( { \frac { 1 } { 2 } } )$ , and find it.

Solution: We first solve for a linear fractional transformation g of D mapping

$$
g ( - { \frac { 1 } { 2 } } ) = 0 , \qquad g ( 0 ) = { \frac { 1 } { 2 } }
$$

and find that the function

$$
g ( z ) = { \frac { z + { \frac { 1 } { 2 } } } { 1 + { \frac { z } { 2 } } } } = { \frac { 2 z + 1 } { 2 + z } }
$$

satisfies these conditions. Then the composition $h = f \circ g ^ { - 1 }$ satisfies

$$
h \colon D \to D , \qquad h ( 0 ) = 0 , \qquad h ( \frac 1 2 ) = \frac 1 2
$$

By Schwarz’s lemma we must have $| h ( z ) | \leq | z |$ in $D .$ . But equality holds for $\begin{array} { r } { z = \frac { 1 } { 2 } } \end{array}$ 1 , so $h ( z )$ must equal z. Hence $f = g$ , and

$$
f ( { \frac { 1 } { 2 } } ) = { \frac { 4 } { 5 } } .
$$

8A. Let $\langle ~ , ~ \rangle$ be a positive-definite Hermitian inner product on a finite-dimensional complex vector space V . Suppose $T \colon V \to V$ is a C-linear map such that $\langle T v , v \rangle = 0$ for all $v \in V$ Prove that $T = 0$

Solution: For $x , y \in V$ , expanding

$$
\langle T ( x + y ) , ( x + y ) \rangle - \langle T x , x \rangle - \langle T y , y \rangle = 0
$$

yields

$$
\langle T x , y \rangle + \langle T y , x \rangle = 0 .
$$

Substituting ix for x yields

$$
i \langle T x , y \rangle - i \langle T y , x \rangle = 0 .
$$

The previous two equalities imply $\langle T x , y \rangle = 0$ for all $x , y \in V$ . Taking $y = T x$ , we get $\langle T x , T x \rangle = 0$ . Since $\langle ~ , ~ \rangle$ is positive-definite, we get $T x = 0$ . This holds for all $x \in V$ , so $T = 0$

Remark: this proof works even when V is infinite-dimensional.

9A. Let $f \colon [ 0 , 1 ] \to \mathbb { R }$ be a continuous function. Show that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f ( x ) e ^ { i n x ^ { 3 } } d x = 0 .
$$

Solution: We can approximate f uniformly by smooth functions in [0, 1], so it suffices to prove the statement when f is smooth.

Choose M such that $| f ( x ) | < M$ for all $x \in [ 0 , 1 ]$ . Let $\epsilon > 0$ . Then

$$
\left| \int _ { 0 } ^ { \epsilon } f ( x ) e ^ { i n x ^ { 3 } } d x \right| \le \epsilon M
$$

On the remaining interval we integrate by parts:

$$
\begin{array} { r c l } { { \displaystyle \int _ { \epsilon } ^ { 1 } f ( x ) e ^ { i n x ^ { 3 } } d x } } & { { = } } & { { \displaystyle \int _ { \epsilon } ^ { 1 } \frac { f ( x ) } { x ^ { 2 } } x ^ { 2 } e ^ { i n x ^ { 3 } } d x } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { i n } \left( f ( 1 ) e ^ { i n } - \frac { f ( \epsilon ) } { \epsilon ^ { 2 } } e ^ { i n \epsilon ^ { 3 } } - \int _ { \epsilon } ^ { 1 } \frac { d } { d x } \left( \frac { f ( x ) } { x ^ { 2 } } \right) e ^ { i n x ^ { 3 } } d x \right) } } \end{array}
$$

Letting n tend to infinity, we obtain

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { \epsilon } ^ { 1 } f ( x ) e ^ { i n x ^ { 3 } } d x = 0
$$

Adding to this the bound on $[ 0 , \epsilon ]$ , we get

$$
\operatorname* { l i m } _ { n \to \infty } \left| \int _ { 0 } ^ { 1 } f ( x ) e ^ { i n x ^ { 3 } } d x \right| \le \epsilon M
$$

The conclusion follows if we let  tend to 0.

1B. Let $S _ { n }$ be the group of permutations of $\{ 1 , \ldots , n \}$ , and let $A _ { n }$ be the alternating subgroup. Suppose $m \leq n$

(a) Identify $S _ { m }$ with the subgroup of $S _ { n }$ consisting of elements that fix $m + 1 , \ldots , n$ Prove that $A _ { n } \cap S _ { m } = A _ { m }$

(b) Is it true in general that if $f \colon S _ { m } \to S _ { n }$ is an injective homomorphism, then $A _ { n } \bigcap { f ( S _ { m } ) } = f ( A _ { m } ) ?$ Give a proof or a counterexample.

Solution: (a) By definition $A _ { n }$ is the kernel of the unique homomorphism $\operatorname { s g n } _ { n } \colon S _ { n }  \{ \pm 1 \}$ mapping each transposition $\mathrm { t o } - 1$ . Restricting $\operatorname { s g n } _ { n }$ to $S _ { m }$ gives a homomorphism mapping each tranposition in $S _ { m }$ to −1, so this restriction must equal $\mathrm { s g n } _ { m }$ . Thus $A _ { m } = \ker ( \mathrm { s g n } _ { m } ) =$ ker $( \mathrm { s g n } _ { n } ) \cap S _ { m } = A _ { n } \cap S _ { m }$ •

(b) It is false. Take $m \ \geq \ 2$ and $n \ = \ 2 m$ There is an obvious action of $S _ { m } \times S _ { m }$ on $\{ 1 , \ldots , 2 m \}$ in which the first $S _ { m }$ permutes $\{ 1 , \ldots , m \}$ and the second $S _ { m }$ permutes $\{ n + 1 , \ldots , 2 m \}$ . Thus we get an injective homomorphism $\iota \colon S _ { m } \times S _ { m } \to S _ { 2 m }$ Define $f \colon S _ { m } \to S _ { 2 m }$ by $f ( { \boldsymbol { \sigma } } ) = \iota ( { \boldsymbol { \sigma } } , { \boldsymbol { \sigma } } )$ . Then f maps each transposition in $S _ { m }$ to an element of $A _ { 2 m }$ , and the transpositions generate $S _ { m } ,$ so $f ( S _ { m } ) \subseteq A _ { 2 m }$ . Hence $A _ { 2 m } \cap f ( S _ { m } ) = f ( S _ { m } )$ , and this is strictly larger than $f ( A _ { m } )$ , since f is injective.

2B. Let $f \colon  { \mathbb { R } } ^ { 3 } \to  { \mathbb { R } }$ be a continuous function of compact support $( \mathrm { i . e . , ~ } f$ vanishes outside some bounded set).

(a) Show that

$$
u ( x ) : = \int { \frac { f ( y ) } { | x - y | } } d y
$$

converges, where the integral is over all $\boldsymbol { y } \in \mathbb { R } ^ { 3 }$

(b) Show that $\scriptstyle \operatorname* { l i m } _ { | x | \to \infty } u ( x ) | x |$ exists.

Solution:(a) Let M be the maximum value of $| f |$ (this exists, since f is 0 outside some compact set and is continuous). Fix x. Choose R large enough that $f ( y ) = 0 { \mathrm { ~ i f ~ } } | x - y | > R$ Using polar coordinates centered at x, we have

$$
\int { \frac { | f ( y ) | } { | x - y | } } d y \leq \int _ { 0 } ^ { R } { \frac { M } { r } } ( 4 \pi r ^ { 2 } d r ) ,
$$

which converges, so the integral defining $u ( x )$ converges absolutely.

(b) By writing $f ( y ) = \operatorname* { m a x } \{ f ( y ) , 0 \} + \operatorname* { m i n } \{ f ( y ) , 0 \}$ , we may reduce to the case that $f$ is nonnegative everywhere. Let $R _ { 0 } > 0$ be such that $f ( y ) = 0$ for $| y | > R _ { 0 }$ $\operatorname { I f } \left| x \right| \geq n R _ { 0 }$ where n is large, and $| y | \le R _ { 0 }$ , then

$$
{ \frac { | x | } { | x - y | } } \leq { \frac { | x | } { | x | - | y | } } = { \frac { 1 } { 1 - | y | / | x | } } \leq { \frac { 1 } { 1 - 1 / n } } = { \frac { n } { n - 1 } }
$$

$$
{ \frac { | x | } { | x - y | } } \geq { \frac { | x | } { | x | + | y | } } = { \frac { 1 } { 1 + | y | / | x | } } \leq { \frac { 1 } { 1 + 1 / n } } = { \frac { n } { n + 1 } } .
$$

Hence

$$
{ \frac { n } { n + 1 } } \int f d y \leq u ( x ) | x | \leq { \frac { n } { n - 1 } } \int f d y
$$

for large x. Thus lim $| x | {  } \infty u ( x ) | x | = \textstyle \int f d y$

3B. For which positive integers n does there exist an $n \times n$ matrix A with rational entries such that $A ^ { 3 } + \bar { A } + I = 0 ?$

Solution: The polynomial $f ( x ) = x ^ { 3 } + x + 1$ is irreducible over $\mathbb { Q }$ (because it is irreducible modulo 2, or because of the rational root test, for instance). Since all eigenvalues of A are roots of $f ( x )$ , the characteristic polynomial of A divides a power of $f ( x )$ , and hence is equal to a power of $f ( x )$ by irreducibility. Therefore n must be a multiple of 3.

Conversely, if $n = 3$ , we may let $V = \mathbb { Q } [ x ] / ( x ^ { 3 } + x + 1 )$ , and let A be the matrix (with respect to some basis) of the Q-linear transformation $V  V$ given by multiplication by the image of x. And for n any larger multiple of 3, we can take A to be block-diagonal with each $3 \times 3$ diagonal block equal to the solution for $n = 3$

4B. Evaluate $I ( w ) : = \int _ { 0 } ^ { \infty } { \frac { e ^ { i w t } } { \sqrt { t } } }$ dt for every nonzero real number w. You may use the formula $\int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \sqrt { \pi } }$

The substitution $t = u ^ { 2 }$ yields

$$
I ( w ) = 2 \int _ { 0 } ^ { \infty } f ( u ) d u .
$$

where $f ( u ) : = e ^ { i w u ^ { 2 } }$ . Suppose $w > 0$ . For $R > 0$ , let $\gamma _ { 1 }$ be the straight-line path from 0 to R, let $\gamma _ { 2 }$ be the circular arc $R e ^ { i t }$ for $t \in [ 0 , \pi / 4 ]$ , and let $\gamma _ { 3 }$ be the straight-line path from $R e ^ { i \pi / 4 }$ to 0. By Cauchy’s Theorem, $\textstyle \sum _ { j = 1 } ^ { 3 } \int _ { \gamma _ { j } } f ( u ) d u = 0$ . For $u = R e ^ { i t }$ , we have

$$
| f ( u ) | = e ^ { \mathrm { R e } ( i w u ^ { 2 } ) } = e ^ { - w \mathrm { I m } ( u ^ { 2 } ) } = e ^ { - w R ^ { 2 } \sin ( 2 t ) } \le e ^ { - w R ^ { 2 } ( 2 ( 2 t ) / \pi ) } ,
$$

where the last step comes from the inequality sin $x \leq 2 x / \pi$ for $x \in [ 0 , \pi / 2 ]$ (concavity of sin x on this interval). Therefore

$$
\left| \int _ { \gamma _ { 2 } } f ( u ) d u \right| \leq \int _ { 0 } ^ { \infty } e ^ { - w R ^ { 2 } ( 2 ( 2 t ) / \pi ) } d t = \frac { \pi } { 4 w R ^ { 2 } } ,
$$

which goes to 0 as $R \to \infty$ . Hence

$$
\begin{array} { r l } { \iota ( w ) - 2 \displaystyle \operatorname* { l i m } _ { m \to \infty } \int _ { \gamma } \langle w | \hat { \sigma } \rangle \ : d w } \\ { } & { = - 2 \displaystyle \operatorname* { l i m } _ { m \to \infty } \int _ { - \infty } ^ { \infty } \int _ { \gamma } \langle i ( \lambda ) ^ { m } \rangle } \\ { } & { = 2 \displaystyle \int _ { \gamma } \eta _ { \varepsilon } \langle i ( \lambda ) ^ { m } | \hat { \sigma } \rangle \ : d w } \\ { } & { = - 2 \displaystyle \int _ { \gamma } \int _ { \gamma } \langle i ( \lambda ^ { m } ) ^ { m } \rangle \ : \theta \ : \mathrm { d } w } \\ { } & { = - \theta ^ { \mathrm { d i d } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = \theta ^ { \mathrm { d i d } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = \frac { 1 + \frac { 1 } { 2 } } { \sqrt { 2 } } \displaystyle \int _ { - \infty } ^ { \infty } \theta ^ { \mathrm { d i d } } \int _ { \gamma } \theta ^ { \mathrm { d i d } } } \\ { } & { = ( 1 + \lambda ) \displaystyle \frac { 1 } { \sqrt { 2 } } \frac { 1 } { \omega ^ { m } } . } \end{array}
$$

Also, $I ( - w )$ is the complex conjugate of $I ( w )$ . Therefore, for any w $\neq 0$

$$
I ( w ) = ( 1 + i \mathrm { s g n } ( w ) ) \sqrt { \frac { \pi } { 2 | w | } } .
$$

5B. What is the cardinality of the smallest field F of characteristic $7$ such that the equation $x ^ { 1 8 } + x ^ { 1 7 } + \cdot \cdot \cdot + x + 1 = 0$ has a solution $x \in F ?$

Solution: We have the identity

$$
( x - 1 ) ( x ^ { 1 8 } + x ^ { 1 7 } + \cdot \cdot \cdot + x + 1 ) = x ^ { 1 9 } - 1 ,
$$

and the latter has no repeated factors over a field of characteristic $7$ (since $x ^ { 1 9 } - 1$ has no factors in common with its derivative), so the given condition is equivalent to the condition that the multiplicative group $F ^ { * }$ contain a nontrivial element of order dividing 19. Since 19 is prime and $F ^ { * }$ is a finite abelian group, this is equivalent to $1 9 \mid \# F ^ { * }$ . The size of $F$ is $7 ^ { m }$ for some m $\geq 1$ , so the condition becomes $1 9 \ : | \ : ( 7 ^ { m } - 1 )$ . We compute $7 ^ { 2 } \equiv 1 1$ (mod 19) and $7 ^ { 3 } \equiv 1$ (mod 19), so the smallest possible m is $^ { 3 , }$ and the smallest possible field $F$ satisfying the conditions is the field $\mathbb { F } _ { 7 ^ { 3 } }$ of $7 ^ { 3 } = 3 4 3$ elements.

6B. Suppose that $f ( z )$ is holomorphic on all of C except for a pole at $z = 0$ . Prove that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { n } } \sum _ { k = 1 } ^ { n } f \left( { \frac { 1 } { n } } e ^ { 2 \pi i k / n } \right)
$$

exists.

Solution: If f were holomorphic at 0, then each term in the sum would be $f ( 0 ) + O ( 1 / n )$ where the implied constant is independent of k and n, so the average of these f-values would also be $f ( 0 ) + O ( 1 / n )$ , which tends to $f ( 0 )$ as $n \to \infty$

In general, using the Laurent series of f , we may write f as a finite linear combination of functions of the form $z ^ { - m }$ for $m > 0$ plus one function that is holomorphic at 0. By linearity, it remains to prove the statement for $f ( z ) = z ^ { - m }$ . In this case, the sum in the problem is a finite geometric series, and its value is 0 when $n > m$ .

7B. Let $n \geq 1$ , and let $M _ { n } ( \mathbb { R } )$ be the ring of $n \times n$ matrices over the field of real numbers. What is the dimension of the subspace V of $M _ { n } ( \mathbb { R } )$ spanned by the matrices of the form $A B - B A$ where A, $B \in M _ { n } ( \mathbb { R } ) ?$

Solution: Let $E _ { i j }$ be the matrix with 1 in the $( i , j )$ position and zeros elsewhere. Since $A B - B A$ is linear in each of A and $B ,$ the subspace V equals the span of $A B - B A$ where A is some $E _ { i j }$ and B is some $E _ { k \ell }$ . We have

$$
E _ { i j } E _ { k \ell } - E _ { k \ell } E _ { i j } = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { i f ~ } } j \neq k { \mathrm { ~ a n d ~ } } i \neq \ell } \\ { E _ { i \ell } } & { { \mathrm { i f ~ } } j = k { \mathrm { ~ a n d ~ } } i \neq \ell } \\ { - E _ { k j } } & { { \mathrm { i f ~ } } j \neq k { \mathrm { ~ a n d ~ } } i = \ell } \\ { E _ { i i } - E _ { j j } } & { { \mathrm { i f ~ } } j = k { \mathrm { ~ a n d ~ } } i = \ell . } \end{array} \right. }
$$

Varying $i , j , k , \ell ,$ , we find that V is spanned by the set of all $E _ { i j }$ with $i \neq j$ together with the set of $E _ { i i } - E _ { i + 1 , i + 1 }$ for $i = 1 , \ldots , n - 1$ These matrices are clearly independent, so dim $V = ( n ^ { 2 } - n ) + ( n - 1 ) = n ^ { 2 } - 1$ . (A more elegant way to describe V is as the space of trace-zero matrices.)

8B. $\mathrm { ~ A ~ } C ^ { 2 }$ function $y ( x )$ for $0 \leq x \leq 1$ , a positive continuous function $a ( x )$ for $0 \leq x \leq 1$ and a real number λ satisfy

$$
\begin{array} { r } { y ^ { \prime \prime } ( x ) + \lambda a ( x ) y ( x ) = 0 , } \\ { y ( 0 ) = 0 , } \\ { y ^ { \prime } ( 1 ) = 0 . } \end{array}
$$

Suppose that $y ( x )$ is not identically zero. Prove that $\lambda > 0$

Solution: Multiply the ODE by $y ( x )$ and integrate from 0 to 1 to get

$$
\begin{array} { r l r } {  { \lambda \int _ { 0 } ^ { 1 } a y ^ { 2 } d x = - \int _ { 0 } ^ { 1 } y y ^ { \prime \prime } d x } } \\ & { } & \\ & { = - y y ^ { \prime } | _ { 0 } ^ { 1 } + \int _ { 0 } ^ { 1 } y ^ { \prime 2 } d x \quad } & { \mathrm { ( i n t e g r a t i o n ~ b y ~ p a r t s , ~ w i t h ~ } u = y , d v = y ^ { \prime \prime } d x \mathrm { ) } } \\ & { } & \\ & { = \displaystyle \int _ { 0 } ^ { 1 } y ^ { \prime 2 } d x } \\ & { } & \\ & { > 0 , } \end{array}
$$

since if $y ^ { \prime }$ were identically zero on [0, 1], then y would be constant on $[ 0 , 1 ]$ , making y identically zero (since $y ( 0 ) = 0 )$ Since $a ~ > ~ 0$ and y is not identically zero, we also have $\begin{array} { r } { \int _ { 0 } ^ { 1 } a y ^ { 2 } d x > 0 } \end{array}$ . Thus λ is a ratio of positive numbers, so $\lambda > 0$

9B. Prove that every group of order 30 has a cyclic subgroup of order 15.

Solution: Let G be the group. For primes $p | 3 0$ , let $n _ { p }$ be the number of Sylow p-subgroups of G. Then $n _ { p } \equiv 1$ (mod p) and $n _ { p } | 3 0 / p$ In particular $n _ { 3 }$ is 1 or 10, and $n _ { 5 }$ is 1 or 6. There are $( p - 1 ) n _ { p }$ elements of exact order 3 in G. If $n _ { 3 } ~ = ~ 1 0$ and $n _ { 5 } ~ = ~ 6$ , then $( 3 - 1 ) n _ { 3 } + ( 5 - 1 ) n _ { 5 } > \# G$ , so either $n _ { 3 } = 1$ or $n _ { 5 } = 1$ •

Suppose $n _ { 3 } = 1$ Then there is a unique Sylow 3-subgroup $P ,$ , and it is normal. Let g be an element of order 5 in G. Conjugation-by-g restricts to an automorphism of $P$ of order dividing 5, but #Aut $P = \# ( \mathbb { Z } / 3 \mathbb { Z } ) ^ { * } = 2$ , so this automorphism must be trivial. Thus g commutes with every element of P . Hence the group generated by g and $P$ is isomorphic to $\mathbb { Z } / 3 \mathbb { Z } \times \mathbb { Z } / 5 \mathbb { Z } \simeq \mathbb { Z } / 1 5 \mathbb { Z }$ .

If instead $n _ { 5 } = 1$ , the same argument with 3 and 5 reversed works, since 3 does not divide $\# ( \mathbb { Z } / 5 \mathbb { Z } ) ^ { * }$