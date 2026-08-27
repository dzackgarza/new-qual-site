# SPRING 2008 PRELIMINARY EXAMINATION

1A. Prove that it is not possible to find two linear operators A and B on a non-zero finite dimensional complex vector space with $A B - B A = I$ , where I is the identity operator. Give an example of two such operators acting on an infinite dimensional complex vector space.

Solution: $T r ( A B - B A ) = 0 \neq T r ( I )$ . The operators $A = d / d x$ and $B = x$ acting on the ring of polynomials satisfy $A B - B A = I$

## 2A. Evaluate

$$
\int _ { - \infty } ^ { + \infty } { \frac { \cos ( x ) } { 1 + x ^ { 2 } } } d x
$$

Solution. The integral is unaffected if we replace $\cos ( x )$ by $e ^ { i x }$ . By the residue theorem the integral is equal to 2πi times the sum of the residues in the upper half plane (as $e ^ { i x }$ is small there). The only residue is at $x = i$ , where the residue is $1 / 2 i e$ . So the integral is $\pi / 2 e$

3A. Find (without proof) the number of subgroups of each possible order of the symmetric group $S _ { 4 }$ of all permutations of 4 points.

Solution: The order of the subgroup has to divide 24. Check each possible order. There is 1 (trivial) subgroup of order 1 $, 6 \ ( \mathrm { t y p e \ 2 ) \ + 3 \ ( \mathrm { t y p e \ 2 ^ { 2 } ) } }$ of order 2, 4 of order 3 (cyclic), 3 (cyclic) +1 (normal 4-group) +3 (non-normal 4-group) of order 4, 4 of order 6 (fixing a point), 3 of order 8 (Sylow subgroups), 1 of order 12 (alternating group), and 1 of order 24 (whole group).

4A. Find the solution of the differential equation

$$
y ^ { \prime \prime } - 2 y ^ { \prime } + y = e ^ { - x }
$$

satisfying $y ( 0 ) = y ^ { \prime } ( 0 ) = 0$

Solution: $y = e ^ { - x } / 4 + a e ^ { x } + b x e ^ { x }$ is the general solution. $y ( 0 ) = 0$ forces $a = - 1 / 4$ , and $y ^ { \prime } ( 0 ) = 0$ then forces $b = 1 / 2$

5A. Suppose M is an $n \times n$ nilpotent matrix over C. Show the set of matrices $C ( M )$ which commute with M is the ring $\mathbb { C } [ M ]$ if and only if the null space of M has dimension one.

Let $V ~ = ~ \mathbb { C } ^ { n }$ . The ring $\mathbb { C } [ M ]$ is a vector space spanned by $1 , M , \ldots , M ^ { n - 1 }$ , because $M ^ { n - 1 } = 0$ . Put M in Jordan form

$$
M _ { 1 }
$$

$$
M _ { r }
$$

$( M _ { j }$ is an $s _ { j } \ \times \ s _ { j }$ matrix with 0’s on the diagonal and 1’s on the supradiagonal). The dimension of the nullspace of M is r.

Suppose $r \ = \ \mathrm { d i m } ( \mathrm { N u l l } \left( M \right) ) \ = \ 1$ . It follows that there is a vector $v \in V$ such that $v , M v , \ldots , M ^ { n - 1 } v$ is a basis for V . Suppose A commutes with M and $\begin{array} { r } { A v = \sum _ { i = 0 } ^ { n - 1 } a _ { i } ( M ^ { i } v ) } \end{array}$ Claim:

$$
A = \sum _ { i = 0 } ^ { n - 1 } a _ { i } M ^ { i } .
$$

Indeed,

$$
A ( M ^ { j } v ) = M ^ { j } ( A v ) = \sum _ { i = 0 } ^ { n - 1 } a _ { i } ( M ^ { i + j } v ) = ( \sum _ { i = 0 } ^ { n - 1 } a _ { i } M ^ { i } ) ( M ^ { j } v ) ,
$$

and so $A \in \mathbb { C } [ M ]$

On the other hand, the n matrices

$$
\delta _ { i 1 } M _ { 1 } ^ { k _ { 1 } }
$$

$$
\delta _ { i r } M _ { r } ^ { k _ { r } }
$$

where $1 \leq i \leq r$ and $0 \leq k _ { i } < s _ { i }$ are linearly independent and commute with M. It follows that if $C ( M ) = \mathbb { C } [ M ]$ $M ^ { n - 1 } \neq 0$ so $1 = r =$ dim(Null (M )).

6A. Suppose G is a finite group with only one automorphism. Show $| G | \le 2$

