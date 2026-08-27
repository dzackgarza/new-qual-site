# FALL 2007 PRELIMINARY EXAMINATION SOLUTIONS

1A. Let $\mathbb { Z } [ i ]$ be the set of complex numbers of the form $a + b i$ where a and b range over all integers. List all subrings of $\mathbb { Z } [ i ]$ . (Your list should contain each subring exactly once.)

Solution: For $n \in \mathbb { Z } _ { \geq 1 }$ , let $R _ { n } = \mathbb { Z } + n \mathbb { Z } i$ . We claim that $\mathbb { Z } , R _ { 1 } , R _ { 2 } , . . .$ . is a list of all subrings of $\mathbb { Z } [ i ]$

First, each $R _ { i }$ is a subring since it contains 0 and 1 and is closed under negation, addition, and multiplication. And of course Z is a subring too.

Now we show that any subring R equals either Z or some $R _ { n }$ Any subring R is an additive subgroup of $\mathbb { Z } [ i ]$ containing Z. The additive subgroups of $\mathbb { Z } [ i ]$ containing Z are the inverse images of subgroups of the quotient group $\mathbb { Z } [ i ] / \mathbb { Z }$ , which is isomorphic to $\mathbb { Z }$ via the homomorphism sending the class of $a + b i$ to b. The subgroups of $\mathbb { Z }$ are {0} and $n \mathbb { Z }$ for $n \in \mathbb { Z } _ { \geq 1 }$ , and their inverse images under $\mathbb { Z } [ i ] \to \mathbb { Z } [ i ] / \mathbb { Z } \simeq \mathbb { Z }$ are Z and $R _ { n }$ , respectively.

2A. Let $f ( z )$ and $g ( z )$ be entire functions such that $f ^ { \prime } ( z ) ~ = ~ g ( z ) , ~ g ^ { \prime } ( z ) ~ = ~ - f ( z )$ , and $f ( 2 z ) = 2 f ( z ) g ( z )$ for all $z \in \mathbb { C }$ . Find all possibilities for $f ( z )$

Solution: The first two identities imply $f ^ { \prime \prime } ( z ) = - f ( z )$ , to which the general solution is $f ( z ) = a e ^ { i z } + b e ^ { - i z }$ where $a , b \in \mathbb { C }$ . Conversely, if $a , b \in \mathbb { C }$ , then the functions $f ( z ) : =$ $a e ^ { i z } + b e ^ { - i z }$ and $g ( z ) : = f ^ { \prime } ( z ) = a i e ^ { i z } - b i e ^ { - i z }$ satisfy the first two identities.

It remains to check which $a , b \in \mathbb { C }$ lead to the third identity being satisfied. The third identity says

$$
a e ^ { 2 i z } + b e ^ { - 2 i z } = 2 ( a e ^ { i z } + b e ^ { - i z } ) ( a i e ^ { i z } - b i e ^ { - i z } )
$$

or equivalently,

$$
( a - 2 a ^ { 2 } i ) e ^ { 4 i z } = - b - 2 b ^ { 2 } i .
$$

This holds for all $z \in \mathbb { C }$ if and only if $a - 2 a ^ { 2 } i = 0$ and $- b - 2 b ^ { 2 } i = 0$ . These equations are equivalent to $a \in \{ 0 , - i / 2 \}$ and $b \in \{ 0 , i / 2 \}$ . Thus there are four possibilities for $f ( z )$ namely $0 , - i e ^ { i z } / 2 , i e ^ { - i z } / 2$ , and

$$
- i e ^ { i z } / 2 + i e ^ { - i z } / 2 = \sin z .
$$

3A. Let A be an $n \times n$ Hermitian matrix, and let $x \in \mathbb { C } ^ { n }$ be a vector such that $A ^ { 2 } x = 0$ Prove that $A x = 0$

Solution: We have: $A ^ { 2 } x = 0 \Rightarrow A ^ { H } A x = 0$ (since $A ^ { H } = A ) \Rightarrow x ^ { H } A ^ { H } A x = 0 \Rightarrow \| A x \| ^ { 2 } =$ $\langle A x , A x \rangle = 0 \Rightarrow \| A x \| = 0 \Rightarrow A x = 0 .$

