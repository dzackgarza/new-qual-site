## Problem 1A.

Suppose that X is a compact metric space. If Y is another metric space (possibly noncompact), let $p : X \times Y  Y$ be the map $p ( x , y ) = y$ . Show that if Z is a closed subset of $X \times Y$ then $p ( Z )$ is closed in Y .

## Solution:

Suppose that $\{ y _ { i } \} _ { i = 1 } ^ { \infty }$ is a sequence in $p ( Z )$ which converges to some $y _ { \infty } \in Y$ . For each $i ,$ we can find $x _ { i } \in X$ so that $( x _ { i } , y _ { i } ) \in Z$ . After passing to a subsequence, we can assume that $\scriptstyle \operatorname* { l i m } _ { i \to \infty } x _ { i } = x _ { \infty }$ for some $x _ { \infty } \in X$ . Then $\begin{array} { r } { \operatorname* { l i m } _ { i \to \infty } ( x _ { i } , y _ { i } ) = ( x _ { \infty } , y _ { \infty } ) } \end{array}$ lies in $Z ,$ so $y _ { \infty } \in p ( Z )$ .

## Problem 2A.

Score:

For G a finite group, H a proper subgroup, show that $G \neq \bigcup \{ g H g ^ { - 1 } ; g \in G \}$

## Solution:

G acts on $A = \{ g H g ^ { - 1 } ; g \in G \}$ . For N = the normalizer of $H , A$ has size $\left\lceil N : G \right\rceil$ . Since $H \subseteq N , [ H : G ] \geq [ N : G ]$ . But e is in each group in A, so $| \bigcup A | < [ H : G ] | H \bar { | } = | G |$

## Problem 3A.

Score:

The moments of a function $f$ are the numbers $\textstyle \int _ { 0 } ^ { \infty } x ^ { n } f ( x ) d x$ for $n = 0 , 1 , 2 . . . ^ { }$ . Find the moments of $f ( x ) = \exp ( - x ^ { 1 / 4 } )$ sin $( x ^ { 1 / 4 } )$ . (Hint: complex analysis.)

Solution: Make the change fo variable $x = y ^ { 4 }$ . Then the integrand is the imaginary part of $4 y ^ { 4 n + 3 } e ^ { ( - 1 + i ) y } d y$ Put $z = ( - 1 + i ) y$ and change the contour of integration to the positive real axis using Cauchy’s theorem. The integral becomes the imaginary part of $( ( - 1 + i ) ^ { 4 n + 4 }$ times something real), which is 0 as $( - 1 + i ) ^ { 4 }$ is real. So all moments are zero.

## Problem 4A.

Score:

Find the eigenvalues of the $n \times n$ matrix with entries $a _ { i j }$ , where $a _ { i j }$ is 1 if $i = j + 1 , - 1$ if $i = j - 1$ , and 0 otherwise.

Solution: If λ is an eigenvalue and $( x _ { 1 } , \ldots , x _ { n } )$ an eigenvector, then $\lambda x _ { j } = x _ { j - 1 } - x _ { j + 1 }$ 2 with $x _ { 0 } = x _ { n + 1 } = 0$ . Solutions to the recurrence are of the form $x _ { j } = a _ { 1 } z _ { 1 } ^ { j } + a _ { 2 } z _ { 2 } ^ { j }$ with $z _ { 1 } , z _ { 2 }$ distinct roots of $\lambda = z ^ { - 1 } - z , \mathrm { ~ s o ~ } z _ { 1 } z _ { 2 } = - 1$ The boundary conditions give $a _ { 1 } + a _ { 2 } = 0 .$ $a _ { 1 } z _ { 1 } ^ { n + 1 } + a _ { 2 } z _ { 2 } ^ { n + 1 } = 0 , 5 0 \ z _ { 1 } ^ { n + 1 } = ( - 1 ) ^ { n + 1 } z _ { 1 } ^ { - ( n + 1 ) }$ . Also $z _ { 1 }$ is not ±i otherwise the roots are the same. So the eigenvalues are $2 \cos ( m \pi / ( n + 1 ) ) i$ for $0 < m \le n$

Problem 5A.

Score:

Find the solution of the differential equation

$$
x ^ { 2 } { \frac { d ^ { 2 } y } { d x ^ { 2 } } } + x { \frac { d y } { d x } } + y = 0
$$

in $x > 0$ , such that $y ( 1 ) = 0$ and $\begin{array} { r } { { \frac { d y } { d x } } = 1 } \end{array}$ at $x = 1$

Solution: The equation is homogeneous, so try $y = x ^ { \lambda }$ . This is a solution if $\lambda ^ { 2 } + 1 = 0$ s o $\lambda = \pm i$ . So real solutioins are given by sin log x and cos log x. The solution satisfying the initial conditions is y = sin log x.

## Problem 6A.

Score:

A positive integer m is called a pseudoprime to the base 2 if m divides $2 ^ { m - 1 } - 1$ . Show $2 ^ { p } - 1$ is a pseudoprime to the base 2 if $p$ is prime.

