1A. Let k be a field, and let $n \geq 1$ . Prove that the following properties of an $n \times n$ matrix A with entries in k are equivalent:

(a) A is a scalar multiple of the identity matrix.

(b) Every nonzero vector $v \in k ^ { n }$ is an eigenvector of A.

Solution: Obviously (a) implies (b). If (b) holds, then in particular, the standard basis vectors $e _ { j }$ are eigenvectors of A, so A is diagonal, say with entries $A _ { i i } = \lambda _ { i }$ . If $\lambda _ { i } \neq \lambda _ { j }$ , then $A ( e _ { i } + e _ { j } ) = \lambda _ { i } e _ { i } + \lambda _ { j } e _ { j }$ is not a scalar multiple of $e _ { i } + e _ { j }$ This contradicts the hypothesis that $e _ { i } + e _ { j }$ is an eigenvector of A. Hence the diagonal entries $\lambda _ { i }$ are all equal and we have (a).

2A. Define $f : \mathbb { R } ^ { 2 } \to \mathbb { R }$ by $f ( x , 0 ) = 0$ and

$$
f ( x , y ) = \left( 1 - \cos { \frac { x ^ { 2 } } { y } } \right) { \sqrt { x ^ { 2 } + y ^ { 2 } } }
$$

for $y \ne 0$

(a) Show that f is continuous at (0, 0).

(b) Calculate all the directional derivatives of f at (0, 0).

(c) Show that f is not differentiable at (0, 0).

Solution:

(a) We have $| f ( x , y ) | \leq 2 { \sqrt { x ^ { 2 } + y ^ { 2 } } }$ , and the latter tends to 0 as $( x , y ) \to ( 0 , 0 )$

(b) In the direction of $( x , y )$ with $y \ne 0$ , the directional derivative is

$$
\operatorname* { l i m } _ { t \to 0 } { \frac { f ( t x , t y ) } { t } } = \operatorname* { l i m } _ { t \to 0 } \left( 1 - \cos { \frac { t ^ { 2 } x ^ { 2 } } { t y } } \right) { \sqrt { x ^ { 2 } + y ^ { 2 } } } = 0 ,
$$

and the limit is trivially zero in the direction of $( x , 0 )$ for any x.

(c) If f were differentiable, the derivative would be zero, and then $f ( x , y ) / \sqrt { x ^ { 2 } + y ^ { 2 } } \to 0$ as $( x , y ) \to ( 0 , 0 )$ . This is false, since if we approach (0, 0) along the curve $x ^ { 2 } / y = \pi$ , the limit of $f ( x , y ) / \sqrt { x ^ { 2 } + y ^ { 2 } } \mathrm { ~ i s ~ } 1 - \cos \pi = 2$

3A. Let $M _ { 2 } ( \mathbb { Q } )$ denote the ring of $2 \times 2$ matrices with entries in $\mathbb { Q }$ . Let R be the set of matrices in $M _ { 2 } ( \mathbb { Q } )$ that commute with $\left( { \begin{array} { c c } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} } \right)$

(a) Prove that R is a subring of $M _ { 2 } ( \mathbb { Q } )$

(b) Prove that R is isomorphic to the ring $\mathbb { Q } [ x ] / ( x ^ { 2 } )$

Solution:

(a) Let $N = { \binom { 1 } { 0 } } \ 1 )$ . If $A , B \in R ,$ , then $( A + B ) N = A N + B N = N A + N B = N ( A + B )$ , so $A + B \in R$ . If ${ \dot { A } } , B \in R$ , then $( A B ) N = A ( B N ) = A ( N B ) = ( A N ) B = ( N A ) B = N ( A B )$ so $A B \in R$ . If I is the identity matrix, then clearly $- I \in R$ . These three facts imply that R is a subring.

