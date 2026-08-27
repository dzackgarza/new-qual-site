1. Answer six of the nine problems each day. You will get no extra credit for attempting more than 6 problems.

2. The exam lasts 3 hours each day. There is an extra half hour to give time to download it and to submit your solutions to gradescope.

3. Do not answer more than one question on any given piece of paper, as this will confuse the examiners.

4. The easiest way to submit your answers is by taking pictures of them with a phone and uploading them to gradescope.

5. The exam is open book: you may use notes or books or calculators or the internet, but should not consult anyone else.

6. In case of questions or unexpected problems during the prelim send email to the chair of the prelim committee If a correction or announcement is needed during the exam it will be sent as an email to the dummy address you use on gradescope for the prelim, so please keep an eye on this during the prelim.

## Problem 1A.

Score:

Find the volume of the solid given by $x ^ { 2 } + z ^ { 2 } \leq 1 , y ^ { 2 } + z ^ { 2 } \leq 1$ . (Hint: $\begin{array} { r } { \int _ { - 1 } ^ { 1 } ( s o m e t h i n g ) d z . ) } \end{array}$

Solution: The volume is $\textstyle \int _ { - 1 } ^ { 1 }$ 4xydz where $x = y = \sqrt { 1 - z ^ { 2 } }$ . This integral has value $1 6 / 3$

Please cross out this problem if you do not wish it graded

## Problem 2A.

Score:

Let

$$
\dots \subset X _ { 2 } \subset X _ { 1 }
$$

be a nested sequence of closed nonempty connected subsets of a compact metric space X.   
Prove that $\cap _ { i = 1 } ^ { \infty } X _ { i }$ is nonempty and connected.

Solution: Since $X _ { i }$ is closed in X, it is compact. The intersection of a nested sequence of nonempty compact sets is nonempty. (Proof : If it is empty then there is an open cover of X by the increasing sequence $\{ X - X _ { i } \} _ { i = 1 } ^ { \infty }$ . This must have a finite subcover, so $X _ { i } = \varnothing$ for some i, which is a contradiction.)

Suppose that $\cap _ { i = 1 } ^ { \infty } X _ { i }$ is not connected. Let A and B be two disjoint nonempty closed sets so that $\textstyle \bigcap _ { i = 1 } ^ { \infty } X _ { i } = A \cup B$ . Find disjoint open sets U and V so that $A \subset U$ and $B \subset V$ Put $F _ { i } = X _ { i } - ( U \cup V )$ Then $\{ F _ { i } \} _ { i = 1 } ^ { \infty }$ is a nested sequence of compact sets, whose intersection is empty. Thus $F _ { i } = \emptyset$ for some i. That is, $X _ { i } \subset U \cup V$

However, $X _ { i }$ intersects both U and V , since $X _ { i } \cap A \neq \emptyset$ and $X _ { i } \cap B \neq \varnothing$ . This contradicts the assumption that $X _ { i }$ is connected.

Please cross out this problem if you do not wish it graded

## Problem 3A.

Score:

Show that the series

$$
\sum _ { n = 1 } ^ { \infty } \sin { \frac { x } { n ^ { 2 } } }
$$

converges uniformly on any bounded interval in R.

Solution: Let I be a bounded interval in R.

Since li $\mathrm { n } _ { x  0 } \frac { \sin x } { x }$ exists, the function $( \sin x ) / x$ extends to a continuous function on all of R, so it is bounded on the bounded interval I. Therefore there is a C such that | sin $x | \leq C | x |$ for all $x \in I$ . (With a little extra work one can show that $C = 1$ works for all of R.)

Therefore if $| x | \le B$ for all $x \in I ,$ then the summands are bounded in absolute value by $B C / n ^ { 2 }$ , and therefore the sum converges uniformly on I by the Weierstrass M-test.

<table><tr><td>Problem 4A. Score:</td></tr></table>

If f is an analytic function from the unit disk into itself with $f ( 0 ) = 0$ , prove that $| f ^ { \prime } ( 0 ) | \le 1$

## Solution:

Put $g ( z ) = f ( z ) / z$ Then we have to show $| g ( 0 ) | \le 1$ But by the maximum modulus principle, for any positive $\epsilon , | g ( 0 ) |$ is at most the maximum of $| g |$ on a circle of radius $1 - \epsilon$ 5 which is at most $1 / ( 1 - \epsilon )$ because $| f ( z ) |$ is at most 1 and $| 1 / z |$ is at most $1 / ( 1 - \epsilon )$ . Since  can be anything positive this shows that $| f ^ { \prime } ( 0 ) | = | g ( 0 ) | \leq 1$

