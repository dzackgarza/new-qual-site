Math prelim spring 2010 solutions

1A. Let X be a compact metric space. Let $f : X \to X$ be an isometry, i.e. $d ( f ( x _ { 1 } ) , f ( x _ { 2 } ) ) =$ $d ( x _ { 1 } , x _ { 2 } )$ for all $x _ { 1 } , x _ { 2 } \in X$ . Show that f is surjective. (Hint: If x is a point, show that one can find $m < n$ so that $f ^ { n } ( x )$ is close to $f ^ { m } ( x ) . )$

Solution. Suppose that x /∈ $I m a g e ( f )$ . Since X is compact and f is continuous, $f ( X )$ is compact, so there is some $\epsilon > 0$ such that the ball $B ( x , \epsilon ) \cap f ( X ) = \emptyset$

The sequence $\{ f ^ { i } ( x ) \} _ { i = 0 } ^ { \infty }$ has a convergent subsequence, so there are some $j , k \geq 0$ such that $j < k$ and $d ( f ^ { j } ( x ) , f ^ { k } ( x ) ) < \epsilon$ . Then $d ( x , f ^ { k - j } ( x ) ) < \epsilon$ , which is a contradiction.

2A.Let G be a group of order $2 0 1 0 = 2 \cdot 3 \cdot 5 \cdot 6 7$ . Determine how many subgroups of order 67 G can have, and give examples for each possible number.

Solution. By the Sylow theorems, this number (call it $m )$ is congruent to 1 mod 67 and divides $| G | = 2 0 1 0$ . (The latter fact holds because G acts transitively by conjugation on the set of $p { \mathrm { - } } { \mathrm { S y } }$ low subgroups of G.)

Since $6 7 \nmid m ,$ , we must have m | 30; in particular $m < 6 8$ and therefore $m = 1$ is the only possibility.

An example of a group G of order 2010 with exactly one subgroup of order $6 7$ is the cyclic group of order 2010.

3A. Suppose that $f$ is an entire function such that for all $z ,$

$$
| f ( z ) | \leq | z | ^ { 2 } .
$$

Find all possibilities for $f ,$ and justify your answer.

Solution. We know that

$$
f ^ { \prime \prime \prime } ( z _ { 0 } ) = { \frac { 3 ! } { 2 \pi i } } \int _ { C } { \frac { f ( z ) d z } { ( z - z _ { 0 } ) ^ { 4 } } } d z .
$$

Taking $C ~ \mathrm { t o }$ be a circle around the origin of radius R, we know that $| f ( z ) |$ is bounded by a constant times $R ^ { 2 }$ , and $\frac { 1 } { | z - z _ { 0 } | ^ { 4 } }$ decays like $R ^ { - 4 }$ . Since the length of C is $2 \pi R .$ , if we take R going to infinity then we get that $f ^ { \prime \prime \prime } ( z _ { 0 } ) = 0$ for all $z _ { 0 } .$ . So $f ( z ) = a z ^ { 2 } + b z + c$ for some constants $a , b , c .$ Since $| f ( z ) | \leq | z | ^ { 2 }$ holds for all z, we can also say that $b = c = 0$ and $| a | \le 1$ . So f is of the form $a z ^ { 2 }$ with $| a | \le 1$

4A. Let A and B be $n \times n$ real matrices such that $A ^ { 3 } = B ^ { 5 } = I _ { n }$ and $A B = B A$ . Show that $A + B$ is an invertible matrix.

Solution. Since A and B commute, the eigenvalues of $A + B$ are sums of eigenvalues of A and eigenvalues of B. The sum of a cube and a fifth root of 1 cannot be 0, so $A + B$ has no zero eigenvalues. Therefore it is invertible.

5A. Let $\boldsymbol { I } = \left( a , b \right)$ be an interval containing 1 and let $y = y ( t )$ be a $C ^ { \infty }$ function on I that satisfies the differential equation

$$
y ^ { \prime } = 2 ^ { y } - { \frac { 1 } { x } } .
$$

Prove rigorously that:

(a). If $y ( 1 ) > 0$ then $y$ is $\mathrm { ( s t r i c t l y ) }$ increasing on the interval $[ 1 , b )$

(b). The same conclusion holds if $y ( 1 ) = 0$

Solution. (a). It will suffice to show that $y ( x ) \geq 0$ for all $x \in ( 1 , b )$ , since then the differential equation would imply $y ^ { \prime } > 0$

