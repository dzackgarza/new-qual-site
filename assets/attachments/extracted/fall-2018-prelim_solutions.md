Show that

$$
\int _ { 0 } ^ { 1 } x ^ { - x } \mathrm { d } x = \sum _ { n = 1 } ^ { \infty } n ^ { - n }
$$

## Solution:

Write $x ^ { - x } = \mathrm { e } ^ { - x \log x }$ , Taylor expand the exponential, and integrate term by term.

## Problem 2A.

Score:

Suppose $f : \mathbb { R }  \mathbb { R }$ is differentiable and satisfies $f ^ { \prime } ( x ) > f ( x )$ for all real x. Show that if $f ( 0 ) = 0$ then $f ( x ) > 0$ for all $x > 0$

## Solution:

Since $f ^ { \prime } ( 0 ) > 0$ we have $f ( x ) = x \cdot f ^ { \prime } ( 0 ) + o ( | x | )$ in a neighborhood of zero, so there is a $t > 0$ such that f is positive on $( 0 , t )$ . Assume for contradiction that $f ( x ) \leq 0$ for some $x > 0$ and let $x _ { 0 }$ be the first such x. Then $f ( x ) > 0$ on $( 0 , x _ { 0 } )$ , which means that $f ^ { \prime } ( x ) > 0$ on $( 0 , x _ { 0 } )$ , so $f ( x _ { 0 } ) > f ( 0 ) = 0$ , a contradiction

## Problem 3A.

Score:

Let X be a metric space.

(a) If U is a subset of X show that there is a unique open set $\neg U$ disjoint from U and containing all open sets disjoint from U .

(b) Give an example of an open set U with $U \neq \lnot \lnot U$

(c) Prove that for all open sets $U , \lnot U = \lnot \lnot U$ . (Hint: if $A \subseteq B$ and $B \subseteq A$ then $A = B . )$

Solution: (a) Take $\neg U$ ¬U to be the union of all open sets disjoint from U , which is open as the union of any collection of open sets is open.

(b) Take X to be the real line and U to be the nonzero reals. Then ¬U is empty so $\neg \neg U$ is the real line.

(c) We have $A \subseteq \neg \neg A$ and applying this to $A = \neg U$ we get $\neg U \subseteq \neg \neg \neg U$ . On the other hand, if $A \subseteq B$ then $\neg B \subseteq \neg A$ , and applying this to $A = U , B = \neg \neg U$ we get $\neg \neg \neg U \subseteq \neg U$

## Problem 4A.

Score:

Let a be a real number with $| a | < 1$ . Prove that

$$
\sum _ { k = 1 } ^ { \infty } a ^ { k } \cos ( k \theta ) = { \frac { - a ^ { 2 } + a \cos \theta } { 1 + a ^ { 2 } - 2 a \cos \theta } }
$$

Solution: We use the fact that for any complex number $z = e ^ { i \theta } = \cos \theta + i \sin \theta \in \mathbb { C }$

$$
{ \frac { 1 } { 1 - a z } } = \sum _ { k = 0 } ^ { \infty } a ^ { k } z ^ { k } = \sum _ { k = 0 } ^ { \infty } a ^ { k } e ^ { i k \theta } = 1 + \sum _ { k = 1 } ^ { \infty } a ^ { k } ( \cos ( k \theta ) + i \sin ( k \theta ) ) .
$$

Therefore

$$
\begin{array} { c } { { \displaystyle \sum _ { k = 1 } ^ { \infty } a ^ { k } \cos ( k \theta ) = \Re \left( \displaystyle \frac { 1 } { 1 - a z } - 1 \right) = \Re \left( \displaystyle \frac { a z } { 1 - a z } \right) = \Re \left( \displaystyle \frac { a z ( 1 - a \bar { z } ) } { | 1 - a z | ^ { 2 } } \right) } } \\ { { = \Re \left( \displaystyle \frac { a \bar { z } - a ^ { 2 } } { ( 1 - a \cos \theta ) ^ { 2 } + ( a \sin \theta ) ^ { 2 } } \right) = \displaystyle \frac { a \cos \theta - a ^ { 2 } } { 1 + a ^ { 2 } - 2 a \cos \theta } . } } \end{array}
$$