(b) Calculating shows that the matrix $A = { \binom { a b } { c d } }$ belongs to R if and only if $a = a + c , $ $a + b = b + d ,$ , and $c + d = d ,$ that is, if and only if A has the form ${ \binom { a } { 0 } } \ b \ \qquad $ . We define a Q-algebra homomorphism $h : \mathbb { Q } [ x ] \to R$ by mapping x to $\left( { \begin{array} { c c } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} } \right)$ . Clearly $h ( x ^ { 2 } ) =$ ${ \left( \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right) } ^ { 2 } = 0$ , so h induces a homomorphism $\mathbb { Q } [ x ] / ( x ^ { 2 } ) \to R$ . Since $h ( a + b x ) = { \binom { a b } { 0 } }$ this homomorphism $\mathbb { Q } [ x ] / ( x ^ { 2 } ) \to R$ is an isomorphism.

4A. Prove that for each integer $n \geq 0$ there is a polynomial $T _ { n } ( x )$ with integer coefficients such that the identity

$$
2 \cos n z = T _ { n } ( 2 \cos z )
$$

holds for all z.

Solution: Put $q = e ^ { i z }$ , so $2 \cos z = q + q ^ { - 1 }$ , and 2 cos $n z = q ^ { n } + q ^ { - n }$ . Then the problem is to find $T _ { n }$ such that $T _ { n } ( q + q ^ { - 1 } ) = q ^ { n } + q ^ { - n }$ . We have

$$
( q + q ^ { - 1 } ) ^ { n } = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } q ^ { 2 k - n } = q ^ { n } + q ^ { - n } + \sum _ { \tiny { n < j < n \atop n - j \mathrm { ~ e v e n } } } { \binom { n } { ( n - j ) / 2 } } ( q ^ { j } + q ^ { - j } ) + \left\{ { \binom { n } { 0 / 2 } } \quad { \mathrm { i f ~ } } n { \mathrm { ~ i s ~ e v e n } } , \atop 0  \right\} .
$$

We can assume we have found $T _ { j }$ for $j < n$ by induction. Then

