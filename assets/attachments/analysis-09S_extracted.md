# Analysis Qualifying Examination - March 26, 2009

## Instructions:

Work any 10 problems and therefore at least 4 from Problems 1 - 6 and at least 4 from Problems ${ { \mathrm { ~ 7 ~ } } \mathrm { ~ - ~ } 1 2 }$ All problems are worth ten points. Full credit on one problem will be better than part credit on two problems.

1. Let f and g be real-valued integrable functions on a measure space $( X , B , \mu )$ , and define

$$
F _ { t } = \{ x \in X : f ( x ) > t \} , G _ { t } = \{ x \in X : g ( x ) > t \} .
$$

Prove

$$
\int | f - g | d \mu = \int _ { - \infty } ^ { \infty } \mu { \big ( } ( F _ { t } \setminus G _ { t } ) \cup ( G _ { t } \setminus F _ { t } ) { \big ) } d t .
$$

2. Let H be an infinite dimensional real Hilbert space.

a) Prove the unit sphere $S = \{ x \in H : \| x \| = 1 \}$ of H is weakly dense in the unit ball $B = \{ x \in H : | | x | | \leq 1 \}$ of H. (i.e. if $x \in B$ , there is a sequence $\{ x _ { n } \} \in S$ such that for all $y \in H$ $< x , y > = \operatorname { l i m } < x _ { n } , y > . )$

b) Prove there is a sequence $T _ { n }$ of bounded linear operators from H to H such that $\left\{ \left| T _ { n } \right| \right| = 1$ for all n but lim $T _ { n } ( x ) = 0$ for all $x \in H$

3. Let X be a Banach space and let $X ^ { * }$ be its dual Banach space. Prove that if $X ^ { * }$ is separable then X is separable.

4. Let $f ( x )$ be a non-decreasing function on [0, 1]. You may assume the theorem that f is differentiable almost everywhere.

aProve that $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) d x \leq f ( 1 ) - f ( 0 ) } \end{array}$

Hint: Fatou.

Let $\{ f _ { n } \}$ be a sequence of non-decreasing functions on the unit interval [0, 1], such that the series $\begin{array} { r } { F ( x ) = \sum _ { n = 1 } ^ { \infty } f _ { n } ( x ) } \end{array}$ converges for all $x \in \{ a , b \}$ Prove that $\begin{array} { r } { F ^ { \prime } ( x ) = \sum _ { n = 1 } ^ { \infty } f _ { n } ^ { \prime } ( x ) } \end{array}$ almost everywhere on [0, 1].

Hint: Let $\begin{array} { r } { r _ { n } ( x ) = \sum _ { k \geq n } f _ { k } ( x ) } \end{array}$ . It is enough to show $r _ { n } ^ { \prime } ( x ) \to 0$ a.e. Take a subsequence $r _ { n _ { j } }$ such that $r _ { n _ { j } } ( 1 ) - r _ { n _ { j } } ( 0 ) \to 0$ and use part (a).

5. Let $I = I _ { 0 , 0 } = [ 0 , 1 ]$ be the unit interval, and for $n = 0 , 1 , 2 , \ldots$ ., and $0 \leq j \leq 2 ^ { n } - 1$ let

$$
I _ { n , j } = [ j 2 ^ { - n } , ( j + 1 ) 2 ^ { - n } ] .
$$

For $f \in L ^ { 1 } ( I , d x )$ define $\begin{array} { r } { E _ { n } f ( x ) = \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } \Bigl ( 2 ^ { n } \int _ { I _ { n , j } } f d t \Bigr ) \chi _ { I _ { n , j } } } \end{array}$

Prove that if $f \in L ^ { 1 } ( I , d x )$ then $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } E _ { n } f ( x ) = f ( x ) } \end{array}$ almost everywhere on I.

6. For $I _ { n , j }$ as in Problem 5, define the Haar function $h _ { n , j } = 2 ^ { n / 2 } \Big ( \chi _ { I _ { n + 1 , 2 j } } - \chi _ { I _ { n + 1 , 2 j + 1 } } \Big )$