Solution: Since p is prime p divides $2 ^ { p } - 2$ . Say $2 ^ { p } - 2 = p k$

$$
2 ^ { 2 ^ { p } - 2 } - 1 = 2 ^ { p k } - 1
$$

and

$$
2 ^ { p k } - 1 = ( 2 ^ { p } - 1 ) ( 2 ^ { p ( k - 1 ) } + 2 ^ { p ( k - 2 ) } + \cdot \cdot \cdot + 1 )
$$

## Problem 7A.

Score:

Show that the unit circle is a natural boundary of the function $\begin{array} { r } { f ( z ) = \sum _ { n > 0 } z ^ { 2 ^ { n } } } \end{array}$ ; in other words, $f ( z )$ cannot be extended to an analytic function on any connected open set strictly larger than the open unit disk. (Hint: find a relation between $f ( z )$ and $f ( z ^ { 2 } ) . )$

Solution: We have $f ( z ) = 1 + f ( z ^ { 2 } )$ . This means that if f is unbounded near z then it is unbounded near $\sqrt { z }$ . As it is unbounded near 1, it is unbounded near all values $e ^ { 2 \pi i m / 2 ^ { n } }$

that can be obtained by repeatedly taking a square root of 1. These are dense in the unit circle, so $f$ cannot be holomorphic in any open set containing a point of the unit circle.

## Problem 8A.

Score:

Suppose L is a linear operator acting on a non trivial vector space V over a field K. Suppose $P ( x ) \in K [ x ]$ is not identically zero and $P ( L ) = 0$ . Show every eigenvalue of L is a root of P . Show that if P factors completely over K then some roots of P are eigenvalues of L.

Solution:

Suppose $\begin{array} { r } { P ( x ) = \sum _ { i = 0 } ^ { n } a _ { i } x ^ { i } , a _ { n } \ne 0 . } \end{array}$

Then if $L v = \lambda v ,$

$$
P ( L ) v = \sum _ { i = 0 } ^ { n } a _ { i } L ^ { i } v = \sum _ { i = 0 } ^ { n } a _ { i } \lambda ^ { i } v = P ( \lambda ) v
$$

so if $v \neq 0 , P ( \lambda ) = 0$

Now suppose $\begin{array} { r } { P ( x ) = { a } _ { n } \prod _ { j = 1 } ^ { n } ( x - \lambda _ { j } ) , v _ { \neq 0 } \in V , \prod _ { j = 1 } ^ { k } ( L - \lambda _ { j } ) v \neq 0 \mathrm { a n d } \prod _ { j = 1 } ^ { k + 1 } ( L - \lambda _ { j } ) v = 0 . } \end{array}$ Then $\lambda _ { k + 1 }$ is an eigenvalue.

## Problem 9A.

Score:

Suppose the power series $\sum _ { n } a _ { n } x ^ { n }$ converges for all real $x ,$ and the smooth real valued function $f$ has the property that

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { f ( x ) - \sum _ { j = 0 } ^ { n } a _ { j } x ^ { j } } { x ^ { n } } } = 0
$$

for all n. Prove or give a counterexample to the claim that $\textstyle f ( x ) = \sum _ { n } a _ { n } x ^ { n }$

Solution: False: take any function $h ( x )$ whose Taylor series at 0 is 0 but that is not identically zero, such as $h ( x ) = e ^ { - 1 / x ^ { 2 } }$ (and $h ( 0 ) = 0 )$ . Then $\textstyle \sum _ { n } a _ { n } x ^ { n } + h ( x )$ is a counterexample.

## Problem 1B.

Score:

Find the Fourier series of the function with period 2π that is 1 if $| x | < \epsilon$ and 0 if $\epsilon \le | x | < \pi$ Find the sum

$$
{ \frac { \sin 1 } { 1 } } + { \frac { \sin 2 } { 2 } } + { \frac { \sin 3 } { 3 } } + \cdots
$$

Solution: The Fourier series is given by $\begin{array} { r } { \frac { \epsilon } { \pi } + \sum _ { n \ne 0 } \frac { \sin n \epsilon } { \pi n } e ^ { i n x } } \end{array}$ The sum can be found by putting $\epsilon = 1 , x = 0$ and is given by $( \pi - 1 ) / 2$

Problem 2B.

Score:

Let G be the group $( Z / 2 0 1 2 Z ) ^ { * }$ (this is the group whose elements are classes a (mod 2012) with gcd $( a , 2 0 1 2 ) = 1$ , and whose group operation is multiplication modulo 2012).

Determine the structure of G as an abstract abelian group. When doing so, break it down into as many (nontrivial) pieces as possible.

Note that 2012 has prime factorization $2 ^ { 2 }$ · 503, and that 502 has prime factorization $2 \cdot 2 5 1$

## Solution:

By the Chinese Remainder Theorem,

$$
( Z / 2 0 1 2 Z ) ^ { \ast } \cong ( Z / 4 Z ) ^ { \ast } \times ( Z / 5 0 3 Z ) ^ { \ast } ~ .
$$

