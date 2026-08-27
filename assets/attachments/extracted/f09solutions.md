Problem 1A.

Let $p ( k )$ be a degree n polynomial with complex coefficients defined by

$$
p ( k ) = p _ { 0 } + { \binom { k } { 1 } } p _ { 1 } + { \binom { k } { 2 } } p _ { 2 } + \cdot \cdot \cdot + { \binom { k } { n } } p _ { n } .
$$

Define

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } p ( k ) z ^ { k } .
$$

Find the radius of convergence of the power series, prove that $f ( z )$ is a rational function restricted to the disk of convergence, and give a formula for $f ( z )$

Solution: We have

$$
\left( \frac { d } { d z } \right) ^ { n } \frac { 1 } { 1 - z } = \frac { n ! } { ( 1 - z ) ^ { n + 1 } } .
$$

Since $\begin{array} { r } { \frac { 1 } { 1 - z } = \sum _ { k = 0 } ^ { \infty } z ^ { k } } \end{array}$ for $| z | < 1$ , we also have for $| z | < 1$

$$
{ \frac { n ! } { ( 1 - z ) ^ { n + 1 } } } = \left( { \frac { d } { d z } } \right) ^ { n } \sum _ { k = 0 } ^ { \infty } z ^ { k } = \sum _ { k = 0 } ^ { \infty } k ( k - 1 ) \cdot \cdot \cdot ( k - n + 1 ) z ^ { k - n } = { \frac { n ! } { ( 1 - z ) ^ { n + 1 } } } .
$$

We may rewrite this as

$$
{ \frac { z ^ { n } } { ( 1 - z ) ^ { n + 1 } } } = \sum _ { k = 0 } ^ { \infty } { \binom { k } { n } } z ^ { k } .
$$

Thus,

$$
f ( z ) = \sum _ { k = 0 } ^ { \infty } \sum _ { j = 0 } ^ { n } p _ { j } { \binom { k } { n } } z ^ { k } = \sum _ { j = 0 } ^ { n } p _ { j } \sum _ { k = 0 } ^ { \infty } { \binom { k } { n } } z ^ { k } = \sum _ { j = 0 } ^ { n } p _ { j } { \frac { z ^ { j } } { ( 1 - z ) ^ { j + 1 } } } ,
$$

which is a sum of rational functions, and is therefore rational. The series converges to this rational function in the disk $| z | < 1$ , and the rational function has a pole on its boundary at $z = 1$ (unless all $p _ { j } = 0 )$ . Thus the convergence radius $R = 1$ if not all $p _ { j } = 0$ (and $R = \infty$ otherwise).

## Problem 2A.

Prove that no polynomial $p ( a , b , c , d )$ in four variables over C has the property that when p is evaluated on the entries of a $2 \times 2$ matrix $A = { \bigg [ } { a b } { \bigg ] }$ , the result is an eigenvalue of A, for all A.

Solution 1: Assuming the opposite, we arrive at the absurd conclusion that $\sqrt { z }$ is a polynomial in z; namely $p ( 0 , z , 1 , 0 ) ^ { 2 } = z$ for all $z \in \mathbb { C }$

Solution 2: Suppose p always evaluates to an eigenvalue of A. Then $q = \operatorname { t r } ( A ) - p = a + d - p$ evaluates to the other eigenvalue, hence

$$
p q = \operatorname* { d e t } ( A ) = a d - b c .
$$

We claim that det(A) is an irreducible polynomial, and therefore either p or q must be constant, contradicting the eigenvalue property (note that q has the same property). One way to prove that $a d - b c$ is irreducible is as follows. Since ad − bc is homogeneous quadratic, its only possible factorization is as a product of linear forms $\lambda \cdot \mu .$ . Since no term of $a d - b c$ is the square of a variable, none of the four variables occurs in both λ and $\mu .$ Since none of the variables divides ad − bc, each of λ and $\mu$ must have at least two terms, and hence exactly two terms. But this would force $\lambda \cdot \mu$ to have four terms.

## Problem 3A.

Find

$$
\int _ { | z | = 2 } { \frac { 1 } { \cos z } } d z ,
$$

