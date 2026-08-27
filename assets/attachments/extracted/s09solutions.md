Problem 1A. Suppose that f is a continuous real function on [0, 1]. Prove that

$$
\operatorname* { l i m } _ { \alpha \to 0 ^ { + } } \alpha \int _ { 0 } ^ { 1 } x ^ { \alpha - 1 } f ( x ) d x = f ( 0 ) .
$$

Solution: This is obvious for f a constant, so by subtracting f (0) from both sides we can assume $f ( 0 ) = 0$ Choose any $\epsilon > 0$ and choose $\delta$ so that $| f ( x ) | < \epsilon$ whenever $x \leq \delta$ and choose M so that $f ( x ) < M$ for all x. Then

$$
\alpha \int _ { 0 } ^ { \delta } x ^ { \alpha - 1 } f ( x ) d x \leq \alpha \int _ { 0 } ^ { 1 } x ^ { \alpha - 1 } \epsilon d x = \epsilon ,
$$

while

$$
\alpha \int _ { \delta } ^ { 1 } x ^ { \alpha - 1 } f ( x ) d x \leq \alpha \int _ { \delta } ^ { 1 } x ^ { \alpha - 1 } M d x = M ( 1 - \delta ^ { \alpha } )
$$

which tends to 0 as α tends to 0. So for any $\epsilon > 0$ the limit is less than " in absolute value, so the limit is 0.

(Assuming that f is differentiable allows an easier solution by integrating by parts.) Problem 2A. Prove that if an $n \times n$ matrix X over R satisfies $X ^ { 2 } = - I$ , then n is even.

Solution: Method 1: Since $X ^ { 2 } + 1 = ( X + i ) ( X - i ) = 0$ , the Jordan form A of X over C is diagonal with eigenvalues ±i. Since X is real, the eigenvalues come in conjugate pairs, hence n is even.

Method 2: The identity $X ^ { 2 } = - I$ implies that $a + b i \mapsto a I + b X$ is a ring homomorphism from C to $M _ { n } ( \mathbb { R } ) = \operatorname { E n d } ( \mathbb { R } ^ { n } )$ . Using this to define complex scalar multiplication, $\mathbb { R } ^ { n }$ becomes a vector space over C such that restriction of scalars to $\mathbb { R }$ recovers its orginal real vector space structure. Since a complex vector space has even real dimension, n is even.

Method 3: det $X ^ { 2 } = ( \operatorname * { d e t } X ) ^ { 2 } = \operatorname * { d e t } ( - I ) = ( - 1 ) ^ { n }$ . Therefore n is even. Problem 3A. Show that if $f : \mathbb { C } \to \hat { \mathbb { C } }$ is a meromorphic function in the plane, such that there exists $R , C > 0$ so that for $| z | > R , | f ( z ) | \leq C | z | ^ { n }$ , then f is a rational function.

Solution: Since f is meromorphic, and $| f ( z ) | < \infty$ for $| z | > R$ , f must have only finitely many poles $a _ { 1 } , \ldots , a _ { m }$ (with multiplicity) in the disk $| z | \le R$ . Let $g ( z ) = ( z - a _ { 1 } ) \cdot \cdot \cdot ( z -$ $a _ { m } ) f ( z )$ , then $g ( z )$ is entire, and $| g ( z ) | \leq C ^ { \prime } | z | ^ { m + n }$ for $| z |$ large enough, and therefore $g ( z )$ is a polynomial of degree a most $m + n$ , using Cauchy’s estimate $| f ^ { N } ( 0 ) | \le C ^ { \prime } r ^ { m + n } N ! r ^ { - N } \to 0$ as $r \to \infty { \mathrm { i f } } N > m + n$ . Thus, $f ( z ) = g ( z ) / ( ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { n } ) )$ must be a rational function. Problem 4A. Let G be a finite group, and for each positive integer n, let

$$
X _ { n } = \{ ( g _ { 1 } , . . . , g _ { n } ) : g _ { i } g _ { j } = g _ { j } g _ { i } \forall i , j \} .
$$

Show that the formula

