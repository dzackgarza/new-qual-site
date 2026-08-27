Find the length of the spiral given in polar coordinates by $r = e ^ { \theta } , - \infty < \theta \leq 0 .$

Solution: The length is $\scriptstyle \int _ { \theta = - \infty } ^ { 0 }$ ds where by Pythagoras ds $= { \sqrt { d r ^ { 2 } + ( r d \theta ) ^ { 2 } } } = d \theta \times { \sqrt { 2 } } e ^ { \theta }$ so the length is $\textstyle \int _ { - \infty } ^ { 0 } { \sqrt { 2 } } e ^ { \theta } { \dot { d \theta } } = { \sqrt { 2 } } .$

Problem 2A. Real analysis

Score:

Prove or disprove the following assertion:

If $f \colon  { \mathbb { R } } \to$ R has the property that $f ( [ a , b ] )$ is a bounded closed interval for every $a \leq b ,$ then $f$ is continuous.

Solution: Counterexample:

$$
f ( x ) = { \left\{ \begin{array} { l l } { \sin ( 1 / x ) } & { x \neq 0 , } \\ { 0 } & { x = 0 . } \end{array} \right. }
$$

Since $\operatorname* { l i m } _ { x \to 0 } f ( x )$ does not exist, f is discontinuous at 0 (this is the classic example of a discontinuity which is not a jump). To verify that it is a counterexample we must show that every $f ( [ a , b ] )$ is a closed interval. Now, the converse of the assertion in the problem is true, since the continuous image of a compact, connected space is compact and connected, and the compact, connected subsets of R are just the closed intervals. Since $f$ is continuous on $\mathbb { R } \backslash \{ 0 \}$ , this implies that $f ( [ a , b ] )$ is a closed interval whenever $0 \not \in [ a , b ]$ . In the remaining cases, if $0 \in [ a , b ]$ and $a < b ,$ then $f ( [ a , b ] ) = [ - 1 , 1 ]$ , while $f ( [ 0 , 0 ] ) = [ 0 , \bar { 0 } ]$

## Problem 3A. Real analysis

Score:

Prove the existence of the limit

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { 1 } } + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \cdots + { \frac { 1 } { n } } - \log n .
$$

Solution: We can write this as $\textstyle 1 / n + \int _ { 1 } ^ { n } ( 1 / [ x ] - 1 / x ) d x$ . The integral is an integral of a positive function, so tends to a limit $\mathrm { o r } + \infty$ as n tends to ∞. On the other hand we can also

write it as $\textstyle 1 + \int _ { 1 } ^ { n } ( 1 / [ x + 1 ] - 1 / x ) d x$ which is at most 1. So the integral in the first sentence above is bounded, and therefore tends to a (finite) limit. So the limit in the question exists.

<table><tr><td>Problem 4A. Complex analysis Score:</td></tr><tr><td>(a) Find the poles and residues of  $1 / ( z ^ { 3 } \cos ( z ) )$  (b) Show that the integral of the function above over a square contour centered at the origin with side  $2 \pi N$  tends to zero as the integer N tends to infinity.</td></tr><tr><td>(c) Find the sum  $1 / 1 ^ { 3 } - 1 / 3 ^ { 3 } + 1 / 5 ^ { 3 } - 1 / 7 ^ { 3 } + \cdot \cdot \cdot$  Solution: (a) There is a simple pole at  $( n + 1 / 2 ) \pi$  of residue  $( - 1 ) ^ { n + 1 } ( ( n + 1 / 2 ) \pi ) ^ { - 3 }$  and a pole of order 3 at 0 with residue  $1 / 2 .$  (b)  $1 / \cos ( z )$  is bounded on the boundary of this square, and  $1 / z ^ { 3 }$  is bounded by a constant times  $1 / N ^ { 3 }$  , and the length of the boundary is bounded by a constant times N, so the integral is bounded by a constant times  $1 / N ^ { 2 }$  which tends to 0. (c) By part b and Cauchy&#x27;s residue theorem the sum of all residues is 0. By part a this</td></tr><tr><td>means that  $\begin{array} { r } { 1 / 2 + \sum _ { n } ( - 1 ) ^ { n + 1 } ( ( n + 1 / 2 ) \pi ) ^ { - 3 } = 0 } \end{array}$  , giving the sum in the question as  $\pi ^ { 3 } / 3 2$  Problem 5A. Complex analysis Score:</td></tr><tr><td>(a) Show that if  $| z | < 1$  then there is a holomorphic function defined on some neigh- borhood of the unit disk whose only zero is at z and that has absolute value 1 on the unit circle. (b) Suppose that f is a holomorphic function on the complex plane and is not identically zero. Show that there is a holomorphic function g defined in some open set containing the</td></tr><tr><td>unit disk such that  $| f ( z ) | = | g ( z ) |$  whenever  $| z | = 1$  , and such that g has no zeros in the open unit disk.</td></tr><tr><td>Solution:  $( \mathrm { a } ) ( z - t ) / ( 1 - \overline { { z } } t )$  (b) Divide f by the product of the functions in part (a) for each zero of f in the unit circle. Problem 6A. Linear algebra Score:</td></tr></table>