4A. Let $( a _ { n } ) _ { n \geq 1 }$ and $( b _ { n } ) _ { n \geq 1 }$ be sequences of real numbers. Suppose that $0 \leq a _ { n + 1 } \leq a _ { n } + b _ { n }$ for all $n \geq 1$ , and that $\sum _ { n = 1 } ^ { \infty } b _ { n }$ converges. Prove that $\operatorname* { l i m } _ { n \to \infty } a _ { n }$ exists and is finite.

Solution: Fix any $\epsilon > 0$ Since $\sum b _ { n }$ converges, there exists $N _ { \epsilon } < \infty$ such that for all $n \geq N _ { \epsilon }$ and all $k \geq 0$ , we have $| b _ { n } + \overline { { { b } } } _ { n + 1 } + \cdot \cdot \cdot + b _ { n + k } | < \epsilon$ . Hence for all $n \geq N _ { \epsilon }$ and $k \geq 0$

$$
\begin{array} { l c l } { { a _ { n + k + 1 } } } & { { \leq } } & { { a _ { n } + b _ { n } + \cdot \cdot \cdot + b _ { n + k } } } \\ { { } } & { { < } } & { { a _ { n } + \epsilon . } } \end{array}
$$

Therefore sup $a _ { m } \leq a _ { n } + \epsilon$ . Hence lim sup $a _ { n } < \infty$ m>n n→∞

All the $a _ { n }$ except possibly $a _ { 1 }$ are nonnegative, so lim inf $a _ { n }$ is finite. Take $n _ { 1 } < n _ { 2 } < . . .$ such that $a _ { n _ { k } } $ lim inf $a _ { n }$ . Then

$$
\begin{array} { l } { \operatorname* { l i m } \operatorname* { s u p } a _ { n } = \displaystyle \operatorname* { l i m } _ { k \to \infty } \operatorname* { s u p } _ { m > n _ { k } } a _ { m } } \\ { \qquad \leq \displaystyle \operatorname* { l i m } _ { k \to \infty } \left( a _ { n _ { k } } + \epsilon \right) } \\ { \qquad = \epsilon + \operatorname* { l i m } \operatorname* { i n f } a _ { n } . } \end{array}
$$

Sending  to zero shows that lim sup $a _ { n } \leq$ lim inf $a _ { n }$ . But lim sup $a _ { n } \geq$ lim inf $a _ { n }$ trivially, so lim sup $a _ { n } = \operatorname* { l i m } \operatorname* { i n f } a _ { n }$ . This means that lim $a _ { n }$ exists and is finite.

5A. Suppose that G is a finite group such that for each subgroup H of G there exists a homomorphism $\phi \colon G \to H$ such that $\phi ( h ) = h$ for all $h \in H$ . Show that G is a product of groups of prime order.

Solution: We proceed by induction on |G|. The base case $| G | = 1$ is trivial. Suppose that $| G | > 1$ and that the statement is true for all smaller groups. Choose a subgroup H of G of prime order p. By assumption, there is a homomorphism $\phi \colon G \to H$ such that $\phi ( h ) = h$ for all $h \in H$ . Let $K = \ker \phi$ . By the inductive hypothesis, K is a product of groups of prime order. Let $\sigma \colon G \to K$ be a homomorphism such that $\sigma ( h ) = h$ for all $h \in K$ . Let $\alpha \colon G \to K \times H$ be the homomorphism defined by

$$
\alpha ( g ) : = ( \sigma ( g ) , \phi ( g ) ) .
$$

Since σ restricted to ker $\phi$ equals the identity on K, the kernel of α is trivial. Also $| G | =$ $| K | | H |$ , so α is an isomorphism. The result follows because H has order $p .$

6A. Let $f ( z ) = z ^ { 4 } + \frac { z ^ { 3 } } { 4 } - \frac { 1 } { 4 } .$ . How many zeros does f have in $\{ z \in \mathbb { C } : \frac { 1 } { 2 } < | z | < 1 \} ?$

Solution: We claim that f has 4 zeros in the given annulus. We use Rouch´e’s Theorem at least once. Let $g _ { 1 } ( z ) = z ^ { 4 }$ . Then $g _ { 1 }$ has four zeros (counted with multiplicity) in $\{ z \in \mathbb { C }$ : $| z | < 1 \}$ and