Since $h \in G \to g h g ^ { - 1 }$ is an automorphism for $g \in G , G$ must be abelian. Then $h \in G \to h ^ { k }$ is an automorphism for $( k , | G | ) = 1$ Thus $h ^ { k } = h$ for $( k , | G | ) = 1$ . In particular, $h = h ^ { - 1 }$ for $h \in G$ Thus $G = ( \mathbb { Z } / 2 \mathbb { Z } ) ^ { r }$ for some $r \geq 0$ . If $r > 1 , ( x _ { 1 } , x _ { 2 } , \ldots , x _ { r } )  ( x _ { 2 } , x _ { 1 } , \ldots , x _ { r } )$ is a non-trivial automorphism. Thus $r \leq 1$

7A. Find all irreducible polynomials of degree at most 4 over the field with 2 elements.

Solution: Using the sieve of Eratosthenes we find $x , x + 1$ of degree 1. Therefore higher degree irreducible polynomials must have constant term 1 and sum of coefficients 1. This gives the irreducible polynomials $x ^ { 2 } + x + 1 , x ^ { 3 } + x + 1 , x ^ { 3 } + x ^ { 2 } + 1$ in degrees 2 and 3. In degree 4 we also have to eliminate polynomials divisible by $x ^ { 2 } + x + 1$ ; the only extra possibility eliminated by this is $( x ^ { 2 } + { \bar { x } } + 1 ) ^ { 2 } = x ^ { 4 } + x ^ { 2 } + 1$ . So in degree 4 the irreducible polynomials are $x ^ { 4 } + x + 1 , x ^ { 4 } + x ^ { 3 } + 1 , x ^ { 4 } + x ^ { 3 } + x ^ { 2 } + x + 1$

8A. Let $p , \ q$ be distinct prime numbers and let R be a commutative ring with 1 of characteristic pq. Show there are rings S, T of characteristic p, q respectively, such that R is isomorphic to $S { \times } T$

Solution:

p and q are relatively prime, so there are integers m, n such that $1 = m p + n q$

pR and $q R$ are ideals of R. Let $S = R / p R$ and $T = R / q R$ . So in ${ \textit { S p } } = 0 ;$ since R does not have characteristic $q , 1 \notin p R$ (since otherwise $q \in q p R = ( 0 ) )$ ; thus S has characteristic exactly p. Similarly $T$ has characteristic q.

There are onto homomorphisms $f : R  S$ and $g : R  T$ given by $f ( a ) = a + p R$ and $g ( a ) = a + q R$ . So there is a homomorphism $h : R \to S { \times } T$ given by $h ( a ) = < f ( a ) , g ( a ) >$ If a is in the kernel of h then $a \in ( p R \cap q R )$ so $a = 1 a = m p a + n q a \in p q R = ( 0 )$ . Thus h is $1 - 1$

Notice $f ( m p ) = 0 _ { S }$ and $g ( m p ) = g ( 1 - n q ) = 1 _ { T }$ while $f ( n q ) = f ( 1 - m p ) = 1 _ { S }$ and $g ( n q ) = 0 _ { T } .$ . So given $a , b \in R$ let $c = a n q + b m p .$ , then $f ( c ) = f ( a ) 1 _ { S } + f ( b ) 0 _ { S } = f ( a )$ and $g ( c ) = g ( a ) 0 _ { T } + g ( b ) 1 _ { T } = g ( b )$ . So $f ( c ) = < f ( a ) , g ( b ) >$ . Since $f , g$ are onto S, T respectively, we get h is onto $S { \times } T$

9A. For integers $n \geq 1$ , let $S _ { n }$ be the symmetric group on n letters, and let $f ( n ) = \mathrm { t h e }$ maximum order of elements of $S _ { n }$ . Show

lim $\begin{array} { r } { \operatorname* { i n f } _ { n \longrightarrow \infty } \frac { n } { f ( n ) } = 0 . } \end{array}$

Solution:

The product of a k-cycle and a k +1-cycle in $S _ { 2 k + 1 }$ or $S _ { 2 k + 2 }$ has order $k ( k + 1 )$ as the cycles have coprime orders, so for $n = 2 k + 1$ or $n = 2 k + 2 , n / f ( n )$ is at most $( 2 k + 2 ) / k ( k + 1 ) \leq$ $2 / k \leq 4 / ( n - 2 )$ . This tends to 0 as n tends to infinity, so $n / f ( n )$ has limit 0 as n tends to infinity.

1B. For integers $n \geq 1$ , let $P _ { n } =$ the set of degree $\leq n$ polynomials with real coefficients. Show there is $q ( x ) \in P _ { n }$ such that for all $p ( x ) \in P _ { n }$