If U, V , W are subspaces of a vector space such that any two have intersection zero,

prove that

$$
\dim ( U + V + W ) + \dim U + \dim V + \dim W \leq \dim ( U + V ) + \dim ( V + W ) + \dim ( W + U )
$$

and give an example where equality does not hold.

## Solution:

Since any two of the subspaces have intersection 0, we have dim $( U + V ) = \dim ( U ) +$ dim(V ). So the inequality is equivalent to dim $( U + V + W ) \leq \dim ( U ) + \dim ( V ) + \dim ( W )$ which is obvious. For an example where equality does not hold, take U, V , W to be 3 distinct 1-dimensional subspaces of a 2-dimensional space.

Problem 7A. Linear algebra

Score:

Let $I _ { n }$ denote the $n \times n$ identity matrix, and $J _ { n }$ the $n \times n$ matrix with all entries equal to 1.   
Determine for which real numbers a the matrix $I _ { n } + a J _ { n }$ is invertible, and find its inverse.

Solution: Clearly rank $( J _ { n } ) = 1$ , and the vector $( 1 , 1 , \ldots , 1 ) ^ { T }$ is an eigenvector with eigenvalue n. Therefore the eigenvalues of J are n, with multiplicity 1, and 0, with multiplicity $n - 1$ . It follows that $I _ { n } + a J _ { n }$ is invertible iff $a \ne - 1 / n$ . To find the inverse, observe that $J _ { n } ^ { 2 } = n J _ { n }$ , hence $( I _ { n } + b J _ { n } ) ( I _ { n } + a J _ { n } ) = I _ { n } + ( a + b + n a b ) J _ { n }$ n. Solving $a + b + n a b = 0$ for b, we see that $( I _ { n } + a J _ { n } ) ^ { - 1 } = ( I _ { n } + b J _ { n } )$ , where $b = - a / ( 1 + n a )$

Problem 8A. Abstract algebra

Score:

Let G be a finite Abelian group of order n. Suppose m is a square-free (not divisible by the square of a prime), positive integer dividing n. Show that G contains an element of order m. Give an example to show that this need not be true if m is not assumed to be square-free.

Solution: Write $m = p _ { 1 } p _ { 2 } \cdots p _ { k }$ , where the $p _ { i }$ are distinct primes. By Cauchy’s theorem G contains an element $a _ { i }$ of order $p _ { i }$ . Claim: $g = : a _ { 1 } a _ { 2 } \cdot \cdot \cdot a _ { k }$ has order m. First

$$
g ^ { d } = a _ { 1 } ^ { d } a _ { 2 } ^ { d } \cdot \cdot \cdot a _ { k } ^ { d } .
$$

