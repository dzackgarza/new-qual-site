1A. (a) Let $( a _ { n } ) _ { 1 } ^ { \infty }$ be a sequence in R such that

$$
\sum _ { n = 1 } ^ { \infty } \left| a _ { n + 1 } - a _ { n } \right| < \infty .
$$

Prove that $( a _ { n } ) _ { 1 } ^ { \infty }$ is a Cauchy sequence.

(b) Is the converse true? Give a proof or a counterexample.

Solution: (a) Given $\varepsilon > 0$ , there is an integer N such that

$$
\sum _ { k = N } ^ { \infty } \left| a _ { k + 1 } - a _ { k } \right| < \varepsilon .
$$

Therefore, for any m, n with $N \leq m < n$

$$
\left| \sum _ { k = m } ^ { n - 1 } ( a _ { k + 1 } - a _ { k } ) \right| \leq \sum _ { k = m } ^ { n - 1 } | a _ { k + 1 } - a _ { k } | < \varepsilon .
$$

The series on the left telescopes, giving

$$
| a _ { n } - a _ { m } | < \varepsilon .
$$

(b) Simple counterexample: $a _ { n } = ( - 1 ) ^ { n } / n$ . Then $| a _ { n + 1 } - a _ { n } | = ( 2 n + 1 ) / ( n ^ { 2 } + n )$ , so $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } \left| a _ { n + 1 } - a _ { n } \right| = \infty } \end{array}$ by the limit comparison test (compare with $\textstyle \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n } } )$

2A. Prove or disprove the statement: Every function $f \colon  { \mathbb { R } } \to  { \mathbb { R } }$ such that $f ( x + y ) =$ $f ( x ) + f ( y )$ for all x and y is continuous.

Solution: The statement is false. Let π be an irrational number. Then 1 and π are linearly independent over $\mathbb { Q } .$ , so we may extend the set $\{ 1 , \pi \}$ to a basis B of R as a Q-vector space. There exists a Q-linear function $f : \mathbb { R } \to \mathbb { Q }$ taking arbitrarily prescribed values on the basis $B ;$ choose f such that $f ( 1 ) = 1 , f ( \pi ) = 0$ The first condition implies $f ( x ) = x$ for all $x \in \mathbb { Q }$ If f were continuous it would follow that $f ( x ) = x$ for all $x \in \mathbb { R }$ , contradicting $f ( \pi ) = 0$

3A. Prove that there is no holomorphic bijection from the punctured disk $0 < | z | < 1$ in $\mathbb { C }$ onto the annulus $r < | z | < R$ , where $0 < r < R < \infty$

Solution: Suppose the analytic function f maps $D \setminus \{ 0 \} = \{ z : 0 < | z | < 1 \}$ onto the annulus A. Then f is bounded in a neighborhood of 0, and therefore f has a removable singularity at 0, so f extends to an analytic function on the open disk D. By the open mapping theorem, $f ( 0 ) = p \in A$ . Also there is some $z _ { 0 } \in D \setminus \{ 0 \}$ with $f ( z _ { 0 } ) = p .$ . Then there are small disjoint neighborhoods $U , V$ of 0 and $z _ { 0 }$ respectively, such that $f ( U )$ and $f ( V )$ are neighborhoods of $p .$

Hence $f ( U \setminus \{ 0 \} )$ and $f ( V )$ are open sets in A which are not disjoint.

This shows that f is not 1 − 1 on $D \setminus \{ 0 \}$

4A. Suppose A and B are commuting $n \times n$ matrices over R. Suppose A and B are each diagonalizable over R. Show that AB is diagonalizable over R.

Solution: Let $V _ { 1 } , \ldots , V _ { r }$ be the eigenspaces in $K ^ { n }$ corresponding to the distinct eigenvalues of A in K. Because A is diagonalizable,

$$
K ^ { n } = \bigoplus _ { i } V _ { i } .
$$