$$
h \cdot ( g _ { 1 } , \ldots , g _ { n } ) = ( h g _ { 1 } h ^ { - 1 } , \ldots , h g _ { n } h ^ { - 1 } ) ,
$$

defines an action of $G$ on $X _ { n }$ , and that $| X _ { n + 1 } | = | G | \cdot | X _ { n } / G |$ for all n, where $X _ { n } / G$ denotes the set of G-orbits in $X _ { n }$

## Solution:

The given formula defines the action of G on $G ^ { n }$ by coordinatewise conjugation, so one only has to verify that if $( g _ { 1 } , \ldots , g _ { n } ) \in X _ { n }$ , then $h \cdot ( g _ { 1 } , \ldots , g _ { n } ) \in X _ { n }$ . Since $g _ { i }$ commutes with $g _ { j }$ implies $h g _ { i } h ^ { - 1 }$ commutes with $h g _ { h } h ^ { - 1 }$ , this is clear.

For the counting asserstion, we have $\begin{array} { r } { | X _ { n } / G | = \frac { 1 } { | G | } \sum _ { h \in G } f _ { n } ( h ) } \end{array}$ , by Burnside’s Lemma, where $f _ { n } ( h )$ is the number of elements of $X _ { n }$ fixed by h. Now $( g _ { 1 } , \ldots , g _ { n } )$ is fixed by h if and only if h commutes with each $g _ { i }$ , that is, if and only if $( g _ { 1 } , \ldots , g _ { n } , h )$ belongs to $X _ { n + 1 }$ Thus $\begin{array} { r } { | X _ { n + 1 } | = \sum _ { h \in G } f _ { n } ( h ) = | G | \cdot | X _ { n } / G | } \end{array}$ .

∈ Problem 5A. There is a “folk theorem” that a four-footed table can always be rotated into a stable position on an uneven floor. Prove the following mathematical formulation of this theorem.

Define four points in $\mathbb { R } ^ { 2 }$ , depending on an angle θ, by $P _ { 1 } ( \theta ) = ( \cos \theta , \sin \theta ) , P _ { 2 } ( \theta ) =$ (− sin θ, cos θ), $P _ { 3 } ( \theta ) \ = \ ( - \cos \theta , - \sin \theta ) , \ P _ { 4 } ( \theta ) \ = \ ( \sin \theta , - \cos \theta )$ Show that given any continuous function $h \colon  { \mathbb { R } } ^ { 2 } \to  { \mathbb { R } }$ , there exists a value of θ such that the four points $Q _ { i } ( \theta ) =$ $( P _ { i } ( \theta ) , h ( P _ { i } ( \theta ) ) )$ on the graph of h are co-planar in $\mathbb { R } ^ { 3 }$

Solution: Let $\tilde { h } ( \theta ) = h ( \cos \theta , \sin \theta )$ and $g ( \theta ) = \tilde { h } ( \theta ) - \tilde { h } ( \theta + \pi / 2 ) + \tilde { h } ( \theta + \pi ) - \tilde { h } ( \theta + 3 \pi / 2 )$ Then g is continuous and satisfies $g ( \theta + \pi / 2 ) = - g ( \theta )$ . In particular, for any real number x that is a value of g, we see that $- x$ is also a value of $^ { g , }$ hence by the Intermediate Value Theorem, there exists θ such that $g ( \theta ) = 0$ . For this θ we have $( \tilde { h } ( \theta ) + \tilde { h } ( \theta + \pi ) ) / 2 =$ $( \tilde { h } ( \theta + \pi / 2 ) + \tilde { h } ( \theta + 3 \pi / 2 ) ) / 2$ . Call the quantity on both sides of this equality z. Then the point $( 0 , 0 , z ) \in \mathbb { R } ^ { 3 }$ lies on both the lines $Q _ { 1 } ( \theta ) Q _ { 3 } ( \theta )$ and $Q _ { 2 } ( \theta ) Q _ { 4 } ( \theta )$ , showing that the four points $Q _ { i } ( \theta )$ are co-planar.

