Suppose $f : \mathbb { R } \to \mathbb { R }$ is a bounded continuous function. Calculate the limit

$$
\operatorname * { l i m } _ { \epsilon  0 ^ { + } } \int _ { - \infty } ^ { \infty } f ( t ) \frac { \epsilon } { \epsilon ^ { 2 } + t ^ { 2 } } d t
$$

Solution: Multiplying t by  gives the limit as

$$
\operatorname* { l i m } _ { \epsilon \to 0 ^ { + } } \int _ { - \infty } ^ { \infty } f ( \epsilon t ) \frac { 1 } { 1 + t ^ { 2 } } d t
$$

which as  tends to 0 becomes

$$
f ( 0 ) \int _ { - \infty } ^ { \infty } \frac { 1 } { 1 + t ^ { 2 } } d t = \pi f ( 0 )
$$

## Problem 2A.

Score:

Suppose that f is a smooth real function defined for all real $x ,$ such that $| f ^ { \prime } ( x ) | \geq \epsilon > 0$ and $| f ^ { \prime \prime } ( x ) | \leq M > 0$ for all x.

(1) Show that f has a unique zero z.

(2) Given $x _ { 0 } ,$ define a sequence by $x _ { n + 1 } = x _ { n } - f ( x _ { n } ) / f ^ { \prime } ( x _ { n } )$ . Show that

$$
| x _ { n + 1 } - z | \leq | x _ { n } - z | ^ { 2 } M / \epsilon .
$$

(Hint: $\begin{array} { r } { f ( x _ { n } ) = \int _ { z } ^ { x _ { n } } f ^ { \prime } ( x ) d x . ) } \end{array}$

(3) Show that the sequence $\{ x _ { n } \}$ converges to the zero z of f provided that $| f ( x _ { 0 } ) | < \epsilon ^ { 2 } / M$

Solution: Part 1 follows from the intermdiate value theorem and Rolles theorem in the usual way.

For part $2$ we can assume $z = 0$ . Then

$$
x _ { n } f ^ { \prime } ( x _ { n } ) - f ( x _ { n } ) = \int _ { 0 } ^ { x _ { n } } ( f ^ { \prime } ( x _ { n } ) - f ^ { \prime } ( x ) ) d x
$$

which has absolute value at most $| x _ { n } | \times | x _ { n } | M \leq x _ { n } ^ { 2 } M$ so

$$
| x _ { n + 1 } | \leq | x _ { n } | ^ { 2 } M / \epsilon .
$$

For part 3, note that part 2 shows that each term of the sequence $| x _ { n } - z | M / \epsilon$ is bounded by the square of the previous term, so the sequence tends to zero if the first term is less than 1, which follows from $| f ( x _ { 0 } ) | < \epsilon ^ { 2 } / M$

## Problem 3A.

Score:

Show that $\begin{array} { r } { \int _ { 0 } ^ { \infty } x \exp ( - x ^ { 6 } ( \sin x ) ^ { 2 } ) } \end{array}$ dx is finite.

Solution: More generally, the convergence of the integral $\begin{array} { r } { \int _ { 0 } ^ { \infty } x ^ { \alpha } \exp ( - x ^ { \beta } ( \sin x ) ^ { 2 } ) } \end{array}$ dx depends on the size of the “spikes” at $x = n \pi$ where $\sin ( x ) = 0$ . The size of the spike at nπ is bounded by a constant times

$$
n ^ { \alpha } \int _ { - \infty } ^ { \infty } \exp ( - n ^ { \beta } x ^ { 2 } ) d x
$$

which is bounded by a constant times

$$
n ^ { \alpha - \beta / 2 } .
$$

So the integral converges if the series $\Sigma n ^ { \alpha - \beta / 2 }$ does, which is true if $\alpha - \beta / 2 < - 1$ , in particular if $\alpha = 1 , \beta = 6$

## Problem 4A.

Score:

Find

$$
\int _ { C } { \frac { \cosh ( \pi z ) } { z ( z ^ { 2 } + 1 ) } } d z
$$

when C is the circle $| z | = 2 ,$ , described in the positive sense.

Solution: The singularities inside of C are at $z = 0$ , i and −i. The residue at 0 is 1. The residues at i and −i are ${ \frac { 1 } { 2 } } .$ . The integral is 4πi.

## Problem 5A.

Score:

Let $n \geq 1$ and let $\{ a _ { 0 } , a _ { 1 } , \ldots , a _ { n } \}$ be complex numbers such that $a _ { n } \neq 0$ . For $\theta \in \mathbf { R }$ , define