Because A and B commute, $B V _ { i } \subseteq V _ { i }$ Because B is diagonalizable over R, its minimal polynomial is a product of linear factors over R, and the minimal polynomial of $B | _ { V _ { i } }$ divides this, so $B | _ { V _ { i } }$ is diagonalizable as well. Thus

$$
V _ { i } = \bigoplus _ { j } W _ { i j } ,
$$

where the $W _ { i j }$ are the eigenspaces of B in $V _ { i }$ corresponding to distinct eigenvalues. Since $W _ { i j }$ is an eigenspace for AB and

$$
\bigoplus _ { i j } W _ { i j } = K ^ { n } ,
$$

AB must be diagonalizable.

5A. Let I be an open interval and let $f \colon I  \mathbb { R }$ have continuous k-th derivatives everywhere on I for all $k \leq n - 1$ . Let $a \in I$ be such that $f ^ { ( k ) } ( a ) = 0$ for $1 \leq k \leq n - 1$ , and assume that $f ^ { ( n ) } ( a )$ is defined and $f ^ { ( n ) } ( a ) > 0$ . Prove that if n is even, then f has a local minimum at a, and if n is odd, then f has no local extremum at a.

Solution: By the definition of derivative and the assumption that $f ^ { ( n - 1 ) } ( a ) = 0$

$$
\operatorname* { l i m } _ { x \to a } { \frac { f ^ { ( n - 1 ) } ( x ) } { x - a } } = f ^ { ( n ) } ( a ) > 0 .
$$

Hence there exists  such that $f ^ { ( n - 1 ) } ( x ) / ( x - a ) > 0$ for all $x \in ( a - \epsilon , a + \epsilon ) - \{ a \}$ . By Taylor’s theorem with remainder, we have

$$
f ( x ) = f ( a ) + f ^ { ( n - 1 ) } ( c ) ( x - a ) ^ { n - 1 } / ( n - 1 ) !
$$

for some $c \in [ a , x ] { \mathrm { ~ i f ~ } } x \geq a .$ , or $c \in [ x , a ] { \mathrm { ~ i f ~ } } x \leq a$ . For $x \in ( a - \epsilon , a )$ we have $f ^ { ( n - 1 ) } ( c ) \leq 0$ , so $f ( x ) \geq f ( a )$ if n is even, $f ( x ) \leq f ( a ) { \mathrm { ~ i f ~ } } n$ is odd. For $x \in ( a , a + \epsilon )$ , we have $f ^ { ( n - 1 ) } ( c ) \geq 0$ , so $f ( x ) \geq f ( a )$ for all n. This implies that f has a local minimum at a if n is even. If n is odd, it implies that either f has no local extremum, or f is constant on $( a - \epsilon , a + \epsilon )$ . But the latter possibility contradicts the assumption that $f ^ { ( n ) } ( a ) > 0$

6A. For every positive integer n, define $[ n ] _ { q } = q ^ { n - 1 } { + } q ^ { n - 2 } { + } \cdot \cdot \cdot { + } q { + } 1$ . Prove that $[ 1 ] _ { q } [ 2 ] _ { q } \cdot \cdot \cdot [ r ] _ { q }$ divides $[ k + \bar { 1 } ] _ { q } [ k + 2 ] _ { q } \cdot \cdot \cdot [ k + r ] _ { q }$ in the polynomial ring $\mathbb { Z } [ q ]$ , for all positive integers k and r.

Solution: Both polynomials are monic, so we need only show that every complex root ω of $[ 1 ] _ { q } [ 2 ] _ { q } \cdot \cdot \cdot [ r ] _ { q }$ is also a root of $[ 1 ] _ { q } [ 2 ] _ { q } \cdots [ r ] _ { q }$ , with equal or greater multiplicity.