Problem 6A. Let $M _ { 2 } ( \mathbb { C } )$ be the set of $2 \times 2$ matrices over the complex numbers. Given $A \in M _ { 2 } ( \mathbb { C } )$ , define $C ( A ) = \{ B \in M _ { 2 } ( \mathbb { C } ) : A B = B A \}$

(a) Prove that $C ( A )$ is a linear subspace of $M _ { 2 } ( \mathbb { C } )$ , for every A.

(b) Determine, with proof, all possible values of the dimension dim $C ( A )$

(c) Formulate a simple and explicit rule to find dim $C ( A )$ , given A. “Simple” means the rule should yield the answer with hardly any computational effort.

Solution:

(a) Either check directly that $C ( A )$ is closed under matrix addition and scalar multiplication, or just note that for fixed A, the matrix equation $A B = B A$ is a system of linear equations in the entries of B.

(b) If $A ^ { \prime } = S A S ^ { - 1 }$ is similar to A, then it is easy to verify that $B \mapsto S B S ^ { - 1 }$ is a linear isomorphism of $C ( A )$ on $C ( A ^ { \prime } )$ . Hence we may assume w.o.l.o.g. that A is in Jordan canonical form. This leads to three cases:

Case I.

$$
A = { \bigg [ } a 0 { \bigg ] } , \quad { \mathrm { w h e r e ~ } } a \neq b .
$$

Then $C ( A )$ consists of the diagonal matrices, dim $C ( A ) = 2$

Case II.

$$
A = \left[ \begin{array} { l l } { a } & { 1 } \\ { 0 } & { a } \end{array} \right] .
$$

Then $C ( A )$ is the set of matrices B of the form

$$
B = \left[ \begin{array} { l l } { a } & { b } \\ { 0 } & { a } \end{array} \right] ,
$$

so again dim $C ( A ) = 2$

Case III. A is a scalar multiple of I. Then $C ( A ) = M _ { 2 } ( \mathbb { C } )$ , dim $C ( A ) = 4$

(c) The result of part (b) can be reformulated as follows: if A is a scalar multiple of I, then dim $C ( A ) = 4$ , otherwise dim $C ( A ) = 2$

Problem 7A. Compute

$$
\int _ { 0 } ^ { \pi } { \frac { d \theta } { a + \cos \theta } }
$$

for $a > 1$ using the method of residues.

Solution: Using $z = e ^ { i \theta } , d z = i e ^ { i \theta } d \theta$ , cos $\theta = ( z + 1 / z ) / 2$ , we may rewrite the integral as a line integral

$$
- 2 i \int _ { | z | = 1 } \frac { d z } { z ^ { 2 } + 2 a z + 1 } .
$$

Factor the denominator as $( z - \alpha ) ( z - \beta )$ , where $\alpha = - a + \sqrt { a ^ { 2 } - 1 } , \beta = - a - \sqrt { a ^ { 2 } - 1 }$ and $| \alpha | < 1 , | \beta | > 1$ . Then

$$
R e s _ { z = a } { \frac { 1 } { z ^ { 2 } + 2 a z + 1 } } = { \frac { 1 } { \alpha - \beta } } ,
$$

and we see that the integral is equal to $- 2 i \cdot 2 \pi i \cdot { \frac { 1 } { \alpha - \beta } } = 2 \pi / \sqrt { a ^ { 2 } - 1 }$

Problem 8A. Let $\mathbb { Q } ( x )$ be the field of rational functions of one variable over $\mathbb { Q } .$ Let $i \colon \mathbb { Q } ( x )  \mathbb { Q } ( x )$ be the unique field automorphism such that $i ( x ) = x ^ { - 1 }$ . Prove that the subfield of elements fixed by i is equal to $\mathbb { Q } ( x + x ^ { - 1 } )$ .

Solution: Let F denote the fixed subfield, and set $y = x + x ^ { - 1 } \in F$ . Clearly $\mathbb { Q } ( y ) \subseteq F \neq$ $\mathbb { Q } ( x )$ . The equation $x ^ { 2 } - y x + 1 = 0$ shows that $\mathbb { Q } ( x )$ is an algebraic extension of degree 2 over $\mathbb { Q } ( y )$ . Hence the only extension of $\mathbb { Q } ( y )$ properly contained in $\mathbb { Q } ( x )$ is $\mathbb { Q } ( y )$ itself, so $F = \mathbb { Q } ( y )$

