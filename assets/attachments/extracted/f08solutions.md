1A

Find a sequence $r _ { n }$ of positive rational numbers such that, $\textstyle \sum _ { n = 0 } ^ { \infty } r _ { n }$ converges and for any prime p and any positive integer m, $p ^ { m }$ divides the numerator of $s _ { k } - s _ { j }$ (written in lowest terms) for k and $j$ sufficiently large, where $\textstyle s _ { k } = \sum _ { n = 0 } ^ { k } r _ { n }$ Tel

Solution. Take

$$
r _ { n } = \frac { n ! } { ( n ! + 1 ) ^ { 2 } } .
$$

The series converges because $r _ { n } \leq 1 / n !$ and other requirement follows from the fact that $p ^ { m } | n !$ for $n \geq p ^ { m }$

2A

Suppose the function f is analytic in the entire complex plane, and suppose that $f ( z ) / z$ is bounded in the region $| z | > 1$ . Prove that $ f ( z ) = a z + b$ for some constants a and b.

Solution. $( f ( z ) - f ( 0 ) ) / z$ is bounded and analytic on the whole plane (when extended to $z = 0$ by continuity), so is constant.

3A

Find the eigenvalues of the n × n-matrix $( a _ { i j } )$ (where $n > 2 )$ such that

$a _ { i j } = 1$ when $j - i \equiv 1$ mod n, $a _ { i j } = - 1$ when $j - i \equiv - 1$ mod $n ,$ and $a _ { i j } = 0$ otherwise.

(Hint: find sequences $b _ { i }$ and complex numbers z such that $( z - z ^ { - 1 } ) b _ { i } =$ $b _ { i + 1 } - b _ { i - 1 } , b _ { i } = b _ { i + n }$ for all integers i.)