$$
\int _ { 0 } ^ { 1 } p ( x ) q ( x ) d x = \int _ { 0 } ^ { 1 } \frac { p ( x ) } { x ^ { 2 } + 1 } d x
$$

Solution:

$P _ { n }$ is a vector space over the reals of dimension $n + 1$

For $p ( x ) \in P _ { n }$ let

$$
T ( p ) = \int _ { 0 } ^ { 1 } \frac { p ( x ) } { x ^ { 2 } + 1 } d x
$$

$$
T
$$

For $p , q \in P _ { n }$ let

$$
P _ { n }
$$

$$
P _ { n } ^ { * }
$$

$$
L _ { p } ( q ) = \int _ { 0 } ^ { 1 } p ( x ) q ( x ) d x
$$

. Each $L _ { p }$ is in $P _ { n } ^ { * }$ . The map L is linear from $P _ { n }$ to $P _ { n } ^ { * }$

If p is in the kernel of L then

$$
0 = L _ { p } ( p ) = \int _ { 0 } ^ { 1 } p ( x ) p ( x ) d x
$$

and so $p ( x )$ is 0 on the unit interval; since $p ( x )$ is a polynomial, $p ( x ) = 0$ . Thus L is $1 - 1$ Since $P _ { n }$ and $P _ { n } ^ { * }$ have the same dimension, L is onto.

Hence there is $q \in P _ { n }$ such that $L _ { q } = T$

2B. (a) Let G be a finite commutative group, and let c be the product of all elements of G. Show that $c ^ { 2 } = 1$

(b) Let F be a finite field, and let c be the product of all nonzero elements in $F .$ . Show that $c = - 1$

Solution: (a) Let $Z \subset G$ be the subset of elements $g \in G$ for which $g \neq g ^ { - 1 }$ (equivalently $g ^ { 2 } \neq 1 )$ . Then

$$
\prod _ { g \in Z } g = 1
$$

since for every $g \in Z$ we have $g ^ { - 1 } \in Z$ and $g ^ { - 1 } \neq g$ . Therefore

$$
c = \prod _ { g \in G , g ^ { 2 } = 1 } g
$$

so

$$
c ^ { 2 } = \prod _ { g \in G , g ^ { 2 } = 1 } g ^ { 2 } = 1 .
$$

(b) Consider the finite group $F ^ { * }$ . Then the set of elements $g \in F ^ { * }$ such that $g ^ { 2 } = 1$ is precisely the set $\{ 1 , - 1 \}$ since $X ^ { 2 } - 1 = ( X - 1 ) ( X + 1 )$ . Therefore by the proof of (a) we have $c = - 1$

3B. Let G be a group and $H \subset G$ a subgroup of finite index n. Show that G contains a normal subgroup N such that $N \subset H$ and the index of $N { \mathrm { ~ i s } } \leq n !$

4B. Let p and q be distinct primes. Show that any group G of order $p ^ { 2 } q ^ { 2 }$ is not simple. Solution. Assume to the contrary that G is simple. Let $s _ { q }$ (resp. $s _ { p } )$ denote the number of $q { \mathrm { - S y } }$ low (resp. p-Sylow) subgroups of G. Then $s _ { q }$ divides $\overline { { p ^ { 2 } } }$ so either $s _ { q } = p \ \mathrm { o r } \ s _ { q } = p ^ { 2 }$ Also $s _ { q } \equiv 1$ (mod q). Therefore either q divides $p - 1$ or q divides $p ^ { 2 } - 1 \dot { = } ( p - 1 ) ( \dot { p } + 1 )$ We conclude that q divides one of $p - 1$ and $p + 1$ . Similarly by symmetry we get that p divides either $q - 1 \mathrm { o r } q + 1$ . This implies that either $q = p - 1$ or $q = p + 1$ . This implies that (after possibly interchanging p and q) we have $q = 3$ and $p = 2$ (since both must be prime). Therefore $| G | = 3 6$ . Let S be the set of 3-Sylow subgroups. Then the group $A u t ( S )$ has order either $2 ! = 2$ or $4 ! = 2 4$ . In either case the homomorphism $\rho : G \to A u t ( S )$ given by the conjugation action on S must have nontrivial kernel as $| G | > A u t ( S )$

5B. Let $\zeta = e ^ { 2 \pi i / 5 }$ and let $\alpha = \sqrt [ 5 ] { 2 } \in \mathbb { R }$ . Let E denote the subfield $\mathbb { Q } [ \zeta , \alpha ] \subset \mathbb { C }$ generated by ζ and α.

