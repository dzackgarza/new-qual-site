# Department of Mathematics, University of California, Berkeley

## GRADUATE PRELIMINARY EXAMINATION, Part A

Fall Semester 2014

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if p 6= q.

4. No notes, books, or calculators may be used during the exam.

## PROBLEM SELECTION

Part A: List the six problems you have chosen:

## GRADE COMPUTATION

1A. 1B. Calculus

Real analysis

Real analysis

Complex analysis

5A. 5B. Complex analysis

6A. 6B. Linear algebra

7A. 7B. Linear algebra

Abstract algebra

9A.

9B.

Abstract algebra

Part A Subtotal: Part B Subtotal: Grand Total:

Please cross out this problem if you do not wish it graded

## Problem 1A.

Score:

Let $a ( n )$ be the number of ways that Harry Potter can buy a new broomstick valued at n knuts using bronze knuts, silver sickles worth 29 knuts, and gold galleons worth 17 sickles. Find $\textstyle \sum _ { n } a ( n ) z ^ { n }$ and $\scriptstyle \operatorname* { l i m } _ { n \to \infty } a ( n ) / n ^ { 2 }$

Solution: The sum is $1 / ( 1 - z ) ( 1 - z ^ { 2 9 } ) ( 1 - z ^ { 1 7 \times 2 9 } )$ . The asymptotic behavior of $a ( n )$ is dominated by the highest order pole of the partial fraction decomposition of this rational function, which is the order 3 pole at $z ~ = ~ 1$ . The leading term of the partial fraction decomposition of this near $z = 1$ is $1 / ( 1 7 \times 2 9 ^ { 2 } \times ( 1 - z ) ^ { 3 } )$ , and $1 / ( 1 - z ) ^ { 3 }$ has the expansion $1 + 3 z + 6 z ^ { 2 } + 1 0 z ^ { 3 } + \cdot \cdot$ · whose coefficients are triangular numbers $( n + 1 ) ( n + 2 ) / 2$ asymptotic to $n ^ { 2 } / 2$ . So the limit above is $1 / ( 1 7 \times 2 9 ^ { 2 } \times 2 )$

Please cross out this problem if you do not wish it graded

## Problem 2A.

Score:

Suppose that $f _ { n }$ is a sequence of non-negative continuous functions on the unit interval. Find counterexamples to three of the following four inequalities:

$$
\operatorname* { l i m } _ { n } \operatorname* { s u p } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \leq \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n } \operatorname* { s u p } f _ { n } ( x ) d x
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { s u p } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \geq \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n } \operatorname* { s u p } f _ { n } ( x ) d x
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { i n f } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \leq \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n } \operatorname* { i n f } f _ { n } ( x ) d x
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { i n f } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \geq \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n } \operatorname* { i n f } f _ { n } ( x ) d x
$$

(The remaining inequality always holds; you do not need to prove this.)

Solution: For numbers 1 and 3 take a sequence of functions $f _ { n }$ that have integral 1 but vanish for $x \ge 1 / n$ . For numbers 2 and 3 take $f _ { n } ( x )$ to be x for n even and $1 - x$ for n odd.

(The remaining inequality holds by Fatous lemma.)

## Problem 3A.

Score:

Suppose that f is a twice-differentiable real-valued function on the real line such that $| f ( x ) | \leq$ 1 and $| f ^ { \prime \prime } ( x ) | \le 1$ for all x. Find, with proof, a constant b such that $| f ^ { \prime } ( x ) | < b$ for all x.

Solution: Suppose $f ^ { \prime } ( x ) = M \geq 0$ Since $| f ^ { \prime \prime } | \le 1$ , f 0 must be greater than a triangular function with peak of height M and sides of slope ±1, which has total area $M ^ { 2 }$ . So f must vary more than this, so $M ^ { 2 } < 2$ as f varies by at most 2. So $b = { \sqrt { 2 } }$ will do. (It is also clear from the proof that this is best possible.)

Please cross out this problem if you do not wish it graded

## Problem 4A.

Score:

Let D be the set consisting of the open unit disk together with the point 1. Show that the power series

$$
\sum _ { n > 0 } z ^ { 3 ^ { n } } / n - z ^ { 2 \times 3 ^ { n } } / n
$$