Solution. The operator can be thought of as a finite difference version of the differentiation on a discretized circle. Its eigen-vectors $( x _ { 1 } , \ldots , x _ { n } )$ are “Fourier modes $^ { \ ' } \ ( 1 , j , j ^ { 2 } , \ldots , j ^ { n - 1 } )$ where $j = e ^ { 2 \pi i k / n }$ $k = 0 , 1 , \ldots , n - 1$ The corresponding eigen-values are $j - j ^ { - 1 } =$ $2 i \sin ( 2 \pi k / n )$

4A

For which integer values of n (positive or negative or zero) is there a holomorphic function of $z$ defined for $| z | > 1$ whose derivative is

$$
{ \frac { z ^ { n } } { 1 + z ^ { 2 } } } .
$$

Solution. Changing z to $1 / z$ we want to know when $\frac { z ^ { - n } } { 1 + z ^ { - 2 } } = z ^ { 2 - n } -$ $z ^ { 4 - n } + z ^ { 6 - n } - \cdot \cdot$ · is the derivative of a function defined near $z = 0$ This holds if and only if the residue at 0 vanishes, in other words if the coefficient of $z ^ { - 1 }$ vanishes, which is true if $n < 0$ or n is even. (An alternative solution is to sum the residues at $z = \pm i . )$ 0

5A

Are the rings $\mathbb { R } [ x ] / ( x ^ { 2 } + x - 1 )$ and $\mathbb { R } [ x ] / ( x ^ { 2 } + 2 x - 3 )$ isomorphic? Solution. Yes. When a real polynomial $f = ( x - a ) ( x - b )$ has distinct real roots $a \neq b$ , the quotient ring $\mathbb { R } [ x ] / ( f )$ is isomorphic to $\mathbb { R } \times \mathbb { R }$ The isomorphism is established by evaluation:

$$
\mathbb { R } [ x ] \to \mathbb { R } \times \mathbb { R } , \ p \mapsto ( p ( a ) , p ( b ) )
$$

whose kernel consists of polynomials divisible by $f .$

6A

If $f$ is a continuous strictly increasing function of x with $f ( 0 ) = 0$ and with inverse $f ^ { - 1 }$ show that

$$
\int _ { 0 } ^ { a } f ( x ) d x + \int _ { 0 } ^ { b } f ^ { - 1 } ( x ) d x \geq a b
$$

for any positive real numbers a and $b .$ (Hint: draw a picture.) Use this to prove Young’s inequality, which states that if $p$ and q are positive reals with $1 / p + 1 / q = 1$ and a and b are positive reals then

$$
\frac { a ^ { p } } { p } + \frac { b ^ { q } } { q } \geq a b .
$$

(The question on the exam had both inequalities the wrong way round.)

Solution. Draw the graph of $f ,$ and color in the region below the graph whose area is the first integral, and the area to the left of the graph whose are is the second integral. These cover the rectangle $0 \leq$ $x \leq a , 0 \leq y \leq b .$ , which proves the first inequality. Young’s inequality follows by taking $f ( x ) = x ^ { p - 1 }$ , with inverse is given by $f ^ { - 1 } ( x ) = x ^ { q - 1 }$ 7A

Suppose $H _ { i }$ is a normal subgroup of a group G for $1 \leq i \leq k$ such that $H _ { i } \cap H _ { j } = \{ 1 \}$ for $i \neq j$ (where 1 is the identity element). Prove that G contains a subgroup isomorphic to $H _ { 1 } \times H _ { 2 } \times \cdots \times H _ { k }$ if $k = 2$ , but not necessarily if $k \geq 3$

Solution: If $k = 2$ the map $H _ { 1 } \times H _ { 2 } \to G$ induced by the inclusions $H _ { i } \subset G$ is injective, as the kernel consists of pairs $( h _ { 1 } , h _ { 2 } )$ with $h _ { i } \in H _ { i }$ such that $h _ { 1 } = h _ { 2 } ^ { - 1 }$ in G which implies that $h _ { 1 } , h _ { 2 } \in H _ { 1 } \cap H _ { 2 } = \{ 1 \}$ To see that this can fail if $k \geq 3$ consider $G = { \bf Z } / ( 2 ) \times { \bf Z } / ( 2 )$ Let $H _ { 1 } = \langle ( 1 , 0 ) \rangle , H _ { 2 } = \langle ( 0 , 1 ) \rangle , H _ { 3 } = \langle ( 1 , 1 ) \rangle$ . Then the assumptions are satisfied but the element $( ( 1 , 0 ) , ( 0 , 1 ) , ( 1 , 1 ) ) \in H _ { 1 } \times H _ { 2 } \times H _ { 3 }$ is in the kernel of the map

$$
H _ { 1 } \times H _ { 2 } \times H _ { 3 } \to G .
$$

8A The infinitely differentiable real function $u ( x , t )$ satisfies the diffusion PDE $u _ { t } = u _ { x x }$ in $- \infty < x < \infty , \ t > 0$ . Assume that u and all its partial derivatives of all orders are rapidly decreasing in x, in other words bounded by a constant times $x ^ { - n }$ for all $n > 0$ in any strip of the form $0 < t < a$ . Also assume that $\textstyle \int _ { - \infty } ^ { \infty } u ( x , 1 ) d x = 1$ . Show that if $t > 0$ then

$$
\frac { d } { d t } \int _ { - \infty } ^ { \infty } x ^ { 2 } u ( x , t ) d x = 2 .
$$

Solution.

$$
\frac { d } { d t } \int _ { - \infty } ^ { \infty } x ^ { 2 } u d x = \int _ { - \infty } ^ { \infty } x ^ { 2 } u _ { t } d x = \int _ { - \infty } ^ { \infty } x ^ { 2 } u _ { x x } d x = 2 \int _ { - \infty } ^ { \infty } u d x .
$$

Last equality is two integrations by parts. Next,

$$
\frac { d } { d t } \int _ { - \infty } ^ { \infty } u d x = \int _ { - \infty } ^ { \infty } u _ { x x } d x = 0
$$

so $\textstyle \int _ { - \infty } ^ { \infty } u d x =$ constant independent of t. The constant is 1 by $\textstyle \int _ { - \infty } ^ { \infty } u ( x , 0 ) d x =$ 1. Hence,

$$
\frac { d } { d t } \int _ { - \infty } ^ { \infty } x ^ { 2 } u ( x , t ) d x = 2 .
$$

9A

Suppose that $f _ { n }$ for $n > 0$ is a sequence of continuous real-valued functions on the unit interval [0, 1] such that $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) = 0 } \end{array}$ for all x. Prove or find a counterexample to the statement

$$
\operatorname* { l i m } _ { n  \infty } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x = 0 .
$$

The statement is false. A counterexample is given by taking $f _ { n }$ to be a function vanishing outside $( 0 , 1 / n )$ , and having a bump of average height n on this interval (so that $\begin{array} { r } { \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x = 1 ) } \end{array}$

1B Let V be a non-zero vector space over an infinite field. Show: V is not the union of finitely many cosets $a _ { 1 } + V _ { 1 } , \dots , a _ { n } + V _ { n }$ of proper subspaces $V _ { 1 } , \ldots , V _ { n }$

