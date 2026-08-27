# Department of Mathematics, University of California, Berkeley

Fall Semester 2016

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q .$

4. No notes, books, calculators or electronic devices may be used during the exam.

## PROBLEM SELECTION

Part A: List the six problems you have chosen:

## GRADE COMPUTATION (for use by grader—do not write below)

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

Please cross out this problem if you do not wish it graded

## Problem 1A.

Score:

(a) Prove that if $s > 1$ then $\textstyle \sum _ { n > 0 } n ^ { - s } = \prod _ { p } 1 / ( 1 - p ^ { - s } )$ , where the product is over all primes p.

(b) Prove that the sum $\textstyle \sum _ { p } 1 / p$ over all primes p diverges.

Solution: Part (a) follows by expanding $1 / ( 1 - p ^ { - s } )$ as the geometric series $1 + p ^ { - s } + p ^ { - 2 s } \cdot \cdot \cdot$ 7 convergent for $s > 1$ , multiplying these series together, and using the fundamental theorem of arithmetic.

Part (b) follows because the left hand side of (a) tends to infinity as s tends to 1, so the product of $1 / ( 1 - p ^ { - 1 } )$ diverges, so the corresponding sum of $p ^ { - 1 }$ diverges.

## Problem 2A.

Score:

Let $x \colon [ a , b ] \to \mathbb { R }$ and $f \colon [ a , b ]  \mathbb { R }$ be non-negative continuous functions satisfying

$$
x ^ { 2 } ( t ) \leq 1 + \int _ { a } ^ { t } f ( s ) x ( s ) d s
$$

for $a \leq t \leq b .$ . Show that

$$
x ( t ) \leq 1 + { \frac { 1 } { 2 } } \int _ { a } ^ { t } f ( s ) d s
$$

for $a \leq t \leq b .$

Solution: Let

$$
y ( t ) = 1 + \int _ { a } ^ { t } f ( s ) x ( s ) d s
$$

so that

$$
x ( t ) \leq { \sqrt { y ( t ) } } .
$$

Then

$$
y ^ { \prime } ( t ) = f ( t ) x ( t ) \leq f ( t ) { \sqrt { y ( t ) } } ,
$$

that is,

$$
y ^ { \prime } / \sqrt { y } = ( 2 y ^ { 1 / 2 } ) ^ { \prime } \leq f .
$$

Integrating this gives

$$
x ( t ) \leq \sqrt { y ( t ) } \leq 1 + \frac { 1 } { 2 } \int _ { a } ^ { t } f ( s ) d s .
$$

Score:

Given $K \geq 0$ , let $\mathrm { L i p } _ { K }$ be the set of functions $f : \mathbb { R } \to \mathbb { R }$ which satisfy $| f ( x ) - f ( y ) | \leq$ $K | x - y |$ for all $x , y \in \mathbb { R }$

(a) Show that the formula

$$
d ( f _ { 1 } , f _ { 2 } ) = \sum _ { j = 1 } ^ { \infty } 2 ^ { - j } \operatorname* { s u p } _ { z \in [ - j , j ] } | f _ { 1 } ( z ) - f _ { 2 } ( z ) |
$$

converges and defines a metric d on $\mathrm { L i p } _ { K }$

(b) Show that $\mathrm { L i p } _ { K }$ is a complete metric space with this metric.

## Solution:

(a) The Lipschitz condition implies a bound $| f _ { 1 } ( x ) - f _ { 2 } ( x ) | \le C + 2 K j$ for all x in $[ - j , j ]$ , where $C = \vert f _ { 1 } ( 0 ) - f _ { 2 } ( 0 ) \vert$ Since the series ${ \textstyle \sum _ { j = 1 } ^ { \infty } 2 ^ { - j } ( C + 2 K j ) }$ is convergent, so is the right hand side in (a). The triangle inequality follows from triangle inequality for each term. We also have to check that $d ( f _ { 1 } , f _ { 2 } ) = 0$ implies $f _ { 1 } = f _ { 2 }$ . But every term in the sum is non-negative, so $d ( f _ { 1 } , f _ { 2 } ) = 0$ implies $\begin{array} { r } { \operatorname* { s u p } _ { z \in [ - j , j ] } | f _ { 1 } ( z ) - f _ { 2 } ( z ) | = 0 } \end{array}$ for all $j$ .