Please cross out this problem if you do not wish it graded

Score:

Use residues to compute

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { x ^ { 4 } + 1 } } .
$$

## Solution:

This is half of $\textstyle \int _ { - \infty } ^ { \infty } { \frac { d x } { x ^ { 4 } + 1 } }$ , and therefore πi times the sum of residues in the upper half plane (using the usual semicircular contour and the residue theorem). The residues are at√ √ $( i \pm 1 ) / \sqrt { 2 }$ and have values $1 / 4 ( i \pm 1 )$ so their sum is $- { \sqrt { 2 } } i / 4$ . The integral is therefore $\pi / 2 \sqrt { 2 }$

<table><tr><td>Problem 6A. Score:</td></tr></table>

Let A be an n by n real matrix such that all entries not on the diagonal are positive, and the sum of the entries in each row is negative. Show that the determinant of A is nonzero.

## Solution:

Proof by induction on the size of the matrix. Add a suitable multiple of the first column to each other column to kill all entries in the first row other than the first. Then the $( n - 1 ) \times ( n - 1 )$ matrix formed by crossing off the first row and column still has the property in the question, so its determinant is nonzero by induction. The determinant of the original matrix is this determinant times the first entry, so is also nonzero.

Please cross out this problem if you do not wish it graded

## Problem 7A.

Score:

Suppose L is a linear operator acting on a nontrivial vector space V over a field K. Suppose $P ( x ) \in K [ x ]$ is not identically zero and $P ( L ) = 0$ . Show every eigenvalue of L is a root of P . Show that if P factors completely over K then some roots of $P$ are eigenvalues of L.

## Solution:

Suppose $\textstyle P ( x ) = \sum _ { i = 0 } ^ { n } a _ { i } x ^ { i } , a _ { n } \neq 0$

Then if $L v = \lambda v .$

$$
P ( L ) v = \sum _ { i = 0 } ^ { n } a _ { i } L ^ { i } v = \sum _ { i = 0 } ^ { n } a _ { i } \lambda ^ { i } v = P ( \lambda ) v
$$

so if $v \neq 0 , P ( \lambda ) = 0$

Now suppose $\begin{array} { r } { P ( x ) = a _ { n } \prod _ { j = 1 } ^ { n } ( x - \lambda _ { j } ) , v _ { \neq 0 } \in V , \prod _ { j = 1 } ^ { k } ( L - \lambda _ { j } ) v \neq 0 \mathrm { a n d } \prod _ { j = 1 } ^ { k + 1 } ( L - \lambda _ { j } ) v = 0 } \end{array}$ Then $\lambda _ { k + 1 }$ is an eigenvalue.

## Problem 8A.

Find an irreducible polynomial over the integers with $2 \cos ( 2 \pi / 7 )$ as a root, and use this to show that it is not contained in any extension of the rational numbers of degree a power of 2.

## Solution:

Write $x = 2 \cos ( 2 \pi / 7 ) = z + 1 / z$ with $z ^ { 7 } = 1 , z \neq 1$ Then $x ^ { 3 } + x ^ { 2 } - 2 x - 1 =$ $z ^ { - 3 } + z ^ { - 2 } + z ^ { - 1 } + 1 + z + z ^ { 2 } + z ^ { 3 } = 0 .$ . This polynomial is irreducible as it is irreducible mod 2. So x generates a field extension of degree 3, so any field containing x has degree divisible by 3, so the degree cannot be a power of 2.

Please cross out this problem if you do not wish it graded

## Problem 9A.

Score:

For G a finite group, H a proper subgroup, show that $G \neq \bigcup \{ g H g ^ { - 1 } ; g \in G \}$

## Solution:

G acts on $A = \{ g H g ^ { - 1 } ; g \in G \}$ . For N = the normalizer of H, A has size $\left\lceil N : G \right\rceil$ . Since $H \subseteq N , [ H : G ] \geq [ N : G ]$ . But e is in each group in A, so $| \bigcup A | < [ H : G ] | H | = | G |$

1. Answer six of the nine problems each day. You will get no extra credit for attempting more than 6 problems.

2. The exam lasts 3 hours each day. There is an extra half hour to give time to download it and to submit your solutions to gradescope.

3. Do not answer more than one question on any given piece of paper, as this will confuse the examiners.

