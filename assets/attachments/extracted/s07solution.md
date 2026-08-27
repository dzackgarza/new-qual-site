## SPRING 2007 PRELIMINARY EXAMINATION SOLUTIONS

1A. Let $x _ { 1 } , x _ { 2 } , . . .$ . be an infinite sequence of real numbers such that every subsequence contains a subsequence converging to 0. Must the original sequence converge?

Solution: Yes; in fact it must converge to 0. If not, there would exist $\epsilon > 0$ such that for infinitely many n, we have $| x _ { n } | > \epsilon$ Choose a subsequence $S$ consisting of such $x _ { n }$ . If $T$ is a subsequence of S, then T also consists of numbers of absolute value greater than , so $T$ cannot converge to 0. Thus S has no subsequence converging to 0. This contradicts the given hypothesis.

2A. Find a matrix U such that $U ^ { - 1 } A U = J$ is in Jordan canonical form, where

$$
A = \left( { \begin{array} { r r r } { 0 } & { - 3 } & { 5 } \\ { - 1 } & { - 6 } & { 1 1 } \\ { 0 } & { - 4 } & { 7 } \end{array} } \right) .
$$

Solution: Expanding by minors along the first column shows that the characteristic determinant is given by

$$
\operatorname* { d e t } ( A - \lambda I ) = - \lambda ^ { 3 } + \lambda ^ { 2 } + \lambda - 1 = - ( \lambda - 1 ) ^ { 2 } ( \lambda + 1 ) .
$$

Thus $\lambda _ { 1 } = - 1$ is an eigenvalue of algebraic (and hence geometric) multiplicity 1 while $\lambda _ { 2 } = 1$ is an eigenvalue of algebraic multiplicity 2. The eigenvectors of A belong to the kernels of the matrices

$$
A - \lambda _ { 1 } I = \left( { \begin{array} { r r r } { 1 } & { - 3 } & { 5 } \\ { - 1 } & { - 5 } & { 1 1 } \\ { 0 } & { - 4 } & { 8 } \end{array} } \right) , \qquad A - \lambda _ { 2 } I = \left( { \begin{array} { r r r } { - 1 } & { - 3 } & { 5 } \\ { - 1 } & { - 7 } & { 1 1 } \\ { 0 } & { - 4 } & { 6 } \end{array} } \right) ,
$$

which can be row-reduced to