where the integral is taken with respect to the counterclockwise (positively oriented) parameterization of the circle $| z | = 2$

Solution: The integral must be invariant under changing $z \ { \mathrm { t o } } \ - z .$ , as this fixes the contour, but this change of variable also changes the sign of the integrand, so the integral is zero. It is also possible to do this question by adding up the residues at $\pm \pi i / 2$

## Problem 4A.

Let p, n be positive integers with p prime. Let $G = G L _ { n } ( F _ { p } )$ be the group of invertible $n \times n$ matrices over the field with p elements. Let $U \subset G$ be the subgroup consisting of upper triangular matrices with all diagonal entries equal to 1. Prove that every p-subgroup of G is conjugate to a subgroup of U .

Solution: By Sylow’s theorems it suffices to show that U is a Sylow p-subgroup of G. The above-diagonal entries of a matrix $X \in U$ may be chosen arbitrarily in $F _ { p } ,$ so $U$ has order $p ^ { { \binom { n } { 2 } } }$ . The order of G is

$$
( p ^ { n } - 1 ) ( p ^ { n } - p ) \cdot \cdot \cdot ( p ^ { n } - p ^ { n - 1 } ) = p ^ { \binom { n } { 2 } } ( p ^ { n } - 1 ) ( p ^ { n - 1 } - 1 ) \cdot \cdot \cdot ( p - 1 ) ,
$$

whose p-power factor is clearly $p ^ { { \binom { n } { 2 } } }$ , as desired. The formula for the order of $G$ can be derived as follows. We may choose the rows of a matrix $Y \in G$ in succession, where the k-th row is arbitrary, provided it does not belong to the $( k - 1 )$ -dimensional subspace spanned by the previously chosen rows (note that this procedure preserves the inductive hypothesis that the chosen rows are linearly independent). This gives $p ^ { n } - p ^ { k - 1 }$ choices for the k-th row. Now take the product over k from 1 to n.

Problem 5A.

Is it possible to find two closed and connected subsets A and B in $\mathbb { R } ^ { 2 }$ such that

$$
A + B = \{ ( x _ { 1 } + x _ { 2 } , y _ { 1 } + y _ { 2 } ) \in \mathbb { R } ^ { 2 } \mid ( x _ { 1 } , y _ { 1 } ) \in A , ( x _ { 2 } , y _ { 2 } ) \in B \}
$$

is not closed?

Solution: Yes; take A to be the x-axis and B to be one of the components of $x y = 1$ , so that $A + B$ is an open half-plane $( y > 0 \mathrm { ~ o r ~ } y < 0 )$

Problem 6A.

For $n \geq 1$ , prove that $a _ { n } + \frac { 1 } { a _ { n - 1 } + \displaystyle \frac { 1 } { \dots + \displaystyle \frac { 1 } { a _ { 1 } + \displaystyle \frac { 1 } { a _ { 0 } } } } } = \frac { \Delta _ { n } } { \Delta _ { n - 1 } } ,$

Solution: Using the cofactor expansion with respect to the last row, we find that $\Delta _ { n } =$ $a _ { n } \Delta _ { n - 1 } + \Delta _ { n - 2 }$ . Dividing by $\Delta _ { n - 1 }$ , we get:

$$
\Delta _ { n } / \Delta _ { n - 1 } = a _ { n } + \frac { 1 } { \Delta _ { n - 1 } / \Delta _ { n - 2 } } .
$$

The required result follows by induction on n since it obviously holds for $n = 1$

Problem 7A.

If $f$ is a meromorphic function which has a pole of order 1 at $z _ { 0 }$ show that

$$
{ \frac { f ^ { \prime \prime \prime } ( z ) } { f ^ { \prime } ( z ) } } - { \frac { 3 } { 2 } } \left( { \frac { f ^ { \prime \prime } ( z ) } { f ^ { \prime } ( z ) } } \right) ^ { 2 }
$$

can be extended to a holomorphic function at $z _ { 0 }$

