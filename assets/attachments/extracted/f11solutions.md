## Problem 1A.

Find the volume of the solid given by $x ^ { 2 } + z ^ { 2 } \leq 1 , y ^ { 2 } + z ^ { 2 } \leq 1$ . (Hint: $\begin{array} { r } { \int _ { - 1 } ^ { 1 } ( s o m e t h i n g ) d z . ) } \end{array}$

Solution: The volume is $\textstyle \int _ { - 1 } ^ { 1 } 4 x y d z$ where $x = y = \sqrt { 1 - z ^ { 2 } }$ . This integral has value $1 6 / 3 .$

## Problem 2A.

Let $f ( x )$ be a irreducible polynomial over the rational numbers Q. Let a in C be a nonzero complex root such that $a ^ { 2 }$ is a root. Prove that for some $n , f ( x )$ divides $x ^ { n } - 1$ .

Solution: For any root b of $f ( x ) , b ^ { 2 }$ is a root. So $a , a ^ { 2 } , \ldots , a ^ { 2 ^ { r } } , \ldots$ . are all roots. So $a ^ { m } = a ^ { n }$ for some $m < n . \ f ( x )$ is the minimal polynomial for a; so $f ( x )$ divides $x ^ { n } - 1$ as a is non-zero.

## Problem 3A.

Let U be a simply connected region, $U \subseteq C =$ the complex numbers. Let $f : U \to C$ be analytic and never 0. Show that there is an analytic $g : U \to C$ such that $f = e ^ { g }$

Solution: Let $h = f ^ { \prime } / f$ . h is analytic, U is simply connected; so there is $k : U \to C$ such that $k ^ { \prime } = h$ . The derivitive of $e ^ { k } / f$ is 0, so $f = c e ^ { k }$ for some c in $C .$

## Problem 4A.

Show that for any integer $n \geq 0$ there is a unique polynomial $S _ { n }$ of degree n with real coefficients such that

$$
\int _ { - 1 } ^ { 1 } S _ { n } ( x ) P ( x ) d x = P ( 1 )
$$

for all polynomials P of degree at most n. Show that $\begin{array} { r } { \int _ { - 1 } ^ { 1 } ( 1 - x ) S _ { m } ( x ) S _ { n } ( x ) d x = 0 } \end{array}$ i f m 6= n . Solution: For any linear function $P \to f ( P )$ from polynomials to reals there is a unique

polynomial $S _ { n }$ such that $\begin{array} { r } { \int _ { - 1 } ^ { 1 } S _ { n } ( x ) P ( x ) d x = f ( P ) } \end{array}$ , becuase this gives a linear map from polynomials $S _ { n }$ to linear functionals that has zero kernel and is between vector spaces of the same dimension. In particular there is a polynomial $S _ { n }$ for $P \mapsto P ( 1 )$

If $m < n$ then $( 1 - x ) S _ { m }$ has degree at most m and has value 0 at 1, so its integral against $S _ { n }$ vanishes by definition of $S _ { n }$ . If m > n a similar argument with m and n exchanged again shows that the integral vanishes, so it vanishes whenever m $\neq n$

## Problem 5A.

Suppose given $a _ { n } > 0$ such that $\Sigma _ { n = 1 } ^ { \infty } a _ { n } = L < \infty$ and such that for all $n , a _ { n } \leq \Sigma _ { m = n + 1 } ^ { \infty } a _ { m } .$ Show that for all t with $0 < t < L$ there is a subseries $a _ { n _ { i } }$ such that $\Sigma _ { i = 1 } ^ { \infty } a _ { n _ { i } } = t .$

Solution: For each n consider partial sums $s = \Sigma _ { i = 1 } ^ { k } a _ { n _ { i } }$ with $n _ { k } < n ;$ we’ll say that \* holds of (n,s) iff $s < t < s + a _ { n }$ . Since $t < L$ there is n, s such that \*. For any n, s with \* since $t - s < a _ { n } \leq \Sigma _ { m = n + 1 } ^ { \infty } a _ { m }$ , we can find $n ^ { \prime } > n$ and extend s to $s ^ { \prime }$ such that $n ^ { \prime } , s ^ { \prime }$ has \*. This produces a subseries $a _ { n _ { i } } ;$ ; since the $a _ { n }$ converges to 0, this subseries converges to t.

## Problem 6A.

Let $G$ be a group. Show that if G has trivial center then its automorphism group Aut(G) has trivial center.

Solution: For a in G let $g _ { a }$ be the inner automorphism $( g _ { a } ( x ) = a x a ^ { - 1 } )$ . For h in $A u t ( G )$ , $h \circ g _ { a } = g _ { h ( a ) } \circ h$ . If h is in the center of Aut(G) then, for all a in $G , g _ { a } = g _ { h ( a ) }$ so $a ^ { - 1 } h ( a )$ is in the center of G, so h is the identity.

## Problem 7A.

Find the Laurent expansion of

$$
f ( z ) = ( 1 + z ) ^ { - 1 } + ( z ^ { 2 } - 9 ) ^ { - 1 }
$$

in the set $\{ z : 1 < | z | < 3 \}$

Solution:

