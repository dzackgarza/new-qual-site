# Department of Mathematics, University of California, Berkeley

Spring Semester 2017

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

Score:

Show that the following improper Riemann integrals exist and are equal:

$$
\int _ { - \infty } ^ { \infty } { \frac { \sin ( x ) } { x } } d x = \int _ { - \infty } ^ { \infty } { \frac { \sin ^ { 2 } ( x ) } { x ^ { 2 } } } d x
$$

Solution: Method 1:

$$
\int _ { - 2 L } ^ { 2 R } { \frac { \sin ( x ) } { x } } d x = \int _ { - L } ^ { R } { \frac { \sin ( 2 x ) } { x } } d x = \int _ { - L } ^ { R } { \frac { 2 \sin ( x ) \cos ( x ) } { x } } d x = \int _ { - L } ^ { R } { \frac { d } { d x } } ( \sin ^ { 2 } ( x ) ) { \frac { d x } { x } } .
$$

Integrate by parts:

$$
= \frac { \sin ^ { 2 } ( x ) } { x } \left| _ { - L } ^ { R } + \int _ { - L } ^ { R } \frac { \sin ^ { 2 } ( x ) } { x ^ { 2 } } d x .\right.
$$

As $L \to \infty$ , si $\mathrm { 1 } ^ { 2 } ( x ) / x  0$ and the tail

$$
\int _ { - \infty } ^ { - L } \frac { \sin ^ { 2 } ( x ) } { x ^ { 2 } } d x  0 .
$$

Hence the improper integrals exist and are equal.

Please cross out this problem if you do not wish it graded

## Problem 2A.

Score:

Suppose f is a function from the reals to the reals satisfying $2 f ( x ) = f ( 2 x )$ for all x.

(a) Prove that if f is differentiable at 0 then f is linear.

(b) Give an example of such a function f that is continuous but not linear.

Solution: (a) We have $f ( 0 ) = 0$ Suppose $f ( x ) = y$ for some $x \neq 0$ Then $f ( x / 2 ^ { n } ) = y / 2 ^ { n }$ so there are points arbitrarily close to 0 such that the graph of f intersects the line through 0 of slope $y / x$ . So if f is differentiable at 0 with derivative c then $f ( x ) / x = y / x = c .$ . Since this holds for any x, f must be the function $y = c x$

(b) The function $f ( x ) = x g ( \log _ { 2 } ( x ) )$ for $x \neq 0 , f ( 0 ) = 0$ , where g is a continuous bounded function of period 1 such as $g ( x ) = \sin ( 2 \pi x )$

## Problem 3A.

Score:

Suppose we have a continuous positive function $f : ( 0 , \pi ) \to ( 0 , \infty )$ such that for all $x , y \in$ $( 0 , \pi )$ we have

$$
\int _ { x } ^ { y } { \frac { f ( x ) f ( y ) } { f ^ { 2 } ( t ) } } d t = \sin ( y - x ) .
$$

(a) Show that $\sin ( z - x ) f ( y ) = \sin ( y - x ) f ( z ) + \sin ( z - y ) f ( x )$

(b) Find all possibilities for f .

Solution: For any $x , y , z \in ( 0 , \pi )$ we have

$$
{ \frac { \sin ( z - x ) } { f ( x ) f ( z ) } } = \int _ { x } ^ { z } { \frac { d t } { f ^ { 2 } ( t ) } } = \int _ { x } ^ { y } { \frac { d t } { f ^ { 2 } ( t ) } } + \int _ { y } ^ { z } { \frac { d t } { f ^ { 2 } ( t ) } } = { \frac { \sin ( y - x ) } { f ( x ) f ( y ) } } + { \frac { \sin ( z - y ) } { f ( y ) f ( z ) } } .
$$

Multiplying both sides by $f ( x ) f ( y ) f ( z )$ yields

$$
\sin ( z - x ) f ( y ) = \sin ( y - x ) f ( z ) + \sin ( z - y ) f ( x ) .
$$

