# Department of Mathematics, University of California, Berkeley

Spring Semester 2015

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q .$

4. No notes, books, or calculators may be used during the exam.

## PROBLEM SELECTION

Part A: List the six problems you have chosen:

## GRADE COMPUTATION

1A.

1B.

Calculus

2A.

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

Please cross out this problem if you do not wish it graded

## Problem 1A.

Score:

(a) Evaluate the integral

$$
\int _ { 0 } ^ { 1 } { \frac { x ^ { 4 } ( 1 - x ) ^ { 4 } } { 1 + x ^ { 2 } } } d x
$$

(b) Prove that $\textstyle 0 < { \frac { 2 2 } { 7 } } - \pi < { \frac { 1 } { 2 5 6 } }$

Solution: (a) The integral is $\begin{array} { r } { \int _ { 0 } ^ { 1 } x ^ { 6 } - 4 x ^ { 5 } + 5 x ^ { 4 } - 4 x ^ { 2 } + 4 - \frac { 4 } { 1 + x ^ { 2 } } d x = \frac { 2 2 } { 7 } - \pi } \end{array}$ (b) This follows because the integrand is between 0 and 1/256.

Please cross out this problem if you do not wish it graded

<table><tr><td></td></tr><tr><td>Problem 2A. Score:</td></tr></table>

Suppose that g is a (not necessarily continuous) positive real valued function of a real number. If $a < b$ are real numbers, show that there is a finite sequence $a = t _ { 0 } < t _ { 1 } < \cdot \cdot \cdot < t _ { n } = b$ of real numbers such that in each interval $[ t _ { k } , t _ { k + 1 } ]$ there is a point where the value of the function g is greater than the length of the interval.

Solution: For fixed a, let B be the infimum of the numbers b such that the result is not true, if any such numbers b exist. If a suitable sequence exists for b then one also exists for every b0 in $( a , b )$ , so if the result does not hold then it fails for every $b > B$ . B must be bigger than a as we can take a small interval of length less than $g ( a )$ around a. Take a small interval [x, y] of size less than $g ( B )$ with B in the interior. Choose a finite sequence $a = t _ { 0 } < t _ { 1 } < \cdot \cdot \cdot < t _ { n } = x$ of numbers satisfying the condition above. Then adding $t _ { n + 1 } = y$ to the sequence gives a sequence for some $b = y > B$ , contradicting the assumption that B is the inf of numbers without such a sequence.

Please cross out this problem if you do not wish it graded

## Problem 3A.

Score:

(a) Describe all sets of reals that can be the image of the real line under a polynomial with real coefficients.

(b) Find the image of the real plane under the polynomial $x ^ { 2 } + ( x y - 1 ) ^ { 2 }$

(c) Describe all sets of reals that can be the image of the real plane under a polynomial in 2 variables with real coefficients.

Solution: (a) The image is a point for a constant, the whole real line for odd degree, and a closed half line for positive even degree. (b) The polynomial $x ^ { 2 } + ( x y - 1 ) ^ { 2 }$ is always positive, but takes arbitrarily small positive values at points $( x , 1 / x )$ , so the image of the real plane is the positive real line. (c) As well as the examples in (a), all open half lines can also be images of polynomials by (b). These are the only possibilities because the image is connected, and unbounded if the polynomial is not constant.

Please cross out this problem if you do not wish it graded

## Problem 4A.

Score:

Write two different Laurent series in powers of the complex variable z for the function

$$
f ( z ) = { \frac { 1 } { z ( 1 + z ^ { 2 } ) } } .
$$

Give the domain of each of these series.

Solution: The denominator has roots at $z = 0$ and $z = \pm i ,$ so we want to look for Laurent series in the domains $0 < | z | < 1$ and $| z | > 1$

For $0 < | z | < 1$ , we can use the geometric series

$$
{ \frac { 1 } { 1 + z ^ { 2 } } } = 1 - z ^ { 2 } + z ^ { 4 } - \cdot \cdot \cdot = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } z ^ { 2 n } \ , \qquad | z | < 1
$$