$$
\begin{array} { r c l } { \displaystyle | f ( z ) - g _ { 1 } ( z ) | } & { = } & { \displaystyle \left| \frac { z ^ { 3 } } { 4 } - \frac { 1 } { 4 } \right| } \\ { \displaystyle } & { \leq } & { \displaystyle \frac { 1 } { 2 } < | g _ { 1 } ( z ) | } \end{array}
$$

on $| z | = 1$ . Hence f also has four zeros in $\{ z \in \lvert z \rvert < 1 \}$ . There are two ways to proceed from here:

(1) For $| z | \leq { \frac { 1 } { 2 } } , | f ( z ) | \geq { \frac { 1 } { 4 } } - { \frac { 1 } { 1 6 } } - { \frac { 1 } { 3 2 } } > 0 .$ . Hence f has no zeros in $| z | \leq { \frac { 1 } { 2 } }$

(2) Let $g _ { 2 } ( z ) ~ = ~ - 3 / 4$ . Then $| f ( z ) - g _ { 2 } ( z ) | \leq { \frac { 1 } { 1 6 } } + { \frac { 1 } { 3 2 } } + { \frac { 1 } { 2 } } < { \frac { 3 } { 4 } } \equiv | g _ { 2 } ( z ) | { \mathrm { ~ f o r ~ } } | z | = { \frac { 1 } { 2 } } .$ Hence f and $g _ { 2 }$ have no zeros inside $| z | \leq 1 / \bar { 2 }$

7A. Let $P \in \mathbb { R } ^ { n \times n }$ be a matrix satisfying $P ^ { 3 } = P$ . Let r be the rank of P and assume $r > 0$ Show that there exist matrices $U , V \in \mathbb { R } ^ { n \times r }$ satisfying $V ^ { T } U = I _ { r }$ such that

$$
P = U S V ^ { T } ,
$$

where $I _ { r }$ is the $r \times r$ identity matrix, and S is an $r \times r$ diagonal matrix with ±1’s on the diagonal.

Solution: Since P satisfies the polynomial equation $x ^ { 3 } - x = 0$ with distinct real roots $0 , 1 , - 1$ , the Jordan normal form theorem implies that there exist matrices $T , J \in \mathbb { R } ^ { n \times n }$ such that $P = T J T ^ { - 1 }$ where T is nonsingular and J is diagonal with r nonzero entries. Moreover, we may assume that these r nonzero entries $( \mathrm { a l l \pm 1 } )$ are in the upper left part of the diagonal of J .

Thus $J = \mathrm { d i a g } ( S , { \bf 0 } )$ , where S is a $r \times r$ diagonal matrix with ±1’s on the diagonal. Let $U \in \mathbb { R } ^ { n \times r }$ be the first r columns of T , and let $V \in \mathbb { R } ^ { n \times r }$ be the transpose of the first r rows of $T ^ { - 1 }$ . It follows that $V ^ { T } U = I _ { r }$ and $P = U S V ^ { T }$

8A. Suppose that $( b _ { n } ) _ { n \geq 1 }$ is a sequence of positive real numbers tending to infinity such that $b _ { n } / n \to 0$ . Must there exist a sequence $( a _ { n } ) _ { n \geq 1 }$ such that $( a _ { 1 } + \cdot \cdot \cdot + a _ { n } ) / n \to 0$ and lim $\textstyle \operatorname* { s u p } _ { n \to \infty } ( a _ { n } / b _ { n } ) = \infty ?$

Solution: Yes. Replacing $b _ { n }$ with $b _ { n } ^ { * } = \operatorname* { m a x } _ { 1 < k < n } b _ { k }$ , we may suppose that $\left( b _ { n } \right)$ is non-decreasing: this does not upset the hypothesis $b _ { n } / n \to 0$ . Then there exist $1 \leq n _ { 1 } < n _ { 2 } < . . .$ . such that both $\frac { n _ { k + 1 } } { n _ { k } }  \infty$ and $\frac { b _ { n _ { k + 1 } } } { b _ { n _ { k } } }  \infty$ as $k  \infty$ . Let $a _ { n _ { k } } = \sqrt { n _ { k } b _ { n _ { k } } }$ and let $a _ { j } = 0$ if $j \not \in \{ n _ { 1 } , n _ { 2 } , . . . \}$ . For $n _ { k } \le j < n _ { k + 1 }$ , we have