$$
{ \frac { 1 } { z } } - { \frac { 1 } { z ^ { 2 } } } + { \frac { 1 } { z ^ { 3 } } } - \ldots - { \frac { 1 } { 9 } } - { \frac { z ^ { 2 } } { 8 1 } } - { \frac { z ^ { 4 } } { 7 2 9 } } - \ldots .
$$

## Problem 8A.

Let A be an n by n real matrix such that all entries not on the diagonal are positive, and the sum of the entries in each row is negative. Show that the determinant of A is non-zero.

## Solution:

Proof by induction on the size of the matrix. Add a suitable multiple of the first column from each other column to kill all entries in the first row other than the first. Then the

$( n - 1 ) \times ( n - 1 )$ matrix formed by the crossing off the first row and column still has the property in the question, so its determinant is nonzero by induction. The determinant of the original matrix is this determinant times the first entry, so is also nonzero.

## Problem 9A.

The Bessel function $J _ { 1 } ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + \cdot \cdot \cdot$ satisfies the differential equation

$$
x ^ { 2 } \frac { d ^ { 2 } J _ { 1 } } { d x ^ { 2 } } + x \frac { d J _ { 1 } } { d x } + ( x ^ { 2 } - 1 ) J _ { 1 } = 0
$$

and also has derivative 1 at 0. Find the coefficients $a _ { n }$

Solution: Looking at the coefficient of $x ^ { n }$ in the differential equation gives

$$
n ( n - 1 ) a _ { n } + n a _ { n } + a _ { n - 2 } - a _ { n } = 0
$$

so

$$
a _ { n } = - a _ { n - 2 } / ( n - 1 ) ( n + 1 ) .
$$

As $a _ { 0 } = 0 , a _ { 1 } = 1$ , this gives $a _ { n } = 0$ for n even, and $a _ { 2 m + 1 } = ( - 1 ) ^ { m } / 4 ^ { m } m ! ( m + 1 ) !$ for $n = 2 m + 1$ odd.

## Problem 1B.

For which pairs of real numbers $( a , b )$ does the series $\scriptstyle \sum _ { n = 3 } ^ { \infty } n ^ { a } ( \log n ) ^ { b }$ converge?

## Solution:

By the integral test this is equivalent to asking for convergence of the integral

$$
\int _ { x = 3 } ^ { \infty } x ^ { a } ( \log x ) ^ { b } d x
$$

This converges if $a < - 1$ and diverges if $a > - 1$ by comparison with $\textstyle \int x ^ { s } d x$ . If $a = - 1$ then it converges for $b < - 1$ and diverges if $b > - 1$ again by doing the integral explicitly, using the fact that the derivative of $( \log x ) ^ { b + 1 }$ is $( b + 1 ) ( \log x ) ^ { b } x ^ { - 1 }$ . For $a = b = - 1$ it diverges as the derivative of log log x is $x ^ { - 1 } ( \log x ) ^ { - 1 }$

## Problem 2B.

Let k be one of the fields $\mathbb { C } , \mathbb { R } , \mathbb { Q } , \mathbb { F } _ { 4 0 4 4 1 2 1 }$ (the finite field with $4 0 4 4 1 2 1 = 2 0 1 1 ^ { 2 }$ elements;   
2011 is prime).

For which of the above choices of k is the ring $k [ x ] / ( x ^ { 4 } + 6 x - 1 2 )$ a field? (Here $( x ^ { 4 } +$ $6 x - 1 2 )$ denotes the ideal in $k [ x ]$ generated by $x ^ { 4 } + 6 x - 1 2 . )$

Solution: In each case, the quotient ring is a field if and only if $x ^ { 4 } + 6 x - 1 2$ is irreducible in $k [ x ]$ . It is not irreducible in $\mathbb { R } [ x ]$ because all irreducible polynomials with real coefficients have degree $\leq 2$ , and it is not irreducible in $\mathbb { C } [ x ]$ because it has a root. In $\mathbb { F } _ { 2 0 1 1 }$ it is either reducible (in which case it is also reducible in $\mathbb { F } _ { 4 0 4 4 1 2 1 } )$ , or it is not reducible, in which case if α is a root in the algebraic closure then that root lies in $\mathbb { F } _ { 2 0 1 1 ^ { 4 } }$ , so it is quadratic over $\mathbb { F } _ { 2 0 1 1 ^ { 2 } }$ and therefore the polynomial has a quadratic factor over that field and is therefore again reducible. Finally, $x ^ { 4 } + 6 x - 1 2$ is irreducible in $\mathbb { Z } [ x ]$ because it is an Eisenstein polynomial with $p = 3$ (but not $p = 2 )$ , hence by Gauss’s lemma it is irreducible in Q[x].

Therefore the given ring is a field only for the field $k = \mathbb { Q }$ (among the given fields).

## Problem 3B.

If a and b are points in the open unit disk of the complex plane, show that there is a holomorphic map from the open unit disc onto itself with holomorphic inverse that takes a to b.

Solution: It is sufficient to do the case $a = 0$ , because for the general case one can just compose a map taking a to 0 with a map taking 0 to b. The Moebius transformation taking z to $( z + b ) / ( z \overline { { b } } + 1 )$ takes $a = 0$ to b.