Note that $| z - x | < \pi$ and therefore sin $( z - x ) \neq 0$ unless $z = x$ . So, fixing $x \neq z$ and letting y vary yields that f must be of the following form:

$$
f ( y ) = a \sin ( y + \theta ) .
$$

for some $a > 0$ and $\theta \in [ 0 , 2 \pi )$ . Since f was required to be positive on $( 0 , \pi )$ , we find that $\theta = 0$ . So

$$
f ( y ) = a \sin ( y ) .
$$

We now claim that any function of this form solves the integral equation from the problem. To see this we compute

$$
\int _ { x } ^ { y } { \frac { d t } { \sin ^ { 2 } ( t ) } } = - { \frac { \cos t } { \sin t } } { \bigg | } _ { x } ^ { y } = { \frac { \cos x } { \sin x } } - { \frac { \cos y } { \sin y } } = { \frac { \cos x \sin y - \cos y \sin x } { \sin x \sin y } } = { \frac { \sin ( y - x ) } { \sin x \sin y } } .
$$

So if $f ( y ) = a \sin ( y )$ , then

$$
\int _ { x } ^ { y } { \frac { f ( x ) f ( y ) } { f ^ { 2 } ( t ) } } d t = \sin x \sin y \int _ { x } ^ { y } { \frac { d t } { \sin ^ { 2 } ( t ) } } = \sin ( y - x ) .
$$

Score:

The Weierstrass zeta function $\zeta$ is a meromorphic function satisfying

$\zeta ( z + \omega _ { 1 } ) = \zeta ( z ) + \eta _ { 1 }$

$\zeta ( z + \omega _ { 2 } ) = \zeta ( z ) + \eta _ { 2 }$

• The singularities of $\zeta$ are poles of residue 1 at the points $m \omega _ { 1 } + n \omega _ { 2 }$ for $m , n \in \mathbb { Z }$

Here $\omega _ { 1 } , \omega _ { 2 } , \eta _ { 1 } , \eta _ { 2 }$ are complex constants with $\omega _ { 2 } / \omega _ { 1 }$ not real. Use Cauchy’s residue theorem to prove Legendre’s relation $\omega _ { 2 } \eta _ { 1 } - \omega _ { 1 } \eta _ { 2 } = \pm 2 \pi i$ and express the sign in terms of $\omega _ { 1 }$ and $\omega _ { 2 }$

Solution: Integrate $\zeta$ around a parallelogram containing 0 with sides parallel to the lines from $0$ to $\omega _ { 1 }$ and $\omega _ { 2 }$ . By the residue theorem the integral is $2 \pi i$ times the sum of the residues, which is $2 \pi i .$ . Suppose $\Im ( \omega _ { 2 } / \omega _ { 1 } ) > 0$ . The sum of the integrals along two of the sides is $- \omega _ { 1 } \eta _ { 2 }$ (using the fact that $\zeta ( z + \omega _ { 2 } ) = \zeta ( z ) + \eta _ { 2 } )$ and similarly the sum of the integrals over the other two sides is $\omega _ { 2 } \eta _ { 1 }$ . Switching $\omega _ { 1 }$ and $\omega _ { 2 }$ changes a lot of signs, so we find $\omega _ { 2 } \eta _ { 1 } - \omega _ { 1 } \eta _ { 2 } = \pm 2 \pi i$ where the sign is the sign of $\Im ( \omega _ { 2 } / \omega _ { 1 } )$

Score:

Suppose the coefficients of the power series

$$
\sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }
$$

are given by the recurrence relation

$$
a _ { 0 } = 1 , a _ { 1 } = - 1 , 3 a _ { n } + 4 a _ { n - 1 } - a _ { n - 2 } = 0 , n = 2 , 3 , \ldots .
$$

Find the radius of convergence of the series and the function to which it converges in its disc of convergence.

Solution: We can solve for $f ( z )$ using the recurrence:

$$
\begin{array}{c} 8 f ( z ) + 4 z f ( z ) - z ^ { 2 } f ( z ) = 3 \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } + 4 \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n + 1 } - \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n + 2 }  \\ { = 3 a _ { 0 } + 3 a _ { 1 } z + 3 \sum _ { n = 2 } ^ { \infty } a _ { n } z ^ { n } + 4 a _ { 0 } z + 4 \sum _ { n = 2 } ^ { \infty } a _ { n - 1 } z ^ { n } - \sum _ { n = 2 } ^ { \infty } a _ { n - 2 } z ^ { n } } \\ { = 3 a _ { 0 } + 3 a _ { 1 } z + 4 a _ { 0 } z + \sum _ { n = 2 } ^ { \infty } ( 3 a _ { n } + 4 a _ { n - 1 } - a _ { n - 2 } ) z ^ { n } } \\ { = 3 + z ~ . } \end{array}
$$

Therefore

$$
f ( z ) = { \frac { 3 + z } { 3 + 4 z - z ^ { 2 } } } \ .
$$

This has poles where $z ^ { 2 } - 4 z - 3 = 0 ; { \mathrm { i . e . , ~ } } z = 2 \pm { \sqrt { 7 } } .$ The smallest absolute value of such a pole is ${ \sqrt { 7 } } - 2$ , so that is the radius of convergence of the series. (The series has positive radius of convergence because the coefficients, being solutions of a recurrence, grow at most exponentially. Therefore it is the Taylor series for the function at $z = 0$ , and converges in the largest disc centered at $z = 0$ over which the function is holomorphic.)

Score:

Let A be an $n \times n$ matrix over the complex numbers. Let $e ^ { A } = 1 + A + A ^ { 2 } / 2 + \cdot \cdot \cdot + A ^ { m } / m ! + \cdot \cdot \cdot$ Show this series converges and det $( e ^ { A } ) = e ^ { T r ( A ) }$

Solution: Let M denote the max of the absolute values of the entries of A. Then one shows by induction that the max of the absolute values of the entries of $A ^ { m }$ is at most $n ^ { m - 1 } M ^ { m }$ Hence, the entries of $e ^ { A }$ are series of the form $\textstyle \sum _ { n \geq 0 } a _ { n } / n !$ such that $| a _ { n } | \leq ( n M ) ^ { m }$ and so converge by the comparison test with $e ^ { n M }$

Now suppose B is an invertible matrix such that $B A B ^ { - 1 } = C$ is upper triangular. Then $B e ^ { A } B ^ { - 1 } = 1 + B A B ^ { - 1 } + B A ^ { 2 } B ^ { - 1 } / 2 + \cdots + B A ^ { m } B ^ { - 1 } / m ! + \cdots = e ^ { C }$ But $e ^ { C }$ is upper triangular and the diagonal entries are $e ^ { c _ { i } }$ where $c _ { 1 } , \ldots , c _ { n }$ are the diagonal entries of C. Hence det $( e ^ { A } ) = \mathrm { d e t } ( \check { e ^ { C } } ) = e ^ { \sum c _ { i } } = e ^ { T r ( C ) } = e ^ { T r ( A ) }$

Please cross out this problem if you do not wish it graded

## Problem 7A.

Score:

Given two vectors x and $y$ in $\mathbb { R } ^ { n }$ with $\| x \| _ { 2 } = \| y \| _ { 2 }$ , construct an orthogonal matrix $Q$ such that $Q x = y$ . Can there be such a matrix if $\| x \| _ { 2 } \neq \| y \| _ { 2 } ?$

Solution: Reflect across a plane $P$ perpendicular to $x - y$ . Let $u = ( x - y ) / \| x - y \| _ { 2 }$ . Then $u u ^ { T }$ implements projection onto $P ,$ so

$$
Q = I - 2 u u ^ { T }
$$

takes x into $y \colon$