$$
\left| { \frac { a _ { 1 } + \cdot \cdot \cdot + a _ { j } } { j } } \right| \leq \sum _ { i = 1 } ^ { k } { \frac { | a _ { n _ { i } } | } { n _ { k } } } \leq { \frac { ( 1 + o ( 1 ) ) { \sqrt { n _ { k } b _ { n _ { k } } } } } { n _ { k } } } ,
$$

which tends to 0 as $k \to \infty$ , while

$$
\operatorname* { l i m } _ { n  \infty } { \frac { a _ { n } } { b _ { n } } } = \operatorname* { l i m } _ { k  \infty } { \frac { a _ { n _ { k } } } { b _ { n _ { k } } } } = \operatorname* { l i m } _ { k  \infty } \sqrt { \frac { n _ { k } } { b _ { n _ { k } } } } = \infty .
$$

9A. Let G be a non-abelian group of order 16 having a subgroup H isomorphic to $C _ { 2 } { \times } C _ { 2 } { \times } C _ { 2 }$ (where $C _ { 2 }$ denotes a cyclic group of order 2). Prove that the number of elements of G of exact order 2 is either 7 or 11.

Solution: Since $( G : H ) = 2$ , the subgroup H is normal in G. We may regard H as a 3-dimensional vector space over $\mathbb { F } _ { 2 }$ . There are $2 ^ { 3 } - 1 = 7$ elements of order 2 in H.

Case $1 \colon G - H$ contains no element of order 2. Then the number of order 2 elements of G is also 7.

Case 2: Suppose that $G - H$ contains an element d of order 2. Then G is the semidirect product of $\langle d \rangle$ by H, and is determined up to isomorphism by the conjugation action of d on

H; this action must be nontrivial, since otherwise G would be Abelian. The action is given by an element D of $M _ { 3 } ( \mathbb { F } _ { 2 } )$ of order 2. In particular the eigenvalues are all 1. A Jordan block of size 3 does not have order 2, so D must consist of Jordan blocks of size 2 and 1.

Thus for a suitable choice of basis of H, we have $D = { \binom { 1 } { 0 } } \ 1 \ 0 \atop { 0 } )$ . An element of $G - H$ of

order 2 is of the form dh where $( d h ) ^ { 2 } = e ,$ or equivalently $( d h d ^ { - 1 } ) h = e ;$ the corresponding values of h are those in the kernel of $D - I .$ , so there are 4 of them. Thus G has $7 + 4 = 1 1$ elements of order 2.

1B. Let $f ( z )$ be a polynomial with complex coefficients, and let a be a complex number.   
Prove that $\{ a , f ( a ) , f ( f ( a ) ) , \ldots \}$ is not dense in C.

Solution: Let $S = \{ a , f ( a ) , f ( f ( a ) ) , \ldots \}$ . If S is bounded, then S is not dense in C. So assume that S is unbounded.

Case 0: f is constant. Then $\# S \leq 2$ , so S is not dense in C.

Case $1 \colon \deg f = 1$ Write $f ( z ) = s z + t$ for some $s , t \in \mathbb { C }$ with $s \neq 0$ . If $s = 1$ , then S is contained in a line, and hence is not dense. So suppose that $s \neq 1$ . Then $f ( z ) = z$ has a solution $z = c .$ , and replacing f(z) by $f ( z + c ) - c$ (and replacing $S { \mathrm { ~ b y ~ } } { - c + S } )$ lets us reduce to the case where $t = 0$ . Now $S = \{ a , s a , s ^ { 2 } a , . . . \}$ Since S is unbounded, $| s | > 1$ . But then S contains only finitely many points in each disk, so S is not dense in C.

Case 2: deg $f \geq 2$ Then $f ( z ) / z \to \infty { \mathrm { ~ a s ~ } } z \to \infty$ , so there exists $M > 0$ such that $| z | > M$ implies $| f ( z ) | > | z |$ . Since S is unbounded, there exists n such that $| f ^ { n } ( a ) | > M$ By induction, we obtain $| f ^ { N } ( a ) | > M$ for all $N \geq n$ . Thus S contains only finitely many points in the disk $| z | \leq M$ , so S is not dense in C.