The roots of $[ n ] _ { q } = ( q ^ { n } - 1 ) / ( q - \hat { 1 } )$ are the n-th roots of unity, excluding 1, and they are distinct. In particular, every root ω of $[ 1 ] _ { q } [ 2 ] _ { q } \cdot \cdot \cdot [ r ] _ { q }$ is a root of unity. Let d be the order of ω in the multiplicative group $\mathbb { C } ^ { * }$ , that is, ω is a primitive d-th root of unity. Then ω is a root of $[ n ] _ { q }$ if and only if $d \mid n$ . It follows that ω has multiplicity $\lfloor r / d \rfloor$ as a root of $[ 1 ] _ { q } [ 2 ] _ { q } \cdot \cdot \cdot [ r ] _ { q }$ and multiplicity $\lfloor ( k + \dot { r } ) / d \rfloor - \lfloor k / d \rfloor$ as a root of $[ k + 1 ] _ { q } [ k + { \bf \bar { 2 } } ] _ { q } \ : \dot { \bf \cdot } \ : \cdot [ k + r ] _ { q }$ . To complete the proof, we need the following inequality.

Lemma. $\lfloor ( k + r ) / d \rfloor \geq \lfloor k / d \rfloor + \lfloor r / d \rfloor$ for all $k , r , d .$

Proof. Set $a = | \boldsymbol { k } / d | , b = | \boldsymbol { r } / d |$ Then k ≥ ad, $r \geq b d .$ , hence $k + r \geq ( a + b ) d$ and $\lfloor ( k + r ) / d \rfloor \geq \lfloor ( a + b ) d / d \rfloor = a + b$ , since the floor function is monotone.

(An alternative proof is to show by induction that the Gauss binomial coefficient

$$
{ \left[ \begin{array} { l } { k + r } \\ { r } \end{array} \right] } _ { q } : = { \frac { [ k + 1 ] _ { q } [ k + 2 ] _ { q } \cdot \cdot \cdot [ k + r ] _ { q } } { [ 1 ] _ { q } [ 2 ] _ { q } \cdot \cdot \cdot [ r ] _ { q } } }
$$

is a polynomial, by using a q-analog of the Pascal’s triangle recurrence.)

7A. Let U be a connected open subset of $\mathbb { C } ,$ and let $f ( z )$ be a meromorphic function on U having at least one pole. For each $c \in U$ that is not a pole of $f ,$ let $R ( c )$ be the radius of convergence of the Taylor series of $f$ centered at c. Prove that $R ( c )$ extends to a continuous function defined on all of $U$

Solution: Let P be the set of poles of f in U . Each pole is isolated, so $P$ is closed in $U .$ , and $U - P$ is open (both in U and in C). For $c \in \mathbb { C }$ and $r > 0$ , let $D ( c , r ) : = \{ z \in \mathbb { C } : | z - c | < r \}$ Fix $c \in U - P$ Choose $\epsilon > 0$ such that $D ( c , \epsilon ) \subseteq U - P$ Then $\epsilon \leq R ( c )$ , and the function $g _ { c }$ on $D ( c , R ( c ) )$ defined by the Taylor series at c agrees with $f$ on $D ( c , \epsilon )$ . Note that $R ( c ) < \infty ,$ since otherwise by connectedness $f$ would equal the restriction to U of an entire function $g _ { c } .$ , contradicting the fact that f has a pole. If $c ^ { \prime } \in D ( c , \epsilon / 2 )$ , then $\{ c , c ^ { \prime } \} \subseteq D ( c ^ { \prime } , \epsilon / 2 ) \subseteq D ( c , \epsilon )$ , so the restrictions of $g _ { c }$ and the analogous function $g _ { c ^ { \prime } }$ to $D ( c ^ { \prime } , \epsilon / 2 )$ each agree with the restriction of $f .$ Thus $g _ { c } , g _ { c ^ { \prime } } , f$ have the same Taylor series centered at $c ,$ and they have the same Taylor series centered at $c ^ { \prime } .$ . The restriction of $g _ { c }$ to $D ( c ^ { \prime } , R ( c ) - | c - c ^ { \prime } | ) \subseteq D ( c , R ( c ) )$ is holomorphic, so $R ( c ^ { \prime } ) \geq R ( c ) - | c - c ^ { \prime } |$ . Similarly $R ( c ) \geq R ( c ^ { \prime } ) - | c - c ^ { \prime } | , \mathrm { s o } | R ( c ) - \dot { R } ( c ^ { \prime } ) | \leq | c - c ^ { \prime } |$ . Thus R is continuous at c.

