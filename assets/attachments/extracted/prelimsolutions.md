1. Answer six of the nine problems each day. You will get no extra credit for attempting more than 6 problems.

2. The exam lasts 3 hours each day. This does not include the time taken to download it or to submit your solutions to gradescope, for which you are allowed an extra half hour. Answers submitted later than this without a good reason may have points deducted.

3. Do not answer more than one question on any given piece of paper, as this will confuse the examiners.

4. The easiest way to submit your answers is by taking pictures of them with a phone and uploading them to gradescope. At the moment gradescope makes you submit answers even for the three questions you did not attempt, so submit a photo of a blank sheet of paper. Please do not use the option to upload all your answers as a single PDF file.

5. The exam is open book: you may use notes or books or calculators or the internet, but should not consult anyone else.

6. In case of questions or unexpected problems during the prelim send email to the chair of the prelim committee at borcherds@berkeley.edu If a correction or announcement is needed during the exam it will be sent as an email to the dummy address you use on gradescope for the prelim, so please keep an eye on this during the prelim.

Please cross out this problem if you do not wish it graded

## Problem 1A.

Score:

Find the indefinite integral

$$
\int e ^ { 2 x } \sin x d x \ .
$$

Solution: Doing integration by parts with

$$
\begin{array} { c c } { { u = e ^ { 2 x } } } & { { \qquad d v = \sin x d x } } \\ { { d u = 2 e ^ { 2 x } d x } } & { { \qquad v = - \cos x } } \end{array}
$$

gives

$$
\int e ^ { 2 x } \sin x d x = - e ^ { 2 x } \cos x + 2 \int e ^ { 2 x } \cos x d x .
$$

Applying integration by parts to the integral in the above with

$$
\begin{array} { c c } { { u = e ^ { 2 x } } } & { { \qquad d v = \cos x d x } } \\ { { d u = 2 e ^ { 2 x } d x } } & { { \qquad v = \sin x } } \end{array}
$$

gives

$$
\int e ^ { 2 x } \cos x d x = e ^ { 2 x } \sin x - 2 \int e ^ { 2 x } \sin x d x .
$$

Therefore, substituting and solving for the integral in question gives

$$
\int e ^ { 2 x } \sin x d x = - e ^ { 2 x } \cos x + 2 \left( e ^ { 2 x } \sin x - 2 \int e ^ { 2 x } \sin x d x \right) ;
$$

$$
5 \int e ^ { 2 x } \sin x d x = e ^ { 2 x } ( 2 \sin x - \cos x ) + C ;
$$

$$
\int e ^ { 2 x } \sin x d x = { \frac { e ^ { 2 x } ( 2 \sin x - \cos x ) } { 5 } } + C \ .
$$

## Problem 2A.

Score:

Let S be a set and let $\left\{ f _ { n } \right\}$ and $\left\{ g _ { n } \right\}$ be sequences of functions $S \to \mathbb { R }$

(a) Show that if $\{ f _ { n } \}$ and $\left\{ g _ { n } \right\}$ converge uniformly to bounded functions f and g on $S _ { i }$ respectively, then $\left\{ f _ { n } g _ { n } \right\}$ converges uniformly to $f g$ on S.

(b) Show by giving a counterexample that the statement is false if f is not required to be bounded.

Solution: (a) Let B and C be bounds such that $| f ( s ) | \le B$ and $| g ( s ) | \le C$ for all $s \in S$ Let $\epsilon > 0$ . Pick $\epsilon _ { 1 } > 0$ and $\epsilon _ { 2 } > 0$ such that $( B + \epsilon _ { 1 } ) \epsilon _ { 2 } + C \epsilon _ { 1 } \leq \epsilon ,$ and pick N such that $| f _ { n } ( s ) - f ( s ) | < \epsilon _ { 1 }$ and $| g _ { n } ( s ) - g ( s ) | < \epsilon _ { 2 }$ for all $n \geq N$ and all $s \in S$ . Then $| f _ { n } ( s ) | \le B + \epsilon _ { 1 }$ for all $n \geq N$ and all $s \in S$ S, so