## Problem 5A.

Score:

Describe a conformal map from the set

$$
\{ | z - 4 i | < 4 \} \cap \{ | z - i | > 1 \}
$$

oto the open unit disk.

Solution: Compose

$$
f _ { 1 } : z \to 1 / z
$$

$$
f _ { 2 } : z \to 8 \pi ( z + i / 2 ) / 3
$$

$$
f _ { 3 } : z \to e x p ( z )
$$

$$
f _ { 4 } : z \to ( z - i ) / ( z + i )
$$

Let A be an $n \times n$ matrix with real entries such that $( A - I ) ^ { m } = 0$ for some $m \geq 1$ . Prove that there exists an $n \times n$ matrix B with real entries such that $B ^ { 2 } = A$

Solution: Write $A = I + N$ , so $N ^ { m } = 0$ . Let $P ( x )$ be the m-th Taylor polynomial of the function $\sqrt { 1 + x }$ , so $P ( x ) ^ { 2 } \equiv 1 + x$ (mod $x ^ { m } )$ . In other words

$$
P ( x ) ^ { 2 } = 1 + x + x ^ { m } Q ( x )
$$

for some $Q ( x ) \in \mathbb { R } [ x ]$ . Then

$$
P ( N ) ^ { 2 } = I + N + N ^ { m } Q ( N ) = I + N = A ,
$$

so $B : = P ( N )$ satisfies $B ^ { 2 } = A$ . S

Problem 7A.

Score:

Suppose $A = \left( a _ { i j } \right)$ is a real symmetric $n \times n$ matrix with nonnegative eigenvalues. Show that

$$
| a _ { i j } | \leq \sqrt { a _ { i i } a _ { j j } }
$$

for all distinct $i , j \le n$

Solution:

Since A is symmetric with nonnegative eigenvalues, we may diagonalize A as $A = U D U ^ { T }$ with positive $D _ { : }$ so $A = B ^ { T } B$ for $\boldsymbol { B } ^ { \bar { T } } = { U D ^ { 1 / 2 } }$ . Thus, A is a Gram matrix, i.e., $a _ { i j } = \langle v _ { i } , v _ { j } \rangle$ where $v _ { i }$ are the columns of $B ,$ so by Cauchy Schwartz $a _ { i j } \leq \| v _ { i } \| \| v _ { j } \| \leq \sqrt { a _ { i i } a _ { j j } }$ , as desired.

## Problem 8A.

Score:

For three non-zero integers a, b and c show that

$$
\operatorname* { g c d } ( a , \operatorname { l c m } ( b , c ) ) = \operatorname { l c m } ( \operatorname* { g c d } ( a , b ) , \operatorname* { g c d } ( a , c ) ) .
$$

where gcd and lcm stand for the greatest common divisor and the least common multiple of two integers, respectively.

Solution: Given a prime $p ,$ let $\alpha , \beta ,$ and $\gamma$ be the exponents of $p$ in the prime factorization of $a , b ,$ and ${ \mathit { c } } ,$ respectively. Then it will suffice to show that

$$
\operatorname* { m i n } \{ \alpha , \operatorname* { m a x } \{ \beta , \gamma \} \} = \operatorname* { m a x } \{ \operatorname* { m i n } \{ \alpha , \beta \} , \operatorname* { m i n } \{ \alpha , \gamma \} \} \ .
$$

Without loss of generality, we may assume that $\beta \leq \gamma ;$ in that case max $\{ \beta , \gamma \} = \gamma$ and min $\{ \alpha , \beta \} \le \operatorname* { m i n } \{ \alpha , \gamma \}$ Therefore the above equation is true because both sides are equal to min $\{ \alpha , \gamma \}$

Problem 9A.

Score:

Suppose a prime number $p$ divides the order of a finite group G. Prove the existence of an element $g \in G$ of order $p .$

Solution: Consider the set $X = \{ ( g _ { 1 } , \dotsc , g _ { p } ) \in G ^ { p } \mid g _ { 1 } \cdot \cdot \cdot g _ { p } = e \}$ . It is acted upon by the cyclic group $\mathbf { Z } / p \mathbf { Z }$ with ${ \bf 1 } \in { \bf Z } / p { \bf Z }$ acting as the cyclic shift