Solution: If V is the union of finitely many cosets, we can assume n is minimal. So there is some v in $a _ { 1 } + V _ { 1 }$ not in any other coset. Pick some vector w not in $V _ { 1 }$ . Then for any coset $V _ { i } .$ , there is at most one value of x such that v + xw is in the other coset. As the field is infinite, there is some x such that $v + w x$ is not in any of the cosets.

2B Evaluate the integral

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { 1 + x ^ { \alpha } } }
$$

for $\alpha > 1$

Solution: Apply Cauchy’s theorem to the sector bounded by the lines arg $( \mathrm { z } ) { = } 0$ $\arg ( z ) = 2 \pi / \alpha$ and a circle of large radius. This expresses $1 - e ^ { 2 \pi i / \alpha }$ times the integral as 2πi times the residue $- e ^ { \pi i / \alpha } / \alpha$ at $z = e ^ { \pi i / \alpha }$ . So the integral is $\frac { \pi } { \alpha \sin ( \pi / \alpha ) }$

3B Let F be a field and p a prime. For $n \geq 1$ show that the number (up to isomorphism) of abelian groups of order $p ^ { n }$ equals the number (up to similarity) of $n \times n$ matrices A over $F$ such that $A ^ { n } = 0$

Solution:An abelian group of order $p ^ { n }$ is a direct sum of groups $G _ { i }$ of the form $\mathbf { Z } / p ^ { d _ { i } }$ , and determined up to isomorphism by, for each $d \leq n$ , how many i have $d _ { i } = d .$

For A a n×n matrix, viewed as operating on $V = F ^ { n }$ , V is the direct sum of A-invariant subspaces $V _ { i }$ of dimension $d _ { i }$ where on $V _ { i } ~ A$ has minimal polynomial $q _ { i } ( x )$ of degree $d _ { i }$ (with $q _ { i } ( x ) = \mathrm { a }$ power of a monic irreducible). Since $A ^ { n } = 0$ , also $A ^ { n } v = 0$ for $v \in V _ { i }$ so the minimal polynomial $q _ { i } ( x )$ divides $x ^ { n }$ . Thus $q _ { i } ( x ) = x ^ { d _ { i } }$ . Up to similarity A is classified by, for each polynomial $q ( x )$ , how many i have $q _ { i } ( x ) = q ( x )$ , or equivalently, for each $d \leq n$ , how many $V _ { i }$ have dimension $d _ { i }$

In both cases, the sum of all the $d _ { i }$ must equal n. So both are counted in the same way, by the number of partitions of $n$

4B How many complex non-real zeros does the polynomial $z ^ { 1 1 } - 3 z ^ { 3 } +$ 1 have with $1 \leq | z | \leq 2 ?$

Solution: By Runge’s theorem, there are 11 zeros with $| z | \le 2$ as $\left| z ^ { 1 1 } \right|$ has 11 zeros in this region and dominates the rest of the polynomial. There are 3 zeros with $| z | < 1$ as $| 3 z ^ { 3 } |$ has 3 zeros in this region and dominates the rest of the polynomial. So there are $8$ zeros in the region $1 \le | z | \le 2$ . Sketching the graph of $f$ shows that exactly two of these 6 zeros are real (more precisely, $f$ is monotonic on each of the intervals [1, 2] and $[ - 2 , - 1 ]$ and changes sign on each of them, so it has exactly one zero in each interval.) So $f$ has 6 complex non-real zeros in the region.

5B Prove that the quotient of the general linear group $G L _ { 2 } ( \mathbb { Z } / 3 \mathbb { Z } )$ by its center is isomorphic to the symmetric group $S _ { 4 }$ on 4 points.

Solution:An invertible linear transformation of $( \mathbb { Z } / 3 \mathbb { Z } ) ^ { 2 }$ permutes the set of 4 subspaces of dimension 1 (with $\mathrm { \mathrm { \Omega ^ { \circ } s l o p e s ^ { \prime \prime } 0 , 1 , - 1 } }$ , and $\infty )$ . This defines a homomorphism $G L _ { 2 } ( \mathbb { Z } / 3 \mathbb { Z } ) \to S _ { 4 }$ . Since the transformations preserving each of the coordinate lines correspond to diagonal matrices, and those of them which preserve the graph of the identity map are scalar, we see that the kernel of the homomorphism coincides with the center of the matrix group, consisting of all invertible scalar matrices. Over $\mathbb { Z } / 3 \mathbb { Z }$ , these are $\pm I$ . The order of the quotient group is $( 3 ^ { 2 } - 1 ) ( 3 ^ { 2 } - 3 ) / 2 = 2 4 = | S _ { 4 } |$ , which shows that the quotient by the center is mapped bijectively onto $S _ { 4 }$