$$
T _ { n } ( x ) = x ^ { n } - \sum _ { \stackrel { 0 < j < n } { n - j \mathrm { ~ e v e n } } } { \binom { n } { ( n - j ) / 2 } } ( T _ { j } ( x ) ) - { \left\{ \begin{array} { l l } { { \binom { n } { n / 2 } } } & { { \mathrm { i f ~ } } n { \mathrm { ~ i s ~ e v e n , } } } \\ { { 0 } } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

has the required property.

5A. Let L be a real symmetric $n \times n$ matrix with 0 as a simple eigenvalue, and let $v \in \mathbb { R } ^ { n }$ (a) Show that for sufficiently small positive real , the equation $L x + \epsilon x = v$ has a unique solution $x = x ( \epsilon ) \in \mathbb { R } ^ { n }$

(b) Evaluate $\scriptstyle \operatorname* { l i m } _ { \epsilon \to 0 ^ { + } } \epsilon x ( \epsilon )$ in terms of v, the eigenvectors of L, and the inner product ( , ) on $\mathbb { R } ^ { n }$

Solution: Since L is real and symmetric, $\mathbb { R } ^ { n }$ has an orthonormal basis of eigenvectors $e _ { 1 } , \ldots , e _ { n }$ of L. Let $\lambda _ { 1 } , \ldots , \lambda _ { n }$ be the associated eigenvalues. Without loss of generality, $\lambda _ { 1 } = 0$ and $\lambda _ { i } \neq 0$ for $i > 1$ Write $\textstyle v = \sum _ { i = 1 } ^ { n } v _ { i } e _ { i }$ and $x = \sum x _ { i } e _ { i }$ with $v _ { i } , x _ { i } \in \mathbb { R }$ The equation $L x + \epsilon x = v$ is equivalent to $\lambda _ { i } x _ { i } + \epsilon x _ { i } = v _ { i }$ for each i, which has the unique solution $x _ { i } = v _ { i } / ( \lambda _ { i } + \epsilon )$ , provided that $\begin{array} { r } { 0 < \epsilon < \operatorname* { m i n } _ { i \neq 1 } | \lambda _ { i } | } \end{array}$ . Now

$$
\epsilon x = \sum \epsilon x _ { i } e _ { i } = \sum \frac { \epsilon } { \lambda _ { i } + \epsilon } v _ { i } e _ { i } .
$$

As $\epsilon  0 .$ , all terms in the sum on the right tend to 0 except the first, which tends to $\boldsymbol { v } _ { 1 } \boldsymbol { e } _ { 1 } = ( v , e _ { 1 } ) \boldsymbol { e } _ { 1 }$

6A. Let $x _ { n }$ be a sequence of real numbers so that lim $_ { 1 _ { n  \infty } } ( 2 x _ { n + 1 } - x _ { n } ) = x$ . Show that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } x _ { n } = x$

Solution: First show that $\{ x _ { n } \}$ is bounded. We know that the sequence $\{ 2 x _ { n + 1 } - x _ { n } \}$ is bounded. Then we can choose M large so that $| x _ { 1 } | \le M$ and $| 2 x _ { n + 1 } - x _ { n } | \leq M$ for all n. We prove by induction that $| x _ { n } | \leq M$ for all n. Indeed, suppose that $| x _ { n } | \leq M$ . Then

$$
| x _ { n + 1 } | = | \frac { x _ { n } + ( 2 x _ { n + 1 } - x _ { n } ) } { 2 } | \leq \frac { 1 } { 2 } ( | x _ { n } | + | 2 x _ { n + 1 } - x _ { n } | ) \leq M
$$

This concludes the induction and shows that $\{ x _ { n } \}$ is bounded.

Now write again

$$
x _ { n + 1 } = { \frac { x _ { n } + ( 2 x _ { n + 1 } - x _ { n } ) } { 2 } }
$$

and take lim sup. We get

$$
\operatorname* { l i m } \operatorname* { s u p } x _ { n } \leq { \frac { \operatorname* { l i m } \operatorname* { s u p } x _ { n } + x } { 2 } }
$$

which gives lim sup $x _ { n } \leq x$ . Similarly we get lim inf $x _ { n } \geq x$ . Together these two inequalities imply that lim $x _ { n } = x$

7A. (a) Suppose that $H _ { 1 }$ H and $H _ { 2 }$ are subgroups of a group G such that $H _ { 1 } \cup H _ { 2 }$ is a subgroup of G. Prove that either $H _ { 1 } \subseteq H _ { 2 }$ or $H _ { 2 } \subseteq H _ { 1 }$

(b) Show that for each integer $n \geq 3$ , there exists a group G with subgroups $H _ { 1 } , H _ { 2 } , \ldots ,$ $H _ { n } .$ such that no $H _ { i }$ is contained in any other, and such that $H _ { 1 } \cup H _ { 2 } \cup \ldots \cup H _ { n }$ is a subgroup of G.

Solution:

(a) If not, there exists $h _ { 1 } \in H _ { 1 } - H _ { 2 }$ and $h _ { 2 } \in H _ { 2 } - H _ { 1 }$ . Since $h _ { 1 }$ and $h _ { 2 }$ belong to the subgroup $H _ { 1 } \cup H _ { 2 }$ , we also have $h _ { 1 } h _ { 2 } \in H _ { 1 } \cup H _ { 2 }$ . If $h _ { 1 } h _ { 2 } \in H _ { 1 }$ , we get the contradiction $h _ { 2 } = h _ { 1 } ^ { - 1 } ( h _ { 1 } h _ { 2 } ) \in H _ { 1 } . \mathrm { ~ I f ~ } h _ { 1 } h _ { 2 } \in H _ { 2 } , \mathrm { ~ w e ~ g e t }$ the contradiction $h _ { 1 } = ( h _ { 1 } h _ { 2 } ) h _ { 2 } ^ { - 1 } \in H _ { 2 }$

(b) Let $G = ( \mathbb { Z } / 2 \mathbb { Z } ) ^ { n - 1 }$ . For $1 \leq i \leq n - 1$ , let $H _ { i } = \{ ( x _ { 1 } , \dots , x _ { n - 1 } ) \in G : x _ { i } = 0 \}$ . Then $H _ { 1 } \cup \ldots \cup H _ { n - 1 } = G - \{ ( 1 , 1 , \ldots , 1 ) \}$ . Let $H _ { n } = \left\{ \left( x _ { 1 } , \dots , x _ { n - 1 } \right) \in G : x _ { 1 } + x _ { 2 } = 0 \right\}$ . Then $( 1 , 1 , \ldots , 1 ) \in H _ { n } , \ s o \ H _ { 1 } \cup \cdots \cup H _ { n } = G$ . No $H _ { i }$ is contained in any other, since they are distinct subgroups of the same order.

## 8A. Evaluate $\textstyle \int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } \cos x ^ { 2 } d x$

Solution: It is the real part of

$$
I : = \int _ { 0 } ^ { \infty } e ^ { - ( 1 + i ) x ^ { 2 } } d x = \int _ { 0 } ^ { \infty } e ^ { - { \sqrt { 2 } } e ^ { i \pi / 4 } x ^ { 2 } } d x = \int _ { 0 } ^ { \infty } e ^ { - { \sqrt { 2 } } ( e ^ { i \pi / 8 } x ) ^ { 2 } } d x .
$$

Let C denote the wedge-shaped closed contour consisting of the straight path from 0 to $R > 0$ , the arc γ given by $e ^ { i t } R$ as t goes from 0 to $\pi / 8$ , and the straight path from $e ^ { i \pi / 8 } R$ to 0. By Cauchy’s Theorem, $\textstyle \int _ { C } e ^ { - { \sqrt { 2 } } z ^ { 2 } } d z = 0$ . But $\textstyle \int _ { \gamma } e ^ { - { \sqrt { 2 } } z ^ { 2 } } d z \to 0$ as $R \to \infty$ , since the integrand is bounded in absolute value by $\vert e ^ { - \sqrt { 2 } e ^ { i \pi / 4 } R ^ { 2 } } \vert = e ^ { - R ^ { 2 } }$ along $\gamma ,$ , while the length of $\gamma$ is $O ( R )$ . Thus $\textstyle \int _ { C } e ^ { - { \sqrt { 2 } } z ^ { 2 } } d z = 0$ implies

$$
0 = \int _ { 0 } ^ { \infty } e ^ { - \sqrt { 2 } z ^ { 2 } } d z - \int _ { 0 } ^ { \infty } e ^ { - \sqrt { 2 } ( e ^ { i \pi / 8 } x ) ^ { 2 } } d ( e ^ { i \pi / 8 } x )
$$

or equivalently,

$$
0 = 2 ^ { - 1 / 4 } \int _ { 0 } ^ { \infty } e ^ { - u ^ { 2 } } d u - e ^ { i \pi / 8 } I ,
$$

so $I = 2 ^ { - 1 / 4 } e ^ { - i \pi / 8 } \frac { \sqrt { \pi } } { 2 }$ . Thus the answer, which is the real part of I, is

$$
2 ^ { - 5 / 4 } ( \cos \pi / 8 ) { \sqrt { \pi } } .
$$

9A. Let R be the set of complex numbers of the form

$$
a + 3 b i , \quad a , b \in \mathbb { Z } .
$$

Prove that R is a subring of C, and that R is an integral domain but not a unique factorization domain.

Solution: It’s routine to verify that R is an additive subgroup and is closed under multiplication. Since C is a field, any subring is an integral domain. Consider two factorizations of the integer 10 in R, namely $1 0 = 2 \cdot 5$ and $1 0 = ( 1 + 3 i ) ( 1 - 3 i )$ . The norm $\vert z \vert ^ { 2 } = a ^ { 2 } + 9 b ^ { 2 }$ of any $z \in R$ is an integer, and if $| z | ^ { 2 } < 9$ then b = 0, so z is a real integer. This implies in particular that 2 has no non-trivial factorization in R. If R were a UFD, then 2 would divide 1 + 3i or $1 - 3 i$ . But that can’t be, since $( 1 \pm 3 i ) / 2$ are not in R.

1B. (a) Prove that there is no continuously differentiable, measure-preserving bijective function $f : \mathbb { R } \to \mathbb { R } _ { > 0 }$

(b) Find an example of a continuously differentiable, measure-preserving bijective function $f \colon \mathbb { R } \times \mathbb { R } \to \mathbb { R } \times \mathbb { R } _ { > 0 }$

Solution: For either (a) or (b), the measure-preserving condition is that the Jacobian determinant $J ( f )$ has absolute value 1 everywhere. By continuity, we must have $J ( f ) = 1$ or $J ( f ) = - 1$ identically. In (a), this would mean $f ^ { \prime } ( x ) = 1$ or $f ^ { \prime } ( x ) = - 1$ , so $f ( x ) = c + x$ or $f ( x ) = c - x$ . Thus f cannot map R into $\mathbb { R } _ { > 0 }$ . One possible example for (b) is $f ( x , y ) =$ $( e ^ { - y } x , e ^ { y } )$

2B. For an analytic function h on C, let $\it { h ^ { ( i ) } }$ denote its i-th derivative. $( \mathrm { I f } \ i \ ) = \ 0$ , then $\begin{array} { r } { h ^ { ( i ) } = h . ) } \end{array}$ Suppose that f and g are analytic functions on C satisfying