(b) Let $\{ f _ { i } \} _ { i = 1 } ^ { \infty }$ be a Cauchy sequence in $\mathrm { L i p } _ { K }$ . For any given $x \in \mathbb { R }$ , if we pick $j \geq | x |$ then $| f _ { i } ( x ) - f _ { j } ( x ) | \leq 2 ^ { j } d ( f _ { i } , f _ { j } )$ . Hence $\{ f _ { i } ( x ) \}$ is a Cauchy sequence, so the $f _ { i }$ converge pointwise. It is easy to see that the limit g belongs to $\operatorname { L i p } _ { K }$ •

It remains to show that $d ( f _ { i } , g )$ converges to zero.

The Lipschitz condition implies that the $f _ { i }$ converge uniformly to g on each $[ - j , j ]$ . To prove this, given $\epsilon > 0$ , we can choose points $x _ { 1 } , . . . , x _ { n } \in [ - j , j ]$ such that every $x \in [ - j , j ]$ has $| x - x _ { i } | < \epsilon / 4 K$ for some i, then choose k large enough so that $| f _ { l } ( x _ { i } ) - g ( x _ { i } ) | < \epsilon / 2$ for all i whenever $l > k$ . Then it follows that $| f _ { l } ( x ) - g ( x ) | < \epsilon$ for all $x \in [ - j , j ]$

Since $\{ f _ { i } ( 0 ) \}$ converges, it is bounded, hence there is a D such that $| f _ { i } ( 0 ) - g ( 0 ) | < D$ for all i. The Lipschitz condition then implies $| f _ { i } ( x ) - g ( x ) | < D + 2 K j$ for all $x \in [ - j , j ]$ and all i. Given $\epsilon > 0$ , we can choose J large enough so that $\textstyle \sum _ { j = J + 1 } ^ { \infty } ( D + 2 K j ) 2 ^ { - j } < \epsilon / 2$ , and therefore $\begin{array} { r } { d ( f _ { i } , g ) < \epsilon / 2 + \sum _ { j = 1 } ^ { J } 2 ^ { - j } \operatorname* { s u p } _ { z \in [ - j , j ] } | f _ { i } ( z ) - g ( z ) | } \end{array}$ for all i. By the uniform convergence on each $\left[ j , j \right]$ , the finite sum $\begin{array} { r } { \sum _ { j = 1 } ^ { J } 2 ^ { - j } \operatorname* { s u p } _ { z \in [ - j , j ] } | f _ { i } ( z ) - g ( z ) | } \end{array}$ is less than $\epsilon / 2$ and therefore $d ( f _ { i } , g ) < \epsilon _ { : }$ , for all sufficiently large i.

Please cross out this problem if you do not wish it graded

Problem 4A.

Score:

Find

$$
\int _ { - \infty } ^ { \infty } { \frac { \sin ^ { 3 } ( x ) } { x ^ { 3 } } } d x .
$$

Solution: Write

$$
\sin ^ { 3 } ( z ) = \left( { \frac { e ^ { i z } - e ^ { - i z } } { 2 i } } \right) ^ { 3 } = { \frac { e ^ { 3 i z } - 3 e ^ { i z } + 3 e ^ { - i z } - e ^ { - 3 i z } } { - 8 i } } = - { \frac { 1 } { 4 } } \operatorname { I m } ( e ^ { 3 i z } - 3 e ^ { i z } ) .
$$

Now use

$$
\int _ { C } { \frac { e ^ { 3 i z } - 3 e ^ { i z } } { z ^ { 3 } } } d z = 0 ,
$$

