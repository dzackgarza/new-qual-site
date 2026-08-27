1A. Compute

$$
\operatorname * { l i m } _ { x \to 0 } { \frac { d ^ { 4 } } { d x ^ { 4 } } } { \frac { x } { \sin x } } .
$$

Solution: By Taylor’s formula,

$$
\sin x = x - { \frac { x ^ { 3 } } { 6 } } + { \frac { x ^ { 5 } } { 1 2 0 } } + o ( x ^ { 5 } ) .
$$

Therefore

$$
\begin{array} { l } { \displaystyle { \frac { x } { \sin x } = \frac { 1 } { 1 - \frac { x ^ { 2 } } { 6 } + \frac { x ^ { 4 } } { 1 2 0 } + o ( x ^ { 4 } ) } } } \\ { \displaystyle { \quad = 1 + ( \frac { x ^ { 2 } } { 6 } - \frac { x ^ { 4 } } { 1 2 0 } + o ( x ^ { 4 } ) ) + ( \frac { x ^ { 2 } } { 6 } + o ( x ^ { 2 } ) ) ^ { 2 } + o ( x ^ { 4 } ) } } \\ { \displaystyle { \quad = 1 + \frac { x ^ { 2 } } { 6 } + \left[ \frac { 1 } { 3 6 } - \frac { 1 } { 1 2 0 } \right] x ^ { 4 } + o ( x ^ { 4 } ) . } } \end{array}
$$

Thus,

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { d ^ { 4 } } { d x ^ { 4 } } } { \frac { x } { \sin x } } = 4 ! \left[ { \frac { 1 } { 3 6 } } - { \frac { 1 } { 1 2 0 } } \right] = { \frac { 2 } { 3 } } - { \frac { 1 } { 5 } } = { \frac { 7 } { 1 5 } } .
$$

2A. Let

$$
A = { \binom { 3 } { 1 } } \ { - 2 } ) .
$$

Compute

$$
e ^ { A } : = \sum _ { n = 0 } ^ { \infty } { \frac { A ^ { n } } { n ! } } .
$$

Solution: The matrix A has eigenvalues 2 and 1 with eigenvectors (2, 1) and (1, 1) respectively. Therefore

$$
A = { \binom { 2 } { 1 } } \left( { \begin{array} { l l } { 2 } & { 0 } \\ { 0 } & { 1 } \end{array} } \right) { \binom { 2 } { 1 } } { \binom { 2 } { 1 } } ^ { - 1 } .
$$

Observe that

$$
e ^ { C B C ^ { - 1 } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( C B C ^ { - 1 } ) ^ { n } } { n ! } } = \sum _ { n = 0 } ^ { \infty } { \frac { C B ^ { n } C ^ { - 1 } } { n ! } } = C e ^ { B } C ^ { - 1 } .
$$

Therefore

$$
e ^ { A } = { \left( \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right) } \left( e ^ { 2 }  & { 0 } \\ { 0 } &  e \right) \left( { \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} } \right) ^ { - 1 } = \left( { \begin{array} { l l } { 2 e ^ { 2 } } & { e } \\ { e ^ { 2 } } & { e } \end{array} } \right) \left( { \begin{array} { l l } { 1 } & { - 1 } \\ { - 1 } & { 2 } \end{array} } \right) = \left( { \begin{array} { l l } { 2 e ^ { 2 } - e } & { - 2 e ^ { 2 } + 2 e } \\ { e ^ { 2 } - e } & { - e ^ { 2 } + 2 e } \end{array} } \right) .
$$

3A. Let U be a connected open subset of C containing −2 and 0. Suppose that $f \colon U \to \mathbb { C }$ is a holomorphic function whose Taylor expansion at 0 is $\textstyle \sum _ { n \geq 0 } { \binom { 2 n } { n } } z ^ { n }$ . Prove that $f ( - 2 ) \in$

$\{ 1 / 3 , - 1 / 3 \}$ . (Note: The original version of this problem had an error: $\{ 3 , - 3 \}$ instead of $\{ 1 / 3 , - 1 / 3 \} . )$