$$
( g _ { 1 } , \dotsc , g _ { p } ) \longmapsto ( g _ { p } , g _ { 1 } , \dotsc , g _ { p - 1 } ) .
$$

A fixed point of this action is a constant p-tuple $( g , \ldots , g )$ such that $g ^ { p } = e$ . The number of fixed points is not zero, since $( e , \ldots , e )$ is a fixed point, and is congruent modulo $p$ to

$$
| X | = | G | ^ { p - 1 } ,
$$

i.e., it is divisible by $p ,$ since $p > 1$ . It follows that there is an element $g \neq e$ with $g ^ { p } = e$

## Problem 1B.

Score:

A mathematician (stupidly) tries to estimate $\textstyle \pi ^ { 2 } / 6 = \sum _ { n = 1 } ^ { \infty } 1 / n ^ { 2 }$ by taking the sum of the first N terms of the series. What is the smallest value of N such that the error of this approximation is at most $1 0 ^ { - 6 } ?$ Hint: integral test.

## Solution:

The integral test shows that $\begin{array} { r } { 1 / ( N + 1 ) < \sum _ { n = N + 1 } ^ { \infty } 1 / n ^ { 2 } < 1 / N . } \end{array}$ , so $N = 1 0 ^ { 6 }$

Score:

Suppose $p ( z )$ is a nonconstant real polynomial such that for some real number $a , p ( a ) \neq 0$ and $p ^ { \prime } ( a ) = p ^ { \prime \prime } ( a ) = 0$ . Prove that $p$ must have at least one nonreal zero.

Solution: Observe that if $q ( z )$ is a real-rooted polynomial with distinct roots, then by Rolle’s theorem $q ^ { \prime } ( z )$ is also real-rooted (since it has degree one less than the degree of $q )$ and has the property that between every two roots of $q ^ { \prime }$ there is a root of q. Since polynomials with distinct roots are dense in the set of real-rooted polynomials, this implies that if $q$ is any real-rooted polynomial and $q ^ { \prime } ( z )$ has a double root at z then $q ( z ) = 0$

For the given polynomial $p ^ { \prime } ( z )$ has a double root at $^ { a , }$ but $\boldsymbol { p } ( \boldsymbol { a } ) \neq 0$ , so $p$ cannot be real-rooted.

Problem 3B.

Score:

Prove that a continuous function from R to R which maps open sets to open sets must be monotone.

Solution: We prove the contrapositive. Assume f is not monotone, i.e., there exist $a < b < c$ with $f ( a ) < f ( b )$ and $f ( b ) > f ( c )$ or with $f ( a ) > f ( b )$ and $f ( b ) < f ( c )$ . In the first case, let m be the point at which $f ( x )$ is maximized in $[ a , c ] ;$ such a point exists since f is continuous. Moreover we must have m $\neq a , c$ by the hypothesis. But now the image of $( a , c )$ under f contains $m _ { : }$ , but does not contain a neighborhood of $m$ , so $f$ cannot map open sets to open sets.

The second case is completely analogous.

Problem 4B.

Score:

Evaluate

$$
\int _ { - \infty } ^ { \infty } { \frac { x - \sin x } { x ^ { 3 } } } \mathrm { d } x .
$$

Solution:

Integrate by parts twice to reduce to $( 1 / 6 ) \int _ { - \infty } ^ { \infty } { \frac { \sin ( x ) } { x } }$ dx, which is a standard example in complex analysis.

Problem 5B.

Score:

Suppose $h ( z )$ is entire, $h ( 0 ) = 3 + 4 i$ , and $| h ( z ) | \leq 5$ whenever $| z | < 1$ . What is $h ^ { \prime } ( 0 ) ?$

Solution: We have $| h ( 0 ) | = \sqrt { 9 + 1 6 } = 5$ , so $| h ( 0 ) | \geq | h ( z ) |$ for $z \in D = \{ | z | < 1 \}$ . By the maximum modulus principle this is only possible if $h ( z )$ is constant on $D$ , which implies that $h ^ { \prime } ( 0 ) = 0$

Problem 6B.