2B. Let A be an $n \times n$ complex matrix. Suppose that m is a positive integer such that $A ^ { m }$ is diagonalizable. Prove that $A ^ { m + 1 }$ is diagonalizable.

Solution: We may assume that A is in Jordan canonical form, and we may reduce to the case where A is a single Jordan block, so $A = \lambda I + N$ , where $\lambda \in \mathbb { C }$ and N is nilpotent.

Case $1 \colon \lambda = 0$ . Then $N ^ { m }$ is nilpotent and diagonalizable, so $N ^ { m } = 0$ . Hence $N ^ { m + 1 } =$ $N \cdot 0 = 0$

Case 2: $\lambda \neq 0$ . Then $A ^ { m }$ is diagonalizable with all eigenvalues equal to $\lambda ^ { m }$ , so $A ^ { m } = \lambda ^ { m } I$ In particular A satisfies the equation $x ^ { m } - \lambda ^ { m } = 0$ with distinct roots, so A is diagonalizable. Thus $A ^ { m + 1 }$ is diagonalizable.

3B. Let $\{ u _ { 1 } , u _ { 2 } , \cdots , u _ { k } \}$ be a set of linearly independent vectors in $\mathbb { R } ^ { n }$ , and let A be a closed set in $\mathbb { R } ^ { k }$ . Let S be the set of linear combinations $\alpha _ { 1 } u _ { 1 } + \alpha _ { 2 } u _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } u _ { k }$ obtained as $\left( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { k } \right)$ ranges over all points of A. Show that S is a closed subset of $\mathbb { R } ^ { n }$

Solution: Extend $u _ { 1 } , \ldots , u _ { k }$ to a basis $u _ { 1 } , \ldots , u _ { n }$ of $\mathbb { R } ^ { n }$ , and let U be the $n \times n$ matrix whose columns are the $u _ { i }$ . Since U is invertible, it induces a homeomorphism of $\mathbb { R } ^ { n }$

Let 0 be the origin in $\mathbb { R } ^ { n - k }$ . Then $A \times \{ \mathbf { 0 } \}$ is closed in $\mathbb { R } ^ { k } \times \mathbb { R } ^ { n - k } = \mathbb { R } ^ { n }$ , and S is the image of $A \times \{ \mathbf { 0 } \}$ under the homeomorphism $U \colon \mathbb { R } ^ { n } \to \mathbb { R } ^ { n }$ , so S is closed.

4B. Let K and L be fields, and let $K \times L$ be the product ring, with addition and multiplication defined componentwise. Find all prime ideals of $K \times L$

Solution: The first projection $K \times L \to K$ is surjective and its kernel is an ideal I such that $( K \times L ) / I$ is a field (isomorphic to K), so I is a maximal ideal. Similarly the kernel of the second projection is a maximal ideal J.

Now let P be any prime ideal of $K \times L$ . Since $( 1 , 0 ) ( 0 , 1 ) = 0$ , either $( 1 , 0 ) { \mathrm { ~ o r ~ } } ( 0 , 1 )$ is in P . If $( 1 , 0 ) \in P$ , then $( a , 0 ) = ( a , 0 ) ( 1 , 0 ) \in \mathcal { P }$ for all a, so $J \subseteq P { \mathrm { : } }$ ; but J is maximal, so then $P = J$ . Similarly if $( 0 , 1 ) \in P$ , then $P = I$

Thus I and J are the only prime ideals of $K \times L$

5B. Let $f ( z )$ be an entire function and let $a _ { 1 } , \ldots , a _ { n }$ be all zeros of f in C. Suppose that there exist real numbers $R > 0$ and $a > 1$ such that $| f ( z ) | \geq | z | ^ { a }$ for all $| z | \geq R$ . Prove that

$$
\sum _ { j = 1 } ^ { n } \operatorname { R e s } _ { z = a _ { j } } { \frac { 1 } { f ( z ) } } = 0 .
$$

Solution: Let $g ( z ) = 1 / f ( z )$ . Let $R _ { 0 } > R$ be large enough that all $a _ { 1 } , \ldots , a _ { n }$ are inside the circle $| z | = R _ { 0 }$ . Let $r \geq R _ { 0 }$ . We have

$$
\int _ { | z | = r } g ( z ) d z = 2 \pi i \sum _ { j = 1 } ^ { n } \operatorname { R e s } ( g , a _ { j } ) .
$$