converges at all points of D. By examining points with argument of the form $\pi / 3 ^ { k }$ , show that the function it converges to is not continuous.

Solution: Convergence on the open disk follows from the ratio test, and convergence at 1 follows from the alternating series test (and is trivial anyway). To show the function is not continuous at 1, look at it on lines of argument $\pi / 3 ^ { n }$ . On these lines, apart from a few terms, the absolute value of the function is bounded below by $\textstyle \sum | z | ^ { 3 ^ { n } } / n$ which tends to infinity as |z| tends to 1 by divergence of the harmonic series. So the function is unbounded in any neighborhood of the point 1, so cannot be continuous there.

## Problem 5A.

Score:

(a) Suppose that $P ( z ) = c ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { n } )$ is a complex polynomial. If z has positive real part and all the roots $a _ { i }$ have negative real part, show that $P ^ { \prime } ( z ) / P ( z )$ has positive real part.

(b) Show that all the roots of the derivative $P ^ { \prime }$ of a complex polynomial lie in the convex hull of the roots of P .

Solution: Part (a) follows by writing $P ^ { \prime } / P = \sum 1 / ( z - a _ { i } )$ and observing that all the terms in the sum have positive real part.

By part (a), if all roots of P have negative real part then so do all roots of its derivative. By a linear change of variable, this shows that if all roots of P are on one side of some straight line, then so are all roots of its derivative. This is another way of saying that all roots of the derivative are in the convex hull of the roots of P .

## Problem 6A.

Score:

Find the order of the group of linear transformations preserving a non-degenerate skewsymmetric bilinear form on a 4-dimensional vector space over the field with 3 elements, and find the number of such forms.

## Solution:

The order of the automorphism group is $( 3 ^ { 4 } - 1 ) \times 3 ^ { 3 } \times ( 3 ^ { 2 } - 1 ) \times 3 ^ { 1 }$ (number of nonzero choices of vector times choices for vector having scalar product 1 with it times number of choices of nonzero vectors with scalar product 0 with both of these times the number of vectors having scalar product 0 with the first 3 vectors and 1 with the third). The general linear group acts transitively on these sorts of forms. So the total number of such forms is the order $( 3 ^ { 4 } - 1 ) \times ( 3 ^ { 4 } - 3 ) \times ( 3 ^ { 4 } - 3 ^ { 2 } ) \times ( 3 ^ { 4 } - 3 ^ { 3 } )$ of the general linear group divided by the order above, which is $( 3 ^ { 3 } - 1 ) \times 3 ^ { 2 } \times ( 3 - 1 )$

## Problem 7A.

Score:

Find a basis of the intersection of the subspace of $\mathbb { R } ^ { 4 }$ spanned by (1, 1, 0, 0), (0, 1, 1, 0), $( 0 , 0 , 1 , 1 )$ and the subspace spanned by (1, 0, t, 0), (0, 1, 0, t), where t is given.

## Solution:

The first subspace consists of the vectors $( a , b , c , d )$ such that $a - b + c - d = 0$ , while the second subspace consists of all vectors of the form $( x , y , t x , t y )$

The intersection is then the set of the vectors in the second subspace satisfying $( x - y ) ( 1 + t ) = 0 . { \mathrm { ~ H ~ } } t \neq - 1$ , the intersection is one-dimensional and is spanned by $( 1 , 1 , t , t )$ $\operatorname { I f } t = - 1$ , the intersection is the second subspace and (1, 0, t, 0), (0, 1, 0, t) is a basis.

<table><tr><td>Problem 8A. Score:</td></tr></table>

Let X be a totally ordered set, (i.e. equipped with a non-reflexive, transitive binary relation < such that for every $x \neq y ,$ , either $x < y$ or $y < x )$ . Let L(X) denote the set of subsets $S \subseteq X$ with the property that for all $y \in S$ and $x < y , x \in S$ . Find, with proof:

(a) a countably infinite totally ordered set X for which L(X) has the smallest possible cardinality;

(b) a countably infinite totally ordered set X for which L(X) has the largest possible cardinality.

## Solution:

(a) If $X = \mathbb { Z }$ is the set of integers with its usual ordering, then $L ( X )$ is countably infinite, as every set $S \in L ( X )$ is either empty, equal to X, or has the form $S _ { x } = \{ y \in X \mid y \leq x \}$ This is the smallest possible cardinality, since for any X, the sets $S _ { x }$ are distinct and belong to L(X), so L(X) is infinite.

