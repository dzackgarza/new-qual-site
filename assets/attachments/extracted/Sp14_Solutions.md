# Department of Mathematics, University of California, Berkeley

GRADUATE PRELIMINARY EXAMINATION, Part A

Spring Semester 2014

1. Please write your 1- or 2-digit student exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q .$

4. No notes, books, or calculators may be used during the exam.

## PROBLEM SELECTION

Part A: List the six problems you have chosen:

## GRADE COMPUTATION

1A.

1B.

2A.

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

Find the sum of the series $\begin{array} { r } { \frac { 1 } { 1 \times 2 \times 3 } + \frac { 1 } { 2 \times 3 \times 4 } + \frac { 1 } { 3 \times 4 \times 5 } + \cdot \cdot \cdot } \end{array}$

Solution: Use the partial fraction decomposition $\begin{array} { r } { \frac { 1 } { ( n - 1 ) n ( n + 1 ) } = \frac { 1 / 2 } { n - 1 } - \frac { 1 } { n } + \frac { 1 / 2 } { n + 1 } } \end{array}$ and rearrange to find that the sum of the first m terms is $1 / 4 - \dot { 1 / 2 } \dot { ( m + 1 ) } ( m + 2 )$ so the sum of all terms is $1 / 4$

Please cross out this problem if you do not wish it graded

<table><tr><td></td></tr><tr><td>Problem 2A. Score:</td></tr></table>

Prove or disprove that there is a sequence $\left\{ f _ { n } \right\}$ of continuous functions on R such that for any rational x the sequence $f _ { n } ( x )$ is bounded but the sequence $f _ { n } ( x + { \sqrt { 2 } } )$ is unbounded.

Solution: There is such a sequence. Number the rationals as $r _ { 1 } , r _ { 2 } , . . . ,$ and choose $f _ { n }$ so that if x is one of the first n rational numbers then $f _ { n } ( x ) = 0$ and $f _ { n } ( x + { \sqrt { 2 } } ) = n$ . Another solution is to set $f _ { n } ( x ) = k$ if x is rational with denominator $k \leq n$ , and extend $f _ { n }$ to all reals by linear interpolation. Then the sequence $f _ { n } ( x )$ is eventually k if x has denominator k but tends to +∞ if x is irrational.

## Problem 3A.

Score:

Find a real number c so that

$$
\left| c - \int _ { - 1 / 2 } ^ { 1 / 2 } \frac { \exp ( x ) - 1 } { x } d x \right| < 0 . 0 1
$$

Solution: The integral is given by integrating the power series term by term, so is ${ \frac { 1 } { 2 ^ { 0 } \times 1 \times 1 ! } } +$ $\textstyle { \frac { 1 } { 2 ^ { 2 } \times 3 \times 3 ! } } + { \frac { 1 } { 2 ^ { 4 } \times 5 \times 5 ! } } + \cdot \cdot \cdot$ . The sum of all but the first two terms is easily seen to be much less than $1 / 1 0 0$ , so we can take c to be the sum of the first two terms which is $7 3 / 7 2 = 1 . 0 1 3 8 8 8 8 \cdot \cdot \cdot$ (A more accurate answer is 1.01399349965)

Please cross out this problem if you do not wish it graded

<table><tr><td>Problem 4A. Score:</td></tr></table>

Let $f$ be analytic on the closed unit disk, and assume that $| f ( z ) | \leq 1$ for all z’s in this set. Suppose also that $\begin{array} { r } { f ( \frac { 1 } { 2 } ) = f ( \frac { i } { 2 } ) = 0 } \end{array}$ . Prove that $\begin{array} { r } { | f ( 0 ) | \le \frac { 1 } { 4 } } \end{array}$

Solution: Set

$$
g ( z ) = { \frac { z - 2 } { 2 z - 1 } } { \frac { z - 2 i } { 2 z - i } } f ( z )
$$

Then $g$ is holomorphic inside the disc and $| g ( z ) | = | f ( z ) | \le 1 { \mathrm { ~ f o r ~ } } | z | = 1$ . Hence by the maximum principle we get $| g | \le 1$ . The conclusion follows.

<table><tr><td>Problem 5A. Score:</td></tr></table>

Let $f , g$ be meromorphic functions on C such that $| f ( z ) | \leq | g ( z ) |$ at all z where both are defined. Show there is a $c \in { \mathcal { C } }$ such that $f ( z ) = c g ( z )$ for all z where both are defined.

## Solution:

This is clear when $g = 0$ . Otherwise g has isolated poles and $f / g$ is meromorphic. But $| f / g | \le 1$ so all its poles are removable. So $f / g$ extends to a bounded entire function which must be constant.

Please cross out this problem if you do not wish it graded

<table><tr><td>Problem 6A. Score:</td></tr></table>

Let R be a finite ring (with 1) of characteristic p. For S a subring of R (not necessarily containing an identity element), S is a vector space over $F _ { p }$ . For $a \in S$ let $T _ { a } ^ { S } : S  S$ be the linear map $T _ { a } ^ { S } ( x ) = a x$

(a) Show: if $1 \in S$ then the minimal polynomial of $T _ { a } ^ { S } =$ the minimal polynomial of $T _ { a } ^ { R }$

(b) Give an example of $p , R , S , a$ where (a) is false.

## Solution:

(a) When $1 \in S$ , the map $a  T _ { a } ^ { S }$ has kernel 0. So the minimal polynomial of $T _ { a } ^ { S }$ is the minimal polynomial $p ( x )$ such that $p ( a ) = 0$ which depends only on a.

(b) $R = F _ { 2 } [ a ] / ( a ^ { 2 } ) , S = \{ 0 , a \}$ . min poly of $T _ { a } ^ { R } = x ^ { 2 } ;$ min poly of $T _ { a } ^ { S } = x$

<table><tr><td>Problem 7A. Score:</td></tr></table>

Let F be a finite field with q elements. A complete $f l a g$ in the vector space $F ^ { n }$ is a nested sequence of linear subspaces $\bar { V } ^ { 1 } \subset V ^ { 2 } \subset \cdots \subset \bar { V } ^ { n - 1 }$ of dimensions $1 , 2 , \ldots , n - 1$ respectively. Let $f _ { n } ( q )$ be the number of complete flags in $F ^ { n }$ as a function of $q .$ Find the limit of $f _ { n } ( q )$ as q tends to 1.

## Solution:

When the subpaces $V ^ { 1 } \subset \cdots \subset V ^ { k }$ are already selected, the subspace $V ^ { k + 1 }$ is determined by a 1-dimensional subspace in the quotient space $F ^ { n } / V ^ { k }$ of dimension $n - k$ . The numebr of such subspaces is equal to $( q ^ { n - k } - 1 ) / ( q - 1 )$ (non-zero vectors up to proportionality), which tends to $n { - } k$ as q tends to 1. Thus the answer is the product of $n { - } k$ over $k = 0 , 1 , 2 , \ldots , n { - } 1$ that is $n !$

Score:

Let G be a group of order 48. Show that G contains a normal subgroup of order 16 or 8.

## Solution:

Let $P \subset G$ be a 2-Sylow subgroup. Then $G / P$ has size 3 and left translation defines a homomorphism $h : G \to \operatorname { A u t } ( G / P ) = S _ { 3 }$ . Let K be the kernel. Then $K \subset P$ since any element $g \notin P$ acts nontrivial on the trivial coset, and the index of K in G divides 6. It follows that the size of K is 8 or 16.

<table><tr><td>Problem 9A. Score:</td></tr></table>

Let A be a finite abelian group (under +) and let R = End(A) be the ring of homomorphisms from A to A. Show there is a subring S of R such that A and S are isomorphic as abelian groups.

## Solution:

A is a product of cyclic groups Ci. For C finite cyclic, End(C) is isomorphic to C as groups. So S = the product of the End(Ci) works.

Spring Semester 2014

1. Please write your 1- or 2-digit student exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q$

4. No notes, books, or calculators may be used during the exam.

## PROBLEM SELECTION

Part B: List the six problems you have chosen:

<table><tr><td>Problem 1B. Score:</td></tr></table>

Let the continuously differentiable function $f : [ 0 , 1 ] ^ { 2 } \to \mathbb { R }$ on the unit square be given by the distance to a fixed point outside the square. Show that there there is no point $( x _ { 0 } , y _ { 0 } )$ in the square such that the gradient of the function $f$ at this point is equal to the average value of the gradient of the function $f .$ In other words the obvious analogue of the mean value theorem for functions of two variables is false. (Hint:first find the length of the gradient of f .)

## Solution:

The function f is continuously differentiable, and has non-constant gradient of unit length at every point in the square. The integral is not equal to the gradient of $f$ at any point since the average of different unit vectors cannot be a unit vector.