a)Carefully draw ${ { I } _ { 2 , 1 } }$ and graph $h _ { 2 , 1 }$

Prove that if $f \in L ^ { 2 } ( I )$ with respect to Lebesgue measure and $\textstyle \int _ { I } f d t = 0$ , then

$$
\int _ { I } | f ( x ) | ^ { 2 } d x = \sum _ { n , j } | \int f ( t ) h _ { n , j } ( t ) d t | ^ { 2 } .
$$

Prove that if $f \in L ^ { 1 } ( I )$ and $\textstyle \int _ { I } f ( t ) d t = 0$ ,then almost everywhere on $I ,$

$$
f ( x ) = \sum _ { n = 1 } ^ { \infty } \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } \left( \int f ( t ) h _ { n , j } ( t ) d t \right) h _ { n , j } ( x ) .
$$

Hint: Compare the n-th partial sum to $E _ { n } f$ from Problem 5.

7. Let $\mu$ be a finite positive Borel measure on the complex plane C.

a)Prove that $\begin{array} { r } { F ( z ) = \int _ { \mathbb { C } } \frac { 1 } { z - w } d \mu ( w ) } \end{array}$ exists for almost all $z \in \mathbb { C }$ and that $\textstyle \int _ { K } | F ( z ) | d x d y < \infty$ for every compact $K \subset \mathbb { C }$

Usg  ov ha m yal l hs intercept), and all compact $K \subset L , \int _ { K } | F ( x + i y ) | d x < \infty$

c) By "almost all squares in $\mathbb { C } ^ { n }$ we mean al squares in C with sides parallel to the axes except for those squares whose lower left and upper right vertices $\left( z _ { 1 } , z _ { 2 } \right)$ belong to a Lebesgue measure zero subset of $\mathbb { C } ^ { 2 } .$ Prove that for almost all open squares ${ \cal S } ,$

$$
\mu ( S ) = { \frac { 1 } { 2 \pi i } } \int _ { \partial S } F ( z ) d z .
$$

Hint: Use b) and the analagous result for vertical lines.

8. Let $f$ be an entire non-constant function that satisfies the functional equation

$$
f ( 1 - z ) = 1 - f ( z )
$$

for all $z \in \mathbb { C } .$ Show that $f ( \mathbb { C } ) = \mathbb { C }$

9. Let $f ( z )$ be an analytic function on the entire complex plane C and assume $f ( 0 ) \neq 0$ Let $\left\{ a _ { n } \right\}$ be the zeros of $f ,$ counted with their multiplicities.

Let $R > 0$ be such that $| f ( z ) | > 0$ on $| z | = R .$ Prove

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log | f ( R e ^ { i \theta } ) | d \theta = \log | f ( 0 ) | + \sum _ { | a _ { n } | < R } \log ( { \frac { R } { | a _ { n } | } } ) .
$$

Assume $| f ( z ) | \leq C e ^ { | z | ^ { \lambda } }$ for positive constants C and λ. Prove that

$$
\sum ( \frac { 1 } { | a _ { n } | } ) ^ { \lambda + \epsilon } < \infty
$$

for all $\epsilon > 0 .$

Hint: Estimate $\# \{ n : | a _ { n } | < R \}$ by using (a) for the circle of radius 2R.

10. Let D be the open unit disc and $\mu$ be Lebesgue measure on D. Let H be the subspace of $L ^ { 2 } ( \mathbb { D } , \mu )$ consisting of holomorphic functions. Show that H is complete.

11. Suppose that $f : \mathbb { D } \to \mathbb { C }$ is holomorphic and injective in some annulus $\{ z : r < | z | < 1 \}$ , where D is the open unit disc. Show that $f$ is injective in D.

12. Let $Q$ be the closed unit square in the complex plane C and let R be the closed rectangle in C with vertices $\{ 0 , 2 , i , 2 + i \}$ . Prove there does not exist a surjective homeomorphism $f : Q  R$ that is conformal on the interior $Q ^ { o }$ and that maps corners to corners.