$$
Q x = x - 2 u u ^ { T } x = ( \| x \| _ { 2 } ^ { 2 } - x ^ { T } y ) x - ( \| x \| ^ { 2 } - y ^ { T } x ) ( x - y ) = y .
$$

Moreover,

$$
Q ^ { T } Q = Q ^ { 2 } = ( I - 2 u u ^ { T } ) ^ { 2 } = I - 4 u u ^ { T } u u ^ { T } + 4 u u ^ { T } = I
$$

so $Q$ is orthogonal.

$\operatorname { I f } \| x \| _ { 2 } \neq \| y \| _ { 2 }$ there can be no $Q ,$ since orthogonal matrices define isometries.

Score:

Show that for each integer $p \geq 0$ the sum

$$
S _ { p } ( n ) = \sum _ { k = 0 } ^ { n } k ^ { p }
$$

is a polynomial of degree $p + 1$ in the variable n.

Solution: Define the backward difference operator $\Delta$ so that

$$
\Delta S _ { p } ( n ) = S _ { p } ( n ) - S _ { p - 1 } ( n ) = n ^ { p } - ( n - 1 ) ^ { p } = \sum _ { k = 0 } ^ { p - 1 } { \binom { n } { k } } n ^ { k } ( - 1 ) ^ { n - k + 1 }
$$

is a polynomial of degree $p - 1$ . Similarly $\Delta ^ { k } S _ { p } ( n )$ is a polynomial of degree $p + 1 - k$ and $\Delta ^ { p + 2 } S _ { p } ( n ) = 0$ This linear homogeneous difference equation of order $p + 2$ has $p + 2$ linearly independent solutions. Among them are all polynomials in n of degree $p + 1$ . Since these polynomials form a subspace of dimension $p + 2$ , they form the full solution space of the difference equation. Hence the solution $S _ { p } ( n )$ determined by $p + 2$ known initial values is a polynomial in n of degree $p + 1$

Please cross out this problem if you do not wish it graded

## Problem 9A.

Score:

The Bell number $P _ { n }$ is the number of partitions of a set of n elements into disjoint nonempty subsets, so for example $\{ 1 , 2 , 3 \} = \{ 1 \} \cup \{ 2 \} \cup \{ 3 \} = \{ 1 , 2 \} \cup \{ 3 \} = \{ 2 , 3 \} \cup \{ 1 \} = \{ 1 , 3 \} \cup \{ 2 \}$ and $P _ { 3 } = 5$ . Show that

$$
{ \frac { P _ { n } } { n ! } }  0
$$

as $n \to \infty$

Solution: For each partition let k be the cardinality of the subset $S$ containing 1. There are $\binom { n - 1 } { k - 1 }$ ways to choose the other k − 1 elements in $S ,$ and $P _ { n - k }$ ways to partition the other $n - k .$ , so

$$
P _ { n } = \sum _ { k = 1 } ^ { n } { \binom { n - 1 } { k - 1 } } P _ { n - k }
$$

where $P _ { 0 } = 1 . { \mathrm { ~ E . g . ~ } } P _ { 1 } = 1 , P _ { 2 } = 2 , P _ { 3 } = 5$ , and so forth. Shifting gives

$$
Q _ { n + 1 } = { \frac { P _ { n + 1 } } { ( n + 1 ) ! } } = { \frac { 1 } { n + 1 } } \sum _ { k = 0 } ^ { n } { \frac { 1 } { k ! } } Q _ { n - k } .
$$

Hence

$$
Q _ { n + 1 } \leq \frac { 1 } { n + 1 } \sum _ { k = 0 } ^ { n } \frac { 1 } { k ! } \operatorname* { m a x } _ { 0 \leq k \leq n } Q _ { k } \leq \frac { e } { n + 1 } \operatorname* { m a x } _ { 0 \leq k \leq n } Q _ { k } .
$$

For $n \geq 2 , e < n + 1$ so (a) the maximum of the $\mathrm { \mathit { Q } ^ { \prime } { s } }$ cannot increase and (b) $Q _ { n } \to 0$ a s $n \to \infty$