Problem 9A. Let $d _ { k } : = \operatorname { L C M } \{ 1 , 2 , \dots , k \}$ (the least common multiple) and $\begin{array} { r } { I _ { m } = \int _ { 0 } ^ { 1 } x ^ { m } ( 1 - } \end{array}$ $x ) ^ { m } \mathrm { d } x$ . Show $d _ { 2 m + 1 } I _ { m }$ is an integer, and use this to show that $d _ { 2 m + 1 } \geq 2 ^ { 2 m }$

Solution:

$$
I _ { m } = \sum _ { n = 0 } ^ { 2 m } { \frac { a _ { n } } { n + 1 } }
$$

for some integers $a _ { n }$ so $d _ { 2 m + 1 } I _ { m } \in Z$ . Also if $f ( x ) = x ( 1 - x ) , f ( 0 ) = f ^ { \prime } ( 1 / 2 ) = f ( 1 ) = 0$ $f ( 1 / 2 ) = 1 / 4$ and $1 / 2$ is the only critical point of f on (0, 1) so $0 < I _ { m } \le ( 1 / 4 ) ^ { m }$ and so $d _ { m } I _ { m } \geq 1$ and the statement follows.

Problem 1B. Let $I \subseteq \mathbb { R }$ be an open interval, and let $f : I  \mathbb { R }$ have continuous k-th derivatives $f ^ { [ k ] }$ on I for $k \leq n - 1$ . Let $a \in I$ be a point such that $f ^ { [ k ] } ( a ) = 0$ for all $1 \leq k \leq n - 1 , f ^ { [ n ] } ( a )$ exists and $f ^ { [ n ] } ( a ) > 0$ . Prove that f has a local minimum at a if n is even, and has no local extremum at a if n is odd.

Solution: Since $f ^ { [ n - 1 ] } ( a ) = 0$ , the definition of derivative gives

$$
\operatorname* { l i m } _ { x \to a } { \frac { f ^ { [ n - 1 ] } ( x ) } { x - a } } = f ^ { [ n ] } ( a ) > 0 ,
$$

and hence there exists $\epsilon > 0$ such that $f ^ { [ n - 1 ] } ( x ) / ( x - a ) > 0$ for all $x \in ( a - \epsilon , a + \epsilon ) \setminus \{ a \}$ Taylor’s Theorem with remainder yields

$$
f ( x ) = f ( a ) + f ^ { [ n - 1 ] } ( c ) ( x - a ) ^ { n - 1 } / ( n - 1 ) !
$$

for some $c \in [ a , x ]$ if $x \geq a$ , or $c \in [ x , a ]$ if $x \leq a$ . For $x \in ( a - \epsilon , a )$ we have $f ^ { [ n - 1 ] } ( c ) \leq 0$ whence $f ( x ) \geq f ( a )$ if n is even, $f ( x ) \leq f ( a )$ if n is odd. Similarly, we find for $x \in ( a , a + \epsilon )$ that $f ( x ) \geq f ( a )$ for any n. For n even, this implies that f has a local minimum at a. For n odd, it implies that either f has no local extremum at a, or else f is constant on $( a - \epsilon , a + \epsilon )$ But the hypothesis $f ^ { [ n ] } ( a ) > 0$ rules out the latter possibility.

Problem 2B. Let A and B be $n \times n$ matrices over a field of characteristic zero. Prove that the condition $B A - A B = A$ implies that A is nilpotent. (Hint: what does A do to eigenvectors of B?)