Suppose $p \in P$ We may choose $\epsilon > 0$ such that $D ( p , \epsilon ) - \{ p \} \subseteq U - P$ . For $c \in$ $D ( p , \epsilon / 2 ) - \{ p \}$ , the restriction of $g _ { c }$ to $D ( c , | c - p | )$ agrees with $f ,$ , and $g _ { c } ( z ) \to \infty$ as $z \longrightarrow p$ within $D ( c , | c - p | )$ , so $R ( c ) = | c - p |$ . Thus defining $R ( p ) = 0$ at each $p \in P$ gives an extension of R to a continuous function on $U$

Remark: It is not true that $R ( c )$ equals the distance from c to the complement of $U -$ {poles of $f \}$ in $\mathbb { C } ,$ even if f does not extend to a larger open subset of C. For example, if f√ is the standard branch of $\frac { \log z } { z - 1 0 0 }$ on $\mathbb { C } - \mathbb { R } _ { \leq 0 }$ , then $R ( - 1 + i ) = \sqrt { 2 }$ 2, not 1.

The correct statement is that if $c \in U$ is not a pole, then $R ( c )$ equals the radius of the largest open disk on which there is some holomorphic function that agrees with $f$ on some open neighborhood of c.

8A. Let C and D be two $n \times n$ positive definite Hermitian matrices over C and let $A = C D$ Prove that all eigenvalues of A are positive real numbers.

Solution: Let $A x = \lambda x , x \neq 0$ . Then $C D x = \lambda x$ . Since D is positive definite, it is invertible, so Dx $\neq 0$ . Let $B ^ { H }$ denote the conjugate transpose of a matrix (or column

vector) B. Since C is positive definite,

$$
0 < \langle D x , C ( D x ) \rangle = ( D x ) ^ { H } C ( D x ) = ( D x ) ^ { H } \lambda x = \lambda x ^ { H } D ^ { H } x = \lambda x ^ { H } D x ,
$$

since D is Hermitian. But $x ^ { H } D x > 0$ since D is positive definite. Dividing, we get $\lambda > 0$

9A. Let $f \colon  { \mathbb { R } } ^ { 2 } \to$ R be an infinitely differentiable function that is zero outside some bounded subset of $\mathbb { R } ^ { 2 }$ . Prove that

$$
\operatorname* { l i m } _ { \epsilon \to 0 } \int \int _ { x ^ { 2 } + y ^ { 2 } \geq \epsilon ^ { 2 } } { \frac { f ( x , y ) } { ( x + i y ) ^ { 3 } } } d x d y
$$

exists.

Solution: The answer is positive. We must prove that

$$
\operatorname* { l i m } _ { \delta , \epsilon \to 0 } \int \int _ { \delta ^ { 2 } < x ^ { 2 } + y ^ { 2 } < \epsilon ^ { 2 } } { \frac { f ( x , y ) } { ( x + i y ) ^ { 3 } } } d x d y = 0
$$

We write

$$
f ( x , y ) = a + b x + c y + O ( x ^ { 2 } + y ^ { 2 } )
$$

and consider each of the three terms. For the last one we note that

$$
{ \frac { x ^ { 2 } + y ^ { 2 } } { | x + i y | ^ { 3 } } } = ( x ^ { 2 } + y ^ { 2 } ) ^ { - { \frac { 1 } { 2 } } }
$$

which is integrable at zero. For the constant we compute

$$
\iint _ { \delta ^ { 2 } < x ^ { 2 } + y ^ { 2 } < \epsilon ^ { 2 } } { \frac { 1 } { ( x + i y ) ^ { 3 } } } d x d y = \int _ { 0 } ^ { 2 \pi } \int _ { \delta < r < \epsilon } r ^ { - 2 } e ^ { - 3 i \theta } d r d \theta = 0
$$

For $f ( x , y ) = y$ we have