So $g ^ { m } = e$ since $a _ { i } ^ { m } = ( a _ { i } ^ { p _ { i } } ) ^ { m / p _ { i } } = e$ . Now suppose m $\quad \bigwedge d .$ . Then there exists an i such that $p _ { i } { \big \rangle } d .$ Then $p _ { i } { \mathrm { ~ } } \nrangle { d m } / p _ { i }$ , but $p _ { j } | d m / p _ { i } { \mathrm { ~ i f ~ } } j \neq i ;$ , so

$$
( g ^ { d } ) ^ { m / p _ { i } } = a _ { i } ^ { d m / p _ { i } } \ne e .
$$

Thus g has order m.

The product of 2 groups of order 2 has order divisible by 4 but contains no element of order 4.

Problem 9A. Abstract algebra

Score:

Does there exists a homomorphism of commutative rings with unit from $\mathbb { Z } [ x ] / ( x ^ { 2 } + 3 )$ to $\mathbb { Z } [ x ] / ( x ^ { 2 } - x + 1 ) ?$ Either exhibit such a homomorphism, or prove that none exists.

Solution: The question amounts to whether −3 has a square root in the ring $S = \mathbb { Z } [ x ] / ( x ^ { 2 } -$ $x + 1 )$ . The elements of $S$ may be written $a x + b , a , b \in \mathbb { Z }$ , and the square of such an element is then given by

$$
( a x + b ) ^ { 2 } = a ^ { 2 } ( x - 1 ) + 2 a b x + b ^ { 2 } = ( a ^ { 2 } + 2 a b ) x + ( b ^ { 2 } - a ^ { 2 } ) .
$$

So we need a solution in integers of the equations $a ^ { 2 } + 2 a b = 0 , b ^ { 2 } - a ^ { 2 } = - 3$ . The solutions are $( b = 1 , a = - 2 )$ and $( b = - 1 , a = 2 )$ . Hence there are two ring homomorphisms

$$
\begin{array} { c } { \mathbb { Z } [ x ] / ( x ^ { 2 } + 3 )  \mathbb { Z } [ x ] / ( x ^ { 2 } - x + 1 ) } \\ { x \mapsto \pm ( 2 x - 1 ) . } \end{array}
$$

(Although not necessary to the solution of the problem, what is happening here is that the ring $\mathbb { Z } [ { \sqrt { - 3 } } ] \cong \mathbb { Z } [ x ] / ( x ^ { 2 } + 3 )$ is not integrally closed. Instead, the full ring of algebraic integers in the field $\mathbb { Q } ( { \sqrt { - 3 } } )$ is the larger ring $\mathbb { Z } [ ( 1 \pm { \sqrt { - 3 } } ) / 2 ] \cong \mathbb { Z } [ x ] / ( x ^ { 2 } - x + 1 ) .$ )

Problem 1B. Calculus

Score:

Prove that

$$
{ \frac { \pi } { 4 } } = 4 \arctan { \frac { 1 } { 5 } } - \arctan { \frac { 1 } { 2 3 9 } } .
$$

In 1706 John Machin used this formula to calculate π to 100 decimal places. Explain briefly why he did not use the simpler formula $\begin{array} { r } { \frac { \pi } { 4 } = \arctan 1 } \end{array}$

Solution: Use tan $( x + y ) = ( \tan ( x ) + \tan ( y ) ) / ( 1 - \tan ( x ) \tan ( y ) )$ three times. $\mathrm { ~ I f ~ } x =$ arctan $( 1 / 5 )$ then $\tan ( x ) = 1 / 5$ , so tan $( 2 x ) = 5 / 1 2$ and tan $( 4 x ) = 1 2 0 / 1 1 9$ . Putting $y =$ arctan(1/239) gives tan $( 4 x - y ) = ( 1 2 0 / 1 1 9 - 1 / 2 3 9 ) / ( 1 + 1 2 0 / ( 1 1 9 \times 2 3 9 ) ) = ( 1 2 0 \times 2 3 9 - 1$ $1 1 9 ) / ( 1 1 9 \times 2 3 9 + 1 2 0 ) = 1 \ { \mathrm { s o } } \ 4 x - y = \pi / 4$ (as an easy estimate shows it is between 0 and $\pi / 2 )$

