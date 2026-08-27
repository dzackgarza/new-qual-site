# Department of Mathematics, University of California, Berkeley

## GRADUATE PRELIMINARY EXAMINATION, Part A

Spring Semester 2019

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if p 6= q.

4. No notes, books, calculators or electronic devices may be used during the exam.

## PROBLEM SELECTION

Part A: List the six problems you have chosen:

## GRADE COMPUTATION (for use by grader—do not write below)

1A.

2A.

1B.

Calculus

2B.

Real analysis

3A.

3B.

Real analysis

4A.

4B.

Complex analysis

5A.

5B.

Complex analysis

6A.

6B.

Linear algebra

7A.

7B.

Linear algebra

8A.

8B.

Abstract algebra

9A.

9B.

Abstract algebra

Part A Subtotal:

Part B Subtotal:

Grand Total:

## Problem 1A.

Score:

Let $y$ be a solution of $y ^ { \prime \prime \prime } { - } y = 0$ such that $y ( t ) \to 0$ as t → ∞. Show that $y ( 0 ) + y ^ { \prime } ( 0 ) + y ^ { \prime \prime } ( 0 ) =$ 0.

## Solution:

The characteristic equation $r ^ { 3 } - 1 = 0$ has a real root at $r ~ = ~ 1$ corresponding to a growing solution, and two complex roots $r _ { 1 }$ and $r _ { 2 }$ with negative real parts. The condition at ∞ implies that y is a linear combination $a _ { 1 } \exp ( r _ { 1 } t ) + a _ { 2 } \exp ( r _ { 2 } t )$ . Both $r _ { 1 }$ and $r _ { 2 }$ satisfy

$$
1 + r + r ^ { 2 } = { \frac { 1 - r ^ { 3 } } { 1 - r } } = 0
$$

so y(0) + y0(0) + y00(0) = a1(1 + r1 + r21) + a2(1 + r2 + r22) = 0.

Please cross out this problem if you do not wish it graded

## Problem 2A.

Score:

Let $f : \mathbb { R } \to \mathbb { R }$ be bounded and continuously differentiable. Show that every solution y of $y ^ { \prime } = f ( y )$ is monotone.

## Solution:

If $y ^ { \prime } ( t _ { 0 } ) = 0$ for some $t _ { 0 }$ then $f ( y ( t _ { 0 } ) ) = 0$ . Hence the constant $y _ { 0 } = y ( t _ { 0 } )$ is a solution matching y at $t = t _ { 0 }$ . By uniqueness, y is constant and therefore monotone.

Please cross out this problem if you do not wish it graded

## Problem 3A.

Score:

Let $f$ be a twice continuously differentiable function on [0, 1] such that $f ( 0 ) = f ( 1 ) = 0$ Prove that

$$
\operatorname* { m a x } _ { x \in [ 0 , 1 ] } | f ( x ) | \leq { \frac { 1 } { 8 } } \operatorname* { m a x } _ { x \in [ 0 , 1 ] } | f ^ { \prime \prime } ( x ) | ,
$$

and find an example where equality holds.

Solution: The equality holds for $f = x ( x - 1 ) / 2$ with constant $f ^ { \prime \prime } = 1$ maximum modulus value $1 / 8$ achieved at $x = 1 / 2$ . In general, let $x = \alpha$ be the point of maximum for |f |. Replacing $f ( x )$ with $f ( 1 - x )$ if necessary, we may assume that $0 < \alpha \le 1 / 2$ . We have:

$$
f ( \alpha ) = \int _ { 0 } ^ { \alpha } f ^ { \prime } ( x ) d x = \alpha f ^ { \prime } ( \alpha ) - \int _ { 0 } ^ { \alpha } x f ^ { \prime \prime } ( x ) d x .
$$

$$
| f ( \alpha ) | \leq M \int _ { 0 } ^ { \alpha } x d x = M \frac { \alpha ^ { 2 } } { 2 } \leq \frac { M } { 8 } .
$$

Let M denote $\mathrm { m a x } _ { x \in [ 0 , 1 ] } | f ^ { \prime \prime } ( x ) |$ . Since α is a critical point of $f ,$ we have $f ^ { \prime } ( \alpha ) = 0$ and find:

Please cross out this problem if you do not wish it graded

## Problem 4A.

Score:

Evaluate