Solution: If $f ( z ) ~ = ~ a z ^ { - 1 } + $ holomorphic, then $f ^ { \prime } ~ = ~ - a z ^ { - 2 } \left( 1 + z ^ { 2 } \right.$ × holomorphic), $f ^ { \prime \prime } ~ = ~ 2 a z ^ { - 3 } ( 1 + z ^ { 3 } \times$ holomorphic), $f ^ { \prime \prime \prime } = - 6 a z ^ { - 4 } ( 1 + z ^ { 4 } \times$ holomorphic). Therefore $\begin{array} { r l r } { f ^ { \prime \prime \prime } / f ^ { \prime } } & { { } = } & { 6 z ^ { - 2 } + } \end{array}$ holomorphic, and $f ^ { \prime \prime } / f ^ { \prime } = - 2 z ^ { - 1 } + z \times$ (holomorphic), so $( f ^ { \prime \prime } / f ^ { \prime } ) ^ { 2 } = 4 z ^ { - 2 } +$ holomorphic. The result follows from this.

Problem 8A.

Find the number of elements a in the ring $R = \mathbb { Z } / 6 4 6 4 \mathbb { Z }$ such that $a = x ^ { 5 }$ for some $x \in R$

Solution: By the Chinese Remainder Theorem, $R \cong ( \mathbb { Z } / 6 4 \mathbb { Z } ) \times ( \mathbb { Z } / 1 0 1 \mathbb { Z } )$ . Since 101 is prime, the multiplicative group $( \mathbb { Z } / 1 0 1 \mathbb { Z } ) ^ { \times }$ is cyclic of order 100. Its subgroup of fifth powers has order 20. Including 0, this gives 21 fifth powers in $\mathbb { Z } / 1 0 1 \mathbb { Z }$ . The multiplicative group $( \mathbb { Z } / 6 4 \mathbb { Z } ) ^ { \times }$ has order 32. Since 32 is coprime to 5, every element of $( \mathbb { Z } / 6 4 \mathbb { Z } ) ^ { \times }$ is a fifth power. The non-invertible elements of $\mathbb { Z } / 6 4 \mathbb { Z }$ belong to the ideal (2), hence their fifth powers belong to $( 2 ^ { 5 } )$ . This shows that the only non-invertible fifth powers in $\mathbb { Z } / 6 4 \mathbb { Z }$ are $\{ 0 , 3 2 \}$ , giving a total of 34 fifth powers in $\mathbb { Z } / 6 4 \mathbb { Z }$ . Hence there are $2 1 \times 3 4 = 7 1 4$ fifth powers in R.

Problem 9A.

Show that

$$
\operatorname* { l i m } _ { n  \infty } ( 1 + { \frac { z } { n } } ) ^ { n } = e ^ { z }
$$

uniformly on compact subsets of C.

Solution: Since $\log ( 1 + u )$ is holomorphic for $| u | < 1$ and has Taylor expansion at 0 is $\begin{array} { r } { \sum _ { k \geq 1 } ( - 1 ) ^ { k + 1 } u ^ { k } / k } \end{array}$ , we infer for $| u | \leq 1 / 2$ that

$$
| \log ( 1 + u ) - u | \leq C | u | ^ { 2 }
$$

for some constant C. If $n > 2 N$ and $| z | \leq N$ this gives $\begin{array} { r } { \left| \log \left( 1 + \frac { z } { n } \right) - \frac { z } { n } \right| \leq C N ^ { 2 } n ^ { - 2 } } \end{array}$ and $\begin{array} { r } { \left| \log \left( 1 + \frac { z } { n } \right) ^ { n } - z \right| \leq C N ^ { 2 } n ^ { - 1 } } \end{array}$ . On the other hand, since $\textstyle | \sum _ { k > 0 } a ^ { k } / k ! | \leq \sum _ { k > 0 } | a | ^ { k } / k !$ , we have $| e ^ { a } - 1 | \leq e ^ { | a | } - 1$ . Hence if $n > 2 N$ and $| z | \leq N$ we find

$$
\left| \left( 1 + \frac { z } { n } \right) ^ { n } - e ^ { z } \right| = | e ^ { z } | \cdot \left| e ^ { \log \left( 1 + \frac { z } { n } \right) ^ { n } - z } - 1 \right| \leq e ^ { N } \cdot \left( e ^ { C N ^ { 2 } n ^ { - 1 } } - 1 \right)
$$