This is true for all $r \geq R _ { 0 }$ . Also

$$
\left| \int _ { | z | = r } g ( z ) d z \right| ~ = ~ \left| i r \int _ { 0 } ^ { 2 \pi } \frac { d t } { f ( r e ^ { i t } ) } e ^ { i t } \right| \leq
$$

$$
r \int _ { 0 } ^ { 2 \pi } \frac { d t } { | f ( r e ^ { i t } ) | } \leq 2 \pi r \frac { 1 } { r ^ { a } } = \frac { 2 \pi } { r ^ { a - 1 } } .
$$

Thus

$$
\left| \sum _ { j = 1 } ^ { n } { \mathrm { R e s } } ( g , a _ { j } ) \right| \leq { \frac { 2 \pi } { r ^ { a - 1 } } } { \mathrm { ~ f o r ~ a l l ~ } } r \geq R _ { 0 } .
$$

Hence $\textstyle \sum _ { j = 1 } ^ { n } \operatorname { R e s } ( g , a _ { j } ) = 0$ , since $\frac { 1 } { r ^ { a - 1 } }  0$ where $r \to \infty$ , since $a > 1$

6B. Given a positive integer n, what are the possible values of the triple $( \operatorname { r k } ( A ) , \operatorname { r k } ( B ) , \operatorname { r k } ( C ) )$ as $A , B , C$ range over real $n \times n$ matrices satisfying $A + B + C = 0 ?$

Solution: We claim that the answer is the set of triples $( a , b , c )$ of integers in [0, n] satisfying $c \leq a + b , a \leq b + c .$ and $b \leq c + a$

The image of C is contained in the sum of the images of A and B, so $\operatorname { r k } ( C ) \leq \operatorname { r k } ( A ) + \operatorname { r k } ( B )$ Similarly, rk $\operatorname { \mathrm { \Omega } } [ A ) \leq \operatorname { \mathrm { r k } } ( B ) + \operatorname { \mathrm { r k } } ( C )$ and r $\operatorname { \mathrm { \Omega } } [ B ] \leq \operatorname { \mathrm { \mathrm { r k } } } ( C ) + \operatorname { \mathrm { \mathrm { r k } } } ( A )$

Conversely, suppose that a, b, c satisfy the inequalities. Without loss of generality, $c \geq a , b$ Let A be the diagonal matrix whose diagonal entries are a ones followed by $n - a$ zeros. Let B be the diagonal matrix whose diagonal entries are $c - b$ zeros followed by b ones followed by $n - c \ \mathrm { z e r o s }$ . Let $C : = - ( A + B )$ ), so $A + B + C = 0$ Then rk $\dot { \mathbf { \eta } } : ( A ) = a , \operatorname { r k } ( B ) = b ,$ , and rk $( C ) = \operatorname { r k } ( A + B ) = c .$ since C is a diagonal matrix with exactly c nonzero entries.

7B. Let f be continuous on $[ 0 , \infty )$ and suppose that lim $f ( x )$ exists and is finite. Must f x→∞   
be uniformly continuous? Give a proof or a counterexample.

Solution: The function f is uniformly continuous. Given $\epsilon > 0$ , we must find $\delta > 0$ such that $| x - y | < \delta$ implies $| f ( x ) - f ( y ) | < \epsilon$ There exists $x _ { 0 } \geq 0$ such that for all $x \geq x _ { 0 }$ , we have $| f ( x ) - L | < \epsilon / 3$ . By compactness of $[ 0 , x _ { 0 } ]$ there exists $\delta > 0$ such that for all $x , y$ in $[ 0 , x _ { 0 } ]$ such that $| x - y | < \delta$ implies $| f ( x ) - \overline { { f ( y ) } } | < \epsilon / 3 \cdot$ choose such a δ.

Suppose that $0 \leq x \leq y < x + \delta ;$ we must prove that $| f ( x ) - f ( y ) | < \epsilon . { \mathrm { ~ I f ~ } } y \leq x _ { 0 }$ we are done. If $x \leq x _ { 0 } < y$ then by the triangle inequality,

$$
\left| f ( x ) - f ( y ) \right| \leq \left| f ( x ) - f ( x _ { 0 } ) \right| + \left| f ( x _ { 0 } ) - L \right| + \left| L - f ( y ) \right| < \epsilon / 3 + \epsilon / 3 + \epsilon / 3 = \epsilon .
$$

