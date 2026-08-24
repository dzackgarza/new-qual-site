Then for such n, we have

$$
\begin{array} { r l } { \displaystyle | \displaystyle \int _ { | z | = 1 } z ^ { n } f ( z ) d \mu ( z ) | \leqslant \displaystyle \int _ { | z | = 1 } | z ^ { n } ( f ( z ) - g ( z ) ) | d \mu ( z ) + \displaystyle \int _ { | z | = 1 } | z ^ { n } ( g ( z ) - P ( z ) ) | d \mu ( z ) + \displaystyle \iint _ { | z | = 1 } z ^ { n } P ( z ) d \mu ( z ) | } & { } \\ { \displaystyle \leqslant \displaystyle \int _ { | z | = 1 } | f ( z ) - g ( z ) | d \mu ( z ) + \displaystyle \int _ { | z | = 1 } | g ( z ) - P ( z ) | d \mu ( z ) + \epsilon } & { } \\ { \displaystyle \leqslant \ \| f - g \| _ { L ^ { 1 } ( \mu ) } + \| g - P \| _ { L ^ { \infty } ( \mu ) } \mu ( S ^ { 1 } ) + \epsilon < 3 \epsilon , } & { } \end{array}
$$

which shows that $\textstyle { \int _ { | z | = 1 } z ^ { n } f ( z ) d \mu ( z ) \to 0 }$ as n Ñ 8.

Problem 3. Let H be a Hilbert space and let E be a closed convex subset of H. Prove that there exists a unique element $x \in E$ such that

$$
| | x | | \ = \ \operatorname* { i n f } _ { y \in E } | | y | | .
$$

Solution.
First note that if $0 \in E$ , then the statement is obviously true by taking $x = 0$ , so assume $0 \notin E$ Let $\begin{array} { r } { \operatorname* { i n f } _ { y \in E } | | y | | = \delta > 0 } \end{array}$ . First we prove that such an x must be unique.
Suppose that $\vert \vert x \vert \vert = \vert \vert x ^ { \prime } \vert \vert = \delta$ . Then since E is convex, we have $( 1 / 2 ) x + ( 1 / 2 ) x ^ { \prime } \in E$ and

$$
\delta \ = \ \frac 1 2 \left| | x | \right| + \frac 1 2 \left| \left| x ^ { \prime } \right| \right| \ = \ \left\| \frac 1 2 x \right\| + \left\| \frac 1 2 x ^ { \prime } \right\| \ \geqslant \ \left\| \frac 1 2 x + \frac 1 2 x ^ { \prime } \right\| \ \geqslant \delta .
$$

But we know that equality in the triangle inequality occurs if and only if x and $x ^ { \prime }$ are scalar multiples of each other.
Thus the above inequality yields the contradiction $\delta > \delta$ unless x and $x ^ { \prime }$ are scalar multiples of each other.
So we can write ˇˇ ˇˇ $\boldsymbol { x } = c \boldsymbol { x } ^ { \prime }$ where $| c | = 1$ . Then since E is convex, $( 1 / 2 ) ( x + x ^ { \prime } ) = { \textstyle { \frac { c + 1 } { 2 } } } x ^ { \prime } \in E$ also, so $\begin{array} { r } { \left| \left| \frac { c + 1 } { 2 } x ^ { \prime } \right| \right| = \left| ( c + 1 ) / 2 \right| \delta \geqslant \delta , } \end{array}$ which implies $c = 1$ , so $x = x ^ { \prime }$

Now we show existence.
Let $\left\{ y _ { n } \right\}$ be a sequence in E such that $| | y _ { n } | |  \delta$ as $n  \infty$ . Then for any n and $m _ { \colon }$ , by the parallelogram law we can write

$$
\left| \left| \frac { 1 } { 2 } y _ { n } + \frac { 1 } { 2 } y _ { m } \right| \right| ^ { 2 } + \left| \left| \frac { 1 } { 2 } y _ { n } - \frac { 1 } { 2 } y _ { m } \right| \right| ^ { 2 } ~ = ~ 2 \left| \left| \frac { 1 } { 2 } y _ { n } \right| \right| ^ { 2 } + 2 \left| \left| \frac { 1 } { 2 } y _ { m } \right| \right| ^ { 2 } .
$$

Since E is convex, $( 1 / 2 ) y _ { n } + ( 1 / 2 ) y _ { m } \in E .$ , so we have

$$
\frac 1 4 \left| | y _ { n } - y _ { m } | \right| ^ { 2 } = \frac 1 2 \left| | y _ { n } | \right| ^ { 2 } + \frac 1 2 \left| | y _ { m } | \right| ^ { 2 } - \left| \left| \frac 1 2 y _ { n } + \frac 1 2 y _ { m } \right| \right| ^ { 2 } \leqslant \frac 1 2 \left| | y _ { n } | \right| ^ { 2 } + \frac 1 2 \left| | y _ { m } | \right| ^ { 2 } - \delta ^ { 2 } .
$$

As $n , m  \infty$ , the right side of the above inequality tends to 0 by definition of the $y _ { n } .$ , so we conclude that $| | y _ { n } - y _ { m } | | ^ { 2 }  0$ as $n , m  \infty .$ 8, so $\left\{ y _ { n } \right\}$ is a Cauchy sequence.
Since H is complete, there is some $x \in H$ such that $y _ { n } \to x$ as $n  \infty .$ , and since E is closed, we must have $x \in E$ . Finally, since the norm is a continuous function on H, we must have $\begin{array} { r } { | | x | | = \operatorname* { l i m } _ { n  \infty } | | y _ { n } | | = \delta } \end{array}$ .

Problem 4. Fix $f \in C ( \mathbb { T } )$ where $\mathbb { T } = \mathbb { R } / 2 \pi \mathbb { Z }$ . Let $s _ { n }$ denote the nth partial sum of the Fourier series of $f .$ . Prove that

$$
\operatorname* { l i m } _ { n \to \infty } \frac { | | s _ { n } | | _ { L ^ { \infty } ( \mathbb { T } ) } } { \log ( n ) } = 0 .
$$

Solution.
Recall that we have $s _ { n } ( f ) ( x ) = ( f * D _ { n } ) ( x )$ , where $D _ { n }$ is the Dirichlet kernel

$$
D _ { n } ( t ) \ = \ \sum _ { k = - n } ^ { n } e ^ { i k t } \ = \ { \frac { \sin ( ( n + 1 / 2 ) t ) } { \sin ( t / 2 ) } } .
$$

Therefore we immediately see that $| | s _ { n } ( f ) | | _ { L ^ { \infty } } \leqslant | | f | | _ { L ^ { \infty } } | | D _ { n } | | _ { L ^ { 1 } }$ . We estimate

$$
| | D _ { n } | | _ { L ^ { 1 } } ~ \lesssim ~ \int _ { - \pi } ^ { \pi } \left| \frac { \sin ( ( n + 1 / 2 ) t ) } { \sin ( t / 2 ) } \right| d t ~ \lesssim ~ \int _ { 0 } ^ { \pi } \left| \frac { \sin ( ( n + 1 / 2 ) t ) } { t } \right| d t
$$

where the second inequality is valid because $D _ { n }$ is even and sin $( t / 2 ) \geqslant t / 1 0 0$ on $[ 0 , \pi ]$ . Continuing,

$$
\begin{array} { r l r } {  { \vert \vert D _ { n } \vert \vert _ { L ^ { 1 } } } } \\ & { \lesssim } & { \int _ { 0 } ^ { ( n + 1 / 2 ) \pi } \frac { \vert \sin ( u ) \vert } { u } d u \ \lesssim \ \sum _ { k = 0 } ^ { n } \int _ { k \pi } ^ { ( k + 1 ) \pi } \frac { \vert \sin ( u ) \vert } { u } d u } \\ & { } & { \lesssim \ \sum _ { k = 0 } ^ { n } \int _ { k \pi } ^ { ( k + 1 ) \pi } \frac { \vert \sin ( u ) \vert } { ( k + 1 ) \pi } d u \ \lesssim \ \sum _ { k = 0 } ^ { n } \frac { 1 } { k + 1 } \ \lesssim \ \log ( n ) . } \end{array}
$$

So we have established $| | s _ { n } ( f ) | | _ { L ^ { \infty } } \ \lesssim \ | | f | | _ { L ^ { \infty } } \log ( n )$ for all $f \in C ( \mathbb { T } )$ Note that if P is a polynomial, then $s _ { n } ( P ) \to P$ uniformly on T (this is proven by integrating by parts twice on the definition of the Fourier coefficients to get $| \hat { P } ( k ) | \lesssim k ^ { - 2 }$ , and then applying the Weierstrass M-test combined with the general fact that $s _ { n } ( P ) \to P$ in $L ^ { 2 } )$ . In particular, $| | s _ { n } ( P ) | | _ { L ^ { \infty } }$ is bounded, so we clearly have $| | s _ { n } ( P ) | | _ { L ^ { \infty } } / \log ( n ) \to 0$ Fix $\epsilon > 0$ and any $f \in C ( \mathbb { T } )$ . We can find a polynomial P with $\| f - P \| _ { L ^ { \infty } } < \epsilon$ . Then we have

$$
\operatorname* { l i m s u p } _ { n \to \infty } \frac { | | s _ { n } ( f ) | | _ { L ^ { \infty } } } { \log ( n ) } \leqslant \operatorname* { l i m s u p } _ { n \to \infty } \frac { | | s _ { n } ( f - P ) | | _ { L ^ { \infty } } } { \log ( n ) } + \frac { | | s _ { n } ( P ) | | _ { L ^ { \infty } } } { \log ( n ) } \leqslant | | f - P | | _ { L ^ { \infty } } < \epsilon .
$$

Take $\epsilon \to 0$ and we’re done.

Problem 5. Let $f _ { n } : \mathbb { R } ^ { 3 } \to \mathbb { R }$ be a sequence of functions such that sup $_ n \| f _ { n } \| _ { L ^ { 2 } } < \infty$ . Show that if $f _ { n }$ converges almost everywhere to a function $f : \mathbb { R } ^ { 3 }  \mathbb { R }$ , then

$$
\int _ { \mathbb { R } ^ { 3 } } \left| | f _ { n } | ^ { 2 } - | f _ { n } - f | ^ { 2 } - | f | ^ { 2 } \right| d x \ \to \ 0 .
$$

Solution.
Let M be such that $\vert \vert f _ { n } \vert \vert _ { L ^ { 2 } } \leqslant M$ for all n. Since $f _ { n }  f$ almost everywhere, we also have $| f _ { n } | ^ { 2 } \to | f | ^ { 2 }$ almost everywhere, so by Fatou’s lemma,

$$
\int | f | ^ { 2 } \ = \ \int \operatorname * { l i m i n f } _ { n \to \infty } | f _ { n } | ^ { 2 } \ \leqslant \ \operatorname* { l i m i n f } _ { n \to \infty } \int | f _ { n } | ^ { 2 } \ \leqslant \ M ^ { 2 } ,
$$

which shows that $f \in L ^ { 2 }$ and $| | f | | _ { L ^ { 2 } } \leqslant M$ . Notice that we have the identity

$$
| | f _ { n } | ^ { 2 } - | f _ { n } - f | ^ { 2 } - | f | ^ { 2 } | \ = \ | | f _ { n } - f + f | ^ { 2 } - | f _ { n } - f | ^ { 2 } - | f | ^ { 2 } | \ = \ 2 | f _ { n } - f | | f | .
$$

Fix $\epsilon > 0$ . Since $| f | ^ { 2 }$ is integrable, there is a ş $\delta > 0$ such that $\lambda ( E ) < \delta$ implies $\int _ { E } | f | ^ { 2 } < \epsilon$ . We can also pick an R which is big enough so that $\int _ { | x | > R } | f | ^ { 2 } < \epsilon$ . Then on the set $| x | \leqslant R$ , we can apply Egorov’s theorem to get a set $E \subseteq \left\{ | x | \leqslant R \right\}$ such that ${ \dot { f } } _ { n }  f$ uniformly on $\{ | x | \leqslant R \} \backslash E$ and $\lambda ( E ) < \delta .$ . So we have the estimate

$$
\int | f _ { n } - f | | f | ~ = ~ \int _ { \{ | x | \leq R \} \backslash E } | f _ { n } - f | | f | + \int _ { E } | f _ { n } - f | | f | + \int _ { \{ | x | > R \} } | f _ { n } - f | | f | ~ = : ~ A + B + C .
$$

Since $f _ { n }  f$ uniformly on $\{ | x | \leqslant R \} \backslash E$ , let n be big enough so that $\int _ { \{ | x | \leqslant R \} \backslash E } | f _ { n } - f | ^ { 2 } < \epsilon$ . Now we estimate each of $A , B , C$ separately using Cauchy-Schwarz.
We have

$$
A ~ \leqslant ~ \left( \int _ { \{ | x | \leqslant R \} \backslash E } | f _ { n } - f | ^ { 2 } \right) ^ { 1 / 2 } \left( \int _ { \{ | x | \leqslant R \} \backslash E } | f | ^ { 2 } \right) ^ { 1 / 2 } ~ \leqslant ~ M \sqrt { \epsilon }
$$

$$
B ~ \leqslant ~ \left( \int _ { E } | f _ { n } - f | ^ { 2 } \right) ^ { 1 / 2 } \left( \int _ { E } | f | ^ { 2 } \right) ^ { 1 / 2 } ~ \leqslant ~ \sqrt { 2 M ^ { 2 } } \sqrt { \epsilon }
$$

$$
C \ \leqslant \ \left( \int _ { \{ | x | > R \} } | f _ { n } - f | ^ { 2 } \right) ^ { 1 / 2 } \left( \int _ { \{ | x | > R \} } | f | ^ { 2 } \right) ^ { 1 / 2 } \ \leqslant \ { \sqrt { 2 M ^ { 2 } } } { \sqrt { \epsilon } } .
$$