(b) If $X = \mathbb { Q }$ is the set of rational numbers with its usual ordering, then $L ( X )$ has the cardinality of the set R of real numbers. In fact, for every $x \in \mathbb { R }$ , the set $S _ { < x } = \{ y \in X \mid$ $y < x \}$ belongs to L(X) and these sets are distinct. This shows that $| L ( X ) | \geq | \mathbb { R } |$ . On the other hand, $L ( X )$ is a subset of the power set $P ( X )$ , and $| P ( X ) | = | \mathbb { R } |$ for every countably infinite set X. This shows both that $| L ( X ) | = | \mathbb { R } |$ in the case X = R, and that |R| is the largest possible cardinality.

## Problem 9A.

Score:

(a) By counting the number of pairs $( g , x )$ with $g \in G , x \in X , g ( x ) = x$ , show that the number of orbits of a finite group G acting on a finite set X is the average number of fixed points of elements of the group.

(b) In how many ways (up to symmetries of the hexagon) can one color the vertices of a regular hexagon using 4 colors?

## Solution.

(a) We can assume there is just one orbit, so have to show that the total number of fixed points of all elements of $G$ is the order of G. This follows by summing the pairs $( g , x )$ with $g ( x ) = x$ in two different ways. Looking at g the sum is the total number of fixed points of all group elements, and looking at x shows that the sum is the number of elements in the orbit times the order of the subgroup fixing a point, which is the order of G.

(b) We have the dihedral group of order 12 acting on a set with $4 ^ { 6 }$ points, and want to know the number of orbits. The identity has $4 ^ { 6 }$ fixed points, rotations through $\pm 6 0 ^ { \circ }$ have 4 fixed points each, through $\pm 1 2 0 ^ { \circ }$ have $4 ^ { 2 }$ fixed points each, the rotation through $1 8 0 ^ { \circ }$ has $4 ^ { 3 }$ fixed points, three reflections about lines passing through the midpoints of opposite sides have $4 ^ { 3 }$ fixed points each, and three reflactions about the lines passing through opposite vertices have $4 ^ { 4 }$ fixed points each. Thus the number of orbits is:

$$
\frac { 4 ^ { 6 } + 2 \cdot 4 + 2 \cdot 4 ^ { 2 } + 4 ^ { 3 } + 3 \cdot 4 ^ { 3 } + 3 \cdot 4 ^ { 4 } } { 1 2 } = \frac { 1 0 2 4 + 2 + 8 + 1 6 + 4 8 + 1 9 2 } { 3 } = \frac { 1 2 9 0 } { 3 } = 4 3 0 .
$$

Fall Semester 2014

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q .$

4. No notes, books, or calculators may be used during the exam.

## PROBLEM SELECTION

Part B: List the six problems you have chosen:

Please cross out this problem if you do not wish it graded

## Problem 1B.

Score:

Using induction or otherwise, show that the polynomial $P _ { n } ( x ) = 1 + x ^ { 1 } / 1 ! + . . . + x ^ { n } / n !$ has exactly 1 real zero if n is odd and none if n is even.

Solution: Use induction on n. The derivative of $P _ { n }$ is $P _ { n - 1 } { \mathrm { . } }$ so the number of zeros of $P _ { n }$ is at most 1 more than that of $P _ { n - 1 }$ . This proves the result for n odd, as a polynomial of odd degree has at least one zero. For n even, we have $P _ { n } ( x ) = P _ { n - 1 } ( x ) + x ^ { n } / n ! \geq P _ { n - 1 } ( x )$ , so $P _ { n }$ is positive at its unique minimum (where $P _ { n - 1 } ( x ) = 0 )$ , and therefore has no zeros.

Please cross out this problem if you do not wish it graded

## Problem 2B.

Score:

Either prove or describe a counterexample to the following statement: If a continuous realvalued function on the plane is bounded on all straight lines then it is bounded.

## Solution:

The statement is false. A counterexample is given by a function which is 0 except within a distance 1 of the set of points (x, x2), where it has value x.

Please cross out this problem if you do not wish it graded

<table><tr><td>Problem 3B. Score:</td></tr></table>