to obtain

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } z ^ { 2 n - 1 } , \quad 0 < | z | < 1 .
$$

For $| z | > 1$ , we similarly use

$$
\frac 1 { 1 + ( 1 / z ^ { 2 } ) } = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } z ^ { - 2 n } , | 1 / z | < 1
$$

to obtain

$$
f ( z ) = { \frac { 1 } { z ^ { 3 } } } \left( { \frac { 1 } { 1 + ( 1 / z ^ { 2 } ) } } \right) = { \frac { 1 } { z ^ { 3 } } } \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } z ^ { - 2 n } = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } } { z ^ { 2 n + 3 } } } \ , \qquad | z | > 1 \ .
$$

Please cross out this problem if you do not wish it graded

## Problem 5A.

Score:

Compute the difference

$$
\int _ { | z | = 3 } { \frac { e ^ { \pi / z } d z } { z ^ { 2 } + 4 } } - \int _ { | z | = 1 } { \frac { e ^ { \pi / z } d z } { z ^ { 2 } + 4 } } \ ,
$$

where both integrals are taken in the counter-clockwise direction.

Solution: The function has simple poles at $z = \pm 2 i$ and also a singularity at $z = 0$ . The residue at $z = 0$ cancels out in the difference, so we only need to compute the residues of the function at $z = 2 i$ and $z = - 2 i$ . Therefore, the answer is

$$
\begin{array} { r l } & { \textstyle 2 \pi i \frac { \mathrm { R e s } } { z = 2 i } \frac { e ^ { \pi / z } } { z ^ { 2 } + 4 } + 2 \pi i \frac { \mathrm { R e s } } { z = - 2 i } \frac { e ^ { \pi / z } } { z ^ { 2 } + 4 } = 2 \pi i \left( \frac { e ^ { \pi / ( 2 i ) } } { 4 i } + \frac { e ^ { - \pi / ( 2 i ) } } { - 4 i } \right) } \\ & { \textstyle \qquad = \frac { \pi } { 2 } \left( e ^ { - ( \pi / 2 ) i } - e ^ { ( \pi / 2 ) i } \right) } \\ & { \textstyle \qquad = \frac { \pi } { 2 } \left( \cos \frac { - \pi } { 2 } + i \sin \frac { - \pi } { 2 } - \cos \frac { \pi } { 2 } - i \sin \frac { \pi } { 2 } \right) } \\ & { \textstyle \qquad = \frac { \pi } { 2 } ( - i - i ) } \\ & { \textstyle \qquad = - i \pi . } \end{array}
$$

Please cross out this problem if you do not wish it graded

Problem 6A.

Score:

Fix $N \geq 1$ . Let $\boldsymbol s = ( s _ { 1 } , \ldots , s _ { N } )$ and $t = ( t _ { 1 } , \ldots , t _ { N } )$ be 2N distinct complex numbers. Define the $N \times N$ matrices C(t, s), P (t, s) and $Q ( s )$ with P and Q diagonal to have entries

$$
C ( t , s ) _ { i j } = \frac { 1 } { t _ { i } - s _ { j } } , \qquad P ( t , s ) _ { i i } = \prod _ { k = 1 } ^ { N } ( t _ { i } - s _ { k } ) , \qquad Q ( s ) _ { j j } = \prod _ { k \neq j } \frac { 1 } { s _ { j } - s _ { k } }
$$

Show that $p ( t ) = P ( t , s ) C ( t , s ) Q ( s ) p ( s )$ , where $p$ is any polynomial of degree less than $N$ and for a vector $r = ( r _ { 1 } , \ldots , r _ { N } ) , p ( r )$ is defined to be the vector $( p ( r _ { 1 } ) , . . . , p ( r _ { N } ) )$ .

Solution:

Expanding out

$$
p ( t ) = P ( t , s ) C ( t , s ) Q ( s ) p ( s )
$$

becomes

$$
p ( t _ { i } ) = \left( \prod _ { k = 1 } ^ { N } ( t _ { i } - s _ { k } ) \right) \sum _ { j = 1 } ^ { N } \frac { 1 } { t _ { i } - s _ { j } } \left( \prod _ { k \neq j } \frac { 1 } { s _ { j } - s _ { k } } \right) p ( s _ { j } ) .
$$