This shows that $\int | f _ { n } - f | | f | \to 0 { \mathrm { ~ a s ~ } } n \to \infty$ , which is enough to conclude the desired result.

Problem 6. Let $f \in L ^ { 1 } ( \mathbb { R } )$ and let Mf denote its maximal function, that is,

$$
( M f ) ( x ) \ = \ \operatorname * { s u p } _ { 0 < r < \infty } { \frac { 1 } { 2 r } } \int _ { - r } ^ { r } | f ( x - y ) | d y .
$$

By the Hardy-Littlewood maximal function theorem,

$$
| \{ x \in \mathbb { R } : ( M f ) ( x ) > \lambda \} | \ \leqslant \ 3 \lambda ^ { - 1 } | | f | | _ { L ^ { 1 } } \quad \mathrm { ~ f o r ~ a l l ~ } \lambda > 0 .
$$

Using this show that

$$
\operatorname* { l i m } _ { r \to 0 } \operatorname* { s u p } _ { 2 r } \int _ { - r } ^ { r } | f ( y ) - f ( x ) | d y \ = \ 0 \quad { \mathrm { f o r ~ a l m o s t ~ e v e r y ~ } } x \in \mathbb { R } .
$$

Solution.
This is actually false as stated.
As a counterexample, take $f = \chi _ { [ - 1 , 1 ] }$ s. For any $x \notin [ - 1 , 1 ]$ , we have $f ( x ) = 0$ but

$$
\operatorname* { l i m s u p } _ { r \to 0 } { \frac { 1 } { 2 r } } \int _ { - r } ^ { r } | f ( y ) - f ( x ) | d y \ = \ \operatorname* { l i m s u p } _ { r \to 0 } { \frac { 1 } { 2 r } } \int _ { - r } ^ { r } | f ( y ) | d y \ = \ 1 .
$$

Presumably, what the question meant to say is to prove that

$$
\operatorname* { l i m } _ { r \to 0 } \operatorname* { s u p } _ { 2 r } \int _ { x - r } ^ { x + r } | f ( y ) - f ( x ) | d y \ = \ 0 \quad { \mathrm { f o r ~ a l m o s t ~ e v e r y ~ } } x \in \mathbb { R } ,
$$

which is the Lebesgue differentiation theorem.
Here is a proof of this:

Define

$$
\begin{array} { r c l } { ( T _ { r } f ) ( x ) } & { : = } & { \displaystyle \frac { 1 } { 2 r } \int _ { x - r } ^ { x + r } | f ( y ) - f ( x ) | d y } \\ { ( T f ) ( x ) } & { : = } & { \displaystyle \operatorname* { l i m } _ { r \to 0 ^ { + } } ( T _ { r } f ) ( x ) . } \end{array}
$$

We want to prove that $T f = 0$ almost everywhere.
Fix some $\epsilon > 0$ Since the set of continuous functions with compact support is dense in $L ^ { 1 } ( \mathbb { R } )$ , let g be a continuous function with compact support such that $| | f - g | | _ { L ^ { 1 } } < \epsilon$ . Define $h = f - g$ so that $f = g + h $ h. Note that for any $r > 0$ we have

$$
T _ { r } f \ = \ T _ { r } ( g + h ) \ \leqslant \ T _ { r } g + T _ { r } h .
$$

By the definition of continuity, it is clear that the desired result holds for continuous functions, so we have that $T g$ is identically zero, and thus we obtain $T f \leqslant T h$

To show that $T f = 0$ almost everywhere, it suffices to show that m $\{ x \in \mathbb { R } : ( T f ) ( x ) > \delta \} = 0$ for any fixed $\delta > 0$ , where m is Lebesgue measure on R. So fix $\delta > 0$ and define $F : = \{ x \in \mathbb { R } : ( T f ) ( x ) > \delta \}$ and $E : = \{ x \in \mathbb { R } : ( T h ) ( x ) > \delta \}$ . Since $T f \leqslant T h , F \subseteq E$ , so we analyze the measure of E. Note that for any x and any $r > 0$ , we have

$$
( T _ { * } h ) ( x ) \ = \ { \frac { 1 } { 2 r } } \int _ { x - r } ^ { x + r } \left| h ( y ) - h ( x ) \right| d y \ \leqslant \ { \frac { 1 } { 2 r } } \int _ { x - r } ^ { x + r } \left| h ( y ) \right| d y + { \frac { 1 } { 2 r } } \int _ { x - r } ^ { x + r } \left| h ( x ) \right| d y \ \leqslant \ ( M h ) ( x ) + \left| h ( x ) \right| .
$$

Therefore we have

$$
E \subseteq \{ x \in \mathbb { R } : ( M h ) ( x ) > \delta / 2 \} \cup \{ x \in \mathbb { R } : | h ( x ) | > \delta / 2 \} ,
$$

so by the Hardy-Littlewood theorem, Chebyshev’s inequality, and the definition of $h ,$

$$
m ( E ) \ \leqslant \ \frac { 6 } { \delta } \| h \| _ { L ^ { 1 } } + \frac { 2 } { \delta } \| h \| _ { L ^ { 1 } } \ < \ \frac { 8 } { \delta } \epsilon .
$$

Thus we have $m ( F ) < ( 8 / \delta ) \epsilon$ . Since the set $F$ does not depend on $\epsilon ,$ this holds for any $\epsilon > 0$ and thus we conclude $m ( F ) = 0 ;$ , which is enough to conclude that $T f = 0$ almost everywhere.
□

Problem 7. Let f be a function holomorphic in C and suppose that $f ( 0 ) = 0 , f ( 1 ) = 1$ , and $f ( \mathbb { D } ) \subseteq \mathbb { D } .$ Show that (a) $f ^ { \prime } ( 1 ) \in \mathbb { R }$ and $( \mathrm { b } ) \ f ^ { \prime } ( 1 ) \geqslant 1$

Solution.
(a) Suppose that $f ^ { \prime } ( 1 ) \not \in \mathbb { R }$ . Then there exists $v \in \mathbb { C }$ with $\mathrm { R e } ( v ) < 0$ such that $\mathrm { R e } ( f ^ { \prime } ( 1 ) v ) > 0$ The limit definition of the derivative, together with the fact that $f ( 1 ) = 1$ implies that

$$
f ^ { \prime } ( 1 ) v = \operatorname* { l i m } _ { t  0 ^ { + } } \frac { f ( 1 + t v ) - 1 } { t } .
$$

For sufficiently small t, we have $1 + t v \in \mathbb { D }$ . Since $f ( \mathbb { D } ) \subseteq \mathbb { D }$ , But then $\begin{array} { r } { \mathrm { R e } { \frac { f ( 1 + t v ) - 1 } { t } } < 0 } \end{array}$ small t. After passing to the limit, we have $\mathrm { R e } ( f ^ { \prime } ( 1 ) v ) \leqslant 0$ which is a contradiction.

(b) Fix $t \in ( 0 , 1 )$ . By the Schwarz lemma, $| f ( 1 - t ) | \leqslant 1 - t .$ . Therefore

$$
{ \frac { | f ( 1 - t ) - 1 | } { t } } \geqslant { \frac { 1 - | f ( 1 - t ) | } { t } } \geqslant 1 .
$$

Taking the limit as $t \to 0 ^ { + }$ , we see that $\left| f ^ { \prime } ( 1 ) \right| \geqslant 1$

Problem 8. Let $f : \mathbb { C } \to \mathbb { C }$ be a nonconstant holomorphic function such that every zero of f has even multiplicity.
Show that f has a holomorphic square root, i.e. there exists a holomorphic function $g : \mathbb { C } \to \mathbb { C }$ such that $f ( z ) = g ( z ) ^ { 2 }$ for all $z \in \mathbb { C }$

Solution.
If the set of zeros of f had a limit point, then f would have to be identically zero.
But f is nonconstant by hypothesis, so the zeros of f are isolated.
Since all of the multiplicities are even and the zeros are isolated, by Weierstrass’s theorem there exists an entire function h such that h has the same zeros as $f ,$ but with each one half the multiplicity.
Then $h ^ { 2 }$ is an entire function with exactly the same zeros as $f$ with all the same multiplicities.
Therefore the function $f / h ^ { 2 }$ is analytic at all points which are not zeros of $f ,$ , and it has removable singularities at the zeros of $f .$ So it can be extended to a function which is analytic everywhere, so we can assume without loss of generality that $f / h ^ { 2 }$ is a nonvanishing entire function.
Since it is nonvanishing, it has a well-defined analytic logarithm, i.e. there is some entire function g such that $f / h ^ { 2 } = \exp ( g )$ . Then $f = h ^ { 2 } \exp ( g ) = ( h \exp ( g / 2 ) ) ^ { 2 }$ , and $h \exp ( g / 2 )$ is an entire function, so this is the desired result.

Problem 9. Suppose f is a holomorphic function in the unit disk D and $\left\{ x _ { n } \right\}$ is a sequence of real numbers satisfying $0 < x _ { n + 1 } < x _ { n } < 1$ for all $n \in$ N and li $\begin{array} { r } { \mathfrak { n } _ { n \to \infty } x _ { n } = 0 } \end{array}$ . Show that if $f ( x _ { 2 n + 1 } ) = f ( x _ { 2 n } )$ for all $n ,$ then f is a constant function.

Solution.
By translating by a constant, we may assume that $f ( 0 ) = 0$ Define $g ( z ) ~ = ~ f ( z ) { \overline { { f ( { \overline { { z } } } ) } } }$ . Since $\overline { { f ( \overline { { z } } ) } }$ is also holomorphic, we see that g is also holomorphic and $g ( z ) \in \mathbb { R }$ whenever $z \in \mathbb { R } .$ . So we can consider the restriction of g to the positive real axis as a differential function on R. Then since $g ( x _ { 2 n + 1 } ) = g ( x _ { 2 n } )$ for all $n ,$ by the mean value theorem there is a number $y _ { n } \in \left( x _ { 2 n + 1 } , x _ { 2 n } \right)$ such that $g ^ { \prime } ( y _ { n } ) = 0$ . Since $x _ { n } \to 0 .$ , also $y _ { n } \to 0$ . Thus $g ^ { \prime }$ is zero on a set with a limit point, so $g ^ { \prime }$ is identically zero.
Therefore g is a constant, and since $f ( 0 ) = 0$ , we also have $g ( 0 ) = 0$ , so g is identically zero.
Therefore we have $f ( z ) { \overline { { f ( { \overline { { z } } } ) } } } = 0$ for all $z \in \mathbb { D }$ , which implies that $f$ is identically zero because either $f ( z )$ or $\overline { { f ( \overline { { z } } ) } }$ is zero on a set with a limit point.
□

Problem 10. Let $\left\{ f _ { n } \right\}$ be a sequence of holomorphic functions on D satisfying $| f _ { n } ( z ) | \leqslant 1$ for all z and all n Let $A \subseteq \mathbb { D }$ be the set of all $z \in \mathbb { D }$ for which the limit li $\mathrm { n } _ { n \to \infty } f _ { n } ( z )$ exists.
Show that if A has an accumulation point in D, then there exists a holomorphic function f on D such that $f _ { n }  f$ locally uniformly on D.

Solution.
Since the sequence $f _ { n }$ is uniformly bounded, by Montel’s theorem we know it is a normal family, so there is a subsequence $f _ { n _ { k } }$ which converges locally uniformly on D to some function $f .$ Since local uniform limits of holomorphic functions are holomorphic, we know that $f$ is holomorphic.
Now, to show that the whole sequence $f _ { n }$ converges locally uniformly to $f ,$ it suffices to prove that every subsequence has a further subsequence which converges locally uniformly to $f .$ Since the whole sequence is uniformly bounded, clearly any subsequence is also uniformly bounded, so by applying Montel’s theorem to the subsequence, we obtain a further subsequence which converges locally uniformly to some holomorphic function $g$ on D. But note that for every $z \in A$ , since the limit of the whole sequence $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( z )$ exists, any subsequences which converge pointwise at z must have the same limit.
This implies in particular, since local uniform convergence implies pointwise convergence, that $f ( z ) = g ( z )$ for $\mathrm { a l l } \ z \in A$ . Since A has a limit point in D and $f$ and g are both holomorphic, this implies that $f = g$ on D. Thus we conclude that any subsequence of $f _ { n }$ has a further subsequence converging locally uniformly to $f ,$ which implies that $f _ { n }$ converges locally uniformly to $f .$ .

Problem 11. Find all holomorphic functions $f : \mathbb { C } \to \mathbb { C }$ satisfying $f ( z + 1 ) = f ( z )$ and $f ( z + i ) = e ^ { 2 \pi } f ( z )$ for all $z \in \mathbb { C }$

Solution.
Note that $\exp ( - 2 \pi i z )$ is one such function.
Let $f : \mathbb { C } \to \mathbb { C }$ be any entire function satis $\mathrm { f y - }$ ing $f ( z + 1 ) = f ( z )$ and $f ( z + i ) = e ^ { 2 \pi } f ( z )$ for all $z \in \mathbb { C }$ . Define $g ( z ) = f ( z ) \exp ( 2 \pi i z )$ . Then $g$ is also an entire function and it satisfies

$$
\begin{array} { r c l } { { g ( z + 1 ) ~ = ~ f ( z + 1 ) \exp ( 2 \pi i ( z + 1 ) ) ~ = ~ f ( z ) \exp ( 2 \pi i z ) \exp ( 2 \pi i ) ~ = ~ g ( z ) } } \\ { { g ( z + i ) ~ = ~ f ( z + i ) \exp ( 2 \pi i ( z + i ) ) ~ = ~ e ^ { 2 \pi } f ( z ) \exp ( 2 \pi i z ) \exp ( - 2 \pi ) ~ = ~ g ( z ) . } } \end{array}
$$