The series $\pi / 4 = \arctan 1 = 1 - 1 / 3 + 1 / 5 - \cdot \cdot \cdot$ converges too slowly to use directly for calculating π: it needs about $1 0 ^ { n }$ terms for n decimal places.

Problem 2B. Real analysis

Score:

(a) Find the sum $1 - 1 / 2 + 1 / 3 - 1 / 4 + \cdot \cdot \cdot$

(b) Find the sum $1 - 1 / 2 - 1 / 4 + 1 / 3 - 1 / 6 - 1 / 8 + 1 / 5 - 1 / 1 0 - 1 / 1 2 + \cdot \cdot \cdot .$

Solution: (a) log 2

(b) Pairing the 1st and 2nd, 4th and 5th terms and so on, this series is equal to $1 / 2 -$ $1 / 4 + 1 / 6 - 1 / 8 + \cdot \cdot \cdot$ whose terms are half thsoe of the preceding series, so the sum is $( \log 2 ) / 2$ . The point is that even though it has the same terms as the first series the sum is different.

Problem 3B. Real analysis

Score:

Let $( X , d _ { X } )$ and $( Y , d _ { Y } )$ be metric spaces. Suppose that a map $\pi : X \to Y$ is a submetry; this means that for every $x \in X$ and any $r > 0$ , the image of the closed r-ball around x is the closed r-ball around $\pi ( x )$

(a) Show that π is surjective if X is nonempty.

(b) Show that π is continuous.

(c) Show that π is open (meaning that the image of any open subset is open).

$$
x _ { 0 } \in X
$$

$$
\pi ( D ( x _ { 0 } , r ) )
$$

$$
y \in Y
$$

$$
r = d _ { Y } ( \pi ( x _ { 0 } ) , y )
$$

$$
x \in D ( x _ { 0 } , r )
$$

$$
y \in D ( \pi ( x _ { 0 } ) , r ) =
$$

$$
\pi ( x ) = y .
$$

(b) Given $x \in X$ and $\epsilon > 0 , \pi ( B ( x , \epsilon / 2 ) ) \subset \pi ( D ( x , \epsilon / 2 ) ) = D ( \pi ( x ) , \epsilon / 2 ) \subset B ( \pi ( x ) , \epsilon )$

(c) It suffices to show that the image of any open ball is open in Y .

$$
\pi ( B ( x , r ) ) = \pi \left( \bigcup _ { r ^ { \prime } < r } D ( x , r ) \right) = \bigcup _ { r ^ { \prime } < r } \pi ( D ( x ) , r ) ) = \bigcup _ { r ^ { \prime } < r } D ( \pi ( x ) , r ) ) = B ( \pi ( x ) , r ) .
$$

Compute

Score:

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { ( x ^ { 2 } + 1 ) ^ { 2 } } } .
$$

Solution: We want to compute

$$
\frac { 1 } { 2 } \int _ { - \infty } ^ { \infty } \frac { d x } { ( x ^ { 2 } + 1 ) ^ { 2 } } .
$$

Put

$$
f ( z ) = { \frac { 1 } { ( z ^ { 2 } + 1 ) ^ { 2 } } } .
$$

Because $| f ( z ) | = O ( | z | ^ { - 4 } )$ , we can apply the Cauchy residue theorem to a semicircle in the upper half plane and just compute residues. The only singularity in the upper half plane is at $z = i$ . The residue there is $- 2 ( 2 i ) ^ { - 3 }$ . The answer is

$$
{ \frac { 1 } { 2 } } \cdot 2 \pi i \cdot - 2 ( 2 i ) ^ { - 3 } = { \frac { \pi } { 4 } } .
$$

Problem 5B. Complex analysis

Score:

Show that as the positive integer N tends to infinity, the change in argument of $e ^ { z } - z$ is bounded on 3 sides of the square with corners $\pm 2 \pi N \pm 2 \pi i N$ but is unbounded on the fourth side. Show that $e ^ { z } = z$ has infinitely many complex roots.