$$
f ( \theta ) = a _ { 0 } + a _ { 1 } e ^ { i \theta } + a _ { 2 } e ^ { 2 i \theta } + . . . + a _ { n } e ^ { n i \theta } .
$$

Prove that there exists $\theta \in \mathbf { R }$ such that $| f ( \theta ) | > | a _ { 0 } |$

Solution: Suppose that the claim is false. Then for all $\theta \in \mathbf { R }$ , we have $| f ( \theta ) | \leq | a _ { 0 } |$ . Put $g ( z ) = a _ { 0 } + a _ { 1 } z + a _ { 2 } z ^ { 2 } + . ~ . ~ . + a _ { n } z ^ { n }$ so that $f ( \theta ) = g ( e ^ { i \theta } )$ . By the maximum modulus principle, applied to $K = \{ z \ : \ | z | \leq 1 \}$ , we know that |g| is maximized on some boundary point of $K$ . Hence $| g |$ also has an interior maximum at 0, so g must be a constant function. This contradicts the assumptions that $n \geq 1$ and $a _ { n } \neq 0$

Problem 6A.

Score:

Show that if V is a real vector space with a positive definite symmetric bilinear form $\langle \cdot , \cdot \rangle$ and $W \subset V$ is a linear subspace then $W ^ { \perp } = ( ( \bar { W } ^ { \perp } ) ^ { \perp } ) ^ { \perp }$ . Give an example such that $W \ne ( \dot { W } ^ { \perp } ) ^ { \perp }$

Solution: For any subspace we have $X \subset X ^ { \bot \bot }$ as X is orthogonal to $X ^ { \perp }$ , so applying this to $X = W ^ { \perp }$ shows that $W ^ { \perp } \subset ( ( W ^ { \perp } ) ^ { \perp } ) ^ { \perp }$ On the other hand, If $X \subset Y$ then $Y ^ { \bot } \subset X ^ { \bot }$ Applying this to X = W , $Y = W ^ { \perp \perp }$ shows that $( ( W ^ { \bot } ) ^ { \bot } ) ^ { \bot } \subset W ^ { \bot }$ . So $( ( W ^ { \perp } ) ^ { \perp } ) ^ { \perp } = W ^ { \perp }$

For the example, take $V = \ell ^ { 2 } ( \mathbb { N } )$ and $W \subset V$ the subspace of eventual ly 0 sequences. Then $W ^ { \perp } = \{ 0 \}$ so $( W ^ { \perp } ) ^ { \perp } = V$ but $( 1 , 1 / 2 , 1 / 3 , . . . ) \notin W$

## Problem 7A.

Score:

Let A be a matrix over the field of complex numbers. Suppose A has finite order, in other words $A ^ { m } = I$ for some positive integer m. Prove that A is diagonalizable. Give an example of a matrix of finite order over an algebraically closed field that is not diagonalizable.

Solution: By a standard theorem of linear algebra, A is diagonalizable if and only if its minimal polynomial has no repeated roots. The hypothesis implies that the minimal polynomial of A divides $X ^ { m } - 1$ . Hence it has distinct roots, since $X ^ { m } - 1$ does.

The matrix $\binom { 1 1 } { 0 1 }$ over an algebraically closed field of characteristic $p > 0$ has finite order $p$ but is not diagonalizable: both eigenvalues are 1, so if it were diagonalizable it would have to be the identity matrix.

Problem 8A.

Score:

Let m and n be integers greater than 1. Prove that $\log _ { m } ( n )$ is rational if and only if $m = l ^ { r }$ and $n = l ^ { s }$ , for some positive integers l, r, and s.

Solution: If $m = l ^ { r }$ and $n = l ^ { s }$ , then $\log _ { m } ( n ) = s / r$ . Conversely, suppose $\log _ { m } ( n ) = s / r ,$ where s and r are integers which we may assume coprime and positive $( n > 1$ implies $\log _ { m } ( n ) ~ > ~ 0 )$ Then $m ^ { s } \ = \ n ^ { r }$ By the fundamental theorem of arithmetic, the prime factorizations of m and n must be of the form $m = p _ { 1 } ^ { e _ { 1 } } \cdot \cdot \cdot p _ { k } ^ { e _ { k } } , n = p _ { 1 } ^ { f _ { 1 } } \cdot \cdot \cdot p _ { k } ^ { f _ { k } }$ , where $s e _ { i } = r f _ { i }$ for all i. Since r and s are coprime, this implies $e _ { i } = r h _ { i } , f _ { i } = s h _ { i }$ for some $h _ { i }$ . Hence $m = l ^ { r }$ and $n = l ^ { s }$ , where $l = p _ { 1 } ^ { h _ { 1 } } \cdot \cdot \cdot \overline { { p } } _ { k } ^ { h _ { k } }$