Thus $g$ is a doubly periodic entire function, so it must be bounded and hence must be constant by Liouville’s theorem.
Thus we conclude that $f ( z ) = C \exp ( - 2 \pi i z )$ for some $C \in \mathbb { C }$ , and these are all of the functions $f$ which satisfy the desired property.

Problem 12a. Let $M \in \mathbb { R } , \Omega \subseteq \mathbb { C }$ be a bounded open set, and $u : \Omega \to \mathbb { R }$ be a harmonic function.
Show that if

$$
\operatorname* { l i m } _ { z \to z _ { 0 } } u ( z ) \ \leqslant \ M
$$

for all $z _ { 0 } \in \partial \Omega$ , then $u ( z ) \leqslant M$ for all $z \in \Omega$

Solution.
Fix $\epsilon > 0$ . By the limsup condition, for each $z _ { 0 } ~ \in ~ \partial \Omega$ , there is a radius $r ( z _ { 0 } )$ such that $| z - z _ { 0 } | < r ( z _ { 0 } )$ implies that $u ( z ) \leqslant M + \epsilon$ . Then the set

$$
\bigcup _ { z _ { 0 } \in \partial \Omega } B ( z _ { 0 } , r ( z _ { 0 } ) )
$$

is an open cover of $\partial \Omega .$ which is a compact set because $\Omega$ is bounded.
Therefore $\partial \Omega$ is covered by only finitely many of these balls.
Call them $B _ { 1 } , \ldots , B _ { N }$ . Now the set

$$
{ \cal A } \ = \ \Omega \backslash ( { \overline { { B _ { 1 } } } } \cup . . . \cup { \overline { { B _ { N } } } } )
$$

is an open set on which u is harmonic, extends continuously to the boundary, and satisfies $u ( w ) \leqslant M + \epsilon$ for all $w \in \partial A$ . Thus by the maximum principle, we conclude that $u ( z ) \leqslant M + \epsilon$ for all $z \in A .$ . By construction of $A ,$ we also know that $u ( z ) \leqslant M + \epsilon$ for all $z \in \Omega \backslash A$ , so we have $u ( z ) \leqslant M + \epsilon$ for all $z \in \Omega$ . Since this argument holds for any $\epsilon > 0$ we conclude that $u ( z ) \leqslant M$ for all $z \in \Omega$

Problem 12b. Show that if u is bounded from above and the above condition holds for all but finitely many $z _ { 0 } \in \partial \Omega$ , then it still follows that $u ( z ) \leqslant M$ for all $z \in \Omega$

Solution.
Since Ω is bounded, let $d = \mathrm { d i a m } ( \Omega ) = \mathrm { s u p } _ { z , w \in \Omega } | z - w | < \infty$ . Let $p _ { 1 } , \ldots , p _ { N }$ be the points in BΩ for which the limsup condition above does not hold.
Define the function

$$
v ( z ) : = - \log \left| \frac { z - p _ { 1 } } { d } \right| - \ldots - \log \left| \frac { z - p _ { N } } { d } \right| .
$$

Note that v is a nonnegative harmonic function in Ω because the function

$$
z \mapsto \left( { \frac { z - p _ { 1 } } { d } } \right) \cdots \left( { \frac { z - p _ { N } } { d } } \right)
$$

is a nonvanishing analytic function in Ω.

Fix $\epsilon > 0$ and define $f ( z ) ~ = ~ u ( z ) - \epsilon v ( z )$ For any $z _ { 0 } \in \partial \Omega \backslash \{ p _ { 1 } , . . . , p _ { N } \}$ , the limsup condition holds, and so as in the previous problem we have a radius $r ( z _ { 0 } )$ such that $| z - z _ { 0 } | < r ( z _ { 0 } )$ implies $u ( z ) \leqslant M + \epsilon .$ , and since $v \geqslant 0$ we also have $f ( z ) \leqslant M + \epsilon$ for all such z. However, for any $p _ { j } .$ , since u is bounded above and $v ( z ) \to \infty { \mathrm { ~ a s ~ } } z \to p _ { j }$ , there is also a radius $r ( j )$ such that $| z - p _ { j } | < r ( j )$ implies $f ( z ) \leqslant M + \epsilon .$ Now we proceed as in the previous problem.
Since $\partial \Omega$ is compact, it can be covered by finitely many of the balls $B ( z _ { 0 } , r ( z _ { 0 } ) )$ and $B ( p _ { j } , r ( j ) )$ . So we obtain a smaller set $A \subseteq \Omega$ on which $f$ is harmonic, extends continuously to the boundary, and satisfies $f ( w ) \leqslant M + \epsilon$ on the boundary of $A .$ . So by the maximum principle and by construction of $A$ we have $f ( z ) \leqslant M + \epsilon$ for all $z \in \Omega$ , i.e. $u ( z ) \leqslant M + \epsilon + \epsilon v ( z )$ for all $z \in \Omega$ . And this argument holds for any $\epsilon > 0$ , so we conclude that $u ( z ) \leqslant M$ for all $z \in \Omega$

## 9 Spring 2013

Problem 1. Suppose $f : \mathbb { R } \to \mathbb { R }$ is bounded, Lebesgue measurable, and

$$
\operatorname* { l i m } _ { h \to 0 } \int _ { 0 } ^ { 1 } { \frac { | f ( x + h ) - f ( x ) | } { h } } d x \ = \ 0 .
$$

Show that f is a.e. constant on r0, 1s.

Solution.
Let $F ( x ) = \int _ { 0 } ^ { x } f ( t ) d t$ . By the Lebesgue differentiation theorem, there is a set E of measure zero such that

$$
\operatorname* { l i m } _ { h \to 0 } { \frac { F ( x + h ) - F ( x ) } { h } } \ = \ f ( x )
$$

for all $x \notin E$ . Then for any $a , b \notin E$ , pick h small enough so that without loss of generality we have $a , a + h < b , b + h$ , then we have

$$
\begin{array} { r l } { \displaystyle | f ( a ) - f ( b ) | = } & { \displaystyle \operatorname* { l i m } _ { h \to 0 } \left| \frac { F ( a + h ) - F ( a ) } { h } - \frac { F ( b + h ) - F ( b ) } { h } \right| = \operatorname* { l i m } _ { h \to 0 } \frac { 1 } { h } \left| \int _ { a } ^ { b } f ( t ) d t - \int _ { a + h } ^ { b + h } f ( t ) d t \right| } \\ { \displaystyle } & { \leqslant \operatorname* { l i m } _ { h \to 0 } \frac { 1 } { h } \int _ { a + h } ^ { b + h } | f ( t + h ) - f ( t ) | d t \leqslant \operatorname* { l i m } _ { h \to 0 } \frac { 1 } { h } \int _ { 0 } ^ { 1 } | f ( t + h ) - f ( t ) | d t = 0 , } \end{array}
$$

so f is constant a.e.

Problem 2. Consider the Hilbert space $\ell ^ { 2 } ( \mathbb { Z } )$ Show that the Borel σ-algebra $\mathcal { N }$ on $\ell ^ { 2 } ( \mathbb { Z } )$ associated to the norm topology agrees with the Borel σ-algebra W on $\ell ^ { 2 } ( \mathbb { Z } )$ associated to the weak topology.

Solution.
Note: I’m pretty sure this argument still works if $\ell ^ { 2 } ( \mathbb { Z } )$ is replaced by any separable Hilbert space.

It’s known that the weak topology is coarser than the norm topology, so we automatically have $\mathcal { W } \subseteq \mathcal { N } .$ We just need to show that any norm-open set in $\ell ^ { 2 } ( \mathbb { Z } )$ is in W. Since $\ell ^ { 2 } ( \mathbb { Z } )$ with the norm topology is separable, any norm-open set is a countable union of open balls, so it suffices to show that every norm-open ball is in W. Fix $B ( x , \bar { r } ) = \{ y \in \ell ^ { 2 } ( \mathbb { Z } ) : | | y - x | | _ { \ell ^ { 2 } } ^ { 2 } < r ^ { 2 } \}$ . We can view this as a preimage $f ^ { - 1 } ( [ 0 , r ^ { 2 } ) )$ where $f : \ell ^ { 2 } ( \mathbb { Z } ) \to \mathbb { R }$ is given by

$$
f ( y ) \ : = \ | | y - x | | ^ { 2 } \ = \ | | y | | ^ { 2 } + | | x | | ^ { 2 } - 2 \operatorname { R e } \langle y , x \rangle \ = \ \sum _ { n = 1 } ^ { \infty } | \langle y , e _ { n } \rangle | ^ { 2 } + | | x | | ^ { 2 } - 2 \operatorname { R e } \langle y , x \rangle
$$

where $\left\{ \boldsymbol { e } _ { n } \right\}$ is an orthonormal basis for $\ell ^ { 2 } ( \mathbb { Z } )$ and we have used Parseval’s theorem.
We claim that this function is W-measurable.
This is because by definition of the weak topology, the function $y \mapsto \langle y , z \rangle$ is weak-continuous for any $z \in \ell ^ { 2 } ( \mathbb { Z } )$ and therefore W-measurable.
So the first term in $f$ is a countable sum of non-negative measurable functions, which is measurable (combination of the facts that g measurable implies $| g | ^ { 2 }$ measurable, sum of measurable functions is measurable, and pointwise limit of measurable functions is measurable).
The second term in f is a constant, which is measurable, and the third term in f is the real part of a measurable function, again measurable.
So f is a W-measurable function, and therefore $B ( x , r ) = f ^ { - 1 } ( [ 0 , r ^ { 2 } ) ) \in { \mathcal { W } } . \quad \sqsupset$

Problem 3. Given $f : \mathbb { R } ^ { 2 } $ R continuous, we define

$$
[ A _ { r } f ] ( x , y ) : = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( x + r \cos ( \theta ) , y + r \sin ( \theta ) ) d \theta
$$

and

$$
[ M f ] ( x , y ) : = \operatorname* { s u p } _ { 0 < r < 1 } [ A _ { r } f ] ( x , y ) .
$$

By a theorem of Borgain, there is an absolute constant C so that

$$
\vert \vert M f \vert \vert _ { L ^ { 3 } ( \mathbb { R } ^ { 2 } ) } \leqslant C \vert \vert f \vert \vert _ { L ^ { 3 } ( \mathbb { R } ^ { 2 } ) }
$$

for all $f \in C _ { c } ( \mathbb { R } ^ { 2 } )$ . Use this to show the following: If $K \subset \mathbb { R } ^ { 2 }$ is compact, then $[ A _ { r } \chi _ { K } ] ( x , y )  1$ as $r  0$ at almost every point $( x , y )$ in $K$ (with respect to Lebesgue measure).

Solution.
We would like to mimic the proof of the Lebesgue differentiation theorem.
This doesn’t work directly since we are only given Borgain’s result for continuous functions, so we start by expanding this result slightly.
In what follows $C$ will always denote an absolute constant which may change from line to line.

Claim.
Let S be a bounded open subset of $\mathbb { R } ^ { 2 }$ with $\lambda ( S ) < \infty$ . Then for $t > 0$ we have

$$
\lambda ( \{ ( x , y ) \in \mathbb { R } ^ { 2 } : [ M \chi s ] ( x , y ) > t \} ) \leqslant C \frac { \lambda ( S ) ^ { 3 } } { t ^ { 3 } } .
$$

Proof.
First note that the restriction of $\chi _ { S }$ to a circle is Borel measurable with respect to the uniform measure on the circle, since the restriction of an open set to a subset of $\mathbb { R } ^ { 2 }$ is open in the subspace topology.
So $[ M \chi _ { S } ]$ is defined.

Note that $\chi _ { S }$ is the characteristic function of an open set and is therefore lower semi-continuous.
Thust we may find an increasing sequence of functions $f _ { k } \in C _ { c } ( \mathbb { R } ^ { 2 } )$ converging monotonically to $\chi _ { S }$ . By replacing $f _ { k }$ with max $( f _ { k } , 0 )$ , we may assume that each $f _ { k }$ is non-negative.
From the weak-type $L ^ { 3 }$ estimate which follows from Borgain’s result, we have

$$
\lambda ( \{ ( x , y ) : [ M f _ { k } ] ( x , y ) > t \} ) \leqslant C t ^ { - 3 } \left| | f _ { k } | \right| _ { 3 } ^ { 3 } \leqslant C t ^ { - 3 } \left| | \chi s | \right| _ { 3 } ^ { 3 } = C t ^ { - 3 } \lambda ( S ) .
$$

If $[ M \chi _ { S } ] ( x , y ) > t .$ , then there exists $r \in ( 0 , 1 )$ such that $[ A _ { r } \chi _ { S } ] ( x , y ) > t .$ and by monotone convergence, we have $[ A _ { r } f _ { k } ] ( x , y ) > t$ for sufficiently large k. Since $M f _ { k }$ is an increasing sequence of functions, we can write

$$
\{ ( x , y ) : [ M \chi s ] ( x , y ) > t \} = \bigcup _ { k = 1 } ^ { \infty } \{ ( x , y ) : [ M f _ { k } ] ( x , y ) > t \} .
$$

Then applying continuity from below along with the earlier weak-type estimate gives

$$
\lambda ( \{ ( x , y ) : [ M \chi _ { S } ] ( x , y ) > t \} ) \leqslant C t ^ { - 3 } \left| \left| f \right| \right| _ { 3 } ^ { 3 } ,
$$

which proves the claim.

To prove the main result, we define

$$
S _ { n } = \{ ( x , y ) \in K : \operatorname * { l i m } _ { r \to 0 } \operatorname * { s u p } _ { } { | A _ { r } \chi _ { K } ( x , y ) - 1 | } > \frac { 1 } { n } \} .
$$