Solution: We claim that $f ( z ) ^ { 2 } = ( 1 - 4 z ) ^ { - 1 }$ . Since a holomorphic function on a connected open set is determined by its values on any nonempty open subset, it suffices to prove $f ( z ) ^ { 2 } = ( 1 - 4 z ) ^ { - 1 }$ in a neighborhood of 0.

One way to do this is to expand $( 1 - 4 z ) ^ { - 1 / 2 }$ using the binomial theorem, and check that it agrees with $\textstyle \sum _ { n > 0 } { \binom { 2 n } { n } } z ^ { n }$ . But this assumes that we guessed the formula $( 1 - 4 z ) ^ { - 1 / 2 }$

A more motivated solution is to find a differential equation satisfied by f(z) (in a neighborhood of 0). Rewrite the series as

$$
f = \sum _ { n = 0 } ^ { \infty } { \frac { ( 2 n - 1 ) ! ! } { n ! } } ( 2 z ) ^ { n } ,
$$

where $( 2 n - 1 ) ! !$ denotes the product of all odd positive integers up to $2 n - 1$ . The series satisfies the 1st order differential equation:

$$
z { \frac { d } { d z } } f = 2 z ( 2 z { \frac { d } { d z } } + 1 ) f .
$$

It can be rewritten as

$$
\frac { d f } { d z } = \frac { 2 f } { 1 - 4 z } ,
$$

which is not hard to solve:

$$
\int \frac { d f } { f } = \int \frac { 2 d z } { 1 - 4 z } , \mathrm { o r } \ln f = - \frac { 1 } { 2 } \ln ( 1 - 4 f ) + c o n s t ,
$$

i.e. $f = C ( 1 - 4 z ) ^ { - 1 / 2 }$ . The value $C = 1$ is found from $f ( 0 ) = 1$

$$
\mathrm { N o w } \ f ( - 2 ) ^ { 2 } = ( 1 - 4 ( - 2 ) ) ^ { - 1 } = 1 / 9 , \mathrm { s o } \ f ( - 2 ) \in \{ 1 / 3 , - 1 / 3 \} .
$$

4A. Let R be a finite commutative ring without zero-divisors and containing at least one element other than 0. (As usual, rings are associative with 1.) Prove that R is a field.

Solution: Let $a \in R , a \neq 0$ and let $f : R  R$ be $f ( x ) = a x , x \in R .$ Then $f$ is one-to-one since there are no zero-divisors in R. Then $f$ is onto since R is finite. Thus there exists a unique $x _ { a } \in R$ such that $a x _ { a } = a$ . Let us show that $x _ { a }$ plays the role of unity in R. Indeed, for every $b \in R$ there is a unique $x _ { b } \in R$ such that $b = a x _ { b }$ . We have $b x _ { a } = a x _ { b } x _ { a } = a x _ { a } x _ { b } = a x _ { b } = b$ . So $x _ { a } = 1$ . For each $0 \neq b \in R$ there is a unique b0 with $b b ^ { \prime } = 1$ . Thus $b ^ { \prime } = b ^ { - 1 }$

5A. Let $C ^ { 0 } [ 0 , 1 ]$ be the vector space over R consisting of continuous functions from $[ 0 , 1 ]$ to R. Show that the linear operator $T \colon C ^ { 0 } [ 0 , 1 ] \to C ^ { 0 } [ 0 , { \bar { 1 } } ]$ defined by

$$
( T f ) ( x ) : = \int _ { 0 } ^ { x } f ( y ) d y
$$

has no nonzero eigenvectors.