$$
\begin{array} { r l } & { | f _ { n } ( s ) g _ { n } ( s ) - f ( s ) g ( s ) | = | f _ { n } ( s ) ( g _ { n } ( s ) - g ( s ) ) + ( f _ { n } ( s ) - f ( s ) ) g ( s ) | } \\ & { \phantom { | f _ { n } ( s ) } \leq | f _ { n } ( s ) | | g _ { n } ( s ) - g ( s ) | + | f _ { n } ( s ) - f ( s ) | | g ( s ) | } \\ & { \phantom { | f _ { n } ( s ) } < ( B + \epsilon _ { 1 } ) \epsilon _ { 2 } + \epsilon _ { 1 } C } \\ & { \phantom { | f _ { n } ( s ) } \leq \epsilon } \end{array}
$$

for all $n \geq N$ and all $s \in S$ . Therefore $\left\{ f _ { n } g _ { n } \right\}$ converges uniformly to $f g$ on $S$

(b) $\operatorname { L e t } \ S \ = \ \mathbb { R }$ and let $f _ { n } ( x ) \ = \ x$ and $g _ { n } ( x ) = 1 + 1 / n$ for all $n \geq 1$ Then $\{ f _ { n } \}$ converges (uniformly) to the (unbounded) function $f = x$ , and $\left\{ g _ { n } \right\}$ converges uniformly to the constant function $g = 1$ . But the sequence $\left\{ f _ { n } g _ { n } \right\} = \left\{ x + x / n \right\}$ converges only pointwise to $f g = x$

<table><tr><td>Problem 3A. Score:</td></tr></table>

Let X be a metric space, and let $\{ T _ { 1 } , T _ { 2 } , \dots \}$ be an infinite sequence of nonempty closed subsets of X. Assume that $T _ { 1 }$ is compact and that $T _ { n } \supseteq T _ { n + 1 }$ for all $n \geq 1$ Show that $\textstyle \bigcap _ { n = 1 } ^ { \infty } T _ { n } \neq \emptyset$

Solution: Suppose by way of contradiction that the intersection is empty. Then $\{ X \} \cap T _ { n }$ : $n = 1 , 2 , \dots \}$ is a cover of $T _ { 1 }$ by open sets. By compactness, it has a finite subcover, which we may assume to be $\{ X \setminus T _ { n } : n = 1 , 2 , . . . , k \}$ for some $k > 0 .$ . Since $X \setminus T _ { n } \subseteq X \setminus T _ { n + 1 }$ for all $n \geq 1$ , we then have $X \setminus T _ { k } \supseteq T _ { 1 }$ , which implies $T _ { k } \cap T _ { 1 } = \emptyset$ , and therefore $T _ { k } = \emptyset$ since $T _ { k } \subseteq T _ { 1 }$ . This is a contradiction, so the intersection must be nonempty.

Score:

By definition, an infinite product converges if the sequence of finite partial products converges to a non-zero number. Find the set of complex numbers z for which the infinite product

$$
\prod _ { k = 1 } ^ { \infty } ( 1 - z ^ { k } )
$$

converges.

## Solution:

Solution. The product $\textstyle \prod _ { k = 1 } ^ { \infty } ( 1 - z ^ { k } )$ converges if and only $\mathrm { i f } \ | z | < 1$

If z is a root of unity, then some of the factors vanish and the product is zero, hence divergent by definition. If $| z | \geq 1$ and z is not a root of unity, then all factors are non-zero, and there is a constant $A > 1$ such that $| 1 - z ^ { k } | > A$ for infinitely many k, which implies that the product diverges.