This holds because each side is a polynomial in $t _ { i }$ of degree less than $N$ , and both sides are equal for the N values $s _ { j }$

Remark: This is a matrix form of the Lagrange interpolation formula.

Please cross out this problem if you do not wish it graded

<table><tr><td colspan="6">Problem 7A. Score:</td></tr><tr><td> $\Delta _ { n } = \left| \begin{array} { c c c c c c } { { { \binom { 0 } { 0 } } } } & { { { \binom { 1 } { 0 } } } } & { { { \binom { 2 } { 0 } } } } & { { \ldots } } & { { { \binom { n - 1 } { 0 } } } } \\ { { { \binom { 1 } { 1 } } } } & { { { \binom { 2 } { 1 } } } } & { { { \binom { 3 } { 1 } } } } & { { \ldots } } & { { { \binom { n } { 1 } } } } \\ { { { \binom { 2 } { 2 } } } } & { { { \binom { 3 } { 2 } } } } & { { { \binom { 4 } { 2 } } } } & { { \ldots } } & { { { \binom { n + 1 } { 2 } } } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { { \binom { n - 1 } { n - 1 } } } } & { { { \binom { n } { n - 1 } } } } & { { { \binom { n + 1 } { n - 1 } } } } & { { \ldots } } & { { { \binom { 2 n - 2 } { n - 1 } } } } \end{array} \right| .$  Compute the determinant</td><td></td><td></td><td></td><td></td></tr></table>

Solution: Due to the defining property $\textstyle { \binom { k + 1 } { l } } = { \binom { k } { l } } + { \binom { k } { l - 1 } }$ , each matrix entry is the sum of the one above it and the one on the left of it. Therefore, if we consecutively subtract column $n - 1$ from column $n ,$ then column $n - 2$ from column $n - 1$ , etc., the resulting n × n-matrix will have the first row $( 1 , 0 , 0 , \ldots , 0 )$ , and rows 2, 3, . . . equal respectively rows $1 , 2 , \ldots$ . of the original matrix. Therefore, if we consecutively subtract row $n - 1$ from row n, row $n - 2$ from row $n - 1 , \ . . .$ , row 1 from row 2, the resulting matrix will have 1 in the left upper corner, all other entries in row 1 and column 1 equal 0, and the remaining $( n - 1 ) \times ( n - 1 )$ matrix the same as the original one with n replaced by $n - 1$ . Since the row / column operations don’t change the determinant, we conclude from the cofactor expansion that $\Delta _ { n } = \Delta _ { n - 1 }$ , and hence (by induction) that $\Delta _ { n } = \Delta _ { 1 } = 1$ .

## YOUR EXAM NUMBER

Please cross out this problem if you do not wish it graded

## Problem 8A.

Score:

Factor the polynomial

$$
1 1 x ^ { 5 } - 1 1 x ^ { 4 } + 1 4 x ^ { 2 } - 2 1 x + 7
$$

into irreducible polynomials in $\mathbb { Q } [ x ]$

Solution: The only possible rational roots of this polynomial $\operatorname { a r e } \pm 1 , \pm 7 , \pm 1 / 1 1$ , and $\pm 7 / 1 1$ . We notice that 1 is a rational root, so we can factor out $x - 1$ and get

$$
( x - 1 ) ( 1 1 x ^ { 4 } + 1 4 x - 7 ) .
$$

The factor $x - 1$ is irreducible because it is linear. The second factor is irreducible by Eisenstein’s criterion with $p = 7$ . Therefore this is the factorization of the polynomial into irreducible factors.

Score:

Find (with proof) a product of cyclic groups that is isomorphic to the group

$$
( \mathbb { Z } _ { 1 2 } \times \mathbb { Z } _ { 1 2 } ) / \langle ( 2 , 6 ) \rangle
$$

(Here $\mathbb { Z } _ { n }$ means $\mathbb { Z } / n \mathbb { Z } . )$