Solution: Without loss of generality we can enlarge the field, say k, to be algebraically closed, since this does not change the hypothesis or the conclusion. Let v be an eigenvector of B, say $B v = \lambda v$ . Then $B A v = A ( B + I ) v = ( \lambda + 1 ) A v .$ in other words, if $A v \neq 0$ then Av is also an eigenvector of B with eigenvalue $\lambda + 1$ . Since B has finitely many eigenvalues, we must have $A ^ { k } v = 0$ for some k, so A is singular. Since $A B = B A - A$ we also see that B preserves the nullspace W of A. Then A and B induce linear transformations $A ^ { \prime } , B ^ { \prime }$ of $k ^ { n } / W$ which again satisfy $B ^ { \prime } A ^ { \prime } - A ^ { \prime } B ^ { \prime } = A ^ { \prime }$ . It follows by induction on n that A# is nilpotent, hence so is A.

Problem 3B. How many roots of the equation $z ^ { 4 } - 5 z ^ { 3 } + z - 2 = 0$ lie in the disk $| z | < 1 2$

Solution: By Rouche’s theorem, since $| z ^ { 4 } - 5 z ^ { 3 } + z - 2 - ( - 5 z ^ { 3 } ) | = | z ^ { 4 } + z - 2 | \leq 4 < 5 =$ $| - 5 z ^ { 3 } | \ \mathrm { f o r } \ | z | = 1$ , then $z ^ { 4 } - 5 z ^ { 3 } + z - 2$ has the same number of zeroes for $| z | < 1 \mathrm { a s } - 5 z ^ { 3 }$ which has three zeroes (counted with multiplicity).

Problem 4B. Consider a polynomial expression $H ( \alpha ) = A + B \alpha + C \alpha ^ { 2 } + \cdot \cdot \cdot + D \alpha ^ { N }$ with rational coefficients A, $B , C , \ldots , D$ , where α is an algebraic number, in other words a root of some polynomial with rational coefficients. Prove that if $H ( \alpha ) \neq 0$ , then the reciprocal $1 / H ( \alpha )$ can be expressed as a polynomial in α with rational coefficients.

Solution:Let $P ( x )$ be a polynomial of minimal degree such that $P ( \alpha ) = 0$ . Then P must be irreducible in $\mathbf { Q } [ x ]$ (since otherwise α would be a root of a polynomial of a smaller degree). By the Euclidean algorithm in $\mathbf Q [ x ]$ , there exist polynomials $F ( x )$ and $G ( x )$ with rational coefficients such that the greatest monic common divisor D of P and H is written as $D ( x ) = F ( x ) P ( x ) + G ( x ) H ( x )$ . Then D cannot be a scalar multiple of P (since otherwirse we would have $H ( \alpha ) = 0 )$ , and cannot be a proper divisor of P (since P is irreducible), and so $D = 1$ . Thus $1 / H ( \alpha ) = G ( \alpha )$

Problem 5B. Let $f : \mathbb { R } ^ { 3 }  \mathbb { I }$ R be a continuous function of compact support. Show that $\begin{array} { r } { u ( x ) = \int _ { \mathbb { R } ^ { 3 } } \frac { f ( y ) } { | x - y | } d y } \end{array}$ is well defined and that $\begin{array} { r } { \operatorname* { l i m } _ { | x |  \infty } u ( x ) | x | = \int _ { \mathbb { R } ^ { 3 } } f ( y ) d y } \end{array}$

Solution:Choose R so that $f ( y ) = 0 { \mathrm { ~ i f ~ } } | y | \geq R$ . Then for $a = R + | x |$ , and using polar coordinates,

$$
\int \left| \frac { f ( y ) } { \left| x - y \right| } \right| d y \leq ( \operatorname* { m a x } | f | ) 4 \pi \int _ { 0 } ^ { a } \frac { 1 } { r } r ^ { 2 } d r < \infty ,
$$

shows that the integral exists. On the other hand, for $| x | \geq L \geq R$ and y satisfying $f ( y ) \neq 0$ we have

$$
\left| { \frac { | x | } { | x - y | } } - 1 \right| \leq { \frac { R } { L - R } } ,
$$

which implies

$$
\left| u ( x ) | x | - \int f ( y ) d y \right| \leq { \frac { R } { L - R } } \int | f ( y ) | d y .
$$

The result follows by sending $L \to \infty$

Problem 6B. Let $\lambda _ { 1 } \geq \cdots \geq \lambda _ { n }$ be eigenvalues of a symmetric real $n \times n$ -matrix A. Prove that

