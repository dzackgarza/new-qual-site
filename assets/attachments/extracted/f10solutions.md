Let

$$
\dots \subset X _ { 2 } \subset X _ { 1 }
$$

be a nested sequence of closed nonempty connected subsets of a compact metric space X.   
Prove that $\cap _ { i = 1 } ^ { \infty } X _ { i }$ is nonempty and connected.

## Solution:

Since $X _ { i }$ is closed in X, it is compact. The intersection of a nested sequence of nonempty compact sets is nonempty. (Proof : If it is empty then there is an open cover of X by the increasing sequence $\{ X - X _ { i } \} _ { i = 1 } ^ { \infty }$ . This must have a finite subcover, so $X _ { i } = \varnothing$ for some i, which is a contradiction.)

Suppose that $\cap _ { i = 1 } ^ { \infty } X _ { i }$ is not connected. Let A and B be two disjoint nonempty closed sets so that $\cap _ { i = 1 } ^ { \infty } X _ { i } \stackrel { \cdot } { = } A \cup B$ . Find disjoint open sets U and V so that $A \subset U$ and $B \subset V$ Put $F _ { i } = X _ { i } - ( U \cup V )$ Then $\{ F _ { i } \} _ { i = 1 } ^ { \infty }$ is a nested sequence of compact sets, whose intersection is empty. Thus $F _ { i } = \emptyset$ for some i. That is, $X _ { i } \subset U \cup V$

However, $X _ { i }$ intersects both U and V , since $X _ { i } \cap A \neq \emptyset$ and $X _ { i } \cap B \neq \varnothing$ . This contradicts the assumption that $X _ { i }$ is connected.

## Problem 2A.

Score:

Let R be a finite ring. Prove that there are positive integers m and n with $m > n$ such that all $x \in R$ satisfy $x ^ { m } = x ^ { n }$

Solution: There are only a finite number of functions from R to R as $| R |$ is finite, so in any infinite list of functions from R to R such as $x \to x ^ { n }$ , two must be the same by the pigeon-hole principle.

## Problem 3A.

Score:

Suppose that a function f is bounded and analytic on a deleted neighborhood $0 < | z | < \epsilon$ of the origin. Let

$$
f ( z ) = \sum _ { j = - \infty } ^ { \infty } c _ { j } z ^ { j }
$$

be the Laurent expansion of f. Show that if j is negative then $c _ { j } = 0$

Solution: We know that

$$
c _ { j } = { \frac { 1 } { 2 \pi i } } \int _ { C } z ^ { - j - 1 } f ( z ) d z ,
$$

where C is a contour around the origin. Taking C of radius r, we can estimate $\left| c _ { j } \right|$ above by

$$
{ \frac { 1 } { 2 \pi } } r ^ { - j - 1 } M 2 \pi r .
$$

If j is negative then by taking r to zero, we get $c _ { j } = 0$

## Problem 4A.

Score:

If the complex conjugate of a complex matrix is equal to its transpose, prove that all its eigenvalues are real.

Solution: If (,) is the usual Hermitian inner product and x a norm 1 eigenvector of the Hermitian matrix A with eigenvalue λ then $\lambda = ( \lambda x , x ) = ( A x , x ) = ( x , \overline { { { A } } } ^ { T } x ) = ( x , A x ) =$ $( x , { \bar { \lambda } } x ) = { \bar { \lambda } }$ so λ is real.

## Problem 5A.

Score:

Show that the series

$$
\sum _ { n = 1 } ^ { \infty } \sin { \frac { x } { n ^ { 2 } } }
$$

converges uniformly on any bounded interval in R.

## Solution:

Let I be a bounded interval in R.

Since $\operatorname* { l i m } _ { x \to 0 } { \frac { \sin x } { x } }$ exists, the function (sin x)/x extends to a continuous function on all of R, so it is bounded on the bounded interval I. Therefore there is a C such that | sin $x | \leq C | x |$ for all $x \in I .$ . (With a little extra work one can show that $C = 1$ works for all of R.)

Therefore if $| x | \le B$ for all $x \in I ,$ , then the summands are bounded in absolute value by $B C / n ^ { 2 }$ , and therefore the sum converges uniformly on I by the Weierstrass M-test.