Solution: Suppose that $f \in C ^ { 0 } [ 0 , 1 ]$ and $\lambda \in \mathbb { R }$ satisfy $T f = \lambda f$ . By the fundamental theorem of calculus, $T f$ is differentiable, and its derivative is $( T f ) ^ { \prime } = f$ . Therefore $\lambda f ^ { \prime } = f$ Solving this differential equation (e.g. by separation of variables), we find that if $\lambda = 0$ then $f = 0$ , while if $\lambda \neq 0$ then $f = C e ^ { x / \lambda }$ . But we observe that $( T f ) ( 0 ) = 0$ , so in the case when $\lambda \neq 0$ we have $C = 0$ . Either way, $f = 0$ . Thus $T$ has no nonzero eigenvector.

6A. Let $p$ be prime. Prove that the polynomial $f \left( x \right) = x ^ { p } - x + 1$ is irreducible over the field $\mathbb { F } _ { p }$ of p elements.

Solution: Let α be a zero of f in some field extension of $\mathbb { F } _ { p } .$ Because of the identity $( x + y ) ^ { p } = x ^ { p } + y ^ { p }$ in characteristic p, we have $f ( x + 1 ) = f ( x )$ . By induction, $f ( x + a ) = f ( x )$ for all $a \in \mathbb { F } _ { p }$ . In particular, $f ( \alpha + a ) = f ( \alpha ) = 0$ . Thus the p elements $\alpha + a$ for $a \in \mathbb { F } _ { p }$ are all the zeros of $f ( x )$ .

Suppose $f ( x ) = g ( x ) h ( x )$ for some monic polynomials $g , h \in \mathbb { F } _ { p } [ x ]$ . Then $\begin{array} { r } { g ( x ) = \prod _ { i \in I } ( x - } \end{array}$ $( \alpha + i ) )$ for some subset $I \subseteq \mathbb { F } _ { p }$ . The sum of the zeros of g is in $\mathbb { F } _ { p } ,$ s o

$$
( \# I ) \alpha + ( \sum _ { i \in I } i ) \in \mathbb { F } _ { p } .
$$

Thus $( \# I ) \alpha \in \mathbb { F } _ { p }$ . Since f is irreducible, $\alpha \notin \mathbb { F } _ { p }$ , so $\# I$ must be divisible by $p .$ . In other words, $\# I$ is 0 or $p ,$ so the factorization is trivial.

$7 \mathrm { A }$ . Prove that for every $a \in \mathbb { C }$ and integer $n \geq 2$ , the equation $1 + z + a z ^ { n } = 0$ has at least one root in the disk $| z | \le 2$

Solution: 1) If $a = 0$ , the problem is trivial.

2) Let $a \neq 0 , b = { \frac { 1 } { a } }$ . Consider

$$
b + b z + z ^ { n } = 0 .\tag{1}
$$

Let $z _ { 1 } , \ldots , z _ { n }$ be the roots of (1).

a) If $| b | \leq 2 ^ { n }$ then there is $z _ { i }$ such that $| z _ { i } | \le 2$ , since otherwise we would have $| b | =$ $| z _ { 1 } \ldots z _ { n } | > 2 ^ { n }$

b) Let $| b | > 2 ^ { n }$ and let $f ( z ) = b ( 1 + z ) + z ^ { n } , g ( z ) = b ( 1 + z )$ . Then $| f ( z ) - g ( z ) | =$ $| z ^ { n } | = 2 ^ { n } < | b | = | b | ( | z | - 1 ) \leq | b ( 1 + z ) | = | g ( z ) | { \mathrm { ~ i f ~ } } | z | = 2$ . By Rouch´e’s Theorem, the function $f$ has as many roots inside the circle $| z | = 2$ as does the function $g ( z )$ But $g ( z )$ has one, namely $z = - 1$ . Hence $f$ also has one inside $| z | = 2$

8A. Let Z denote the ring of integers and consider the linear map $\mathbf { Z } ^ { 3 } \to \mathbf { Z } ^ { 3 }$ defined by the   
3 × 3-matrix

$$
A = { \left( \begin{array} { l l l } { 6 } & { 9 } & { 1 2 } \\ { 6 } & { 9 } & { 1 2 } \\ { 1 2 } & { 1 8 } & { 2 4 } \end{array} \right) }
$$

