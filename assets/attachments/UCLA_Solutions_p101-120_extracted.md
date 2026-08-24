D, which implies that $| f / B | = 1$ throughout D, which by the open mapping theorem implies that $f / B$ must be equal to a constant C with $| C | = 1$ on all of D.

So we can write

$$
f ( z ) ~ = ~ C B ( z ) ~ = ~ C \prod _ { j = 1 } ^ { n } \frac { z - a _ { j } } { 1 - \overline { { { a _ { j } } } } z }
$$

for all $z \in \mathbb { D }$ Since $f$ is entire, by the uniqueness of analytic continuations we know that B must also be entire. But notice that if any $a _ { j }$ is nonzero, then B has a pole at $\overline { { a _ { j } } }$ , which would be a contradiction. So we must have all $a _ { j } = 0$ and thus $B ( z ) = z ^ { m }$ for some integer m. Since we know $f ( z ) = C B ( z ) = C z ^ { m }$ for all $z \in \mathbb { D }$ , since both sides are entire functions this implies that $f ( z ) = C z ^ { m }$ for all $z \in \mathbb { C }$ □

Alternate solution. This solution is basically just a worse version of the first one, but it uses the reflection principle so it’s cool.

The fact that $| f | = 1$ on the unit circle essentially allows us to use the reflection principle. But we need to get rid of the roots at 0 first. More concretely:

Let m be the order of vanishing of $f$ at 0 and let $g ( z ) = z ^ { - m } f ( z )$ . Then g is entire, $g ( 0 ) \neq 0$ , and we still have $| g ( z ) | = 1$ for all $| z | = 1$ We can write this as $1 ~ = ~ g ( z ) { \overline { { g ( z ) } } } ~ = ~ g ( z ) { \overline { { g ( 1 / { \overline { { z } } } ) } } }$ for $| z | = 1$ . The function $\begin{array} { r } { z \mapsto \frac { 1 } { g ( 1 / \overline { { z } } ) } } \end{array}$ is analytic in a neighborhood of the unit circle (because $g ( 1 / \overline { { z } } )$ does not vanish on the unit circle) and agrees with g on the unit circle. Therefore since the unit circle has a limit point, by uniqueness of analytic continuation we have

$$
g ( z ) = { \frac { 1 } { \overline { { { g ( 1 / \overline { { { z } } } ) } } } } } \quad { \mathrm { f o r ~ a l l ~ } } z \neq 0 .
$$

Taking $z  \infty$ , we see that lim $\iota _ { z \to \infty } g ( z ) \ = \ 1 / g ( 0 ) < \infty$ because g does not vanish at 0. So g is bounded, but it’s not necessarily entire because zeros of g inside D reflect to poles outside of D. Let $a _ { 1 } , \ldots , a _ { m }$ be the zeros of $g$ inside $\mathbb { D } ,$ counted with multiplicity. Then

$$
z \mapsto g ( z ) { \frac { ( z - 1 / { \overline { { a _ { 1 } } } } ) \cdot \cdot \cdot ( z - 1 / { \overline { { a _ { n } } } } ) } { ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { n } ) } }
$$

is bounded and entire, so it must be a constant. Therefore we conclude

$$
f ( z ) = C z ^ { m } { \frac { ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { n } ) } { ( z - 1 / { \overline { { a _ { 1 } } } } ) \cdot \cdot \cdot ( z - 1 / { \overline { { a _ { n } } } } ) } } ,
$$

but since f is entire, it can’t have any of those poles, so it also can’t have any of the corresponding zeros, so $f ( z ) = C z ^ { m } . \qquad \bigsqcup$

Problem 10. Does there exist a function $f ( z )$ holomorphic in the disk $| z | < 1$ such that lim $_ { | z |  1 } | f ( z ) | = \infty ?$ Either find one or prove that none exist.

Solution. No such function exists. Suppose f had that property. Then in particular $f$ is not identically zero, so $f$ has only finitely many zeros $r _ { 1 } , \ldots , r _ { n } \in \mathbb { D }$ (where roots are listed as many times as their multiplicity). Let $g ( z ) = f ( z ) / ( z - r _ { 1 } ) \cdot \cdot \cdot ( z - r _ { n } )$ Then g is a function which is holomorphic and nonvanishing in D, and since $\left( z - r _ { 1 } \right) \cdot \cdot \cdot \left( z - r _ { n } \right)$ does not tend to 8 as $| z |  1$ , we still have that $| g ( z ) | \to \infty$ as $| z |  1$ . Since $g$ is nonvanishing, $1 / g$ is also holomorphic in D and $| 1 / g ( z ) | \to 0 { \mathrm { ~ a s ~ } } | z | \to 1$ . But applying the maximum principle to $1 / g ,$ we see that $| 1 / g |$ can’t have any local maximum inside $\mathbb { D } ,$ and since it extends continuously to be identically zero on BD, this implies that $1 / g$ must be identically zero on all of D, which is a contradiction because $g$ is a holomorphic function on D. Thus no such function $f$ can exist.

Problem 11. Assume that $f ( z )$ is holomorphic on $| z | < 2$ . Show that

$$
\operatorname* { m a x } _ { | z | = 1 } \left| f ( z ) - { \frac { 1 } { z } } \right| \ \geqslant \ 1 .
$$

Solution. Let M be the max in question, and let $\gamma$ be the counterclockwise contour around the unit circle. By the ML inequality

$$
\left| \int _ { \gamma } f ( z ) - { \frac { 1 } { z } } \ d z \right| \leqslant 2 \pi M .
$$

On the other hand,

$$
\int _ { \gamma } f ( z ) - { \frac { 1 } { z } } \ d z = 0 - 2 \pi i = - 2 \pi i .
$$

Therefore $2 \pi \leqslant 2 \pi M$ , hence the result.

Alternate solution. I think these two solutions are essentially equivalent but this one feels less like a trick.

Suppose instead that $| f ( z ) - 1 / z | < 1$ for all $| z | = 1$ Let C be the unit circle. The idea is that the image of C under $1 / z$ has winding number ´1 around the origin, and if $f ( z )$ is always less than 1 away from $1 / z$ , then f should also wind C around the origin ´1 times, which is bad.

By assumption we have $| z f ( z ) - 1 | < | z | = 1$ for all $z \in C$ So the image of C under $z f ( z )$ is contained in $B ( 1 , 1 )$ , which implies it has winding number 0 around the origin. Therefore by the argument principle, $z f ( z )$ has no zeros inside D, which is impossible if $f$ is analytic. Alternatively, one can apply Rouche’s theorem to the inequality $| z f ( z ) - 1 | < | z | = 1$ to conclude that $z f ( z )$ has the same number of zeros in D as the constant function 1, which is zero (the first argument given here is essentially just a proof of Rouche’s theorem).

Problem 12a. Find a real-valued harmonic function v defined on the disk $| z | < 1$ such that $v ( z ) > 0$ and $\begin{array} { r } { \operatorname* { l i m } _ { z \to 1 } v ( z ) = \infty } \end{array}$

Solution. Define $\begin{array} { r } { v ( z ) = \log \left| \frac { z + 1 } { z - 1 } - 1 \right| } \end{array}$ . It is clear that $v ( z ) \to \infty { \mathrm { ~ a s ~ } } z \to 1$ . To see that v is harmonic in D, note that the map $\begin{array} { r } { z \mapsto \frac { z + 1 } { z - 1 } - 1 } \end{array}$ is nonvanishing on D, $\begin{array} { r } { \mathbf { s o } z \mapsto \log \left( \frac { z + 1 } { z - 1 } - 1 \right) } \end{array}$ is a well-defined analytic function on $\mathbb { D } ,$ and $\begin{array} { r } { v ( z ) = \operatorname { R e } \left( \log \left( \frac { z + 1 } { z - 1 } - 1 \right) \right) } \end{array}$ , so v is harmonic in D. To show that $v ( z ) > 0$ on D, note that $\begin{array} { r } { z \mapsto \frac { z - 1 } { z + 1 } - 1 } \end{array}$ is a conformal map from D to $\{ z \in \mathbb { C } : \operatorname { I m } ( z ) < - 1 \} , \operatorname { s o } \left| { \frac { z - 1 } { z + 1 } } - 1 \right| > 1$ for all $z \in \mathbb { D }$ and thus $v ( z ) > 0 . \quad \sqcup$

“Alternate” Solution Simply define $\begin{array} { r } { v ( z ) = - \log \left| { \frac { z - 1 } { 2 } } \right| } \end{array}$ . On the disc, $\frac { z - 1 } { 2 }$ is nonzero and holomorphic, so $v ( z )$ is harmonic. It is also non-negative since $\begin{array} { r } { \frac { z - 1 } { 2 } \dot { < } \dot { 1 } } \end{array}$ for $| z | < 1$ . The blowup near 1 is clear.

Problem 12b. Let u be a real-valued harmonic function in the disk $| z | < 1$ such that $u ( z ) \leqslant M < \infty$ and lim $\iota _ { r  1 } u ( r e ^ { i \theta } ) \leqslant 0$ for almost all θ. Show that $u ( z ) \leqslant 0$

Solution. For any $0 ~ < ~ r ~ < ~ 1$ , u is harmonic on the closed disk $| z | \leqslant r$ . So for any $0 ~ < ~ s ~ < ~ 1$ , we can use the Poisson integral formula to write

$$
u ( r s e ^ { i \theta } ) ~ = ~ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \frac { r ^ { 2 } - ( r s ) ^ { 2 } } { | r e ^ { i \phi } - r s e ^ { i \theta } | ^ { 2 } } u ( r e ^ { i \phi } ) d \phi .\tag{2}
$$

For a fixed s and θ, define

$$
g _ { r } ( \phi ) ~ = ~ \frac { r ^ { 2 } - ( r s ) ^ { 2 } } { | r e ^ { i \phi } - r s e ^ { i \theta } | ^ { 2 } } u ( r e ^ { i \phi } ) .
$$

We see that $g _ { r }$ is bounded on r0, 2πs because $u \leqslant M$ on all of D by hypothesis and $| r e ^ { i \phi } - r s e ^ { i \theta } | ^ { 2 }$ is bounded away from 0 because $s < 1$ . So say that $| g _ { r } ( \phi ) | \leqslant A$ for all $\phi \in [ 0 , 2 \pi ]$ . Therefore we can apply Fatou’s

lemma to the functions $A - g _ { r } ( \phi )$ to get

$$
\int _ { 0 } ^ { 2 \pi } \operatorname* { l i m i n f } _ { r \to 1 } ( A - g _ { r } ( \phi ) ) d \phi \ \leqslant \ \operatorname* { l i m i n f } _ { r \to 1 } \int _ { 0 } ^ { 2 \pi } ( A - g _ { r } ( \phi ) ) d \phi ,
$$

which implies that

$$
\int _ { 0 } ^ { 2 \pi } \operatorname* { l i m } _ { r \to 1 } \operatorname* { s u p } _ { } g _ { r } ( \phi ) d \phi \ \geqslant \ \operatorname* { l i m } _ { r \to 1 } \operatorname* { s u p } _ { } \int _ { 0 } ^ { 2 \pi } g _ { r } ( \phi ) d \phi .
$$

So taking the lim sup as $r \to 1$ on both sides of equation (1) yields, since u is continuous on $\mathbb { D }$

$$
u ( s e ^ { i \theta } ) = \operatorname* { l i m s u p } _ { r  1 } u ( r s e ^ { i \theta } ) = \operatorname* { l i m s u p } _ { r  1 } \int _ { 0 } ^ { 2 \pi } g _ { r } ( \phi ) d \phi \leqslant \int _ { 0 } ^ { 2 \pi } \operatorname* { l i m s u p } _ { r  1 } g _ { r } ( \phi ) d \phi = \int _ { 0 } ^ { 2 \pi } { \frac { 1 - s ^ { 2 } } { | e ^ { i \phi } - s e ^ { i \theta } | ^ { 2 } } } \operatorname* { l i m s u p } _ { r  1 } u ( r e ^ { i \phi } ) d \phi .
$$

By hypothesis, the integral on the far right is an integral of a function which is $\leqslant 0$ almost everywhere, so we have $u ( s e ^ { i \theta } ) \leqslant 0$ . This argument holds for any $0 < s < 1$ and any $\theta \in \left[ 0 , 2 \pi \right]$ , so we conclude that $u \leqslant 0$ on D. □

## 16 Fall 2016

Problem 1. We consider the space $L ^ { 1 } ( \mu )$ of integrable functions on a measure space $( X , { \mathcal { M } } , \mu )$ . For $f \in L ^ { 1 } ( \mu )$ let

$$
| | g | | _ { 1 } = \int | g ( x ) | d \mu
$$

be the corresponding $L ^ { 1 } { \mathrm { - n o r m } }$ . Suppose that $f$ and $f _ { n }$ for $n \in \mathbb { N }$ are functions in $L ^ { 1 } ( \mu )$ such that