## Problem 9A.

Score:

Let K be a field. Let R be an integral domain which contains K and is finite-dimensional (as a vector space) over K. Prove that R is a field.

Solution: Let $x \in R , x \neq 0 .$ The map $m _ { x } \colon R \to R$ defined by $m _ { x } ( r ) = x r$ is a linear endomorphism of R as a vector space over K. Since R is an integral domain, the kernel of $m _ { x }$ is zero, $i . e . , m _ { x }$ is injective. Since R is finite-dimensional, this implies that $m _ { x }$ is surjective. Then the element y such that $m _ { x } ( y ) = 1$ is an inverse of x.

Alternate solution: the fact that R is an integral domain implies that the minimal polynomial $P ( X )$ of x over K is irreducible. In particular, its constant term c is non-zero. The identity $P ( x ) = 0$ can be rewritten as $x Q ( x ) = - c ,$ where $P ( X ) - c = X Q ( X )$ , so $y = - Q ( x ) / c$ is an inverse of x.

## Problem 1B.

Score:

Find $\textstyle \int _ { 0 } ^ { 1 }$ arctan(x)dx.

Solution: Integration by parts gives

$$
1 \times \arctan ( 1 ) - \int _ { 0 } ^ { 1 } \frac { x } { 1 + x ^ { 2 } } d x = \pi / 4 - ( \log 2 ) / 2 .
$$

## Problem 2B.

Score:

Prove that the intersection of a decreasing sequence of closed connected subsets of a compact metric space is connected. Give an example to show that this is false if the assumption that the space is compact is dropped.

## Solution:

Suppose that $X _ { 1 } , X _ { 2 } , \ldots$ is a decreasing sequence of closed connected subsets with intersection X. If X is not connected, it is the union of non-empty disjoint closed subsets Y and Z. Pick disjoint open subsets U and V containing $Y$ and Z. Then U, V , and the complements of the $X _ { i }$ form an open cover of a compact space, which therefore has a finite subcover, so some $X _ { i }$ is contained in the union of U and V . But this contradicts the fact that $X _ { i }$ is connected.

The sequence of connected subsets of the plane consisting of the union of the set $x = 0$ $x = 1 , y \geq n$ has disconnected intersection.

## Problem 3B.

Score:

Let g be 2π-periodic, continuous on $[ - \pi , \pi ]$ and have Fourier series

$$
{ \frac { a _ { 0 } } { 2 } } + \sum _ { n = 1 } ^ { \infty } ( a _ { n } \cos n x + b _ { n } \sin n x ) .
$$

Let f be 2π-periodic and satisfy the differential equation

$$
f ^ { \prime \prime } ( x ) + k f ( x ) = g ( x )
$$

where $k \neq n ^ { 2 } , n = 1 , 2 , 3 , . . . .$ Find the Fourier series of f and prove that it converges everywhere.

Solution:

$$
f ( x ) = { \frac { a _ { 0 } } { 2 k } } + \sum _ { n = 1 } ^ { \infty } ( { \frac { a _ { n } } { k - n ^ { 2 } } } \cos n x + { \frac { b _ { n } } { k - n ^ { 2 } } } \sin n x ) .
$$

This converges (uniformly) for all x as the numbers $a _ { n }$ and $b _ { n }$ are bounded, and the series $\textstyle \sum { \frac { 1 } { k - n ^ { 2 } } }$ converges.

## Problem 4B.

Score:

Let U be an open subset of C. Let K be a closed bounded subset of C that is contained in U . Put

$$
D = \operatorname* { m i n } _ { p \in K , q \notin U } | p - q | .
$$

That is, D is the closest distance between K and C − U . (If U = C then we put $D = \infty . )$

Suppose that f is an analytic function on U so that for all $z \in U$ , we have $| f ( z ) | \leq M$ Here M is a fixed positive number. Find an explicit number $C < \infty ,$ depending on M and D, so that for all $z _ { 0 } \in K$ we have $\left| f ^ { \prime } ( z _ { 0 } ) \right| \le C$ . Justify your answer.

Solution: Given $z _ { 0 } \in K$ and $r < D .$ , put $C _ { r } = \{ z : | z - z _ { 0 } | = r \}$ . Then $f$ is analytic in and on $C _ { r }$ . We have

$$
f ^ { \prime } ( z _ { 0 } ) = \frac { 1 } { 2 \pi i } \int _ { C _ { r } } \frac { f ( z ) } { ( z - z _ { 0 } ) ^ { 2 } } d z ,
$$