## Problem 4B.

The sequence $u _ { n }$ is defined by $u _ { 0 } = 0 , u _ { 1 } = 1 , u _ { n } = 3 u _ { n - 1 } + u _ { n - 2 }$ . Calculate lim $\mathfrak { l } _ { n \to + \infty } u _ { n } / u _ { n - 1 }$

Solution: $u _ { n }$ is given by a linear combination of the powers $\lambda _ { 1 } ^ { n } , \lambda _ { 2 } ^ { n }$ of $\lambda ^ { 2 } = 3 \lambda + 1$ (with non-zero coefficients), so the limit of the ratio $u _ { n } / u _ { n - 1 }$ is the root $( 3 + { \sqrt { 1 3 } } ) / 2$ of largest absolute value.

## Problem 5B.

Prove that a continuous map from a compact metric space to a metric space has closed image.

Solution: This follows from the facts that the image of a compact set under a continuous map is compact, and any compact subset of a metric space is closed, both of which are standard bookwork.

## Problem 6B.

(a) Show that if every element of a group has order 1 or 2 then the group is abelian.

(b) Show that there is a non-abelian group such that every element has order 1 or 3.

Solution: (a) $a b a b = ( a b ) ^ { 2 } = 1$ so $\imath b = b ^ { - 1 } a ^ { - 1 }$ , but $a = a ^ { - 1 }$ and $b = b ^ { - 1 }$ so $a b = b a .$

(b) Use the group of order 27 of 3 by 3 matrices over the field with 3 elements that are upper triangular with diagonal elements 1.

## Problem 7B.

Find

$$
\int _ { 0 } ^ { 2 \pi } { \frac { 1 } { 1 + { \frac { 1 } { 2 } } \sin ( \theta ) } } d \theta .
$$

Solution: Put $z = e ^ { i \theta }$ . Then the integral is

$$
\int _ { C } { \frac { 1 } { 1 + { \frac { 1 } { 2 } } { \frac { z - z ^ { - 1 } } { 2 i } } } } { \frac { d z } { i z } } ,
$$

where C is the unit circle with a positive orientation. The only singularity inside of C is at√ $z = ( - 2 + { \sqrt { 3 } } ) i$ . The residue there is

$$
{ \frac { 2 } { \sqrt { 3 } i } } ,
$$

so the answer is

$$
{ \frac { 4 \pi } { \sqrt { 3 } } } .
$$

## Problem 8B.

Compute $A ^ { 1 0 0 }$ where A is the matrix $\left( \begin{array} { l l } { { 3 / 2 } } & { { 1 / 2 } } \\ { { - 1 / 2 } } & { { 1 / 2 } } \end{array} \right)$

Solution: The only eigenvalue of A is 1, and the only eigenvectors are multiples of $v = \left( \begin{array} { l } { 1 } \\ { - 1 } \end{array} \right)$ The matrix A takes v to v and u to $u + v / 2$ where $u = { \binom { 1 } { 0 } }$ . So $A ^ { 1 0 0 }$ takes v to v and u to $u + 5 0 v$ , so is $\left( _ { - 5 0 , - 4 9 } ^ { \ 5 1 , 5 0 } \right)$

(Alternative solution: $A ^ { 1 0 0 } = ( ( A ( ( ( A ^ { 3 } ) ^ { 2 } ) ^ { 2 } ) ^ { 2 } ) ^ { 2 } ) ^ { 2 } . )$

Let X and Y be metric spaces, with metrics $d _ { X }$ and $d _ { Y } .$ , respectively. Let $f , f _ { 1 } , f _ { 2 } , \ldots$ . be bijective functions from X to Y , with inverses $g , g _ { 1 } , g _ { 2 } , \ldots$ , respectively. Assume that

1. g is uniformly continuous; and

2. $f _ { n }  f$ uniformly as $n \to \infty$

Prove that $g _ { n }  g$ uniformly as $n \to \infty$

Solution: Let $\epsilon > 0$ be given. Because g is uniformly continuous we may fix $\delta > 0$ such that $d _ { X } ( g ( y ) , g ( y ^ { \prime } ) ) < \epsilon$ for all $y , y ^ { \prime } \in Y$ for which $d _ { Y } ( y , y ^ { \prime } ) < \delta$

Because $f _ { n }  f$ uniformly, we may fix an integer $N > 0$ such that $d _ { Y } ( f _ { n } ( x ) , f ( x ) ) < \delta$ for all $x \in X$ and all $n \geq N$

Then, for all $n \geq N$ and all $y \in Y$ , we have

$$
d _ { Y } ( f ( g _ { n } ( y ) ) , y ) = d _ { Y } ( f ( g _ { n } ( y ) ) , f _ { n } ( g _ { n } ( y ) ) ) < \delta
$$

by choice of N, and therefore

$$
d _ { X } ( g _ { n } ( y ) , g ( y ) ) = d _ { X } ( g ( f ( g _ { n } ( y ) ) ) , g ( y ) ) < \epsilon
$$

by choice of δ. Thus $g _ { n }  g$ uniformly.