Solution: Let $G = \mathbb { Z } _ { 1 2 } \times \mathbb { Z } _ { 1 2 }$ , and let H be the cyclic subgroup h(2, 6)i. Since $| G | = 1 2 ^ { 2 }$ and $\vert H \vert = \mathrm { l c m } ( 6 , 2 ) = 6 , G / H$ has order 24.

Also, $G / H$ is abelian, so it must be one of the groups

$$
\mathbb { Z } _ { 2 4 } \ , \qquad \mathbb { Z } _ { 1 2 } \times \mathbb { Z } _ { 2 } \ , \qquad \mathrm { o r } \qquad \mathbb { Z } _ { 6 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 } \ .
$$

Since G has no elements of order $> 1 2 .$ , neither does $G / H , \mathrm { { s o } } \ G / H \not \cong \mathbb { Z } _ { 2 4 }$ . The elements of H are $( 0 , 0 ) , ( 2 , 6 ) , ( 4 , 0 ) , ( 6 , 6 ) , ( 8 , 0 )$ , and (10, 6). Therefore $( 1 , 0 ) + H$ has order 4, so $G / H \not \cong \mathbb { Z } _ { 6 } \times \mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 }$

Thus $G / H \cong \mathbb { Z } _ { 1 2 } \times \mathbb { Z } _ { 2 }$

Another way to solve the problem is to reduce the matrix with columns (12, 0), (0, 12) and (2,6) to Smith canonical form.

## GRADUATE PRELIMINARY EXAMINATION, Part B

Spring Semester 2015

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q$

4. No notes, books, or calculators may be used during the exam.

## PROBLEM SELECTION

Part B: List the six problems you have chosen:

## YOUR EXAM NUMBER

Please cross out this problem if you do not wish it graded

## Problem 1B.

Score:

For all integers $n > 2$ prove the inequality

$$
{ \frac { n ^ { n } } { e ^ { n - 1 } } } < n ! < { \frac { ( n + 1 ) ^ { n + 1 } } { e ^ { n } } }
$$

Solution: Take the logarithm. Then the inequality becomes

$$
n \log ( n ) - n + 1 < \sum _ { k = 1 } ^ { n } \log ( k ) < ( n + 1 ) \log ( n + 1 ) - n .
$$

Since $y = \log ( x )$ is an increasing function on the interval $x > 1$ , we have

$$
\int _ { 1 } ^ { n } \log ( x ) d x < \sum _ { k = 1 } ^ { n } \log ( k ) < \int _ { 1 } ^ { n + 1 } \log ( x ) d x .
$$

We have

$$
\int \log ( x ) d x = x \log ( x ) - x + C , \quad \int _ { 1 } ^ { n } \log ( x ) d x = n \log ( n ) - n + 1 , \quad \int _ { 1 } ^ { n + 1 } d x = ( n + 1 ) \log ( n + 1 ) - n .
$$

<table><tr><td>Problem 2B. Score:</td></tr></table>

Find the maximum area of all triangles that can be inscribed in an ellipse with semiaxes a and b.

## Solution:

Change the ellipse to a circle using an affine transformation (that multiples all areas by a constant). This shows the max area is ab times the max area of a triangle in a circle of radius 1. The triangle of max area in a circle is an equilateral triangle of area√ $3 { \sqrt { 3 } } / 4$ , so the max area of a triangle in the ellipse is ab3 3/4.

YOUR EXAM NUMBER

Please cross out this problem if you do not wish it graded

<table><tr><td>Problem 3B. Score:</td></tr></table>

Suppose that $a _ { 1 , 1 } + a _ { 1 , 2 } + \cdots , \qquad a _ { 2 , 1 } + a _ { 2 , 2 } + \cdots . \nonumber$ , are a countable collection of convergent series of non-negative real numbers. Show that there is a convergent series $x _ { 1 } + x _ { 2 } + \cdots$ of real numbers converging more slowly than any of the given series in the sense that for any m we have $x _ { n } \geq a _ { m , n }$ for all sufficiently large n. (Hint: The problem is not affected by changing a finite number of terms of each of the given series.)