4. The easiest way to submit your answers is by taking pictures of them with a phone and uploading them to gradescope.

5. The exam is open book: you may use notes or books or calculators or the internet, but should not consult anyone else.

6. In case of questions or unexpected problems during the prelim send email to the chair of the prelim committee If a correction or announcement is needed during the exam it will be sent as an email to the dummy address you use on gradescope for the prelim, so please keep an eye on this during the prelim.

Score:

For which pairs of real numbers $( a , b )$ does the series $\scriptstyle \sum _ { n = 3 } ^ { \infty } n ^ { a } ( \log n ) ^ { b }$ converge?

## Solution:

By the integral test this is equivalent to asking for convergence of the integral

$$
\int _ { x = 3 } ^ { \infty } x ^ { a } ( \log x ) ^ { b } d x
$$

This converges if $a < - 1$ and diverges if $a > - 1$ by comparison with $\textstyle \int x ^ { s } d x$ . If $a = - 1$ then it converges for $b < - 1$ and diverges if $b > - 1$ again by doing the integral explicitly, using the fact that the derivative of $( \log x ) ^ { b + 1 }$ is $( b + 1 ) ( \log x ) ^ { b } x ^ { - 1 }$ . For $a = b = - 1$ it diverges as the derivative of log log x is $x ^ { - 1 } ( \log x ) ^ { - 1 }$

<table><tr><td>Problem 2B. Score:</td></tr></table>

Suppose that X is a compact metric space. If Y is another metric space (possibly noncompact), let $p : X \times Y  Y$ be the map $p ( x , y ) = y$ . Show that if Z is a closed subset of $X \times Y$ then $p ( Z )$ is closed in Y .

## Solution:

Suppose that $\{ y _ { i } \} _ { i = 1 } ^ { \infty }$ is a sequence in $p ( Z )$ which converges to some $y _ { \infty } \in Y$ . For each $i ,$ we can find $x _ { i } \in X$ so that $( x _ { i } , y _ { i } ) \in Z$ . After passing to a subsequence, we can assume that $\scriptstyle \operatorname* { l i m } _ { i \to \infty } x _ { i } = x _ { \infty }$ for some $x _ { \infty } \in X$ . Then li $\mathrm { m } _ { i \to \infty } ( x _ { i } , y _ { i } ) = ( x _ { \infty } , y _ { \infty } )$ lies in $Z _ { i }$ so $y _ { \infty } \in p ( Z )$ .

Score:

Prove the existence of the limit

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { 1 } } + { \frac { 1 } { 2 } } + { \frac { 1 } { 3 } } + \cdots + { \frac { 1 } { n } } - \log n .
$$

## Solution:

We can write this as $\textstyle 1 / n + \int _ { 1 } ^ { n } ( 1 / [ x ] - 1 / x ) d x$ The integral is an integral of a positive function, so tends to a limit or +∞ as n tends to ∞. On the other hand we can also write it as $\textstyle 1 + \int _ { 1 } ^ { n } ( 1 / [ x + 1 ] - 1 / x ) d x$ which is at most 1. So the integral in the first sentence above is bounded, and therefore tends to a (finite) limit. So the limit in the question exists.

## Problem 4B.

Score:

If $0 < r < 1$ , find

$$
\sum _ { k = 0 } ^ { \infty } r ^ { k } \cos ( k \theta ) .
$$

Your final answer should not involve any complex numbers.

## Solution:

Put $z = r e ^ { i \theta }$ . It’s enough to find the real part of

$$
\sum _ { k = 0 } ^ { \infty } z ^ { k } = { \frac { 1 } { 1 - z } } = { \frac { 1 } { 1 - r e ^ { i \theta } } } { \frac { 1 - r e ^ { - i \theta } } { 1 - r e ^ { - i \theta } } } = { \frac { 1 - r \cos ( \theta ) + i r \sin ( \theta ) } { 1 - 2 r \cos ( \theta ) + r ^ { 2 } } } ,
$$

so the answer is

$$
{ \frac { 1 - r \cos ( \theta ) } { 1 - 2 r \cos ( \theta ) + r ^ { 2 } } } .
$$

## Problem 5B.

If a and b are points in the open unit disk of the complex plane, show that there is a holomorphic map from the open unit disc onto itself with holomorphic inverse that takes a to b.

## Solution:

It is sufficient to do the case a = 0, because for the general case one can just compose a map taking a to 0 with a map taking 0 to b. The M¨obius transformation taking z to $( z + b ) / ( z \overline { { b } } + 1 )$ takes a = 0 to b.