Next we fix $\epsilon > 0$ and approximate K by a bounded open set $U \supseteq K$ where $\lambda ( U \backslash K ) < \epsilon$ . Note that the stated theorem is true if we replaced K with U. For fixed $r \in ( 0 , 1 )$ and $( x , y ) \in K$ we have

$$
\begin{array} { r l } & { | A _ { r } \chi _ { K } ( x , y ) - 1 | \leqslant | A _ { r } \chi _ { K } ( x , y ) - A _ { r } \chi _ { U } ( x , y ) | + | A _ { r } \chi _ { U } ( x , y ) - 1 | | } \\ & { \qquad = \left[ A _ { r } \chi _ { U \backslash K } \right] ( x , y ) + \left| A _ { r } \chi _ { U } ( x , y ) - 1 \right| | } \\ & { \qquad \leqslant \left[ M \chi _ { U \backslash K } \right] ( x , y ) + \left| A _ { r } \chi _ { U } ( x , y ) - 1 \right| | . } \end{array}
$$

As $r \to 0$ the last term tends to $0 ,$ so if $( x , y )$ lies in $S _ { n }$ then $[ M \chi _ { U \backslash K } ] ( x , y ) > 1 / n$ . Note that $U \backslash K$ is open, so the claim applies and gives

$$
\lambda ^ { * } ( S _ { n } ) \leqslant C ( 1 / n ) ^ { - 3 } \lambda ( U \backslash K ) ^ { 3 } \leqslant C n ^ { 3 } \epsilon ^ { 3 } .
$$

But  was arbitrary, so $\lambda ^ { * } ( S _ { n } ) = \lambda ( S _ { n } ) = 0$ . Finally we have $\textstyle \lambda ( \bigcup _ { n = 1 } ^ { \infty } S _ { n } ) = 0$ , so

$$
\operatorname* { l i m } _ { r \to 0 } | A _ { r } \chi _ { K } ( x , y ) - 1 | = 0
$$

for a.e. $( x , y )$ in $K ,$ , and the main result follows.

Problem 4. Let K be a non-empty compact subset of $\mathbb { R } ^ { 3 }$ . For any Borel probability measure $\mu$ on $K .$ , define the Newtonian energy $I ( \mu ) \in ( 0 , + \infty ]$ by

$$
I ( \mu ) : = \int _ { K } \int _ { K } { \frac { 1 } { | x - y | } } d \mu ( x ) d \mu ( y )
$$

and let $R _ { K }$ be the infimum of $I ( \mu )$ over all Borel probability measures $\mu$ on $K$ . Show that there exists a Borel probability measure $\mu$ such that $I ( \mu ) = R _ { K }$

Solution.
Let M be the set of all Borel probability measures on $K$ By the Riesz representation theorem, M is a subset of the unit ball in the dual space $C ( K ) ^ { * }$ . Let $\mu _ { n }$ be a sequence in M with $I ( \mu _ { n } ) \to R _ { K }$ By the Banach-Alaoglu theorem, the unit ball in $C ( K ) ^ { * }$ is weak-˚ compact, and since $C ( K )$ is separable, it is also sequentially compact.
So by passing to a subsequence if necessary, we have a measure $\mu$ in the unit ball of $C ( K ) ^ { * }$ with $\mu _ { n }  \mu$ in weak-˚. By applying weak-˚ convergence to the constant function 1, we see that $\mu$ is also a probability measure on $K$

Now we claim that $I ( \mu ) = R _ { K }$ . We first need to show that $\mu _ { n } \otimes \mu _ { n } \to \mu \otimes \mu$ in weak-˚, i.e. that

$$
\int \int f ( x , y ) d \mu _ { n } ( x ) d \mu _ { n } ( y ) \to \int \int f ( x , y ) d \mu ( x ) d \mu ( y )
$$

for all $f \in C ( K \times K )$ This is clear for all functions of the form $( x , y ) \mapsto g ( x ) h ( y )$ with $g , h \in C ( K )$ by the weak-˚ convergence of $\mu _ { n }$ to $\mu$ . Let $\mathcal { F }$ be the span of all functions of the above form.
Then it’s easy to check that $\mathcal { F }$ is dense in $C ( K \times K )$ by the Stone-Weierstrass theorem.
Thus the desired result holds for all of $C ( K \times K )$ . This establishes that $\mu _ { n } \otimes \mu _ { n } \to \mu \otimes \mu$ in weak-˚.

We want to conclude that

$$
{ \cal I } ( \mu ) ~ = ~ \operatorname * { l i m } _ { n  \infty } { \cal I } ( \mu _ { n } ) ~ = ~ R _ { K } .
$$

We would be done by the weak-˚ convergence of $\mu _ { n } \otimes \mu _ { n }$ to $\mu \otimes \mu ,$ , except $( x , y ) \mapsto { \frac { 1 } { | x - y | } }$ isn’t continuous on $K \times K$ . However, it is lower semicontinuous, so by the portmanteau theorem, we have

$$
\operatorname* { l i m } _ { n \to \infty } I ( \mu _ { n } ) \ \geqslant \ I ( \mu ) .
$$

But lim inf $_ { n  \infty } I ( \mu _ { n } ) = R _ { K }$ and $R _ { K }$ is the inf of all values of $I ( \mu )$ , so also $R _ { K } \leqslant I ( \mu )$ and thus $I ( \mu ) = R _ { K }$ so I achieves its minimum.
□

Problem 5. Define a Hilbert space

$$
H : = \{ u : \mathbb { D }  \mathbb { R } : u { \mathrm { ~ i s ~ h a r m o n i c ~ a n d ~ } } \int _ { \mathbb { D } } | u ( x , y ) | ^ { 2 } d x d y < \infty \}
$$

with inner product $\langle f , g \rangle = \int _ { \mathbb { D } } f g d x d y$

(a) Show that $f \mapsto f _ { x } ( 0 , 0 )$ is a bounded linear functional on $H$

(b) Compute the norm of this linear functional.

Solution (bad).
We show that the norm is $2 / { \sqrt { \pi } }$ . Since u is harmonic, $u _ { x }$ also is.
So we apply the mean value property on a disc of radius $r \in ( 0 , 1 )$ to get

$$
\left| u _ { x } ( 0 ) \right| ~ = ~ { \frac { 1 } { \pi r ^ { 2 } } } \left| \int _ { B ( 0 , r ) } u _ { x } { \ : } d A \right| ~ = ~ { \frac { 1 } { \pi r ^ { 2 } } } \left| \int _ { \partial B ( 0 , r ) } u { \ : } d y \right|
$$

by Green’s theorem.
So

$$
\begin{array} { r c l } { { | u _ { x } ( 0 ) | } } & { { = } } & { { \displaystyle \frac { 1 } { \pi r ^ { 2 } } \left| \int _ { 0 } ^ { 2 \pi } u ( r \cos \theta , r \sin \theta ) r \cos ( \theta ) d \theta \right| } } \\ { { | u _ { x } ( 0 ) | ^ { 2 } } } & { { \leqslant } } & { { \displaystyle \frac { 1 } { \pi ^ { 2 } r ^ { 2 } } \left( \int _ { 0 } ^ { 2 \pi } u ( r \cos \theta , r \sin \theta ) ^ { 2 } d \theta \right) \left( \int _ { 0 } ^ { 2 \pi } \cos ^ { 2 } \theta \right) \quad \mathrm { b y ~ C a u c h y - S c h w a r z } } } \\ { { \pi r ^ { 2 } | u _ { x } ( 0 ) | ^ { 2 } } } & { { \leqslant } } & { { \displaystyle \int _ { 0 } ^ { 2 \pi } u ( r \cos \theta , r \sin \theta ) ^ { 2 } d \theta . } } \end{array}
$$

Multiplying both sides by r and integrating over $r \in [ 0 , 1 ]$ we get

$$
\frac { \pi } { 4 } \left| u _ { x } ( 0 ) \right| ^ { 2 } \ \leqslant \ \int _ { \mathbb { D } } u ^ { 2 } d A ,
$$

so $\begin{array} { r l } { | u _ { x } ( 0 ) | } & { { } \leqslant \frac { 2 } { \sqrt { \pi } } \left| | u | \right| _ { H } } \end{array}$ . Finally, it’s easy to check that $u ( x , y ) = x$ achieves this bound, so $2 / \sqrt { \pi }$ is the operator norm.

Alternate solution (way better).
Since D is simply connected, u is the real part of an analytic functionř $f = u + i v \mathrm { ~ o n ~ } \mathbb { D }$ Write $\textstyle f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ . We know this power series converges uniformly on compact subsets of D. We have

$$
u ( r e ^ { i \theta } ) \ = \ \sum _ { n = 0 } ^ { \infty } \mathrm { R e } ( a _ { n } r ^ { n } e ^ { i n \theta } ) \ = \ \sum _ { n = 0 } ^ { \infty } r ^ { n } ( \mathrm { R e } ( a _ { n } ) \cos ( n \theta ) - \mathrm { I m } ( a _ { n } ) \sin ( n \theta ) ) .
$$

We also know that $u _ { x } = \operatorname { R e } ( f ^ { \prime } )$ , so we have $u _ { x } ( 0 ) = \operatorname { R e } ( a _ { 1 } )$ . We have

$$
\begin{array} { r l } { \displaystyle \int _ { \mathbb { D } } u ^ { 2 } d A } & { = \displaystyle \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 2 \pi } \left( \sum _ { n = 0 } ^ { \infty } r ^ { n } ( \mathrm { R e } ( a _ { n } ) \cos ( n \theta ) - \mathrm { I m } ( a _ { n } ) \sin ( n \theta ) ) \right) ^ { 2 } r d \theta d r } \\ & { = \displaystyle \int _ { 0 } ^ { 1 } r \int _ { 0 } ^ { 2 \pi } \sum _ { n , k = 0 } ^ { \infty } r ^ { n } r ^ { k } ( \mathrm { R e } ( a _ { n } ) \cos ( n \theta ) - \mathrm { I m } ( a _ { n } ) \sin ( n \theta ) ) ( \mathrm { R e } ( a _ { k } ) \cos ( k \theta ) - \mathrm { I m } ( a _ { k } ) \sin ( k \theta ) ) d \theta d r . } \end{array}
$$

Using the orthonormality properties of sin and cos and the fact that the power series converges uniformly on compact sets, this is equal to

$$
\begin{array} { r l } { \displaystyle } & { = \ \int _ { 0 } ^ { 1 } \displaystyle \sum _ { n = 0 } ^ { \infty } r ^ { 2 n + 1 } \int _ { 0 } ^ { 2 \pi } \left( \mathrm { R e } ( a _ { n } ) ^ { 2 } \cos ^ { 2 } ( n \theta ) + \mathrm { I m } ( a _ { n } ) ^ { 2 } \sin ^ { 2 } ( n \theta ) \right) d \theta d r } \\ { \displaystyle } & { = \ \int _ { 0 } ^ { 1 } \displaystyle \sum _ { n = 0 } ^ { \infty } r ^ { 2 n + 1 } \pi ( \mathrm { R e } ( a _ { n } ) ^ { 2 } + \mathrm { I m } ( a _ { n } ) ^ { 2 } ) d r } \\ { \displaystyle } & { \geqslant \ \int _ { 0 } ^ { 1 } r ^ { 3 } \pi \mathrm { R e } ( a _ { 1 } ) ^ { 2 } \ = \ \frac { \pi } { 4 } \mathrm { R e } ( a _ { 1 } ) ^ { 2 } . } \end{array}
$$

Thus we see that

$$
\mathrm { R e } ( a _ { 1 } ) ^ { 2 } \ \leqslant \ \frac { 4 } { \pi } \int _ { \mathbb { D } } u ^ { 2 } d A ,
$$

so

$$
u _ { x } ( 0 ) \ = \ \mathrm { R e } ( a _ { 1 } ) \ \leqslant \ \frac { 2 } { \sqrt { \pi } } \left| | u | | _ { H } . \right.
$$

This shows that the operator norm is at most $2 / \sqrt { \pi }$ . And by inspecting the above proof, we see that equality holds if $\mathrm { R e } ( a _ { n } ) = \mathrm { I m } ( a _ { n } ) = 0$ for $n \neq 1$ and $\mathrm { I m } ( a _ { 1 } ) = 0$ This is achieved when $f ( z ) = z , { \mathrm { i . e . ~ } } u ( x , y ) = x .$ , so the operator norm is exactly $2 / \sqrt { \pi }$ . Alternatively one could compute directly that $u ( x , y ) = x$ achieves this bound.

Problem 6. Let

$$
X \ : = \ \left\{ \xi \mapsto \int _ { \mathbb { R } } e ^ { i \xi x } f ( x ) d x : f \in L ^ { 1 } ( \mathbb { R } ) \right\} .
$$

Show that (a) X is a subset of $C _ { 0 } ( \mathbb { R } )$ , (b) X is a dense subset of $C _ { 0 } ( \mathbb { R } )$ , and (c) $X \neq C _ { 0 } ( \mathbb { R } )$

Solution.
Note that $\xi \mapsto \int _ { \mathbb { R } } e ^ { i \xi x } f ( x )$ is the function ${ \widehat { f } } ( - \xi )$ . For the sake of a having a convenient notation, we will prove each of these results for the Fourier transform.
Obviously $\mathrm { ( a ) - ( c ) }$ will follow.

(a) Continuity follows immediately from the dominated convergence theorem, since $\left| e ^ { - i \xi x } f ( x ) \right| \leqslant \left| f ( x ) \right|$ which is integrable by hypothesis.

By directly calculating the integral, it is easy to see that sp lies in $C _ { 0 } ( \mathbb { R } )$ when s is a sum of characteristic functions of open intervals.
The set of such functions is dense in ˇˇ ˇˇ $L ^ { 1 } ( \mathbb { R } )$ , so given $f \in L ^ { 1 }$ choose s with $\| f - s \| _ { 1 } < \epsilon$ . Then $\Big | \Big | \widehat { f } - \widehat { s } \Big | \Big | _ { \infty } \leqslant | | f - s | | _ { 1 } < \epsilon$ , and so