Solution: Change a finite number of terms of each series so that the sum of the mth series is at most $1 / 2 ^ { m }$ . Then take $\begin{array} { r } { x _ { n } = \sum _ { m } a _ { m , n } } \end{array}$

Please cross out this problem if you do not wish it graded

<table><tr><td>Problem 4B. Score:</td></tr></table>

Prove that there is no one-to-one conformal map from the punctured unit disk $\{ z : 0 < | z | <$ 1} onto the annulus $\{ z : 1 < | z | < 2 \}$

Solution: Any holomorphic function from the punctured unit disk to the annulus is bounded near 0, so can be extended to a function that is holomorphic at 0. In particular it has a square root as it is a nonzero holomorphic function on a simply connected region. However there is a holomorphic function from the annulus to itself without a square root (for example the identity function). So the punctured unit disc cannot be conformal to the annulus.

Please cross out this problem if you do not wish it graded

<table><tr><td>Problem 5B. Score:</td></tr></table>

Show that if $f : \mathbb { C } \to \mathbb { C } \cup \infty$ is a meromorphic function in the plane, such that there exists $R , C > 0$ so that for $| z | > R , | f ( z ) | \leq C | z | ^ { n }$ , then f is a rational function.

Solution: Since f is meromorphic, and $| f ( z ) | < \infty$ for $| z | > R ,$ , f must have only finitely many poles $a _ { 1 } , \ldots , a _ { m }$ (with multiplicity) in the disk $| z | \le R$ Let $g ( z ) = ( z - a _ { 1 } ) \cdot \cdot \cdot ( z -$ $a _ { m } ) f ( z )$ then $g ( z )$ is entire, and $| g ( z ) | \leq C ^ { \prime } | z | ^ { m + n }$ for |z| large enough, and therefore $g ( z )$ is a polynomial of degree a most $m + n$ , using Cauchy’s estimate $\vert f ^ { N } ( 0 ) \vert \le C ^ { \prime } r ^ { m + n } N ! r ^ { - N } \overset { , } { \to } 0$ as $r  \infty$ if $N > m + n$ . Thus, $f ( z ) = g ( z ) / ( ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { n } ) )$ must be a rational function.

Please cross out this problem if you do not wish it graded

## Problem 6B.

Score:

What is the maximal dimension of subspaces in $\mathbb { R } ^ { 4 }$ on which the quadratic form $x _ { 1 } x _ { 2 } - 3 x _ { 2 } ^ { 2 } +$ $x _ { 3 } ^ { 2 } + 2 x _ { 2 } x _ { 4 } + x _ { 4 } ^ { 2 }$ is positive definite?

Solution: By completing squares, the quadratic form can be rewritten as

$$
( x _ { 4 } + x _ { 2 } ) ^ { 2 } - ( 2 x _ { 2 } - { \frac { x _ { 1 } } { 4 } } ) ^ { 2 } + \left( { \frac { x _ { 1 } } { 4 } } \right) ^ { 2 } + x _ { 3 } ^ { 2 } ,
$$

i.e. as $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } - y _ { 3 } ^ { 3 } + y _ { 4 } ^ { 2 }$ , where $y _ { 1 } = x _ { 3 } , y _ { 2 } = x _ { 4 } + x _ { 2 } , y _ { 3 } = 2 x _ { 2 } - x _ { 1 } / 4$ , and $y _ { 4 } = x _ { 1 } / 4$ are new coordinates. Thus, the maximal dimension of the subspace on which the quadratic form is positive definite is 3 (= the positive inertia index of the form).

Please cross out this problem if you do not wish it graded

## Problem 7B.

Score:

Fix $N \geq 1$ . Let $s _ { 1 } , \ldots , s _ { N } , t _ { 1 } , \ldots , t _ { N }$ be 2N complex numbers of magnitude less than or equal to 1. Let A be the $N \times N$ matrix with entries

$$
A _ { i j } = \exp { ( t _ { i } s _ { j } ) } .
$$

Show that A can be approximated by matrices of small rank in the following sense: for any $m \geq 1$ the $N \times N$ matrix B with entries $\scriptstyle \sum _ { n = 0 } ^ { m - 1 } { \frac { ( t _ { i } s _ { j } ) ^ { n } } { n ! } }$ satisfies