where the contour C consists of the intervals $[ - R , r ]$ and $[ r , R ]$ on the real axis, and semicircles in the upper half-plane of radii r and R. Letting $r \to 0$ and $R \to \infty$ , the contribution from the big semicircle vanishes. Since the leading term of $e ^ { 3 i z } - 3 e ^ { i z }$ is $- 9 z ^ { 2 } / 2 + 3 z ^ { 2 } / 2 = - 3 z ^ { 2 }$ the contribution from the small semicircle is the same as that of

$$
\int - { \frac { 3 } { z } } d z ,
$$

or 3πi.

The contribution along the x axis is therefore

$$
\int _ { - \infty } ^ { \infty } \frac { e ^ { 3 i z } - 3 e ^ { i z } } { z ^ { 3 } } d z = - 3 \pi i .
$$

It follows that the value of our original integral is $3 \pi / 4$

Please cross out this problem if you do not wish it graded

Score:

Is there a function $f ( z )$ analytic in C \ {0} such that $\begin{array} { r } { | f ( z ) | \geq \frac { 1 } { \sqrt { | z | } } } \end{array}$ for all $z \neq 0 ?$

Solution: Suppose f is such a function. Then $g ( z ) = 1 / f ( z )$ is analytic in $\mathbb { C } \setminus \{ 0 \}$ and $| g ( z ) | \le | z | ^ { 1 / 2 }$ for all $z \neq 0 .$ . In particular, $g ( z )$ is bounded in a punctured neighborhood of zero so by Riemann’s theorem on removable singularities it has a removable singularity there. Redefining $g ( 0 ) : = \mathrm { l i m } _ { z  0 } g ( z )$ we obtain an entire function. By Cauchy’s integral formula we have for any z:

$$
g ^ { \prime } ( z ) = \frac { 1 } { 2 \pi i } \oint _ { C _ { R } } \frac { g ( s ) } { ( s - z ) ^ { 2 } } d s ,
$$

where $C _ { R }$ is any circle centered at zero containing z and the integral is taken counterclockwise. Note that $| g ( s ) | \leq { \sqrt { R } }$ on $C _ { R }$ and that $| s - z | ^ { 2 } > ( R / 2 ) ^ { 2 }$ whenever $R > 2 | z |$ . Thus,

$$
| g ^ { \prime } ( z ) | < \frac { 2 \pi R } { 2 \pi } \cdot \frac { 4 \sqrt { R } } { R ^ { 2 } } = \frac { 4 } { \sqrt { R } }
$$

whenever $R > 2 | z |$ |. Letting $R \to \infty$ we find that $g ^ { \prime } ( z ) = 0$ for all $z \in \mathbb { C }$ , whence g must be constant. But $| \dot { g ( z ) } | \le \sqrt { | z | }$ in a neighborhood of zero, so this is only possible if $g ( z ) = 0$ , a contradiction. Thus, no such function f can exist.

Score:

Fix $N \geq 1$ . Let $s _ { 1 } , \ldots , s _ { N } , t _ { 1 } , \ldots , t _ { N }$ be 2N complex numbers of magnitude less than or equal to 1. Let A be the $N \times N$ matrix with entries

$$
A _ { i j } = \exp { ( t _ { i } s _ { j } ) } .
$$

Show that for every $m \geq 1$ there is an $N \times N$ matrix B with rank less than or equal to m such that

$$
\vert A _ { i j } - B _ { i j } \vert \le \frac { 2 } { m ! }
$$

for all i and $j .$

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

<table><tr><td>Problem 7A. Score:</td></tr></table>

Let A and B be two $n \times n$ matrices with coefficients in $\mathbb { Q } .$ For any field extension K of Q, we say that A and B are similar over K if $A = P B P ^ { - 1 }$ for some $n \times n$ invertible matrix P with coefficients in K. Prove that A and B are similar over $\mathbb { Q }$ if and only if they are similar over C.

## Solution:

The “only $\mathrm { i f } ^ { \dag }$ part is trivial. For the $ { \mathrm { \hat { \rho } } } _ { \mathrm { 1 f } }  { \mathrm { \Omega } } ^ { \le }$ part, assume that A and B are similar over $\mathbb { C } ,$ and we are going to prove that A and B are similar over Q. We first rewrite the problem as solutions of equations and inequalities.