so that $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \left| \left( 1 + \frac { z } { n } \right) ^ { n } - e ^ { z } \right| = 0 } \end{array}$ uniformly for $| z | \leq N$

## Problem 1B.

Find the real values of $\beta$ for which the following limit exists and is finite:

$$
\operatorname* { l i m } _ { R \to \infty } \int _ { 1 } ^ { R } x ^ { 2 } \cos ( x ^ { \beta } ) d x .
$$

Solution: When $\beta \leq 0$ , cos(xβ) tends to a positive limit as $x \to \infty$ , and hence

$$
\operatorname* { l i m } _ { R \to \infty } \int _ { 1 } ^ { R } x ^ { 2 } \cos ( x ^ { \beta } ) d x = \infty .
$$

When $\beta > 0$ , write the integral as $\begin{array} { r } { I ( R ) : = \beta ^ { - 1 } \int _ { 1 } ^ { R } x ^ { 3 - \beta } d \sin ( x ^ { \beta } ) } \end{array}$ . When $0 < \beta \le 3$ , the limit does not exist, since the differences $I ( ( 2 \pi k + \pi / \bar { 2 } ) ^ { 1 / \beta } ) - I ( ( 2 \pi k - \pi / 2 ) ^ { 1 / \beta } )$ do not tend to 0 as $k \to \infty$ . When $\beta > 3$ , integration by parts shows that

$$
I ( R ) = \mathrm { c o n s t } + \mathrm { c o n s t } R ^ { 3 - \beta } \mathrm { s i n } ( R ^ { \beta } ) + \mathrm { c o n s t } \int _ { 1 } ^ { R } x ^ { 2 - \beta } \mathrm { s i n } ( x ^ { \beta } ) d x .
$$

The integral on the right has a limit since $\sin ( x ^ { \beta } )$ is bounded, and $\int _ { 1 } ^ { \infty } x ^ { 2 - \beta } d x$ converges absolutely when $2 - \beta < - 1$ . The finite terms have a limit since $R ^ { 3 - \beta } \stackrel { \circ } { \to } 0$ . Therefore, when $\beta > 3$ , the limit of $I ( R )$ exists and is finite.

## Problem 2B.

Let P be a square matrix over R such that $P ^ { T } P = P$ . Prove that there exists a matrix A such that $A ^ { T } A$ is invertible and $P = A ( A ^ { T } A ) ^ { - 1 } A ^ { T }$

Solution: For any matrix A with linearly independent columns, $A ^ { T } A$ is invertible, and $A ( A ^ { T } A ) ^ { - 1 } A ^ { T }$ is the matrix of the orthogonal projection on the column space of A. (Indeed, the null space of $A ^ { T }$ is the orthogonal complement to the column space of A, and for every x from the column space of A we have $x = A z$ for some z, an hence $A ( A ^ { T } A ) ^ { - 1 } A ^ { T } x = A z = x . )$ Taking A to be a matrix whose columns are a basis of the column space of $P ,$ we have only to prove that P is the matrix of an orthogonal projection (necessarily onto its own column space). In other words, we must show that $x - P x$ is orthogonal to $P y$ for all vectors x, y. But $( x - P x ) ^ { T } P y = x ^ { T } ( P - P ^ { T } P ) y = 0$ by the hypothesis. (Another way: $P ^ { T } P = P$ implies that $P ^ { T } = ( { P } ^ { T } P ) ^ { T } = { P } ^ { T } P = P .$ , i.e. P is a self-adjoint idempotent: $P ^ { 2 } = P . )$

## Problem 3B.

Prove that the function $\begin{array} { r } { f ( z ) = \frac { z } { ( 1 - z ) ^ { 2 } } } \end{array}$ is injective on the disk $B _ { 1 } ( 0 ) = \{ z \in \mathbb { C } | | z | < 1 \}$ Find the Taylor series about $z = 0 ,$ , and determine its radius of convergence. What is the maximal disk $B _ { r } ( 0 ) = \{ w \in \mathbb { C } | | w | < r \}$ such that $B _ { r } ( 0 ) \subset f ( B _ { 1 } ( 0 ) ) ?$