Finally, if $x _ { 0 } \leq x$ then $| f ( x ) - f ( y ) | \leq | f ( x ) - L | + | L - f ( y ) | < \epsilon$ . Thus f is uniformly continuous.

8B. Show that for every positive integer n, there exists an irreducible polynomial over $\mathbb { Q }$ of degree n such that all its roots are real.

Solution: Let N be a large positive integer. Let $\begin{array} { r } { f ( x ) = \prod _ { k = 1 } ^ { n } ( x - 2 ^ { N } k ) } \end{array}$ and $g ( x ) = 2 + f ( x )$ Then $g ( x )$ is irreducible by Eisenstein’s criterion. Also

$$
\operatorname * { l i m } _ { x \to \infty } g ( x ) = \infty , { \mathrm { ~ a n d ~ } } \operatorname * { l i m } _ { x \to - \infty } g ( x ) = ( - 1 ) ^ { n } \infty .
$$

Let $1 \leq j \leq n - 1$ be an integer.

$$
f ( 2 ^ { N } ( j + 1 / 2 ) ) = 2 ^ { N n } \prod _ { k = 1 } ^ { n } ( j + 1 / 2 - k )
$$

$$
\prod _ { k = 1 } ^ { n } ( j + 1 / 2 - k ) = { \frac { - 1 } { 4 } } \prod _ { k = 1 } ^ { j - 1 } ( j + 1 / 2 - k ) \prod _ { k = j + 2 } ^ { n } ( j + 1 / 2 - k ) .
$$

Thus

$$
| f ( 2 ^ { N } ( j + 1 / 2 ) ) | > 2 ^ { N n - 2 } \mathrm { ~ a n d ~ } \mathrm { s g n } ( f ( 2 ^ { N } ( j + 1 / 2 ) ) ) = ( - 1 ) ^ { n - j } .
$$

Itin ctua for $N \geq 2$ work),  and in $g ( x )$ $( - \infty , 2 ^ { N } ( 1 + 1 / 2 ) )$ ,l $( 2 ^ { N } ( j + 1 / 2 ) , 2 ^ { N } ( \hat { j } + 3 / \hat { 2 } ) )$ $1 \leq j \leq n - 2$ $( \dot { 2 } ^ { N } ( n - 1 / 2 , \infty ) )$ roots.

9B. Let f be holomorphic on a neighborhood of the closed disk $\overline { { B _ { 1 } ( 0 ) } } = \{ z : | z | \leq 1 \}$ Suppose that m $\begin{array} { r } { \operatorname { 1 a x } _ { | z | = 1 } | f ( z ) | \le 1 } \end{array}$ . Prove that there exists a complex number z such that $| z | \le 1$ and $f ( z ) = { \dot { z } }$

Solution: Let $\alpha _ { n } \ > \ 1$ and $\alpha _ { n } \ \to \ 1$ . Let $g _ { n } ( z ) = f ( z ) - \alpha _ { n } z$ and $h _ { n } ( z ) \ : = \ : \alpha _ { n } z$ Then $| g _ { n } ( z ) + h _ { n } ( z ) | = | f ( z ) | \le 1 < \alpha _ { n } = | h _ { n } ( z ) |$ for all $| z | = 1$ . By Rouch´e’s Theorem there is $z _ { n }$ with $| z _ { n } | < 1$ such that $g _ { n } ( z _ { n } ) = 0$ or $f ( z _ { n } ) = \alpha _ { n } z _ { n } , n = 1 , 2 , . . .$ Let z be a limit point of $\begin{array} { r } { \{ z _ { n } \} , \ \mathrm { i . e . , } \ z = \operatorname* { l i m } _ { k \to \infty } z _ { n _ { k } } } \end{array}$ for some subsequence $\left\{ z _ { n _ { k } } \right\}$ of $\left\{ z _ { n } \right\}$ . Then $| z | \le 1$ and $f ( z ) = \operatorname * { l i m } ( \alpha _ { n _ { k } } z _ { n _ { k } } ) = ( \operatorname* { l i m } \alpha _ { n _ { k } } ) ( \operatorname* { l i m } z _ { n _ { k } } ) = 1 \cdot z = z$