Denote by $x _ { i j }$ the $( i , j ) \mathrm { - e n t r y }$ of P . Rewrite $A = P B P ^ { - 1 }$ as $A P = P B$ , and view it as a system of linear equations on the variables $\{ x _ { i j } \} _ { i , j }$ . The coefficients of the linear equations are in Q. The condition that P is invertible is equivalent to the inequality det $( P ) \neq 0$ , where det(P ) is viewed as a polynomial of the variables $\{ x _ { i j } \} _ { i , j }$ with coefficients in Q.

The condition that A and B are similar over C is equivalent to the statement that the system

$$
A P = P B , \quad \operatorname* { d e t } ( P ) \neq 0
$$

has a solution $( x _ { i j } ) \in \mathbb { C } ^ { n ^ { 2 } }$ . We need to prove that the system has a solution $( x _ { i j } ) \in \mathbb { Q } ^ { n ^ { 2 } }$

Denote by W (resp. V ) the set of solutions of $( x _ { i j } ) \in \mathbb { C } ^ { n ^ { 2 } } \ ( \mathrm { r e s p . . } \ ( x _ { i j } ) \in \ \bar { \mathbb { Q } } ^ { n ^ { 2 } } )$ for the equation $A P = P B$ Then W (resp. V ) is a vector subspace of $\mathbb { C } ^ { n ^ { 2 } }$ (resp. $\mathbb { Q } ^ { n ^ { 2 } } )$ over C (resp. Q), and we have a natural isomorphism $W = V \otimes _ { \mathbb { Q } } \mathbb { C }$ . We see that V is nonzero since W is nonzero. This shows that $A P = P B$ has nonzero rational solutions, and we are left to consider the condition det $( P ) \neq 0$

Take a basis of V over Q, and make an identification $V = \mathbb { Q } ^ { m }$ by this basis. This basis also gives an identification $W = \mathbb { C } ^ { m }$ The restriction of det(P ) to $V$ becomes a polynomial $f ( y _ { 1 } , \cdots , y _ { m } )$ of m variables with rational coefficients via the identification. By the condition, f is not identically zero over $\mathbb { C } ^ { m }$ , so it is not the zero polynomial. Hence, we can find an element of $\mathbb { Q } ^ { m }$ at which $f$ is nonzero. This element gives the desired solution $( x _ { i j } ) \in \mathbb { Q } ^ { n ^ { 2 } }$ of the system.

<table><tr><td>Problem 8A. Score:</td></tr></table>

Let $M _ { 2 } ( \mathbb { Q } )$ be the ring of all $2 \times 2$ matrices with coefficients in Q. Describe all field extensions K of $\mathbb { Q }$ such that there is an injective ring homomorphism $K \to M _ { 2 } ( \mathbb { Q } )$ . (Note: we take the convention that a ring homomorphism maps the multiplicative identity to the multiplicative identity.)

## Solution:

Our conclusion is that K is either $\mathbb { Q }$ or a quadratic extension of $\mathbb { Q } .$

For the necessity, let K be an extension of $\mathbb { Q }$ with an injective ring homomorphism $i : K \to M _ { 2 } ( \mathbb { Q } )$ . The homomorphism is Q-linear, so we have

$$
\begin{array} { r } { [ K : \mathbb { Q } ] \leq \dim _ { \mathbb { Q } } M _ { 2 } ( \mathbb { Q } ) = 4 . } \end{array}
$$

In particular, K is a finite extension of Q. Assume $K = \mathbb { Q } ( \alpha )$ , so that $\alpha$ is a generator of $K$ over $\mathbb { Q } .$ . By the Cayley–Hamilton theorem, $i ( \alpha )$ is annihilated by its characteristic polynomial, which has degree 2 and rational coefficients. Thus α is annihilated by a polynomial of degree 2 with rational coefficients. This proves that $[ K : \mathbb { Q } ] \leq 2$