$$
f ^ { ( n ) } + a _ { n - 1 } f ^ { ( n - 1 ) } + \cdot \cdot \cdot + a _ { 0 } f ^ { ( 0 ) } = 0
$$

$$
g ^ { ( m ) } + b _ { m - 1 } g ^ { ( m - 1 ) } + \cdot \cdot \cdot + b _ { 0 } g = 0
$$

for some constants $a _ { 0 } , \dots , a _ { n - 1 } , b _ { 0 } , \dots , b _ { m - 1 } \in \mathbb { C }$ . Show that the product function $F = f g$ satisfies

$$
c _ { m n } F ^ { ( m n ) } + c _ { m n - 1 } F ^ { ( m n - 1 ) } + \cdot \cdot \cdot + c _ { 0 } F = 0
$$

for some constants $c _ { 0 } , \ldots , c _ { m n } \in \mathbb { C }$ not all zero.

Solution: By induction on k, the function $F ^ { ( k ) }$ is a linear combination of the mn functions $f ^ { ( i ) } g ^ { ( j ) }$ for $0 \leq i < n , 0 \leq j < m$ , with constant coefficients. Therefore the $m n + 1$ functions $F ^ { ( 0 ) } , \ldots , F ^ { ( m n ) }$ are linearly dependent over C.