$$
I = \int _ { - \infty } ^ { \infty } { \frac { x \sin x } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x .
$$

## Solution:

Integrate by parts to get

$$
I = { \frac { 1 } { 2 } } \int _ { - \infty } ^ { \infty } { \frac { \cos x } { 1 + x ^ { 2 } } } \ d x
$$

Change $\cos ( x )$ to $\exp ( i x )$ and close the contour in the upper half plane to get

$$
I = { \frac { \pi } { 2 e } } .
$$

## Problem 5A.

Score:

Find the number of complex roots of $e ^ { z } = 3 z ^ { 6 }$ with $| z | < 1$ that have positive imaginary part.

Solution: On the unit circle $\left| 3 z ^ { 6 } \right| > \left| e ^ { z } \right|$ so the number of real or complex roots in the unit disk is the same as the number of roots of $3 z ^ { 6 }$ by Rouche’s theorem, which is 6. There are exactly two real roots (look at the graphs) so there are exactly 4 roots that are complex but not real. The complex roots occur in complex conjugate pairs, so there are exactly two that have positive imaginary part.

## Problem 6A.

Score:

Let n be a positive integer and let a be a complex number. Prove that $a ^ { n } = 1$ if and only if there are invertible n by n complex matrices X, Y such that $Y X = a X Y$

## Solution:

To show the second condition implies the first take determinants of both sides.

To show that the first condition implies the second, choose a basis $e _ { 0 } , e _ { 1 } , . . . , e _ { n } = e _ { 0 }$ . Put $X e _ { m } = e _ { m + 1 } , Y e _ { m } = a ^ { m } e _ { m } .$

Score:

Let A be a complex $n \times n$ matrix satisfying $A ^ { 3 7 } = I$ . Show that A is diagonalizable.

## Solution:

The minimal polynomial of A divides $x ^ { 3 7 } - 1$ which has only linear factors.

Score:

Show that $F : \mathbb { C } ^ { 3 } \to \mathbb { C } ^ { 3 }$ defined by

$$
F ( u , v , w ) = ( - u - v - w , u v + u w + v w , - u v w )
$$

is surjective but not injective.

## Solution:

Since F takes the three roots of a monic polynomial to its coefficients, it is surjective. It is not injective because permuting distinct roots gives the same polynomial.

<table><tr><td>Problem 9A. Score:</td></tr></table>

Let S be a countable set of real numbers. Show that there are function $g _ { n } : \mathbb { N } \to \mathbb { N }$ such that if $f : \mathbb { N } \to \mathbb { N }$ is a function from N to N with $f ( n + 1 ) > g _ { n } ( f ( n ) )$ for all n, then $\textstyle A = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { f ( n ) } }$ converges to a real that is not in the set S.

## Solution:

Suppose $\boldsymbol { S } = \{ s _ { 1 } , s _ { 2 } , \ldots \}$ . We will choose all functions $g _ { n }$ so that $g _ { n } ( m ) > 2 m$ (so in particular the series will converge). Suppose we have chosen the functions $g _ { 1 } , . . . g _ { n }$ . We choose $g _ { n + 1 }$ so that the sum cannot be $s _ { n + 1 }$ . For any given value of $f ( n )$ there are only a finite number of possible values for the sum of the first n terms of A. Let $\epsilon _ { n }$ be the minimum of the non-zero distances from these values to $s _ { n + 1 }$ . Then just choose $g _ { n + 1 } ( f ( n ) )$ larger than $2 / \epsilon _ { n } .$ so that the sum of all but the first n terms of the sum A is less than $\epsilon _ { n } .$ . This implies that the sum cannot be $s _ { n + 1 }$

Spring Semester 2019

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q$

4. No notes, books, calculators or electronic devices may be used during the exam.

## PROBLEM SELECTION

Part B: List the six problems you have chosen:

Problem 1B.

Score:

Evaluate

$$
I = \int _ { 0 } ^ { \pi / 2 } { \frac { \sin { x } \cos { x } } { \sin ^ { 4 } { x } + \cos ^ { 4 } { x } } } d x
$$

Solution:

Put t = tan x.

$$
I = \int _ { 0 } ^ { \pi / 2 } { \frac { \tan x \sec ^ { 2 } x } { 1 + \tan ^ { 4 } x } } d x = \int _ { 0 } ^ { \infty } { \frac { t } { 1 + t ^ { 4 } } } d t = \int _ { 0 } ^ { \infty } { \frac { 1 / 2 } { 1 + y ^ { 2 } } } d y = { \frac { \pi } { 4 } }
$$

## Problem 2B.

Score:

For $t \geq 0$ let

$$
F ( t ) = \int _ { 0 } ^ { t } \exp ( - x ^ { 2 } ) d x
$$

and

$$
G ( t ) = \int _ { 0 } ^ { 1 } \frac { \exp ( - t ^ { 2 } ( 1 + x ^ { 2 } ) ) } { 1 + x ^ { 2 } } d x .
$$