1. Please write your 1- or 2-digit exam number on this cover sheet and on all problem sheets (even problems that you do not wish to be graded).

2. Indicate below which six problems you wish to have graded. Cross out solutions you may have begun for the problems that you have not selected.

3. Extra sheets should be stapled to the appropriate problem at the upper right corner. Do not put work for problem p on either side of the page for problem q if $p \neq q$

4. No notes, books, calculators or electronic devices may be used during the exam.

## PROBLEM SELECTION

Part B: List the six problems you have chosen:

Score:

Find all differentiable functions $f : \mathbb { R } \to \mathbb { R }$ with the property that

$$
f ^ { \prime } ( x ) = { \frac { f ( x + h ) - f ( x - h ) } { 2 h } }
$$

for all $x \in \mathbb { R }$ and all $h \neq 0$ . (Hint: multiply both sides by 2h.)

Solution: Note first that for fixed $h \neq 0$ the right-hand side of the equation is differentiable in x. So $f ( x )$ is twice differentiable. Iterating this argument yields that $f ( x )$ is even smooth.

Now if we multiply both sides of the equation by 2h, then we get

$$
2 h \cdot f ^ { \prime } ( x ) = f ( x + h ) - f ( x - h ) .
$$

If we differentiate this equation by h (for some fixed x), we obtain

$$
2 f ^ { \prime } ( x ) = f ^ { \prime } ( x + h ) + f ^ { \prime } ( x - h ) .
$$

Differentiating this equation once more by h gives

$$
0 = f ^ { \prime \prime } ( x + h ) - f ^ { \prime \prime } ( x - h ) .
$$

Since this equation holds for all $x \in \mathbb { R }$ and $h \neq 0$ , we can conclude that $f ^ { \prime \prime } ( x )$ is constant. Therefore, f (x) must be of the form

$$
f ( x ) = a x ^ { 2 } + b x + c
$$

for some fixed $a , b , c \in \mathbb { R }$

We claim that, conversely, any function of this form satisfies the desired equation. To see this, observe that

$$
{ \begin{array} { r l } & { { \frac { f ( x + h ) - f ( x - h ) } { 2 h } } = { \frac { a ( x + h ) ^ { 2 } + b ( x + h ) + c - a ( x - h ) ^ { 2 } - b ( x - h ) - c } { 2 h } } } \\ & { \qquad = { \frac { 4 a x h + 2 b h } { 2 h } } = 2 a x + b = f ^ { \prime } ( x ) . } \end{array} }
$$

Please cross out this problem if you do not wish it graded

## Problem 2B.

Score:

Suppose $f : [ - 1 , 1 ] \to \mathbb { C }$ is a continuous complex-valued function, and for all non-negative integers n

$$
\int _ { - 1 } ^ { 1 } x ^ { n } f ( x ) d x = 0 .
$$

Prove that $f = 0 .$

Solution: Method 1: By taking linear combinations,

$$
\int _ { - 1 } ^ { 1 } f ( x ) P ( x ) d x = 0
$$

whenever $P$ is a polynomial. Given $\epsilon > 0$ , the Weierstrass Approximation Theorem provides a polynomial P with

$$
| f ( x ) - P ( x ) | \leq \epsilon
$$

for $- 1 \leq x \leq 1$ . Then

$$
\int _ { - 1 } ^ { 1 } f ( x ) ^ { 2 } d x = \int _ { - 1 } ^ { 1 } f ( x ) ( f ( x ) - P ( x ) + P ( x ) ) d x \leq \epsilon \int _ { - 1 } ^ { 1 } | f ( x ) | d x .
$$

Since $\epsilon > 0$ was arbitrary,

$$
\int _ { - 1 } ^ { 1 } f ( x ) ^ { 2 } d x = 0 .
$$

Since f is continuous, $f = 0$

Method 2: By Taylor expansion, all the Fourier coefficients