$$
\lambda _ { k } = \operatorname* { m a x } _ { V ^ { k } } \operatorname* { m i n } _ { x \in \left( V ^ { k } - 0 \right) } \frac { \left( A x , x \right) } { \left( x , x \right) } ,
$$

where the maximum is taken over all k-dimensional linear subspaces $V ^ { k }$ , the minimum over all non-zero vectors in the subspace, and $( x , y )$ denotes the Euclidean dot-product. (Hint: any k-dimensional subspace intersects the space spanned by the eigenvectors of the $n + 1 - k$ smallest eigenvalues in a space of dimension at least 1.)

Solution: In the orthonormal basis of eigenvectors of A (provided by the orthogonal diagonalization theorem) we have:

$$
( A x , x ) = \lambda _ { 1 } x _ { 1 } ^ { 2 } + \cdot \cdot \cdot + \lambda _ { n } x _ { n } ^ { 2 } .
$$

Let W denotes the subspace of codimension $k - 1$ given by the equations $x _ { 1 } = \cdot \cdot \cdot = x _ { k - 1 } = 0$ On $W$ , we have:

$$
( A x , x ) = \lambda _ { k } x _ { k } ^ { 2 } + \cdot \cdot \cdot + \lambda _ { n } x _ { n } ^ { 2 } \leq \lambda _ { k } ( x _ { k } ^ { 2 } + \cdot \cdot \cdot + x _ { n } ^ { 2 } ) = \lambda _ { k } ( x , x ) ,
$$

i.e. the ratio $( A x , x ) / ( x , x ) \le \lambda _ { k }$ Since every k-dimensional subspace $V ^ { k }$ has a non-trivial intersection with W , we conclude that min $( A x , x ) / ( x , x )$ on every $V ^ { k }$ does exceed $\lambda _ { k }$ . On the other hand, in the k-dimensional subspace $V _ { 0 } ^ { k }$ given by the equations $x _ { k + 1 } = \cdot \cdot \cdot = x _ { n } = 0$ we have:

$$
( A x , x ) = \lambda _ { 1 } x _ { 1 } ^ { 2 } + \cdot \cdot \cdot + \lambda _ { k } x _ { k } ^ { 2 } \geq \lambda _ { k } ( x _ { 1 } ^ { 2 } + \cdot \cdot \cdot + x _ { k } ^ { 2 } ) = \lambda _ { k } ( x , x ) ,
$$

the ratio $( A x , x ) / ( x , x ) \geq \lambda _ { k }$

Problem 7B. If is a univalent (1-1 analytic) function with domain the unit disc such that $\begin{array} { r } { f ( z ) = z + \sum _ { n = 2 } ^ { \infty } a _ { n } z ^ { n } } \end{array}$ , then prove that

$$
g ( z ) = { \sqrt { f ( z ^ { 2 } ) } }
$$

is an odd analytic univalent function on the unit disc.

Solution:The function $f ( z ^ { 2 } ) = z ^ { 2 } \phi ( z )$ , where $\phi ( 0 ) = 1$ Since f is univalent, $\phi ( z ) \neq 0$ for $z \neq 0$ . Then we may define a well-defined branch $h ( z ) = \sqrt { \phi ( z ) }$ , since $B _ { 1 } ( 0 )$ is simplyconnected. Since $f ( z ^ { 2 } )$ is even, and $z ^ { 2 }$ is even, we must have $\phi ( z )$ is even. Since $\phi ( z ) = \phi ( - z )$ for z near zero, we must have $\sqrt { \phi ( z ) } = \sqrt { \phi ( - z ) }$ for z near zero, and therefore everywhere. Thus $\sqrt { \phi ( z ) }$ is an even function too. Thus, $g ( z ) = 1 / \sqrt { f ( z ^ { 2 } ) } = 1 / z \sqrt { \phi ( z ) }$ is an odd function defined for $z \in B _ { 1 } ( 0 ) - \{ 0 \}$