Score:

Show that if A is an $n \times n$ complex matrix satisfying

$$
| a _ { i i } | > \sum _ { j \neq i } | a _ { i j } |
$$

for all $i \in \{ 1 , \ldots , n \}$ , then A must be invertible.

Solution:

Assume $A x = 0$ and choose i such that $\left| x _ { i } \right| = \operatorname* { m a x } _ { j } \left| x _ { j } \right|$ . Then

$$
| a _ { i i } | | x _ { i } | \leq \sum _ { j \neq i } | a _ { i j } | | x _ { j } | \leq \sum _ { j \neq i } | a _ { i j } | | x _ { i } |
$$

so that

$$
\left( \left| a _ { i i } \right| - \sum _ { j \neq i } \left| a _ { i j } \right| \right) \left| x _ { i } \right| \leq 0 .
$$

Since the first factor is positive by assumption and the second is nonnegative, we must have $x _ { i } = 0$ . By choice of i we must have $x = 0$ so A is invertible.

Problem 7B.

Score:

For a real symmetric positive definite matrix A and a vector $v \in R ^ { n }$ , show that

$$
\int _ { \mathbb { R } ^ { n } } \exp ( - x ^ { T } A x + 2 v ^ { T } x ) \mathrm { d } x = { \frac { \pi ^ { n / 2 } } { \sqrt { \operatorname* { d e t } { A } } } } \exp ( v ^ { T } A ^ { - 1 } v )
$$

You may assume that $\textstyle \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \sqrt { \pi } }$

Solution:

Complete the square, orthogonally diagonalize A, change variables, and integrate.

Show that there are no natural numbers x, $y \geq 1$ such that

$$
x ^ { 2 } + y ^ { 2 } = 7 x y .
$$

Solution: Assume that there was such a solution. Taking remainders modulo 7 gives us

$$
x ^ { 2 } + y ^ { 2 } \equiv 0 \mod 7 .
$$

The quadratic remainders modulo 7 are 0, 1, 2, 4. The only two quadratic remainders whose sum is $\equiv 0$ are 0 and 0. So

$$
x ^ { 2 } \equiv y ^ { 2 } \equiv 0 \mod 7 .
$$

It follows that $x , y$ are both divisible by 7, i.e. $x = 7 x _ { 1 } , y = 7 y _ { 1 }$ , for some natural numbers $x _ { 1 } , y _ { 1 }$ . It follows that

$$
x _ { 1 } ^ { 2 } + y _ { 1 } ^ { 2 } = 7 x _ { 1 } y _ { 1 } .
$$

Repeating this process would produce an infinite sequence of pairs $( x , y ) , ( x _ { 1 } , y _ { 1 } ) , ( x _ { 2 } , y _ { 2 } ) , . . .$ such that $x _ { i }$ and $y _ { i }$ are strictly decreasing sequences of integers. Contradiction.

Problem 9B.

Score:

Find the smallest n for which the permutation group $S _ { n }$ contains a cyclic subgroup of order 111.

Solution: Let the partition $n = n _ { 1 } + n _ { 2 } + \ldots + n _ { k }$ represent the cycle structure of an element $g \in S _ { n }$ , i.e. g is a products of commuting cycles of the lengths $n _ { 1 } \le n _ { 2 } \le \dots \le n _ { k }$ . The order of the cyclic subgroup generated by $g$ is obviously equal to the least common multiple of $n _ { 1 } , . . . , n _ { k }$ . We want this least common multiple to be $1 1 1 = 3 \cdot 3 7$ One of the possibilities is $( n _ { 1 } , n _ { 2 } , . . . , n _ { k } ) = ( 3 , 3 7 )$ in which case $n = 3 + 3 7 = 4 0$ . We claim that this value of n is the minimal possible. Indeed, if 111 is the least common multiple of $n _ { 1 } , . . . , n _ { k }$ then each of the prime factors 3, 37 divides at least one of the numbers $n _ { i }$ and moreover, the sum of such factors dividing $n _ { i }$ does not exceed their product and thus does not exceed $n _ { i }$ . This implies $n = n _ { 1 } + . . . + n _ { k } \geq 3 + 3 7 = 4 0$ .