$$
\begin{array} { r c l } { { \displaystyle \iint _ { \delta ^ { 2 } < x ^ { 2 } + y ^ { 2 } < \epsilon ^ { 2 } } \frac { y } { ( x + i y ) ^ { 3 } } d x d y } } & { { = } } & { { \displaystyle \int _ { 0 } ^ { 2 \pi } \int _ { \delta < r < \epsilon } r ^ { - 1 } \cos \theta ~ e ^ { - 3 i \theta } d r d \theta } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } ( \ln \epsilon - \ln \delta ) \int _ { 0 } ^ { 2 \pi } e ^ { - 2 i \theta } + e ^ { - 4 i \theta } d \theta } } \\ { { } } & { { = } } & { { 0 } } \end{array}
$$

The case $f ( x , y ) = x$ is similar by symmetry. This concludes the proof.

1B. Let G be a finite group. Suppose ab = ba holds whenever $a , b \in G$ have prime power order. Prove that G is abelian.

Solution: Let $x , y \in G$ By the Chinese Remainder Theorem, the finite cyclic group generated by x is a product of cyclic groups of prime power order, so we can write $x = x _ { 1 } x _ { 2 } \cdot \cdot \cdot x _ { m }$ where each $x _ { i }$ has prime power order. Write $y = y _ { 1 } y _ { 2 } \cdot \cdot \cdot y _ { n }$ similarly. By assumption $x _ { 1 }$ commutes with each $y _ { j } , \operatorname { s o } x _ { 1 }$ commutes with their product $y$ . Similarly $x _ { i }$ commutes with $y$ for each $i ,$ so their product x commutes with y.

2B. Prove that, for any $\varepsilon > 0$ , the function $\begin{array} { r } { f ( z ) = \sin { z } + \frac { 1 } { z + i } } \end{array}$ has infinitely many zeros in the strip $| \operatorname { I m } z | < \varepsilon$ •

Solution: We use Rouch´e’s theorem. Without loss of generality, assume $\varepsilon < \pi$ . Let $\delta$ be the minimum value of | sin $z |$ on the compact set $| z | = \varepsilon$ . Since the zeros of sin z in C are the integer multiples of $\pi .$ , we have $\delta > 0$ . By periodicity, we have | sin $z | \geq \delta$ also on the circle $C _ { n }$ defined by $| z - 2 \pi n | = \varepsilon$ for any $n \in \mathbb { Z }$ . On the other hand, if n is sufficiently large, then $\begin{array} { r } { | \frac { 1 } { z + i } | < \delta } \end{array}$ on $C _ { n }$ . For such n, Rouch´e’s theorem implies that $f ( z )$ has the same number of zeros as sin z inside $C _ { n }$ , namely 1. Letting n vary, we find infinitely many zeros of $f ( z )$ inside the strip.

3B. Let $M _ { n } ( F )$ be the ring of $n \times n$ matrices over a field F . Prove that for every $A \in M _ { n } ( F )$ there exists $X \in M _ { n } ( F )$ such that $A X A = A$

Solution: Let $\phi \colon F ^ { n } \to F ^ { n }$ be the linear transformation defined by A. Let $W =$ ker $\phi _ { ; }$ , and let $V \subseteq F ^ { n }$ be a complementary subspace, such that $F ^ { n } = W \oplus V$ . Let $U = \operatorname { i m } \phi$ . Note that dim U = dim $V = { \mathrm { r a n k } } A$ . The restriction $\phi$ of $\phi$ to V is injective, hence ${ \overline { { \phi } } } \colon V \to U$ is an isomorphism. Let ${ \overline { { \psi } } } \colon U \to V$ be its inverse, and let $\psi$ be any extension of $\overline { { \psi } }$ from U to all of $F ^ { n }$ . Take X to be the matrix of $\psi$ . Then for every vector v in the column space $U$ of $A .$ , we have $A X v = \phi \psi v = v$ , which implies $A X A = A$

4B. Let D be a subset of R, and let $f \colon D \to \mathbb { R }$ be a function. The graph of f is the subset

$$
G : = \left\{ ( x , y ) : x \in D , \ y = f ( x ) \right\}
$$

