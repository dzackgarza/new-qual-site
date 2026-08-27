## Problem 1A.

Score:

Find the real values of x for which

$$
\sum _ { n = 0 } ^ { \infty } { \frac { ( 1 / 2 ) ( 3 / 2 ) \cdots ( ( 2 n - 1 ) / 2 ) } { n ! } } ( { \frac { 2 x } { 1 + x ^ { 2 } } } ) ^ { 2 n } = 1 + { \frac { 1 } { 2 } } { \bigl ( } { \frac { 2 x } { 1 + x ^ { 2 } } } { \bigr ) } ^ { 2 } + { \frac { 1 } { 2 } } { \frac { 3 } { 4 } } { \bigl ( } { \frac { 2 x } { 1 + x ^ { 2 } } } { \bigr ) } ^ { 4 } + \cdots
$$

converges and sum it for these numbers. Caution: there is something unusual about the sum of this series.

Solution: The series converges for $| x | \neq 1$ . The sum is $( 1 + x ^ { 2 } ) / | ( 1 - x ^ { 2 } ) |$

## Problem 2A.

Score:

Show that there is a real-valued function on the real plane that is not continuous, but is continuous when restricted to any straight line.

Solution: Take the function to be 0 if $y \le 0$ or $y \ge 2 x ^ { 2 }$ , and 1 if $y = x ^ { 2 } \neq 0$ , and extend it to be continuous on the plane except at the origin.

## Problem 3A.

Score:

Let $f ( x )$ be differentiable on an interval $( a , b )$

(a) Prove that if X is the range of $( f ( u ) - f ( v ) ) / ( u - v )$ for $a < u < v < b$ and Y is the range of $f ^ { \prime } ( x )$ on (a, b) then $X \subseteq Y \subseteq { \overline { { X } } }$

(b) Prove that the range of $f ^ { \prime } ( x )$ on $( a , b )$ is an interval (possibly unbounded). Do not assume that $f ^ { \prime } ( x )$ is continuous.

Solution: Let $m ( u , v ) = ( f ( u ) - f ( v ) ) / ( u - v )$ . The definition of derivative implies that $f ^ { \prime } ( x ) = \dim _ { v \to x ^ { + } } m ( x , v )$ , and hence that the range Y of $f ^ { \prime } ( x )$ is contained in the closure X of the range X of m. The Mean Value Theorem implies that X is contained in Y . For part (b), since f (x) is differentiable, it is continuous, so m is continuous in both variables. The set of pairs $( u , v )$ such that $a < u < v < b$ is connected, hence the range X of m is connected, i.e., an interval. Then $X \subseteq Y \subseteq { \overline { { X } } }$ implies that Y is also an interval.

Let $S = \mathbb { C } \cup \{ \infty \}$ be the Riemann sphere. Let $\phi \colon \mathbb { C } ^ { 2 } \setminus \{ ( 0 , 0 ) \}  S$ be the map defined by $\phi ( w , z ) = w / z \mathrm { ~ f o r ~ } z \neq 0 , \phi ( w , 0 ) = \infty$

(a) Prove that there is a unique map $\tau \colon S  S$ with the following property: $\begin{array} { r l } { \tau ( \phi ( w , z ) ) = } \end{array}$ $\phi ( w ^ { \prime } , z ^ { \prime } )$ if and only if the one-dimensional subspaces $\mathbb { C } \cdot ( w , z )$ and $\mathbb { C } \cdot ( w ^ { \prime } , z ^ { \prime } )$ are orthogonal under the standard Hermitian inner product on $\mathbb { C } ^ { 2 }$ in which the unit vectors (1, 0) and (0, 1) are orthonormal.

(b) Prove that $\tau$ is continuous and bijective.

(c) Determine, with proof, whether $\tau$ is holomorphic or not.

Solution: Extending $1 / z$ as usual to a holomorphic map on S, the inner product $w \overline { { w ^ { \prime } } } + z \overline { { z ^ { \prime } } }$ vanishes if and only if $\phi ( w , z ) = - \overline { { 1 / \phi ( w ^ { \prime } , z ^ { \prime } ) } }$ . Hence the unique function with the property in $\mathrm { ( a ) }$ is $\tau ( z ) = - { \overline { { 1 / z } } }$ For (b) and (c), it is clear from the formula that $\tau$ is continuous, bijective, and not holomorphic.

Problem 5A.

Score:

(a) Suppose z, $c _ { 1 } , \ldots , c _ { n }$ are distinct complex numbers, and

$$
{ \frac { 1 } { z - c _ { 1 } } } + \cdots + { \frac { 1 } { z - c _ { n } } } = 0 .
$$

Show that z lies in the convex hull of $c _ { 1 } , \ldots , c _ { n } .$