(i) $f _ { n } ( x )  f ( x )$ for µ-almost every $x \in X$ and

(ii) $\left| \left| f _ { n } \right| \right| _ { 1 } \to \left| \left| f \right| \right| _ { 1 }$

Show that then $\vert \vert f _ { n } - f \vert \vert _ { 1 } \to 0 .$

Solution. Note that the function $| f | + | f _ { n } | - | f - f _ { n } |$ is nonnegative for all n (this just follows from the triangle inequality). Then we apply Fatou’s lemma to get

$$
\int \operatorname* { l i m i n f } _ { n \to \infty } ( | f | + | f _ { n } | - | f - f _ { n } | ) d \mu \ \leqslant \ \operatorname* { l i m i n f } _ { n \to \infty } \int ( | f | + | f _ { n } | - | f - f _ { n } | ) d \mu .
$$

Since $f _ { n }  f$ pointwise almost everywhere, the left side of the above inequality reduces to

$$
2 \int | f | d \mu .
$$

Since $\vert \vert f _ { n } \vert \vert _ { L ^ { 1 } }  \vert \vert f \vert \vert _ { L ^ { 1 } }$ as $n  \infty ,$ , the right side reduces to

$$
2 \int | f | d \mu - \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } \int | f - f _ { n } | d \mu .
$$

Together these imply that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } \int | f - f _ { n } | d \mu _ { } \ \leqslant \ 0 ,
$$

which implies that $\vert \vert f - f _ { n } \vert \vert _ { L ^ { 1 } } \to 0$ as $n \to \infty$

Problem 2. Let $\mu$ be a finite positive Borel measure on R that is singular to the Lebesgue measure. Show that

$$
\operatorname* { l i m } _ { r \to 0 ^ { + } } { \frac { \mu ( [ x - r , x + r ] ) } { 2 r } } = + \infty
$$

for µ-almost every $x \in \mathbb { R }$

Solution. Let λ be Lebesgue measure on R. It suffices to show that

$$
\operatorname* { l i m } _ { r \to 0 ^ { + } } { \frac { \lambda ( [ x - r , x + r ] ) } { \mu ( [ x - r , x + r ] ) } } = 0
$$

for µ-almost every $x \in \mathbb { R } .$ . Since λ and $\mu$ are singular, write $\mathbb { R } = A \cup A ^ { c }$ where $\lambda ( A ) = 0$ and $\mu ( A ^ { c } ) = 0$ . It suffices to just look at $x \in A$ because $\mu ( A ^ { c } ) = 0$ . Define

$$
E _ { k } \ = \ \left\{ x \in A : \operatorname* { l i m } _ { r \to 0 ^ { + } } \operatorname* { s u p } _ { \mu \left( \left[ x - r , x + r \right] \right) } > \frac { 1 } { k } \right\} .
$$

To prove the desired result it suffices to show that $\mu ( E _ { k } ) = 0$ for each fixed k. Fix $\epsilon > 0$ . By the regularity of Lebesgue measure, let V be an open set with $E _ { k } \subseteq V$ and $\lambda ( V ) < \epsilon .$ By definition of $E _ { k }$ , for each $x \in E _ { k }$ there is an open interval $I ( x ) = ( x - r ( x ) , r + r ( x ) )$ such that

$$
\frac { \lambda ( I ( x ) ) } { \mu ( I ( x ) ) } \ \geqslant \ \frac { \lambda ( [ x - r ( x ) , x + r ( x ) ] ) } { \mu ( [ x - r ( x ) , x + r ( x ) ] ) } \ > \ \frac { 1 } { k } ,
$$

and $r ( x )$ may be chosen small enough so that $I ( x ) \subseteq V$ for each $x .$ . Then $\cup _ { x \in E _ { k } } ( 1 / 5 ) I ( x )$ is a covering of $E _ { k }$ by open intervals, so by the Vitali covering lemma, we can pick a countable subcollection $\{ ( 1 / 5 ) I ( x _ { n } ) \}$ which is pairwise disjoint and satisfies

$$
E _ { k } \ \subseteq \ \bigcup _ { x \in E _ { k } } ( 1 / 5 ) I ( x ) \ \subseteq \ \bigcup _ { n = 1 } ^ { \infty } I ( x _ { n } ) .
$$

Therefore we have the estimate

$$
\mu ( E _ { k } ) \ \leqslant \ \sum _ { n = 1 } ^ { \infty } \mu ( I ( x _ { n } ) ) \ \leqslant \ k \sum _ { n = 1 } ^ { \infty } \lambda ( I ( x _ { n } ) ) \ = \ k \lambda \left( \bigcup _ { n = 1 } ^ { \infty } I ( x _ { n } ) \right) \ \leqslant \ k \lambda ( V ) \ < \ k \epsilon .
$$

Since $\mu ( E _ { k } )$ is independent of $\epsilon ,$ we may take $\epsilon \to 0$ and conclude that $\mu ( E _ { k } ) = 0$ , so we are done.

Problem 3a. If X is a compact metric space, we denote by ${ \mathcal { P } } ( X )$ the set of all positive Borel measures $\mu$ on X with $\mu ( X ) = 1$ . Let $\phi : X  [ 0 , \infty ]$ be lower semicontinuous function on $X$ . Show that if $\mu$ and $\mu _ { n }$ are in ${ \mathcal { P } } ( X )$ and $\mu _ { n }  \mu$ with respect to the weak-star topology on ${ \mathcal { P } } ( X )$ , then

$$
\int \phi d \mu \leqslant \operatorname* { l i m i n f } _ { n  \infty } \int \phi d \mu _ { n } .
$$

Solution. Since $\phi$ is lower semicontinuous, we can write it as a monotonically increasing limit of continuous functions, and since $\phi \geqslant 0$ we may also take these continuous functions to be nonnegative. So say that $0 \leqslant f _ { k } \nearrow \phi$ as $k  \infty$ Then, by definition of weak-˚ convergence of measures and applying the Monotone Convergence Theorem twice, we have

$$
\int \phi d \mu ~ = ~ \operatorname* { l i m } _ { k \to \infty } \int f _ { k } d \mu ~ = ~ \operatorname* { l i m } _ { k \to \infty } \operatorname* { l i m } _ { n \to \infty } \int f _ { k } d \mu _ { n } ~ \leqslant ~ \operatorname* { l i m } _ { n \to \infty } \operatorname* { l i m } _ { k \to \infty } \int f _ { k } d \mu _ { n } ~ = ~ \operatorname* { l i m i n f } _ { n \to \infty } \int \phi d \mu _ { n } .
$$

The interchange of the limits with the inequality is justified by the following statement:

Let $\{ a _ { n , k } \} _ { n , k = 1 } ^ { \infty }$ be nonnegative numbers such that lim $\scriptstyle { \mathcal { n } } \to \infty \displaystyle a _ { n , k }$ and li $1 _ { k \to \infty } a _ { n , k }$ both exist for each fixed k and n respectively, lim $\scriptstyle { 1 _ { k } } \to \infty \operatorname* { l i m } _ { n \to \infty } a _ { n , k }$ exists, and for each fixed $n , \ a _ { n , k }$ is increasing in k. Then lim $\begin{array} { r } { { 1 } _ { k \to \infty } \operatorname* { l i m } _ { n \to \infty } a _ { n , k } \leqslant } \end{array}$ lim $\scriptstyle \operatorname { n f } _ { n \to \infty } \operatorname* { l i m } _ { k \to \infty } a _ { n , k }$

Proof: Define

$$
b _ { n } \ : = \ \operatorname* { l i m } _ { k \to \infty } a _ { n , k } \qquad c _ { k } \ : = \ \operatorname* { l i m } _ { n \to \infty } a _ { n , k } \qquad L \ : = \ \operatorname* { l i m } _ { k \to \infty } c _ { k } .
$$

Fix $\epsilon > 0 .$ . Let K be big enough so that $c _ { K } > L - \epsilon$ . By the increasing condition, we have $b _ { n } \geqslant a _ { n , K }$ for each n. Therefore

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { } b _ { n } \ \geqslant \ \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { } a _ { n , K } \ = \ c _ { K } \ > \ L - \epsilon .
$$

Since lim in $\textstyle \mathrm { f } _ { n \to \infty } b _ { n }$ does not depend on , we conclude that lim in $\mathrm { f } _ { n \to \infty } b _ { n } \geqslant L$

Problem 3b. Let $K \subseteq \mathbb { R } ^ { d }$ be a compact set. For $\mu \in { \mathcal { P } } ( K )$ , define

$$
{ \cal E } ( \mu ) ~ = ~ \int _ { K } \int _ { K } { \frac { 1 } { | x - y | } } d \mu ( x ) d \mu ( y ) .
$$

Show that the function $E : \mathcal { P } ( K )  [ 0 , \infty ]$ attains its minimum on $\mathcal { P } ( K )$ (which could possibly be infinity).

Solution. See Spring 2013 # 4

Problem 4. Let $L ^ { 1 } = L ^ { 1 } ( [ 0 , 1 ] )$ be the space of integrable functions and $L ^ { 2 } \ = \ L ^ { 2 } ( [ 0 , 1 ] )$ be the space

of square-integrable functions on $[ 0 , 1 ]$ . Then $L ^ { 2 } \subset L ^ { 1 }$ . Show that $L ^ { 2 }$ is a meager subset of $L ^ { 1 } . , \mathrm { i . e . , } L ^ { 2 }$ can be written as a countable union of sets in $L ^ { 1 }$ that are closed and have empty interior in $L ^ { 1 }$

Solution. Write

$$
L ^ { 2 } \ = \ \bigcup _ { N = 1 } ^ { \infty } \left\{ f \in L ^ { 1 } : \int _ { 0 } ^ { 1 } | f | ^ { 2 } \leqslant N \right\} \ = : \ E _ { N } .
$$

To show that $L ^ { 2 }$ is a meager subset of $L ^ { 1 }$ , it suffices to show that each $E _ { N }$ is closed and nowhere dense with respect to the $L ^ { 1 }$ norm. To show $E _ { N }$ is closed, let $f _ { k }$ be a sequence in $E _ { N }$ and suppose that $f _ { k }  f$ in the $L ^ { 1 }$ norm. This implies that a subsequence converges to $f$ almost everywhere, so by relabeling if necessary we may just assume that $f _ { k }  f$ almost everywhere, so also $| f _ { k } | ^ { 2 }  | { \check { f } } | ^ { 2 }$ almost everywhere. Therefore by Fatou’s lemma we have

$$
\int _ { 0 } ^ { 1 } | f | ^ { 2 } \ = \ \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { k \to \infty } | \operatorname* { i f } _ { k } | ^ { 2 } \ = \ \operatorname* { l i m } _ { k \to \infty } \operatorname* { i n f } _ { 0 } \int _ { } ^ { 1 } | f _ { k } | ^ { 2 } \ \leqslant \ N ,
$$

so $f \in E _ { N }$ . Thus $E _ { N }$ is closed.

To show $E _ { N }$ is nowhere dense, fix $f \in E _ { N }$ and $\epsilon > 0$ It suffices to find a function $g$ such that $g \notin E _ { N }$ and $| | g - f | | _ { L ^ { 1 } } < \epsilon$ . Define $g ( x ) = f ( x ) + \epsilon x ^ { - 1 / 2 }$ . It is clear that $g \notin E _ { N }$ because if $g$ were in $L ^ { 2 }$ , then $x ^ { - 1 / 2 }$ would also be, which is a contradiction. It is also clear that

$$
| | g - f | | _ { L ^ { 1 } } \ = \ \epsilon \int _ { 0 } ^ { 1 } x ^ { - 1 / 2 } d x \ = \ 2 \epsilon ,
$$

so we are done.

Problem 5. Let $X = C ( [ 0 , 1 ] )$ be the Banach space of real valued continuous functions on r0, 1s equipped with the sup norm. Let A be the Borel σ-algebra on X. Show that A is the smallest σ-algebra on X that contains all sets of the form

$$
S ( t , B ) \ = \ \{ f \in X : f ( t ) \in B \}
$$

for $t \in [ 0 , 1 ]$ and B a Borel subset of R.

Solution. First we show that each set of the form $S ( t , B )$ is actually a Borel set in X. Note that for each t, the evaluation map $\phi _ { t } : X \to \mathbb { R }$ given by $f \mapsto f ( t )$ is a bounded linear functional on X because $| f ( t ) | \leqslant | | f | | _ { X }$ Therefore $\phi _ { t }$ is a continuous function $X  \mathbb { R }$ , and since $S ( t , B ) = \phi _ { t } ^ { - 1 } ( B )$ where B is a Borel set in R, we see that $S ( t , B )$ must be a Borel set in X.