Let $f : [ 0 , 1 ] \times [ 0 , 1 ] \to \mathbb { R }$ be continuous and assume that for all $x \in [ 0 , 1 ]$ there is a unique $y _ { x }$ such that $f ( x , y _ { x } ) = \operatorname* { m a x } \{ f ( x , y ) ; y \in [ 0 , 1 ] \}$ . Let $g ( x ) = y _ { x }$ . Show that $g : [ 0 , 1 ]  [ 0 , 1 ]$ is continuous.

## Solution:

If $a _ { n }$ converges to a and $g ( a _ { n } )$ does not converge to $g ( a )$ then, since $[ 0 , 1 ]$ is compact, there is a subsequence $a _ { n _ { i } }$ such that $g ( a _ { n _ { i } } )$ converges to some $b \neq g ( a )$ . So $f ( a , b ) < f ( a , g ( a ) )$ But for i large enough $f ( a _ { n _ { i } } , g ( a _ { n _ { i } } ) )$ is close to $f ( a , b )$ while $f ( a _ { n _ { i } } , g ( a ) )$ is close to $f ( a , g ( a ) )$ . So for i large enough $f ( a _ { n _ { i } } , g ( a _ { n _ { i } } ) ) < f ( a _ { n _ { i } } , g ( a ) )$ . Contradiction.

Please cross out this problem if you do not wish it graded

## Problem 4B.

Score:

Find four power series $f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 }$ with radius of convergence 1 such that $f _ { 1 } , f _ { 2 }$ converge at 1 but $f _ { 3 } , f _ { 4 }$ do not, and the functions given by $f _ { 1 } , f _ { 3 }$ can be extended to functions holomorphic in a neighborhood of 1, but the functions given by $f _ { 2 } , f _ { 4 }$ cannot be.

## Solution:

$$
f _ { 1 } ( z ) = z - z ^ { 2 } / 2 + z ^ { 3 } / 3 - \cdot \cdot \cdot = \log ( 1 + z )
$$

(Alternating series test)

$$
f _ { 2 } ( z ) = z / 1 ^ { 2 } + z ^ { 2 } / 2 ^ { 2 } + z ^ { 3 } / 3 ^ { 2 } + \cdot \cdot \cdot
$$

(Integral test; derivative unbounded near $z = 1$ by divergence of harmonic series.) Or use $\begin{array} { r } { ( 1 - z ) \log ( 1 - z ) = - z + \sum _ { n > 1 } z ^ { n } / ( n - 1 ) n } \end{array}$

$$
f _ { 3 } ( z ) = 1 - z + z ^ { 2 } - \cdot \cdot \cdot = 1 / ( 1 + z )
$$

(Terms do not tend to 0)

$$
f _ { 4 } ( z ) = z + z ^ { 2 } / 2 + z ^ { 3 } / 3 + \cdot \cdot \cdot = - \log ( 1 - z )
$$

(Harmonic series diverges)

## Problem 5B.

Score:

Let f be a doubly-periodic meromorphic function: $f ( z + 1 ) = f ( z ) = f ( z + i )$ for all $z \in \mathbf { C }$ Let $z _ { a }$ be the zeroes of $f$ inside the unit square $0 < R e z , I m z < 1 , w _ { b }$ be its poles inside the square, and $k _ { a }$ and $l _ { b }$ be respective multiplicities. Assuming that f has no zeroes or poles on the boundary of the square, prove that

$$
\sum _ { a } k _ { a } z _ { a } - \sum _ { b } l _ { b } w _ { b } \in \mathbb { Z } [ i ] ,
$$

that is, is a Gaussian integer. Hint: Show that the following integral along the boundary of the square is a Gaussian integer:

$$
{ \frac { 1 } { 2 \pi i } } \oint z { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z .
$$

## Solution:

Due to periodicity, the integrals over the left and right edges add up to $\begin{array} { r } { ( 2 \pi i ) ^ { - 1 } \int _ { 0 } ^ { i } f ^ { \prime } ( 1 + } \end{array}$ $t ) / f ( 1 + t ) d t = ( 2 \pi i ) ^ { - 1 } [ \log f ( 1 + i ) - \log f ( 1 ) ] \in \mathbb { Z }$ (since branches of the logarithm differ by integer multiples of 2πi. Similarly, the integrals over the top and bottom edges add up to an imaginary integer. On the other hand, $z f ^ { \prime } / f$ has first order poles at $z _ { a }$ and $w _ { b }$ with the residues $z _ { a } k _ { a }$ and $- w _ { b } l _ { b }$ respectively. By the residue theorem, the contour integral is equal to their sum.

Please cross out this problem if you do not wish it graded

## Problem 6B.

Score:

Show that there is a sequence of $4 \times 4$ matrices $A ( n )$ with real entries, which converges to

$$
A = { \left( \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } \end{array} \right) }
$$

and such that $A ( n )$ has 4 distinct real eigenvalues, two of which are positive and two negative.

## Solution:

Let $D ( n )$ be a diagonal matrix diag $\cdot ( 1 / n , 2 / n , - 1 / n , - 2 / n )$ . Then computing the characteristic polynomial shows that $A + D ( n )$ has eigenvalues $1 / n , 2 / n , - 1 / n , - 2 / n$ and converges to A as $n \to \infty$ .

Please cross out this problem if you do not wish it graded

## Problem 7B.

Score:

Let n be a fixed positive integer, and define two n by n real symmetric matrices A and B to be equivalent if there is a non-singular real matrix C with $C A C ^ { T } = B$ (where $C ^ { T }$ is the transpose of C). How many equivalence classes are there?

Solution: This is asking for a classification of symmetric bilinear forms over the reals. By Sylvesters law of inertia these correspond to diagonal matrices with entries −1, 0, and 1 (with order not counting). So the number of equivalence classes is the number of solutions to $a + b + c = n$ in non-negative integers $a , b , c ,$ which is $( n + 1 ) ( n + 2 ) / 2$

## Problem 8B.

Score:

Determine, up to isomorphism, all finite groups G such that G has exactly three conjugacy classes.

## Solution:

Let $g = | G |$ . One of the conjugacy classes is $\{ 1 \}$ . Let r and s be the sizes of the other two. If g is odd, then, since r and s divide g, we have $r , s \le g / 3$ , hence $g = r + s + 1 \leq 2 g / 3 + 1$ which implies $g \le 3$ . In this case we must therefore have $g = 3$ , so G is the cyclic group of order 3, which (being abelian) has exactly three conjugacy classes. Otherwise, g is even, and $r , s \le g / 2$ . If r and s are both less than $g / 2$ , then $r , s \le g / 2 - 1$ , which contradicts $g = r + s + 1$ . So one of r and s, say s, is equal to $g / 2$ . Then we have $g = 2 r + 2$ . Since r divides g, this implies r divides 2, that is, $r = 1$ or $r = 2$ . If $r = 1$ , then $g = 4$ . But then G is abelian and has four conjugacy classes. Hence $r = 2$ , and G must be a group of order 6 with conjugacy classes of sizes 1, 2 and 3. Up to isomorphism, the unique non-abelian group of order 6 is the symmetric group $S _ { 3 }$ (isomorphic to the dihedral group of order 6), which does in fact have three conjugacy classes of these sizes. So the groups are: (i) the cyclic group of order 3, and (ii) the symmetric group $S _ { 3 }$ on 3 letters.

## Problem 9B.

Score:

How many roots does the polynomial $x ^ { 1 0 0 0 0 0 } { - 1 }$ have in the finite field $\mathbb { F } _ { 6 5 5 3 7 } ?$ $( 6 5 5 3 7 = 2 ^ { 1 6 } + 1$ is a prime.)

Solution. The roots all have multiplicity 1 as the polynomial is coprime to its derivative. We are looking for the number of units x in $\mathbb { F } _ { 6 5 5 3 7 }$ whose order divides 100000. Since 65537 is prime, the group $\mathbb { F } _ { 6 5 5 3 7 } ^ { \times }$ is cyclic of order $2 ^ { 1 6 }$ . Thus the order of x, which is a power of 2 not exceeding the 16th, must be a divisor of $1 0 0 0 0 0 = 2 ^ { 5 } \cdot 5 ^ { 5 }$ . Thus the roots are those elements x which satisfy $x ^ { 2 ^ { 5 } } = 1$ . In the cyclic group of order $2 ^ { 1 6 }$ , there are $2 ^ { 5 } = 3 2$ such elements.