Show that $F ( t ) ^ { 2 } + G ( t )$ is constant and deduce the value of $F ( \infty )$

## Solution:

Differentiate with respect to t. $F ( \infty ) = \sqrt { G ( 0 ) } = \sqrt { \pi } / 2$

Please cross out this problem if you do not wish it graded

## Problem 3B.

Score:

Show that $x _ { n + 1 } = ( 1 + x _ { n } ) ^ { - 1 }$ converges and find its limit for any $x _ { 0 } > 0$

## Solution:

If the limit $x \geq 0$ exists it must satisfy $x ( 1 + x ) = 1$ by continuity, so $x = ( \sqrt { 5 } - 1 ) / 2$ Subtraction shows that

$$
| e _ { n + 1 } | = | x _ { n + 1 } - x | = \frac { | e _ { n } | } { ( 1 + x _ { n } ) ( 1 + x ) } \leq \frac { 2 } { 3 } | e _ { n } |
$$

so $x _ { n } \to x$

## Problem 4B.

Score:

Let $c _ { 0 } , c _ { 1 } , . . . , c _ { n - 1 }$ be complex numbers. Prove that all the zeroes of the polynomial

$$
z ^ { n } + c _ { n - 1 } z ^ { n - 1 } + \cdot \cdot \cdot + c _ { 1 } z + c _ { 0 }
$$

lie in the open disc with center 0 and radius

$$
1 + \left| c _ { n - 1 } \right| + \cdot \cdot \cdot + \left| c _ { 1 } \right| + \left| c _ { 0 } \right| .
$$

## Solution:

If $\cdot \ | z | \geq 1 + | c _ { n - 1 } | + \cdot \cdot \cdot + | c _ { 1 } | + | c _ { 0 } |$ then $\left| z ^ { n } \right|$ is greater than the sum of the remaining terms of the polynomial so the polynomial cannot vanish.

Please cross out this problem if you do not wish it graded

## Problem 5B.

Score:

If $f ( z )$ is analytic in the open disc $\mathbb { D } = \{ z : | z | < 1 \}$ , and $\mathrm { i f } \ | f ( z ) | < 1 / ( 1 - | z | )$ for $\mathrm { a l l } ~ z \in \mathbb { D }$ show that

$$
\left| \frac { f ^ { ( n ) } ( 0 ) } { n ! } \right| \le ( n + 1 ) \left( 1 + \frac { 1 } { n } \right) ^ { n } < e ( n + 1 ) .
$$

Solution:

By Cauchy’s inequality with $r = n / ( n + 1 )$ , we have

$$
\left| { \frac { f ^ { ( n ) } ( 0 ) } { n ! } } \right| \leq { \frac { 1 / ( 1 - r ) } { r ^ { n } } } = { \frac { 1 } { 1 - { \frac { n } { n + 1 } } } } \left( { \frac { n + 1 } { n } } \right) ^ { n } = { \frac { n + 1 } { 1 } } \left( 1 + { \frac { 1 } { n } } \right) ^ { n } .
$$

To prove the last inequality, note that

$$
\left( 1 + { \frac { 1 } { n } } \right) ^ { n } < e \iff n \log \left( 1 + { \frac { 1 } { n } } \right) < 1 \iff \log \left( 1 + { \frac { 1 } { n } } \right) < { \frac { 1 } { n } }
$$

for all $n = 1 , 2 , 3 , \ldots$ . Letting $g ( x ) = \log ( 1 + x ) - x$ , we see that $g ( 0 ) = 0$ and $g ^ { \prime } ( x ) =$ $1 / ( 1 + x ) - 1 < 0$ for all $x > 0$ , therefore $g ( 1 / n ) < 0$ for all $n > 0$ as above. This proves the last inequality.

Score:

Let $\mathbb { Z } _ { 2 }$ be the ring of integers mod 2. Prove the following identity in $\mathbb { Z } _ { 2 } [ x _ { 1 } , \ldots , x _ { n } ]$

$$
\operatorname* { d e t } { \left[ \begin{array} { l l l } { x _ { 1 } } & { \ldots } & { x _ { n } } \\ { x _ { 1 } ^ { 2 } } & { \ldots } & { x _ { n } ^ { 2 } } \\ & { \ldots } & \\ { x _ { 1 } ^ { 2 n - 1 } } & { \ldots } & { x _ { n } ^ { 2 n - 1 } } \end{array} \right] } = \prod _ { ( a _ { 1 } , \ldots , a _ { n } ) \neq ( 0 , \ldots , 0 ) } ( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } ) ,
$$

where $\left( a _ { 1 } \ldots a _ { n } \right)$ run all non-zero values in $\mathbb { Z } _ { 2 } ^ { n }$