Now $( Z / 4 Z ) ^ { * } \cong Z / 2 Z$ because it has two elements, and $( Z / 5 0 3 Z ) ^ { * } \cong Z / 5 0 2 Z$ because the group of nonzero elements of a finite field is cyclic. Therefore

$$
( Z / 2 0 1 2 Z ) ^ { \ast } \cong ( Z / 2 Z ) \times ( Z / 5 0 2 Z ) \cong ( Z / 2 Z ) ^ { 2 } \times ( Z / 2 5 1 Z ) .
$$

Problem 3B.

Score:

Compute

$$
\int _ { C } { \frac { z ^ { 4 } } { z ^ { 5 } - z - 1 } } d z ,
$$

where C is a circle of radius 2 around the origin.

Solution: It is enough to compute the residue at infinity, which is −1, so the answer is 2πi.

## Problem 4B.

Score:

How many conjugacy classes of nilpotent 5 by 5 complex matrices are there (up to conjugacy by invertible matrices)?

Solution: Consider the matrix in Jordan normal form. A nilpotent $n \times n$ matrix has Jordan normal form given by nilpotent Jordan blocks down the diagonal. There is one such block for each positive integer, so the number of conjuagacy classes is the number of partitions of n into a sum of positive integers. For $n = 5$ there are 7 partitions $5 = 4 + 1 = 3 + 2 =$ $3 + 1 + 1 = 2 + 2 + 1 = 2 + 1 + 1 + 1 = 1 + 1 + 1 + 1$ so there are 7 conjugacy classes of nilpotent matrices.

## Problem 5B.

Score:

Let $f : \mathcal { R }  \mathcal { R }$ be an increasing function from the reals to the reals. Show that there is an x such that f is continuous at x.

## Solution:

Let $D = \{ x ; f$ is discontinuous at x}.For each $x \in D$ , there is an non-empty open interval $I _ { x }$ disjoint from the image of f such that $f ( x )$ is an end point of $I _ { x } .$ . So the $I _ { x }$ are pairwise disjoint. Let $r _ { x }$ be a rational in $I _ { x }$ . So D can be mapped 1-1 to the rationals. Hence D is countable.

## Problem 6B.

Score:

Suppose $f ( x ) \in Q [ x ]$ is a polynomial with rational coefficient, n is a positive integer, $n f ( x ) \in$ $Z [ x ]$ has integer coefficients and $f ( m )$ is an integer for all integers m, $0 \leq m < n$ . Show $f ( m )$ is an integer for all integers m.

Solution:

Write $f ( x ) = g ( x ) / n$ , where $g ( x ) \in Z [ x ]$ . Suppose m is an integer. There exist integers $0 \leq i <$ < m and q so that $m = i + q n$ . As

$$
( m ) ^ { k } = i ^ { k } + k ( q n ) i ^ { k - 1 } + { \binom { k } { 2 } } ( q n ) ^ { 2 } i ^ { k - 2 } + \cdot \cdot \cdot + ( q n ) ^ { k }
$$

$g ( m ) - g ( i )$ is divisible by n.Thus

$$
f ( m ) = f ( i ) + \frac { g ( m ) - g ( i ) } { n }
$$

is an integer.

## Problem 7B.

Score:

Let $f , g : { \mathcal { C } } \to { \mathcal { C } }$ be entire functions. Write < for the real part of a complex number. Assume $\Re ( f ( z ) ) \geq \Re ( g ( z ) )$ for all z such that $| z | = 1$ . Show $\Re ( f ( z ) ) \geq \Re ( g ( z ) )$ for all z such that $| z | < 1$

Solution: Let $h ( z ) = ( e ^ { g ( z ) } ) / ( e ^ { f ( z ) } )$ . So $| h ( z ) | \leq 1 { \mathrm { ~ f o r ~ } } | z | = 1$ . By the maximum modulus theorem, $| h ( z ) | \leq 1 \ \mathrm { f o r } \ | z | < 1$

## Problem 8B.

Score:

Suppose that V is a finite-dimensional vector space over a field F , and $P , Q$ are commuting diagonalizable linear maps from V to V . Show $P Q$ is diagonalizable.

Solution: Let $\lambda _ { 1 } , . . . , \lambda _ { r }$ be the eigenvalues of Q. Let $W _ { i } = \{ w ; Q w = \lambda _ { i } w \}$

For $w \in W _ { i } , Q P w = P Q w = P \lambda _ { i } w = \lambda _ { i } P w ;$ so $P$ maps $W _ { i }$ to $W _ { i }$

But $P | W _ { i }$ is diagonalizable, since $W _ { i }$ is a direct sum of minimal P invariant spaces and each must be of dimension 1 since P is diagonalizable. So there is a basis of V consisting of simultaneous eigenvectors for P and $Q$

## Problem 9B.

Score:

Show that there are infinitely many integer solutions of $x ^ { 2 } - 2 y ^ { 2 } = 7$

Solution: $x + { \sqrt { 2 } } y = \pm ( 3 + { \sqrt { 2 } } ) ( 1 + { \sqrt { 2 } } ) ^ { 2 n }$