3B. Let f be an entire function such that Re $f ( z ) \geq - 2$ for all $z \in \mathbb { C }$ . Show that f is constant.

Solution: The function $g ( z ) = e ^ { - f ( z ) }$ is entire, and $| g ( z ) | = e ^ { - \mathrm { R e } f ( z ) } \leq e ^ { 2 }$ . Liouville’s Theorem implies that g is constant, say $g ( z ) = c$ . Clearly $c \neq 0$ . Then f maps the connected set C into the discrete set of all logarithms of c, so $f$ is constant.

4B. Suppose $G$ is a nonabelian simple group, and A is its automorphism group. Show that A contains a normal subgroup isomorphic to G.

Solution: For $g$ in $G ,$ let $c _ { g } : G \to G$ be the inner automorphism $c _ { g } ( h ) = g h g ^ { - 1 }$ Then it is easy to check that $g \mapsto c _ { g }$ defines a homomorphism $G  A$ . It is nontrivial since $G$ is nonabelian, and thus an injection since G is simple. Let B be the image, so $B \simeq G$ . If $\alpha \in A$ and $g , h \in G$ , then

$$
\alpha ( c _ { g } ( h ) ) = \alpha ( g h g ^ { - 1 } ) = \alpha ( g ) \alpha ( h ) \alpha ( g ) ^ { - 1 } = c _ { \alpha ( g ) } ( \alpha ( h ) ) ,
$$

so α $\circ c _ { g } = c _ { \alpha ( g ) }$ ◦ α in A. Thus $\alpha \circ c _ { g } \circ \alpha ^ { - 1 } = c _ { \alpha ( g ) }$ , so $B$ is normal in $G .$