For nonzero integers $a , b , c ,$ show that

$$
\operatorname* { g c d } \{ a , \operatorname { l c m } \{ b , c \} \} = \operatorname { l c m } \{ \operatorname* { g c d } \{ a , b \} , \operatorname* { g c d } \{ a , c \} \} \ .
$$

Here gcd denotes greatest common divisor and lcm denotes least common multiple. Solution:

If we factor $a = p _ { 1 } ^ { m _ { 1 } } p _ { 2 } ^ { m _ { 2 } } . .$ . and $b = p _ { 1 } ^ { n _ { 1 } } p _ { 2 } ^ { n _ { 2 } } . .$ . as products of prime powers, then the lcm is the product of $p _ { i } ^ { m a x m _ { i } , n _ { i } }$ and the gcd is the product of $p _ { i } ^ { m a x m _ { i } , n _ { i } }$ . The result then follows from $m i n ( x , m a x ( y , z ) ) = m a x ( m i n ( x , y ) , m i n ( x , z ) )$ , which in turn follows because both sides are x unless x is largest, in which case both sides are max(y,z).

Problem 7A.

Score:

Use residues to compute

$$
\int _ { - \infty } ^ { \infty } { \frac { \sin ( x ) } { x ^ { 2 } + 4 x + 5 } } d x .
$$

Solution:

It’s enough to compute the imaginary part of

$$
\int _ { - \infty } ^ { \infty } { \frac { e ^ { i x } } { x ^ { 2 } + 4 x + 5 } } d x .
$$

Put

$$
f ( z ) = { \frac { e ^ { i z } } { z ^ { 2 } + 4 z + 5 } } .
$$

Using Jordan’s Lemma, we can apply the Cauchy residue theorem to a semicircle in the upper half plane and just compute residues. The only singularity in the upper half plane is at $z = - 2 + i$ . The residue there is

$$
{ \frac { e ^ { - 1 - 2 i } } { 2 i } } ,
$$

so the answer is

$$
- { \frac { \pi } { e } } \sin ( 2 ) .
$$

## Problem 8A.

Score:

Suppose that $\begin{array} { r } { f ( x _ { 1 } , \ldots , x _ { n } ) = \sum _ { j k } a _ { j k } x _ { j } x _ { k } } \end{array}$ for some real numbers $\boldsymbol { a } _ { j k }$ . If f is non-negative for all real arguments, show that f can be written as a finite sum of squares of linear forms in $x _ { 1 } , \ldots , x _ { n }$

## Solution:

We can assume the matrix is symmetric. We use induction on $n .$ If $a _ { 1 1 } = 0$ then all other entries in the first row or column must be 0 otherwise $f$ would take negative values, so we can assume that $a _ { 1 1 } > 0$ . Then by changing $x _ { 1 }$ to $x _ { 1 }$ minus a suitable linear combination of the other variables, we can kill all the other entries in the first row and column of the matrix. This writes $f$ as the sum of the square of a linear form and a non-negative quatratic form in $n - 1$ varaibles $x _ { 2 } , . . . , x _ { n }$ , so by induction $f$ is a sum of squares.

Problem 9A.

Score:

Show that there is more than one real-valued differentiable function y with domain the real numbers such that $\textstyle { \frac { d y } { d x } } = y ^ { 2 / 3 }$ and $y ( 0 ) = 1$

## Solution:

The obvious general solution of the differential equation is $y \ = \ ( ( x - C ) / 3 ) ^ { 3 }$ , which satisfies the boundary condition for the unique value −3 of $C ,$ and the problem is to find another solution. One example is given by taking this solution, and changing its values for $x < - 3$ (when y is negative) to be 0. This is still differentiable (though not infinitely differentiable) at $x = - 3$ and satisfies the differential equation. (There are infinitely many other solutions satisfying the boundary condition: draw a picture of the solutions to see what is going on.)

Problem 1B.

Score:

Let $f : { \bf R } ^ { 2 }  { \bf R }$ be a continuous map such that the inverse image of any bounded set is bounded. Show that $f$ achieves either a minimum value or a maximum value.