Solution: Suppose that $f ( z _ { 1 } ) = f ( z _ { 2 } )$ , where $| z _ { i } | < 1$ . Then $\begin{array} { r } { \frac { z _ { 1 } } { ( 1 - z _ { 1 } ) ^ { 2 } } = \frac { z _ { 2 } } { ( 1 - z _ { 2 } ) ^ { 2 } } } \end{array}$ , and crossmultiplying, we have $z _ { 1 } ( 1 - z _ { 2 } ) ^ { 2 } = z _ { 2 } ( 1 - z _ { 1 } ) ^ { 2 }$ . Thus, $z _ { 1 } - z _ { 2 } = z _ { 2 } z _ { 1 } ^ { 2 } - z _ { 1 } z _ { 2 } ^ { 2 } = z _ { 1 } z _ { 2 } ( z _ { 1 } - z _ { 2 } )$ $\operatorname { I f }  z _ { 1 } \neq z _ { 2 }$ , then dividing we see that $1 = z _ { 1 } z _ { 2 }$ , which is impossible since then we would have $1 = | z _ { 1 } z _ { 2 } | = | z _ { 1 } | | z _ { 2 } | < 1$ , a contradiction. So $z _ { 1 } \neq z _ { 2 }$ , and $f ( z )$ is thus injective on $B _ { 1 } ( 0 )$

Noting that $\begin{array} { r } { f ( z ) = \frac { z - 1 + 1 } { ( 1 - z ) ^ { 2 } } = \frac { - 1 } { 1 - z } + \frac { 1 } { ( 1 - z ) ^ { 2 } } } \end{array}$ , and that $\scriptstyle { \frac { 1 } { ( 1 - z ) ^ { 2 } } } = { \frac { 1 } { 1 - z } } ^ { \prime } = ( 1 + z + z ^ { 2 } + \cdots ) ^ { \prime } =$ $1 + 2 z + 3 z ^ { 2 } + \cdot \cdot \cdot$ , we have $f ( z ) = - 1 - z - z ^ { 2 } - \cdot \cdot \cdot + 1 + 2 z + 3 z ^ { 2 } + \cdot \cdot \cdot = z + 2 z ^ { 2 } + 3 z ^ { 3 } + \cdot \cdot \cdot$

$$
f ( z )
$$

$$
B _ { 1 } ( 0 )
$$

Note that for $| z | = \rho < 1$ , we have $\begin{array} { r } { | f ( z ) | = \left| \frac { z } { ( 1 - z ) ^ { 2 } } \right| \ge \rho / ( 1 + \rho ) ^ { 2 } } \end{array}$ , since $| 1 - z | \leq 1 + | z | \leq$ $1 + \rho .$ , and this is an equality if $z = - \rho .$ . Thus, the disk $B _ { \rho / ( 1 + \rho ) ^ { 2 } } ( 0 )$ lies outside of the curve $f ( \rho e ^ { i \theta } ) , 0 \leq \theta < 2 \pi$ . Let $| a | < 1 / 4$ , and choose $0 < \rho < 1$ such that $| a | < \rho / ( 1 + \rho ) ^ { 2 }$ , which we may do since $\operatorname* { l i m } _ { \rho \to 1 } \rho / ( 1 + \rho ) ^ { 2 } = 1 / 4$ . The integral $\begin{array} { r } { { \frac { 1 } { 2 \pi i } } \int _ { | z | = \rho } { \frac { f ^ { \prime } ( z ) } { f ( z ) - a } } d z } \end{array}$ gives the multiplicity $| \{ z | \ f ( z ) \ = \ a , | z | \ < \ \rho \} |$ by the argument principle. Since f is injective, $f ( 0 ) = 0$ , and $B _ { \rho / ( 1 + \rho ) ^ { 2 } }$ lies in the complement of the contour $f ( \rho e ^ { i \theta } )$ , we see that there exists $| z | < \rho ,$ $f ( z ) = a$

## Problem 4B.