(a) Show that E is Galois over Q.

(b) What is $[ E : \mathbb { Q } ] ?$

Solution. For (a) note that

$$
X ^ { 5 } - 2 = \prod _ { i = 0 } ^ { 4 } ( X - \zeta ^ { i } \alpha ) ,
$$

which implies that E is the splitting field of $X ^ { 5 } - 2$ over $\mathbb { Q }$

For (b) consider the diagram of fields

<!-- image-->

The irreducible polynomial of $\zeta$ is $X ^ { 4 } + X ^ { 3 } + X ^ { 2 } + X + 1$ so the extension $\mathbb { Q } [ \zeta ]$ has degree 4 over Q. On the other hand, the field extension $\mathbb { Q } [ \alpha ]$ has degree 5 over Q. Since 4 and 5 are relatively prime it follows that $[ E : \mathbb { Q } ] = 2 0$

6B. The function $y ( x )$ defined on $[ 0 , \infty )$ is smooth and satisfies $y ^ { \prime \prime } - y = f ( x )$ in $x > 0$ $y ( 0 ) = 0 , y ^ { \prime } ( 0 ) = 0$ and $y ( x )$ and $y ^ { \prime } ( x )$ tend to 0 as $x  \infty$ Here $f ( x )$ is a continuous function on $[ 0 , \infty )$ which vanishes for $x > 1$ . Find a non-zero function $g ( x )$ (not depending on y or $f )$ such that $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ( x ) g ( x ) d x = 0 } \end{array}$

Solution. Multiply ODE by $e ^ { - x }$ and integrate over $[ 0 , L ]$

$$
\int _ { 0 } ^ { L } e ^ { - x } \ y ^ { \prime \prime } \ d x - \int _ { 0 } ^ { L } e ^ { - x } \ y \ d x = \int _ { 0 } ^ { L } e ^ { - x } \ f ( x ) \ d x .\tag{1}
$$

Do two integrations by parts to the first integral on LHS, and use $y ( 0 ) = 0 , y ^ { \prime } ( 0 ) = 0$ . When the dust settles, (1) becomes

$$
e ^ { - L } ( y ^ { \prime } ( L ) + y ( L ) ) = \int _ { 0 } ^ { L } e ^ { - x } ~ f ( x ) ~ d x .\tag{2}
$$

Now take $L > 1$ . In $x > 1 , y ^ { \prime \prime } - y = 0$ and the solutions which decay to zero as $x \to \infty$ are proportional to $e ^ { - x }$ . Hence in LHS of (2), $y ^ { \prime } ( L ) + y ( L ) = 0$ for $L > 1$ . In RHS we can replace L by 1 since $f ( x ) = 0$ for $x > 1$ , so we find the condition $\begin{array} { r } { \int _ { 0 } ^ { 1 } e ^ { - x } \ f ( x ) \ d x = 0 } \end{array}$

7B. Evaluate $\int _ { - \infty } ^ { \infty } { \frac { d x } { ( 1 + x ^ { 2 } ) ^ { 5 } } } .$

Solution. Lets avoid doing residue of 5th order pole at $z = i$ . First, for $a > 0$

$$
\int _ { - \infty } ^ { \infty } { \frac { d x } { a + x ^ { 2 } } } = a ^ { - { \frac { 1 } { 2 } } } \int _ { - \infty } ^ { \infty } { \frac { d x } { 1 + x ^ { 2 } } } = \pi a ^ { - { \frac { 1 } { 2 } } } .
$$

Differentiate with respect to a:

$$
\int _ { - \infty } ^ { \infty } \frac { d x } { ( a + x ^ { 2 } ) ^ { 2 } } = \frac { 1 } { 2 } \pi \ a ^ { - \frac { 3 } { 2 } } .
$$

Do it again three times:

$$
\int _ { - \infty } ^ { \infty } { \frac { d x } { ( a + x ^ { 2 } ) ^ { 5 } } } = { \frac { 1 } { 2 } } { \frac { 3 } { 2 } } { \frac { 5 } { 2 } } { \frac { 7 } { 2 } } \pi \ a ^ { - { \frac { 9 } { 2 } } } .
$$

Now set $a = 1$

$$
\int _ { - \infty } ^ { \infty } { \frac { d x } { ( 1 + x ^ { 2 } ) ^ { 5 } } } = { \frac { 1 . 3 . 5 . 7 } { 2 ^ { 4 } } } \pi .
$$