For the sufficiency, assume that K is an extension of Q with $[ K : \mathbb { Q } ] \leq 2$ , and we need to construct an injective ring homomorphism $i : K \to M _ { 2 } ( \mathbb { Q } )$ . If $K = \mathbb { Q }$ , take the usual embedding sending rational numbers to the corresponding scalar matrices. If K is a quadratic extension of $\mathbb { Q } .$ write $V = K$ , viewed as a 2-dimensional vector space over $\mathbb { Q }$ . Let K act on V by multiplication. The action is Q-linear, and thus induces a homomorphism $K \to \operatorname { E n d } _ { \mathbb { Q } } ( V ) \simeq M _ { 2 } ( \mathbb { Q } )$ . This map is the desired injective homomorphism. Alternatively, write $K = \mathbb { Q } ( { \sqrt { d } } )$ , and define an injection $K \to M _ { 2 } ( \mathbb { Q } )$ by the explicit formula

$$
a + b { \sqrt { d } } \longmapsto \left( { a \atop b d } \right) .
$$

Please cross out this problem if you do not wish it graded

<table><tr><td>Problem 9A. Score:</td></tr></table>

Let p be a prime number, $\mathbb { F } _ { p }$ be the finite field of $p$ elements, and $\mathrm { G L } _ { n } ( \mathbb { F } _ { p } )$ be the finite group of all invertible $n \times n$ matrices with coefficients in $\mathbb { F } _ { p } .$ . Find the order of ${ \mathrm { G L } } _ { n } ( \mathbb { F } _ { p } )$ .

## Solution:

Let A be an element of $\mathrm { G L } _ { n } ( \mathbb { F } _ { p } )$ , and denote the columns of A by $A _ { 1 } , \cdots , A _ { n }$ . Note that $A _ { 1 }$ can be any element of $\mathbb { F } _ { p } ^ { n } \setminus \{ 0 \}$ , which has $p ^ { n } - 1$ choices. Then $A _ { 2 }$ can be any element of $\mathbb { F } _ { p } ^ { n } \setminus$ span $\{ A _ { 1 } \}$ , which has $p ^ { n } - p$ choices. In general, for $i = 1 , \cdots , n , A _ { i }$ can be any element of $\mathbb { F } _ { p } ^ { n } \setminus \operatorname { s p a n } \{ A _ { 1 } , \cdot \cdot \cdot , A _ { i - 1 } \}$ , which has $p ^ { n } - p ^ { i - 1 }$ choices. Hence, the total number of choices are

$$
( p ^ { n } - 1 ) ( p ^ { n } - p ) \cdot \cdot \cdot ( p ^ { n } - p ^ { n - 1 } ) .
$$

This number is the order of ${ \mathrm { G L } } _ { n } ( \mathbb { F } _ { p } )$

# Department of Mathematics, University of California, Berkeley

Fall Semester 2016

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q$

4. No notes, books, calculators or electronic devices may be used during the exam.

## PROBLEM SELECTION

Part B: List the six problems you have chosen:

## Problem 1B.

Score:

Let $\begin{array} { r } { C = \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x } \end{array}$ and let $S _ { n }$ be the (n − 1)-dimensional “surface area” of the unit sphere in $R ^ { n } \ ( \mathrm { s o } \ S _ { 2 } = 2 \pi , \ : S _ { 3 } = 4 \pi / 3 )$

(a) Prove that $C ^ { n } = S _ { n } \Gamma ( n / 2 ) / 2$ , where $\textstyle \Gamma ( s ) = \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { s - 1 } d t$ . (Evaluate the integral of $e ^ { - ( x _ { 1 } ^ { 2 } + \cdots + x _ { n } ^ { 2 } ) }$ over $R ^ { n }$ in rectangular and polar coordinates.)

(b) Show that $s \Gamma ( s ) = \Gamma ( s + 1 ) , \Gamma ( 1 ) = 1$