Determine the number of rotationally distinct colorings by two colors of the edges of a regular tetrahedron T .

Solution 1: The number of colorings with 0, 1, 2, 3, 4, 5, 6 red edges is 1, 1, 2, 4, 2, 1, 1.   
Total 12.

Solution 2: According to Cauchy’s theorem, the number of orbits of a finite group (of 12 rotations of the tetrahedron in this case) on a finite set (of all 2-color colorings of the edges) is equal to the average number of fixed points of group elements. A rotation g permutes the edges, and in the cycle decomposition of this permutation, the edges of the same cycle must have the same color for the coloring to be fixed by g, and vice versa. The identity rotation has 6 cycles (of length 1), each of the 8 rotations through the angle $1 2 0 ^ { \circ }$ has 2 cycles (of length 3 each), and each of the 3 rotations by $1 8 0 ^ { \circ }$ has 4 cycles (of lengths 1,1,2,2). Thus, the average number of fixed points is

$$
{ \frac { 1 } { 1 2 } } \left( 1 \times 2 ^ { 6 } + 8 \times 2 ^ { 2 } + 3 \times 2 ^ { 4 } \right) = { \frac { 1 4 4 } { 1 2 } } = 1 2 .
$$

## Problem 5B.

Solve the differential equation

$$
x y ^ { \prime } + y = y ^ { 2 }
$$

with initial condition $y ( 1 ) = 2$

Solution: Separation of variables gives dx $/ x = d y / ( y ^ { 2 } - y )$ , and integrating both sides of this gives log $x = \log ( y - 1 ) - \log ( y ) + c , { \mathrm { ~ o r ~ } } y = 1 / ( K x + 1 )$ , so using the initial condition we get $y = 2 / ( 2 - x )$

## Problem 6B.

Let $\langle z , w \rangle = \sum z _ { i } { \bar { w } } _ { i }$ be the Hermitian dot product on $\mathbb { C } ^ { n }$ , and let A be a normal linear operator on Cn, i.e. $A ^ { * } A = A A ^ { * }$ where $A ^ { * } = \bar { A } ^ { t }$ is Hermitian adjoint to A. Prove that the set of complex numbers

$$
\Lambda _ { A } : = \{ \langle A z , z \rangle \mid z \in \mathbb { C } ^ { n } , \langle z , z \rangle = 1 \}
$$

is a convex polygon.

Solution: According to the orthogonal diagonalization theorem, a normal operator has an Hermitian orthonormal basis of eigenvectors. In such a basis, $\langle A z , z \rangle = \sum \lambda _ { i } | z _ { i } | ^ { 2 }$ , where $\lambda _ { i }$ are the eigenvalues of A, while $\langle z , z \rangle = 1$ becomes $\sum | z _ { i } | ^ { 2 } = 1$ This shows that $\Lambda _ { A }$ coincides with the convex hull of the finite set $\lambda _ { 1 } , \ldots , \lambda _ { n }$ of eigenvalues of A.

Problem 7B.

Suppose α is a complex number, $| \alpha | \neq 1$ . Compute

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 \alpha \cos \theta + \alpha ^ { 2 } } }
$$

by integrating $( z - \alpha ) ^ { - 1 } ( z - \alpha ^ { - 1 } ) ^ { - 1 }$ over the unit circle.

Solution: Parameterize the unit circle C by $z ( \theta ) = e ^ { i \theta } , \theta \in [ 0 , 2 \pi ]$ . Then $z ^ { \prime } ( \theta ) = i e ^ { i \theta } =$ $i z ( \theta )$ , and we have cos $\theta = { \textstyle { \frac { 1 } { 2 } } } ( e ^ { i \theta } + e ^ { - i \theta } ) = { \textstyle { \frac { 1 } { 2 } } } ( z + \dot { z ^ { - 1 } } )$ . We also have $d \theta = - i d z / z$ , so we have