$$
\operatorname* { l i m } _ { | \xi | \to \infty } { \widehat { f } } ( \xi ) \leqslant \operatorname* { l i m } _ { | \xi | \to \infty } s ( \xi ) + \epsilon = \epsilon .
$$

But  was arbitrary, so the limit is 0.

Remark.
One could also solve this problem by invoking the density of $C _ { c } ^ { \infty }$ (or even $C _ { c } ^ { 1 } )$ in $L ^ { 1 } ( \mathbb { R } )$ and then applying integration by parts.

(b) We claim that $C _ { c } ^ { \infty } ( \mathbb { R } )$ is dense in $C _ { c } ( \mathbb { R } )$ To see this, fix $f \in C _ { c } ( \mathbb { R } )$ and choose M large enough so that $| f ( x ) | < \epsilon$ when $| x | > M .$ . Let g be a smooth function such that $| f ( x ) - g ( x ) | < \epsilon$ for $x \in$ $[ - ( M + 1 ) , M + 1 ]$ . Also let $\beta : \mathbb { R }  [ 0 , 1 ]$ be a smooth bump function with supp $\textstyle \left( { \beta } \right) \subseteq \left[ - ( M + 1 ) \right]$ , M \`1s and which takes the value 1 on $[ - M , M ]$ . Then $_ { \beta g }$ is smooth, and we have $| | f - \beta g | | _ { \infty } < 2 \epsilon$

So $C _ { c } ^ { \infty } ( \mathbb { R } )$ is dense in $C _ { c } ( \mathbb { R } )$ , and in particular the space of Schwartz functions is dense in $C _ { c } ( \mathbb { R } )$ The Fourier transform is a bijection on the space of Schwartz functions, so X contains all Schwartz functions which gives a dense subset.

(c) Recall that the Fourier transform $\mathcal { F }$ is an injective bounded linear map from $L ^ { 1 } ( \mathbb { R } )$ to $C _ { 0 } ( \mathbb { R } )$ . If the Fourier transform was surjective onto $C _ { 0 } ( \mathbb { R } )$ then by the open mapping theorem $\mathcal { F } ^ { - 1 } : C _ { 0 } ( \mathbb { R } ) \to L ^ { 1 } ( \mathbb { R } )$ would be bounded.

Let $h = \chi _ { [ - 1 , 1 ] }$ and let $h _ { i } \in C _ { c } ^ { \infty } ( \mathbb { R } )$ be a uniformly bounded sequence of functions which converges to h in $L ^ { 2 ^ { - } } \left( \mathrm { f o r } \right)$ instance, bump functions would suffice).
Also let $g _ { i } = \mathcal { F } ^ { - 1 } ( h _ { i } )$ . Note that the $g _ { i } \mathrm { \dot { s } }$ are Schwartz functions and therefore lie in $L ^ { 1 }$ . (Alternatively, this must be true by the hypothesis of surjectivity.)
Now h lies in $L ^ { 2 }$ and is therefore the Fourier-Plancherel transform of a function $g .$ Since the Fourier-Plancherel transform is an $L ^ { 2 }$ isometry, we have that $g _ { i } \to g$ in $L ^ { 2 }$ . By passing to a subsequence if necessary, we may assume that $g _ { i } \to g$ pointwise almost everywhere.

On the other hand g is not in $L ^ { 1 }$ , otherwise its Fourier transform would be continuous.
Thus by Fatou’s lemma, lim $_ { i \to \infty } \left| \left| g _ { i } \right| \right| _ { 1 } = \infty$ . However this contradicts the boundedness of ${ \mathcal { F } } ^ { - 1 }$ , since we assumed that the $h _ { i } \mathrm { { ' s } }$ were uniformly bounded.

Remark.
It turns out that $g ( \underline { { x } } ) = \frac { \sin ( x ) } { x }$ . However this wasn’t important to us.
In fact we could have taken h to be any bounded L2 function which doesn’t agree a.e. with a continuous function.

Problem 7. Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function such that log $| f |$ is absolutely integrable with respect to planar Lebesgue measure.
Show that f is constant.

Solution.
Suppose that $f$ is not constant.
By Liouville there exists $z _ { 0 } ~ \in \ \mathbb { C }$ such that log $| f ( z _ { 0 } ) | > 1$ Recall that log |f| is subharmonic.
By the mean value property we have

$$
\int _ { \mathbb { R } ^ { 2 } } \log | f ( z ) | d \lambda = \int _ { r = 0 } ^ { \infty } r \int _ { 0 } ^ { 2 \pi } \log | f ( z _ { 0 } + r e ^ { i \theta } ) | d \theta d r \geqslant \int _ { r = 0 } ^ { \infty } 2 \pi r d r = \infty . \quad \boxed { \mathrm { I } }
$$

Problem 8a. Let A and B be positive definite $n \times n$ real symmetric matrices with the property

$$
\left| \left| B A ^ { - 1 } x \right| \right| \leqslant \left| \left| x \right| \right|
$$

for all $x \in \mathbb { R } ^ { n }$ , where $\left| \left| x \right| \right|$ denotes the usual Euclidean norm.
Show that for each pair $x , y \in \mathbb { R } ^ { n }$

$$
z \mapsto \left. y , B ^ { z } A ^ { - z } x \right.
$$

admits an analytic continuation from $0 < z < 1$ to the whole complex plane.

Solution.
Since A and B are symmetric and positive definite, we can write $A = S _ { A } \Lambda _ { A } S _ { A } ^ { - 1 } $ and $B \ =$ $S _ { B } \Lambda _ { B } S _ { B } ^ { - 1 }$ where $\Lambda _ { A }$ and $\Lambda _ { B }$ are diagonal matrices with positive diagonal entries.
Then for $z \in \mathsf { \Gamma } ( 0 , 1 )$ $A ^ { - z } = \stackrel { \smile } { S } _ { A } \Lambda _ { A } ^ { z } S _ { A } ^ { - 1 }$ and $B ^ { z } = S _ { B } \Lambda _ { B } ^ { z } S _ { B } ^ { - 1 }$ , where $\Lambda _ { A } ^ { z }$ is simply the matrix gotten by raising each diagonal entry to the power z. The given function is seen to be a polynomial in the zth powers of the eigenvalues of B and the inverses of the eigenvalues of $B ,$ and therefore extends to a holomorphic function on C. (Note that $\lambda ^ { z } = e ^ { \log ( \lambda ) z }$ , which is holomorphic.)

Problem 8b. Show that $\left| \left| B ^ { \theta } A ^ { - \theta } x \right| \right| \leqslant \left| \left| x \right| \right|$ for all $0 \leqslant \theta \leqslant 1$

Solution.
For $x , y \in \mathbb { R } ^ { n }$ , let $f _ { x , y } ( z )$ be holomorphic function from part $\mathrm { ( a ) }$

When $\mathrm { R e } ( z ) = 0$ we note that the eigenvalues of $B ^ { z }$ and $A ^ { - z }$ have norm 1. These matrices are symmetric, so they each have operator norm 1, which implies that

$$
| f _ { x , y } ( z ) | = |  y , B ^ { z } A ^ { - z } x  | \leqslant | | y | | | B ^ { z } A ^ { - z } x | | \leqslant | | y | | | | x | | .
$$

When $\mathrm { R e } ( z ) = 1$ , write $z = 1 + b i$ . Then

$$
\begin{array} { r } { \left| \left| B ^ { z } A ^ { - z } \right| \right| _ { \mathrm { o p } } = \left| \left| B ^ { i z } B A ^ { - 1 } A ^ { - i z } \right| \right| _ { \mathrm { o p } } \leqslant \left| \left| B ^ { i z } \right| \right| _ { \mathrm { o p } } \left| \left| B A ^ { - 1 } \right| \right| _ { \mathrm { o p } } \left| \left| A ^ { - i z } \right| \right| _ { \mathrm { o p } } \leqslant 1 , } \end{array}
$$

and so

$$
| f _ { x , y } ( z ) | \leqslant | | y | | | B ^ { z } A ^ { - z } x | | \leqslant | | y | | | | x | | .
$$

Also note that $f _ { x , y }$ is bounded on the strip $S = \{ z : \mathrm { R e } ( z ) \in [ 0 , 1 ] \}$ , since each function $\lambda ^ { z }$ is bounded on the strip (recall the solution to part (a)). By the Hadamard three lines theorem, we conclude that $f _ { x , y }$ is bounded by $\lvert \lvert x \rvert \rvert \lvert y \rvert \rvert$ everywhere in S. (Alternatively one can mimic the proof of this theorem by applying the Phragmen-Lindelof method.)

Finally for $\theta \in [ 0 , 1 ]$ we have

$$
\left| \left| B ^ { \theta } A ^ { - \theta } x \right| \right| = \operatorname* { s u p } _ { | | y | | = 1 } \left| f _ { x , y } ( \theta ) | \leqslant | | x | | . \right|
$$

Problem 9. Let $P ( z )$ be a non-constant polynomial, all of whose zeros lie in a half plane $\left\{ z \in \mathbb { C } : \operatorname { R e } ( z ) < \sigma \right\}$ Show that all zeros of $P ^ { \prime } ( z )$ also lie in the same half plane.

Solution.
Write $P ( z ) = \left( z - a _ { 1 } \right) \cdot \cdot \cdot \left( z - a _ { n } \right)$ . Then we have

$$
{ \frac { P ^ { \prime } ( z ) } { P ( z ) } } = { \frac { 1 } { z - a _ { 1 } } } + \ldots + { \frac { 1 } { z - a _ { n } } } .
$$

Suppose that $P ^ { \prime } ( z ) = 0$ . If $P ( z ) = 0$ also, then z is obviously in the same half plane, so assume otherwise.
Then in particular we have

$$
\begin{array} { l } { 0 = \displaystyle \operatorname { R e } \left( \frac { 1 } { z - a _ { 1 } } \right) + \ldots + \operatorname { R e } \left( \frac { 1 } { z - a _ { n } } \right) } \\ { = \displaystyle \frac { \operatorname { R e } ( z ) - \operatorname { R e } ( a _ { 1 } ) } { | z - a _ { 1 } | ^ { 2 } } + \ldots + \frac { \operatorname { R e } ( z ) - \operatorname { R e } ( a _ { n } ) } { | z - a _ { n } | ^ { 2 } } . } \end{array}
$$

So

$$
{ \mathrm { R e } } ( z ) \sum _ { j = 1 } ^ { n } { \frac { 1 } { | z - a _ { j } | ^ { 2 } } } \ = \ \sum _ { j = 1 } ^ { n } { \frac { { \mathrm { R e } } ( a _ { j } ) } { | z - a _ { j } | ^ { 2 } } } \ < \ \sigma \sum _ { j = 1 } ^ { n } { \frac { 1 } { | z - a _ { j } | ^ { 2 } } } ,
$$

so $\operatorname { R e } ( z ) < \sigma . \quad \quad \varbigcup$

Problem 10. Let $f : \mathbb { C } \to \mathbb { C }$ be a non-constant entire function.
Without using either of the Picard theorems, show that there exist arbitrarily large complex numbers z for which $f ( z )$ is a positive real.

Solution.
Fix a closed ball Br centered at 0 of radius r so that $f ( z ) \in \mathbb { C } \backslash \mathbb { R } _ { \geqslant 0 }$ for $| z | > r .$ By compactness, $| f ( z ) |$ attains a maximum value R on $B _ { r }$ . Then $f ( z ) - R$ is a holomorphic function which avoids the poitive real axis.

Let $\phi : \mathbb { C } \backslash \mathbb { R } _ { \geq 0 }  \mathbb { D }$ be a conformal equivalence of the complex plane with the positive real axis removed, and the open unit disc.
Such a map exists by the Riemann mapping theorem.
For the sake of being concrete we may take

$$
\phi ( z ) = { \frac { { \sqrt { z } } - i } { { \sqrt { z } } + i } }
$$

where ${ \sqrt { e ^ { i \theta } } } = e ^ { i \theta / 2 }$ for $\theta \in \left[ 0 , 2 \pi \right)$

The $\operatorname* { m a p } z \mapsto \phi ( f ( z ) - R )$ is holomorphic and bounded, and therefore constant by Liouville.
So for some constant $C ,$ we have $f ( z ) = \phi ^ { - 1 } ( C ) + R$ . We conclude that $f$ is constant.

Problem 11. Let $f ( z ) = - \pi z \cot ( \pi z )$ be a meromorphic function on $\mathbb { C } .$

(a) Locate all poles of f and determine their residues.

(b) Show that for each $n \geqslant 1$ the coefficient of $z ^ { 2 n }$ in the Taylor expansion of $f ( z )$ about $z = 0$ coincides with

$$
a _ { n } \ = \ \sum _ { k = 1 } ^ { \infty } { \frac { 2 } { k ^ { 2 n } } } .
$$

Solution.
(a) We have

$$
- \pi z \cot ( \pi z ) ~ = ~ \frac { - \pi z \cos ( \pi z ) } { \sin ( \pi z ) } .
$$

From this representation it is clear that f has simple poles at every nonzero integer.
(because sinpπzq has a simple pole at every integer).
So to calculate the residue at z “ n we have

$$
\mathrm { R e s } ( f , z = n ) ~ = ~ \operatorname* { l i m } _ { z \to n } { \frac { - \pi z ( z - n ) \cos ( \pi z ) } { \sin ( \pi z ) } } ~ = ~ \operatorname* { l i m } _ { z \to n } - z \cdot \cos ( \pi z ) \cdot { \frac { \pi ( z - n ) } { \sin ( \pi ( z - n ) ) } } ~ = ~ ( - 1 ) ^ { n + 1 } n .
$$

(b) Here we use the other standard representation

$$
\pi \cot ( \pi z ) = \displaystyle \sum _ { k = - \infty } ^ { \infty } \frac { 1 } { z - k } = \frac { 1 } { z } + \displaystyle \sum _ { k = 1 } ^ { \infty } \frac { 2 z } { z ^ { 2 } - k ^ { 2 } } ,
$$

so we have

$$
f ( z ) ~ = ~ - 1 - \sum _ { k = 1 } ^ { \infty } \frac { 2 z ^ { 2 } } { z ^ { 2 } - k ^ { 2 } } .
$$

Write $f ( z ) = g ( z ^ { 2 } )$ where $\begin{array} { r } { g ( z ) = - 1 - \sum _ { k = 1 } ^ { \infty } \frac { 2 z } { z - k ^ { 2 } } } \end{array}$ . Note that $g$ is holomorphic except at the points where it equals 8 because the series defining it converges uniformly on compact sets.
So the coefficient of $z ^ { 2 n }$ in the power series for f is the same as the coefficient of $z ^ { n }$ in the power series for g. It now suffices to show

that $\begin{array} { r } { g ^ { ( n ) } ( 0 ) = n ! \cdot \sum _ { k = 1 } ^ { \infty } \frac { 2 } { k ^ { 2 n } } } \end{array}$ . Write $g ( z ) = - 1 - 2 z h ( z )$ , where $\begin{array} { r } { h ( z ) = \sum _ { k = 1 } ^ { \infty } \frac { 1 } { z - k ^ { 2 } } } \end{array}$ . Again, h is holomorphic except for at the points where it blows up.
Therefore we have

$$
g ^ { ( n ) } ( 0 ) ~ = ~ - 2 \sum _ { j = 0 } ^ { n } { \binom { n } { j } } ( z \mapsto z ) ^ { ( j ) } ( 0 ) h ^ { ( n - j ) } ( 0 ) ~ = ~ - 2 h ^ { ( n - 1 ) } ( 0 ) .
$$

Since the series defining h converges uniformly on compact sets, it can be differentiated term-by-term, so it’s easy to see by induction that

$$
h ^ { ( n ) } ( z ) ~ = ~ \sum _ { k = 1 } ^ { \infty } \frac { ( - 1 ) ^ { n } n ! } { ( z - k ^ { 2 } ) ^ { n + 1 } } .
$$

Therefore

$$
g ^ { ( n ) } ( 0 ) ~ = ~ - 2 h ^ { ( n - 1 ) } ( 0 ) ~ = ~ n ! \sum _ { k = 1 } ^ { \infty } \frac { 2 } { k ^ { 2 n } } . ~ \boxed { { \frac { \pi } { \it { \Psi } \mathrm { \tiny ~ I ~ } } } }
$$

Problem 12. Let $f : \mathbb { H } \to \mathbb { H }$ be a holomorphic function obeying

$$
\operatorname* { l i m } _ { y \to \infty } y f ( i y ) \ = \ i \quad { \mathrm { a n d } } \quad | f ( z ) | \ \leqslant \ { \frac { 1 } { \operatorname { I m } ( z ) } } \quad { \mathrm { f o r ~ a l l ~ } } z \in \mathbb { H } .
$$

(a) For $\epsilon > 0 .$ , write $\textstyle g _ { \epsilon } ( x ) : = { \frac { 1 } { \pi } }$ Im $f ( x + i \epsilon )$ . Show that

$$
f ( z + i \epsilon ) \ = \ \int _ { \mathbb { R } } { \frac { g _ { \epsilon } ( x ) } { x - z } } d x .
$$

(b) Show that there exists a Borel probability measure µ on R such that

$$
f ( z ) \ = \ \int _ { \mathbb { R } } { \frac { d \mu ( x ) } { x - z } } d x .
$$

Solution.

## 10 Fall 2013

Problem 1. Let U and V be open and connected sets in the complex plane C, and $f : U \to \mathbb { C }$ be a holomorphic function with $f ( U ) \subseteq V$ . Suppose that $f$ is a proper map from U into $V , { \mathrm { i . e . , ~ } } f ^ { - 1 } ( K ) \subseteq U$ is compact, whenver $K \subseteq V$ is compact.
Then f is surjective.

Solution.
We use a connectedness argument.
First note that f can’t be constant on $U ,$ otherwise f isn’t proper.
Then by the open mapping theorem, $f ( U )$ is open.

We claim that $V \backslash f ( U )$ is also open.
Fix Ş $v \in V \backslash f ( U )$ , and let $B _ { 1 } \subseteq B _ { 2 } \subseteq . . . \subseteq V$ be a seqence of nested closed balls around v such that $\bigcap _ { i \in \mathbb { N } } B _ { i } = v$ . We have

$$
\mathcal { O } = f ^ { - 1 } ( \{ v \} ) = f ^ { - 1 } \left( \bigcap _ { i \in \mathbb { N } } B _ { i } \right) = \bigcap _ { i \in \mathbb { N } } f ^ { - 1 } ( B _ { i } ) .
$$

By properness, each $f ^ { - 1 } ( B _ { i } )$ is compact.
In general, a nested sequence of nonempty compact sets has nontrivial intersection1 It follows that one of the sets $f ^ { - 1 } ( B _ { i } )$ must be empty.
The interior of $B _ { i }$ is an open neighborhood of v lying in $V \backslash f ( U )$ . But $v \in V \backslash f ( U )$ was arbitrary, so $V \backslash f ( U )$ is open.

Since $f ( U )$ is nonempty, and V is connected we must have V “ fpUq.

Problem 2. Show that there is no function f that is holomorphic near $0 \in \mathbb { C }$ and satisfies

$$
f ( 1 / n ^ { 2 } ) ~ = ~ { \frac { n ^ { 2 } - 1 } { n ^ { 5 } } }
$$

for all large $n \in \mathbb { N } .$

Solution.
Since f is holomorphic near 0, there is an $r > 0$ such that f has a power series expansion

$$
f ( z ) ~ = ~ \sum _ { j = 0 } ^ { \infty } a _ { j } z ^ { j }
$$

valid in $B ( 0 , r )$ . If $f$ is identically zero then it obviously does not satisfy the condition, so assume it isn’t. Then let k be the smallest $j$ for which $a _ { j } \neq 0 ,$ , so we can write

$$
f ( z ) ~ = ~ x ^ { k } \sum _ { j = k } ^ { \infty } a _ { j } z ^ { j - k } .
$$

When n is big enough so that $1 / n ^ { 2 } < r .$ , we have

$$
f ( 1 / n ^ { 2 } ) ~ = ~ { \frac { 1 } { n ^ { 2 k } } } \sum _ { j = 1 } ^ { \infty } { \frac { a _ { j } } { n ^ { 2 ( j - k ) } } } .
$$

We have the inequalities

$$
| f ( 1 / n ^ { 2 } ) | \ \leqslant \ \frac { 1 } { n ^ { 2 k } } \left( | a _ { k } | + \frac { 1 } { n ^ { 2 } } \left| \sum _ { j = k + 1 } ^ { \infty } \frac { a _ { j } } { n ^ { 2 ( j - k - 1 ) } } \right| \right) \ \leqslant \ \frac { ( 3 / 2 ) | a _ { k } | } { n ^ { 2 k } }
$$

$$
| f ( 1 / n ^ { 2 } ) | \geqslant \frac { 1 } { n ^ { 2 k } } \left( | a _ { k } | - \frac { 1 } { n ^ { 2 } } \left| \sum _ { j = k + 1 } ^ { \infty } \frac { a _ { j } } { n ^ { 2 ( j - k - 1 ) } } \right| \right) \geqslant \frac { ( 1 / 2 ) | a _ { k } | } { n ^ { 2 k } }
$$

for sufficiently large n. Thus if the condition $f ( 1 / n ^ { 2 } ) = ( n ^ { 2 } - 1 ) / n ^ { 5 }$ is satisfied, we would have

$$
\frac { ( 1 / 2 ) | a _ { k } | } { n ^ { 2 k } } \ \leqslant \ \frac { n ^ { 2 } - 1 } { n ^ { 5 } } \ \leqslant \ \frac { ( 3 / 2 ) | a _ { k } | } { n ^ { 2 k } }
$$

for all sufficiently large n. But since $( n ^ { 2 } - 1 ) / n ^ { 5 }$ is asymptotic to $n ^ { - 3 }$ as $n \to \infty$ , it can’t be $\Theta ( n ^ { - 2 k } )$ for any integer k, and so there is no integer k for which this is true.
So f can’t satisfy the condition.

Alternate Solution.
By setting $x = 1 / n$ , we have $f ( x ^ { 2 } ) ~ = ~ x ^ { 3 } - x ^ { 5 }$ for all x of the form $1 / n$ where $n \in \mathbb { N }$ is large enough.
We also have $f ( 0 ) = 0$ by continuity.
Thus $f ( x ^ { 2 } )$ is a holomorphic function on a neighborhood of 0 which agrees with $x ^ { 3 } - x ^ { 5 }$ on a set with a limit point.
So $f ( x ^ { 2 } ) = x ^ { 3 } - x ^ { 5 }$ everywhere on a neighborhood of 0. Then for |z| small enough we must have

$$
z ^ { 3 } - z ^ { 5 } = f ( z ^ { 2 } ) = f ( ( - z ) ^ { 2 } ) = ( - z ) ^ { 3 } - ( - z ) ^ { 5 } ,
$$

which is false for $z \neq 0$

Problem 3. Does there exist a holomorphic function $f : \mathbb { D } \to \mathbb { C }$ such that

$$
\operatorname* { l i m } _ { n \to \infty } | f ( z _ { n } ) | ~ = ~ + \infty
$$

for all sequences $\left\{ z _ { n } \right\}$ in D with lim $\begin{array} { r } { \operatorname { 1 } _ { n  \infty } | z _ { n } | = 1 ? } \end{array}$

Solution.
There does not exist such a function.
Roughly, we would like to apply the minimum principle on the disk.
Unfortunately f may take on the value 0 so this doesn’t work directly.
We can rectify the situation as follows.

By hypothesis, f cannot have a sequence of zeros approaching the boundary of D. Moreover the zeros of f cannot have a limit point in the interior of D, otherwise f would be identically 0. Moreover each zero of f occurs with finite multiplicity.
So by compactness, f has only finitely many zeros $\alpha _ { 1 } , \ldots . a \alpha _ { n }$ in D counting multiplicity.
Let $p ( z ) = \left( z - \alpha _ { 1 } \right) . . . \left( z - \alpha _ { n } \right)$ . Then $p ( z ) / f ( z )$ has removable singularities at the zeros of $f ,$ and hence may be regarded as an analytic function on D. By hypothesis, $p ( z ) / f ( z )$ extends continuously to take the value 0 on the boundary of D. But then by the maximum principle, $p ( z ) / f ( z )$ is identically 0, which is a contradiction.
□

Problem 4. Let u be a non-negative continuous function on ${ \overline { { \mathbb { D } } } } \backslash \{ 0 \}$ that is subharmonic on $\mathbb { D } \backslash \{ 0 \}$ . Suppose that $u | _ { \partial \mathbb { D } } = 0$ and

$$
\operatorname * { l i m } _ { r  0 ^ { + } } \frac 1 { r ^ { 2 } \log ( 1 / r ) } \int _ { \{ z \in \mathbb C : 0 < | z | < r \} } u ( z ) d \lambda ( z ) \ = \ 0 ,
$$

where integration is with respect to Lebesgue measure λ on C. Show that then $u \equiv 0$

Solution.
First we want to show that $u ( z ) = o ( \log | 1 / z | ) { \mathrm { ~ a s ~ } } | z | \to 0$ . Fix $\epsilon < 0$ . By the hypothesis, let $| z |$ be small enough so that

$$
\int _ { \{ z \in \mathbb { C } : 0 < | w | < 3 | z | / 2 \} } u ( w ) d \lambda ( w ) < \epsilon | z | ^ { 2 } \log | 1 / z | .
$$

Then by the mean value property for subharmonic functions we have

$$
u ( z ) \leqslant \frac { 1 } { \pi ( | z | / 2 ) ^ { 2 } } \int _  \{ w \in \Xi \} : | w - z | < ( 1 / 2 ) | z | \} u ( w ) d \lambda ( w ) \leqslant \frac { 4 \pi } { | z | ^ { 2 } } \int _ { \{ w \in \Xi : ( | \infty | \infty | < 3 | z | / 2 ) } \} u ( w ) d \lambda ( w ) < \frac { 4 \pi \epsilon | z | ^ { 2 } \log | 1 / z | } { | z | ^ { 2 } } ,
$$

which shows that $u ( z ) = o ( \log | 1 / z | )$ as |z| Ñ 0.

Now let $\alpha > 0$ and note that the function $f ( z ) : = \alpha \log | 1 / z |$ is harmonic on $\mathbb { D } \backslash \{ 0 \}$ . Thus we know that $u - f$ does not have a maximum value inside $\mathbb { D } \backslash \{ 0 \}$ . Notice that since $u ( z ) ~ = ~ o ( \log | 1 / z | )$ as $| z | \to 0 ,$ , $u ( z ) - f ( z ) \to - \infty { \mathrm { ~ a s ~ } } | z | \to 0$ . Thus there exists an $r > 0$ such that $u ( z ) - f ( z ) \leqslant 0$ for $| z | \leqslant r$ Now on the compact set $S : = \left\{ z \in \mathbb { C } : r \leqslant | z | \leqslant 1 \right\}$ , $u - f$ is continuous so it achieves a maximum.
But the maximum must be achieved on the boundary of f because $u - f$ doesn’t have any maxima inside $\mathbb { D } \backslash \{ 0 \}$ Since $u - f = 0$ on BD and $u - f \leqslant 0 \mathrm { ~ o n ~ } | z | = r$ by choice of $r ,$ this implies that $u - f \leqslant 0$ in all of $\mathbb { D } \backslash \{ 0 \}$ So $u ( z ) - \alpha \log | 1 / z | \leqslant 0$ for all $z \in \mathbb { D } \backslash \{ 0 \}$ , and since α is arbitrary this implies $u ( z ) \leqslant 0$ for all $z \in \mathbb { D } \backslash \{ 0 \}$ , which since u $\geqslant 0$ by hypothesis gives that u is identically zero.

Problem 5. Let $\left\{ f _ { n } \right\}$ be a sequence of holomorphic functions on D and suppose that

$$
\int _ { \mathbb { D } } | f _ { n } ( z ) | d \lambda ( z ) \ \leqslant 1
$$

for all $n \in \mathbb N$ . Show that then there exists a subsequence $\left\{ f _ { n _ { k } } \right\}$ that converges uniformly on all compact subsets of D.

Solution.
We would like to show that the functions $f _ { n }$ form a normal family.
Since each $f _ { n }$ is holomorphic, this is equivalent to verifying that the $f _ { n } \mathrm { \mathrm { ' s } }$ are uniformly bounded on the closed ball $B _ { r } = B ( 0 , r )$ for each $r \in ( 0 , 1 )$ . (Note that each compact subset of D is contained in some such ball.)
Fix $z _ { 0 } \in B _ { r }$ and let $U = B ( z _ { 0 } , 1 - | z _ { 0 } | )$ . Applying the mean value property we have

$$
1 \geqslant \int _ { U } | f _ { n } ( z ) | d \lambda ( z ) \geqslant \left| \int _ { U } f _ { n } ( z ) d \lambda \right| \geqslant \pi ( 1 - | z _ { 0 } | ) ^ { 2 } | f ( z _ { 0 } ) | \geqslant \pi ( 1 - r ) ^ { 2 } | f ( z _ { 0 } ) | .
$$

Therefore $\begin{array} { r } { | f ( z _ { 0 } ) | \leqslant \frac { 1 } { \pi ( 1 - r ) ^ { 2 } } } \end{array}$ for all $z _ { 0 } \in B _ { r }$ , and so f is uniformly bounded on compact sets.

Problem 6. Let $U \subseteq \mathbb { C }$ be a bounded open set with $0 \in U ,$ and $f : U \to \mathbb { C }$ be holomorphic with $f ( U ) \subseteq U$ and $f ( 0 ) = 0$ . Show that $\left| f ^ { \prime } ( 0 ) \right| \leqslant 1$ . Hint: Consider the iterates $f ^ { n } = \underset { ^ { \prime } } { \boldsymbol { f } } \circ \cdots \circ \underset { ^ { \prime } } { \boldsymbol { f } }$ of f .

n times

Solution.
First we prove by induction that $( f ^ { n } ) ^ { \prime } ( 0 ) = ( f ^ { \prime } ( 0 ) ) ^ { n }$ . The case $n = 1$ is obviously true.
Supposing $( f ^ { n - 1 } ) ^ { \prime } ( 0 ) = ( f ^ { \prime } ( 0 ) ) ^ { \bar { n } - 1 }$ , since $f ( 0 ) = 0$ we have

$$
( f ^ { n } ) ^ { \prime } ( 0 ) \ = \ ( f ^ { n - 1 } \circ f ) ^ { \prime } ( 0 ) \ = \ ( f ^ { n - 1 } ) ^ { \prime } ( f ( 0 ) ) f ^ { \prime } ( 0 ) \ = \ ( f ^ { \prime } ( 0 ) ) ^ { n } ,
$$

so the induction is finished.
Note that since U is a bounded set and $f ( U ) \subseteq U$ , also $f ^ { n } ( U ) \subseteq U$ for all n and there is an M such that $| f ^ { n } ( z ) | \leqslant M$ for all $z \in U$ and all n. Since U is open, let $R > 0$ be such that ${ \overline { { B ( 0 , R ) } } } \subseteq U$ . Then applying the Cauchy estimate to $f ^ { n }$ , we get

$$
| f ^ { \prime } ( 0 ) | ^ { n } ~ = ~ | ( f ^ { n } ) ^ { \prime } ( 0 ) | ~ \leqslant ~ { \frac { 1 } { R } } \operatorname* { s u p } _ { | z | = R } | f ^ { n } ( z ) | ~ \leqslant ~ { \frac { M } { R } }
$$

for all n. If $| f ^ { \prime } ( 0 ) | > 1$ this would be impossible because $| f ^ { \prime } ( 0 ) | ^ { n }$ would tend to infinity as $n  \infty$ , so $| f ^ { \prime } ( 0 ) | \leqslant 1 . \quad \bigsqcup$

Problem 7. Show that there is a dense set of functions $f \in L ^ { 2 } ( [ 0 , 1 ] )$ such that $x \mapsto x ^ { - 1 / 2 } f ( x ) \in L ^ { 1 } ( [ 0 , 1 ] )$ and $\int _ { 0 } ^ { 1 } x ^ { - 1 / 2 } f ( x ) d x = 0$

Solution.
Let $S : = \{ f \in L ^ { 2 } ( [ 0 , 1 ] ) : x \mapsto x ^ { - 1 / 2 } f ( x ) \in L ^ { 1 } ( [ 0 , 1 ] )$ and $\int _ { 0 } ^ { 1 } x ^ { - 1 / 2 } f ( x ) d x \ = \ 0 \}$ . Since the set of continuous functions with compact support properly contained in r0, 1s is dense in $L ^ { 2 } ( [ 0 , 1 ] )$ , it suffices to show that S is dense in that set.
Let g be a function which is continuous on rδ, 1s and identically zero on r0, δs for some fixed $\delta > 0$ . Fix $\epsilon > 0$ . Define

$$
I : = \int _ { \delta } ^ { 1 } x ^ { - 1 / 2 } g ( x ) d x \ = \ < \ \infty
$$

because $x ^ { - 1 / 2 }$ is bounded on rδ, 1s. Now define the function $f _ { \epsilon }$ by

$$
f _ { \epsilon } ( x ) \ : = \ \left\{ \begin{array} { l l } { g ( x ) } & { x \in [ \delta , 1 ] } \\ { \frac { - I \epsilon } { \delta ^ { \epsilon } } x ^ { - 1 / 2 + \epsilon } } & { x \in ( 0 , \delta ) } \\ { 0 } & { x = 0 } \end{array} \right. .
$$

We calculate

$$
\int _ { 0 } ^ { 1 } x ^ { - 1 / 2 } f _ { \epsilon } ( x ) d x \ = \ \frac { - I \epsilon } { \delta ^ { \epsilon } } \int _ { 0 } ^ { \delta } x ^ { - 1 + \epsilon } d x + I \ = \ 0
$$

and

$$
\begin{array} { r c l } { \displaystyle \left| | f _ { \epsilon } - g | \right| _ { 2 } ^ { 2 } ~ = ~ \displaystyle \int _ { 0 } ^ { \delta } | f _ { \epsilon } ( x ) - g ( x ) | ^ { 2 } d x ~ \leqslant ~ 4 \displaystyle \int _ { 0 } ^ { \delta } | f _ { \epsilon } ( x ) | ^ { 2 } d x } \\ { \displaystyle ~ < ~ \frac { 4 I ^ { 2 } \epsilon ^ { 2 } } { \delta ^ { 2 \epsilon } } \displaystyle \int _ { 0 } ^ { \delta } x ^ { - 1 + 2 \epsilon } d x ~ = ~ \frac { 4 I ^ { 2 } \epsilon ^ { 2 } } { \delta ^ { 2 \epsilon } } \cdot \frac { \delta ^ { 2 \epsilon } } { 2 \epsilon } ~ = ~ 2 I ^ { 2 } \epsilon , } \end{array}
$$

which can be made as small as desired.
So S is dense in $L ^ { 2 } ( [ 0 , 1 ] )$

Problem ${ \mathbf 8 } ( { \mathbf a } )$ . Compute

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { k } x ^ { n } \left( 1 - { \frac { x } { k } } \right) ^ { k } d x
$$

where $n \in \mathbb { N } .$

Solution.
Define the functions $f _ { k } ( x ) : = x ^ { n } ( 1 - x / k ) ^ { k } \cdot \chi _ { \lceil 0 , k \rceil }$ For each $x \in [ 0 , \infty )$ , as soon as $k \geqslant x$ we have $f _ { k } ( x ) = x ^ { n } ( 1 - x / k ) ^ { k }$ , so we see that $f _ { k } ( x )  x ^ { n } e ^ { - x }$ pointwise on $[ 0 , \infty )$ . Also note that for each $k ,$ $f _ { k } ( x ) \geqslant 0$ for all $x \in \left[ 0 , \infty \right)$ because $( 1 - x / k ) \geqslant 0$ for $x \in [ 0 , k ]$ and $f _ { k } ( x ) = 0$ for $x > k$ . We want to show that $f _ { k } ( x ) \leqslant f _ { k + 1 } ( x )$ for all x so that we can use the Monotone Convergence Theorem.
By the AM-GM inequality, we have

$$
\left( 1 \cdot \left( 1 - { \frac { x } { k } } \right) ^ { k } \right) ^ { 1 / ( k + 1 ) } \leqslant { \frac { 1 + k \left( 1 - { \frac { x } { k } } \right) } { k + 1 } } = { \frac { 1 + k - x } { k + 1 } } = 1 - { \frac { x } { k + 1 } } ,
$$

so $( 1 - x / k ) ^ { k } \leqslant ( 1 - x / ( k + 1 ) ) ^ { k + 1 }$ . This establishes that $f _ { k } \leqslant f _ { k + 1 }$ . Since $x ^ { n } e ^ { - x }$ is integrable on $[ 0 , \infty )$ , the Monotone Convergence Theorem gives

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { k } x ^ { n } \left( 1 - { \frac { x } { k } } \right) ^ { k } d x \ = \ \int _ { 0 } ^ { \infty } f _ { k } ( x ) d x \ = \ \int _ { 0 } ^ { \infty } x ^ { n } e ^ { - x } d x \ = \ n ! \quad \boxed { 1 }
$$

Problem 8(b). Compute

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { \infty } { \left( 1 + { \frac { x } { k } } \right) } ^ { - k } \cos ( x / k ) d x .
$$

Solution.
For each $k \geqslant 2$ define $f _ { k } ( x ) : = ( 1 + ( x / k ) ) ^ { - k } \cos ( x / k )$ . For a fixed $x \in [ 0 , \infty )$ , we have cos $( x / k ) \to 1$ as $k \to \infty$ and $( 1 + ( x / k ) ) ^ { - k } \to e ^ { - x }$ as $k \to \infty$ . Thus $f _ { k } ( x )$ converges pointwise to $e ^ { - x }$ on $[ 0 , \infty )$ . Using the same AM-GM inequality argument as in the problem above, we see

$$
\left( 1 \cdot \left( 1 + { \frac { x } { k } } \right) ^ { k } \right) ^ { 1 / ( k + 1 ) } \leqslant { \frac { 1 + k \left( 1 + { \frac { x } { k } } \right) } { k + 1 } } = { \frac { k + 1 + x } { k + 1 } } = 1 + { \frac { x } { k + 1 } } ,
$$

which establishes $( 1 + x / k ) ^ { k } \leqslant ( 1 + x / ( k + 1 ) ) ^ { k + 1 }$ . Thus $f _ { k } ( x ) \geqslant f _ { k + 1 } ( x )$ for all $x \in [ 0 , \infty )$ . So we have the estimate

$$
| f _ { k } ( x ) | \ \leqslant \ \left( 1 + { \frac { x } { k } } \right) ^ { - k } \ \leqslant \ { \frac { 1 } { ( 1 + x / 2 ) ^ { 2 } } }
$$

which is integrable on $[ 0 , \infty )$ , for all $k \geqslant 2 .$ . Thus by the Dominated Convergence Theorem we have

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { \infty } \left( 1 + { \frac { x } { k } } \right) ^ { - k } \cos ( x / k ) d x \ = \ \int _ { 0 } ^ { \infty } e ^ { - x } \ = \ 1 . \quad \bigsqcup
$$

Note.
Alternate way of showing that Dominated Convergence applies: we just need to show that $0 ~ \leqslant$ $( 1 - x / k ) ^ { k } \ \leqslant \ e ^ { - x }$ for all k and all $x \in [ 0 , k ]$ Equivalent, we want $k \log ( 1 - x / k ) \ \leqslant \ - x$ . Expanding $t \mapsto \log ( 1 - t )$ in a power series around $t = 0$ gives this.

Problem 9. Let X be a Banach space, Y be a normed linear space, and $B : X \times Y  \mathbb { R }$ be a bilinear function.
Suppose that for each $x \in X$ there exists a constant $C _ { x } \geqslant 0$ such that $| B ( x , y ) | \leqslant C _ { x } | | y | |$ for all $y \in Y$ , and for each $y \in Y$ there exists $C _ { y } \geqslant 0$ such that $| B ( x , y ) | \leqslant C _ { y } | | x | |$ for all $x \in X$ Show that then there exists a constant $C \geqslant 0$ such that $| B ( x , y ) | \leqslant C | | x | | | y | |$ for all $x \in X$ and all $y \in Y$

Solution.
For each $y \in Y$ , define the function $T _ { y } : X  \mathbb { R }$ by $T _ { y } ( x ) \ = \ B ( x , y )$ . Since B is bilinear, $T _ { y }$ is a linear functional on X. By hypothesis, for each y we have $| \bar { T _ { y } } ( x ) | = | B ( x , y ) | ~ \leqslant ~ C _ { y } | | x | | , \mathrm { ~ s o ~ } T _ { y }$ is actually a bounded linear functional.
Let $\mathcal { F } = \{ T _ { y } : | | y | | = 1 \}$ . This is a family of bounded linear functionals on X, and for each $x \in X$ we have by the other hypothesis

$$
\operatorname* { s u p } _ { | | y | | = 1 } | T _ { y } ( x ) | \ = \ \operatorname* { s u p } _ { | | y | | = 1 } | B ( x , y ) | \ \leqslant \ C _ { x } \ < \ \infty .
$$

Thus since X is a Banach space, we can apply the uniform boundedness principle to conclude that su $\mathrm { p } _ { | | y | | = 1 } | | T _ { y } | | <$ $\infty .$ This means that there is a $C \geqslant 0$ such that $| | T _ { y } | | \leqslant C$ for any $| | y | | = 1$ , which means that $| \overset { \cdot \cdot } { T _ { y } } ( x ) | =$ $| B ( x , y ) | \leqslant C | | x | |$ for any $x \in X$ and any $| | y | | = 1$ . Then by linearity in the second variable we get that $| B ( x , y ) | \leqslant C | | x | | | y | |$ for any $x \in X , y \in Y . \quad \sqcup$

Problem 10a. Let $f \in L ^ { 2 } ( \mathbb { R } )$ and define $h ( x ) \ = \ \int _ { \mathbb { R } } f ( x - y ) f ( y )$ dy for $x \in \mathbb { R }$ . Show that then there exists a function $g \in L ^ { 1 } ( \mathbb { R } )$ such that

$$
h ( \xi ) \ = \ \int _ { \mathbb { R } } e ^ { - i \xi x } g ( x ) d x
$$

for $\xi \in \mathbb { R }$ , i.e. h is the Fourier transform of a function in $L ^ { 1 } ( \mathbb { R } )$

Solution.
We are motivated by the fact that if g were such a function, then we would have ${ \mathcal { F } } ( g ) =$ $f \ast f = \mathcal { F } ( \mathcal { F } ^ { - 1 } ( f ) ) \ast \mathcal { F } ( \mathcal { F } ^ { - 1 } ( f ) ) = \mathcal { F } ( \mathcal { F } ^ { - 1 } ( f ) ^ { 2 } ) , \mathrm { ~ s o ~ } g = \mathcal { F } ^ { - 1 } ( f ) ^ { 2 }$

Let F denote the Fourier-Plancherel transform.
Recall it is an isometric isomorphism $L ^ { 2 } \to L ^ { 2 }$ Given $f \in L ^ { 2 }$ , define $g : = \mathcal { F } ^ { - 1 } ( f ) ^ { 2 }$ . It’s clear that $g \in L ^ { 1 }$ . Let p¨ denote the regular Fourier transform $L ^ { 1 } \to L ^ { \infty }$ Recall that p¨ and $\mathcal F ( \cdot )$ agree on $L ^ { 1 } \cap L ^ { 2 }$ . We verify

$$
\widehat { g } \ = \ \mathcal { F } ^ { - 1 } \widehat { ( f ) \mathcal { F } ^ { - 1 } } ( f ) \ = \ \mathcal { F } ( \mathcal { F } ^ { - 1 } ( f ) ) * \mathcal { F } ( \mathcal { F } ^ { - 1 } ( f ) ) \ = \ f * f .
$$

In the previous line we used the identity $\widehat { a b } = \mathcal { F } ( a ) \ast \mathcal { F } ( b )$ for $a , b \in L ^ { 2 }$ . Here is a proof of it (not sure if this would be required on the qual or not):

We know the identity holds for Schwartz functions (this follows from basic properties of the Fourier transform and a lot of Fubini’s theorem).
Let $a _ { n } , b _ { n }$ be Schwartz functions with $a _ { n } \to a$ and $b _ { n } \to b$ in $L ^ { 2 }$ . We know that $\widehat { a _ { n } b _ { n } } = \mathcal { F } ( a _ { n } ) * \mathcal { F } ( b _ { n } )$ for each $n ,$ so it suffices to show that ${ \widehat { a _ { n } b _ { n } } } \to { \widehat { a b } }$ and ${ \mathcal { F } } ( a _ { n } ) * { \mathcal { F } } ( b _ { n } ) \to { \mathcal { F } } ( a ) * { \mathcal { F } } ( b )$ in $L ^ { \infty }$ . We have

$$
\begin{array} { r l r } { \Big \vert \Big \vert \widehat { a _ { n } b _ { n } } - \widehat { a b } \Big \vert \Big \vert _ { L ^ { \infty } } \ = \ \Big \vert \Big \vert a _ { n } \widehat { b _ { n } } - a b \Big \vert \Big \vert _ { L ^ { \infty } } \ \leqslant \ \left. \left. a _ { n } b _ { n } - a b \right. \right. _ { L ^ { 1 } } \ \leqslant \ \left. \left. ( a _ { n } - a ) b \right. \right. _ { L ^ { 1 } } + \left. \left. ( b _ { n } - b ) a \right. \right. _ { L ^ { 1 } } } \end{array}
$$

$$
\begin{array} { r } { \leqslant \left| \left| a _ { n } - a \right| \right| _ { L ^ { 2 } } \left| \left| b \right| \right| _ { L ^ { 2 } } + \left| \left| b _ { n } - b \right| \right| _ { L ^ { 2 } } \left| \left| a \right| \right| _ { L ^ { 2 } } \ \to \ 0 } \end{array}
$$

$$
\begin{array} { r l } { | | \mathcal { F } ( a _ { n } ) \ast \mathcal { F } ( b _ { n } ) - \mathcal { F } ( a ) \ast \mathcal { F } ( b ) | | _ { L ^ { \infty } } \ : \leqslant \ : | | \mathcal { F } ( a _ { n } - a ) \ast \mathcal { F } ( b ) | | _ { L ^ { \infty } } + | | \mathcal { F } ( b _ { n } - b ) \ast \mathcal { F } ( a ) | | _ { L ^ { \infty } } } & { } \\ { \leqslant \ : | | \mathcal { F } ( a _ { n } - a ) | | _ { L ^ { 2 } } | | \mathcal { F } ( b ) | | _ { L ^ { 2 } } + | | \mathcal { F } ( b _ { n } - b ) | | _ { L ^ { 2 } } | | \mathcal { F } ( a ) | | _ { L ^ { 2 } } } & { } \\ { = \ : | | a _ { n } - a | | _ { L ^ { 2 } } | | b | | _ { L ^ { 2 } } + | | b _ { n } - b | | _ { L ^ { 2 } } | | a | | _ { L ^ { 2 } } \ : \to \ : 0 . \ : \ : \boxed { 1 } } \end{array}
$$

Problem 10b. Conversely, show that if $g \in L ^ { 1 } ( \mathbb { R } )$ , then there is a function $f \in L ^ { 2 } ( \mathbb { R } )$ such that the Fourier transform of $g$ is given by $x \mapsto h ( x ) : = \int _ { \mathbb { R } } f ( x - y ) f ( y ) d y$

Solution.
Using a similar motivating argument as in part $\mathrm { ( a ) }$ , we see that we want to set $f = \mathcal { F } ^ { - 1 } ( \sqrt { \check { g } } )$ (recall that a $\forall ( x ) : = g ( - x )$ and that for Schwartz functions, $\mathcal { F } ^ { 2 } ( s ) = \widecheck { s } )$ This is a little annoying becausea $\sqrt { \check { g } }$ isn’t even necessarily defined.
But in general, for measurable functions $h : \mathbb { R }  \mathbb { C }$ , we can define $\sqrt { h ( x ) }$ to be the square root defined by removing the positive real axis if $h ( x )$ is not a positive real, and define it to be the positive real square root if $h ( x )$ is a positive real.
The representation

$$
\sqrt { h } \ = \ s q r t _ { 1 } \big ( h \cdot \chi _ { \{ x : h ( x ) \notin \mathbb { R } ^ { + } \} } \big ) + s q r t _ { 2 } \big ( h \cdot \chi _ { \{ x : h ( x ) \in \mathbb { R } ^ { + } \} } \big )
$$

where $s q r t _ { 1 }$ is the branch cut square root and $s q r t _ { 2 }$ is the positive real square root immediately shows that the square root defined this way is measurable, anda $\mathrm { i t } ^ { \prime } \mathrm { s }$ clear that $\sqrt { h } \in L ^ { 2 }$ if and only if $h \in L ^ { 1 }$ . So the definition $f : = \mathcal { F } ^ { - 1 } ( \sqrt { \check { g } } ) \in L ^ { 2 }$ makes sense.
Again, we just verify

$$
f * f \ = \ { \mathcal { F } } ^ { - 1 } ( { \sqrt { \check { g } } } ) * { \mathcal { F } } ^ { - 1 } ( { \sqrt { \check { g } } } ) \ = \ { \mathcal { F } } ( \check { \check { g } } ) \ = \ { \mathcal { F } } ( g ) .
$$

Here we have used the identity ${ \mathcal { F } } ^ { - 1 } ( a ) * { \mathcal { F } } ^ { - 1 } ( b ) = { \mathcal { F } } ( { \check { a } } b )$ for $a , b \in L ^ { 2 }$ This is proven using a similar argument as for the corresponding identity in part (a), recalling that $\mathcal { F } ^ { - 1 } = \mathcal { F } ^ { 3 }$ for Schwartz functions.

Problem 11. Consider the space $C ( [ 0 , 1 ] )$ of real-valued continuous functions on the unit interval r0, 1s. We denote by $\left| \left| f \right| \right| _ { \infty } : = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } \left| f ( x ) \right|$ the supremum norm and by $\vert \vert f \vert \vert _ { 2 } : = \left( \int _ { 0 } ^ { 1 } \vert f ( x ) \vert ^ { 2 } \right) ^ { 1 / 2 }$ the $L ^ { 2 } .$ -norm of a function $f \in C ( [ 0 , 1 ] )$

Let S be a subspace of $C ( [ 0 , 1 ] )$ . Show that if there exists a constant $K \geqslant 0$ such that $\vert \vert f \vert \vert _ { \infty } \leqslant K \vert \vert f \vert \vert _ { 2 }$ for all $f \in S$ , then S is finite-dimensional.

Solution.
Let S denote the closure of S with respect to the $L ^ { 2 }$ norm.
It obviously suffices to show that S is finite-dimensional.
First we show that S is still contained in $C ( [ 0 , 1 ] )$ . Suppose $f \in { \overline { { S } } }$ , then there is a sequence $f _ { n } \in S$ with $\vert \vert f _ { n } - f \vert \vert _ { 2 } \to 0$ as $n \to \infty$ . For any $n , m$ , we have $| | f _ { n } - f _ { m } | | _ { \infty } \leqslant K \left| | f _ { n } - f _ { m } | \right| _ { 2 } ,$ , and since $\left\{ f _ { n } \right\}$ converges in $L ^ { 2 }$ , it is also Cauchy in $L ^ { 2 } .$ so by the above inequality it is also a Cauchy sequence in $C ( [ 0 , 1 ] )$ . Since $C ( \lceil 0 , 1 \rceil )$ is complete, there is some $g \in C ( [ 0 , 1 ] )$ with $| | f _ { n } - g | | _ { \infty } \to 0$ as $n \to \infty$ . Note that since $| | h | | _ { 2 } \leqslant | | h | | _ { \infty }$ for any $h \in C ( [ 0 , 1 ] )$ , we have

$$
| | g - f | | _ { 2 } \leqslant | | g - f _ { n } | | _ { 2 } + | | f _ { n } - f | | _ { 2 } \leqslant | | g - f _ { n } | | _ { \infty } + | | f _ { n } - f | | _ { 2 } \to 0
$$

as $n \to \infty$ . Thus $| | g - f | | _ { 2 } = 0$ , so $f = g$ in $L ^ { 2 }$ , hence f is continuous.
Thus ${ \overline { { S } } } \subseteq C ( [ 0 , 1 ] )$ .

For each $x \in \ [ 0 , 1 ]$ , define the map between normed vector spaces $\phi _ { x } : ( \overline { { S } } , | | \cdot | | _ { 2 } ) \ :  \ : \mathbb { R }$ by $f \mapsto f ( x )$ This is clearly a linear functional on the space S. For any $f \in { \overline { { S } } }$ , we have

$$
| \phi _ { x } ( f ) | ~ = ~ | f ( x ) | ~ \leqslant ~ | | f | | _ { \infty } ~ \leqslant ~ K | | f | | _ { 2 } ,
$$

so in fact $\phi _ { x }$ is a bounded linear functional on S. Since $\overline { S }$ is a closed subspace of the Hilbert space $L ^ { 2 } ( [ 0 , 1 ] )$ 2 it is also a Hilbert space, and thus by the Riesz representation theorem for each x there exists some $g _ { x } \in \overline { { S } }$ such that $f ( x ) = \phi _ { x } ( f ) = \langle f , g _ { x } \rangle$ for all $f \in { \overline { { S } } }$ . Note also that for each x

$$
| | g _ { x } | | _ { 2 } ^ { 2 } ~ = ~ | \langle g _ { x } , g _ { x } \rangle | ~ = ~ | g _ { x } ( x ) | ~ \leqslant ~ | | g _ { x } | | _ { \infty } ~ \leqslant ~ K | | g _ { x } | | _ { 2 } ,
$$

so $\begin{array} { r } { | | g _ { x } | | _ { 2 } \leqslant K . } \end{array}$

Now let $\{ f _ { 1 } , \ldots , f _ { N } \}$ be any linearly independent set in ${ \overline { { S } } } .$ By applying the Gram-Schmidt process if necessary we may assume that it is an orthonormal set.
Then by Bessel’s inequality, we have for each x that

$$
\sum _ { j = 1 } ^ { N } | f _ { j } ( x ) | ^ { 2 } \ = \ \sum _ { j = 1 } ^ { N } | \langle f _ { j } , g _ { x } \rangle | ^ { 2 } \ \leqslant \ | | g _ { x } | | _ { 2 } ^ { 2 } \ \leqslant \ K ^ { 2 } .
$$