Solution: Choose n so that $f ^ { - 1 } ( [ - n , n ] )$ is nonempty. Since $f ^ { - 1 } ( [ - n , n ] )$ is compact, it lies   
within some closed ball $D _ { R }$ around the origin in $\mathbf { R } ^ { 2 }$ Since $\mathbf { R } ^ { 2 } - D _ { R }$ is connected, and $f ( \mathbf { R } ^ { 2 } - D _ { R } ) \subset \mathbf { R } - [ - n , n ]$ , it follows that $f ( \mathbf { R } ^ { 2 } - D _ { R } ) \subset$   
$( - \infty , - n )$ or $f ( \mathbf { R } ^ { 2 } - D _ { R } ) \subset ( n , \infty )$ If $f ( \mathbf { R } ^ { 2 } - D _ { R } ) \subset ( - \infty , - n )$ then sup $\boldsymbol { f } = \operatorname* { s u p } \boldsymbol { f } \big | _ { D _ { R } }$ is achieved. If $f ( \mathbf { R } ^ { 2 } - D _ { R } ) \subset ( n , \infty )$ then inf $f = \operatorname { i n f } f { \big | } _ { D _ { R } }$ is achieved.

Score:

Show that the splitting field of $x ^ { 5 } - 1 0 x + 5$ over the rational numbers has Galois group the symmetric group $S _ { 5 }$ on 5 points. (You may assume that any subgroup of $S _ { 5 }$ containing a 5-cycle and a 2-cycle is the whole of $S _ { 5 } . )$

Solution: The polynomial is irreducible by Eisenstein’s criterion for $p = 5 .$ , so the Galois group has order divisible by 5. It has exactly 3 real roots (the derivative has just 2 real roots so it has at most 3 real roots, and looking at the signs at −∞, 0, 1, ∞ shows that it has at least 3 real roots) so complex conjugation is a transposition in the Galois group. Since the Galois group is a subgroup of $S _ { 5 }$ containing a 5-cycle and a transposition, it must be the whole of $S _ { 5 }$

## Problem 3B.

Score:

Give an example of a conformal map from the unit disk $\{ z \ : \ | z | < 1 \}$ onto the sector $\{ z : 0 < \arg ( z ) < \pi / 4 \}$ .

Solution: $z  z - i$ takes the unit disk to the unit disk with center −i. Applying $z \to 1 / z$ takes this to the halfplane with imaginary part greater than $1 / 2 .$ . Subtracting $i / 2$ takes this to the half plane with positive imaginary part. Taking 4th roots takes this to the desired sector.

## Problem 4B.

Score:

Find the determinant of the 6 by 6 matrix with entries $a _ { j , k } = j ^ { k }$ for $1 \leq j , k \leq 6$ . (You may give your answer in terms of a product of powers of primes.)

Solution: This is essentially a Vandermonde matrix for the values 1,2,3,4,5,6 (at least if the rows are divided by these numbers) so the determinant is the product of all the differences of 0, 1, 2, 3, 4, 5, 6 which is $1 ^ { 6 } 2 ^ { 5 } 3 ^ { 4 } 4 ^ { 3 } \dot { 5 } ^ { 2 } 6 ^ { 1 } = 2 ^ { 1 2 } 3 ^ { 5 } 5 ^ { 2 }$

## Problem 5B.

Score:

Let $f : [ 0 , \infty ) \to { \mathbb R }$ be a function such that   
$f$ is continuous,   
$f ( 0 ) = 0 ,$   
• f is differentiable on (0, ∞), and   
$f ^ { \prime }$ is increasing on (0, ∞).

Define $g : ( 0 , \infty ) \to { \mathbb R }$ by

$$
g ( x ) = { \frac { f ( x ) } { x } } .
$$

Show that $g$ is an increasing function.

[Hint: Differentiate.]

Solution: Following the hint, we have

$$
g ^ { \prime } ( x ) = \frac { x f ^ { \prime } ( x ) - f ( x ) } { x ^ { 2 } } ,
$$

and it will suffice to show that $x f ^ { \prime } ( x ) > f ( x )$ for all $x \in ( 0 , \infty )$

Fix $x > 0 .$ . By the Mean Value Theorem applied to f on $[ 0 , x ]$ , there is ${ \mathrm { ~ a ~ c ~ } } \in ( 0 , x )$ such that