5B. Let C and D be nonempty closed subsets of $\mathbb { R } ^ { n }$ , and assume that $C$ is bounded. Prove that there exist points $x _ { 0 } \in C$ and $y _ { 0 } \in D$ such that $d ( x _ { 0 } , y _ { 0 } ) \leq d ( x , y )$ for all $x \in C , y \in D$ Here $d ( x , y )$ denotes the Euclidean metric on $\mathbb { R } ^ { n }$

Solution: It follows from the triangle inequality that $d ( x , y )$ is uniformly continuous as a real-valued function on $C \times D$ . If C and D were both bounded, then $C \times D$ would be compact and $d ( x , y )$ would attain its minimum. In the general case, let $d _ { 0 }$ be the infimum of $d ( x , y )$ on $C \times D$ . Let $\boldsymbol { B } _ { R _ { 0 } }$ be a closed ball of radius $R _ { 0 }$ around the origin containing $C _ { i }$ and set $R _ { 1 } = R _ { 0 } + d _ { 0 } + \epsilon .$ for some arbitrary $\epsilon > 0$ . Then for $y \notin B _ { R _ { 1 } }$ , we clearly have $d ( x , y ) > d _ { 0 } + \epsilon$ for all $x \in C$ It follows that $D \cap B _ { R _ { 1 } }$ is non-empty, and the infimum of $d ( x , y )$ on $C \times ( D \cap B _ { R _ { 1 } } )$ is equal to $d _ { 0 }$ . Since $C \times ( D \cap B _ { R _ { 1 } } )$ is compact, the minimum is attained for some $( x _ { 0 } , y _ { 0 } ) \in C \times ( D \cap B _ { R _ { 1 } } )$

6B. Let $\mathrm { G L _ { 2 } ( \mathbb { C } ) }$ denote the group of invertible $2 \times 2$ matrices with coefficients in the field of complex numbers. Let $\mathrm { P G L _ { 2 } ( C ) }$ denote the quotient of $\mathrm { G L _ { 2 } ( \mathbb { C } ) }$ by the normal subgroup $\left\{ { \binom { \lambda } { 0 } } { \binom { \bar { 0 } } { \lambda } } : \lambda \in \mathbb { C } ^ { * } \right\}$ . Let n be a positive integer, and suppose that $a , b$ are elements of $\mathrm { P G L _ { 2 } ( C ) }$ of order exactly n. Prove that there exists $c \in \mathrm { P G L } _ { 2 } ( \mathbb { C } )$ such that cac−1 is a power of $b .$

Solution: Choose $A \ \in \ \mathrm { G L } _ { 2 } ( \mathbb { C } )$ representing a. Then $A ^ { n } = \lambda I$ for some $\lambda \in \mathbb { C } ^ { * }$ . B y dividing A by an n-th root of λ, we may assume without loss of generality that $A ^ { n } = I$ . Since the polynomial $x ^ { n } - 1$ has distinct roots, A is diagonalizable, and the eigenvalues must be n-th roots of unity. Without loss of generality, we may conjugate, and divide A by the first root of unity, to assume that $A = { \binom { 1 } { 0 } } \zeta \zeta$ . If for some $m \geq 1 , A ^ { m } = s I$ for some $s \in \mathbb { C } ^ { * }$ then comparing upper left hand corners shows that $s = 1$ . Since the order of a is exactly n, the previous sentence implies that A has order exactly n, so that ζ is a primitive n-th root of unity.

Similarly, b is represented by a matrix that is conjugate to $B = \left( { \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { \zeta ^ { \prime } } \end{array} } \right)$ for some primitive n-th root of unity $\zeta ^ { \prime } .$ . Then $\zeta ^ { \prime }$ is a power of $\zeta ,$ so B is a power of A, and b is conjugate to a power of a.

7B. Let $f ( z )$ be a function that is analytic in the unit disk $D = \{ | z | < 1 \}$ . Suppose that $| f ( z ) | \leq 1$ in D. Prove that if $f ( z )$ has at least two fixed points $z _ { 1 }$ and $z _ { 2 }$ (that is, $f ( z _ { j } ) = z _ { j }$ for $j = 1 , 2 )$ , then $f ( z ) = z$ for all $z \in D$