Otherwise, we have $| z | < 1$ . Let “log” denote the principal branch of the logarithm. Since $\log ( 1 ) = 0$ and $\begin{array} { r } { \frac { d } { d x } \log ( 1 + x ) | _ { x = 0 } = 1 } \end{array}$ , we have $| \mathrm { l o g } ( 1 + x ) | < C | x | { \mathrm { ~ f o r ~ } } | x |$ sufficiently small, where C is any constant greater than 1. In particular, |log $( 1 - z ^ { k } ) | < C | z | ^ { k }$ for k sufficiently large, which implies that $\textstyle \sum _ { k = 1 } ^ { \infty } \log ( 1 - z ^ { k } )$ converges. This is equivalent to $\textstyle \prod _ { k = 1 } ^ { \infty } ( 1 - z ^ { k } )$ converging.

Please cross out this problem if you do not wish it graded

## Problem 5A.

Score:

(a) Find a Laurent series representing $f ( z ) = 1 / ( z ( 1 + z ^ { 2 } ) )$ for $| z | < 1$ . (b) Find another Laurent series representing $f ( z )$ for $| z | > 1$

Solution: (a) By the geometric series,

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } z ^ { 2 n - 1 }
$$

for $| z | < 1$

(b)

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } ( - 1 ) ^ { n } z ^ { - 2 n - 3 } .
$$

for $| z | > 1$

<table><tr><td>Problem 6A. Score:</td></tr></table>

Let A be an $n \times n$ symmetric positive definite matrix. (a) Show that there is an upper triangular matrix R with positive diagonal elements such that $R ^ { T } R = A$ . (b) Show that $R R ^ { T }$ has the same eigenvalues as A.

Solution: (a) Let $B = Q R$ be a QR factorization (obtained for example by Gram-Schmidt orthonormalization of the columns of B) of the symmetric positive definite square root $B = B ^ { T }$ of A (obtained for example by eigenvalue-eigenvector decomposition). Then R is upper triangular with positive diagonal entries and Q is orthogonal, so

$$
\begin{array} { r } { R ^ { T } R = R ^ { T } Q ^ { T } Q R = B ^ { T } B = B ^ { 2 } = A . } \end{array}
$$

Or use Gaussian elimination or induction on n.

(b) Since R is invertible and $R ^ { T } R = A$ , we have $R ^ { T } = A R ^ { - 1 }$ . Hence $R R ^ { T } = R A R ^ { - 1 }$ is a similarity transform of A and therefore has the same eigenvalues as A.

Please cross out this problem if you do not wish it graded

## Problem 7A.

Score:

Let V be a vector space of dimension n over a finite field with q elements. Prove that the number of subspaces $W \subseteq V$ of dimension k is equal to

$$
\frac { \prod _ { j = 1 } ^ { n } ( q ^ { j } - 1 ) } { ( \prod _ { j = 1 } ^ { k } ( q ^ { j } - 1 ) ) ( \prod _ { j = 1 } ^ { n - k } ( q ^ { j } - 1 ) ) } .
$$

Solution: The number of ordered bases of V is $( q ^ { n } - 1 ) ( q ^ { n } - q ) \cdot \cdot \cdot ( q ^ { n } - q ^ { - 1 } )$ , since after choosing the first j basis elements, we have $q ^ { n } - q ^ { j }$ choices for a next element not in the span of the first j.

Similarly, the number of ordered bases of V that start with a basis of any given kdimensional subspace W is $( q ^ { k } - 1 ) ( q ^ { k } - q ) \cdot \cdot \cdot ( q ^ { k } - q ^ { k - 1 } ) \times ( q ^ { n } - q ^ { k } ) ( q ^ { n } - q ^ { k + 1 } ) \cdot \cdot \cdot ( q ^ { n } - q ^ { n - 1 } )$

Dividing the first of these by the second and simplifying gives the desired formula.

## Problem 8A.

Score:

Let $F = \mathbb { Z } / ( 1 7 9 )$ be the finite field with 179 elements.

(a) Prove that the residue class of 10 (mod 179) is not the square of any element of F .

(b) Prove that this residue class generates the multiplicative group of non-zero elements of F .