From the differential equation, we have $y ^ { \prime } ( 1 ) > 0$ , so by the definition of derivative there is some $\epsilon > 0$ such that $y ( x ) > y ( 1 )$ for all $x \in ( 1 , 1 + \epsilon )$ Therefore if $y ( b ^ { \prime } ) < 0$ for some $b ^ { \prime } \in ( 1 , b )$ , then the maximum of the continuous function y on the closed (hence compact) interval $[ 1 , b ^ { \prime } ]$ must occur at a critical point $c \in ( 1 , b )$ . At that point, we will have $y ( c ) > 0$ and $y ^ { \prime } ( c ) = 0$ , contradicting the differential equation.

(b). From the differential equation, we now have $y ^ { \prime } ( 1 ) = 0$ , but since

$$
y ^ { \prime \prime } = 2 ^ { y } ( \log y ) y ^ { \prime } + \frac { 1 } { x ^ { 2 } } ~ ,
$$

we have $y ^ { \prime \prime } ( 1 ) > 0$ . Therefore $y ^ { \prime } ( x ) > 0$ for all $x \in ( 1 , 1 + \epsilon )$ for some $\epsilon > 0$ , so y is increasing on $[ 1 , 1 + \epsilon ]$ . Therefore if $y ( b ^ { \prime } ) < 0$ for some $b ^ { \prime } \in ( 1 , b )$ , then the maximum of y on $[ 1 , b ^ { \prime } ]$ must again occur at a critical point in $( 1 , b ^ { \prime } )$ , and the remainder of the proof proceeds as in (a).

6A.How many subfields does the splitting field of $x ^ { 5 } - 2$ over the rationals have?

Solution. The subfields correspond to subgroups of the Galois group of the polynomial, which is a semidirect product of cyclic groups of orders 4 and 5. The subgroups of order divisible by 5 all contain the normal subgroup of order 5, so correspond to subgroups of the quotient of order 4. So there is one of each of the orders 5, 10, 20. A subgroup of order not divisible by 5 must have order dividing 4, so lies in one of the 5 cyclic Sylow subgroups of order 4, whose non-trivial elements are disjoint. So there are 5 subgroups of order 2, 5 of order 4, and 1 of order 1. The total is 14 subgroups or subfields.

7A. Use residues to compute

$$
\int _ { 0 } ^ { \infty } { \frac { x \sin ( 2 x ) } { x ^ { 2 } + 3 } } d x .
$$

Solution. It’s enough to compute the imaginary part of

$$
{ \frac { 1 } { 2 } } \int _ { - \infty } ^ { \infty } { \frac { x e ^ { 2 i x } } { x ^ { 2 } + 3 } } d x .
$$

Put

$$
f ( z ) = { \frac { z e ^ { 2 i z } } { z ^ { 2 } + 3 } } .
$$

Using Jordan’s Lemma, we can apply the Cauchy residue theorem to a semicircle in the upper half plane and just compute residues. The only singularity in the upper half plane is√ at $z = \sqrt { 3 } i$ . The residue there is

$$
{ \frac { 1 } { 2 } } e ^ { - 2 { \sqrt { 3 } } } ,
$$

so the answer is

$$
{ \frac { \pi } { 2 } } e ^ { - 2 { \sqrt { 3 } } } .
$$

8A.Let V be a finite dimensional vector space over a field k, and let $T : V  V$ be a linear transformation. Let $W \subseteq V$ be a linear subspace such that T maps W to W . Show that the characteristic polynomial of $T _ { W }$ (the restriction of T to W ) divides the characteristic polynomial of T .

Solution. Choose a basis $B = \{ \mathbf { v } _ { 1 } , \ldots , \mathbf { v } _ { n } \}$ for V such that $B ^ { \prime } = \{ \mathbf { v } _ { 1 } , \ldots , \mathbf { v } _ { m } \}$ is a basis for W . Let A be the matrix for T relative to B; then A is a block matrix of the form

$$
\left[ \begin{array} { l l } { B } & { C } \\ { 0 } & { D } \end{array} \right] \ ,
$$

where B is the matrix for $T _ { W }$ relative to $B ^ { \prime }$ . Then the characteristic polynomial for T is

$$
\operatorname* { d e t } ( x I - A ) = \operatorname* { d e t } ( x I - B ) \operatorname* { d e t } ( x I - D ) ,
$$

which is a multiple of the characteristic polynomial det $( x I - B )$ of $T _ { W }$

9A.Find all solutions of the differential equation $x y ^ { \prime } + y = x$ for $x > 0$

Solution. Guessing polynomials as solutions shows that one solution is $y = x / 2$ . The solutions of the corresponding homogeneous equation are $y = c / x$ for constant c, by separation of variables. So the general solution is $y = c / x + x / 2$

1B.Show that the infinite series

$$
f ( x ) = \sum _ { n = 0 } ^ { \infty } { \frac { e ^ { i { \sqrt { n } } x } } { n ^ { 2 } + 1 } }
$$