(b) Let $p ( z )$ be a non-constant polynomial. Show that every zero of $p ^ { \prime } ( z )$ lies in the convex hull of the zeroes of $p ( z )$

Solution: For $\mathrm { ( a ) }$ , suppose the contrary. Adding a constant to z and the $c _ { i }$ and multiplying by another constant, we can assume that $z = 0$ and all the $c _ { i }$ lie in the half-plane $\mathrm { R e } ( w ) > 0$ But then all the numbers $1 / ( z - c _ { i } )$ also lie in this half-plane, so their sum cannot be zero.

For (b), let $c _ { 1 } , \ldots , c _ { n }$ be the zeroes of $p ( z )$ . We can assume that $p ( z ) = ( z - c _ { 1 } ) \cdot \cdot \cdot ( z - c _ { n } )$ Then $p ^ { \prime } ( z ) = p ( z ) ( 1 / ( z - c _ { 1 } ) + \cdot \cdot \cdot + 1 / ( z - c _ { n } ) )$ . When $p ^ { \prime } ( z ) = 0 .$ , this implies z is in the convex hull of the $c _ { i } ,$ by part (a).

## Problem 6A.

Score:

In the Euclidean space $\mathbb { R } ^ { 4 }$ , consider the “hyper-ellipsoid” $2 x ^ { 2 } + 3 y ^ { 2 } + 4 z ^ { 2 } + 5 u ^ { 2 } = 1$ . Does there exist a 3-dimensional subspace passing through the origin which intersects the ellipsoid in a sphere?

Solution: The answer is $^ { 6 } \mathrm { n o } ^ { \dag }$ : A 3-dimensional subspace will intersect the plane $x = y =$ 0 in a subspace of dimension $\geq 1$ , and therefore it will contain a point from the ellipse $4 z ^ { 2 } + 5 u ^ { 2 } = 1$ , all of whose points lie $\leq 1 / 2$ away from the origin. Likewise, the same 3-dimensional section will contain another point, from ellipse $2 x ^ { 2 } + 3 y ^ { 3 } = 1$ (in the plane $z = u = 0 )$ , all of whose points lie $> 1 / 2$ away from the origin. Thus, the section is not a sphere.

Problem 7A.

Score:

It is a corollary to the Jordan canonical form theorem that n×n matrices in Jordan canonical form, all of whose eigenvalues are zeroes, are similar if and only if the sizes of their Jordan blocks coincide (up to permutations). Prove this directly, without using the Jordan canonical form theorem.

Solution: A permutation of coordinates is a similarity transformation, so in one direction the statement is obvious. In the other direction, record the sizes $n _ { 1 } \geq n _ { 2 } \geq \cdot \cdot \cdot \geq n _ { k }$ of the Jordan blocks of a given nilpotent Jordan matrix N in decreasing order, and express the resulting partition of $n = n _ { 1 } + n _ { 2 } + \cdot \cdot \cdot + n _ { k }$ by the Young diagram with k rows of lengths $n _ { 1 } , n _ { 2 } , \ldots , n _ { k }$ . Then the sizes $m _ { 1 } \ge m _ { 2 } \ge \cdot \cdot \cdot \ge m _ { l }$ of columns of this diagram are determined by $m _ { i } =$ dim Ker N i−dim Ker $N ^ { i - 1 }$ . Thus, the partition $n = m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { l }$ is determined by the similarity class of the operator N , and so is the partition $n = n _ { 1 } + n _ { 2 } + \cdot \cdot \cdot + n _ { k }$ dual to it.

Problem 8A.

Score:

Find all the subgroups of the dihedral group of order 12 (the group of symmetries of a regular hexagon).

Solution: There is 1 subgroup of order 1, 7 of order 2 (1 generated by a rotation, 6 by reflections), 1 of order 3, 3 of order 4, 3 of order 6, 1 of order 12.

## Problem 9A.

Score:

Show that $x ^ { 3 } - 2 x$ is an injective function from the rational numbers to the rational numbers.

Solution: We have to show that if $x ^ { 3 } - 2 x = y ^ { 3 } - 2 y$ then $x = y .$ Factoring out $x - y$ we have to show that $x ^ { 2 } + x y + y ^ { 2 } = 2$ has no solutions in rational numbers, or equivalently that there is no nonzero solution of $x ^ { 2 } + x y + y ^ { 2 } = 2 z ^ { 2 }$ in integers. However looking at this mod 2 shows that x and y must be even, so z must also be even. A smallest nonzero solution must have at least one of them odd otherwise we could divide by 2. So there is no nonzero solution (mod 3 also works).