(c) Evaluate C. (Hint: $S _ { 2 } = 2 \pi . $

(d) Evaluate $S _ { 4 }$

## Solution:

(a) The integral in rectangular coordinates is $C ^ { n }$ , and the integral in polar coordinates is $\begin{array} { r } { \dot { S _ { n } } \int _ { 0 } ^ { \infty } e ^ { - r ^ { 2 } } r ^ { n - 1 } d r } \end{array}$ . Substitute $t = r ^ { 2 }$ •

(b) Integrate by parts.

(c) Put n = 2 in part (a) to get $C ^ { 2 } = S _ { 2 } \Gamma ( 1 ) / 2 = \pi , \mathrm { s o } C = \sqrt { \pi } .$

(d) By (a) $S _ { 4 }$ is $2 C ^ { 4 } / \Gamma ( 2 ) = 2 \pi ^ { 2 }$

<table><tr><td></td></tr><tr><td>Problem 2B. Score:</td></tr></table>

Let K be a compact subset of $\mathbb { R } ^ { n }$ and $\boldsymbol { f } ( \boldsymbol { x } ) = \boldsymbol { d } ( \boldsymbol { x } , K )$ be the Euclidean distance from x to the nearest point of K.

(a) Show that f is continuous and $f ( x ) = 0 { \mathrm { ~ i f ~ } } x \in K$

(b) Let $g ( x ) = \operatorname* { m a x } ( 1 - f ( x ) , 0 )$ . Show that $\textstyle \int g ^ { n }$ converges to the n-dimensional volume of K as $n \to \infty$

(The n-dimensional volume of K is defined to be $\textstyle \int 1 _ { K }$ , if the integral exists, where $1 _ { K } ( x ) = 1$ for $x \in K$ , and $1 _ { K } ( x ) = 0$ for $x \notin K . )$

## Solution:

(a) Note that for any x, there is a nearest point of K to $x ,$ that is, $d ( x , y )$ assumes a minimum for $y \in K$ , since K is compact.

Obviously $f ( x ) = 0 { \mathrm { ~ i f ~ } } x \in K$ . For any two points $x , y \in \mathbb { R } ^ { n }$ , the triangle inequality implies that $d ( x , K ) \leq d ( y , K ) + d ( x , y )$ and $d ( y , K ) \leq d ( x , K ) + d ( x , y )$ . This shows that $| f ( x ) - f ( y ) | \leq d ( x , y )$ , hence f is continuous.

(b) Since K is compact, it is bounded. Hence the set of points x such that $d ( x , K ) \leq 1$ is also bounded, and g vanishes outside this set. This implies that $\int g ^ { n }$ exists for all $n .$ . Clearly $g ^ { n }$ converges monotonically to $1 _ { K }$ . Hence $\textstyle \int 1 _ { K }$ exists and is equal to $\scriptstyle \operatorname* { l i m } _ { n \to \infty } \int g ^ { n }$

Score:

(a) Suppose that I is a closed interval and f is a smooth function from I to I such that $\left| f ^ { \prime } \right|$ is bounded by some number $r < 1 \AA$ on I. Let $a _ { 0 }$ be in I and put $a _ { n + 1 } = f ( a _ { n } )$ . Prove that the sequence $a _ { n }$ tends to the unique root of $f ( x ) = x$ in I .

(b) Show that if $a _ { 0 }$ is real and $a _ { n + 1 } = \cos ( a _ { n } )$ then $a _ { n }$ tends to a root of $\cos ( x ) = x $

## Solution:

(a) Say $I = [ a , b ]$ . Since f maps I into $I , f ( a ) - a \geq 0$ and $f ( b ) - b \leq 0$ . Since f is continuous, $f ( x ) - x = 0$ has at least one root. If $f ( x ) = x$ had more than one root, it would imply $f ^ { \prime } ( c ) = 1$ for some $c \in I$ by the Mean Value Theorem. Hence the root is unique.

Changing variables we may assume that $f ( 0 ) = 0$ . Then $| f ( x ) | \leq r | x |$ for all x in I, so $| a _ { n + 1 } | \leq r | a _ { n } |$ . As $r < 1$ , this proves that the sequence $a _ { n }$ tends to 0.

(b) Note that $a _ { 1 } \in [ - 1 , 1 ]$ , hence $a _ { 2 } \in [ \cos ( 1 ) , 1 ]$ and $a _ { 3 } \in [ \cos ( 1 ) , \cos ( \cos ( 1 ) ) ]$ . Taking I to be this last interval, cos x maps I into itself, and since $0 < \cos ( 1 ) < \cos ( \cos ( 1 ) ) < 1 < \pi / 2 .$ the derivative cos0 x = − sin x has absolute value less than some $r < 1$ on I. Now apply part (a).

Please cross out this problem if you do not wish it graded

<table><tr><td></td></tr><tr><td>Problem 4B. Score:</td></tr></table>

Put $f ( z ) = z ( e ^ { z } - 1 )$ . Prove there exists an analytic function h(z) defined near $z = 0$ such that $f ( z ) = h ( z ) ^ { 2 }$ . Find the first 3 terms in the power series expansion $h ( z ) = \sum a _ { n } z ^ { n }$ Does h(z) extend to an entire function on C?

## Solution:

The function f vanishes to order 2 at 0, so there is a holomorphic function g defined on all of C such that $f ( z ) = z ^ { 2 } g ( z )$ , and $g ( 0 ) \neq 0$ . Since g is continuous, it is nonzero on some neighborhood U of the origin. Shrinking U, we may choose a branch of $\log ( g ( z ) )$ . Define h on U by

$$
h ( z ) = z e ^ { \frac { 1 } { 2 } \log ( g ( z ) ) } ;
$$

then $f ( z ) = h ( z ) ^ { 2 }$

Choosing the sign of ±h to have positive leading coefficient, the power series expansion of h is

$$
h ( z ) = z + \frac { 1 } { 4 } z ^ { 2 } + \frac { 5 } { 9 6 } z ^ { 3 } + . . .
$$

The function h does not extend to an entire function on C because such an extension would be a global square root of $f ,$ which cannot exist because f has a simple zero at 2πi.

## Problem 5B.

Score:

Let $f _ { t } ( z )$ be a family of entire functions depending analytically on $t \in \Delta$ , where $\Delta$ is the open unit disk in C. Suppose that for all $t , f _ { t } ( z )$ is non-vanishing on the unit circle $S ^ { 1 }$ in $\mathbb { C } .$ Prove that for each $k \geq 0$ ,

$$
N _ { k } ( t ) = \sum _ { | z | < 1 : f _ { t } ( z ) = 0 } z ^ { k }
$$

is an analytic function of t (the zeroes of $f _ { t } ( z )$ are taken with multiplicity in the sum).

## Solution:

By the residue theorem, for each $t \in \Delta$ we have

$$
N _ { k } ( t ) = { \frac { 1 } { 2 \pi i } } \int _ { S ^ { 1 } } { \frac { f _ { t } ^ { \prime } ( z ) z ^ { k } } { f _ { t } ( z ) } } d z .
$$

This integral representation makes it clear that $N _ { k } ( t )$ is analytic in t (for example, by Morera’s theorem).

<table><tr><td>Problem 6B. Score:</td></tr></table>

Let A be an $m \times n$ matrix of rank r and B a $p \times q$ matrix of rank s. Find the dimension of the vector space of $n \times p$ matrices X such that $A X B = 0$ •

## Solution:

Let $W \subseteq \mathbb { R } ^ { n }$ be the nullspace of A and $V \subseteq \mathbb { R } ^ { p }$ the column space of B. The problem then asks for the dimension of the space of linear transformations $T \colon \mathbb { R } ^ { p }  \mathbb { R } ^ { n }$ such that $T ( V ) \subseteq W$ . Changing bases in Rn and Rp, we see that the answer depends only on the dimensions dim $( V ) = s$ and dim $( W ) = n - r$ . In particular, we are free to assume that V is the span of the first s unit vectors, and W is the space of vectors whose first r coordinates are zero.

In that case, X is any $n \times p$ matrices whose upper-left $r \times s$ block is zero. These form a space of dimension $n p - r s$

Problem 7B.

Score:

Find an example of a vector space V over the real numbers R and two linear maps $f , g : V \to V$ such that $f$ is injective but not surjective and g is surjective but not injective and such that $f + g$ is equal to the identity map $1 _ { V }$

Hint: construct V as a subspace of the space of sequences of real numbers, closed under the linear maps

$$
f ( a _ { 1 } , a _ { 2 } , a _ { 3 } , . . . ) = ( a _ { 1 } - a _ { 2 } , a _ { 2 } - a _ { 3 } , . . . )
$$

and

$$
g ( a _ { 1 } , a _ { 2 } , a _ { 3 } , . . . ) = ( a _ { 2 } , a _ { 3 } , . . . ) .
$$

## Solution:

Following the hint, the space V of sequences which converge to zero works.

Obviously, $f + g = 1 _ { V }$ . It is also clear that the map g is surjective but not injective. To see that f is injective, note that the kernel of f is the set of constant sequences $( a , a , a , \ldots )$ which converge to zero (by the definition of V ), forcing $a = 0$ . To see that $f$ is not surjective, we argue, for example, that there is no sequence $( a _ { 1 } , a _ { 2 } , a _ { 3 } , . . . ) \in V$ such that

$$
{ ( a _ { 1 } - a _ { 2 } , a _ { 2 } - a _ { 3 } , a _ { 1 } - a _ { 4 } , . . . ) = \Big ( - \frac { 1 } { 1 } , - \frac { 1 } { 2 } , - \frac { 1 } { 3 } , . . . \Big ) } .
$$

Otherwise, we would have

$$
a _ { k + 1 } = a _ { k } + { \frac { 1 } { k } } ,
$$

which would imply by induction

$$
a _ { k } = a _ { 1 } + { \frac { 1 } { 1 } } + \ldots + { \frac { 1 } { k - 1 } } .
$$

This gives us a contradiction, since the left-hand side converges to zero by definition and the right-hand side diverges. Of course, the same argument works with any divergent series whose terms converge to zero in place of the harmonic series.

<table><tr><td>Problem 8B. Score:</td></tr></table>

Let G be a group and n be a positive integer. Assume that there exists a surjective group homomorphism $\mathbb { Z } ^ { n } \to G$ and an injective group homomorphism $\mathbb { Z } ^ { n } \to G$ . Prove that the group G is isomorphic to $\mathbb { Z } ^ { n }$

## Solution:

By the surjection $\mathbb { Z } ^ { n } \to G , G$ is an abelian group generated by n elements. In particular, G is a finitely generated abelian group. By the structure theorem, G is isomorphic to $\mathbb { Z } ^ { r } \times G _ { 0 }$ where $r \geq 0$ and $G _ { 0 }$ is a finite abelian group. By the injection $\mathbb { Z } ^ { n } \to G ,$ , we have $r \geq n$ Use the property that G is generated by n elements again, we have $r = n$ and $G _ { 0 } = 0$ . This proves that G is isomorphic to $\mathbb { Z } ^ { n }$

<table><tr><td>Problem 9B. Score:</td></tr></table>

Find (with proof) the number of groups of order 12 up to isomorphism. You may assume the Sylow theorems (if a prime power pn is the largest power of p dividing the order of a group, then the group has subgroups of order pn and the number of them is 1 mod p.)

Solution: By Sylow’s theorems, there are either 1 or 4 subgroups of order 3.

If there is 1 subgroup of order 3 it is normal, so the group is a semidirect product of this subgroup with a Sylow subgroup of order 4. This gives 4 possibilities, as the subgroup of order 4 can be cyclic or the Klein 4-group, and each of these can act either trivially or non-trivially on the group of order 3.

If there are 4 subgroups of order 3, there are 4 elements not of order 3, which must therefore form the normal Sylow 2-subgroup. The group is a semidirect product of this Sylow 2-subgroup by a group of order 3 acting nontrivially, and the only possibility is the semidirect product of a cyclic group of order 3 acting nontrivially on the Klein 4-group.

So there are 5 groups of order 12.