Please cross out this problem if you do not wish it graded

## Problem 6B.

Score:

For each of the following 4 statements, give either a counterexample or a reason why it is true.

(a) For every real matrix A there is a real matrix B with $B ^ { - 1 } A B$ diagonal.

(b) For every symmetric real matrix A there is a real matrix B with $B ^ { - 1 } A B$ diagonal.

(c) For every complex matrix A there is a complex matrix B with $B ^ { - 1 } A B$ diagonal.

(d) For every symmetric complex matrix A there is a complex matrix B with $B ^ { - 1 } A B$ diagonal.

## Solution:

To generate counterexamples, observe that a nonzero 2 by 2 matrix with trace and determinant 0 cannot be diagonalizable as both eigenvalues vanish.

(a) False   0 10 0 

(b) True as Hermitean matrices are diagonalizable

(c) False   0 10 0 

(d) False $\left( \begin{array} { l l } { 1 } & { \it { i } } \\ { \it { i } } & { - 1 } \end{array} \right)$

<table><tr><td>Problem 7B. Score:</td></tr></table>

Find the eigenvalues of the $n \times n$ matrix with entries $a _ { i j }$ , where $a _ { i j }$ is 1 if $i = j + 1 , - 1$ if $i = j - 1$ , and 0 otherwise.

## Solution:

If λ is an eigenvalue and $( x _ { 1 } , \ldots , x _ { n } )$ an eigenvector, then $\lambda x _ { j } ~ = ~ x _ { j - 1 } - x _ { j + 1 }$ , with $x _ { 0 } = x _ { n + 1 } = 0$ . Solutions to the recurrence are of the form $x _ { j } = a _ { 1 } z _ { 1 } ^ { j } + a _ { 2 } z _ { 2 } ^ { j }$ with $z _ { 1 } , z _ { 2 }$ distinct root s of $\lambda = z ^ { - 1 } - z , \mathrm { ~ s o ~ } z _ { 1 } z _ { 2 } = - 1$ The boundary conditions give $a _ { 1 } + a _ { 2 } = 0$ $a _ { 1 } z _ { 1 } ^ { n + 1 } + a _ { 2 } z _ { 2 } ^ { n + 1 } = 0$ , so $z _ { 1 } ^ { n + 1 } = ( - 1 ) ^ { n + 1 } z _ { 1 } ^ { - ( n + 1 ) }$ . Also $z _ { 1 }$ is not ±i otherwise the roots are the same. So the eigenvalues are $2 \cos ( m \pi / ( n + 1 ) ) i$ for $0 < m \le n$

## Problem 8B.

Score:

Does there exists a homomorphism of commutative rings with unit from $\mathbb { Z } [ x ] / ( x ^ { 2 } + 3 )$ to $\mathbb { Z } [ x ] / ( x ^ { 2 } - x + 1 ) ?$ Either exhibit such a homomorphism, or prove that none exists.

## Solution:

The question amounts to whether −3 has a square root in the ring $S = \mathbb { Z } [ x ] / ( x ^ { 2 } - x + 1 )$ The elements of S may be written $a x + b , a , b \in \mathbb { Z }$ , and the square of such an element is then given by

$$
( a x + b ) ^ { 2 } = a ^ { 2 } ( x - 1 ) + 2 a b x + b ^ { 2 } = ( a ^ { 2 } + 2 a b ) x + ( b ^ { 2 } - a ^ { 2 } ) .
$$

So we need a solution in integers of the equations $a ^ { 2 } + 2 a b = 0 , b ^ { 2 } - a ^ { 2 } = - 3$ . The solutions are $( b = 1 , a = - 2 )$ and $( b = - 1 , a = 2 )$ . Hence there are two ring homomorphisms

$$
\mathbb { Z } [ x ] / ( x ^ { 2 } + 3 ) \to \mathbb { Z } [ x ] / ( x ^ { 2 } - x + 1 )
$$

$$
x \mapsto \pm ( 2 x - 1 ) .
$$

Score:

Prove that the polynomial $x ^ { 4 } + x + 2 0 2 1$ is irreducible over $\mathbb { Q } .$

## Solution:

It is sufficient to check irreducibility in $\mathbb { Z } [ x ]$ and for this it is enough to check irreducibility mod 2. For this just check it has no linear factors and is not divisible by the only irreducible degree 2 mod 2 polynomial $x ^ { 2 } + x + 1$