Let $\mathcal { F }$ denote the σ-algebra generated by the sets of the form $S ( t , B )$ To show that ${ \mathcal { F } } = A ,$ it suffices to show that every closed neighborhood in X is in ${ \mathcal F } .$ . So fix $g \in X$ and $\epsilon > 0$ . We need to show that $E : = \left\{ f \in X : \left| | f - g | \right| _ { X } \leqslant \epsilon \right\}$ is an element of $\mathcal { F }$ . For any $q \in \mathbb { Q } \cap [ 0 , 1 ]$ , define $B _ { q } ~ : = ~ \left[ g ( q ) - \epsilon , g ( q ) + \epsilon \right]$ It is clear that $B _ { q }$ is a Borel subset of R. Now we claim that

$$
{ \cal E } ~ = ~ \bigcap _ { q \in \mathbb { Q } \cap [ 0 , 1 ] } { \cal S } ( q , B _ { q } ) .
$$

Proving this is enough to conclude that E is an element of ${ \mathcal { F } } ,$ so this will finish the problem.

If $f \in E ,$ then $| | f - g | | _ { X } \leqslant \epsilon .$ so in particular $| f ( q ) - g ( q ) | \leqslant \epsilon$ for every $q \in \mathbb { Q } \cap [ 0 , 1 ]$ , which implies that $f ( q ) \in B _ { q }$ for every q, so $f$ is an element of the set on the right side of the above equation. Conversely, let $f$ be an element of the right side and suppose that $f \notin E$ Then we have $| f ( x ) - g ( x ) | > \epsilon$ for some $x \in [ 0 , 1 ]$ , and since $f$ and $g$ are both continuous, we can find a rational number q near x such that $| f ( q ) - g ( q ) | > \epsilon .$ , which contradicts the assumption that $f \in S ( q , B _ { q } )$ . Therefore we conclude that $\begin{array} { r } { E \ = \ \bigcap _ { q \in \mathbb { Q } \cap \{ 0 , 1 \} } S ( q , B _ { q } ) \in \mathcal { F } } \end{array}$ , so we are done. □

Problem 6a. Consider the Banach space $\ell ^ { 1 }$ consisting of all sequences $u = \left\{ x _ { i } \right\}$ in R with

$$
| | u | | _ { \ell ^ { 1 } } = \sum _ { i = 1 } ^ { \infty } | x _ { i } | < \infty
$$

and the Banach space $\ell ^ { \infty }$ consisting of all sequences $v = \{ y _ { i } \}$ in R with

$$
| | v | | _ { \ell ^ { \infty } } = \operatorname* { s u p } _ { i \in \mathbb { N } } | y _ { i } | < \infty .
$$

There is a well-defined dual pairing between $\ell ^ { 1 }$ and $\ell ^ { \infty }$ given by

$$
\langle u , v \rangle \ = \ \sum _ { i = 1 } ^ { \infty } x _ { i } y _ { i }
$$

for $u = \{ x _ { i } \} \in \ell ^ { 1 }$ and $v = \{ y _ { i } \} \in \ell ^ { \infty }$ . With this dual pairing, $\ell ^ { \infty } = ( \ell ^ { 1 } ) ^ { * }$ is the dual space of $\ell ^ { 1 }$

Show that there exists no sequence $\left\{ u _ { n } \right\}$ in $\ell ^ { 1 }$ such that $\lvert | u _ { n } \rvert | _ { \ell ^ { 1 } } \geqslant 1$ for all n and $\langle u _ { n } , v \rangle \to 0$ for each $v \in \ell ^ { \infty }$

Solution. Let $\left\{ u _ { n } \right\}$ be a sequence in $\ell ^ { 1 }$ satisfying $\lvert | u _ { n } \rvert | _ { \ell ^ { 1 } } \geqslant 1$ for all n. We can assume by scaling that $\vert \vert u _ { n } \vert \vert _ { \ell ^ { 1 } } = 1$ for each n because scaling the sequences down can only decrease $\langle u _ { n } , v \rangle$ for any $v \in \ell ^ { \infty }$ . Suppose that $\langle u _ { n } , v \rangle \to 0$ as $n \to \infty$ for all $v \in \ell ^ { \infty }$ . We will get a contradiction by constructing a sequence $v \in \ell ^ { \infty }$ such that $\langle u _ { n } , v \rangle$ is bounded away from zero infinitely often.

First note that by letting v be the sequence which has a 1 in the jth spot and 0 everywhere else, we know that $( u _ { n } ) _ { j } \to 0$ as $n  \infty$ for each fixed j. Also note that since $\lvert | u _ { n } \rvert | _ { \ell ^ { 1 } } = 1$ for each $n ,$ necessarily $| | u _ { n } | | _ { \ell ^ { \infty } } \leqslant 1$ for all n. Now, for any fixed $\epsilon \in ( 0 , 1 / 2 )$ , we can do the following construction:

Pick $J _ { 1 }$ to be large enough so that

$$
\sum _ { j \in [ 1 , J _ { 1 } ] } | ( u _ { 1 } ) _ { j } | \ > \ 1 - \epsilon .
$$

Now, since we know that $( u _ { n } ) _ { j }$ tends to zero in each slot individually, pick $N _ { 1 }$ to be large enough so that

$$
\operatorname* { m a x } ( | ( u _ { N _ { 1 } } ) _ { 1 } | , \ldots , | ( u _ { N _ { 1 } } ) _ { J _ { 1 } } | ) \ < \ \frac { \epsilon } { 2 J _ { 1 } } .
$$

Then we see that

$$
\sum _ { j \in [ 1 , J _ { 1 } ] } | ( u _ { N _ { 1 } } ) _ { j } | \ < \ \epsilon / 2 ,
$$

so we may pick $J _ { 2 }$ such that

$$
\sum _ { j \in [ J _ { 1 } + 1 , J _ { 2 } ] } \left. ( u _ { N _ { 1 } } ) _ { j } \right. > 1 - \epsilon .
$$

Now pick $N _ { 2 }$ to be large enough so that

$$
\operatorname* { m a x } ( | ( u _ { N _ { 2 } } ) _ { 1 } | , \ldots , | ( u _ { N _ { 2 } } ) _ { J _ { 2 } } | ) \ < \ \frac { \epsilon } { 2 J _ { 2 } } .
$$

We may repeat this process indefinitely, and so we obtain a sequence $\{ N _ { k } \}$ and a sequence $\left\{ J _ { k } \right\}$ such that for each k

$$
\sum _ { j \in [ J _ { k } + 1 , J _ { k + 1 } ] } \lvert ( u _ { N _ { k } } ) _ { j } \rvert > 1 - \epsilon .
$$

Now, letting spxq denote the function which is 1 if $x \geqslant 0$ and ´1 if $x < 0$ , define the sequence $v \in \ell ^ { \infty }$ by

$$
( v ) _ { j } \ = \ s ( ( u _ { N _ { k } } ) _ { j } ) { \mathrm { w h e n } } \ j \in [ J _ { k } + 1 , J _ { k + 1 } ] .
$$

Note that each $( v ) _ { j }$ is an entry of some $u _ { n } .$ , so we have $| | v | | _ { \ell ^ { \infty } } \leqslant 1$ . By construction, for each k we have

$$
\begin{array} { l } { { \displaystyle \sum _ { j \in [ J _ { k } + 1 , J _ { k + 1 } ] } ( u _ { N _ { k } } ) _ { j } ( v ) _ { j } \ = \ \sum _ { j \in [ J _ { k } + 1 , J _ { k + 1 } ] } \ | ( u _ { N _ { k } } ) _ { j } | \ > \ 1 - \epsilon , } } \\ { { \displaystyle \mathrm { s o } } } \\ { { \displaystyle \langle u _ { N _ { k } } , v \rangle \ = \ \sum _ { \substack { j \in [ J _ { k } + 1 , J _ { k + 1 } ] } } ( u _ { N _ { k } } ) _ { j } ( v ) _ { j } \ + \sum _ { \substack { j \in [ J _ { k } + 1 , J _ { k + 1 } ] } } ( u _ { N _ { k } } ) _ { j } ( v ) _ { j } \ \geqslant \ 1 - \epsilon - \| v \| _ { \ell ^ { \infty } \atop j \in [ J _ { k } + 1 , J _ { k + 1 } ] } \ \sum _ { \substack { l ( u _ { N _ { k } } ) _ { j } \in [ J _ { k } + 1 , J _ { k + 1 } ] } } | ( u _ { N _ { k } } ) _ { j } | \ > \ 1 - 2 \epsilon . } } \end{array}
$$

Therefore, picking (for example) $\epsilon = 1 / 3$ , we see that $\langle u _ { N _ { k } } , v \rangle$ is bounded away from zero for every k, which is our contradiction. (Note: I would really prefer a nicer, non-constructive solution)

Problem 6b. Show that every weakly convergent sequence $\left\{ u _ { n } \right\}$ in $\ell ^ { 1 }$ converges in the norm topology of $\ell ^ { 1 }$ .