To justify the last claim, consider a continuous non-constant unit vector field $\vec { v }$ in the unit square $D ,$ and put $\begin{array} { r } { \vec { c } : = \int \int _ { D } \vec { v } ( x , y ) } \end{array}$ dxdy. Since $| \vec { c } | \geq \vec { c } \cdot \vec { v } ,$ where the equality holds true only at the points where $\vec { c }$ has the same direction as ${ \vec { v } } ,$ we find

$$
| \vec { c } | > \int \int _ { D } \vec { c } \cdot \vec { v } ( x , y ) \ d x d y = \vec { c } \cdot \int \int _ { D } \vec { v } ( x , y ) \ d x d y = | \vec { c } | ^ { 2 } .
$$

Hence $| \vec { c } | < 1$

<table><tr><td>Problem 2B. Score:</td></tr></table>

Prove that a non-empty closed convex subset of the real vector space Rn with the usual Euclidean distance has a unique element of minimum norm (distance to the origin).

Solution: We first check uniqueness: if a and b are two distinct points of the same minimum norm then their midpoint has smaller norm, and is in the set as the set is convex: contradiction. To show existence, take a nonzero intersection with some closed ball with center the origin. This intersection is compact, so the norm attains a minimum value.

## Problem 3B.

Score:

Prove that there exists a constant C such that for every polynomial P of degree 2014

$$
P ( 0 ) \leq C \int _ { 0 } ^ { 1 } \left| P ( x ) \right| d x .
$$

## Solution:

In the space of polynomials of degree $\leq 2 0 1 4 , \ P \ \mapsto \ P ( 0 )$ is a linear function, and $\textstyle P \mapsto \| P \| : = \int _ { 0 } ^ { 1 } | P ( x ) | d$ x is a continuous homogeneous function of degree 1 vanishing only at the origin. Thus, it suffices to take C to be the maximum of the linear function on the compact subset $\{ P | \| P \| \leq 1 \}$

To justify continuity of $\| \cdot \|$ , consider a sequence $P _ { n } = P + \Delta P _ { n }$ such that $\Delta P _ { n } \to 0$ coefficientwise. We have

$$
\int _ { 0 } ^ { 1 } | \sum c _ { k } x ^ { k } | d x \leq \sum | c _ { k } | \int _ { 0 } ^ { 1 } x ^ { k } d x = \sum { \frac { | c _ { k } | } { k } } ,
$$

and hence $\| \Delta P _ { n } \| \to 0$ . Then by the triangle inequality

$$
| \| P _ { n } \| - \| P \| | \leq \int _ { 0 } ^ { 1 } | | P _ { n } ( x ) | - | P ( x ) | | { \big . } d x \leq \int _ { 0 } ^ { 1 } | \Delta P _ { n } ( x ) | { \big . } d x = \| \Delta P _ { n } \|
$$

, and therefore $\| P _ { n } \| \to \| P \|$

## Problem 4B.

Score:

If f is an injective holomorphic function defined on the open unit disk U of the complex plane, show that the area of the image of U under f is $\int _ { U } | f ^ { \prime } | ^ { 2 } d x d y$ . Compute the area of the image of the unit disk U under the map $f ( z ) = z + ( \bar { z ^ { 2 } } ) / 2$

## Solution:

The area of the unit disk is given by the integral above, because $| { f ^ { \prime } } | ^ { 2 } = { f ^ { \prime } } { \overline { { f ^ { \prime } } } }$ is the amount by which f locally multiplies areas. If $f ( z ) = a _ { 0 } + a _ { 1 } z + \cdot \cdot$ · then this integral (evaluated in polar coordinates) is given by $\pi \sum n | a _ { n } ^ { 2 } |$ . The function $f ( z ) = z + ( z ^ { 2 } ) / 2$ is injective on the unit disk as $f ( z _ { 1 } ) = f ( z _ { 2 } )$ implies $z _ { 1 } = z _ { 2 }$ or $1 + ( z _ { 1 } + z _ { 2 } ) / 2 = 0$ , so the area of the image of the unit disk is $\pi ( 1 + 2 \times ( 1 / 2 ) ^ { 2 } ) = 3 \pi / 2$

## Problem 5B.

Score:

Find the integral $\int _ { 0 } ^ { \infty } { \frac { \cos x } { 1 + x ^ { 2 } } } d x .$

Solution: This is half the real part of $\int _ { - \infty } ^ { \infty } { \frac { e ^ { i x } } { 1 + x ^ { 2 } } } d x$ . Taking the usual semicircular contour in the upper half plane (and checking that the integral over the curved bit tends to 0) we see that this latter integral is 2πi times the residue at i. The residue is $\frac { e ^ { - 1 } } { 2 i }$ , so the original integral is $\pi / 2 e$