converges uniformly for real x. Prove that the limit

$$
\operatorname* { l i m } _ { R \to + \infty } { \frac { 1 } { 2 R } } \int _ { - R } ^ { R } f ( x ) d x
$$

exists and calculate it.

Solution. The nth term is at most $1 / ( n ^ { 2 } + 1 )$ independently of x. As this series converges absolutely, the original series is uniformly convergent. Uniform convergence implies the limit exists and is given by the sum of the limits of the individual terms. The average value of the first term of f is 1, and the average values of the remaining terms are 0 as they are oscillating, so the limit is 1.

2B.Show that the ring of all $n \times n$ matrices over a field has no 2-sided ideals other than 0 and itself.

Solution. Suppose I is a non-zero ideal. Pick some element with a non-zero term. By using row and column operations (given by left and right multiplications) we can make all other entries 0. Applying row and column permutations then shows that I has an element that is 1 at some given position and 0 elsewhere. These form a basis, so I is the whole matrix ring.

3B.How many complex numbers z are there such that $| z | < 2$ , Im $( z ) > 0$ , and $z ^ { 7 } + e ^ { z } = 0 ?$

Solution. By Rouche’s theorem there are 7 roots of $z ^ { 7 } + e ^ { z }$ for $| z | < 2$ , as $| z ^ { 7 } | > | e ^ { z } |$ in this region. One is real, and the remaining ones occur in complex conjugate pairs, so there are 3 with positive imaginay part.

4B.Let A and B be complex square matrices of the same size. Prove or disprove each of the following statements:

If A and B are diagonalizable so is $A + B$

If A and B are diagonalizable so is $A B$

If $A ^ { 2 } = A$ then A is diagonalizable.

If AB is diagonalizable and invertible then so is BA.

Solution. False, False (pick any non-daigonalizable matrix for A+B or AB. Then almost any choice of diagonalizable A will do), True (min polynomial has no repeated roots), True (by conjugation)

5B.Show that if a continuous function f on [0, 1] has the property that

$$
\int _ { 0 } ^ { 1 } f ( x ) x ^ { n } d x = 0
$$

for all sufficiently large n then f is identically 0. (Hint: first do the case when this integral vanishes for all $n \geq 0 . )$

Solution. If the integral vanishes for $n > N$ , then by Stone-Weierstrass $x ^ { N } f$ is orthogonal to a dense subset of the continuous functions, so vanishes as it is continuous.

6B.Find the last decimal digit of

$$
7 ^ { 7 ^ { 7 ^ { 7 } } }
$$

Solution. $7 ^ { 7 }$ is odd, so $7 ^ { 7 ^ { 7 } }$ is 3 mod $\phi ( 1 0 ) = 4 { \it \Omega }$ so $7 ^ { 7 ^ { 7 ^ { 7 } } }$ is $7 ^ { 3 } \equiv 3$ mod 10.

7B.Find all residues of cot $\cdot ( z ) / z ^ { 2 }$ and use this to find the sum $1 / 1 ^ { 2 } + 1 / 2 ^ { 2 } + 1 / 3 ^ { 2 } + \cdot \cdot \cdot$

Solution. Residues are $1 / n ^ { 2 } \pi ^ { 2 }$ at nπ for non-zero integers n, and $- 1 / 3$ at 0. Integrating over a large square shows that the sum of the residues is 0, so $1 / 1 ^ { 2 } + 1 / 2 ^ { 2 } + \cdot \cdot \cdot = \pi ^ { 2 } / 6$

8B. If A is a Hermitian matrix such that $A ^ { 5 } + A = 2$ prove that A is the identity matrix.

Solution. The only real root of $x ^ { 5 } + x = 2$ is 1. As A is Hermitian, its eigenvalues are all real, so are all 1. Like all Hermitian matrices A is diagonalizable, so A is the identity matrix.

9B.Prove that if all edges of the complete graph on $\binom { m + n } { m }$ points are colored either red or blue, then there is either a complete red subgraph on $m + 1$ points or a complete blue subgraph on $n + 1$ points. (Hint: pick a point, divide the remaining points into two subsets, and use induction on $m + n . )$

Solution. Note that it is the EDGES not the VERTICES that are colored! Pick a point. There are either $\binom { m + n - 1 } { m - 1 }$ other points joined to x by a red line, or $\binom { m + n - 1 } { m }$ points joined to it by a blue line, as the sum of these 2 numbers is $\binom { m + n } { m }$ . In the first case these other points either contain a blue subgraph on $n + 1$ points or a red one on m points by induction on $m + n$ , when adding x to this set produces a red graph on $m + 1$ points. The second case is similar.