$$
\hat { f } ( k ) = \int _ { - 1 } ^ { 1 } e ^ { i \pi k x } f ( x ) d x = 0 .
$$

By the uniqueness of Fourier series coefficients, we must have $f = 0$ almost everywhere, and since $f$ is continuous we must have $f = 0$

Score:

The error of a quadrature rule with $p + 1$ distinct points $x _ { j }$ , weights $w _ { j }$ is

$$
E _ { p } ( f ) = \int _ { a } ^ { b } f ( x ) d x - \sum _ { j = 0 } ^ { p } w _ { j } f ( x _ { j } ) .
$$

Suppose that $E _ { p } ( f ) = 0$ whenever $f$ is a polynomial of degree $\leq q$ . Show that $q \leq 2 p + 1$ and if $q \geq 2 p$ then $w _ { j } > 0$ for all $j$ .

Solution: Define a polynomial f of degree $2 p + 2$ by

$$
f ( x ) = \prod _ { j = 0 } ^ { p } ( x - x _ { j } ) ^ { 2 } ,
$$

so that

$$
E _ { p } ( f ) = \int _ { a } ^ { b } f ( x ) d x > 0 .
$$

Since deg $f = 2 p + 2$ , we must have $q \leq 2 p + 1$

Let

$$
f _ { j } ( x ) = \prod _ { k \neq j } ( x - x _ { j } ) ^ { 2 } .
$$

Since deg $f = 2 p .$ , we must have $E _ { p } ( f ) = 0$ . Hence

$$
\int _ { a } ^ { b } f ( x ) d x = w _ { j } \prod _ { k \neq j } ( x _ { k } - x _ { j } ) ^ { 2 }
$$

and

$$
w _ { j } = \frac { \int _ { a } ^ { b } f ( x ) d x } { \prod _ { k \ne j } ( x _ { k } - x _ { j } ) ^ { 2 } } > 0 .
$$

Please cross out this problem if you do not wish it graded

## Problem 4B.

Score:

Given n distinct points $z _ { j } \in \mathbb { C }$ and n values $f _ { j } \in \mathbb { C }$ , show that there is a unique polynomial P of degree at most $n - 1$ such that

$$
P ( z _ { j } ) = f _ { j }
$$

for $1 \leq j \leq n .$

Solution: Define n polynomials $P _ { j }$ of degree $n - 1$ by

$$
P _ { j } ( z ) = \prod _ { k \neq j } { \frac { z - z _ { k } } { z _ { j } - z _ { k } } } ,
$$

so that $P _ { j } ( z _ { k } ) = \delta _ { j k }$ . Then

$$
P ( z ) = \sum _ { j = 1 } ^ { n } f _ { j } P _ { j } ( z )
$$

satisfies $P ( z _ { j } ) = f _ { j }$ for $1 \leq j \leq n$

Since the solution $a \in \mathbb { C } ^ { n }$ of the $n \times n$ linear system

$$
\sum _ { j = 0 } ^ { n - 1 } a _ { j } z _ { k } ^ { j } = f _ { k }
$$

exists for every right-hand side vector $f \in \mathbb { C } ^ { n }$ , the fundamental theorem of linear algebra guarantees uniqueness.

Please cross out this problem if you do not wish it graded

## Problem 5B.

Score:

Write all values of $i ^ { i }$ in the form $a + b i$

Solution: We have log $i = \log | i | + i \arg i = 0 + i \pi / 2$ (using the main branch of the log function). Taking all branches, we have log $i = i ( \pi / 2 + 2 n \pi ) , n \in \mathbb { Z }$ . Therefore

$$
i ^ { i } = e ^ { i \log i } = e ^ { i ^ { 2 } ( \pi / 2 + 2 n \pi ) } = e ^ { - ( \pi / 2 + 2 n \pi ) } + 0 i \ , \quad n \in \mathbb { Z } \ .
$$

Please cross out this problem if you do not wish it graded