For a real, find a 2-dimensional space of real-valued solutions of $y ^ { \prime \prime } = a y / x ^ { 2 }$ for $x > 0$ . When $a = - 1 / 4$ find the solution with $y = 0 , y ^ { \prime } = 1 \mathrm { ~ a t ~ } x = 1$

Solution: If $a > - 1 / 4 ,$ two independent solutions are $y = x ^ { \lambda }$ for $( \lambda - 1 / 2 ) ^ { 2 } = a + 1 / 4$ If $a < - 1 / 4$ , since $\lambda = 1 / 2 \pm i \tau$ , where $\tau = \sqrt { - 1 / 4 - a }$ , the solutions $y = x ^ { \lambda }$ are complex. Two independent real solutions in this case are $y = x ^ { 1 / 2 } \cos ( \tau \log x )$ and $y = x ^ { 1 / 2 } \sin ( \tau \log x )$ If $a = - 1 / 4 , y = x ^ { \lambda } = x ^ { 1 / 2 }$ is one solution. A second solution is $y = x ^ { 1 / 2 }$ log x (which solves the given initial conditions).

## Problem 2B.

Score:

Let $f \colon [ 0 , \infty )  \mathbb { R }$ be a function, and assume that:

• f is continuous on $[ 0 , \infty )$

• f is differentiable on $( 0 , \infty )$

$f ^ { \prime } ( x ) \leq 0$ for all $x > 0$ such that $f ( x ) > 1 ;$ and

$f ( 0 ) = 1 .$

Prove that $f ( x ) \leq 1$ for all $x \ge 0 .$

Solution: The set $\{ x \in [ 0 , \infty ) : f ( x ) > 1 \}$ is an open subset of $[ 0 , \infty )$ , and does not contain 0, so it is an open subset of R. Assume that this set is nonempty. Since it is open, it is a disjoint union of open intervals. Let $( a , b )$ be one such interval; note that $a \geq 0 . \mathrm { B y }$ continuity, $f ( a ) = 1$ . The third assumption implies that $f ( x )$ is non-increasing on $[ a , b )$ , which contradicts the fact that $f ( c ) > 1$ for $c \in ( a , b )$ . Thus the given set is empty, and so the conclusion follows.

## Problem 3B.

Score:

The unit cube in the space $C [ 0 , 1 ]$ of continuous real-valued functions on the interval is defined as the subset

$$
\{ f \in C [ 0 , 1 ] \mid \| f \| : = \operatorname* { s u p } _ { 0 \leq t \leq 1 } | f ( t ) | \leq 1 \} .
$$

Prove that there exists a 2-dimensional linear subspace in $C [ 0 , 1 ]$ whose intersection with the unit cube is a circular disk.

Solution: Take the plane spanned by cos 2πt, sin 2πt.

A Schur function is a non-constant holomorphic function defined in the open unit disk whose values have absolute value at most 1. Show that if f is a Schur function then

$$
\frac { f ( 0 ) - f ( z ) } { ( 1 - { \overline { { f ( 0 ) } } } f ( z ) ) z }
$$

is also a Schur function.

Solution: We must have $f ( 0 ) < 1$ , as f would be constant otherwise. $\mathrm { I f } \ | a | < 1$ , then $( a - b ) / ( 1 - \overline { { a } } b )$ has absolute value at most 1 for $| b | < 1$ by the maximum principle, because it has absolute value 1 for $| b | = 1$ . The function $\frac { { \dot { f } } ( 0 ) - f ( z ) } { ( 1 - { \overline { { f ( 0 ) } } } f ( z ) ) }$ has absolute value at most 1 in the open unit disk and vanishes at $z = 0$ , so we can divide it by z and the quotient still has absolute value at most 1 by the maximum principle (applied to circles approaching the unit circle).

Correction: As some students noticed, the problem as stated is incorrect, because the non-constant function $f ( z ) = z$ leads to a constant function

$$
g ( z ) = \frac { f ( 0 ) - f ( z ) } { ( 1 - \overline { { f ( 0 ) } } f ( z ) ) z } = - 1 .
$$

One cannot drop the “non-constant” hypothesis, since $g ( z )$ is undefined if $f ( z )$ is constant with absolute value 1. The problem should have been formulated as follows.

A Schur function is a holomorphic function defined in the open unit disk whose values have absolute value at most 1. Show that if f is a non-constant Schur function then

$$
\frac { f ( 0 ) - f ( z ) } { ( 1 - { \overline { { f ( 0 ) } } } f ( z ) ) z }
$$

is also a Schur function.

To be fair, answers were only graded on whether the student showed that $g ( z )$ is well-defined and holomorphic with $| g ( z ) | \leq 1$ on the disk. No marks were deducted for failing to show that $g ( z )$ is non-constant.

## Problem 5B.

Score:

Find all entire functions $f ( z )$ such that $\ell ( f ( x + i y ) ) = x ^ { 3 } y - x y ^ { 3 }$ . Express your answer directly in terms of z, not in terms of x and y.

Solution: $f ( z ) = - i z ^ { 4 } / 4 + C i$ , where C is a real number.

Given a positive integer n, let $\dots c _ { - 1 } , c _ { 0 } , c _ { 1 } , \dots c _ { - }$ be a sequence of real numbers with period $n ,$ that is, $c _ { k + n } = c _ { k }$ for all $k \in \mathbf { Z }$ . Let C be the $n \times n { \mathrm { - m a t r i x } }$ defined by $c _ { i j } = c _ { j - i }$ . Prove that all matrices of this form (for n fixed) have a common Hermitian-orthonormal basis of complex eigenvectors, find these eigenvectors, and the corresponding eigenvalues.

Solution: Let $T$ denote the cyclic shift operator $T ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = ( x _ { 2 } , \ldots , x _ { n } , x _ { 1 } )$ on $\mathbb { R } ^ { n }$ Then C is the matrix of the operator $c _ { 0 } + c _ { 1 } T + c _ { 2 } T ^ { 2 } + \cdot \cdot \cdot + c _ { n - 1 } T ^ { n }$ . Since T is orthogonal, it commutes with its adjoint $T ^ { * } = T ^ { - 1 }$ , and hence $T$ is normal. By the Spectral Theorem for normal operators, T has an Hermitian-orthonormal basis of complex eigenvectors. Explicitly, the eigenvectors of T have the form $( 1 , \lambda , \lambda ^ { 2 } , \dots , \lambda ^ { n - 1 } )$ , where λ is the corresponding eigenvalue, satisfying $\lambda ^ { n } = 1$ . The eigenvalues are all distinct, and hence the eigenvectors are pairwise Hermitian-orthogonal. Dividing by $\sqrt { n }$ makes them unit. The corresponding eigenvalues of C are $c _ { 0 } + c _ { 1 } \lambda + \cdot \cdot \cdot + c _ { n - 1 } \lambda ^ { n - 1 }$ where λ runs through the nth roots of unity: $\lambda = \exp ( 2 \pi i k / n ) , k = 0 , 1 , \ldots , n - 1$

Problem 7B.

Score:

Find the number of surjective linear maps from an n-dimensional vector space over the field with 2 elements to itself.

Solution: $( 2 ^ { n } - 1 ) ( 2 ^ { n } - 2 ^ { 1 } ) \cdot \cdot \cdot ( 2 ^ { n } - 2 ^ { n - 1 } )$

## Problem 8B.

Score:

If A is the ring of $n \times n$ matrices with entries in a field K, show that the only two-sided ideals of A are A itself and 0.

Solution: Let J be the two-sided ideal generated by a non-zero matrix $M \in A$ . Let $v \in K ^ { n }$ be a vector such that $w = M v \neq 0$ . Let Y be the matrix such that $Y e _ { 1 } = v$ and $Y e _ { j } = 0$ for $j > 1$ , where $e _ { j }$ is the j-th unit vector. Let X be a matrix such that $X w = e _ { 1 }$ . Then $X M Y$ is the unit matrix $E _ { 1 , 1 }$ with entry 1 in position (1, 1) and all other entries zero, so $E _ { 1 , 1 } \in J$ Similarly, every unit matrix $E _ { i , j }$ belongs to J, hence $J = A$

Score:

How many ways are there to arrange 8 rooks on an 8 by 8 chessboard so that no two attack each other (in other words, each row and column contains exactly one rook), where two ways are counted as the same if they are equivalent under one of the 8 symmetries of the chessboard? You may assume the Polya–Burnside theorem that the number of orbits of a finite group on a finite set is the average number of fixed points of elements of the group.

Solution: Use Polya–Burnside formula. Count the number of fixed points for each of the 8 symmetries acting on the 8! arrangements of non-attacking rooks, as follows. Identity: $8 ! = 4 0 3 2 0$ . Two reflections in a vertical or horizontal line: 0. Two reflections in a diagonal line: $1 + 8 \cdot 7 / 2 + 8 \cdot 7 \cdot 6 \cdot 5 / 2 ^ { 2 } \cdot 2 + 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 / 2 ^ { 3 } \cdot 3 ! + 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 / 2 ^ { 4 } \cdot 4 ! = 7 7 4$ Two 90-degree rotations: $6 \cdot 2 = 1 2$ One 180-degree rotation: $8 \cdot 6 \cdot 4 \cdot 2 = 3 8 4$ . Total $( 4 0 3 2 0 + 2 \cdot 0 + 2 \cdot 7 7 4 + 2 \cdot 1 2 + 1 \cdot 3 8 4 ) / 8 = 5 2 8 2$