<table><tr><td></td></tr><tr><td>Problem 6B. Score:</td></tr></table>

Let n be an integer and let $O ( n )$ be the group of $n \times n$ orthogonal matrices. View $O ( n )$ as a topological group with the induced topology from the embedding $O ( n ) \subset \mathbb { R } ^ { n ^ { 2 } }$ given by the entries. Show that $O ( n )$ is compact.

## Solution:

Let group $O ( n )$ is realized as the intersection of the compact closed unit ball in $\mathbb { R } ^ { n ^ { 2 } }$ with the closed subsets characterized by the conditions $v _ { i } \cdot v _ { j } = 0$ for $i \neq j$ , where $v _ { i }$ denotes the i-th column vector.

## Problem 7B.

Score:

Let A be the matrix

$$
A = \binom { 5 / 2 0 - 1 / 2 } { 0 } \ 3 \ \quad 0 \quad \quad
$$

Calculate $A ^ { 1 6 }$ . (You may give your answer as a polynomial in A of degree at most 2.)

Solution: The minimal polynomial $m ( T )$ of A is equal to $T ( T - 2 ) ( T - 3 )$ . By the euclidian algorithm we can write

$$
T ^ { 1 6 } = p ( T ) m ( T ) + a T ^ { 2 } + b T + c ,
$$

for some polynomial p. Plugging in $T = 0$ we get $c = 0 , T = 2$ gives $2 ^ { 1 6 } = 4 a + 2 b$ , and $T = 3$ gives $3 ^ { 1 6 } = 9 a + 3 b$ . Solving these equations we get $a = 3 ^ { 1 5 } - 2 ^ { 1 5 }$ and $b = 3 \cdot 2 ^ { 1 5 } - 2 \cdot 3 ^ { 1 5 }$ Therefore

$$
A ^ { 1 6 } = a A ^ { 2 } + b A
$$

for these values of a and b.

<table><tr><td>Problem 8B. Score:</td></tr></table>

Let $B = C ^ { - 1 } A C$ , where A and C are n×n-matrices with integer entries, such that det $A = 1$ , and det $C \neq 0$ . Prove that there exists a positive integer m such that all entries of $B ^ { m }$ are integers.

## Solution:

Let $d = | \operatorname* { d e t } C |$ . Then $d C ^ { - 1 }$ is the adjoint matrix of C and thus has integer entries. Let m be the order of A in the finite group $G L _ { n } ( \mathbb { Z } / d \mathbb { Z } )$ of automorphisms of the abelian group $( \mathbb { Z } / d \mathbb { Z } ) ^ { n }$ Then $A ^ { m } = I + d \tilde { A }$ where $\tilde { A }$ has integer entries. Therefore $B ^ { m } = C ^ { - 1 } A ^ { m } C =$ $\dot { I } + d \dot { C } ^ { - 1 } \tilde { A } C$ has integer entries.

## Problem 9B.

Score:

Let G be a finite group acting on a finite set X with a single orbit. For an element $g \in G$ let $\operatorname { F i x } _ { g } ( X )$ denote the set $\{ x \in X | g ( x ) = x \}$

(a) Show that

$$
\# G = \sum _ { g \in G } \# \mathrm { F i x } _ { g } ( X ) .
$$

Hint: Count the set $S = \{ ( x , g ) \in X \times G | g x = x \}$ two ways.

(b) Show that if X has more than 1 point then there exists an element $g \in G$ fixing no points of X.

Solution:

Summing over x we get that the size of S is equal to

$$
\sum _ { x \in X } \operatorname { S t a b } ( x ) ,
$$

where $\operatorname { S t a b } ( x )$ is the stabilizer group of x. Summing over g first we get that the size of S is

$$
\sum _ { g \in G } \# \mathrm { F i x } _ { g } ( X ) .
$$

From the orbit stabilizer formula, and using the fact that we have just a single orbit, we have

$$
\sum _ { g \in G } \# \mathrm { F i x } _ { g } ( X ) = \# G
$$

as desired in (a). For (b) note that since $\mathrm { F i x } _ { e } ( X ) = X$ we from (a) that if $\operatorname { F i x } _ { g } ( X ) \neq \varnothing$ for all g that

$$
\# G \geq \# X + ( \# G - 1 ) > \# G ,
$$

a contradiction.