Compute the structure of the three abelian groups kernel(A), image(A), and cokernel $( A ) =$ $\mathbf { Z } ^ { 3 } / \mathrm { i m a g e } ( A )$ . In particular, in each case determine whether the group is free abelian. If yes, give a basis.

Solution: We perform elementary row and column operations to diagonalize the matrix A:

$$
\begin{array} { r l r } { \left( \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } \\ { - 2 } & { 0 } & { 1 } \end{array} \right) \cdot A \cdot \left( \begin{array} { c c c } { - 1 } & { - 3 } & { - 2 } \\ { 1 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) } & { { } = } & { \left( \begin{array} { c c c } { 3 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right) . } \end{array}
$$

Both transformation matrices have determinant one, so they are invertible over the integers. Hence image, kernel and cokernel can be computed from the transformed matrix. We find

$$
\operatorname { i m a g e } ( A ) \simeq \mathbf { Z } ^ { 1 } , \quad \operatorname { k e r n e l } ( A ) \simeq \mathbf { Z } ^ { 2 } , \quad \operatorname { c o k e r } ( A ) \simeq \mathbf { Z } ^ { 2 } \oplus \mathbf { Z } / 2 \mathbf { Z } .
$$

We see that the column vector $( 3 , 3 , 6 ) ^ { T }$ is a basis for image(A). The last two columns of the right transformation matrix give the basis $\big \{ ( - 3 , 2 , 0 ) ^ { T } , ( - 2 , 0 , 1 ) ^ { T } \big \}$ for kernel(A).

9A. Let k be a field such that the additive group of k is finitely generated. Prove that k is finite.

Solution: First suppose that k has characteristic 0. A subgroup of a finitely generated abelian group is also finitely generated, so if the additive group of k is finitely generated, then so is the additive group of Q. But the additive group generated by a finite list of rational numbers $a _ { 1 } / b _ { 1 } , . . . , a _ { n } / b _ { n }$ is contained in the integer multiples of $1 / ( b _ { 1 } \cdots b _ { n } )$ , so if $p$ is a prime larger than $| b _ { 1 } \cdots b _ { n } | ,$ , then $1 / p$ is not in this group. This contradiction shows that k cannot have characteristic 0.

Let p be the characteristic of k. Then k is a vector space over the field $\mathbb { F } _ { p }$ of $p$ elements. Now, to say that k is finitely generated as an additive group is the same as saying that it is finite-dimensional as an $\mathbb { F } _ { p } \mathrm { - v e c t o r }$ space. If $d = \dim _ { \mathbb { F } _ { p } } k$ , then $\# k = p ^ { d }$ , so k is finite.

1B. Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Assume that $| f ( z ^ { 2 } ) | \leq 2 | f ( z ) |$ for all $z \in \mathbb { C }$ . Show that f is constant.

Solution: By induction on n we have that $| f ( z ^ { 2 ^ { n } } ) | \leq 2 ^ { n } | f ( z ) |$

(proof: n = 0 says $| f ( z ^ { 1 } ) | \leq 1 | f ( z ) |$ ; if this is true for n then:

$$
| f ( z ^ { 2 ^ { n + 1 } } ) | = | f ( ( z ^ { 2 ^ { n } } ) ^ { 2 } ) | \leq 2 | f ( z ^ { 2 ^ { n } } ) | \leq 2 ( 2 ^ { n } ) | f ( z ) | ) .
$$

Let M = max $\{ | f ( z ) | : | z | = 2 \}$ . Let $R _ { n } = 2 ^ { 2 ^ { n } } . { \mathrm { ~ I f ~ } } | w | = R _ { n }$ then $w = z ^ { 2 ^ { n } }$ for some z of length 2, and so $| f ( w ) | \leq 2 ^ { n } | f ( z ) | \leq 2 ^ { n } M$

For each integer m $\geq 1$ , by Cauchy’s inequalities for the circle about 0 of radius $R _ { n } .$ $| f ^ { ( m ) } ( 0 ) | \le ( 2 ^ { n } \bar { M } ) / ( R _ { n } ) ^ { m } \le \bar { M } ( 2 ^ { n - 2 ^ { n } } )$ . But as $n \to \infty$ , this converges to 0. So $f ^ { ( m ) } ( 0 ) = 0$ for all $m \geq 1$ , and the power series of f is constant.

2B. Let $C ^ { 0 } [ 0 , 1 ]$ be the vector space over R consisting of continuous functions from [0, 1] to R. Show that the functions $1 , x , x ^ { 2 } , \ldots$ . are linearly independent in $C ^ { 0 } [ 0 , 1 ]$

Solution: Suppose that a finite linear combination $p ( x ) = c _ { 0 } + c _ { 1 } x + c _ { 2 } x ^ { 2 } + \cdot \cdot \cdot + c _ { n } x ^ { n }$ is equal to zero in $C ^ { 0 } [ 0 , 1 ]$ , where $c _ { 0 } , \ldots , c _ { n } \in \mathbb { R }$ This means that $p ( x ) = 0$ for all $x \in \left[ 0 , 1 \right]$ We need to show that $c _ { 0 } = \cdots = c _ { n } = 0$ . Pick any $n + 1$ distinct points $a _ { 1 } , \dotsc , a _ { n + 1 } \in [ 0 , 1 ]$ Since $p ( a _ { 1 } ) = 0$ , we have $p ( x ) = ( x - a _ { 1 } ) q ( x )$ where q is a polynomial of degree $n - 1$ . Since $p ( a _ { 2 } ) = 0$ and $a _ { 2 } - a _ { 1 } \neq 0$ , we have $q ( a _ { 2 } ) = 0$ , so the polynomial q is divisible by $x - a _ { 2 }$ Continuing, we find that the polynomial $p$ is divisible by $( x - a _ { 1 } ) \cdot \cdot \cdot ( x - a _ { n + 1 } )$ , and since the latter polynomial has degree $n + 1$ , this is possible only if $p = 0$

3B. Let $f \colon  { \mathbb { R } } \times [ 0 , 1 ] \to  { \mathbb { R } }$ be a continuous function. For $x \in \mathbb { R }$ , define

$$
g ( x ) : = \operatorname* { m a x } \{ f ( x , y ) : y \in [ 0 , 1 ] \} .
$$

Show that g is continuous.

Solution: Given $a \in \mathbb { R }$ , let $A = [ a - 1 , a + 1 ] . \ K = A { \times } [ 0 , 1 ]$ is compact, so f restricted to K is uniformly continuous. Given $\epsilon > 0$ , let $\delta > 0$ be such that for all $x , z \in A , | x - z | < \delta$ implies for all $y \in [ 0 , 1 ] , | f ( x , y ) - f ( z , y ) | < \epsilon$

So for $x , z \in A , { \mathrm { i f ~ } } | x - z | < \delta$ , then $g ( x ) < g ( z ) + \epsilon$

(proof: Let y be such that $f ( x , y ) = g ( x ) ; \mathrm { ~ s o ~ } | f ( x , y ) - f ( z , y ) | < \epsilon .$ and $g ( x ) = f ( x , y ) <$ $f ( z , y ) + \epsilon \le g ( z ) + \epsilon )$

By symmetry, for $x , z \in A$ A, if | $| x - z | < \delta$ then $| g ( x ) - g ( z ) | < \epsilon .$ . So g is continuous at a.

4B. Let $f ( x ) \in \mathbb { Q } [ x ]$ be an irreducible polynomial. Suppose there is a field extension F of Q containing a root a of $f ( x )$ such that $F$ does not contain any cube root of a. Show that $f ( x ^ { 3 } )$ is irreducible over $\mathbb { Q } .$

$$
n = \deg f
$$

$$
f ( x ^ { 3 } )
$$

$$
\mathbb { Q } .
$$

$$
b ^ { 3 }
$$

$$
f ( x )
$$

$$
f ( x )
$$

$$
b ^ { 3 }
$$

$$
\mathbb { Q } ( a )
$$

$$
\mathbb { Q } ( b ^ { 3 } )
$$

$$
\mathbb { Q } ( b ^ { 3 } )
$$

$$
[ \mathbb { Q } ( b ) : \mathbb { Q } ( b ^ { 3 } ) ] = 3
$$

$$
f ( x )
$$

$$
x ^ { 3 } - b ^ { 3 }
$$

$$
x ^ { 3 } - b ^ { 3 }
$$

$$
\mathbb { Q } ( b ^ { 3 } )
$$

$$
\mathbb { Q } , [ \mathbb { Q } ( b ^ { 3 } ) : \mathbb { Q } ] = n .
$$

So $[ \mathbb { Q } ( \boldsymbol { b } ) : \mathbb { Q } ] = [ \mathbb { Q } ( \boldsymbol { b } ) : \mathbb { Q } ( \boldsymbol { b } ^ { 3 } ) ] [ \mathbb { Q } ( \boldsymbol { b } ^ { 3 } ) : \mathbb { Q } ] = 3 n =$ the degree of $f ( x ^ { 3 } )$ . Thus $f ( x ^ { 3 } )$ is the irreducible polynomial of b over Q.

5B. Let f and g be entire functions such that

$$
\int _ { | z | = 1 } { \frac { f ( z ) } { ( \sin z ) ^ { m } } } d z = \int _ { | z | = 1 } { \frac { g ( z ) } { ( \sin z ) ^ { m } } } d z
$$

for all positive integers m. Prove that $f = g .$

Solution: Suppose $f \neq g$ . Let $h ( z ) = f ( z ) - g ( z )$ , so

$$
\int _ { | z | = 1 } { \frac { h ( z ) } { ( \sin z ) ^ { m } } } d z = 0 .
$$

Since h is not identically zero, we may take $m = 1 + \mathrm { o r d } _ { z = 0 } h ( z )$ . Then $h ( z ) / ( \sin z ) ^ { m }$ has a simple pole at $z = 0$ and is holomorphic elsewhere in $| z | \leq 1$ , so the residue theorem gives

$$
\int _ { | z | = 1 } { \frac { h ( z ) } { ( \sin z ) ^ { m } } } d z \neq 0 ,
$$

a contradiction.

6B. Let G be a nonabelian group of order 21. Find the largest positive integer n with the property that whenever G acts on a set S of size n, some element of S is fixed by every element of G.

Solution: Finite G-sets are finite unions of transitive G-sets, and each transitive G-set is of the form $G / H$ for some subgroup H (namely, H is the stabilizer of a point in the G-set). Hence an integer n does not have the property if and only if there is a sequence of proper subgroups of $G$ whose indices sum to n. The possibilities for the index of a proper subgroup of G are 3, 7, and 21 (consider Sylow subgroups, and the trivial group). Thus we seek the largest n that is not a sum of integers each of which equals 3, 7, or 21. The set of such sums consists of numbers of the form 3k, numbers of the form $3 k + 1$ that are at least 7, and numbers of the form $3 k + 2$ that are at least 14, so the largest n that is not such a sum is 11.

7B. Let X and Y be metric spaces, and let $f _ { 1 } , f _ { 2 } , \ldots$ . be continuous functions from X to $Y$ . Suppose that the sequence $\left\{ f _ { n } \right\}$ converges uniformly to a function $f .$ Show that f is continuous.

Solution: Let $\epsilon > 0$ and $x \in X$ be given; we must find $\delta > 0$ such that $d ( x , x ^ { \prime } ) < \delta$ implies $d ( f ( x ) , f ( x ^ { \prime } ) ) < \epsilon .$ Since the sequence $\left\{ f _ { n } \right\}$ converges uniformly to $f ,$ , there exists n such that for all $x \in X$ we have $d ( f _ { n } ( x ) , f ( x ) ) < \epsilon / 3$ . Since $f _ { n }$ is continuous, there exists $\delta > 0$ such that $d ( x , x ^ { \prime } ) < \delta$ implies $d ( f _ { n } ( x ) , f _ { n } ( x ^ { \prime } ) ) < \epsilon / 3$ . In particular, $d ( x , x ^ { \prime } ) < \delta$ implies that

$$
\begin{array} { l } { { d ( f ( x ) , f ( x ^ { \prime } ) ) \leq d ( f ( x ) , f _ { n } ( x ) ) + d ( f _ { n } ( x ) , f _ { n } ( x ^ { \prime } ) ) + d ( f _ { n } ( x ^ { \prime } ) , f ( x ^ { \prime } ) ) } } \\ { { \displaystyle \qquad < \frac { \epsilon } { 3 } + \frac { \epsilon } { 3 } + \frac { \epsilon } { 3 } = \epsilon . } } \end{array}
$$

8B. Let A be an $n \times n$ Hermitian matrix and B an $n \times n$ positive definite (complex) matrix. Prove that there is an invertible complex $n \times n$ matrix S such that $S ^ { H } A S$ is diagonal and $S ^ { H } B S = I$ . (Here $S ^ { H }$ denotes the conjugate transpose of the matrix S.)

Solution: Since B is positive definite there is a unitary V such that √ $B = V D V ^ { H }$ where D is√ diagonal with positive diagonal. Let $Q = V ( \sqrt { D } ) ^ { - 1 }$ . Then $Q ^ { H } B Q = ( { \sqrt { D } } ) ^ { - 1 } V ^ { H } B V ( { \sqrt { D } } ) ^ { - 1 } =$ I. Then $Q ^ { H } A Q$ is Hermitian hence there is a unitary U such that $\dot { U } ^ { H } ( \dot { Q } ^ { H } A Q ) U = \dot { \Lambda }$ is diagonal. Set $S = Q U$ . We have $S ^ { H } B S = U ^ { H } Q ^ { H } B Q \bar { U } = I$ and $S ^ { H } A S = U ^ { H } Q ^ { H } A Q U = \Lambda$ •

9B. Let $z _ { 0 } , z _ { 1 } , \ldots$ . be a sequence of complex numbers such that $z _ { n + 1 } = 1 + 1 / z _ { n }$ for all $n \geq 0$ Prove that the sequence is convergent.

Solution: Let $\textstyle f \left( z \right) = { \frac { z + 1 } { z } }$ . Then the equation $f \left( z \right) = z$ has two solutions

$$
\alpha = { \frac { 1 + { \sqrt { 5 } } } { 2 } } , \beta = { \frac { 1 - { \sqrt { 5 } } } { 2 } } .
$$

Let

$$
w = \frac { z - \alpha } { z - \beta } , z = \frac { \beta w - \alpha } { w - 1 } .
$$

Then

$$
{ \frac { f \left( z \right) - \alpha } { f \left( z \right) - \beta } } = { \frac { z + 1 - \alpha z } { z + 1 - \beta z } } .
$$

Use $\alpha + \beta = 1$ and $\alpha \beta = - 1$

$$
{ \frac { z + 1 - \alpha z } { z + 1 - \beta z } } = { \frac { \beta z + 1 } { \alpha z + 1 } } = { \frac { \beta } { \alpha } } { \frac { z - \alpha } { z - \beta } } = { \frac { \beta } { \alpha } } w .
$$

Therefore if $z _ { n + 1 } = f \left( z _ { n } \right)$ , then $w _ { n + 1 } = \gamma w _ { n } .$ , where $\begin{array} { r } { \gamma = \frac { \beta } { \alpha } } \end{array}$ . Since $| \gamma | < 1$

$$
\operatorname* { l i m } _ { n \to \infty } w _ { n } = 0 ,
$$

that implies

$$
\operatorname* { l i m } _ { n \to \infty } z _ { n } = \alpha
$$

for any $z _ { 0 }$ , except $z _ { 0 } = \beta$ . If $z _ { 0 } = \beta$ , obviously the limit is $\beta .$