Score:

Let D be the unit disk in the complex plane $\mathbb { C } , f : D  \mathbb { C }$ an analytic function with

$$
| f ^ { ( k ) } ( 0 ) | \le M
$$

for all $k \geq 0$ , and let $t _ { p } \in D , s _ { p } \in D$ for $1 \leq p \leq n$ . For each $n \geq 1$ define $A _ { i j } = f ( t _ { i } s _ { j } )$ for $1 \leq i , j \leq n$ . For each $r \geq 1$ find an $n \times n$ matrix B with rank $\leq r$ and

$$
| A _ { i j } - B _ { i j } | \leq { \frac { 2 M } { r ! } }
$$

for $1 \leq i , j \leq n$

Solution: By Taylor expansion,

$$
B _ { i j } = \sum _ { k = 0 } ^ { r - 1 } \frac { ( t _ { i } s _ { j } ) ^ { k } } { k ! } f ^ { ( k ) } ( 0 )
$$

satisfies

$$
| A _ { i j } - B _ { i j } | \leq \sum _ { k = r } ^ { \infty } { \frac { M } { k ! } } \leq { \frac { 2 M } { r ! } }
$$

by the geometric series.

## Problem 7B.

Score:

Suppose R is an invertible upper triangular complex matrix and A is symmetric. Find an explicit formula for the entries of the upper triangular matrix E satisfying

$$
E ^ { T } R + R ^ { T } E = A
$$

and show that your solution is unique. Hint: Multiply by $R ^ { - 1 T }$ and $R ^ { - 1 }$

Solution: Multiply by $R ^ { - 1 T }$ and $R ^ { - 1 }$ to get

$$
R ^ { - 1 T } E ^ { T } + E R ^ { - 1 } = R ^ { - T } A R ^ { - 1 }
$$

Since invertible upper triangular matrices form a group, $E R ^ { - 1 }$ is upper triangular and $R ^ { - T } E ^ { T }$ is lower triangular. Hence equating the two sides entry by entry shows that

$$
E = \mathrm { u p h } ( R ^ { - 1 T } A R ^ { - 1 } )
$$

where uph(B) is the upper triangle of B with the diagonal entries halved. Since E has $n ( n + 1 ) / 2$ entries satisfying $n ( n + 1 ) / 2$ linear equations to which we have shown a solution exists for every right-hand side A, the fundamental theorem of linear algebra guarantees its uniqueness.

Score:

Find a product of cyclic groups of prime power order isomorphic to (Z/1000000Z)∗ (the group of units of the ring of integers mod 1000000).

Solution: $\mathbb { Z } / 2 \mathbb { Z } \times \mathbb { Z } / 2 ^ { 4 } \mathbb { Z } \times \mathbb { Z } / 4 \mathbb { Z } \times \mathbb { Z } / 5 ^ { 5 } \mathbb { Z } .$

Please cross out this problem if you do not wish it graded

## Problem 9B.

Score:

Let $S _ { 9 }$ denote the group of permutations of 9 objects.

(a) Exhibit an element of $S _ { 9 }$ of order 20.

(b) Prove that no element of $S _ { 9 }$ has order 18.

Solution: (a) (1 2 3 4)(5 6 7 8 9) has order 20, because it is a product of a 4-cycle and a (disjoint) 5-cycle. They commute because they are disjoint, and they have orders 4 and 5, respectively, so their product has order 20.

(b) Suppose that $\sigma \in S _ { 9 }$ has order 18. Let $n _ { 1 } , \ldots , n _ { r }$ be the orders of its nontrivial cycles in a disjoint cycle decomposition. Then $n _ { i } > 1$ for all i, their lcm is 18, and their sum is at most 9.

This is impossible. Indeed, At least one $n _ { i }$ is a multiple of 9, so it must equal 9, and there can then be no other $n _ { i }$ in the sequence because the sum is $\leq 9$ . But {9} does not have lcm 18, a contradiction.