6B Show that

$$
\int _ { 0 } ^ { 1 } { \frac { 1 } { x ^ { x } } } d x = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { n } } } .
$$

(Hint: Write $x ^ { x }$ in terms of the exponential and logarithm functions, and evaluate the integral $\textstyle \int _ { 0 } ^ { 1 } x ^ { s } \log ( x ) ^ { n } d x . )$

Solution: Integration by parts shows that $\begin{array} { r } { \int _ { 0 } ^ { 1 } x ^ { s } \log ( x ) ^ { n } d x = - ( n / ( s + } \end{array}$ $\textstyle 1 ) ) \int _ { 0 } ^ { 1 } x ^ { s } \log ( x ) ^ { n - 1 } d x$ , and repeating this n times shows that it is equal to $\begin{array} { r } { n ! ( - 1 / ( s + 1 ) ) ^ { n } \int _ { 0 } ^ { 1 } x ^ { s } d x = n ! ( - 1 ) ^ { n } / ( s + 1 ) ^ { n + 1 } } \end{array}$ . The identity follows from this by expanding $x ^ { - x }$ as $\textstyle \sum _ { n \geq 0 } ( - x \log ( x ) ) ^ { n } / n !$ and integrating term by term (which is justified as all terms are positive).

7B (a) Prove that $\alpha = \sqrt { 3 } + \sqrt { 2 }$ is algebraic over Q by writing down a polynomial $f ( x ) \in \mathbf { Q } [ x ]$ of degree 4 having α as a root. (b) Show that $f ( x )$ is irreducible over Q.

Solution: For (a) take $f ( x )$ to be

$$
\begin{array} { c } { { ( x - ( \sqrt { 3 } + \sqrt { 2 } ) ) ( x + ( \sqrt { 3 } + \sqrt { 2 } ) ) ( x - ( \sqrt { 3 } - \sqrt { 2 } ) ) ( x + ( \sqrt { 3 } + \sqrt { 2 } ) ) } } \\ { { { } } } \\ { { = x ^ { 4 } - 1 0 x ^ { 2 } + 1 . } } \end{array}
$$

For (b) note that if $f ( x )$ factors over Q then some product of two of the factors of the above factorization into linear terms over C must be in $\mathbb { Q } [ x ]$ On the other hand, by direct computation no two of the above linear terms multiply together to give a polynomial with rational coefficients.

8B We have a fair N-sided die. One side is black and others are white. Let $n ( N )$ be the smallest number of throws so the probability of getting at least one black is bigger than $1 / 2$ . Compute

$$
\operatorname* { l i m } _ { N \to \infty } \frac { n ( N ) } { N } .
$$

Solution:The probability of getting only whites in n throws is $\left( 1 - { \frac { 1 } { N } } \right) ^ { n }$ so we want the smallest integer n so

$$
\left( 1 - \frac { 1 } { N } \right) ^ { n } < \frac { 1 } { 2 }
$$

or equivalently

$$
\frac { n } { N } > \frac { - \log 2 } { N \log \left( 1 - \frac { 1 } { N } \right) } \to \log 2 \mathrm { ~ a s ~ } N \to \infty .
$$

Hence,

$$
\operatorname* { l i m } _ { N  \infty } \frac { n ( N ) } { N } = \log 2 \approx 0 . 6 9 .
$$

9B Let $n \geq 2$ be an integer such that $2 ^ { n } + n ^ { 2 }$ is prime. Show that $n \equiv 3 { \pmod { 6 } }$

Solution: Let $p$ denote the prime $2 ^ { n } + n ^ { 2 }$ . The prime $p$ is odd as $n \geq 2$ . Therefore we find that $n ^ { 2 } \equiv 1$ (mod 2) so n is odd. It therefore suffices to show that $3 | n$ . Suppose 3 does not divide n. Then we have

$$
2 ^ { n } + n ^ { 2 } \equiv ( - 1 ) ^ { n } + 1 { \pmod { 3 } } .
$$

Now this expression is not zero mod 3 as 3 does not divide p since $p$ is prime and greater than 8 (by the assumption on n). Therefore n is even contradicting the earlier result that shows that n is odd. Therefore we must have 3|n.