of $\mathbb { R } ^ { 2 }$ . Prove that if G is compact, then $f$ is continuous.

Solution: It suffices to prove that $f ^ { - 1 } ( C )$ is closed in D for every closed subset C of R. Let $\pi _ { 1 } , \pi _ { 2 }$ be the coordinate projections $\mathbb { R } ^ { 2 } \to \mathbb { R }$ . Then $\pi _ { 2 } ^ { - 1 } ( C )$ is closed in $\mathbb { R } ^ { 2 }$ . Thus $\pi _ { 2 } ^ { - 1 } ( C ) \cap G$ is closed in $G$ and hence compact. Now $f ^ { - 1 } ( C ) = \bar { \pi _ { 1 } } ( \pi _ { 2 } ^ { - 1 } ( C ) \cap G )$ is the continuous image of a compact set, so it is compact. Thus $f ^ { - 1 } ( C )$ is closed in R, hence closed in D.

5B. Let $\mathbb { Q } ( x )$ be the field of rational functions in one variable over $\mathbb { Q }$ . Let i : $\mathbb { Q } ( x ) \to \mathbb { Q } ( x )$ be the unique field automorphism such that $i ( x ) = x ^ { - 1 }$ Prove that the fixed subfield $\{ r \in \mathbb { Q } ( x ) : i ( r ) = r \}$ is equal to $\mathbb { Q } ( x + x ^ { - 1 } )$ .

Solution: Let F denote the fixed subfield, and set $y = x + x ^ { - 1 }$ Obviously $\mathbb { Q } ( y ) \subseteq F \neq$ $\mathbb { Q } ( x )$ . The equation $x ^ { 2 } - y x + 1 = 0$ shows that $\mathbb { Q } ( x )$ is an algebraic extension of $\mathbb { Q } ( y )$ , and $[ \mathbb { Q } ( x ) : \mathbb { Q } ( y ) ] = 2$ . Since the intermediate field F is not equal to $\mathbb { Q } ( x )$ , we must have $F = \mathbb { Q } ( y )$

6B. Evaluate the integral $\int _ { 0 } ^ { \infty } { \frac { x \sin { x } } { x ^ { 2 } + a ^ { 2 } } }$ dx, where $a > 0$

Solution: Let I be the desired integral. Then

$$
{ \begin{array} { l } { I \ = \ { \frac { 1 } { 2 } } \displaystyle \int _ { - \infty } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x } \\ { \ = \ { \frac { 1 } { 2 } } \operatorname* { l i m } _ { R \to \infty } \displaystyle \int _ { - R } ^ { R } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x } \\ { \ = \ { \frac { 1 } { 2 } } \operatorname* { l i m } _ { R \to \infty } \operatorname { I m } _ { { \stackrel { . } { > } } } { \frac { x e ^ { i x } } { x ^ { 2 } + a ^ { 2 } } } d x . } \end{array} }
$$

Integrate $\frac { z e ^ { i z } } { z ^ { 2 } + a ^ { 2 } }$ counterclockwise around the curve $- R \leq x \leq R , z = R e ^ { i \theta } , 0 \leq \theta \leq \pi$ , where $R > a$

The residue of the integrand at $z = i a$ is

$$
\frac { i a e ^ { - a } } { 2 i a } = \frac { e ^ { - a } } { 2 } .
$$

Moreover, by “Jordan’s lemma”, the integral over the semicircular part of the curve tends to 0 as $R \to \infty$

Therefore $I = { \textstyle \frac { 1 } { 2 } } \cdot \operatorname { I m } ( 2 \pi i e ^ { - a } / 2 ) = { \textstyle \frac { \pi e ^ { - a } } { 2 } }$