Solution: In $\mathbb { Z } _ { 2 } [ x _ { 1 } , \ldots , x _ { n } ]$ , we have for all $k = 0 , 1 , 2 , \ldots$

$$
\left( a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n } \right) ^ { 2 ^ { k } } = a _ { 1 } x _ { 1 } ^ { 2 ^ { k } } + \cdot \cdot \cdot + a _ { n } x _ { n } ^ { 2 ^ { k } } , \mathrm { ~ p r o v i d e d ~ t h a t ~ } a _ { i } \in \mathbb { Z } _ { 2 } .
$$

Therefore, given some $( a _ { 1 } , \ldots , a _ { n } ) \neq ( 0 , \ldots , 0 )$ , the linear combination of the columns with these coefficients yields a column divisible by the linear form $a _ { 1 } x _ { 1 } + \cdot \cdot \cdot + a _ { n } x _ { n }$ , thus showing that the whole determinant is divisible by it. (Indeed, if, say, $a _ { i } = 1$ , the ith column can be replaced by this linear combination without changing the determinant.) Notice that the determinant has the same degree $1 + 2 + \cdots + 2 ^ { n - 1 }$ as the number $2 ^ { n } - 1$ of non-zero linear forms. Since $\mathbb { Z } _ { 2 } [ x _ { 1 } , \ldots , x _ { n } ]$ is a UFD, with 1 being the only unit, and since non-zero linear forms are irreducible, we conclude that the determinant on the LHS is divisible by, and hence coincides with, the product on the RHS.

## Problem 7B.

Is it true that elements of the group $G L _ { 2 } ^ { + } ( \mathbb { R } )$ of real 2 × 2-matrices with positive determinant are conjugate in $G L _ { 2 } ^ { + } ( \mathbb { R } )$ if and only if the matrices are similar (conjugate in $G L _ { 2 } ( \mathbb { R } ) ) ?$ Either prove this or give a counterexample.

## Solution:

Solution. No. The rotations of the plane through the same angle $0 ~ < ~ \theta ~ < ~ \pi$ in clockwise and in counter-clockwise directions are similar (i.e. conjugated in $G L _ { 2 } ( \mathbb { R } ) )$ , but not conjugated in $G L _ { 2 } ^ { + } ( \mathbb { R } )$ since the latter group consists of orientation-preserving linear transformations of the plane.

## Problem 8B.

Score:

Let R be a ring (possibly non-commutative, possibly without an identity 1) in which every element is idempotent (this means that for all $a \in R , a ^ { 2 } = a )$ . Show that R has characteristic 2 (2a = 0 for all a) and is commutative.

## Solution:

Let a and b be elements of R.

To see that R has characteristic 2, consider $( a + a ) ^ { 2 } = a ( a + a ) + a ( a + a ) = a ^ { 2 } + a ^ { 2 } + a ^ { 2 } + a ^ { 2 } =$ 4a. Since $( a + a ) ^ { 2 } = a + a .$ , 4a = 2a and hence $2 a = 0 .$

To see that R is commutative, consider $( a + b ) ^ { 2 } = a ( a + b ) + b ( a + b ) = a ^ { 2 } + a b + b a + b ^ { 2 }$ Since $a ^ { 2 } = a , b ^ { 2 } = b$ and $( a + b ) ^ { 2 } = ( a + b ) , a + b = a + a b + b a + b . \mathrm { T h u s } , 0 = a b + b a$ . Since 2ba = 0, 2ba = ab + ba and hence ba = ab.

## Problem 9B.

Recall that $S _ { 6 }$ and $A _ { 6 }$ are the symmetric group and alternating group on 6 letters, respectively.

Prove or give a counterexample (with explanation): For every $\sigma \in A _ { 6 }$ there is ${ \mathrm { ~ a ~ } } \tau \in S _ { 6 }$ such that $\tau ^ { 2 } = \sigma$

Solution:

Counterexample. Let

$$
\sigma = ( 1 2 3 4 ) ( 5 6 ) .
$$

and assume that $\sigma = \tau ^ { 2 }$ for some $\tau \in S _ { 6 }$ What are the orbits of $\tau ?$ Since {1, 2, 3, 4} and {5, 6} are the orbits of $\sigma .$ , the orbits of τ would have to either be these two sets, or they would have to be one orbit. The former is not true, because (5 6) is not the square of a permutation of the elements {5, 6}. The latter is not true, because then τ would have to be a 6-cycle $( a b c d e f )$ , but $( a b c d e f ) ^ { 2 } = ( a c e ) ( b d f )$ does not contain a transposition.