$$
P _ { 1 } ( A - \lambda _ { 1 } I ) = \left( { \begin{array} { r r r } { 1 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { - 2 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) , \qquad P _ { 2 } ( A - \lambda _ { 2 } I ) = \left( { \begin{array} { r r r } { 1 } & { 0 } & { - 1 / 2 } \\ { 0 } & { 1 } & { - 3 / 2 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right) ,
$$

where $P _ { 1 }$ and $P _ { 2 }$ are products of elementary row operations. We see that $u _ { 1 } = ( 1 , 2 , 1 ) ^ { T }$ and $u _ { 2 , 0 } = ( 1 , 3 , 2 ) ^ { T }$ are the eigenvectors of A and the geometric multiplicity of $\lambda _ { 2 }$ is 1. To put A in Jordan canonical form, we want $A ( u _ { 1 } , u _ { 2 , 0 } , u _ { 2 , 1 } ) = A U = U J = ( \lambda _ { 1 } u _ { 1 } , \lambda _ { 2 } u _ { 2 , 0 } , \lambda _ { 2 } u _ { 2 , 1 } + u _ { 2 , 0 } )$ so we need to find a vector $u _ { 2 , 1 }$ satisfying $A u _ { 2 , 1 } = \lambda _ { 2 } u _ { 2 , 1 } + u _ { 2 , 0 }$ . This can be done by solving $P _ { 2 } ( A - \lambda _ { 2 } I ) u _ { 2 , 1 } = P _ { 2 } u _ { 2 , 0 } .$

$$
\begin{array} { r l r } { ( \begin{array} { c c c } { - 1 } & { - 3 } & { 5 } \\ { - 1 } & { - 7 } & { 1 1 } \\ { 0 } & { - 4 } & { 6 } \end{array} ) \xrightarrow { 1 } ) \quad } & { \mathrm { r o w ~ r e d u c e ~ } } & { ( \begin{array} { c c c } { 1 } & { 0 } & { - 1 / 2 } \\ { 0 } & { 1 } & { - 3 / 2 } \\ { 0 } & { 0 } & { 0 } \end{array} | \begin{array} { c } { 1 / 2 } \\ { - 1 / 2 } \\ { 0 } \end{array} ) . } \end{array}
$$

Thus $u _ { 2 , 1 } = ( 1 , 1 , 1 ) ^ { T }$ works (as does $( 1 , 1 , 1 ) ^ { T } + \alpha ( 1 , 3 , 2 ) ^ { T }$ for any $\alpha \in \mathbb { C } )$ and we have

$$
\begin{array}{c} U = { \binom { 1 } { 2 } } \ 3 \ 1  \\ { 1 \ 2 \ 1 } \end{array}  \qquad U ^ { - 1 } A U = J = { ( \begin{array} { l l l } { - 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 1 } \end{array} ) } \ .
$$

3A. Suppose $f : \mathbb { R } \to \mathbb { R }$ is real analytic and periodic with period $2 \pi$ . Prove that $f$ has an analytic continuation F defined on a strip

$$
S = \{ x + i y \in \mathbb { C } ~ : ~ | y | < \rho \}
$$

with $\rho > 0$ , and that $F ( z + 2 \pi ) = F ( z )$ for $z \in S$

Solution: Since f is real analytic, it possesses derivatives of all orders and agrees with its (convergent) Taylor series on a neighborhood $( x - r _ { x } , x + r _ { x } )$ of every point $x \in \mathbb { R }$ . The same power series may be used to define F on the complex neighborhood $B ( x , r _ { x } )$ of radius $r _ { x }$ centered at x. Since $f$ is periodic, the coefficients of the Taylor series at $x + 2 \pi$ are the same as those at $x ,$ so we may assume that $r _ { x + 2 \pi } = r _ { x }$ for all $x \in \mathbb { R }$ . Let us cover the compact interval $[ - \pi , \pi ] \subset \mathbb { C }$ with open squares $\begin{array} { r } { U _ { x } = \left( x - \frac { 1 } { 2 } r _ { x } , x + \frac { 1 } { 2 } r _ { x } \right) \times \left( - \frac { 1 } { 2 } r _ { x } , \frac { 1 } { 2 } r _ { x } \right) } \end{array}$ and choose a finite sub-cover $U _ { x _ { 1 } } , . . . , U _ { x _ { n } } \mathrm { o f } [ - \pi , \pi ]$ . We now define

$$
\rho = \operatorname* { m i n } \left\{ { \frac { 1 } { 2 } } r _ { x _ { i } } : 1 \leq i \leq n \right\}
$$

and note that since each square $U _ { x _ { i } }$ has half-height $\geq \rho$ and satisfies $U _ { x _ { i } } \subset B ( x _ { i } , r _ { x _ { i } } )$ , the balls $\{ B ( x _ { i k } , r _ { x _ { i } } ) : x _ { i k } = x _ { i } + 2 \pi k , 1 \leq i \leq n , k \in \mathbb { Z } \}$ cover the strip S. For any $z \in S$ , we define $F ( z )$ using the Taylor series at any $x _ { i k }$ for which $z \in B ( x _ { i k } , r _ { x _ { i } } )$ . A different choice of $x _ { i k }$ will yield the same value $F ( z )$ since the intersection of two balls containing z will contain a positive interval of the real axis on which the Taylor expansions agree with $f ,$ s o they represent the same analytic function on this intersection. F satisfies $F ( z + 2 \pi ) = F ( z )$ for $z \in S$ since the Taylor expansion centered at $x _ { i k }$ defining F at $z \in B ( x _ { i k } , r _ { x _ { i } } )$ has the same coefficients as the one centered at $x _ { i , k + 1 }$ defining $F$ at $z + 2 \pi$

4A. Define six fields as follows:

• Let $A = \mathbb { Q } ( \alpha )$ where $\mathbb { Q }$ is the field of rational numbers and α is the real cube root of 2.

• Let B be a splitting field of $x ^ { 3 } - 2$ over $\mathbb { Q }$

• Let C be an algebraic closure of the field $\mathbb { F } _ { 2 }$ of 2 elements.

• Let D be the subfield of C generated over $\mathbb { F } _ { 2 }$ by the set of $a \in C$ such that there exists $n \geq 1$ with $a ^ { n } = 1$ .

• Let E be the field R of real numbers.

• Let F be the field $\mathbb { Q } [ [ T ] ( T ^ { - 1 } )$ of formal Laurent series with rational coefficients.

For each pair of these, determine with proof whether or not they are isomorphic.

Solution: We will show that the only isomorphic pair consists of $C$ and $D$

Let $S _ { 1 } = \{ A , B \} , S _ { 2 } = \{ C , D \}$ , and $S _ { 3 } = \{ E , F \}$ The fields in $S _ { 1 }$ are of finite dimension over Q, hence countable and of characteristic 0. The fields in $S _ { 2 }$ are of characteristic 2. The fields in $S _ { 3 }$ are uncountable and of characteristic 0. Hence no field in $S _ { i }$ is isomorphic to a field in $S _ { j }$ if $i \neq j$ .

By Eisenstein’s criterion, $x ^ { 3 } - 2$ is irreducible, so $\left[ A : \mathbb { Q } \right] = 3$ . The zeros of this polynomial are $\omega ^ { i } \alpha$ where ω is a primitive cube root of unity. Thus $\omega \in B$ . Since $[ \mathbb { Q } ( \omega ) : \mathbb { Q } ] = 2$ , the degree $\left[ B : \mathbb { Q } \right]$ is even. Hence $A \not \simeq B$

If $a \in C$ , then $\mathbb { F } _ { 2 } ( a )$ is a finite extension of $\mathbb { F } _ { 2 }$ , hence finite, say of order $q ;$ if moreover $a \neq 0$ , then $a ^ { q - 1 } = 1$ . Hence $C \subseteq D$ . But $D \subseteq C$ , so $C = D$

The square of a nonzero element of $\mathbb { Q } [ [ T ] ( T ^ { - 1 } )$ has a leading coefficient that is a rational square. Thus 2 is not a square in $\mathbb { Q } [ [ T ] ] ( T ^ { - 1 } )$ . But 2 is a square in R. So $E \not \simeq F$

$\mathrm { 5 A }$ . Let $a _ { 0 } ( x ) , a _ { 1 } ( x ) , \dots , a _ { r - 1 } ( x )$ and $b ( x )$ be $C ^ { m }$ functions on R. Prove that if $y ( x )$ is a solution of the differential equation

$$
y ^ { ( r ) } + a _ { r - 1 } ( x ) y ^ { ( r - 1 ) } + \cdot \cdot \cdot + a _ { 1 } ( x ) y ^ { \prime } + a _ { 0 } ( x ) y = b ( x )
$$

(in particular, assuming that the derivatives $y ^ { \prime } , y ^ { \prime \prime } , \ldots , y ^ { ( r ) }$ exist), then $y ( x )$ is $C ^ { m + r }$

Solution: Rewrite the differential equation as

$$
y ^ { ( r ) } = b - \left( a _ { r - 1 } y ^ { ( r - 1 ) } + \cdot \cdot \cdot + a _ { 1 } y ^ { \prime } + a _ { 0 } y \right) ,\tag{1}
$$

and proceed by induction on m. For $m = 0$ , the derivatives of $y$ on the right-hand side of (1) are differentiable and hence continuous. The functions $a _ { i }$ and b are continuous by assumption, so $y ^ { ( r ) }$ is continuous, $i . e . , y$ is $C ^ { r }$

For $m > 0$ , assume by induction that y is $C ^ { m + r - 1 }$ Then the derivatives of y on the right-hand side of (1) are $C ^ { m }$ . The functions $a _ { i }$ and b are $C ^ { m }$ by assumption, so $y ^ { ( r ) }$ is $C ^ { m }$ hence y is $C ^ { m + r }$

6A. Let $A = \alpha _ { 1 } \sigma _ { 1 } + \alpha _ { 2 } \sigma _ { 2 } + \alpha _ { 3 } \sigma _ { 3 }$ where $\alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } \in \mathbb { C }$ and $\sigma _ { 1 } = { \binom { 0 } { 1 } } , 1 ) , \sigma _ { 2 } = { \binom { 0 } { i } } \quad 0 \quad$ $\sigma _ { 3 } = { \binom { 1 } { 0 } } \ { \_ { - 1 } } )$ . Let $\beta \in \mathbb { C }$ be any square root of $\alpha _ { 1 } ^ { 2 } + \alpha _ { 2 } ^ { 2 } + \alpha _ { 3 } ^ { 2 }$

(a) Prove that $\begin{array} { r } { \exp ( A ) = \cosh ( \beta ) + \frac { \sinh \beta } { \beta } A } \end{array}$ , where $\frac { \sinh ( \beta ) } { \beta }$ is interpreted as 1 if $\beta = 0$ . (Hint: First show that $A ^ { 2 }$ is a scalar multiple of the identity.)

(b) Evaluate exp(A) explicitly in the case $\alpha _ { 1 } = i \pi , \alpha _ { 2 } = i \pi$ , and $\alpha _ { 3 } = \pi$

Solution: (a) An explicit calculation shows that $A ^ { 2 } = ( \alpha _ { 1 } ^ { 2 } + \alpha _ { 2 } ^ { 2 } + \alpha _ { 3 } ^ { 2 } ) I = \beta ^ { 2 } I$ . Thus

$$
{ \begin{array} { r l } & { \exp ( A ) = I + A + { \cfrac { 1 } { 2 ! } } A ^ { 2 } + { \cfrac { 1 } { 3 ! } } A ^ { 3 } + \cdots } \\ & { ~ = I + A + { \cfrac { \beta ^ { 2 } } { 2 ! } } I + { \cfrac { \beta ^ { 2 } } { 3 ! } } A + { \cfrac { \beta ^ { 4 } } { 4 ! } } I + { \cfrac { \beta ^ { 4 } } { 5 ! } } A + \cdots } \\ & { ~ = \cosh ( \beta ) + { \cfrac { \sinh \beta } { \beta } } A , } \end{array} }
$$

where the last step is valid (with our convention) even if $\beta = 0$

(b) The values $\alpha _ { 1 } = i \pi , \alpha _ { 2 } = i \pi , \alpha _ { 3 } = \pi \mathrm { g i v e } \beta ^ { 2 } = - \pi ^ { 2 }$ , so we choose $\beta = i \pi$ and obtain cosh $( \beta ) = \cos ( i \beta ) = \cos ( - \pi ) = - 1 , \sinh ( \beta ) = - i \sin ( i \beta ) = - i \sin ( - \pi ) = 0$ , and $\exp ( A ) = - I$

7A. Let a and b be complex numbers, and let $f \colon \mathbb { C } \to \mathbb { C }$ be a non-constant entire function such that $f ( a z + b ) = f ( z )$ for all $z \in \mathbb { C }$ . Prove that there is a positive integer n such that $a ^ { n } = 1$

Solution: If $a = 1$ , we are done, so assume that $a \neq 1$ . Then $a z + b = z$ has a unique solution, say c. Define $g ( z ) : = f ( z + c )$ , so

$$
g ( a z ) = f ( a z + c ) = f ( a z + a c + b ) = f ( a ( z + c ) + b ) = f ( z + c ) = g ( z ) .
$$

If the Taylor series of $g ( z )$ at z = 0 is $\textstyle \sum _ { i \geq 0 } g _ { i } z ^ { i }$ , then equating coefficients of $z ^ { n }$ in $g ( a z ) =$ $g ( z )$ yields

$$
a ^ { n } g _ { n } = g _ { n } .
$$

Since $f$ is not constant, g is not constant. Therefore for some $n \geq 1$ we have $g _ { n } \neq 0$ , and hence $a ^ { n } = 1$

8A. Let $n \geq 3$ , and let $A _ { n }$ be the alternating subgroup of the symmetric group on n letters. Prove that $A _ { n }$ is generated by (123) and $( 1 2 \cdots n )$ if n is odd, or by (123) and $( 2 \cdots n )$ if n is even.

Solution: We prove the statement by induction on n. The base case $n = 3$ is trivial.

Let G be the subgroup of $A _ { n }$ generated by these elements. Then G acts transitively on $\{ 1 , \ldots , n \}$ , so it suffices to show that the stabilizer of 1 in G is the full alternating group on $\{ 2 , \ldots , n \}$ . By induction we need only show for $n \geq 4$ that G contains (234) and either $( 3 \cdots n ) { \mathrm { ~ } } ( { \mathrm { i f ~ } } n$ is odd) or $( 2 \cdots n )$ (if n is even).

Case 1: n is odd. Then conjugating (123) by (12 · · · n) yields $( 2 3 4 ) \in G$ . And

$$
( 3 \cdot \cdot \cdot n ) = ( 1 2 3 ) ^ { - 1 } ( 1 2 \cdot \cdot \cdot n ) \in G .
$$

Case 2: n is even. Then conjugating (123) by $( 2 \cdots n )$ yields $( 1 3 4 ) \in G$ , and conjugating (123) by (134) yields $( 3 2 4 ) \in G$ , and hence $( 2 3 4 ) = ( 3 2 4 ) ^ { - 1 } \in G$ . This time, $( 2 \cdots n ) \in G$ is part of the inductive hypothesis.

9A. Suppose b and L are positive constants and $f : [ 0 , b ] \to \mathbb { R }$ is continuous and satisfies

$$
f ( x ) \geq L \int _ { 0 } ^ { x } f ( t ) d t , \qquad ( 0 \leq x \leq b ) .
$$

Show that $f ( x ) \geq 0$ for $0 \leq x \leq b .$

Solution: Let $\textstyle F ( x ) = \int _ { 0 } ^ { x } f ( t ) d t$ . Since f is continuous, F is differentiable and we have

$$
F ^ { \prime } ( x ) = f ( x ) \geq L F ( x ) , \qquad ( 0 \leq x \leq b ) .
$$

Thus, for $0 \leq t \leq b$ we have

$$
F ^ { \prime } ( t ) - L F ( t ) \geq 0 ,
$$

$$
\begin{array} { r } { \big ( F ^ { \prime } ( t ) - L F ( t ) \big ) e ^ { - L t } \geq 0 , } \end{array}
$$

$$
\frac { d } { d t } \Big ( F ( t ) e ^ { - L t } \Big ) \geq 0 ,
$$

and since definite integrals preserve inequalities:

$$
F ( x ) e ^ { - L x } - F ( 0 ) e ^ { 0 } = \int _ { 0 } ^ { x } { \frac { d } { d t } } { \Big ( } F ( t ) e ^ { - L t } { \Big ) } d t \geq \int _ { 0 } ^ { x } 0 d t = 0 , \quad ( 0 \leq x \leq b ) .
$$

Since $F ( 0 ) = 0$ and $e ^ { - L x } > 0$ , we learn that $F ( x ) \geq 0 { \mathrm { ~ f o r ~ } } 0 \leq x \leq b$ , hence the original inequality $f ( x ) \geq L F ( x )$ gives the desired result.

An alternative proof might run as follows. Let $x _ { 0 } = \operatorname* { s u p } \{ x < b ~ : ~ f ( t ) \geq 0$ for $t \in [ 0 , x ] \}$ We know $x _ { 0 } \geq 0$ since $f ( 0 ) \geq 0$ . We must show that $x _ { 0 } = b$ Suppose to the contrary that $x _ { 0 } < b$ . Since $f ( x )$ is continuous and non-negative to the left of $x _ { 0 } , f ( x _ { 0 } ) \geq 0$ . On the other hand, there are points $x > x _ { 0 }$ arbitrarily close to $x _ { 0 }$ at which $f ( x ) < 0$ . Thus $f ( x _ { 0 } ) = 0$ . The given inequality now implies that $f ( x ) = 0$ for $0 \leq x \leq x _ { 0 }$ . Now define $x _ { 1 } = \operatorname* { m i n } ( x _ { 0 } + L ^ { - 1 } , b )$ Then there is an $x _ { 2 }$ in the interval $x _ { 0 } < x _ { 2 } < x _ { 1 }$ which satisfies $f ( x _ { 2 } ) < 0$ . Let $\varepsilon = | f ( x _ { 2 } ) |$ The given inequality implies that $\begin{array} { r } { f ( x ) \geq L \int _ { x _ { 0 } } ^ { x } f ( t ) } \end{array}$ dt for $x _ { 0 } \leq x \leq x _ { 1 }$ . Thus $u ( x ) = f ( x ) + \varepsilon$ satisfies $u ( x _ { 0 } ) = \varepsilon , u ( x _ { 2 } ) = 0$ , and

$$
u ( x ) \geq L \int _ { x _ { 0 } } ^ { x } u ( t ) - \varepsilon d t + \varepsilon = \int _ { x _ { 0 } } ^ { x } u ( t ) d t + \varepsilon [ 1 - L ( x - x _ { 0 } ) ] \geq \int _ { x _ { 0 } } ^ { x } u ( t ) d t
$$

for $x _ { 0 } \leq x \leq x _ { 1 }$ But since u is continuous and $u ( x _ { 0 } ) = \varepsilon > 0$ , it’s impossible for u to reach 0 over the interval $x _ { 0 } < x < x _ { 1 }$ , for at the first crossing $x _ { 3 }$ where $u ( x _ { 3 } ) = 0$ , the integral $\textstyle \int _ { x _ { 0 } } ^ { x _ { 3 } } u ( x ) d x > 0$ . Thus the assumption that $u ( x _ { 2 } ) = 0$ leads to a contradiction, and we conclude that $x _ { 0 } = b$

1B. If $c \in \mathbb { R }$ , say that a real-valued function $f : \mathbb { R } \to \mathbb { R }$ is periodic with period c if it satisfies $f ( x + c ) = f ( x )$ for all $x \in \mathbb { R }$

(i) Let V be the set of continuous real-valued functions f having a positive integer as a period. Prove that V is a vector space.

(ii) Let $p _ { 1 } < p _ { 2 } < . . . < p _ { n } < . . .$ . be the sequence of prime numbers, and for each $i ,$ let $f _ { i }$ be a function whose minimal positive period is $p _ { i }$ . Prove that the functions $f _ { 1 } , f _ { 2 } , \ldots$ . are linearly independent in V .

Solution: (i) The set of all functions $\mathbb { R } \to \mathbb { R }$ is a vector space, so it suffices to check that V contains 0 and is closed under addition and scalar multiplication. The only nontrivial claim is closure under addition. Suppose $f , g \in V$ , say with periods c and d. Any positive integer multiple of a period is a period of the same function, so $f , g$ have cd as a common period. Thus $f + g$ has cd as a period (and it is continuous).

(ii) Suppose not. Then there exists a relation

$$
a _ { 1 } f _ { 1 } + \cdots + a _ { n } f _ { n } = 0
$$

where $a _ { i } \in \mathbb { R }$ and $a _ { n } \neq 0$ Solving for $f _ { n }$ shows that $f _ { n }$ has $p _ { 1 } p _ { 2 } \cdots p _ { n - 1 }$ as a period. It also has $p _ { n }$ as a period. Now $p _ { 1 } p _ { 2 } \cdots p _ { n - 1 }$ and $p _ { n }$ are relatively prime, so 1 is an integer combination of $p _ { 1 } p _ { 2 } \cdots p _ { n - 1 }$ and $p _ { n }$ . Any integer combination of periods is a period, so in particular 1 is also a period of $f _ { n }$ . This contradicts the hypothesis that $p _ { n }$ is the minimal period of $f _ { n }$

2B. Given any real number $a _ { 0 }$ , define $a _ { 1 } , a _ { 2 } , \dotsc$ . by the rule $a _ { n + 1 } = \cos a _ { n }$ for all $n \geq 0$ . Prove that the sequence $\left( a _ { n } \right)$ converges, and that the limit is the unique solution of the equation $\cos x = x$

Solution: Let $g ( x ) = \cos x - x$ . Then $g ( 1 ) < 0$ , and since cos x is decreasing on $[ 0 , \pi ]$ , we have cos $; ( 1 / 2 ) > \cos ( \pi / 3 ) = 1 / 2$ , that is, $g ( 1 / 2 ) > 0$ By the Intermediate Value Theorem, there exists $1 / 2 < a < 1$ such that cos $a = a$ . To see that this a is the unique solution of $\cos x = x$ , observe first that any solution must clearly lie in $[ - 1 , 1 ]$ . On $[ - 1 , 0 )$ we have $x < 0 <$ cos x, so all solutions lie in [0, 1]. But $g ( x )$ is strictly decreasing on [0, 1], so the solution is unique.

Consider any function f which is differentiable and satisfies $| f ^ { \prime } ( x ) | < c$ for all x in an interval $( a - d , a + d )$ , where $c < 1$ 1, and $f ( a ) = a$ . For any $a _ { 0 } \in ( a - d , a + d )$ define a sequence $\left( a _ { n } \right)$ by $a _ { n + 1 } = f ( a _ { n } )$ . It follows easily by induction on n using the Mean Value Theorem that $| a _ { n + 1 } - a | < c | a _ { n } - a |$ for all n, hence $\left( a _ { n } \right)$ converges to a.

We’ll apply this with $f ( x ) = \cos x .$ , a the solution of cos $a = a$ , and $d = 1 / 2$ . Note that $[ a - d , a + d ] \subseteq ( 0 , 3 / 2 ) \subseteq ( 0 , \pi / 2 )$ since $a \in ( 1 / 2 , 1 )$ , and therefore $\cos ^ { \prime } ( x ) | = | \sin x | < c$ for some $c < 1$

The given sequence $\left( a _ { n } \right)$ satisfies $a _ { 1 } \in [ - 1 , 1 ]$ , hence $a _ { 2 } \in [ \cos ( 1 ) , 1 ] \subseteq [ 1 / 2 , 1 ] \subseteq ( a -$ $1 / 2 , a + 1 / 2 )$ . We conclude that $( a _ { 2 } , a _ { 3 } , \ldots )$ converges to a.

3B. Let k and l be positive integers. Let $\mathbb { Q } ( x ) ( { \sqrt [ k ] { 1 - x ^ { l } } } )$ be any extension field of $\mathbb { Q } ( x )$ generated by a k-th root of $1 - x ^ { l }$ . Define $\mathbb { Q } ( x ) ( { \sqrt { 1 - x ^ { k } } } )$ similarly. Prove that $\mathbb { Q } ( x ) ( { \sqrt [ k ] { 1 - x ^ { l } } } )$ and $\mathbb { Q } ( x ) ( { \sqrt [ { l ] { 1 - x ^ { k } } } } )$ are isomorphic.

Solution: The polynomial $y ^ { k } + x ^ { l } - 1$ is irreducible, for any positive integers k, l. One way to prove this is to regard $y ^ { k } + x ^ { l } - 1$ as a polynomial in y over $\mathbb { Q } [ x ]$ and apply Eisenstein’s criterion, using the fact that $x - 1$ divides $x ^ { l } - 1$ but $( x - 1 ) ^ { 2 }$ does not. It follows that the fields in question are the fraction fields of $\mathbb { Q } [ x , y ] / ( y ^ { k } + x ^ { l } - 1 )$ and $\mathbb { Q } [ x , y ] / ( y ^ { l } + x ^ { k } - 1 )$ , respectively, which are obviously isomorphic by the exchange of x and $y .$

4B. Let E be the C-vector space of entire functions. Let V be a nonzero finite-dimensional C-subspace of E with the property that $f \in V$ implies $f ^ { \prime } \in V$ . Prove that V contains a function that is everywhere nonzero.

Solution: The map $T \colon V \to V$ sending f to $f ^ { \prime }$ is a linear transformation. Since V is a C-vector space, there exists an eigenvalue $\lambda \in \mathbb { C }$ . Let $f \in V$ be a corresponding (nonzero) eigenvector. Then $f ^ { \prime } = \lambda f$ , so $f ( z ) = c e ^ { \lambda z }$ for some $c \in \mathbb { C } ^ { \times }$ . This function is everywhere nonzero.

5B. Let $\mathbb { F } _ { q }$ denote the finite field with q elements, where q is a power of a prime. Let $\mathrm { S L } _ { n } ( \mathbb { F } _ { q } )$ be the group of $n \times n$ matrices with entries in $\mathbb { F } _ { q }$ and determinant 1, under matrix multiplication. Determine (with proof) a simple necessary and sufficient condition on n and $q$ for the center of $\mathrm { S L } _ { n } ( \mathbb { F } _ { q } )$ to be trivial.

Solution: Let $E _ { i j }$ denote the $n \times n$ matrix with $( i , j )$ entry equal to 1 and all other entries zero. For $i \neq j$ , we have $I _ { n } + E _ { i j } \in \mathrm { S L } _ { n } ( \mathbb { F } _ { q } )$ . A matrix A commutes with $I _ { n } + E _ { i j }$ if and only if $E _ { i j } A = A E _ { i j }$ . The latter condition implies that $A _ { j k } = 0$ for $k \neq j$ , that $A _ { k i } = 0$ for $k \neq i ,$ and that $A _ { i i } = A _ { j j }$ . If this holds for all $i \neq j$ , then $A = x I _ { n }$ is a scalar multiple of the identity, and we have $\overset { \cdot \mathrm { ~ \tiny ~ . ~ } } { A } \in \mathrm { S L } _ { n } ( \mathbb { F } _ { q } )$ if and only if $x ^ { n } = 1$ in $\mathbb { F } _ { q }$

The multiplicative group $\mathbb { F } _ { q } ^ { \times }$ is cyclic, so the necessary and sufficient condition for $x = 1$ to be the unique solution of $x ^ { n } = 1$ in $\mathbb { F } _ { q }$ is that $q - 1$ and n are relatively prime.

6B. Let U be a non-empty open subset of $\mathbb { R } ^ { d }$ and let $f : U \to \mathbb { R } ^ { d }$ be a continuous vector field defined on U. Let $K$ be a compact subset of U and let $b > 0$ . Suppose $\varphi : [ 0 , b ) \to K$ is a continuous function satisfying

$$
\varphi ( t ) = \varphi ( 0 ) + \int _ { 0 } ^ { t } f ( \varphi ( s ) ) d s , \qquad ( 0 \leq t < b ) .
$$

Prove that $\operatorname* { l i m } _ { t  b ^ { - } } \varphi ( t )$ exists, where $t \to b ^ { - }$ means t approaches b from the left.

Solution: Let $M = \operatorname* { s u p } _ { y \in K } \| f ( y ) \|$ . For any two points $t _ { 1 } , t _ { 2 } \in [ 0 , b )$

$$
\| \varphi ( t _ { 2 } ) - \varphi ( t _ { 1 } ) \| = \Big \| \int _ { t _ { 1 } } ^ { t _ { 2 } } f ( \varphi ( t ) ) d t \Big \| \leq M | t _ { 2 } - t _ { 1 } |
$$

so $\varphi$ is Lipschitz continuous on [0, b) and hence preserves Cauchy sequences. Let $t _ { k } \to b$ from the left. Then $\varphi ( t _ { k } )$ is Cauchy and hence converges to some $y _ { 0 } ~ \in ~ \mathbb { R } ^ { d }$ . We claim that $\begin{array} { r } { \operatorname* { l i m } _ { t \to b ^ { - } } \varphi ( t ) = y _ { 0 } } \end{array}$ Let $\varepsilon > 0$ and choose k large enough that $\begin{array} { r } { | t _ { k } - b | < \frac { \varepsilon } { M + 1 } } \end{array}$ and $\begin{array} { r } { \| \varphi ( t _ { k } ) - y _ { 0 } \| < \frac { \varepsilon } { M + 1 } } \end{array}$ . Then for $\begin{array} { r } { 0 < b - t < \delta = \frac { \varepsilon } { M + 1 } } \end{array}$ we have

$$
\begin{array} { c } { \displaystyle \| \varphi ( t ) - y _ { 0 } \| \le \| \varphi ( t ) - \varphi ( t _ { k } ) \| + \| \varphi ( t _ { k } ) - y _ { 0 } \| } \\ { \displaystyle \le M | t - t _ { k } | + \frac { \varepsilon } { M + 1 } \le \varepsilon } \end{array}
$$

as required.

Alternative solution, based on a suggestion of Andre Kornell (using the dominated convergence theorem of Lebesgue integration, however): Because of the given integral equation, it suffices to apply the following claim to the function $g ( s ) ~ = ~ f ( \varphi ( s ) )$ : for any continuous bounded function $g \colon [ 0 , b )   { \mathbb { R } } ^ { d }$ , the limit lim $\begin{array} { r } { \mathbf { \ i } _ { t  b ^ { - } } \int _ { 0 } ^ { t } g ( s ) } \end{array}$ ds exists. To prove this, it suffices to prove that for every increasing sequence $\left( t _ { k } \right)$ i n $[ 0 , b )$ tending to $b ,$ the limit $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { t _ { k } } g ( s ) } \end{array}$ ds exists. This follows from the dominated convergence theorem applied to the sequence of functions

$$
g _ { k } ( s ) : = { \left\{ \begin{array} { l l } { g ( s ) , } & { { \mathrm { ~ i f ~ } } s \in [ 0 , t _ { k } ] } \\ { 0 , } & { { \mathrm { ~ i f ~ } } s \in ( t _ { k } , b ] . } \end{array} \right. }
$$

7B. Given any group G, define a binary operation ∗ on the set $H = G \times G$ by $( g _ { 1 } , h _ { 1 } ) *$ $( g _ { 2 } , h _ { 2 } ) = ( g _ { 1 } g _ { 2 } , g _ { 2 } ^ { - 1 } h _ { 1 } g _ { 2 } h _ { 2 } )$

(a) Show that $( H , * )$ is group.

(b) In the case that G is the alternating group $A _ { n }$ on n letters with $n \geq 5$ , prove that H has no subgroup of index 2.

Solution: (a) $( H , * )$ is the semidirect product $G \ltimes G$ where $G$ acts on itself by conjugation.

(b) By the solution to part (a), H contains a normal subgroup N such that $N \cong H / N \cong$ $A _ { n }$ . Since $A _ { n }$ is simple, the Jordan-H¨older theorem implies that $H / M \cong A _ { n }$ for every nontrivial proper normal subgroup $M \subseteq H$ . In particular, H cannot have a subgroup M of index 2, since such a subgroup is always normal.

(Alternatively, one could “avoid” the Jordan-H¨older theorem by essentially proving it in the special case needed, considering first the intersection of M with N, and then the image of M in $H / N . )$

8B. Let A be the set of $z \in \mathbb { C }$ such that $| z | \leq 1$ , Im $( z ) \geq 0$ , and $z \not \in \{ 1 , - 1 \}$ . Find an explicit continuous function u : $A \to \mathbb { R }$ such that

• u is harmonic on the interior of A,

$u ( z ) = 3 { \mathrm { ~ f o r ~ } } z \in A \cap \mathbb { R }$

• u(z) = 7 for z in the intersection of A with the unit circle.

Solution: We use a conformal transformation to reduce to a problem on a different region. The transformation $w = f ( z )$ where $f ( z ) : = ( 1 + z ) / ( 1 - z )$ maps the interval $( - 1 , 1 )$ to $( 0 , \infty )$ and maps the upper half of the unit circle to the ray from $f ( - 1 ) = 0 { \mathrm { ~ t o ~ } } f ( 1 ) = \infty$ passing through $f ( i ) = i$ It therefore maps A to the first quadrant or its complement (ignoring boundaries); that it is the former can be determined by calculating $f ( i / 2 )$ , or by observing the orientation of the image of the path from −1 to 1.

Let $Q = f ( A )$ , so Q is the closed first quadrant minus the origin. The function Im log w (where we use the standard branch of log) is a continuous function on $Q _ { i }$ , harmonic on the interior, whose values along the positive real and imaginary axes are 0 and $\pi / 2$ , respectively, so $\textstyle 3 + { \frac { 8 } { \pi } }$ Im log w is harmonic on the interior of Q and has the values 3 and 7 along those axes. Substituting $w = f ( z )$ , we find that

$$
u = 3 + { \frac { 8 } { \pi } } \operatorname { I m } \log \left( { \frac { 1 + z } { 1 - z } } \right)
$$

is a solution.

9B. Let k and n be integers with $n \geq k \geq 0$ Let A and B be $n \times k$ matrices with real coefficients. Let At be the transpose of A. For each size-k subset $I \subseteq \{ 1 , \ldots , n \}$ , let $A _ { I }$ be the $k \times k$ matrix obtained by discarding all rows of A except those whose index belongs to I. Define $B _ { I }$ similarly. Prove that

$$
\operatorname* { d e t } ( A ^ { t } B ) = \sum _ { I } \operatorname* { d e t } ( A _ { I } ) \operatorname* { d e t } ( B _ { I } ) ,
$$

where the sum is over all size-k subsets $I \subseteq \{ 1 , \ldots , n \}$ . (Suggestion: use linearity to reduce to the case where the columns of A and B are particularly simple.)

Solution: Let $a _ { i }$ be the i-th column vector of A. Let $b _ { j }$ be the j-th column vector of B. Let $e _ { 1 } , \ldots , e _ { n }$ be the standard basis of $\mathbb { R } ^ { n }$ . Both sides of the identity are linear in each $a _ { i }$ and $b _ { j }$ , so we may assume that each column is a standard basis vector, say $\boldsymbol a _ { i } = \boldsymbol e _ { f ( i ) }$ and $b _ { j } = e _ { g ( j ) }$ Then $A ^ { t } B$ is the matrix whose ij-entry is $a _ { i } ^ { t } b _ { j }$ , which is 1 if $f ( i ) = g ( j )$ and 0 otherwise.

If $f ( 1 ) , \ldots , f ( k )$ are not all different, then $A ^ { t } B$ has a repeated row, and every $A _ { I }$ has a repeated column, so both sides of the desired identity are 0. So assume that the $f ( i )$ are all different.

Similarly, if $g ( 1 ) , \ldots , g ( k )$ are not all different, then $A ^ { t } B$ has a repeated column, and every $B _ { I }$ has a repeated column, so both sides of the desired identity are $0 .$ . So assume that the $g ( j )$ are all different.

If $I \ne \{ f ( 1 ) , \ldots , f ( k ) \}$ , then $A _ { I }$ has fewer than k nonzero entries, so det $A _ { I } \ = \ 0$ . If $I \neq \{ g ( 1 ) , \ldots , g ( k ) \}$ , then $B _ { I }$ has fewer than k nonzero entries, so det $B _ { I } = 0$

Suppose that $\{ f ( 1 ) , \ldots , f ( k ) \} \neq \{ g ( 1 ) , \ldots , g ( k ) \}$ . Then $A ^ { t } B$ has fewer than k nonzero entries. But also, by the previous paragraph, for every I, either det $A _ { I }$ or det $B _ { I }$ is 0. Thus the desired identity holds.

Finally, suppose that $\{ f ( 1 ) , \ldots , f ( k ) \} \ = \ \{ g ( 1 ) , \ldots , g ( k ) \}$ Let $S$ be this common $k -$ element subset of $\{ 1 , \ldots , n \}$ Then $A ^ { t } B = ( A _ { S } ) ^ { t } ( B _ { S } )$ , so the left hand side of the identity equals det $( A _ { S } )$ det(BS). If $I \neq S$ , then det $\left( A _ { I } \right) \operatorname* { d e t } ( B _ { I } ) = 0$ , so the right hand side of the identity equals det $( A _ { S } )$ det(BS) too.