so $\begin{array} { r } { | f ^ { \prime } ( z _ { 0 } ) | \le \frac { 1 } { 2 \pi } \cdot \frac { M } { r ^ { 2 } } \cdot 2 \pi r = \frac { M } { r } } \end{array}$ . Taking $r  D$ , we can put $\begin{array} { r } { C = \frac { M } { D } } \end{array}$

## Problem 5B.

Score:

Which of the following domains are biholomorphically equivalent to each other: the complex plane $\mathbb { C } .$ , the unit disk $D \subset \mathbb { C }$ , the upper halfplane $\mathbb { H } \subset \mathbb { C } ?$ Write explicit biholomorphisms or prove they cannot exist.

Solution: An explicit biholomorphism $\phi : \mathbb { H }  D$ is given by

$$
\phi ( z ) = { \frac { z - i } { z + i } }
$$

If a holomorphic function $f : \mathbb { C } \to \mathbb { C }$ is bounded then it is constant. In particular, any holomorphic function $f : \mathbb { C } \to D \subset \mathbb { C }$ is constant and hence not a biholomorphism.

Problem 6B.

Score:

Show that the $n \times n$ (Cauchy) matrix with entries $1 / ( x _ { i } - y _ { j } )$ has determinant

$$
\frac { \prod _ { 1 \leq j < i \leq n } ( x _ { i } - x _ { j } ) ( y _ { j } - y _ { i } ) } { \prod _ { 1 \leq i , j \leq n } ( x _ { i } - y _ { j } ) }
$$

Solution: Multiplying the determinant by $\textstyle \prod _ { 1 \leq i , j \leq n } ( x _ { i } - y _ { j } )$ gives a polynomial of degree $n ( n - 1 )$ . This polynomial vanishes whenever two $x _ { \mathrm { ~ s ~ } } ^ { \prime }$ or two $y ^ { \prime } \mathrm { s }$ are equal so is divisible by $\Pi _ { 1 \leq j < i \leq n } ( x _ { i } - x _ { j } ) ( y _ { j } - y _ { i } )$ , and therefore equal to a constant times this as the degrees are the same. The constant can be checked to be 1 by looking at the coefficient of some monomial.

## Problem 7B.

Score:

Prove the following three statements about real $n \times n$ matrices.

1. If A is an orthogonal matrix whose eigenvalues are all different from −1, then $I + A$ is nonsingular and $S = ( I - A ) ( I + A ) ^ { - 1 }$ is skew-symmetric.

2. If S is a skew-symmetric matrix, then $A = ( I - S ) ( I + S ) ^ { - 1 }$ is an orthogonal matrix with no eigenvalue equal to −1.

3. The correspondence (called the Cayley transform) $A  S$ from Parts 1 and 2 is one-to-one.

Solution: For part 1, $S = I + A$ has no eigenvalues 0 so is non-singular. Its transpose is $( I + A ^ { T } ) ^ { - 1 } ( I - A ^ { T } ) = ( I + A ^ { - 1 } ) ^ { - 1 } ( I - \bar { A ^ { - 1 } } ) = ( A + I ) ^ { - 1 } ( A - I ) \stackrel {  } { = } - S$ so S is skew symmetric. Part 2 is similar to part 1 (noting that all eigenvalues of S are imaginary so $1 + S$ is invertible). Since the maps in parts 1 and 2 are inverses we get a 1:1 bijection.

Problem 8B.

Score:

Consider the symmetric group $\Sigma _ { n }$ in its presentation as $n \times n$ permutation matrices. Define the “expected trace” to be the weighted sum of traces

$$
E _ { n } = { \frac { 1 } { n ! } } \sum _ { g \in \Sigma _ { n } } { \mathrm { T r a c e } } ( g )
$$

Calculate $E _ { n } .$

Solution: The ith diagonal entry of the permutation matrix g is equal to 1 for exactly $( n - 1 ) !$ elements g since such g can be regarded as elements of $\Sigma _ { n - 1 }$ . Thus summing over i, we find $E _ { n } = n ( n - 1 ) ! / n ! = 1$

## Problem 9B.

Score:

If F is a finite field, show that more than half the elements of F are squares. Show that every element is the sum of 2 squares.

Solution: Any non-zero element has at most 2 square roots, so at least half the non-zero elements are squares. The element 0 is also a square, so more than half the elements are squares.

If b is any element of the finite field, then the sets of elements of the form $x ^ { 2 }$ and $b - y ^ { 2 }$ both contain more than half the elements of the field, so they have an element in common. So $x ^ { 2 } = b - y ^ { 2 }$ for some x and y, so b is the sum of the squares of x and y.