8B. Compute the sequence $\{ x _ { n } \} _ { 0 } ^ { \infty }$ of real numbers so that $\begin{array} { r } { x _ { n } = x _ { n - 1 } - \frac { 1 } { 2 } x _ { n - 2 } } \end{array}$ for $n \geq 2$ , and $x _ { 0 } = 1 , x _ { 1 } = 1$ .

Solution. Seek elementary solutions of the difference equation in the form $x _ { n } = r ^ { n }$ . Get $r ^ { 2 } - r + { \textstyle { \frac { 1 } { 2 } } } = 0$ , with solutions $\textstyle r = { \frac { 1 \pm { \sqrt { 1 - 2 } } } { 2 } } = { \frac { 1 \pm i } { 2 } }$ . General solution of difference equation is linear combination of $\left( { \frac { 1 + i } { 2 } } \right) ^ { n }$ and $\left( { \frac { 1 - j } { 2 } } \right) ^ { - n }$ , and the linear combination with $x _ { 0 } = 1 , x _ { 1 } = 1$ is

$$
x _ { n } = \left( \frac { 1 + i } { 2 } \right) ^ { n } + \left( \frac { 1 - i } { 2 } \right) ^ { n } = \left( \frac { 1 } { \sqrt { 2 } } e ^ { i \frac { \pi } { 4 } } \right) ^ { n } + \left( \frac { 1 } { \sqrt { 2 } } e ^ { - i \frac { \pi } { 4 } } \right) ^ { n } = 2 ^ { - \frac { n } { 2 } } \left( e ^ { i \frac { \pi \pi } { 4 } } + e ^ { - i \frac { n \pi } { 4 } } \right) ,
$$

or

$$
\left| x _ { n } = 2 ^ { 1 - { \frac { n } { 2 } } } { \mathrm { ~ a s ~ } } { \frac { n \pi } { 4 } } \right|
$$

Solution. Seek elementary solutions of the difference equation in the form $x _ { n } = r ^ { n }$ . Get $\begin{array} { r } { r ^ { 2 } - r + \frac { 1 } { 2 } = 0 } \end{array}$ , with solutions $\textstyle r = { \frac { 1 \pm { \sqrt { 1 - 2 } } } { 2 } } = { \frac { 1 \pm i } { 2 } }$ . General solution of difference equation is linear combination of $\left( { \textstyle { \frac { 1 + i } { 2 } } } \right) ^ { n }$ and $\left( { \frac { 1 - j } { 2 } } \right) ^ { 2 }$ , and the linear combination with $x _ { 0 } = 1 , x _ { 1 } = 1$ is

$$
x _ { n } = \left( \frac { 1 + i } { 2 } \right) ^ { n } + \left( \frac { 1 - i } { 2 } \right) ^ { n } = \left( \frac { 1 } { \sqrt { 2 } } e ^ { i \frac { \pi } { 4 } } \right) ^ { n } + \left( \frac { 1 } { \sqrt { 2 } } e ^ { - i \frac { \pi } { 4 } } \right) ^ { n } = 2 ^ { - \frac { n } { 2 } } \left( e ^ { i \frac { \pi \pi } { 4 } } + e ^ { - i \frac { n \pi } { 4 } } \right) ,
$$

or

$$
x _ { n } = 2 ^ { 1 - { \frac { n } { 2 } } } { \mathrm { ~ a s ~ } } { \frac { n \pi } { 4 } }
$$

## 9B. Compute

$$
\operatorname * { l i m } _ { x \to 0 } { \frac { d ^ { 4 } } { d x ^ { 4 } } } { \frac { x } { \sin x } } .
$$

Solution: By Taylor’s formula,

$$
\sin x = x - { \frac { x ^ { 3 } } { 6 } } + { \frac { x ^ { 5 } } { 1 2 0 } } + o ( x ^ { 5 } ) .
$$

Therefore

$$
\begin{array} { l } { \displaystyle \frac { x } { \sin x } = \frac { 1 } { 1 - \frac { x ^ { 2 } } { 6 } + \frac { x ^ { 4 } } { 1 2 0 } + o ( x ^ { 4 } ) } } \\ { \displaystyle = 1 + ( \frac { x ^ { 2 } } { 6 } - \frac { x ^ { 4 } } { 1 2 0 } + o ( x ^ { 4 } ) ) + ( \frac { x ^ { 2 } } { 6 } + o ( x ^ { 2 } ) ) ^ { 2 } + o ( x ^ { 4 } ) } \\ { \displaystyle = 1 + \frac { x ^ { 2 } } { 6 } + \left[ \frac { 1 } { 3 6 } - \frac { 1 } { 1 2 0 } \right] x ^ { 4 } + o ( x ^ { 4 } ) . } \end{array}
$$