7B. Let $\mathbb { F } _ { p }$ be the field of p elements. Let $\operatorname { S L } _ { 2 } ( \mathbb { F } _ { p } )$ be the group of $2 \times 2$ matrices over $\mathbb { F } _ { p }$ of determinant 1. Let G be a normal subgroup of $\dot { \mathrm { S L } } _ { 2 } ( \mathbb { F } _ { p } )$ . Suppose G contains a non-identity element $\gamma$ that fixes a nonzero vector v. Show that any $\gamma ^ { \prime } \in \mathrm { S L } _ { 2 } ( \mathbb { F } _ { p } )$ that fixes a nonzero vector $v ^ { \prime }$ belongs to $G .$

Solution: For each vector u, let $S _ { u }$ be the set of elements of $\operatorname { S L } _ { 2 } ( \mathbb { F } _ { p } )$ that fix u. First, we can complete {v} to a basis $\{ v , w \}$ . With respect to this basis, the matrix of $\gamma$ is uppertriangular and hence is

$$
\left( { \begin{array} { l l } { 1 } & { x } \\ { 0 } & { 1 } \end{array} } \right)
$$

for some $x \neq 0$ . Then $S _ { v }$ (where now $v = { \binom { 1 } { 0 } } )$ consists of the powers $\gamma ^ { k } = { \binom { 1 } { 0 } } \quad k x \quad $ , so $S _ { v } \subseteq G$

Now suppose $v ^ { \prime } : = { \binom { a } { c } } \in \mathbb { F } _ { p } ^ { 2 } \backslash 0$ . Then we can find $b , d \in \mathbb { F } _ { p }$ so that $a d - b c = 1$ (take $d = 0$ and $c = - 1 / b$ or $c = 0$ and $d = 1 / a )$ . Thus

$$
\rho : = { \binom { a \quad b } { c \quad d } } \in \mathrm { S L } _ { 2 } ( \mathbb { F } _ { p } )
$$

satisfies $\rho \boldsymbol { v } = \boldsymbol { v } ^ { \prime }$ . Now $S _ { v ^ { \prime } } = \rho S _ { v } \rho ^ { - 1 } \subseteq \rho G \rho ^ { - 1 } = G$ , which is what we needed to show.

Remark: Many students confused $\mathrm { S L _ { 2 } } ( \mathbb { F } _ { p } ) – \mathrm { c o n j u g a c y }$ with similarity, which is $\operatorname { G L } _ { 2 } ( \mathbb { F } _ { p } ) .$ conjugacy.

8B. Let $f : \mathbb { R } \to \mathbb { R }$ be differentiable on R. Suppose that $f ( 0 ) = 0$ , and that $| f ^ { \prime } ( x ) | \leq | f ( x ) |$ for all $x \in \mathbb { R }$ . Prove that $f ( x ) = 0$ for all $x \in \mathbb { R }$

Solution: Let us show that $f ( x ) = 0$ for all $x \in [ 0 , 1 ]$ . Let $a = \operatorname* { m a x } \{ | f ( x ) | : x \in [ 0 , 1 ] \}$ . We have to show that $a = 0$ . Suppose on the contrary $a > 0$ . Let $E = \{ x \in [ 0 , 1 ] : | f ( x ) | = a \}$ Then E is closed and $\alpha =$ inf $E \in E$ , i.e., $| f ( \alpha ) | = a > 0 \Rightarrow \alpha > { \dot { 0 } }$ since $f ( 0 ) = 0$ . Thus $0 < \alpha \leq 1$ and $| f ( c ) | < a ( * )$ for all $0 \leq c < \alpha$ . We have $a = | f ( \alpha ) | = | f ( \alpha ) - f ( 0 ) | = | f ^ { \prime } ( c ) | \cdot \alpha$ (for some $c \in ( 0 , \alpha )$ by the Mean Value ${ \mathrm { T h e o r e m } } ) \leq | f ( c ) | \cdot \alpha \leq | f ( c ) |$ (since $0 < \alpha \le 1 )$ . This contradicts (∗). Thus $f \equiv 0$ on [0, 1]. In particular, $f ( 1 ) = 0$ and we can use the same argument to show $f \equiv 0 \mathrm { { o n } \ [ 1 , 2 ] }$ and on every $[ n , n + 1 ] , n = \pm 1 , \pm 2 , . . .$