$$
f ^ { \prime } ( c ) = \frac { f ( x ) - f ( 0 ) } { x - 0 } = \frac { f ( x ) } { x } \ .
$$

Since $f ^ { \prime }$ is increasing, it then follows that

$$
x f ^ { \prime } ( x ) > x f ^ { \prime } ( c ) = f ( x ) ,
$$

and therefore $g ^ { \prime } ( x ) > 0$

## Problem 6B.

Score:

Show that there are no simple groups of order 30. (Hint: show that if a non-cyclic simple group has order divisible by a prime $p ,$ then it has at least $p ^ { 2 } - 1$ non-trivial elements of order a power of $p . \mathrm { _ { \ell } }$ )

Solution: Suppose there is a simple group of order 30. For p prime dividing the order of the group the Sylow p-subgroups cannot be normal, so there is more than 1 of them, so there are at least $p + 1$ of them. Since any 2 have at most 1 element in common there are at least $p ^ { 2 } - 1$ elements of order $p .$ So there are at least 24 elements of order 5, and 8 of order 3. But this is more than 30 elements which is impossible.

## Problem 7B.

Score:

If f is an analytic function from the unit disk into itself with $f ( 0 ) = 0$ , prove that $| f ^ { \prime } ( 0 ) | \le 1$

Solution: Put $g ( z ) = f ( z ) / z$ . Then we have to show $| g ( 0 ) | \le 1$ . But bythe maximum modulus principle, for any positive $\epsilon , ~ | g ( 0 ) |$ is at most the maximum of $| g |$ on a circle of

radius $1 - \epsilon .$ , which is at most $1 / ( 1 - \epsilon )$ because $| f ( z ) |$ is at most 1 and $| 1 / z |$ is at most $1 / ( 1 - \epsilon )$ . Since  can be anything positive this shows that $| f ^ { \prime } ( 0 ) | = | g ( 0 ) | \leq 1$

Since this problem is part of the proof of the Schwarz lemma, quoting this lemma will not get full marks.

## Problem 8B.

Score:

Suppose that f is a positive continuous function on the interval $[ a , b ]$ . Prove that there are polynomials $p _ { n }$ for $n = 0 , 1 , 2 , . . .$ . such that $p _ { n }$ has highest coefficient $x ^ { n }$ , and

$$
\int _ { a } ^ { b } p _ { m } ( x ) p _ { n } ( x ) f ( x ) d x = 0
$$

if m $\neq n .$

Solution: Apply the Gram-Schmidt process to $1 , x , x ^ { 2 } , \ldots$ using the inner product $( g , h ) =$ $\textstyle \int _ { a } ^ { b } g ( x ) h ( x ) f ( x ) d x .$

## Problem 9B.

Score:

(a) Prove that the series $0 ! / x - 1 ! / x ^ { 2 } + 2 ! / x ^ { 3 } - 3 ! / x ^ { 4 } \cdot \cdot$ · diverges for all nonzero x.

(b) If $x > 0$ and

$$
G ( x ) = \int _ { 0 } ^ { \infty } \frac { e ^ { - t x } } { 1 + t } d t
$$

show that the difference between $G ( x )$ and the sum of the first n terms of the series in (a) has absolute value at most that of the first term omitted.

(c) If $x = 1 0 0$ , prove that the sum of the first 10 terms of the divergent series in (a) gives $G ( x )$ correctly to more than 10 decimal places.

Solution:

(a) The terms tend to infinity so the series cannot converge.

(b) Repeated integration by parts shows that the integral is the sum of the first few terms of the series above up to an error term

$$
( - 1 ) ^ { n } \frac { n ! } { x ^ { n } } \int _ { 0 } ^ { \infty } \frac { e ^ { - t x } } { ( 1 + t ) ^ { n + 1 } } d t
$$

whose sign is $( - 1 ) ^ { n }$ , from which the result follows as the successive partial sums must be alternately too big and too small.

(c) This follows from (b) as the error is less than the magnitude $1 0 ! / 1 0 0 ^ { 1 1 }$ of the first term omitted which is less than $1 0 ^ { - 1 1 }$