Solution. Suppose that $u _ { n } \ \to \ u$ weakly in $\ell ^ { 1 }$ . This means that $\phi ( u _ { n } )  \phi ( u )$ for every bounded linear functional $\phi \in ( \ell ^ { 1 } ) ^ { * }$ , and by the given dual pairing this means that $\langle u _ { n } , v \rangle  \langle u , v \rangle$ for every $v \in \ell ^ { \infty }$ , i.e. $\langle u _ { n } - u , v \rangle \to 0$ for every $v \in \mathcal { \ell } ^ { \infty }$ . Suppose that $u _ { n }$ did not converge to u in the norm topology on $\ell ^ { 1 }$ . Then there is a subsequence $u _ { n _ { k } }$ and a $\delta > 0$ such that $| | u _ { n _ { k } } - u | | _ { \ell ^ { 1 } } \geqslant \delta$ for all k. Replacing $u _ { n _ { k } } \ : - \ : u$ with $( 1 / \delta ) ( u _ { n _ { k } } - u )$ if necessary, we may assume that $| | u _ { n _ { k } } - u | | _ { \ell ^ { 1 } } \geqslant 1$ for all k. But we still must have $\langle u _ { n _ { k } } - u , v \rangle \to 0$ for every $v \in \ell ^ { \infty }$ , which contradicts part (a). Therefore we must have $u _ { n } \to u$ in the norm topology on \`1. □

Problem 7a. Let H be the space of holomorphic functions f on D such that

$$
\int _ { \mathbb { D } } | f ( z ) | ^ { 2 } d A ( z ) < \infty .
$$

Here integration is with respect to Lebesgue measure A on D. The vector space H is a Hilbert space if equipped with the inner product

$$
\langle f , g \rangle \ = \ \int _ { \mathbb { D } } f ( z ) { \overline { { g ( z ) } } } d A ( z )
$$

for $f , g \in { \mathcal { H } }$ . Fix $z _ { 0 } \in \mathbb { D }$ and define $L _ { z _ { 0 } } ( f ) = f ( z _ { 0 } )$ for $f \in \mathcal H$

Show that $L _ { z _ { 0 } } : \mathcal { H } \to \mathbb { C }$ is a bounded linear functional on H.

Solution. It’s obvious that $L _ { z _ { 0 } }$ is a linear functional. For $z _ { \mathrm { 0 } }$ fixed, let $\delta > 0$ be small enough so that $B ( z _ { 0 } , \delta ) \subseteq \mathbb { D }$ . Then for any $f \in \mathcal H$ , we have by the mean value formula

$$
\begin{array} { r l } & { | L _ { z _ { 0 } } ( f ) | = | f ( z _ { 0 } ) | = \displaystyle \left| \frac { 1 } { \pi \delta ^ { 2 } } \int _ { B ( z _ { 0 } , \delta ) } f ( z ) d A ( z ) \right| \leqslant \displaystyle \frac { 1 } { \pi \delta ^ { 2 } } \int _ { B ( z _ { 0 } , \delta ) } | f ( z ) | d A ( z ) \leqslant \displaystyle \frac { 1 } { \pi \delta ^ { 2 } } \int _ { \mathbb D } | f ( z ) | d A ( z ) } \\ & { \leqslant \displaystyle \frac { 1 } { \pi \delta ^ { 2 } } \left( \int _ { \mathbb D } 1 ^ { 2 } d A ( z ) \right) ^ { 1 / 2 } \left( \int _ { \mathbb D } | f ( z ) | ^ { 2 } d A ( z ) \right) ^ { 1 / 2 } \quad \mathrm { b y ~ C a u c h y - S c h w a r z } } \\ & { \leqslant \displaystyle \frac { 1 } { \sqrt { \pi \delta ^ { 2 } } } | | f | | _ { \mathcal H } , } \end{array}
$$

so $L _ { z _ { 0 } }$ is a bounded linear functional.

Problem 7b. Find an explicit function $g _ { z _ { 0 } } \in \mathcal { H }$ such that

$$
L _ { z _ { 0 } } ( f ) ~ = ~ f ( z _ { 0 } ) ~ = ~ \langle f , g _ { z _ { 0 } } \rangle
$$

for all $f \in \mathcal H$

Solution. Note that such a $g _ { z _ { 0 } }$ exists for each $z _ { 0 } ~ \in ~ \mathbb { D }$ by the Riesz representation theorem. First we claim that the set

$$
\left\{ e _ { n } ( z ) : = { \sqrt { \frac { n + 1 } { \pi } } } z ^ { n } \right\}
$$

is an orthonormal basis for H. It’s easy to compute directly using polar coordinates that it’s an orthonormal set. To show it’s a basis, it’s enough to show that $\langle f , e _ { n } \rangle = 0$ for all n implies $f = 0$ . We compute

$$
\langle f , e _ { n } \rangle ~ = ~ C ( n ) \int _ { \mathbb { D } } f ( z ) { \overline { { z ^ { n } } } } d A ( z ) ~ = ~ C ( n ) \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 2 \pi } f ( r e ^ { i \theta } ) r ^ { n + 1 } e ^ { - i n \theta } d \theta d r .
$$

The Cauchy integral formula gives

$$
f ^ { ( n ) } ( 0 ) ~ = ~ C ( n ) \int _ { 0 } ^ { 2 \pi } \frac { f ( r e ^ { i \theta } ) } { r ^ { n + 1 } e ^ { i ( n + 1 ) \theta } } r e ^ { i \theta } d \theta .
$$

Combining these two we can observe that

$$
\langle f , e _ { n } \rangle ~ = ~ C ( n ) \int _ { 0 } ^ { 1 } r ^ { 2 n + 1 } f ^ { ( n ) } ( 0 ) d r ~ = ~ C ( n ) f ^ { ( n ) } ( 0 ) .
$$

$( C ( n )$ is a constant in terms of n that is different from line to line). This implies that $\langle f , e _ { n } \rangle = 0$ implies $f ^ { ( n ) } ( 0 ) = 0$ Therefore because holomorphic functions have power series expansions, $\langle f , e _ { n } \rangle = 0$ for all n implies $f = 0$ . This shows that the $e _ { n }$ form an orthonormal basis for $\mathcal { H } .$

Now we determine $g _ { z _ { 0 } }$ . For $z \in \mathbb { D }$ we have

$$
\begin{array} { r c l } { { g _ { z _ { 0 } } ( z ) ~ = ~ \displaystyle \langle g _ { z _ { 0 } } , g _ { z } \rangle ~ = ~ \displaystyle \sum _ { n = 0 } ^ { \infty } \langle g _ { z _ { 0 } } , e _ { n } \rangle \overline { { { \langle g _ { z } , e _ { n } \rangle } } } ~ \mathrm { b y ~ P a r s e v a l } } } \\ { { } } & { { ~ } } & { { ~ } } \\ { { } } & { { ~ = ~ \displaystyle \sum _ { n = 0 } ^ { \infty } \overline { { { \langle e _ { n } , g _ { z _ { 0 } } \rangle } } } \langle e _ { n } , g _ { z } \rangle ~ ( e _ { n } , g _ { z } \rangle ~ = ~ \displaystyle \sum _ { n = 0 } ^ { \infty } \overline { { { e _ { n } ( z _ { 0 } ) } } } e _ { n } ( z ) } } \\ { { } } & { { ~ } } & { { ~ } } \\ { { } } & { { ~ = ~ \displaystyle \sum _ { n = 0 } ^ { \infty } \frac { n + 1 } { \pi } ( \overline { { { z _ { 0 } } } } z ) ^ { n } ~ = ~ \displaystyle \frac { 1 } { \pi ( 1 - \overline { { { z _ { 0 } } } } z ) ^ { 2 } } . ~ \Omega } } \end{array}
$$

Problem $\mathbf { 8 a } .$ . Let $f$ be a continuous complex-valued function on $\overline { { \mathbb { D } } }$ which is holomorphic on D and $f ( 0 ) \neq 0$ Show that if $0 < r < 1$ and inf $_ { | z | = r } \left| f ( z ) \right| > 0$ , then

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log \left| f ( r e ^ { i \theta } ) \right| d \theta \ \geqslant \ \log \left| f ( 0 ) \right| .
$$

Solution. Let $r$ be such that inf $\dot { \left| z \right| } = r \left| f ( z ) \right| > 0$ . Since $f$ is not identically zero, it has only finitely many zeros inside the disc $| z | < r$ . Denote them by $a _ { 1 } , \ldots , a _ { n } .$ . Define the function

$$
g ( z ) ~ = ~ \left( { \frac { r ( z - a _ { 1 } ) } { r ^ { 2 } - { \overline { { a _ { 1 } } } } z } } \right) \cdot \cdot \cdot \left( { \frac { r ( z - a _ { n } ) } { r ^ { 2 } - { \overline { { a _ { n } } } } z } } \right) .
$$

We know that $| g ( z ) | = 1$ for all $| z | = r$ and g has the same zeros as $f$ and no poles in $| z | \leqslant r$ Therefore the function $f / g$ is a nonvanishing holomorphic function on $| z | < r$ with $| f ( z ) / g ( z ) | = | f ( z ) |$ for $| z | = r .$ Since it is nonvanishing we know that it has a holomorphic single-valued logarithm, so log $| f ( z ) / g ( z ) | =$ $\operatorname { R e } ( \log ( f ( z ) / g ( z ) ) )$ q is harmonic in $| z | < r$ . Therefore we can apply the mean value property to log $| f / g |$ to obtain

$$
\log \left| { \frac { f ( 0 ) } { g ( 0 ) } } \right| ~ = ~ { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log \left| { \frac { f ( r e ^ { i \theta } ) } { g ( r e ^ { i \theta } ) } } \right| d \theta ~ = ~ { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log \left| f ( r e ^ { i \theta } ) \right| d \theta .
$$

We compute

$$
\log \left| { \frac { f ( 0 ) } { g ( 0 ) } } \right| ~ = ~ \log \left| f ( 0 ) \right| - \sum _ { j = 1 } ^ { n } \log \left| { \frac { a _ { j } } { r } } \right| .
$$

Since each $| a _ { j } | < r ,$ we have log $| a _ { j } / r | < 0$ and therefore

$$
\log | f ( 0 ) | \ \leqslant \ { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log { \big | } f ( r e ^ { i \theta } ) { \big | } \ d \theta . \quad \boxed { \begin{array} { r l } \end{array} }
$$

Problem 8b. Show that $\left| \{ \theta \in [ 0 , 2 \pi ] : f ( e ^ { i \theta } ) = 0 \} \right| = 0$ , where $| E |$ denotes the Lebesgue measure of $E .$

Solution. Let $E = \{ \theta \in [ 0 , 2 \pi ] : f ( e ^ { i \theta } ) = 0 \}$ Suppose that $| E | > 0$ Since $\overline { { \mathbb { D } } }$ is compact, we know that $f$ is uniformly continuous on ${ \overline { { \mathbb { D } } } } .$ Fix $\epsilon > 0$ Then we know that there is some $r _ { \epsilon } ~ > ~ 0$ such that $| f ( r _ { \epsilon } e ^ { i \theta } ) | < \epsilon$ for every $\theta \in E$ . We can also say $| f | \leqslant M$ on ${ \overline { { \mathbb { D } } } } .$ . Now we have the following estimate:

$$
\int _ { 0 } ^ { 2 \pi } \log \big | f ( r _ { \epsilon } e ^ { i \theta } ) \big | \ d \theta \ = \ \int _ { E } \log \big | f ( r _ { \epsilon } e ^ { i \theta } ) \big | \ d \theta + \int _ { E ^ { \epsilon } } \log \big | f ( r _ { \epsilon } e ^ { i \theta } ) \big | \ d \theta \ \leqslant \ | E | \log ( \epsilon ) + 2 \pi \log ( M ) .
$$

But since $f ( 0 ) \neq 0$ , we can pick $\epsilon > 0$ small enough so that the right side above is smaller than 2π log ş $| f ( 0 ) |$ but part (a) says that we must have $\int _ { 0 } ^ { 2 \pi } \log \left| f ( r e ^ { i \theta } ) \right| d \theta \geqslant 2 \pi \log \left| f ( 0 ) \right|$ for any $r > 0$ , so this is a contradiction.

Alternate Solution. Since $f$ is continuous on the compact set ${ \overline { { \mathbb { D } } } } ,$ we can say $| f | \leqslant M$ Thus log |f| takes values in $[ - \infty , M ]$ . Let $g _ { r } ( \theta ) = M - \log | f ( r e ^ { i \theta } )$ |. Then each $g _ { r }$ for $0 < r < 1$ takes values in r0, 8s, so we can apply Fatou’s lemma:

$$
\begin{array}{c}  2 \pi M - \int _ { 0 } ^ { 2 \pi } \operatorname* { l i m } _ { r  1 } \log | f ( r e ^ { i \theta } ) d \theta \ \leqslant \ \operatorname* { l i m i n f } _ { r  1 } \int _ { 0 } ^ { 2 \pi } g _ { r } ( \theta ) d \theta  \\ { 2 \pi M - \int _ { 0 } ^ { 2 \pi } \operatorname* { l i m s u p } _ { r  1 } \log | f ( r e ^ { i \theta } ) | d \theta \ \leqslant \ 2 \pi M - \operatorname* { l i m s u p } _ { r  1 } \int _ { 0 } ^ { 2 \pi } \log | f ( r e ^ { i \theta } ) | d \theta } \\ { \int _ { 0 } ^ { 2 \pi } \log | f ( e ^ { i \theta } ) | d \theta \ \geqslant \ \operatorname* { l i m s u p } _ { r  1 } \int _ { 0 } ^ { 2 \pi } \log | f ( r e ^ { i \theta } ) | d \theta \ \geqslant \ 2 \pi \log | f ( 0 ) | \ > \ - \infty } \end{array}
$$

by part (a). But if E had positive measure, then the integral on the left side would be $- \infty .$ , a contradiction. □

Problem 9a. Let $\mu$ be a positive Borel measure on r0, 1s with $\mu ( [ 0 , 1 ] ) = 1$ . Show that the function $f$ defined as

$$
f ( z ) = \int _ { [ 0 , 1 ] } e ^ { i z t } d \mu ( t )
$$

for $z \in \mathbb { C }$ is holomorphic on $\mathbb { C }$

Solution. For $h _ { k } \in \mathbb { C }$ with $| h _ { k } | \to 0$ we have

$$
\frac { 1 } { h } ( f ( z + h _ { k } ) - f ( z ) ) = \int _ { [ 0 , 1 ] } e ^ { i z t } \cdot \frac { e ^ { i h _ { k } t } - 1 } { h _ { k } } d \mu ( t )
$$

Notice that

$$
\operatorname* { l i m } _ { k  \infty } { \frac { e ^ { i h _ { k } t } - 1 } { h _ { k } } } = ( { \frac { d } { d z } } e ^ { i t z } ) ( 0 ) = i t .
$$

Thus for fixed $z ,$ the magnitude of the integrand is bounded by $2 \operatorname* { s u p } _ { t \in [ 0 , 1 ] } | e ^ { i z t } | < \infty$ for k large enough. By dominated convergence, we have

$$
f ^ { \prime } ( z ) = \int _ { [ 0 , 1 ] } i t e ^ { i z t } d \mu ( t ) .
$$

Note that all functions in question are continuous, and hence Borel measurable, so applying dominated convergence was justified.

Alternate solution. We are motivated by the fact that if f is holomorphic it should have ş $f ^ { \prime } ( z ) \ =$ $\int _ { 0 } ^ { 1 } i t e ^ { i z t } d \mu ( t )$ . We estimate, for a fixed z,

$$
\begin{array} { r l r } { \displaystyle \left. \frac { 1 } { h } ( f ( z + h ) - f ( z ) ) - \int _ { 0 } ^ { 1 } i t e ^ { i z t } d \mu ( t ) \right. ~ = ~ \displaystyle \left. \frac { 1 } { h } \int _ { 0 } ^ { 1 } ( e ^ { i ( z + h ) t } - e ^ { i z t } - i h t e ^ { i z t } ) d \mu ( t ) \right. } & { } & \\ { \leqslant ~ \displaystyle \frac { 1 } { | h | } \int _ { 0 } ^ { 1 } \left. e ^ { i z t } \right. \left. e ^ { i h t } - ( 1 + i h t ) \right. d \mu ( t ) . } & { } & \end{array}
$$

We can pick $| h |$ to be small enough so that $\left| e ^ { i h t } - ( 1 + i h t ) \right| \leqslant C \left| i h t \right| ^ { 2 } = C t ^ { 2 } | h | ^ { 2 }$ for some absolute constant C. Then we have

$$
| \frac { 1 } { h } ( f ( z + h ) - f ( z ) ) - \int _ { 0 } ^ { 1 } i t e ^ { i z t } d \mu ( t ) | \leqslant  \frac { 1 } { | h | } C | h | ^ { 2 } \int _ { 0 } ^ { 1 } ( e ^ { | z | } ) ^ { t } t ^ { 2 } d \mu ( t ) \ \leqslant \ C e ^ { | z | } | h | \int _ { 0 } ^ { 1 } d \mu ( t ) \ = \ C e ^ { | z | } | h | ,
$$

which tends to 0 as $| h |  0$ , so we conclude that $f ^ { \prime } ( z ) = \int _ { 0 } ^ { 1 } i t e ^ { i z t } d \mu ( t )$

Problem 9b. Suppose that there exists $n \in \mathbb { N }$ such that

$$
\operatorname* { l i m } _ { | z | \to \infty } | f ( z ) | / | z | ^ { n } < \infty
$$

Show that then $\mu$ is equal to the Dirac measure $\delta _ { 0 }$ at 0.

Solution. By the given condition, we have for large |z| that $| f ( z ) | < C | z | ^ { n }$ for some constant C. Since $f$ is polynomially bounded and holomorphic, f must in fact be a polynomial.

For z real,

$$
| f ( z ) | \leqslant \int _ { [ 0 , 1 ] } | e ^ { i z t } | d \mu ( t ) \leqslant 1 .
$$

But a polynomial which is bounded on the real line must be constant. Since $f ( 0 ) = 1$ , we have $f ( z ) = 1$ for all z.

For real $z ,$ we must therefore have equality in the rightmost inequality above. This occurs only if $e ^ { i z t }$ is real, outside a subset of $[ 0 , 1 ]$ with measure 0. However $e ^ { i z t }$ is real only for t an integer multiple of $\pi k / z$ . It follows that the set of multiples $M _ { z }$ of $\pi k / z$ has µ-measure 1 for all z. But $M _ { z }$ and $M _ { \sqrt { 2 } z }$ intersect only at 0, so we must have $\mu ( \{ 0 \} ) = 1$ . (Is there a nicer way to finish off the problem?)

Alternate solution. Using the same argument from above, we know that f is a polynomial of degreeş n and the derivatives of $f$ are given by $f ^ { ( j ) } ( z ) = \int _ { 0 } ^ { 1 } ( i t ) ^ { j } e ^ { i z t } d \mu ( t )$ . Since it’s a polynomial of degree $n ,$ the $( n + 1 )$ st derivative is identically zero, so

$$
\int _ { 0 } ^ { 1 } t ^ { n + 1 } e ^ { i z t } d \mu ( t ) \ = \ 0
$$

for all $z \in \mathbb { C } .$ If $\mu$ is not a point mass at 0, then $\mu ( 0 , 1 ] > 0$ , so by continuity, $\mu [ \delta , 1 ] > 0$ for some $\delta > 0$ Then taking $z = - i$ we have

$$
0 ~ = ~ \int _ { 0 } ^ { 1 } t ^ { n + 1 } e ^ { t } d \mu ( t ) ~ \geqslant ~ \int _ { \delta } ^ { 1 } t ^ { n + 1 } e ^ { t } d \mu ( t ) ~ \geqslant ~ \delta ^ { n + 1 } e ^ { \delta } \mu [ \delta , 1 ] ~ > ~ 0 ,
$$

a contradiction.

Problem 10 a. Consider the quadratic polynomial $f ( z ) = z ^ { 2 } - 1$ on C. We are interested in the iterates $f ^ { n }$ of $f$ for $n \in \mathbb { N }$ . Find an explicit constant $M > 0$ such that the following dichotomy holds for each

point $z \in \mathbb { C } \colon$ either $( \mathrm { i } ) \ \left| f ^ { n } ( z ) \right| \to \infty \ \mathrm { a s } \ n \to \infty$ or (ii) $| f ^ { n } ( z ) | \leqslant M$ for all $n \in  { \mathbb { N } } _ { 0 }$

Solution. We take M “ 2. For $| z | \geqslant 2$ , we have

$$
\begin{array} { l } { \displaystyle | f ( z ) | = | z ^ { 2 } - 1 | } \\ { \displaystyle = \left| z - \frac 1 z \right| \cdot | z | } \\ { \displaystyle \geqslant \left( | z | - \frac 1 { | z | } \right) \cdot | z | } \\ { \displaystyle \geqslant \frac 3 2 | z | . } \end{array}
$$

Thus $\mathrm { i f ~ } | z | \geqslant 2$ , we have $f ^ { n } ( z ) > 2 \cdot ( 3 / 2 ) ^ { n }$ . So if $| f ^ { k } ( z ) |$ is greater than 2 for some $k ,$ then $\left| f ^ { n } ( z ) \right| \to \infty$ as $k  \infty$ . In particular if (i) does not hold, then (ii) must hold. It is clear that (i) and (ii) cannot hold simultaneously.

Problem 10b. Let U be the set of all $z \in \mathbb { C }$ for which the first alternative (i) holds and K be the set of all $z \in \mathbb { C }$ for which the second alternative (ii) holds. Show that $U$ is an open set and K is a compact set without ${ } ^ { \mathfrak { a } } \mathrm { b o l e s } ^ { \mathfrak { s } } , \ \mathrm { i . e . , } \ \mathbb { C } \backslash K$ has no bounded connected components.

Solution. For $k \in \mathbb N ,$ let $U _ { k }$ be the set of all $z \in \mathbb { C }$ where $| f ^ { k } ( z ) | > M$ . Then $U _ { k }$ is the preimage of an open set, and hence open. By part (a) we have that U is the union of the sets $U _ { k } , { \mathrm { s o ~ } } U$ is open.

It is immediate that K is closed, since K is the complement of U. Any element z in K must satisfy $| z | \leqslant M$ , so K is compact.

Suppose that S was a bounded connected component of U. By part (a) we have that $f ^ { k } ( x ) < M$ for all $x \in K$ , and hence for all $x \in \partial S .$ But then the maximum principle implies that $f ^ { k } ( x )$ is bounded by M for all x in S. Thus (i) is not satisfied, and so $x \notin U$ , which is a contradiction.

Problem 11 a. Suppose $f : \mathbb { C } \to \mathbb { C }$ is a holomorphic function such that the function $z \mapsto g ( z ) = f ( z ) f ( 1 / z )$ is bounded on $\mathbb { C } \backslash \{ 0 \}$ . Show that if $f ( 0 ) \neq 0$ , then f is constant.

Solution. Let $| g ( z ) |$ be bounded by M. Since $f ( 0 ) \neq 0$ , there is a constant $m > 0$ such that $| f ( z ) | > m$ on a δ-neighborhood of 0. For $| z | < \delta ,$ we then have

$$
M \geqslant f ( z ) f ( 1 / z ) \geqslant m f ( 1 / z ) .
$$

So $f ( 1 / z ) \leqslant M / m$ for $| z | < \delta ,$ and hence fpzq is bounded for $| z | > 1 / \delta$ . It follows that $f$ is bounded and therefore constant.

Problem 11 b. Show that if $f ( 0 ) = 0$ , then there exists $n \in \mathbb N$ and $a \in \mathbb { C }$ such that $f ( z ) ~ = ~ a z ^ { n }$ for all $z \in \mathbb { C }$ .

Solution. Let n be the order of f’s zero at 0. Then we can write $f ( z ) ~ = ~ z ^ { n } h ( z )$ where h is holomorphic and $h ( 0 ) \neq 0$ . Note that $h ( z ) h ( 1 / z ) = f ( z ) f ( 1 / z ) = g ( z )$ for $z \neq 0$ . By part $( \mathrm { a } ) \ h ( z ) = a$ identically for some constant a, and then we have $f ( z ) = a z ^ { n }$

Problem 12a. Let $U \subseteq \mathbb { C }$ be an open set and $K \subseteq U$ be a compact subset of U. Prove that there exists a bounded open set V with $K \subseteq V \subseteq { \overline { { V } } } \subseteq U$ such that BV consists of finitely many closed line segments.

Solution. Since K is compact and $U ^ { c }$ is closed, we have $\mathrm { d i s t } ( K , U ^ { c } ) = \delta > 0$ Tile the complex plane with squares of side length δ{100. Let $\mathcal { Q }$ be the family of all squares $Q$ such that dist $( Q , K ) \leqslant \delta / 1 0$ . This is a finite family because K is compact and therefore bounded. Then let V be the interior of $\cup _ { Q \in \mathcal { Q } } Q$ . This is clearly a bounded open set such that $K \subseteq V \subseteq { \overline { { V } } } \subseteq U$ , and $\partial V$ just consists of finitely many edges of

squares.

Problem 12b. Let $f$ be a holomorphic function on U. Show that there exists a sequence $\left\{ R _ { n } \right\}$ of rational functions such that $R _ { n } \to f$ uniformly on K and none of the functions $R _ { n }$ has a pole in $K$

Solution. Let the set V be as in the previous part. For any $z \in K$ , by the Cauchy integral formula we can write

$$
f ( z ) ~ = ~ { \frac { 1 } { 2 \pi i } } \int _ { \partial V } { \frac { f ( w ) } { w - z } } d w ~ = ~ { \frac { 1 } { 2 \pi i } } \sum _ { j = 1 } ^ { N } \int _ { \gamma _ { j } } { \frac { f ( w ) } { w - z } } d w
$$

where each $\gamma _ { j }$ is a straight line and they all have the same length. We parametrize each of these integrals and write

$$
f ( z ) ~ = ~ { \frac { 1 } { 2 \pi i } } \sum _ { j = 1 } ^ { N } \int _ { 0 } ^ { 1 } { \frac { f ( \gamma _ { j } ( t ) ) \gamma _ { j } ^ { \prime } ( t ) } { \gamma _ { j } ( t ) - z } } d t
$$

and we know that $| \gamma _ { j } ^ { \prime } ( t ) | = c$ for some constant c and all $j .$

We want to show that the above integral can be approximated uniformly in $z \in K$ by its Riemann sums. Fix $\epsilon > 0$ . By construction of the set $V ,$ we know that $| \gamma _ { j } ( t ) - z |$ is bounded away from zero uniformly for $z \in K$ and $t \in [ 0 , 1 ]$ , and therefore, since everything involved is continuous, we know that there is a $\delta > 0$ such that $| t _ { 1 } - t _ { 2 } | < \delta$ implies

$$
\left| \frac { f ( \gamma _ { j } ( t _ { 1 } ) ) \gamma _ { j } ^ { \prime } ( t _ { 1 } ) } { \gamma _ { j } ( t _ { 1 } ) - z } - \frac { f ( \gamma _ { j } ( t _ { 2 } ) ) \gamma _ { j } ^ { \prime } ( t _ { 2 } ) } { \gamma _ { j } ( t _ { 2 } ) - z } \right| ~ < ~ \epsilon
$$

for every $z \in K$ . So for each $j ,$ let $\{ 0 = t _ { j , 0 } < t _ { j , 1 } < \ldots < t _ { j , M ( j ) } = 1 \}$ be a partition of r0, 1s with mesh size less than δ. Then we have, for any $z \in K$

$$
\begin{array} { r l } & { \displaystyle \left| f ( z ) - \sum _ { j = 1 } ^ { N } \displaystyle \sum _ { i = 1 } ^ { M ( j ) } \frac { f ( \gamma _ { j } ( t _ { j , i } ) ) \gamma _ { j } ^ { \prime } ( t _ { j , i } ) } { \gamma _ { j } ( t _ { j , i } ) - z } ( t _ { j , i } - t _ { j , i - 1 } ) \right| = \displaystyle \left| \sum _ { j = 1 } ^ { N } \frac { 1 } { 2 \pi i } \int _ { 0 } ^ { 1 } \frac { f ( \gamma _ { j } ( t ) ) \gamma _ { j } ^ { \prime } ( t ) } { \gamma _ { j } ( t ) - z } d t - \displaystyle \sum _ { i = 1 } ^ { M ( j ) } \frac { f ( \gamma _ { j } ( t _ { j , i } ) ) \gamma _ { j } ^ { \prime } ( t _ { j , i } ) } { \gamma _ { j } ( t _ { j , i } ) - z } ( t _ { j , i } - t _ { j , i - 1 } ) \right| } \\ & { = \displaystyle \left| \sum _ { j = 1 } ^ { N } \displaystyle \sum _ { i = 1 } ^ { N ( j ) } \int _ { t _ { j , i - 1 } } ^ { t _ { j , i } } \left( \frac { f ( \gamma _ { j } ( t ) ) \gamma _ { j } ^ { \prime } ( t ) } { \gamma _ { j } ( t ) - z } - \frac { f ( \gamma _ { j } ( t _ { j , i } ) ) \gamma _ { j } ^ { \prime } ( t _ { j , i } ) } { \gamma _ { j } ( t _ { j , i } ) - z } \right) d t \right| } \\ &  \leqslant \displaystyle \sum _ { j = 1 } ^ { N } \displaystyle \sum _ { i = 1 } ^ { M ( j ) } \int _ { t _ { j , i - 1 } } ^ { t _ { j , i } } \left| \frac { f ( \gamma _ { j j } ( t ) ) \gamma _ { j } ^ { \prime } ( t ) } { \gamma _ { j } ( t ) - z } - \frac { f ( \gamma _ { j } ( t _ { j , i } ) ) \gamma _ { j } ^ { \prime } ( t _ { j , i } ) } { \gamma _ { j } ( t _ { j , i } ) - z } \right| d t < \displaystyle \sum _ { j = 1 } ^  N  \end{array}
$$

Finally, notice that the big double sum in the first term is exactly a rational function in z which only has poles on the lines $\gamma _ { j }$ , which are all outside of $K$ , so this gives us the desired result. □

## 17 Spring 2017

Problem 1. Let $K \subseteq \mathbb { R }$ be a compact set of positive measure and let $f \in L ^ { \infty } ( \mathbb { R } )$ . Show that the function

$$
F ( x ) \ = \ { \frac { 1 } { | K | } } \int _ { K } f ( x + t ) d t
$$

is uniformly continuous on R. Here $| K |$ denotes the Lebesgue measure of $K$

Solution. We calculate

$$
\begin{array} { l } { \displaystyle | F ( x ) - F ( y ) | = \frac { 1 } { | K | } \left| \int _ { K } f ( x + t ) d t - \int _ { K } f ( y + t ) d t \right| = \frac { 1 } { | K | } \left| \int _ { K - x } f ( t ) d t - \int _ { K - y } f ( t ) d t \right| } \\ { \displaystyle \leqslant \frac { 1 } { | K | } \int _ { ( K - x ) \triangleq ( K - y ) } | f ( t ) | d t \leqslant \frac { | | f | | _ { L ^ { \infty } } } { | K | } \lambda ( ( K - x ) \Delta ( K - y ) ) = \frac { | | f | | _ { L ^ { \infty } } } { | K | } \lambda ( ( K - ( x - y ) ) \Delta K ) } \end{array}
$$

where $\Delta$ denotes the symmetric difference of two sets and λ is Lebesgue measure.

Fix $\epsilon > 0$ . Let $h = x - y ;$ we want to estimate the measure of $( K - h ) \Delta K$ . Since K is compact, there is a set V which is a finite union of disjoint open intervals such that $K \subseteq V$ and $\lambda ( V \backslash K ) < \epsilon .$ . Say $V = I _ { 1 } \cup . . . \cup I _ { n }$ We have

$$
\begin{array} { r l } { ( K - h ) \Delta K } & { = \ ( ( K - h ) \backslash K ) \cup ( K \backslash ( K - h ) ) } \\ & { \subseteq \ ( ( V - h ) \backslash V ) \cup ( V \backslash K ) \cup ( V \backslash ( V - h ) ) \cup ( ( V - h ) \backslash ( K - h ) ) } \\ & { = \ ( ( V - h ) \Delta V ) \cup ( V \backslash K ) \cup ( ( V - h ) \backslash ( K - h ) ) . } \end{array}
$$

Since V is a finite union of disjoint open intervals, it is clear that

$$
\lambda ( ( V - h ) \Delta V ) \ \leqslant \ 2 n | h | .
$$

Therefore we have $\lambda ( ( K - h ) \Delta K ) \leqslant 2 \epsilon + 2 n | h |$ . So for any $x , y \in \mathbb { R }$ satisfying $\begin{array} { r } { | x - y | < \frac { \epsilon } { 2 n + 2 } } \end{array}$ , we have

$$
| F ( x ) - F ( y ) | < \frac { | | f | | _ { L ^ { \infty } } } { | K | } \lambda ( ( K - ( x - y ) ) \Delta K ) < \frac { | | f | | _ { L ^ { \infty } } } { | K | } \epsilon .
$$

Since n is a parameter depending only on  and the set K, this shows that F is uniformly continuous on R.

Problem 2. Let $f _ { n } ~ : ~ [ 0 , 1 ] \to [ 0 , \infty )$ be a sequence of functions, each of which is non-decreasing on the interval r0, 1s. Suppose the sequence is uniformly bounded in $L ^ { 2 } ( [ 0 , 1 ] )$ . Show that there exists a subsequence that converges in $L ^ { 1 } ( [ 0 , 1 ] )$

Solution. Let M be a uniform upper bound for $| | f _ { n } | | _ { L ^ { 2 } }$ . Since each $f _ { n }$ is nondecreasing, we get the bound $\begin{array} { r } { 0 \leqslant f _ { n } ( t ) \leqslant \frac { M } { \sqrt { 1 - t } } } \end{array}$ for $t \in [ 0 , 1 ]$ . In particular note that for fixed $t , f _ { n } ( t )$ is restricted to a compact set. Therefore the standard diagonalization argument allows us to construct a subsequence $f _ { n _ { k } }$ which converges on $[ 0 , 1 ] \cap \mathbb { Q }$

We claim that $f _ { n _ { k } }$ converges pointwise a.e. as $k \to \infty$ . For a rational $q ,$ let $a _ { q }$ be the limit of the sequence   
$f _ { n _ { k } } ( q )$ . Note that $a _ { q } \leqslant a _ { q ^ { \prime } }$ for $q < q ^ { \prime }$ , since each $f _ { n _ { k } }$ is nondecreasing. For $r \in \mathbb { R }$ let $L _ { r } = \operatorname* { s u p } _ { q < r } a _ { q }$ and   
$U _ { r } = \mathrm { i n f } _ { q ^ { \prime } > r } a _ { q ^ { \prime } }$ . Observe that the intervals $( L _ { r } , U _ { r } )$ are all disjoint, so at most countably many of them are   
nonempty. The interval is empty exactly when $L _ { r } = U _ { r }$ , so this equality holds for almost every r. But when   
$L _ { r } = U _ { r } ,$ , the sequence $f _ { n _ { k } } ( r )$ converges to this value. This establishes pointwise a.e. convergence. Let f be a function on r0, 1s such that $f _ { n _ { k } }  f$ pointwise a.e. We have $\textstyle | f _ { n _ { k } } ( t ) - f ( t ) | \leqslant { \frac { M } { \sqrt { 1 - t } } }$ for almost Since lies in Dor ∞d C implies that in

$$
\frac { M } { \sqrt { 1 - t } }
$$

$$
L ^ { 1 } ( [ 0 , 1 ] )
$$

$$
f _ { n }  f
$$

$$
L ^ { 1 }
$$

Note that there are no issues of measurability to worry about; an increasing function is continuous a.e. (in fact everywhere except possibly on a countable set) and therefore measurable.

Problem 3. Let $C ( [ 0 , 1 ] )$ denote the Banach space of continuous functions on the interval r0, 1s endowed with the sup-norm. Let $\mathcal { F }$ be a σ-algebra on $C ( [ 0 , 1 ] )$ so that for all $x \in [ 0 , 1 ]$ , the map defined via

$$
L _ { x } ( f ) ~ = ~ f ( x )
$$

is ${ \mathcal { F } } .$ measurable. Show that $\mathcal { F }$ contains all open sets.

Solution. Since $C ( [ 0 , 1 ] )$ is separable, every open set is a countable union of open balls, so it suffices to show that $\mathcal { F }$ contains every open ball. And every open ball is a countable union of closed balls, so it suffices to show $\mathcal { F }$ contains every closed ball. Fix $g \in C ( [ 0 , 1 ] ) , \epsilon > 0 .$ , and let

$$
E ~ = ~ \{ f \in C ( [ 0 , 1 ] ) : | | f - g | | _ { L ^ { \infty } } \leqslant \epsilon \}
$$

be a closed ball. For each $q \in \mathbb { Q } \cap [ 0 , 1 ]$ , let

$$
E _ { q } ~ = ~ \{ f \in C ( [ 0 , 1 ] ) : | f ( q ) - g ( q ) | \leqslant \epsilon \} .
$$

Note that each $E _ { q } \in \mathcal { F }$ because $E _ { q } = L _ { q } ^ { - 1 } ( B ( g ( q ) , \epsilon ) )$ and $B ( g ( q ) , \epsilon )$ is a Borel set in $\mathbb { C } .$ Now we claim that

$$
E \ = \ \bigcap _ { q \in \mathbb { Q } } E _ { q } .
$$

First, if Ş $f \in E .$ then $| f ( x ) - g ( x ) | \leqslant | | f - g | | _ { L ^ { \infty } } \leqslant \epsilon$ for all $x \in [ 0 , 1 ]$ , so clearly $f \in E _ { q }$ for every $q ,$ so $\begin{array} { r } { E \subseteq \bigcap _ { q \in \mathbb { Q } } E _ { q } . } \end{array}$ Conversely, suppose $f \in E _ { q }$ for every q. If we had $f \notin E$ , then we would have $| f ( x ) - g ( x ) | > \epsilon$ for some $\mathrm { { ; } \in \left[ 0 , 1 \right] }$ , but since $| f - g |$ is continuous and Q is dense, this would imply the existence of Ş $q \in [ 0 , 1 ]$ with $| f ( q ) - g ( q ) | > \epsilon .$ , a contradiction. So $\textstyle E = \bigcap _ { q \in \mathbb { Q } } E _ { q }$ , which expresses $E$ as a countable intersection of elements of ${ \mathcal { F } } ,$ so $E \in { \mathcal { F } } . \qquad \bigsqcup$

Problem 4. For $n \geqslant 1$ , let $a _ { n } : [ 0 , 1 ) \to \{ 0 , 1 \}$ denote the nth digit in the binary expansion of $x ,$ so that

$$
x \ = \ \sum _ { n \geq 1 } a _ { n } ( x ) 2 ^ { - n } \quad { \mathrm { f o r ~ a l l ~ } } x \in [ 0 , 1 ) .
$$

(We remove any ambiguity from this definition by requiring that lim inf $a _ { n } ( x ) = 0$ for all $x \in [ 0 , 1 ) . )$ Let $M ( \left[ 0 , 1 \right) )$ denote the Banach space of finite complex Borel measures on $[ 0 , 1 )$ and define linear functionals $L _ { n }$ on $M ( [ 0 , 1 ) )$ via

$$
L _ { n } ( \mu ) \ = \ \int _ { 0 } ^ { 1 } a _ { n } ( x ) d \mu ( x ) .
$$

Show that no subsequence of the sequence $L _ { n }$ converges in the weak-˚ topology on $M ( [ 0 , 1 ) ) ^ { * }$

Solution. Let $L _ { n _ { k } }$ be any subsequence of the $L _ { n }$ . To show that $L _ { n _ { k } }$ is not weak-˚ convergent, it suffices to find some $\mu \in M ( [ 0 , 1 ) )$ such that $\{ L _ { n _ { k } } ( \mu ) \} _ { k = 1 } ^ { \infty }$ is not a convergent sequence in C. Let

$$
b \ = \ \sum _ { k = 1 } ^ { \infty } ( k \ \mathrm { m o d } \ 2 ) \cdot 2 ^ { - n _ { k } } ,
$$

i.e. b is the number in r0, 1q whose nth digit in binary is equal to 1 if $n = n _ { k }$ for some odd $k ,$ and 0 otherwise. Now let $\mu = \delta _ { b }$ be the point mass measure at b. Clearly $\mu \in M ( [ 0 , 1 ) )$ , and we have

$$
L _ { n _ { k } } ( \mu ) \ = \ \int _ { 0 } ^ { 1 } a _ { n _ { k } } ( x ) d \mu ( x ) \ = \ a _ { n _ { k } } ( b ) \ = \ k \ \mathrm { m o d } \ 2 .
$$

So $\{ L _ { n _ { k } } ( \mu ) \} _ { k = 1 } ^ { \infty }$ is not a convergent sequence, so $\left\{ L _ { n _ { k } } \right\}$ does not weak-˚ converge.

Problem 5. Let $d \mu$ be a finite complex Borel measure on r0, 1s such that

$$
\hat { \mu } ( n ) ~ = ~ \int _ { 0 } ^ { 1 } e ^ { 2 \pi i n x } d \mu ( x ) ~ \to ~ 0 ~ \mathrm { a s } ~ n \to \infty .
$$

Let dν be a finite complex Borel measure on r0, 1s that is absolutely continuous with respect to $d \mu$ . Show that

$$
{ \hat { \nu } } ( n ) \to 0 \quad { \mathrm { a s ~ } } n \to \infty .
$$

Solution. Since dν is absolutely continuous with respect to $d \mu$ , by the Radon-Nikodym theorem there is a function $\begin{array} { r } { f = \frac { d \nu } { d \mu } \in L ^ { 1 } ( d \mu ) } \end{array}$ such that

$$
\hat { \nu } ( n ) ~ = ~ \int _ { 0 } ^ { 1 } e ^ { 2 \pi i n x } d \nu ( x ) ~ = ~ \int _ { 0 } ^ { 1 } e ^ { 2 \pi i n x } f ( x ) d \mu ( x ) .
$$

Fix $\epsilon > 0$ . Since $d \mu$ is a finite Borel measure on a compact metric space, we know that the set of continuous functions is dense in $L ^ { 1 } ( d \mu )$ with respect to the $L ^ { 1 }$ norm, so let g be a continuous function satisfying $\| f - g \| _ { L ^ { 1 } } < \epsilon .$ . We also know that trigonometric polynomials are dense in the set of continuous functions with respect to the sup norm, so let ř $P$ be a trigonometric polynomial such that $| | g - P | | _ { L ^ { \infty } } < \epsilon$ . Writing $\begin{array} { r } { P ( x ) = \sum _ { m = - N } ^ { N } a _ { n } e ^ { 2 \pi i m x } } \end{array}$ , we calculate

$$
\operatorname * { l i m } _ { n  \infty } \int _ { 0 } ^ { 1 } e ^ { 2 \pi n x } P ( x ) d \mu ( x ) \ = \ \operatorname * { l i m } _ { n  \infty } \sum _ { m = - N } ^ { N } a _ { n } \int _ { 0 } ^ { 1 } e ^ { 2 \pi i ( n + m ) x } d \mu ( x ) \ = \ 0
$$

by hypothesis. Thus, as soon as n is big enough so that

$$
\left| \int _ { 0 } ^ { 1 } e ^ { 2 \pi n x } { \cal P } ( x ) d \mu ( x ) \right| \ < \epsilon ,
$$

we have

$$
\begin{array} { r l r } { | \hat { \nu } ( n ) | } & { = } & { \displaystyle \left. \int _ { 0 } ^ { 1 } e ^ { 2 \pi i n x } f ( x ) d \mu ( x ) \right. } \\ & { \leqslant } & { \displaystyle \left. \int _ { 0 } ^ { 1 } e ^ { 2 \pi i n x } \bigl ( f ( x ) - g ( x ) \bigr ) d \mu ( x ) \right. + \left. \int _ { 0 } ^ { 1 } e ^ { 2 \pi i n x } \bigl ( g ( x ) - P ( x ) \bigr ) d \mu ( x ) \right. + \left. \int _ { 0 } ^ { 1 } e ^ { 2 \pi i n x } P ( x ) d \mu ( x ) \right. } \\ & { \leqslant } & { \displaystyle \epsilon + \int _ { 0 } ^ { 1 } \left. f ( x ) - g ( x ) \right. d \mu ( x ) + \int _ { 0 } ^ { 1 } \left. g ( x ) - P ( x ) \right. d \mu ( x ) } \\ & { \leqslant } & { \displaystyle \epsilon + \epsilon + \epsilon \mu [ 0 , 1 ] , } \end{array}
$$

which shows ${ \hat { \nu } } ( n ) \to 0 { \mathrm { ~ a s ~ } } n \to \infty . \quad \boxed { }$

Problem 6. Let D be the closed unit disc in the complex plane, let $\left\{ p _ { n } \right\}$ be distinct points in D and let $r _ { n } > 0$ be such that the discs $D _ { n } = \{ z : | z - p _ { n } | \leqslant r _ { n } \}$ satisfy

1. $D _ { n } \subseteq \mathbb { D } ;$

2. $D _ { n } \cap D _ { m } = \emptyset { \mathrm { ~ i f ~ } } n \neq m ;$ and

3. $\textstyle \sum r _ { n } < \infty .$

Prove ${ X } = \overline { { \mathbb { D } } } \backslash \bigcup _ { n } D _ { n }$ has positive area.

Solution. Let $\begin{array} { r } { f ( x , y ) = \sum _ { i = 1 } ^ { \infty } \chi _ { D _ { i } } ( x , y ) } \end{array}$ . Also let $\begin{array} { r } { u ( x ) = \sum _ { i = 1 } ^ { \infty } \chi _ { \pi ( D _ { i } ) } ( x ) } \end{array}$ where π denotes projection onto the real axis. We have

$$
\int _ { - 1 } ^ { 1 } u ( x ) d x \ = \ \sum _ { i = 1 } ^ { \infty } 2 r _ { i } \ < \ \infty
$$

by hypothesis, so we conclude that $u ( x ) < \infty$ for a.e. $x \in ( - 1 , 1 )$ . For a fixed $x , u ( x )$ counts the number of the $D _ { i }$ that intersect the line $\operatorname { R e } ( z ) = x$ . Since the $D _ { i }$ are closed disjoint discs, $u ( x ) < \infty$ implies that the portion of the line $\operatorname { R e } ( z ) = x$ not contained in any of the $D _ { i }$ has positive (one-dimensional) Lebesgue measure. Let $m ( x )$ denote the one-dimensional measure of the portion of the lineş $\operatorname { R e } ( z ) = x$ not contained in any of the $D _ { i }$ . Then the area of X is given exactly by $\int _ { - 1 } ^ { 1 } m ( x )$ dx, and since m is a non-negative function which has a positive value for a.e. $x \in ( - 1 , 1 )$ , this implies that $\int _ { - 1 } ^ { 1 } m ( x ) d x > 0$

Problem 7. Let $f ( z )$ be a one-to-one continuous mapping from the closed annulus

$$
\{ 1 \leqslant | z | \leqslant R \}
$$

onto the closed annulus

$$
\{ 1 \leqslant | z | \leqslant S \}
$$

such that $f$ is analytic on the open annulus $\{ 1 < | z | < R \}$ . Prove $S = R .$

Solution. Let $A = \{ z : 1 < | z | < R \}$ and $B = \{ z : 1 < | z | < S \}$ We know that f maps BA to $\partial B ,$ so by composing f with an inversion if necessary we may assume that f maps the unit circle to itself. Since $f$ is a nonvanishing analytic function in A, log |f| is harmonic in A and extends continuously to $\partial A .$ , and satisfies log $| f ( z ) | = 0 \mathrm { o n } | z | = 1$ and log $| f ( z ) | = \log ( S ) { \mathrm { o n } } | z | = R .$ . Since A is a region on which the Dirichlet problem can be solved, log |f| is uniquely determined by its boundary values. Since $z \mapsto \log | z | \cdot { \frac { \log ( S ) } { \log ( R ) } }$ is another harmonic function on A with the same boundary values, we conclude that

$$
\log | f ( z ) | ~ = ~ \log | z | \cdot { \frac { \log ( S ) } { \log ( R ) } }
$$

for all $z \in A$ . Therefore we have $\left| f ( z ) \right| = \left| z ^ { \alpha } \right|$ where $\alpha : = \log ( S ) / \log ( R )$ . Since $f ( z )$ and $z ^ { \alpha }$ are both analytic functions in the slit annulus ${ \tilde { A } } : = { \tilde { A } } { \tilde { \bigcup } } - R , - 1 { \tilde { \mathit { \Pi } } }$ s, this implies that $f ( z ) = C z ^ { \alpha }$ for some $| C | = 1$ (this is proven by applying the maximum principle to $f ( z ) / z ^ { \alpha }$ and $z ^ { \alpha } / f ( z ) )$ . But we know that $f$ analytically continues to all of $A ,$ , so by uniqueness of analytic continuation, $z ^ { \alpha }$ must also, which implies that α is a positive integer. But if $\alpha \geqslant 2 .$ , then $z ^ { \alpha }$ is not one-to-one on A, so we must have $\alpha = 1$ and therefore $\log ( R ) = \log ( S )$ , so $R = S . \quad \sqcup$

Problem 8. Let $a _ { 1 } , \ldots , a _ { n }$ be $n \geqslant 1$ points in the disc D (possibly with repetitions), so that the function

$$
B ( z ) \ = \ \prod _ { j = 1 } ^ { n } { \frac { z - a _ { j } } { 1 - { \overline { { a _ { j } } } } z } }
$$

has n zeros in D. Prove that the derivative $B ^ { \prime } ( z )$ has n ´ 1 zeros in D.

Solution. First assume that $B ( 0 ) \neq 0 \neq B ^ { \prime } ( 0 )$ and that B has no repeated roots. One can calculate that

$$
\frac { B ^ { \prime } ( z ) } { B ( z ) } \ = \ \sum _ { j = 1 } ^ { n } \frac { 1 - | a _ { j } | ^ { 2 } } { ( z - a _ { j } ) ( 1 - \overline { { { a _ { j } } } } z ) } \ = \ \frac { \sum _ { j = 1 } ^ { n } \Big [ ( 1 - | a _ { j } | ^ { 2 } ) \prod _ { i \neq j } ( z - a _ { i } ) ( 1 - \overline { { { a _ { i } } } } z ) \Big ] } { \prod _ { j = 1 } ^ { n } ( z - a _ { j } ) ( 1 - \overline { { { a _ { j } } } } z ) } .
$$

Since we assume B has no repeated roots, the zeros of $B ^ { \prime } / B$ are precisely the zeros of $B ^ { \prime }$ . Note that $B ^ { \prime } / B$ is a rational function with a numerator of degree $2 ( n - 1 )$ , so it has $2 ( n - 1 )$ total zeros. With a lot of calculation, one can verify the identity

$$
{ \frac { \overline { { B ^ { \prime } ( 1 / \overline { { z } } ) } } } { \overline { { B ( 1 / \overline { { z } } ) } } } } \ = \ z ^ { 2 } { \frac { B ^ { \prime } ( z ) } { B ( z ) } } .
$$

This shows that for $z \neq 0 , B ^ { \prime } ( z ) = 0$ if and only if $B ^ { \prime } ( 1 / \overline { { z } } ) = 0$ Since we assumed neither B nor $B ^ { \prime }$ vanish at $0 ,$ this implies that the zeros come in pairs $\{ z , 1 / \overline { { z } } \}$ . Exactly one member of each pair is inside D and the other is outside D, so since there are $2 ( n - 1 )$ total zeros of $B ^ { \prime }$ , it must have $n - 1$ zeros inside D.

For the general case, it is a theorem that if B is any function of the given form with n factors, then there is a sequence $B _ { k }$ of functions of the given form, each with n factors, satisfying (a) $B _ { k } \to B$ uniformly on ${ \overline { { \mathbb { D } } } } ,$ (b) $B _ { k } ( 0 ) \neq 0 \neq B _ { k } ^ { \prime } ( 0 )$ , and $\mathrm { ~ ( c ) ~ } B _ { k }$ has no repeated roots. To see why this is true, note that $\frac { z - \alpha } { 1 - \overline { { \alpha } } z }$ converges uniformly on D to $\frac { z - \beta } { 1 - \overline { { \beta } } z }$ as $\alpha  \beta$ . Therefore this is also true for products of functions of that form. Also note that $B _ { k } ( 0 )$ and $B _ { k } ^ { \prime } ( 0 )$ are continuous functions of the roots $a _ { 1 } , \ldots , a _ { n }$ . Therefore by just taking the original function B and perturbing its roots by sufficiently small amounts, we can guarantee that the new function has all of the desired properties and is still uniformly close to $B$

So by the first part of this problem, we know that each $B _ { k }$ has exactly $n - 1$ roots in D. Since the convergence is uniform on D, we also know that $B _ { k } ^ { \prime } \to B ^ { \prime }$ uniformly on D. Since each $B _ { k }$ has absolute value 1 on $\partial \mathbb { D }$ , we then have that $B _ { k } ^ { \prime } / B _ { k }$ converges uniformly to $B ^ { \prime } / B$ on ${ \widehat { o } } \mathbb { D } ,$ , so by the argument principle

$$
{ \frac { \# } { \hbar } } { \mathrm { ~ z e r o s ~ o f ~ } } B { \mathrm { ~ i n ~ } } \mathbb { D } \ = \ \int _ { \partial \mathbb { D } } { \frac { B ^ { \prime } } { B } } d z \ = \ \operatorname* { l i m } _ { k \to \infty } \int _ { \partial \mathbb { D } } { \frac { B _ { k } ^ { \prime } } { B _ { k } } } d z \ = \ \operatorname* { l i m } _ { k \to \infty } ( { \mathcal { \# } } { \mathrm { ~ z e r o s ~ o f ~ } } B _ { k } { \mathrm { ~ i n ~ } } \mathbb { D } ) \ = \ n - 1 . \quad \mathbb { D } \neq \mathbf { D } .
$$

Problem 9a. Let $f ( z )$ be an analytic function in the entire complex plane C and assume $f ( 0 ) ~ \neq ~ 0$ Let $\left\{ a _ { n } \right\}$ be the zeros of $f _ { : }$ , repeated according to their multiplicities. Let $R > 0$ be such that $| f ( z ) | > 0$ on $| z | = R$ . Prove

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log { \big | } f ( R e ^ { i \theta } ) { \big | } ~ d \theta ~ = ~ \log { \big | } f ( 0 ) { \big | } + \sum _ { | a _ { n } | < R } \log { \frac { R } { | a _ { n } | } } .
$$

Solution. Since $f$ is not identically zero, there are only finitely many $a _ { n }$ satisfying $\left| a _ { n } \right| < R$ . Define

$$
g ( z ) \ = \ \prod _ { | a _ { n } | < R } { \frac { R ( z - a _ { n } ) } { R ^ { 2 } - { \overline { { a _ { n } } } } z } } .
$$

Note that in the disc $| z | < R , g$ has the same zeros as $f ,$ no poles, and $| g ( z ) | = 1$ for $| z | = R$ . Therefore $f / g$ is a nonvanishing holomorphic function in $| z | < R$ , and $| f / g | = | f |$ on the boundary $| z | = R$ . Therefore log $| f / g |$ is a harmonic function in $| z | < R ,$ so we apply the mean value formula to obtain

$$
\log \left| { \frac { f ( 0 ) } { g ( 0 ) } } \right| ~ = ~ { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log \left| { \frac { f ( R e ^ { i \theta } ) } { g ( R e ^ { i \theta } ) } } \right| d \theta ~ = ~ { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log \left| f ( R e ^ { i \theta } ) \right| d \theta .
$$

We also have

$$
\log \left| \frac { f ( 0 ) } { g ( 0 ) } \right| = \log | f ( 0 ) | - \sum _ { \left| a _ { n } \right| < R } \log \left| \frac { R ( 0 - a _ { n } ) } { R ^ { 2 } - 0 } \right| = \log | f ( 0 ) | + \sum _ { \left| a _ { n } \right| < R } \log \left| \frac { R } { a _ { n } } \right| ,
$$

so combining this with the above equation gives the desired result.

Problem 9b. Prove that if there are constants C and λ such that $| f ( z ) | \leqslant C e ^ { | z | ^ { \lambda } }$ for all z, then

$$
\sum \left( \frac { 1 } { \left| a _ { n } \right| } \right) ^ { \lambda + \epsilon } < \infty
$$

for all $\epsilon > 0 .$

Solution. Let $N ( R ) = \# \{ n : | a _ { n } | < R \}$ . Applying part (a) with 2R in place of R we get

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log | f ( 2 R e ^ { i \theta } ) | d \theta = \log | f ( 0 ) | + \sum _ { \{ a _ { \mathrm { r } } | < 2 R \} } \log \left( \frac { 2 R } { | a _ { n } | } \right) \leqslant \log | f ( 0 ) | + \sum _ { \{ a _ { \mathrm { r } } | < R \} } \log \left( \frac { 2 R } { | a _ { n } | } \right) \leqslant \log | f ( 0 ) | + N ( R ) \log ( 2 ) .
$$

By the hypothesis on the growth rate of $f ,$ we also have

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log | f ( 2 R e ^ { i \theta } ) | d \theta \ \leqslant \ ( 2 R ) ^ { \lambda } + \log ( C ) ,
$$

so combining the two estimates gives $( 2 R ) ^ { \lambda } + \log ( C ) \geqslant \log \vert f ( 0 ) \vert + N ( R ) \log ( 2 )$ , which implies that

$$
N ( R ) \ \leqslant \ { \frac { ( 2 R ) ^ { \lambda } - \log ( C ) - \log | f ( 0 ) | } { \log ( 2 ) } } \ \leqslant \ K ( 2 R ) ^ { \lambda }
$$

for some constant K and R sufficiently large. Let M be big enough so that the above estimate holds whenever $R \geqslant 2 ^ { M - 1 }$ . It suffices to show that

$$
\sum _ { | a _ { n } | \geq 2 ^ { M - 1 } } \left( { \frac { 1 } { | a _ { n } | } } \right) ^ { \lambda + \epsilon } ~ < ~ \infty
$$

for any $\epsilon > 0$ . We estimate

$$
\begin{array} { r l } { \displaystyle \sum _ { | a _ { n } | \geqslant 2 ^ { M - 1 } } ( \frac { 1 } { | a _ { n } | } ) ^ { \lambda + \epsilon } } & { = \displaystyle \sum _ { r = M } ^ { \infty } \displaystyle \sum _ { 2 r ^ { - 1 } \leqslant | a _ { n } | < 2 ^ { r } } ( \frac { 1 } { | a _ { n } | } ) ^ { \lambda + \epsilon } \leqslant \displaystyle \sum _ { r = M } ^ { \infty } ( N ( 2 ^ { r } ) - N ( 2 ^ { r - 1 } ) ( \frac { 1 } { 2 ^ { r - 1 } } ) ^ { \lambda + \epsilon } } \\ & { \leqslant \displaystyle \sum _ { r = M } ^ { \infty } \frac { N ( 2 ^ { r } ) } { ( 2 ^ { r - 1 } ) ^ { \lambda + \epsilon } } \leqslant K \displaystyle \sum _ { r = M } ^ { \infty } \frac { ( 2 ^ { r + 1 } ) ^ { \lambda } } { ( 2 ^ { r - 1 } ) ^ { \lambda + \epsilon } } = K \cdot 2 ^ { 2 \lambda + \epsilon } \displaystyle \sum _ { r = M } ^ { \infty } ( 2 ^ { - \epsilon } ) ^ { r } < \infty . } \end{array}
$$

Problem 10. Let $a _ { 1 } , \ldots , a _ { n }$ be $n \geqslant 1$ distinct points in C and let $\Omega = \mathbb { C } \backslash \{ a _ { 1 } , . . . , a _ { n } \}$ Let $H ( \Omega )$ be the vector space of real-valued harmonic functions on Ω and let $R ( \Omega ) \subseteq H ( \Omega )$ be the space of real parts of analytic functions on Ω. Prove the quotient space $\frac { H ( \Omega ) } { R ( \Omega ) }$ has dimension $n ,$ find a basis for this space, and prove it is a basis.

Solution. We claim that the functions $f _ { i } = \log | z - a _ { i } |$ form a basis for this space. We will work with a homology basis $\gamma _ { 1 } , \ldots , \gamma _ { n }$ for Ω, consisting of small counterclockwise circles around each point. For a function $u \in H ( \Omega )$ be arbitrary, we let ˚du $= - u _ { y } d x + u _ { x } d y$ denote the conjugate differential for u. Recallş that the periods of ˚du with respect our homology basis are defined to be the real numbers $\int _ { \gamma _ { i } } u .$ (See section 6.1 in Ahlfors.)

The harmonic function $a ( z ) = \log | z |$ defined on $\mathbb { C } \backslash \{ 0 \}$ has conjugate differential $d \theta _ { \colon }$ , and so the period of ˚da on a counterclockwise circle about the origin is 2π. Alternatively one can see this by setting $f = a _ { x } - i a _ { y }$ (which is analytic) and then writing $f d z = d a + i * d a$ . The differential da is exact, and we can compute that $\textstyle f ( z ) = { \frac { 1 } { z } }$ . Thus the integral of i ˚ dv around a counterclockwise circle is $2 \pi i .$ and we again get a period of 2π. Note that the period of ˚da around any cycle homologous to 0 is 0, since the integral of $f d z$ around such a cycle is 0. Therefore by translating, we see that the period of ˚dfi along $\gamma _ { j }$ is $2 \pi \delta _ { i j }$

If $u \in R ( \Omega )$ then u has a harmonic conjugate v and $* d u = d v$ , which is exact. Thus each period of u is 0. $\begin{array} { r } { \operatorname { I f } \sum _ { i = 1 } ^ { n } a _ { i } f _ { i } \in R ( \Omega ) } \end{array}$ , then it must have period 0 about each cycle. By linearity of periods, this can only happen if each $a _ { i }$ is 0. So our $f _ { i } ^ { \mathrm { ~ : ~ } }$ s are independent.

Let $g \in H ( \Omega )$ be arbitrary, with ˚dg having periods $p _ { i }$ on $\gamma _ { i }$ . Set

$$
\widetilde g = g - \frac { 1 } { 2 \pi } \sum _ { i = 1 } ^ { n } p _ { i } f _ { i } ,
$$

so that $\ast d \widetilde g$ has period 0 on each $\gamma _ { i }$ . We claim that $\widetilde g$ lies in $R ( \Omega )$ , which will imply that the $f _ { i } { } ^ { \mathrm { ' } } \mathrm { s }$ span. Indeed we have that $\ast d \widetilde g$ is exact and so we may integrate $\ast d \widetilde g$ to obtain a harmonic conjugate for $\widetilde g .$ . More precisely, set $f ( z ) = \widetilde { u } _ { x } - i \widetilde { u } _ { y }$ . Then $f d z = d u + i$ ˚ du is exact on Ω and so $f$ has an anti-derivative $F = U + i V$ on Ω. It’s easy to verify that U and u agree up to constants, so $V$ is a harmonic conjugate for u.

Problem 11. Let $1 \leqslant p < \infty$ and let $U ( z )$ be a harmonic function on the complex plane C such that

$$
\iint _ { \mathbb { R } \times \mathbb { R } } | U ( x + i y ) | ^ { p } d x d y < \infty .
$$

Prove that $U ( z ) = 0$ for all $z = x + i y \in \mathbb { C }$

Solution. Let $q$ be the conjugate exponent, so $1 / p + 1 / q = 1$ . Since $U$ is harmonic on all of $\mathbb { C } .$ for any $r > 0$ and any $z \in \mathbb { C }$ we have the mean value property

$$
U ( z ) ~ = ~ \frac { 1 } { \pi r ^ { 2 } } \int \int _ { B ( z , r ) } U ( x + i y ) d x d y .
$$

By H¨older’s inequality we have

$$
\begin{array} { l l l } { | U ( z ) | \ \leqslant \ \displaystyle \frac { 1 } { \pi r ^ { 2 } } \displaystyle \iint _ { B ( z , r ) } | U ( x + i y ) | d x d y \ = \ \displaystyle \frac { 1 } { \pi r ^ { 2 } } \left( \displaystyle \iint B ( z , r ) | U ( x + i y ) | ^ { p } d x d y \right) ^ { 1 / p } \left( \displaystyle \iint _ { B ( z , r ) } 1 d x d y \right) ^ { 1 / q } } \\ { \leqslant \ \displaystyle \frac { ( \pi r ^ { 2 } ) ^ { 1 / q } } { \pi r ^ { 2 } } \left( \displaystyle \iint | U ( x + i y ) | ^ { p } d x d y \right) ^ { 1 / p } \ \leqslant \ C r ^ { 2 ( 1 / q - 1 ) } \ = \ C r ^ { - 2 / p } } \end{array}
$$

for some constant $C < \infty$ . This holds for any $r > 0$ , so we can take $r  \infty$ and conclude that $U ( z ) = 0$ (because $- 2 / p < 0 )$

Problem 12. Let $0 < \alpha < 1$ and let $f ( z )$ be an analytic function on the unit disc D. Prove that if

$$
| f ( z ) - f ( w ) | \ \leqslant \ C | z - w | ^ { \alpha }
$$

for all $z , w \in \mathbb { D }$ and some constant $C \in \mathbb { R }$ , then there is a constant $A = A ( C ) < \infty$ such that

$$
| f ^ { \prime } ( z ) | \ \leqslant \ A ( 1 - | z | ) ^ { \alpha - 1 } .
$$

Solution. Fix $z \in \mathbb { D }$ . Then for any $r > 0$ we have

$$
\int _ { | w - z | = r } \frac { 1 } { ( w - z ) ^ { 2 } } d w \ = \ 0 ,
$$

so by the Cauchy integral formula we can write

$$
f ^ { \prime } ( z ) ~ = ~ \int _ { | w - z | = r } { \frac { f ( w ) } { ( w - z ) ^ { 2 } } } d w ~ = ~ \int _ { | w - z | = r } { \frac { f ( w ) - f ( z ) } { ( w - z ) ^ { 2 } } } d w .
$$

Therefore taking absolute values inside we get

$$
| f ^ { \prime } ( z ) | \ \leqslant \ 2 \pi r \cdot { \frac { 1 } { r ^ { 2 } } } \cdot \operatorname* { s u p } _ { | w - z | = r } | f ( z ) - f ( w ) | \ \leqslant \ { \frac { 2 \pi } { r } } C r ^ { \alpha } \ = \ 2 \pi C r ^ { 1 - \alpha } .
$$

This is true for any $r$ for which $B ( z , r ) \subseteq \mathbb { D }$ , so pick $\begin{array} { r } { r = \frac { 1 - | z | } { 2 } } \end{array}$ , then we get

$$
| f ^ { \prime } ( z ) | \ \leqslant \ A ( 1 - | z | ) ^ { \alpha - 1 } . \quad \varPi
$$