Alternative solution: Suppose $f ( x )$ is not identically zero. Replacing f (x) by $\pm f ( \pm x )$ we may assume that there exists $b > 0$ such that $f ( b ) > 0$ . Let $a = \operatorname* { s u p } \{ x \in [ 0 , b ] : f ( x ) = 0 \}$ .

Thus f is positive on $( a , b )$ . So $f ^ { \prime } \leq f$ on $( a , b )$ . Thus the derivative of $g = e ^ { - x } f { \mathrm { ~ i s ~ } } \leq 0$ on $( a , b )$ . This contradicts $g ( a ) = 0 < g ( b )$

9B. (a) Prove that if $n > 0$ is even, there does not exist $f ( x ) \in \mathbb { R } [ x ]$ such that $f ( x ) ^ { 2 } - x$ is divisible by $x ^ { n } - 1$

(b) For odd $n > 0$ , find the number of $f ( x ) \in \mathbb { R } [ x ]$ of degree $< n$ such that $f ( x ) ^ { 2 } - x$ is divisible by $x ^ { n } - 1$

Solution: (a) If $f ( x ) ^ { 2 } - x$ is divisible by $x ^ { n } - 1$ , it is divisible by the factor $x + 1$ , so $f ( - 1 ) ^ { 2 } - ( - 1 ) = 0$ . This is impossible since $f ( - 1 ) \in \mathbb { R }$ .

(b) Equivalently, we must count the square roots of the image of x in $\mathbb { R } [ x ] / ( x ^ { n } - 1 )$ . If n is odd, only one zero of $x ^ { n } - 1$ is real, so $\begin{array} { r } { x ^ { n } - 1 = ( x - 1 ) \prod _ { i = 1 } ^ { ( n - 1 ) / 2 } f _ { j } ( x ) } \end{array}$ where $f _ { j } ( x ) \in \mathbb { R } [ x ]$ is irreducible of degree 2. Moreover, the factors are distinct, since $x ^ { n } - 1$ shares no zeros with its derivative $n x ^ { n - 1 }$ . By the Chinese Remainder Theorem,

$$
\mathbb { R } [ x ] / ( x ^ { n } - 1 ) \simeq \frac { \mathbb { R } [ x ] } { ( x - 1 ) } \times \prod _ { j = 1 } ^ { ( n - 1 ) / 2 } \frac { \mathbb { R } [ x ] } { ( f _ { j } ( x ) ) } \simeq \mathbb { R } \times \prod _ { j = 1 } ^ { ( n - 1 ) / 2 } \mathbb { C } .
$$

To choose a square root of the image of x is equivalent to choosing a square of the image of $x$ in each factor. The image of x in the factor R is 1, and the image in each factor C is nonzero (since x has an inverse in $\mathbb { R } [ x ] / ( x ^ { n } - 1 )$ , namely $x ^ { n - 1 } )$ , so there are 2 choices of square root in each of the $( n + 1 ) / 2$ factors. Thus the answer is $2 ^ { ( n + 1 ) / 2 }$

Alternative solution to (b): By Lagrange interpolation, a polynomial $f ( x ) \in \mathbb { C } [ x ]$ of degree $< n$ is uniquely specified by its values at the n-th roots of unity. Such a specification gives a polynomial with real coefficients if and only if the prescribed values at complex conjugate roots of unity are complex conjugates. Now $f ( x ) ^ { 2 } - x$ is divisible by $x ^ { n } - 1$ if and only if $f ( w )$ is a square root of w for each n-th root of unity w. We can construct such $f$ by prescribing $f ( 1 ) = \pm 1$ and $f ( w )$ for each n-th root of unity in the upper half plane, but then we must choose $f ( \overline { { w } } ) = \overline { { f ( w ) } }$ . There are $( n - 1 ) / 2 \ n { \mathrm { - t h } }$ roots of unity in the upper half plane, so we have $1 + ( n - 1 ) / 2 = ( n + 1 ) / 2$ sign choices. Thus there are $2 ^ { ( n + 1 ) / 2 }$ possibilities for $f$