Solution: Let S be a linear fractional transformation which maps D onto itself so that $S ( 0 ) = x _ { 1 }$ . Then $g = S ^ { - 1 } \circ f \circ S$ has the same properties as f and its two fixed points are $0 = S ^ { - 1 } ( z _ { 1 } )$ and $y = S ^ { - 1 } ( z _ { 2 } )$

Since $g ( 0 ) = 0$ we can define the analytic function $h ( z ) = g ( z ) / z$ . On the circle $| z | = 1 - \epsilon$ for fixed $\epsilon \in ( 0 , 1 )$ , we have $| h ( z ) | = | g ( z ) | / | z | \le 1 / ( 1 - \epsilon )$ , so the maximum principle implies $| h ( z ) | \leq 1 / ( 1 - \epsilon )$ for $| z | \le 1 - \epsilon$ . This holds for arbitrarily small $\epsilon > 0$ , so $| h ( z ) | \leq 1$ for all $z \in D$

On the other hand we know that $h ( y ) = 1$ , so h assumes a maximum inside D. By the maximum principle h must be constant; that is, $h = 1$ . This implies that $g ( z ) = z$ and then $f ( z ) = z$

8B. Let $N = 3 0 0 3 0$ , which is the product of the first six primes. How many nonnegative integers x less than N have the property that N divides $x ^ { 3 } - 1 2$

Solution: We want the number of solutions to $x ^ { 3 } = 1$ in the ring $\mathbb { Z } / N \mathbb { Z }$ . By the Chinese Remainder Theorem, $\mathbb { Z } / N \mathbb { Z }$ is isomorphic as a ring to $\begin{array} { r } { \prod _ { p \in \{ 2 , 3 , 5 , 7 , 1 1 , 1 3 \} } \mathbb { Z } / p \mathbb { Z } } \end{array}$ . Thus the answer is $\begin{array} { r } { \prod _ { p \in \{ 2 , 3 , 5 , 7 , 1 1 , 1 3 \} } n _ { p } } \end{array}$ , where $n _ { p }$ is the number of solutions to $x ^ { 3 } - 1$ in $\mathbb { Z } / p \mathbb { Z }$ . Now $n _ { p }$ is the number of elements of order dividing 3 in the multiplicative group $( \mathbb { Z } / p \mathbb { Z } ) ^ { \ast }$ . Since $( \mathbb { Z } / p \mathbb { Z } ) ^ { \ast }$ is cyclic of order $p - 1$ , we have $n _ { p } = 3$ if 3 divides $p - 1$ , and $n _ { p } = 1$ otherwise. Thus the answer is

$$
n _ { 2 } n _ { 3 } n _ { 5 } n _ { 7 } n _ { 1 1 } n _ { 1 3 } = 1 \cdot 1 \cdot 1 \cdot 3 \cdot 1 \cdot 3 = 9 .
$$

9B. Let $A \subseteq \mathbb { R }$ be uncountable.

(a) Show that A has at least one accumulation point.

(b) Show that A has uncountably many accumulation points.

(Recall that a point is said to be an accumulation point of A if and only if it is the limit of a sequence of distinct terms from A.)

Solution:

(a) For $n \in \mathbb { Z }$ let $A _ { n } = A \cap [ n , n + 1 )$ Then $A = \cup _ { n \in \mathbb { Z } } A _ { n }$ Since A is uncountable, at least one of the sets $A _ { n }$ needs to be uncountable. Then we can find a sequence in $A _ { n }$ with distinct terms. This sequence is bounded, so it has a convergent subsequence. The limit of the subsequence is an accumulation point for A.

(b) Denote by B the set of accumulation points. Assume by contradiction that B is at most countable. The set B is closed, so its complement R\B is open. Then we can represent it as a countable union of closed sets, R $\backslash B = \cup C _ { n }$ . If B is at most countable then A must have uncountably many elements in $\mathbb { R } \ \backslash B ,$ therefore in one of the sets $C _ { n }$ . By part $\mathrm { ( a ) }$ $A \cap C _ { n }$ has at least one accumulation point. $C _ { n }$ is closed, so this accumulation point is in $C _ { n }$ This contradicts the fact that all accumulation points of A are in B which does not intersect $C _ { n }$