$$
\vert A _ { i j } - B _ { i j } \vert \le \frac { 2 } { m ! }
$$

for all i and j and has rank at most m.

Solution: By Taylor expansion,

$$
| \exp ( z ) - \sum _ { n = 0 } ^ { m - 1 } { \frac { z ^ { n } } { n ! } } | \leq \sum _ { n = m } ^ { \infty } { \frac { 1 } { n ! } } \leq { \frac { 2 } { m ! } }
$$

whenever $| z | \leq 1$ . Hence

$$
B _ { i j } = \sum _ { n = 0 } ^ { m - 1 } \frac { ( t _ { i } s _ { j } ) ^ { n } } { n ! } = \sum _ { n = 0 } ^ { m - 1 } \frac { 1 } { n ! } t _ { i } ^ { n } s _ { j } ^ { n }
$$

gives the entries of a matrix B of rank less than or equal to m with

$$
\vert A _ { i j } - B _ { i j } \vert \leq \frac { 2 } { m ! } .
$$

The matrix B has rank at most m because all its rows are linear combinations of the m vectors $( t _ { 1 } ^ { i } , . . . , t _ { N } ^ { i } )$ for $i = 0 , . . . , m - 1$

Score:

Let p be a prime number and G be a group such that $g ^ { p } = 1$ for all $g \in G$ . Show that if $p { = } 2$ then G is abelian, and give an example with $p > 2$ where G is not abelian.

Solution: If $p = 2$ , this is true. Indeed, $( g h ) ^ { 2 } = 1$ implies $g h = h ^ { - 1 } g ^ { - 1 } = h g$

If p is odd, it is not true. Let G be the subgroup of $3 \times 3$ upper triangular matrices with entries in $\mathbb { Z } / p \mathbb { Z }$ and 1 on the main diagonal. For any $g \in G$ , we have $g = 1 + X$ where X is a nilpotent matrix. Then $X ^ { 3 } = 0$ . Therefore we have

$$
g ^ { p } = ( 1 + X ) ^ { p } = 1 + p X + \frac { p ( p - 1 ) } { 2 } X ^ { 2 } = 1 .
$$

On the other hand, if $g = { \left( \begin{array} { l l l } { 1 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) }$ and $h = { \left( \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) }$ , then $g h \neq h g$ . Thus, G is not abelian.

Please cross out this problem if you do not wish it graded

## Problem 9B.

Score:

Let p be a prime. Let $p ^ { a ( n ) }$ be the largest power of p dividing n! and let b(n) be the sum of the digits of n in base p.

(a) Show that $a ( n ) = [ n / p ] + [ n / p ^ { 2 } ] + [ n / p ^ { 3 } ] + \cdot \cdot$ · where [x] is the largest integer at most equal to x.

(b) Express $a ( n )$ in terms of the digits $d _ { k }$ of the base p expansion $n = \sum d _ { k } p ^ { k }$ of n (where $0 \leq d _ { k } < p )$

(c) Find a nontrivial linear relation between the functions $n , a ( n )$ and $b ( n )$ (with coefficients that may depend on p but do not depend on n).

Solution: (a) $\begin{array} { r } { a ( n ) = \sum _ { k } k { \times } ( \mathrm { n u m b e r } } \end{array}$ of integers at most n divisible by exactly k powers of $p )$ which is $\textstyle \sum _ { k }$ (number of integers at most n divisible by $p ^ { k } )$ which is the sum in the question.

$$
\begin{array} { r } { \mathrm { ( b ) } a ( n ) = \sum _ { k > 0 } ( d _ { k } + p d _ { k + 1 } + p ^ { 2 } d _ { k + 2 } + \cdot \cdot \cdot ) = \sum d _ { k } ( p ^ { k - 1 } + \cdot \cdot \cdot + p + 1 ) } \end{array}
$$

(c) $n = ( p - 1 ) a ( n ) + b ( n )$ . This follows from part b and the obvious expressions for n and a(n) in terms of the digits.