$$
\begin{array} { l } { \displaystyle \int _ { 0 } ^ { 2 \pi } \displaystyle \frac { d \theta } { 1 - 2 \alpha \cos \theta + \alpha ^ { 2 } } = \int _ { C } \displaystyle \frac { - i d z / z } { 1 - \alpha ( z + z ^ { - 1 } ) + \alpha ^ { 2 } } = \int _ { C } \displaystyle \frac { i d z \alpha ^ { - 1 } } { z ^ { 2 } - ( \alpha + \alpha ^ { - 1 } ) z + 1 } } \\ { = \displaystyle \frac { i } { \alpha } \int _ { C } \displaystyle \frac { d z } { ( z - \alpha ) ( z - \alpha ^ { - 1 } ) } . } \end{array}
$$

If $\alpha = 0$ , then

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 \alpha \cos \theta + \alpha ^ { 2 } } } = \int _ { 0 } ^ { 2 \pi } d \theta = 2 \pi = { \frac { 2 \pi } { 1 - \alpha ^ { 2 } } } .
$$

If $0 < | \alpha | < 1$ , then $\frac { 1 } { z - \alpha ^ { - 1 } }$ is analytic inside C since $| \alpha ^ { - 1 } | > 1$ , so by Cauchy’s integral formula, we have

$$
i \alpha ^ { - 1 } \int _ { C } \frac { ( z - \alpha ^ { - 1 } ) ^ { - 1 } d z } { z - \alpha } = i \alpha ^ { - 1 } \frac { 2 \pi i } { \alpha - \alpha ^ { - 1 } } = \frac { 2 \pi } { 1 - \alpha ^ { 2 } } .
$$

If $| \alpha | > 1$ , then exchanging the roles of α and $\alpha ^ { - 1 }$ , we have

$$
i \alpha ^ { - 1 } \int _ { { \cal C } } \frac { ( z - \alpha ) ^ { - 1 } d z } { z - \alpha ^ { - 1 } } = i \alpha ^ { - 1 } \frac { 2 \pi i } { \alpha ^ { - 1 } - \alpha } = \frac { 2 \pi } { \alpha ^ { 2 } - 1 } .
$$

So we have for $| \alpha | \neq 1$

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 \alpha \cos \theta + \alpha ^ { 2 } } } = { \frac { 2 \pi } { \alpha ^ { 2 } - 1 } } \cdot { \frac { | \alpha | - 1 } { | | \alpha | - 1 | } } .
$$

## Problem 8B.

Let n be a positive integer, $C _ { n }$ the cyclic group of order $n ,$ and $S _ { n }$ the symmetric group on n points. For each of the groups

$$
\begin{array} { l l l l } { A = \mathbf { R } ^ { * } } & { B = \mathbf { C } ^ { * } } & { C = C _ { 2 } \times C _ { 3 } } & { D = S _ { 4 } } & { E = S L _ { 2 } ( \mathbf { R } ) } \end{array}
$$

prove or disprove that $C _ { 6 }$ is isomorphic to a subgroup of it.

Solution: $C _ { 6 }$ is not a subgroup of A because in $\mathbb { R } ^ { * }$ , if $r \neq \pm 1$ , then $r ^ { 6 } \neq 1$ , or of D because if $s \in D$ and s is not the identity s has a cycle decompositions of the form $( a b ) ( c d ) , ( a b c )$ or $( a b c d )$ and these have orders $2 , 3$ and 4.

$C _ { 6 }$ is a subgroup of $B , C$ and E because cos $( \pi / 3 ) + i \sin ( \pi / 3 ) \in B , ( 1 , 1 ) \in C$ , and

$$
\left( \begin{array} { c c } { \cos ( 2 \pi / 3 ) } & { - \sin ( 2 \pi / 3 ) } \\ { \sin ( 2 \pi / 3 ) } & { \cos ( 2 \pi / 3 ) } \end{array} \right) \in { \cal E }
$$

all have order 6.

## Problem 9B.

If f is a smooth real valued function of x, y, z such that

$$
\frac { \partial ^ { 2 } f } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } f } { \partial y ^ { 2 } } + \frac { \partial ^ { 2 } f } { \partial z ^ { 2 } } > 0
$$

for all $x , y , z$ , show that f does not have a local maximum.

Solution: At a local maximum of f all second derivatives with respect to $x , y , z$ must be at most 0, so their sum cannot be positive.