Suppose that $g ( z _ { 1 } ) = g ( z _ { 2 } )$ . Then $f ( z _ { 1 } ^ { 2 } ) = f ( z _ { 2 } ^ { 2 } )$ , which means that $z _ { 1 } ^ { 2 } = z _ { 2 } ^ { 2 }$ , since $f$ is univalent. If $z _ { 1 } = - z _ { 2 }$ , then $g ( z _ { 1 } ) = - g ( z _ { 2 } )$ , which may hold only if $z _ { 1 } = z _ { 2 } = 0$ . Otherwise, $z _ { 1 } = z _ { 2 }$ , so in either case g is univalent.

Problem 8B.

1. Let G be a non-abelian finite group. Show that $G / Z ( G )$ is not cyclic, where $Z ( G )$ is the center of G.

2. If $| G | = p ^ { n }$ , with p prime and $n > 0$ , show that $Z ( G )$ is not trivial.

3. If $| G | = p ^ { 2 }$ , show that G is abelian.

## Solution:

1. If $g$ is an element of G whose image generates the cyclic group $G / Z$ , then G is generated by the commuting set g and $Z _ { i }$ so is abelian.

2. All conjugacy classes have order a power of p (as their order is the index of a centralizer of one of their elements) so the number of conjugacy classes with just one element is a multiple of $p .$ These conjugacy classes form the center, so the center has order a multiple of p so is non-trivial.

3. By part 2 the center has order at least $p ,$ so $G / Z$ has order at most p and is therefore cyclic. By part 1 the group must be abelian.

Problem 9B. Prove that the sequence of functions $f _ { n } ( x ) = \sin n x$ has no pointwise convergent subsequence. (Hint: show that given any subsequence and any interval of positive length there is a subinterval such that some element of the subsequence is at least $1 / 2$ on this subinterval, and another element is at most $- 1 / 2 . )$ )

Remark. This is an example from Ch. 7 of W. Rudin’s Principles of Mathematical Analysis, which is treated by the author using a result from the more advanced chapter on Lebesgue measure, namely the bounded convergence theorem. According to it, if a sequence of bounded continuous functions $g _ { k } \ ( = ( \sin n _ { k } x - \sin n _ { k + 1 } x ) ^ { 2 }$ in this example) tends to 0 pointwise, then $\textstyle \int g _ { k } ( t ) d t$ tend to 0 too. (In the example, the integral over the period $[ 0 , 2 \pi ]$ is equal to 2π regardless of k.) Below, an elementary proof is given; it is due to Evan O’Dorney (a high-school student taking Givental’s H104 class).

Solution: Given a subsequence sin $n _ { k } x$ , we find a subsequence sin $n _ { k _ { l } }$ in it and a point $x _ { 0 }$ where $\mathrm { l i m } _ { l  \infty }$ sin $n _ { k _ { l } } x _ { 0 }$ does not exist. Start with picking an interval $[ a _ { 1 } , b _ { 1 } ]$ where sin $n _ { 1 } x \ge$ $1 / 2$ . Passing to a term sin $n _ { k } x$ which oscillates sufficiently many times on the interval $[ a _ { 1 } , b _ { 1 } ]$ find in it an interval $[ a _ { 2 } , b _ { 2 } ]$ where sin $n _ { k } x \le - 1 / 2$ . Passing to a term sin $n _ { m } x$ which oscillates sufficiently many times on $[ a _ { 2 } , b _ { 2 } ]$ , find in it an interval $a _ { 3 } , b _ { 3 } ]$ where sin $n _ { m } x \ge 1 / 2$ , and so on. Call the selected functions sin $n _ { k _ { 1 } } x$ , sin $n _ { k _ { 2 } } x$ , sin $n _ { k _ { 3 } } x$ , etc., and let $x _ { 0 }$ be a common point of the nested sequence of intervals $[ a _ { 1 } , b _ { 1 } ] \supset [ a _ { 2 } , b _ { 2 } ] \supset . . .$ . Since sin $n _ { k _ { l } } x _ { 0 }$ is $\geq 1 / 2$ for odd l and $\leq - 1 / 2$ for even l, the limit at $x _ { 0 }$ does not exist.