Solution: (a) Since the multiplicative group $F ^ { \times }$ is cyclic of order $2 \times 8 9$ , the non-zero squares in F are the elements x such that $x ^ { 8 9 } = 1$ . Hence −1 is not a square, and therefore $1 0 \equiv - 1 \cdot 1 3 ^ { 2 }$ is also not a square. (Alternative solution: use quadratic reciprocity to show that 5 is a square and 2 is not a square.)

(b) The group $F ^ { \times }$ is isomorphic to $( \mathbb { Z } / ( 2 ) ) \times ( \mathbb { Z } / ( 8 9 ) )$ . Since 89 is prime, the only elements which do not generate $F ^ { \times }$ are the 89th powers and the squares. The 89th powers in F are ±1, and we saw in part (a) that 10 is not a square.

<table><tr><td>Problem 9A.</td><td>Score:</td></tr><tr><td></td><td></td></tr></table>

Prove that if a and b are odd integers, then the polynomial $f ( x ) = x ^ { 3 } + a x + b$ has no rational roots.

## Solution:

If f has a rational root, then it is reducible over Q. By Gauss’s Lemma, this implies that f factors properly over Z, and therefore the reduction of f (mod 2) factors over the field $F = \mathbb { Z } / ( 2 )$ Since f is cubic, at least one factor must be linear, so f must have a root in F . But f reduces mod 2 to $x ^ { 3 } + x + 1$ , and neither element of $F = \{ 0 , 1 \}$ is a root.

Department of Mathematics, University of California, Berkeley

1. Answer six of the nine problems each day. You will get no extra credit for attempting more than 6 problems.

2. The exam lasts 3 hours each day. This does not include the time taken to download it or to submit your solutions to gradescope, for which you are allowed an extra half hour. Answers submitted later than this without a good reason may have points deducted.

3. Do not answer more than one question on any given piece of paper, as this will confuse the examiners.

4. The easiest way to submit your answers is by taking pictures of them with a phone and uploading them to gradescope.

5. The exam is open book: you may use notes or books or calculators or the internet, but should not consult anyone else.

6. In case of questions or unexpected problems during the prelim send email to the chair of the prelim committee at borcherds@berkeley.edu If a correction or announcement is needed during the exam it will be sent as an email to the dummy address you use on gradescope for the prelim, so please keep an eye on this during the prelim.

<table><tr><td>Problem 1B. Score:</td></tr></table>

Prove that it is not possible to find 4 polynomials $\boldsymbol { a } ( \boldsymbol { x } ) , \boldsymbol { b } ( \boldsymbol { x } ) , \boldsymbol { c } ( \boldsymbol { x } ) , d ( \boldsymbol { x } )$ with real coefficients such that $a ( x ) < b ( x ) < c ( x ) < d ( x )$ for $0 \textless x \textless 1$ and $b ( x ) < d ( x ) < a ( x ) < c ( x )$ for $- 1 < x < 0$

(Hint: show that you may assume one polynomial is equal to zero, and then examine the smallest nonzero terms of the others.)

Solution: We can assume $a ( x ) = 0$ . Suppose the smallest nonzero terms are given by $b ( x ) = b _ { i } x ^ { i } + . . . , c ( x ) = c _ { j } x ^ { j } + . . . , d ( x ) = d _ { k } x ^ { k } + . . . .$ By looking at $0 < x < 1$ we see that $b _ { i } > 0 , c _ { j } > 0 , d _ { k } > 0$ and $i \geq j \geq k$ . By looking at the values for $x < 0$ and using the fact that $b _ { i } > 0 , c _ { i } > 0 , d _ { k } > 0$ we then see that $j$ is even and i and k are odd, so $i > j > k$ . But $i > k$ then implies that $b ( x ) > d ( x )$ for small negative x, which is a contradiction.

## Problem 2B.

Score:

Either prove or give a counterexample to each of the following statements:

(a) If the series (of real numbers) $a _ { 1 } + a _ { 2 } + \cdots$ and $b _ { 1 } + b _ { 2 } + \cdots$ are both convergent then so is $( a _ { 1 } + b _ { 1 } ) + ( a _ { 2 } + b _ { 2 } ) + \cdot \cdot \cdot$

(b) If the series (of real numbers) $a _ { 1 } + a _ { 2 } + \cdots$ and $b _ { 1 } + b _ { 2 } + \cdots$ are both convergent then so is $a _ { 1 } b _ { 1 } + a _ { 2 } b _ { 2 } + \cdots$ •

Solution: (a) is true. This follows from Cauchy’s criterion of convergence.

(b) is false. For example, $a _ { n }$ and $b _ { n }$ might be alternating and tending very slowly to 0, such as $a _ { n } = b _ { n } = ( - 1 ) ^ { n } / { \sqrt { n } }$

## Problem 3B.

Score:

Prove that every closed subset C of the real line is the closure of a finite or countable set.

Solution: Let the countable collection of subsets $E _ { n }$ of R be the closed intervals with rational endpoints. If $C \cap E _ { n }$ is nonempty pick a point $e _ { n }$ in it. Then the set of points $e _ { n }$ has closure C.

Please cross out this problem if you do not wish it graded

<table><tr><td>Problem 4B. Score:</td></tr></table>

(a) Let n be a positive integer. Find all poles of $\pi / ( z ^ { n } \tan ( \pi z ) )$ and find the residues of all poles of order 1.

(b) Prove that if n is a positive even integer then $( 1 / 1 ^ { n } + 1 / 2 ^ { n } + 1 / 3 ^ { n } + \cdot \cdot \cdot ) / \pi ^ { n }$ is a rational number.

Solution: $\pi / ( z ^ { n } \tan ( \pi z ) )$ has poles of order 1 and residue $1 / m ^ { n }$ at all nonzero integers m. The sum of all its residues is 0 by Cauchy’s theorem applied to a suitable large rectangle centered on 0. So the sum in the question is $( - 1 / 2 )$ times the residue at 0, which is a rational multiple of $\pi ^ { n }$ because the Laurent series of $1 / \tan ( z )$ has rational coefficients.

<table><tr><td>Problem 5B. Score:</td></tr></table>

(a) Find a function, holomorphic on the closed unit disc, that has absolute value 1 on the unit circle and whose only zero inside the unit circle is at $1 / 2$

(b) Let f be holomorphic on the closed unit disc, with $f ( 1 / 2 ) = 0$ and $| f ( z ) | \leqslant | e ^ { z } |$ for all z with $| z | = 1$ . How large can $| f ( 0 ) |$ be?

Solution: (a) $g ( z ) = ( z - 1 / 2 ) / ( 1 - z / 2 )$

(b) $f ( z ) / g ( z ) e ^ { z }$ is holomorphic on the unit disk and bounded by 1 on the boundary, so is bounded by 1 everywhere in the disc. So $| f ( 0 ) | \le | g ( 0 ) e ^ { 0 } | = 1 / 2$ (with equality when $f ( z ) = g ( z ) e ^ { z } )$

Problem 6B.

Score:

Let

$$
H _ { i j } = \int _ { 0 } ^ { 1 } t ^ { i } t ^ { j } d t , \qquad 0 \leq i , j \leq n
$$

be the elements of the $n + 1 \times n + 1$ Hilbert matrix H. Let

$$
P _ { i } ( t ) = \sum _ { j = 0 } ^ { i } p _ { i j } t ^ { j } , \qquad 0 \leq i , j \leq n ,
$$

define the coefficients $p _ { i j }$ of the orthonormal Legendre polynomials so that

$$
\int _ { 0 } ^ { 1 } P _ { i } ( t ) P _ { j } ( t ) d t = \delta _ { i j } , 0 \leq i , j \leq n .
$$

Show that $H ^ { - 1 } = P ^ { T } P$ , where P is the matrix with entries $p _ { i j }$

Solution:

$$
\int _ { 0 } ^ { 1 } P _ { i } ( t ) P _ { j } ( t ) d t = \sum _ { \alpha = 0 } ^ { i } p _ { i \alpha } \sum _ { \beta = 0 } ^ { j } p _ { j \beta } H _ { \alpha \beta } = \delta _ { i j } ,
$$

so

$$
I = P H P ^ { T } .
$$

Since I is invertible, so are P , H and $P ^ { T }$ and applying $P ^ { - 1 }$ and $( P ^ { - 1 } ) ^ { T } = P ^ { - T }$ gives

$$
P ^ { - 1 } P ^ { - T } = H .
$$

Inverting both sides gives

$$
H ^ { - 1 } = P ^ { T } P
$$

so $L = P$ is the desired invertible lower-triangular factor.

Let A be a linear transformation on a vector space W over a field k, such that $A ^ { 5 } = I$ (the identity transformation).

(a) Show that if k does not have characteristic 5 then W can be written as a direct sum of subspaces U and V where U consists of the vectors u with $A u = u$ , and $A V = V$ . (The condition $A V = V$ was accidentally omitted on the actual prelim, making the first part trivial and the second part false. Most students who tried this question correctly figured out the missing condition.)

(b) Give an example to show that this property can fail if k has characteristic 5.

## Solution:

(a) Project W onto U by mapping each vector to the average $( u + A u + A ^ { 2 } u + A ^ { 3 } u + A ^ { 4 } u ) / 5$ and take V to be the kernel of this projection.

YOUR EXAM NUMBER

Please cross out this problem if you do not wish it graded

Problem 8B.

Score:

Recall that $S _ { 3 }$ is the symmetric group on 3 letters.

Find all conjugacy classes of elements of $S _ { 3 }$ (list the elements of each conjugacy class).

Solution: The conjugacy classes are

$$
\{ 1 \} , \quad \{ ( 1 2 ) , ( 1 3 ) , ( 2 3 ) \} , \quad \mathrm { a n d } \quad \{ ( 1 2 3 ) , ( 3 2 1 ) \} .
$$

The fact that no element of any of the above sets is conjugate to any element of any other set follows from the fact that all elements of these sets have order 1, 2, and 3, respectively. Since conjugating gives an automorphism of $S _ { 3 }$ , it preserves the order of an element, so no two elements of different orders can be conjugate.

As for the fact that all elements of each set are conjugate to each other, this needs to be proved by showing explicit conjugacies. For the first set there is nothing to be shown. For the second set, we have

$$
( 2 3 ) ( 1 2 ) ( 2 3 ) ^ { - 1 } = ( 1 3 ) ,
$$

$$
( 1 2 ) ( 3 1 ) ( 1 2 ) ^ { - 1 } = ( 3 2 ) ,
$$

$$
( 3 1 ) ( 2 3 ) ( 3 1 ) ^ { - 1 } = ( 2 1 ) .
$$

And, for the third set:

$$
( 2 3 ) ( 1 2 3 ) ( 2 3 ) ^ { - 1 } = ( 3 2 1 ) .
$$

Score:

For which integers n is $x ^ { 4 } + n$ a reducible polynomial in $\mathbb { Z } [ x ] ?$

Solution: Reducible if n is of the form $4 m ^ { 4 } \ { \mathrm { o r } } \ - m ^ { 2 }$

It has a linear factor if and only $\mathrm { i f } - n$ is a 4th power. For quadratic factors we have $( x ^ { 2 } + a x + b ) ( x ^ { 2 } - a x + b )$ or $( x ^ { 2 } + b ) ( x ^ { 2 } - b )$ (the constant terms must have the same sign if $a \neq 0 . )$ The first case gives $a ^ { 2 } = 2 b , b ^ { 2 } = n$ so $4 n = a ^ { 4 }$ . Then $a = 2 m$ is even and $n = 4 m ^ { 4 }$ The second case gives $n = - b ^ { 2 }$