Solution: On the left side of the square the argument is dominated by $z { \mathrm { ~ a s ~ } } e ^ { z }$ is very small and the function has negative real part, so the change in argument is bounded. On the top and bottom of the square the function has positive or negative imaginary part, so the change in argument is bounded. On the right of the square the function is dominated by $e ^ { z }$ for N large and z makes little change to the argument, so the change is about that of $e ^ { z }$ which is roughly proportional to N and therefore tends to infinity.

The number of roots of $e ^ { z } = z$ in a large square is proportional to the change in argument on the boundary of the square, which tends to infinity so there are infinitely many roots.

Problem 6B. Linear algebra

Score:

Find all eigenvalues and eigenvectors of the linear map $T \colon \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$ given by $T ( ( x _ { 1 } , \dots , x _ { n } ) ) =$ $\left( x _ { 2 } , x _ { 3 } , \ldots , x _ { n } , x _ { 1 } \right)$

Solution: Since $T ^ { n } = I ,$ every eigenvalue is an n-th root of unity $\omega = e ^ { 2 \pi i k / n }$ . Every n-th root of unity is an eigenvalue, because $( 1 , \omega , \omega ^ { 2 } , \ldots , \omega ^ { n - 1 } )$ is an eigenvector with eigenvalue ω.

Suppose that A and B are linear transformations of a finite dimensional complex

vector space such that $A B - B A = A$ . If v is an eigenvector of B with eigenvalue λ, show that Av is zero or an eigenvector of B and find its eigenvalue. Prove that A is nilpotent.

Solution: If $B v = \lambda v$ then $B A v = ( A B - A ) v = ( \lambda - 1 )$ Av so $A v$ is a (possibly zero) eigenvector with eigenvalue $\lambda - 1$ Since $\lambda , \lambda - 1 , \lambda - 2 , .$ .. cannot all be eigenvalues of nonzero eigenvectors, $A ^ { n } v$ must be zero for large n.

Suppose V is the vector space, and if it is nonzero pick a non-zero eigenvector v of B. By induction on the dimension of V , A is nilpotent on $V / \mathbb { C } v$ , and is nilpotent on v, so is nilpotent on V .

Problem 8B. Abstract algebra

Score:

Let R be a commutative ring with unit. Suppose that there is a monic polynomial $p ( x ) \in R [ x ]$ such that the ideal $( p ( x ) ) \subseteq R [ x ]$ is maximal. Prove that R is a field.

Solution: Let $p ( x )$ be monic of degree d. Then $R [ x ] / ( p ( x ) )$ is a free R module with basis $\{ 1 , x , \ldots , x ^ { d - 1 } \}$ , that is, each of its elements can be written uniquely in the form $f = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot a _ { d - 1 } x ^ { d - 1 } $ , where $a _ { i } \ \in \ R$ , with multiplication in $R [ x ] / ( p ( x ) )$ given by multiplication of polynomials followed by reduction mod $( p ( x ) )$ . In particular, if $r \in R$ , then $r a _ { 0 } + r a _ { 1 } x + \cdot \cdot \cdot + r a _ { d - 1 } x ^ { d - 1 }$ is the unique canonical expression for $r f$

The hypothesis that $( p ( x ) )$ is maximal is equivalent to $R [ x ] / ( p ( x ) )$ being a field. So for every nonzero $r \in R$ , there is an element f as above such that $r f = 1$ . By the uniqueness of the expression for $r f$ , this implies $r a _ { 0 } = 1$ . Thus r has an inverse in $R ,$ so R is a field.

Score:

Let M be a (possibly singular) square matrix over a field F . Let p be the product of the nonzero eigenvalues (counted with multiplicities) of M in some algebraically closed extension K of F . Prove that $p \in F$

Solution: The characteristic polyomial $f ( x ) = \operatorname* { d e t } ( M - x I )$ factors as $\textstyle x ^ { m } \prod _ { i } ( x - \lambda _ { i } )$ , where m is the nullity of M and the $\lambda _ { i }$ are the non-zero eigenvalues. The product of the non-zero eigenvalues is therefore ± the coefficient of $x ^ { m }$ in $f ( x )$ , hence an element of F .