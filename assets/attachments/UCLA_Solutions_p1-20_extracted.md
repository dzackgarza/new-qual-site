## UCLA Analysis Qualifying Exam Solutions Last updated: January 25, 2019

Contents\
1 Spring 2009 2\
2 Fall 2009 7\
3 Spring 2010 12\
4 Fall 2010 16\
5 Spring 2011 22\
6 Fall 2011 26\
7 Spring 2012 33\
8 Fall 2012 40\
9 Spring 2013 47\
10 Fall 2013 55\
11 Spring 2014 63\
12 Fall 2014 69\
13 Spring 2015 76\
14 Fall 2015 84\
15 Spring 2016 95\
16 Fall 2016 104\
17 Spring 2017 114\
18 Fall 2017 121\
19 Spring 2018 127\
20 Fall 2018 137

## 1 Spring 2009

Problem 1. Let f and g be real-valued integrable functions on a measure space $( X , B , \mu )$ and define

$$
F _ { t } \ = \ \{ x \in X : f ( x ) > t \} , \quad G _ { t } \ = \ \{ x \in X : g ( x ) > t \} .
$$

Prove

$$
\int | f - g | d \mu \ = \ \int _ { - \infty } ^ { \infty } \mu \left( ( F _ { t } \backslash G _ { t } ) \cup ( G _ { t } \backslash F _ { t } ) \right) .
$$

Solution.
First assume that X is σ-finite.
Then we have

$$
\begin{array} { r l } { \displaystyle \int _ { - \infty } ^ { \infty } \mu \left( \left( F _ { t } \backslash G _ { t } \right) \cup \left( G _ { t } \backslash F _ { t } \right) \right) } & { = \displaystyle \int _ { - \infty } ^ { \infty } \int _ { X } \chi _ { \left\{ x \in X : \operatorname* { m i n } \left( f ( x ) , g ( x ) \right) \leqslant t < \operatorname* { m a x } \left( f ( x ) , g ( x ) \right) \right\} } ( x ) d \mu ( x ) d t } \\ & { = \displaystyle \int _ { X } \int _ { - \infty } ^ { \infty } \chi _ { \left\{ x \in X : \operatorname* { m i n } \left( f ( x ) , g ( x ) \right) \leqslant t < \operatorname* { m a x } \left( f ( x ) , g ( x ) \right) \right\} } ( x ) d t d \mu ( x ) \quad \mathrm { b y ~ T o n e l l i } } \\ & { = \displaystyle \int _ { X } \left| f ( x ) - g ( x ) \right| d \mu ( x ) , } \end{array}
$$

which is the desired result.
Now drop the assumption that X is σ-finite.
Let Ť $Y = \{ x \in X : | f ( x ) - g ( x ) | \neq 0 \}$ and let $\nu = \mu | _ { Y }$ . Note that $Y = \bigcup _ { n = 1 } ^ { \mathcal { O } } \{ x \in X : | f ( x ) - g ( x ) | > 1 / n \}$ , and since f and g are both integrable, each of those sets must have finite measure.
Thus $( Y , \nu )$ is a σ-finite measure space.
Thus by the work above we have

$$
\int _ { Y } \left| f - g \right| d \nu \ = \ \int _ { - \infty } ^ { \infty } \nu \left( \left( F _ { t } \cap Y \backslash G _ { t } \cap Y \right) \cup \left( G _ { t } \cap Y \backslash F _ { t } \cap Y \right) \right) .
$$

But note that $\int _ { X } \left| f - g \right| d \mu = \int _ { Y } \left| f - g \right| d \mu + \int _ { Y ^ { c } } \left| f - g \right| d \mu = \int _ { Y } \left| f - g \right| d \nu$ by definition of Y and ν. Also note that $F _ { t } \backslash G _ { t } , G _ { t } \backslash F _ { t } \subseteq Y$ for every t, so $( { \vec { F _ { t } } } \cap { \cal Y } \backslash { G _ { t } } \cap { \cal Y } ) \cup ( { \vec { G } } _ { t } \cap { \cal Y } \backslash { F _ { t } } \cap { \cal Y } ) = ( { \cal F } _ { t } \backslash { G _ { t } } ) \cup ( { G _ { t } } \backslash { F _ { t } } )$ , and $\nu \left( \left( F _ { t } \backslash G _ { t } \right) \cup \left( G _ { t } \backslash F _ { t } \right) \right) = \mu \left( \left( F _ { t } \backslash G _ { t } \right) \cup \left( G _ { t } \backslash F _ { t } \right) \right)$ . Substituting all of this into the above equation gives the desired result.

Problem 2. Let H be an infinite dimensional real Hilbert space.

(a) Prove the unit sphere $S = \{ x \in H : | | x | | = 1 \}$ is weakly dense in the unit ball $B = \left\{ x \in H : | | x | | \leqslant 1 \right\}$ (b) Prove there is a sequence $T _ { n }$ of bounded linear operators from H to H such that $| | T _ { n } | | = 1$ for all n but lim $\iota _ { n  \infty } T _ { n } ( x ) = 0$ for all $x \in H$

Solution.
(a) Fix $x \in B$ We may assume $| | x | | < 1$ because if $x \in S$ the result is obvious.
Using a standard Zorn’s Lemma/Gram-Schmidt argument, together with the fact that H is infinite-dimensional, web can construct an orthonormal set $\left\{ x / \left| \left| x \right| \right| , e _ { 1 } , e _ { 2 } , \ldots \right\}$ . Let $x _ { n } = x + { \sqrt { 1 - \left| \left| x \right| \right| ^ { 2 } } } e _ { n }$ . By the Pythagorean theorem we have $\left| \left| x _ { n } \right| \right| ^ { 2 } = \left| \left| x \right| \right| ^ { 2 } + \left( 1 - \left| \left| x \right| \right| ^ { 2 } \right) \left| \left| e _ { n } \right| \right| ^ { 2 } = 1$ , so $x _ { n } \in S$ . Now we claim that $\left\{ x _ { n } \right\}$ converges weakly to x. For $y \in H$ fixed, we have

$$
\langle x _ { n } - x , y \rangle \ = \ \sqrt { 1 - \left| \left| x \right| \right| ^ { 2 } } \langle e _ { n } , y \rangle .
$$

This goes to 0 as $n \to \infty$ because since $\left\{ \boldsymbol { e } _ { n } \right\}$ is an orthonormal set, Bessel’s inequality gives $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } | \langle e _ { n } , y \rangle | ^ { 2 } \leqslant } \end{array}$ $| | y | | ^ { 2 }$ and the terms of a convergent series must go to $0 . \quad \boxed { \begin{array} { r l r l } \end{array} }$

(b) Fix an infinite orthonormal set $\{ e _ { 1 } , e _ { 2 } , \ldots \}$ . Define $T _ { n } ( x ) : = \langle x , e _ { n } \rangle e _ { n }$ It’s clear that $T _ { n }$ is a linear operator $H  H$ . We have $| | T _ { n } ( x ) | | = | \langle x , e _ { n } \rangle | | | e _ { n } | | \leqslant | | x | |$ by Cauchy-Schwarz, so $| | T _ { n } | | \leqslant 1$ . Also it’s clear that $T _ { n } ( e _ { n } ) = e _ { n } , \mathrm { s o } \ | | T _ { n } | | = 1$ . Finally, for any x P H we have lim $\begin{array} { r } { \mathsf { l } _ { n \to \infty } \left\| T _ { n } ( x ) \right\| = \operatorname* { l i m } _ { n \to \infty } \left| \langle x , e _ { n } \rangle \right| = 0 } \end{array}$ by the same Bessel’s inequality argument in part (a).

Problem 3. Let X be a Banach space.
Prove that if $X ^ { * }$ is separable then X is separable.

Solution.
See Fall 2014 $\# 6 .$

Problem 4. Let $f ( x )$ be a non-decreasing function on $[ 0 , 1 ]$

(a) Prove that $\int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) d x \leqslant f ( 1 ) - f ( 0 )$

(b) Let $\left\{ f _ { n } \right\}$ be a sequence of non-decreasing functions on r0, 1s such that the series ř $\begin{array} { r } { F ( x ) = \sum _ { n = 1 } ^ { \infty } f _ { n } ( x ) } \end{array}$ converges for all $x \in [ 0 , 1 ]$ . Prove that $\begin{array} { r } { F ^ { \prime } ( x ) = \sum _ { n = 1 } ^ { \infty } f _ { n } ^ { \prime } ( x ) } \end{array}$ almost everywhere.

Solution.
(a) First we extend the definition of f by setting $f ( x ) \ = \ f ( 1 )$ for $x \ > \ 1$ . Note that $f$ is differentiable almost everywhere because it is non-decreasing.
So for almost every x, the representation

$$
f ^ { \prime } ( x ) ~ = ~ \operatorname* { l i m } _ { h  0 ^ { + } } { \frac { f ( x + h ) - f ( x ) } { h } }
$$

is valid.
Since f is non-decreasing, the difference quotient is non-negative for every x and every h. Thus by Fatou’s lemma we have

$$
\begin{array} { r c l } { \displaystyle \int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) d x } & { = } & { \displaystyle \int _ { 0 } ^ { 1 } \displaystyle \operatorname* { l i m } _ { h \to 0 ^ { + } } \frac { f ( x + h ) - f ( x ) } { h } d x \leqslant \displaystyle \operatorname* { l i m } _ { h \to 0 ^ { + } } \int _ { 0 } ^ { 1 } \frac { f ( x + h ) - f ( x ) } { h } d x } \\ & { = } & { \displaystyle \operatorname* { l i m i n f } _ { h \to 0 ^ { + } } \frac { 1 } { h } \int _ { 1 } ^ { 1 + h } f ( x ) d x - \displaystyle \frac { 1 } { h } \int _ { 0 } ^ { h } f ( x ) d x \leqslant f ( 1 ) - f ( 0 ) } \end{array}
$$

where we used the fact that f is non-decreasing again in the last inequality.

(b) First note that since each $f _ { n }$ is non-decreasing, F also is, so F is differentiable almost everywhere.
Let $\begin{array} { r } { r _ { N } ( x ) = \sum _ { n = N + 1 } ^ { \infty } f _ { n } ( x ) } \end{array}$ and write $\begin{array} { r } { F ( x ) = \sum _ { n = 1 } ^ { N } f _ { n } ( x ) + r _ { N } ( x ) } \end{array}$ . Since $r _ { N }$ is also non-decreasing, we can write $\begin{array} { r } { F ^ { \prime } ( x ) = \sum _ { n = 1 } ^ { N } f _ { n } ^ { \prime } ( x ) + r _ { N } ^ { \prime } ( x ) } \end{array}$ for all x at which all three of those functions are differentiable, which is still almost everywhere.
Thus to show the desired result it’s enough to show that $r _ { N } ^ { \prime } ( x )  0$ almost everywhere as $N  \infty$ . First note that for almost every x, $r _ { N } ^ { \prime } ( x ) - r _ { N + 1 } ^ { \prime } ( x ) = ( r _ { N } - r _ { N + 1 } ) ^ { \prime } ( x ) = f _ { N } ^ { \prime } ( x ) \geqslant 0$ because $f _ { N }$ is non-decreasing so its derivative is non-negative wherever it exists.
So $\{ r _ { N } ^ { \prime } ( x ) \}$ is monotonically decreasing in N for almost every x. So the limit lim $N \to \infty \ r _ { N } ^ { \prime } ( x )$ exists almost everywhere and is non-negative (as a limit of non-negative terms).
Thus by the monotone convergence theorem we have

$$
\int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { N \to \infty } r _ { N } ^ { \prime } ( x ) d x \ = \ \operatorname* { l i m } _ { N \to \infty } \int _ { 0 } ^ { 1 } r _ { N } ^ { \prime } ( x ) d x \ \leqslant \ \operatorname* { l i m } _ { N \to \infty } r _ { N } ( 1 ) - r _ { N } ( 0 ) \ = \ 0
$$

where the second to last inequality uses part (a) because each $r _ { N }$ is non-decreasing and the last equality is by the hypothesis that the series defining $F$ converges everywhere.
Thus lim $N \to \infty \ r _ { N } ^ { \prime } ( x )$ is a non-negative function which integrates to 0, so it must be zero almost everywhere.

Problem 5. Let $I _ { 0 , 0 } = [ 0 \AA , 1 ]$ and for $n \geqslant 0 , 0 \leqslant j \leqslant 2 ^ { n } - 1$ , let

$$
{ \cal I } _ { n , j } \ = \ [ j 2 ^ { - n } , ( j + 1 ) 2 ^ { - n } ] .
$$

For $f \in L ^ { 1 } ( [ 0 , 1 ] )$ q define $\begin{array} { r } { E _ { n } f = \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } \left( 2 ^ { n } \int _ { I _ { n , j } } f ( t ) d t \right) \chi _ { I _ { n , j } } } \end{array}$ . Prove that $E _ { n } f \to f$ almost everywhere on r0, 1s.

Solution.
For a fixed $x \in [ 0 , 1 ] , E _ { n } f ( x )$ is simply the average value of f over the interval $I _ { n , j ( n , x ) }$ that x lies in.
It’s clear that the family of intervals $\{ I _ { n , j ( n , x ) } \} _ { n = 1 } ^ { \infty }$ shrinks nicely to x, so it’s a direct consequence of the Lebesgue differentation theorem that $E _ { n } f ( x ) \to f ( x )$ for all Lebesgue points of $f ,$ which is almost everywhere.

Problem 6. For $I _ { n , j }$ as in Problem 5, define the Haar function $h _ { n , j } = 2 ^ { n / 2 } \left( \chi _ { I _ { n + 1 , 2 j } } - \chi _ { I _ { n + 1 , 2 j + 1 } } \right)$ (a) Draw $I _ { 2 , 1 }$ and graph $h _ { 2 , 1 }$

(b) Prove that if $f \in L ^ { 2 } ( [ 0 , 1 ] )$ and $\int _ { 0 } ^ { 1 } f ( t ) d t = 0$ , then

$$
\int _ { 0 } ^ { 1 } | f ( x ) | ^ { 2 } d x \ = \ \sum _ { n \geqslant 0 , 0 \leqslant j \leqslant 2 ^ { n } - 1 } \left| \int _ { 0 } ^ { 1 } f ( t ) h _ { n , j } ( t ) d t \right| ^ { 2 } .
$$

(c) Prove that if $f \in L ^ { 1 } ( [ 0 , 1 ] )$ and $\int _ { 0 } ^ { 1 } f ( t ) d t = 0$ , then almost everywhere on r0, 1s,

$$
f ( x ) \ = \ \sum _ { n = 0 } ^ { \infty } \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } \left( \int _ { 0 } ^ { 1 } f ( t ) h _ { n , j } ( t ) d t \right) h _ { n , j } ( x ) .
$$

Solution.
(a)

(b) Let $M = \left\{ f \in L ^ { 2 } ( [ 0 , 1 ] ) : \int _ { 0 } ^ { 1 } f = 0 \right\}$ . First note that M is a closed subspace of $L ^ { 2 } ;$ if $f _ { n } \in M$ and $f _ { n }  f$ in $L ^ { 2 }$ , then by Cauchy-Schwarz we also have $f _ { n }  f$ in $L ^ { 1 }$ , so in particular $\int f _ { n } \to \int f ,$ , so $\int _ { f } \ d z = 0$ as well.
Thus we can consider M as a Hilbert space.
Next note that ş ş $\{ h _ { n , j } \} _ { n , j }$ form an orthonormal set in M : It’s clear that $\int h _ { n , j } ^ { 2 } = 1$ for each $n , j$ . Now consider $\int h _ { n , j } h _ { m , k }$ . Suppose without loss of generality that $m \geqslant n ,$ There are only two possibilities, either $h _ { n , j }$ and $h _ { m , k }$ have disjoint supports, in which case the integral is clearly zero, or the support of $h _ { m , k }$ is contained in a set on which $h _ { n , j }$ is constant, in which case the integral is just a constant multiple of $\int h _ { m , k }$ , which is 0. Thus they form an orthonormal set.
We want to show they form an orthonormal basis for M. If we show this, then the desired conclusion is just theş statement of Parseval’s identity and we will be done.
Let $f \in M$ and suppose that $\int f h _ { n , j } = 0$ for all $n , j$ It’s enough to show this implies $f = 0$ . First note that we have $\int _ { 0 } ^ { 1 } f = \int _ { 0 } ^ { 1 / 2 } f + \int _ { 1 / 2 } ^ { 1 } f = 0$ . We also have by assumption $\int f h _ { 0 , 0 } = \int _ { 0 } ^ { 1 / 2 } f - \int _ { 1 / 2 } ^ { 1 } f = 0$ . Combining these two yields $\begin{array} { l } { { \int _ { 0 } ^ { 1 / 2 } f = \int _ { 1 / 2 } ^ { 1 } f = 0 } } \end{array}$ . Continuing, we have $0 = \int _ { 0 } ^ { 1 / 2 } f = \int _ { 0 } ^ { 1 / 4 } f + \int _ { 1 / 4 } ^ { 1 / 2 }$ , and by assumption, $0 = \textstyle \int f h _ { 1 , 0 } = \int _ { 0 } ^ { 1 / 4 } f - \int _ { 1 / 4 } ^ { 1 / 2 } f ,$ and combining these gives $\begin{array} { l } { { \int _ { 0 } ^ { 1 / 4 } f = \int _ { 1 / 4 } ^ { 1 / 2 } f = 0 } } \end{array}$ . Continuing in this way inductively shows that $\textstyle \int _ { I n , j } f = 0$ for all $n , j$ . Any closed interval can be written as a countable disjoint union of the $I _ { n , j }$ , so the integral of f over any closed interval vanishes, which implies $f = 0$ □

(c) Let

$$
S _ { N } f ( x ) ~ = ~ \sum _ { n = 0 } ^ { N } \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } \left( \int _ { 0 } ^ { 1 } f ( t ) h _ { n , j } ( t ) d t \right) h _ { n , j } ( x ) .
$$

In light of problem 5 above, it’s enough to show that ${ \cal S } _ { N } f ( x ) = { \cal E } _ { N + 1 } f ( x )$ for almost every x. We show this holds for any x which is not an endpoint of any $I _ { n , j }$ . Fix such an x. Define $j ( n )$ to be the unique j such that $x \in I _ { n , j }$ and define $j ( n ) ^ { c }$ to be the unique $j \neq j ( n )$ such that $I _ { n , j ( n ) } \cup I _ { n , j ( n ) ^ { c } } = I _ { n - 1 , j ( n - 1 ) }$ . Then we have

$$
\begin{array} { r l } { S _ { N } f ( x ) } & { = \displaystyle \sum _ { n = 0 } ^ { N } \left( \int _ { 0 } ^ { 1 } f ( \bar { y } ) h _ { n , j , ( n ) } ( \bar { y } ) \ d x \right) h _ { n , j , ( n ) } ( x ) } \\ & { = \displaystyle \sum _ { n = 0 } ^ { N } 2 ^ { n } \left( \int _ { x _ { n + 1 , ( n + 1 ) } } f - \int _ { L _ { n + 1 , ( n + 1 ) } } f \right) } \\ & { = \displaystyle \sum _ { n = 0 } ^ { N } 2 ^ { n } \left( 2 \int _ { L _ { n + 1 , ( n + 1 ) } } f - \int _ { L _ { n + 1 , ( n - 1 ) } } f \right) } \\ & { = \displaystyle \sum _ { n = 0 } ^ { N } 2 ^ { n + 1 } \left( 2 \int _ { L _ { n + 1 , ( n + 1 ) } } f - \int _ { L _ { n + 1 , ( n + 1 ) } } f \right) } \\ & { = \displaystyle \sum _ { n = 0 } ^ { N } 2 ^ { n + 1 } \int _ { L _ { n + 1 , ( n + 1 ) } } f - 2 ^ { n } \int _ { L _ { n + 1 , ( n + 1 ) } } f } \\ & { - 2 ^ { N + 1 } \displaystyle \int _ { L _ { n + 1 , ( n + 1 ) } } f - \int _ { L _ { n + 1 , ( n + 1 ) } } f } \\ & { - 2 ^ { N + 1 } \displaystyle \int _ { L _ { n - 1 , ( n + 1 ) } } f - \int _ { L _ { n + 1 , ( n + 1 ) } } f ( x ) \ d x \ d x } \end{array}
$$

Problem 7. Let µ be a finite positive Borel measure on C.

(a) Prove that $F ( z ) = \int _ { \mathbb { C } } \frac { 1 } { z - w } d \mu ( w )$ exists for almost all $z \in \mathbb { C }$ and that $\int _ { K } | F ( z ) |$ dx dy ă 8 for every compact $K \subseteq \mathbb { C }$

(b) Prove that for almost every horizontal line L and all compact $K \subseteq L , \int _ { K } | F ( x + i y ) | d x < \infty$

(c) Prove that for almost all open squares S with sides parallel to the axes,

$$
\mu ( S ) \ = \ { \frac { 1 } { 2 \pi i } } \int _ { \partial S } F ( z ) d z .
$$

Solution.
(a) The second half of the assertion implies the first half, so we focus on the second.
It’sş enough to show that $\int _ { | z | \leqslant R } | F ( z ) | d A ( z ) < \infty$ for each R. We estimate

$$
\begin{array} { r l } { \displaystyle \int _ { | z | \leqslant R } | F ( z ) | d A ( z ) } & { \leqslant \displaystyle \int _ { | z | \leqslant R } \int _ { w \leqslant \mathsf { C } } \frac { 1 } { | z - w | } d \mu ( w ) d A ( z ) \ = \ \displaystyle \int _ { w \in \mathsf { C } } \int _ { | z | \leqslant R } \frac { 1 } { | z - w | } d A ( z ) d \mu ( w ) \quad \mathrm { b y ~ T o n e l l i } } \\ & { = \ \displaystyle \int _ { | w | \leqslant 2 R } \int _ { | z | \leqslant R } \frac { 1 } { | z - w | } d A ( z ) d \mu ( w ) + \displaystyle \int _ { | w | > 2 R } \int _ { | z | \leqslant R } \frac { 1 } { | z - w | } d A ( z ) d \mu ( w ) } \\ & { \leqslant \ \displaystyle \int _ { | w | \leqslant 2 R } \int _ { | z - w | \leqslant 3 R } \frac { 1 } { | z - w | } d A ( z ) d \mu ( w ) + \displaystyle \int _ { | w | > 2 R } \int _ { | z | \leqslant R } \frac { 1 } { R } d A ( z ) d \mu ( w ) } \\ & { \leqslant \displaystyle \int _ { | w | \leqslant 2 R } C _ { R } d \mu ( w ) + \displaystyle \int _ { | w | > 2 R } \pi R d \mu ( w ) \quad \mathrm { w h e r e ~ } C _ { R } \mathrm { ~ i s ~ s o m e ~ c o n s t a n t ~ d e p e n d i n g ~ o n ~ } R } \\ & { \sim \ \displaystyle \int _ { | w | \leqslant 2 R } } \end{array}
$$

because µ is a finite measure.

(b) As in part (a), it’s enough to prove the assertion with any compact set K replaced by any interval of the form $[ - R , R ]$ . Fix some R and an integer m. Then by part (a) and Tonelli’s theorem, we know $\int _ { m } ^ { m + 1 } \int _ { R } ^ { R } | F ( x + i y ) |$ dx dy ă 8. This implies that there is a set $Y _ { m , R }$ of full measure in $[ m , m + 1 ]$ such that $\int _ { R } ^ { R } | F ( x + i y ) |$ dx ă 8 for each $y \in Y _ { m , R }$ . By setting $\begin{array} { r } { Y _ { m } = \bigcap _ { R = 1 } ^ { \infty } Y _ { m , R } } \end{array}$ , we see that Y still has full measure in $[ m , m + 1 ]$ and now for any $\textstyle y \in Y _ { m } , \int _ { R } ^ { R } | F ( x + i y ) |$ | dx ă 8 for every R. Thus we have shown that almost everyŤ horizontal line with y-intercept in $[ m , m + 1 ]$ satisfies the desired property.
Now setting ş $\textstyle Y = \bigcup _ { m = - \infty } ^ { \infty } Y _ { m }$ , we see that Y is an almost everywhere subset of R with the property that $y \in Y$ implies $\textstyle \int _ { R } ^ { R } | F ( x + i y ) | d x < \infty$ for every R, which is the desired conclusion.
In fact, by examining the proof of part (a) it’s clear that weş ş actually proved something a bit stronger, which is that $y \in Y$ implies $\begin{array} { r } { \int _ { K } \int _ { w \in \mathbb { C } } \frac { 1 } { | x + i y - w | } d \mu ( w ) d x < \infty } \end{array}$ for all compact sets K (we’ll need this version in part (c)).

(c) The same argument as in part (b) shows that the analogous result to part (b) for vertical lines also holds.
Let S be the collection of squares S in C such that all four sides of S lie on lines for which the conclusion of part (b) holds.
It’s clear that S is almost every square in C. Thus for $S \in S$ , we have

$$
\begin{array} { r c l } { { \displaystyle \int _ { \partial S } F ( z ) d z ~ = ~ \int _ { \partial S } \int _ { \mathbb { C } } \frac { 1 } { z - w } d \mu ( w ) d z ~ = ~ \displaystyle \int _ { \mathbb { C } } \int _ { \partial S } \frac { 1 } { z - w } d z d \mu ( w ) } } \\ { { { } } } & { { { } } } & { { { } = ~ \displaystyle \int _ { \mathbb { C } } 2 \pi i \chi _ { S } ( w ) d \mu ( w ) ~ = ~ 2 \pi i \mu ( S ) , } } \end{array}
$$

which is the desired result.
We just need to justify switching the order of integration in the first line.
Note that by definition of S,

$$
\int _ { \partial S } \int _ { \mathbb { C } } { \frac { 1 } { | z - w | } } d \mu ( w ) d z
$$

is simply a sum of four integrals along horizontal or vertical lines which are known to be finite by the comment at the end of part (b). Thus Fubini-Tonelli applies, so the switch is justified.

Problem 8. Let f be an entire non-constant function that satisfies the functional equation

$$
f ( 1 - z ) ~ = ~ 1 - f ( z )
$$

for all $z \in \mathbb { C } .$ . Show that $f ( \mathbb { C } ) = \mathbb { C }$

Solution.
The functional equation implies that $w \in \operatorname { I m } ( f )$ if and only ${ \mathrm { i f ~ 1 - } } w \in \operatorname { I m } ( f )$ . Thus suppose that there were some w $\notin$ Impfq, then 1 ´ w R Impfq either, so f misses two points $( \mathrm { i f } w \ne 1 / 2 )$ . But Picard’s little theorem says that an entire function that misses two points is constant, a contradiction.
Thus f hits everything except possibly $1 / 2$ . But putting $z = 1 / 2$ into the functional equation gives $f ( 1 / 2 ) = 1 - f ( 1 / 2 )$ so $f ( 1 / 2 ) = 1 / 2$ . Thus $f$ is surjective.
□

Problem 9. Let $f ( z )$ be an analytic function on the entire complex plane C and assume $f ( 0 ) \neq 0$ . Let $\left\{ a _ { n } \right\}$ be the zeros of $f ,$ counted with multiplicity.

(a) Let $R > 0$ be such that $| f ( z ) | > 0 \mathrm { o n } | z | = R .$ . Prove

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log \left| f ( R e ^ { i \theta } ) \right| d \theta \ = \ \log \left| f ( 0 ) \right| + \sum _ { \left| a _ { n } \right| < R } \log \left( \frac { R } { \left| a _ { n } \right| } \right) .
$$

(b) Assume $| f ( z ) | \leqslant C e ^ { | z | ^ { \lambda } }$ for positive constants C and λ. Prove that

$$
\sum _ { n } \left( \frac { 1 } { | a _ { n } | } \right) ^ { \lambda + \epsilon } < \infty
$$

for all $\epsilon > 0 .$

Solution.
See Spring 2017 $\# 9$

Problem 10. Let $\mu$ be Lebesgue measure on D. Let H be the subspace of $L ^ { 2 } ( \mathbb { D } , \mu )$ consisting of holomorphic functions.
Show that H is complete.

Solution.
See Fall 2014 $\# 1 0$ (not exactly the same problem, but a similar idea).

Problem 11. Suppose that $f : \mathbb { D } \to \mathbb { C }$ is holomorphic and injective in some annulus $\{ z : r < | z | < 1 \}$ . Show that $f$ is injective in D.

Solution.
Suppose there are $z _ { 1 } , z _ { 2 } \in \mathbb { D }$ with $f ( z _ { 1 } ) ~ = ~ f ( z _ { 2 } ) ~ = ~ w$ Then there is a circle $C$ of radius $s \in ( r , 1 )$ containing both $z _ { 1 }$ and $z _ { 2 }$ in its interior.
Then the function $f - w$ has at least two zeros inside $C ,$ so the argument principle tells us that the curve $f ( C )$ has winding number at least 2 around zero.
But a curve of winding number at least 2 has to intersect itself, meaning that there are two different points on the curve C at which $f - w$ takes the same value.
But since S lies in the annulus $r < | \boldsymbol { z } | < 1$ , this contradicts the fact that $f$ is injective on the annulus.

Problem 12. Let Q be the closed unit square in C and let R be the closed rectangle in C with vertices $\{ 0 , 2 , i , 2 + i \}$ . Prove there does not exists a surjective homeomorphism $f : Q  R$ that is conformal on the interior of Q and maps corners to corners.

Solution.
Suppose $f : Q  R$ satisfies the given conditions.
By continuity, it must preserve the order of the vertices, so by precomposing with rotations and flips if necessary, we may assume that $f$ fixes the vertical line segment r0, is.
By the Schwarz reflection principle, applied iteratively and reflecting over the vertical lines, we can extend $f$ to a map from the strip $0 \leqslant \mathrm { I m } ( z ) \leqslant 1$ to itself.
We can then reflect over the two horizontal lines to extend $f$ to a map from the strip ´1 ď Impzq ď 2 to itself.
This strip is simply connected and so is conformally equivalent to D. So $f$ has been extended to a conformal automorphism of a region conformally equivalent to D, and f has two fixed points, which implies $f$ is the identity, a contradiction.

## 2 Fall 2009

Problem 1. Find a non-empty closed set in the Hilbert space $L ^ { 2 } ( [ 0 , 1 ] )$ that does not contain an element of smallest norm.

Solution.
Let $f _ { n } = n \cdot \chi _ { [ 0 , 1 / n ^ { 2 } + 1 / n ^ { 3 } ] }$ . We claim $\{ f _ { n } \} _ { n = 2 } ^ { \infty }$ is such a set.
First note that

$$
\int | f _ { n } | ^ { 2 } = \left( { \frac { 1 } { n ^ { 2 } } } + { \frac { 1 } { n ^ { 3 } } } \right) \cdot n ^ { 2 } \ = \ 1 + { \frac { 1 } { n } } ,
$$

so we see that the set has no element of smallest norm.
To show it’s closed, suppose $g \in L ^ { 2 }$ is a limit point.
Then there is a subsequence $f _ { n _ { k } }$ converging to g in $L ^ { 2 }$ . But this implies there is a further subsequence $f _ { n _ { k _ { \ell } } }$ converging almost everywhere to g. But it’s clear that $f _ { n } \to 0$ almost everywhere, so $g = 0$ . But 0 is clearly not a limit point of $\left\{ f _ { n } \right\}$ because $\| f _ { n } \| _ { L ^ { 2 } } > 1$ for each n. Thus $\left\{ f _ { n } \right\}$ has no limit points so it’s closed.

Problem 2. Let v be a trigonometric polynomial in two variables, i.e.

$$
v ( x , y ) \ = \ \sum _ { n , m \in \mathbb { Z } } a _ { n , m } e ^ { 2 \pi i ( n x + m y ) }
$$

with only finitely many nonzero $a _ { n , m }$ . If $u = v - \Delta v$ where $\Delta = \hat { \sigma } _ { x } ^ { 2 } + \hat { \sigma } _ { y } ^ { 2 }$ is the Laplacian, prove that

$$
\| v \| _ { L ^ { \infty } ( [ 0 , 1 ] ^ { 2 } ) } \ \leqslant \ C \| u \| _ { L ^ { 2 } ( [ 0 , 1 ] ^ { 2 } ) }
$$

for some constant C independent of v.

Solution.
A straightforward computation shows that

$$
u ( x , y ) ~ = ~ \sum _ { n , m } a _ { n , m } ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) e ^ { 2 \pi i ( n x + m y ) } .
$$

Thus, using orthonormality and the fact that only finitely many coefficients are nonzero, we have

$$
\begin{array} { r l } { \displaystyle \int _ { 0 } ^ { 1 } \displaystyle \int _ { 0 } ^ { 1 } | u ( x , y ) | ^ { 2 } \ d x \ d y \ = } & { \displaystyle \int _ { 0 } ^ { 1 } \displaystyle \int _ { 0 } ^ { 1 } \displaystyle \sum _ { n , m , k , \ell } a _ { n , m } \overline { { a _ { k , \ell } } } ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) ( 1 + 4 \pi ^ { 2 } ( k ^ { 2 } + \ell ^ { 2 } ) ) e ^ { 2 \pi i ( n \cdot 2 + m y ) } e ^ { - 2 \pi i ( k x + \xi y ) } d x \ d y } \\ { \displaystyle } & { = \displaystyle \sum _ { n , m , k , \ell } a _ { n , m } \overline { { a _ { k , \ell } } } ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) ( 1 + 4 \pi ^ { 2 } ( k ^ { 2 } + \ell ^ { 2 } ) ) \displaystyle \int _ { 0 } ^ { 1 } e ^ { 2 \pi i ( n - k ) x } d x \int _ { 0 } ^ { 1 } e ^ { 2 \pi i ( m - \ell ) y } d y } \\ { \displaystyle } & { = \displaystyle \sum _ { n , m } \left| a _ { n , m } \right| ^ { 2 } ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) ^ { 2 } . } \end{array}
$$

Now we simply estimate v using the triangle inequality and Cauchy-Schwarz:

$$
\begin{array} { r c l } { | v ( x , y ) | ^ { 2 } } & { \leqslant \displaystyle \left( \sum _ { n , m } | a _ { n , m } | \right) ^ { 2 } = \displaystyle \ \left( \sum _ { n , m } | a _ { n , m } | ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) \cdot \frac { 1 } { ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) } \right) ^ { 2 } } \\ & { \leqslant \displaystyle \left( \sum _ { n , m } | a _ { n , m } | ^ { 2 } ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) ^ { 2 } \right) \left( \sum _ { n , m } \frac { 1 } { ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) ^ { 2 } } \right) } \\ & { = \displaystyle C \cdot | | u | | _ { L ^ { 2 } ( [ 0 , 1 ] ^ { 2 } ) } ^ { 2 } } \end{array}
$$

because $\scriptstyle \sum _ { n , m } { \frac { 1 } { ( 1 + 4 \pi ^ { 2 } ( n ^ { 2 } + m ^ { 2 } ) ) ^ { 2 } } }$ converges.
Thus we have established $\| v \| _ { L ^ { \infty } ( [ 0 , 1 ] ^ { 2 } ) } ^ { 2 } \leqslant C \| u \| _ { L ^ { 2 } ( [ 0 , 1 ] ^ { 2 } ) } ^ { 2 }$ which implies the desired result.

Problem 3. Let $f : [ 0 , 1 ] \to \mathbb { R }$ be continuous with

$$
\operatorname* { m i n } _ { x \in [ 0 , 1 ] } f ( x ) \ = \ 0 .
$$

Assume that for all $0 \leqslant a < b \leqslant 1$ we have

$$
\int _ { a } ^ { b } ( f ( x ) - \operatorname* { m i n } _ { y \in [ a , b ] } f ( y ) ) d x \ \leqslant \ { \frac { 1 } { 2 } } ( b - a ) .
$$

(a) Prove that for all $\lambda \geqslant 0$

$$
| \{ x : f ( x ) > \lambda + 1 \} | \ \leqslant \ { \frac { 1 } { 2 } } \left| \{ x : f ( x ) > \lambda \} \right| .
$$

(b) Prove that for all $1 \leqslant c < 2$

$$
\int _ { 0 } ^ { 1 } c ^ { f ( x ) } d x \leqslant { \frac { 1 0 0 } { 2 - c } } .
$$

Solution.
(a) Fix $\lambda \geqslant 0 ,$ Since $f$ is continuous, $\{ x : f ( x ) > \lambda \}$ is open, and thus it can be written as a countable union of disjoint open intervals $( a _ { j } , b _ { j } )$ (the set is only open relative to r0, 1s, so it’s possible that one of the intervals is closed on the left at 0 and another is closed on the right at 1, but that doesn’t change any of the following work, so we ignore it).
Also by continuity, we must have min $ _ { \cdot y \in [ a _ { j } , b _ { j } ] } f ( y ) = \lambda$ for each $j .$ Thus using the hypothesis on $f ,$ for each $j$ we have

$$
{ \frac { 1 } { 2 } } ( b _ { j } - a _ { j } ) \ \geqslant \ \int _ { a _ { j } } ^ { b _ { j } } { \big ( } f ( x ) - \lambda { \big ) } d x \ = \ \int _ { a _ { j } } ^ { b _ { j } } f ( x ) d x - \lambda ( b _ { j } - a _ { j } ) .
$$

Summing both sides from $j = 1$ to 8 gives

$$
\left( { \frac { 1 } { 2 } } + \lambda \right) \left| \left\{ x : f ( x ) > \lambda \right\} \right| \geqslant \int _ { \left\{ f > \lambda \right\} } f ( x ) d x .
$$

We also have

$$
\begin{array} { r l } { \displaystyle \int _ { \{ f > \lambda \} } f ( x ) d x \ = \ \int _ { \{ f > \lambda + 1 \} } f ( x ) d x + \int _ { \{ \lambda < f \leqslant \lambda + 1 \} } f ( x ) d x } \\ { \geqslant \ ( \lambda + 1 ) \left| \{ x : f ( x ) > \lambda + 1 \} \right| + \lambda \left| \{ x : f ( x ) > \lambda + 1 \} \backslash \{ x : f ( x ) > \lambda \} \right| } \\ { \ = \ ( \lambda + 1 ) \left| \{ x : f ( x ) > \lambda + 1 \} \right| + \lambda \left( \left| \{ x : f ( x ) > \lambda \} \right| - \left| \{ x : f ( x ) > \lambda + 1 \} \right| \right) } \\ { \ = \ \left| \{ x : f ( x ) > \lambda + 1 \} \right| + \lambda \left| \{ x : f ( x ) > \lambda \} \right| . } \end{array}
$$

Combining this with the above inequality and rearranging gives the desired result.

(b) Fix $1 \leqslant c < 2$ . We can write

$$
\int _ { 0 } ^ { 1 } c f ^ { ( \alpha ) } d x = c ^ { 0 } \cdot | \{ f = 0 \} | + \sum _ { j = 0 } ^ { \infty } \int _ { \{ j < f \leq j + 1 \} } c f ^ { ( \alpha ) } d x \leqslant 1 + \sum _ { j = 0 } ^ { \infty } c ^ { j + 1 } \left| \{ j < f \leqslant j + 1 \} \right| \leqslant 1 + \sum _ { j = 0 } ^ { \infty } c ^ { j + 1 } \left| \{ f > j \} \right| .
$$

We know that $| \{ x : f ( x ) > 0 \} | \ \leqslant \ 1$ , so by inductively applying the conclusion of part (a) we see that $| \{ x : f ( x ) > j \} | \leqslant 2 ^ { - j }$ . Thus we have

$$
\int _ { 0 } ^ { 1 } c ^ { f ( x ) } d x \leqslant 1 + \sum _ { j = 0 } ^ { \infty } c ^ { j + 1 } 2 ^ { - j } = 1 + c \sum _ { j = 0 } ^ { \infty } ( c / 2 ) ^ { j } = 1 + { \frac { c } { 1 - c / 2 } } = { \frac { 2 + c } { 2 - c } } \leqslant { \frac { 1 0 0 } { 2 - c } }
$$

where the geometric series converges because $c < 2 . \qquad \square$

Problem 4. Prove the following variant of the Lebesgue differentiation theorem: Let $\mu$ be a finite Borel measure on R, singular with respect to Lebesgue measure.
Then for Lebesgue almost every $x \in \mathbb { R }$ ,

$$
\operatorname* { l i m } _ { \epsilon \to 0 } { \frac { \mu ( [ x - \epsilon , x + \epsilon ) } { 2 \epsilon } } ~ = ~ 0 .
$$

Solution.
See Fall 2016 $\# 2$

Problem 5. Construct a Borel subset E of the real line R such that for all intervals ra, bs we have

$$
0 ~ < ~ m ( E \cap [ a , b ] ) ~ < ~ b - a
$$

where m denotes Lebesgue measure.

Solution.

Problem 6. The Poisson kernel for $0 \leqslant \rho < 1$ is the 2π-periodic function on R defined by

$$
P _ { \rho } ( \theta ) ~ = ~ \mathrm { R e } \left( \frac { 1 + \rho e ^ { i \theta } } { 1 - \rho e ^ { i \theta } } \right) .
$$

For functions h continuous on and harmonic inside the closed disc of radius R about the origin one has

$$
h ( r e ^ { i \eta } ) ~ = ~ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } P _ { r / R } ( \eta - \theta ) h ( R e ^ { i \theta } ) d \theta .
$$

Assume that h is harmonic and positive on D. Prove that there exists a positive Borel measure $\mu$ on r0, 2πs such that for all $r e ^ { i \eta } \in \mathbb { D }$ one has

$$
h ( r e ^ { i \nu } ) ~ = ~ \int _ { 0 } ^ { 2 \pi } P _ { r } ( \eta - \theta ) d \mu ( \theta ) .
$$

Solution.
For each $0 ~ < ~ R < ~ 1$ define the measure $\mu _ { R }$ by $d \mu _ { R } ( \theta ) ~ = ~ h ( R e ^ { i \theta } ) d \theta$ By scaling we may assume $h ( 0 ) = 1$ Since h is positive and continuous, each $\mu _ { R }$ is a positive Borel measure on r0, 2πs. By the Riesz representation theorem, we may view each $\mu _ { R }$ as a bounded linear functional on the Banach space $C ( [ 0 , 2 \pi ] )$ . Note that by the special case of the given formula with $r = 0 ~ ( \mathrm { i . e }$ . the mean value property), we have

$$
| | \mu _ { R } | | ~ = ~ \mu _ { R } ( [ 0 , 2 \pi ] ) ~ = ~ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } h ( R e ^ { i \theta } ) d \theta { } ~ = ~ h ( 0 ) .
$$

Thus each $\mu _ { R }$ is in the unit ball of the dual space $C ( [ 0 , 2 \pi ] ) ^ { * }$ By Banach-Alaoglu and the fact that $C ( [ 0 , 2 \pi ] )$ is separable, this implies that we have a subsequence of Rs converging to 1 and some measure $\mu$ in the unit ball of $C ( [ 0 , 2 \pi ] )$ with $\mu _ { R } \to \mu$ in the weak-˚ topology.
A standard approximation argument shows that $\mu$ must also be a positive measure since each $\mu _ { R }$ is.
We claim that $\mu$ is the desired measure.
Fix $r e ^ { i \eta } \in \mathbb { D } .$ Note that each $P _ { \rho }$ is continuous on r0, 2πs and $P _ { r / R }  P _ { r }$ uniformly on r0, 2πs as $R \to 1$ . For each $R < 1$ the given formula tells us

$$
h ( r e ^ { i \eta } ) ~ = ~ \int _ { 0 } ^ { 2 \pi } P _ { r / R } ( \eta - \theta ) d \mu _ { R } ( \theta ) .
$$

Taking the limit as $R \to 1$ on both sides gives the desired result, where we have assumed the followingş ş lemma: if $f _ { n }$ are continuous and $f _ { n }  f$ uniformly on r0, 2πs and $\mu _ { n }  \mu$ in weak-˚, then $\int f _ { n } d \mu _ { n } \to \int f d \mu .$ The proof of this just follows by writing

$$
\left| \int f _ { n } d \mu _ { n } - \int f d \mu \right| \leqslant \ \left| \int f _ { n } d \mu _ { n } - \int f _ { n } d \mu \right| + \left| \int f _ { n } d \mu - \int f d \mu \right|
$$

and noting that the first term goes to 0 by weak-˚ convergence and the second term goes to zero by uniform convergence.

Problem 7. (a) Define unitary operator on a complex Hilbert space.

(b) Let S be a unitary operator on a complex Hilbert space.
Prove that for every complex number $| \lambda | < 1$

the operator $S - \lambda I$ is invertible.

(c) For a fixed vector v in the Hilbert space and all $| \lambda | < 1$ , define

$$
h ( \lambda ) \ = \ \left. ( S + \lambda I ) ( S - \lambda I ) ^ { - 1 } v , v \right. .
$$

Show $\mathrm { R e } ( h )$ is a positive harmonic function (you may not use the spectral theorem).

Solution.
$( \mathrm { a } ) \ S : H \to H$ is unitary if $\langle S x , S y \rangle = \langle x , y \rangle$ for all $x , y \in H$

(b) Suppose $( S - \lambda I ) x = 0$ but $x \neq 0$ . Then we have

$$
\begin{array} { r l } { 0 \ = \ \langle ( S - \lambda I ) x , ( S - \lambda I ) x \rangle \ = \ \langle S x - \lambda x , S x - \lambda x \rangle \ = \ \left. \lvert S x \right. \| ^ { 2 } + \left. \lambda \right. ^ { 2 } \left. \lvert x \right. \| ^ { 2 } - 2 \operatorname { R e } ( \lambda \langle x , S x \rangle ) } \\ { = \ ( 1 + \left. \lambda \right. ^ { 2 } ) \left. \left. x \right. \right. ^ { 2 } - 2 \operatorname { R e } ( \lambda \langle x , S x \rangle ) . } \end{array}
$$

Thus we have

$$
( 1 + | \lambda | ^ { 2 } ) | | x | | ^ { 2 } \ = \ 2 \operatorname { R e } ( \lambda \langle x , S x \rangle ) \ \leqslant \ 2 | \lambda | | \langle x , S x \rangle | \ \leqslant \ 2 | \lambda | | | x | | | | S x | | \ = \ 2 | \lambda | | | x | | ^ { 2 } .
$$

Since we are assuming $x \neq 0$ this implies $( 1 + | \lambda | ^ { 2 } ) \leqslant 2 | \lambda |$ , which is impossible for $| \lambda | < 1$ . Thus $S - \lambda I$ is injective and therefore invertible.

(c)

Problem 8. Let Ω be an open convex region in the complex plane.
Assume $f$ is a holomorphic function on Ω and the $\mathrm { R e } ( f ^ { \prime } ( z ) ) > 0$ for all $z \in \Omega$

(a) Prove that f is one-to-one.

(b) Show by example that the word “convex” cannot be replaced by “connected and simply connected”.

Solution.
(a) Let $a \ne b \in \Omega$ . Let $\gamma$ be a straight line from a to ş $b ,$ parameterized by $\gamma ( t ) = ( 1 - t ) b + t a .$ By convexity, γ lies in Ω. So we can write $\int _ { \gamma } f ^ { \prime } ( z ) d z \ = \ f ( b ) - f ( a )$ . Write $f = u + i v$ , then $f ^ { \prime } = u _ { x } + i v _ { x }$ Examining the integral above, we have

$$
f ( b ) - f ( a ) \ = \ \int _ { \gamma } f ^ { \prime } ( z ) d z \ = \ \int _ { 0 } ^ { 1 } ( u _ { x } ( \gamma ( t ) ) + i v _ { x } ( \gamma ( t ) ) ) ( b - a ) d t \ = \ ( b - a ) \int _ { 0 } ^ { 1 } ( u _ { x } ( \gamma ( t ) ) + i v _ { x } ( \gamma ( t ) ) ) d t .
$$

Note that the integral on the right side has nonzero real part because $u _ { x }$ is always positive.
Thus the whole right side is just some nonzero complex number since $b - a$ is a nonzero constant, so $f ( b ) \neq f ( a ) . \quad $

Problem 9. Let f be a non-constant meromorphic function on C that obeys

$$
f ( z ) ~ = ~ f ( z + \sqrt { 2 } ) ~ = ~ f ( z + i \sqrt { 2 } ) .
$$

Assume f has at most one pole in the closed unit disc D.

(a) Prove that f has exactly one pole in D.

(b) Prove that this is not a simple pole.

Solution.
(a) We just need to show f has at least one pole in D. Let $\Lambda \ = \ \left\lceil 0 , \sqrt { 2 } \right\rceil \times \left\lceil 0 , i \sqrt { 2 } \right\rceil$ be a fundamental domain for f and let M be the discrete lattice generated by $\sqrt { 2 }$ and $i { \sqrt { 2 } }$ Simple geometry shows that every point of Λ is at most 1 away from one of the vertices.
Thus every point of Λ is equivalent mod M to some point of D. Since f is non-constant and doubly periodic, it must have a pole somewhere (otherwise it would be holomorphic and bounded and therefore constant), so it must have a pole in Λ, and thus must have a pole in D.

(b) The work in part (a) shows that every point of C is equivalent mod M to some point of ${ \overline { { \mathbb { D } } } } ,$ so the fact that f has exactly one pole in D implies that f has exactly one distinct pole mod M. The desired result now follows from the general fact that a doubly periodic function can’t have only a single simple pole (mod

M), a proof of which is reproduced here (see e.g. Ahlfors Complex Analysis).
Since the zeros and poles of f are discrete, we can find a fundamental domain Λ of M such that f has no zeros or poles on BΛ. Thusş by double periodicity, it is clear that $\int _ { \partial \Lambda } f ( z ) d z = 0$ because the integrals over opposite sides of Λ going in opposite directions cancel each other out.
So by the residue theorem, the sums of residues of all the poles inside Λ is 0, implying there can’t only be one simple pole.

## 3 Spring 2010

Problem 1. (a) Let $1 \leqslant p < \infty$ . Show that if a sequence of real-valued functions $\left\{ f _ { n } \right\}$ converges in $L ^ { p } ( \mathbb { R } )$ then it contains a subsequence that converges almost everywhere.

(b) Give an example of a sequence of functions converging to 0 in $L ^ { 2 } ( \mathbb { R } )$ that does not converge almost everywhere.

Solution.

Problem 2. Let $p _ { 1 } , \ldots , p _ { n }$ be distinct points in $\mathbb { C }$ and let U be the domain $C \backslash \{ p _ { 1 } , \ldots , p _ { n } \}$ Let A be the vector space of real harmonic functions on U and let $B \subseteq A$ be the subspace of real parts of complex analytic functions on U. Find the dimension of the quotient space $A / B$ and give a basis.

Solution.
See Spring 2017 #10.

Problem 3. For $f : \mathbb { R } \to \mathbb { R }$ in $L ^ { 1 } ( \mathbb { R } )$ , let $M f$ be the (centered) Hardy-Littlewood maximal function.
Prove there is a constant A such that for any $\lambda > 0$

$$
m \{ x \in \mathbb { R } : M f ( x ) > \lambda \} ~ \leqslant ~ \frac { A } { \lambda } \vert \vert f \vert \vert _ { L ^ { 1 } }
$$

where m is Lebesgue measure.
If you use a covering lemma, you should prove it.

Solution.
See Fall 2011 $\# 5$

Problem 4. Let $f ( z )$ be a continuous function on $\overline { { \mathbb { D } } }$ such that $f$ is analytic on D and $f ( 0 ) \neq 0$ (a) Prove that if $0 < r < 1$ and if $\begin{array} { r } { \operatorname* { i n f } _ { | z | = r } | f ( z ) | > 0 } \end{array}$ , then

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log \left| f ( r e ^ { i \theta } ) \right| d \theta \ \geqslant \ \log \left| f ( 0 ) \right| .
$$

(b) Prove that $m \{ \theta \in [ 0 , 2 \pi ] : f ( e ^ { i \theta } ) = 0 \} = 0$ where m is Lebesgue measure.

Solution.
See Fall 2016 #8.

Problem 5. (a) For $f \in L ^ { 2 } ( \mathbb { R } )$ and a sequence $\{ x _ { n } \} \subseteq \mathbb { R }$ which converges to zero, define $f _ { n } ( x ) : = f ( x + x _ { n } )$ Show that $\left\{ f _ { n } \right\}$ converges to f in $L ^ { 2 }$

(b) Let $W \subseteq \mathbb { R }$ be a Lebesgue measurable set of positive Lebesgue measure.
Show that the set of differences $W - W = \{ x - y : x , y \in W \}$ contains an open neighborhood of the origin.

Solution.
(a) See Fall 2011 $\# 3$

(b) Let $f ( x ) = \chi _ { W } ( x )$ and $f _ { y } ( x ) = \chi _ { W } ( x + y )$ . We calculate

$$
\begin{array} { r c l } { \displaystyle | | f - f _ { y } | | _ { L ^ { 2 } } ^ { 2 } } & { = } & { \displaystyle \int ( \chi _ { W } ( x ) - \chi _ { W } ( x + y ) ) ^ { 2 } d x } \\ { \displaystyle } & { = } & { \displaystyle \int \chi _ { W } ( x ) ^ { 2 } + \chi _ { W } ( x + y ) ^ { 2 } - 2 \chi _ { W } ( x ) \chi _ { W } ( x + y ) d x } \\ { \displaystyle } & { = } & { 2 m ( W ) - 2 \int \chi _ { W } ( x ) \chi _ { W } ( x + y ) d x . } \end{array}
$$

By part (a), this quantity goes to 0 as $y  0$ . Thus for all y sufficiently small,

$$
\int \chi _ { W } ( x ) \chi _ { W } ( x + y ) d x ~ > ~ \frac { 1 } { 2 } m ( W ) ~ > ~ 0 .
$$

In particular, there is at least one x such that $\chi _ { W } ( x ) \chi _ { W } ( x + y ) = 1$ , i.e. $x \in W$ and $x + y \in W$ , so $y \in W - W$ Thus $W - W$ contains all sufficiently small $y ,$ as desired.

Problem 6. Let $\mu$ be a finite, positive, regular Borel measure supported on a compact subset of C and define the Newtonian potential

$$
U _ { \mu } ( z ) ~ = ~ \int _ { \mathbb { C } } \left| \frac { 1 } { z - w } \right| \ : d \mu ( w ) .
$$

(a) Prove that $U _ { \mu }$ exists at Lebesgue almost all $z \in \mathbb { C }$ and that

$$
\iint _ { K } U _ { \mu } ( z ) d x d y < \infty
$$

for every compact $K \subseteq \mathbb { C }$

(b) Prove that for almost every horizontal or vertical line $L \subseteq \mathbb { C } , \mu ( L ) = 0$ and $\int _ { K } U _ { \mu } ( z )$ ds ă 8 for every compact subset $K \subseteq L$ , where ds denotes Lebesgue linear measure on L.

(c) Define the Cauchy potential of $\mu$ to be

$$
\int _ { \mathbb { C } } \frac { 1 } { z - w } d \mu ( w ) .
$$

Let R be a rectangle in C whose four sides are contained in lines L having the conclusions of (b). Prove that

$$
\frac { 1 } { 2 \pi i } \int _ { \partial \cal R } S _ { \mu } ( z ) d z \ = \ \mu ( { \cal R } ) .
$$

Solution.
See Spring 2009 $\# 7 .$

Problem 7. Let H be a Hilbert space and let E be a closed convex subset of H. Prove that there exists a unique element $x \in E$ such that

$$
\vert \vert x \vert \vert = \int _ { y \in E } \left. \vert y \vert \right. .
$$

Solution.
See Fall 2012 $\# 3$

Problem 8. Let $F ( z )$ be a non-constant meromorphic function on the complex plane C such that $F ( z + 1 ) =$ $F ( z ) = F ( z + i )$ for all z. Let $Q$ be a square with vertices $z , z + 1 , z + i ,$ and $z + 1 + i$ such that F has no zeros and no poles on $\partial Q$ . Prove that inside $Q$ the function $F$ has the same number of zeros as poles (counting multiplicities).

Solution.

Problem 9. Let

$$
A \ = \ \{ x \in \ell ^ { 2 } : \sum _ { n \geqslant 1 } n | x _ { n } | ^ { 2 } \ \leqslant \ 1 \} .
$$

(a) Show that A is compact in the $\ell ^ { 2 }$ topology.

(b) Show that the mapping from A to R defined by

$$
x \mapsto \int _ { 0 } ^ { 2 \pi } \left| \sum _ { n \geqslant 1 } x _ { n } e ^ { i n \theta } \right| { \frac { d \theta } { 2 \pi } }
$$

achieves its maximum on $A .$

Solution.

Problem 10. Let $\Omega \subseteq \mathbb { C }$ be a connected open set, let $z _ { 0 } \in \Omega .$ , and let U be the set of positive harmonic functions U on Ω such that $U ( z _ { 0 } ) = 1$ . Prove that for every compact set $K \subseteq \Omega$ there is a finite constant M such that

$$
\operatorname* { s u p } _ { U \in \mathcal { U } } \operatorname* { s u p } _ { z \in K } U ( z ) \ \leqslant \ M .
$$

## Solution.

Problem 11. Let $\phi : \mathbb { R }  \mathbb { R }$ be a continuous function with compact support.

(a) Prove there is a constant A such that

$$
\left| \left| f * \phi \right| \right| _ { L ^ { q } } \ \leqslant \ A \left| \left| f \right| \right| _ { L ^ { p } } \quad { \mathrm { ~ f o r ~ a l l ~ } } 1 \leqslant p \leqslant q \leqslant \infty \quad { \mathrm { ~ a n d ~ a l l ~ } } f \in L ^ { p } .
$$

If you use Young’s convolution inequality you should prove it.

(b) Show by example that such a general inequality cannot hold for $p > q$

Solution.
(a) Define α to be the number ě 1 so that $1 / \alpha = 1 / q - 1 / p + 1 \mathrm { ~ ( i f ~ } q \ : = \ : \infty$ and $p = 1$ then $\alpha = \infty )$ . Then $1 / q + 1 = 1 / p + 1 / \alpha$ , so by Young’s convolution inequality we have

$$
\left| \left| f * \phi \right| \right| _ { L ^ { q } } \ \leqslant \ \left| \left| f \right| \right| _ { L ^ { p } } \left| \left| \phi \right| \right| _ { L ^ { \alpha } } \ \leqslant \ \operatorname* { s u p } _ { x \in \mathbb { R } } \left| \phi ( x ) \right| \cdot \left| \left| f \right| \right| _ { L ^ { p } }
$$

as desired.
Now we prove Young’s convolution inequality: the statement is that if $1 / p + 1 / q = 1 / r + 1$ , and $f \in L ^ { p }$ and $g \in L ^ { q }$ , then $| | f * g | | _ { L ^ { r } } \leqslant | | f | | _ { L ^ { p } } | | g | | _ { L ^ { q } }$ . Proof: note that the condition on $p , q , r$ implies that $1 / p , 1 / q \geqslant 1 / r$ . We have

$$
1 ~ = ~ { \frac { 1 } { p } } + { \frac { 1 } { q } } - { \frac { 1 } { r } } ~ = ~ \left( { \frac { 1 } { p } } - { \frac { 1 } { r } } \right) + \left( { \frac { 1 } { q } } - { \frac { 1 } { r } } \right) + { \frac { 1 } { r } } ~ = ~ { \frac { r - p } { p r } } + { \frac { r - q } { q r } } + { \frac { 1 } { r } } .
$$

By H¨older using the three conjugate exponents above, we have

$$
\begin{array} { r l } { \displaystyle  ( f \ast g ) ( x )  \leqslant } & { \displaystyle \int  f ( x - y ) g ( y )  d y } \\ { \displaystyle } & { \leqslant \int  f ( x - y )  ^ { ( r - p ) / r } \displaystyle  g ( y )  ^ { ( r - q ) / r } \displaystyle  f ( x - y ) ^ { p / r } g ( y ) ^ { q / r }  d y } \\ { \displaystyle } & { \leqslant } & { \displaystyle ( \int  f ( x - y )  ^ { p } d y ) ^ { ( r - p ) / p r } ( \displaystyle \int  g ( y )  ^ { q } d y ) ^ { ( r - q ) / p r } ( \displaystyle \int  f ( x - y ) ^ { p } g ( y ) ^ { q }  d y ) ^ { 1 / r } } \\ { \displaystyle } & { = ~ \displaystyle \lVert f  _ { L ^ { p } } ^ { ( r - p ) / r } \displaystyle  | g  _ { L ^ { q } } ^ { ( r - q ) / r } ( \displaystyle \int  f ( x - y ) ^ { p } g ( y ) ^ { q }  d y ) ^ { 1 / r } . } \end{array}
$$

Thus

$$
\begin{array} { r l } { | | f * g | | _ { L ^ { r } } ^ { r } } & { = \displaystyle \int | ( f * g ) ( x ) | ^ { r } d x \leqslant | | f | | _ { L ^ { p } } ^ { r - p } | | g | | _ { L ^ { q } } ^ { r - q } \displaystyle \int \bigg | | f ( x - y ) ^ { p } g ( y ) ^ { q } | d y d x } \\ & { = | | f | | _ { L ^ { p } } ^ { r - p } | | g | | _ { L ^ { q } } ^ { r - q } \displaystyle \int \bigg | f ( x - y ) ^ { p } g ( y ) ^ { q } | d x d y \quad \mathrm { b y ~ T o n e l l i } } \\ & { = | | f | | _ { L ^ { p } } ^ { r } | | g | | _ { L ^ { q } } ^ { r } . \quad \bigtriangleup } \end{array}
$$

(b) Fix $p \ > \ q .$ Let φ be equal to 1 on r0, 1s, have support contained in $[ - 1 , 2 ]$ , and have $0 \leqslant \phi \leqslant 1$ everywhere.
Fix $1 / \alpha \in ( q , p )$ and let $f ( y ) = 1 / y ^ { \alpha }$ for $y \in \left[ 1 0 , \infty \right)$ and 0 otherwise.
Note that $f \in L ^ { p }$ but $f \notin L ^ { q }$ . We have, for all $x > 1 0 0$ 0,

$$
( f * \phi ) ( x ) ~ = ~ \int f ( x - y ) \phi ( y ) d y ~ \geqslant ~ \int _ { 0 } ^ { 1 } f ( x - y ) d y ~ = ~ \int _ { x - 1 } ^ { x } f ( y ) d y ~ = ~ \int _ { x - 1 } ^ { x } { \frac { 1 } { y ^ { \alpha } } } d y ~ \geqslant ~ { \frac { 1 } { x ^ { \alpha } } } .
$$

Thus $f * \phi \notin L ^ { q }$ , so the inequality fails.

Problem 12. Let F be a function from D to D such that whenever $z _ { 1 } , z _ { 2 } , z _ { 3 }$ are distinct points of D there exists an analytic function $f _ { z _ { 1 } , z _ { 2 } , z _ { 3 } }$ from D into D such that $F ( z _ { j } ) = f _ { z _ { 1 } , z _ { 2 } , z _ { 3 } } ( z _ { j } )$ . Prove that F is analytic at every point of D.

## Solution.

Problem 13. Let X and Y be Banach spaces.
A bounded linear transformation $A : X  Y$ is compact if for every bounded sequence $\{ x _ { n } \} \subseteq X$ , the sequence $\left\{ A x _ { n } \right\}$ has a convergent subsequence in Y . Suppose X is reflexive $( X ^ { * * } = X )$ and $X ^ { * }$ is separable.
Show that $A : X  Y$ is compact if and only if for every bounded sequence $\{ x _ { n } \} \subseteq X$ , there exists a subsequence $\{ x _ { n _ { j } } \}$ and a vector $\phi \in X$ such that $x _ { n _ { j } } = \phi + r _ { n _ { \mathrm { . } } }$ nj and $A r _ { n _ { i } }  0$ in Y .

Solution.

## 4 Fall 2010

Problem 1. Consider just Lebesgue measurable functiions $f : [ 0 , 1 ] \to \mathbb { R }$ together with Lebesgue measure.
(a) State Fatou’s lemma,

(b) State and prove the Dominated Convergence Theorem.ş

(c) Give an example where $f _ { n } ( x )  0$ a.e. but $\int f _ { n } ( x ) d x  1$

Solution.
(a) If $f _ { n }$ are non-negative, then $\begin{array} { r } { \left\{ \operatorname* { l i m } \operatorname* { i n f } _ { n \to \infty } f _ { n } \leqslant \operatorname* { l i m } \operatorname* { i n f } _ { n \to \infty } \right\} f _ { n } } \end{array}$

(b) If $f _ { n }  f$ almost everywhere and $\left| f _ { n } \right| \leqslant g$ for some integrable function g and all $f _ { n } .$ , then $\int | f - f _ { n } | \to 0$ Proof: Since $\left| f _ { n } \right| \leqslant g$ and $f _ { n }  f$ almost everywhere, we also have $| f | \leqslant g$ almost everywhere, so the functions $2 g - | f - f _ { n } |$ are non-negative.
Thus we can apply Fatou’s lemma to get

$$
\int \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { 0 } 2 g - | f - f _ { n } | \ \leqslant \ \operatorname* { l i m } _ { n \to \infty } \int ( 2 g - | f - f _ { n } | ) .
$$

The left side simplifies to $\int 2 g$ and the right side simplifies to ş $\left. \int 2 g - \operatorname* { l i m } \operatorname* { s u p } _ { n \to \infty } \right\} | f - f _ { n } |$ Thus by canceling and rearranging we get lim sup $\int | f - f _ { n } | \leqslant 0$ , and since it’s a limsup of non-negative quantities this implies the limit exists and equals 0.

(c) Let $f _ { n } = n \cdot \chi _ { [ 0 , 1 / n ] } . \ f _ { n } \to 0$ almost everywhere but $\textstyle \int f _ { n } = 1$ for all n.

Problem 2. Prove the following form of Jensen’s inequality: if $f : [ 0 , 1 ] \to \mathbb { R }$ is continuous, then

$$
\int _ { 0 } ^ { 1 } e ^ { f ( x ) } d x \ \geqslant \ \exp \left( \int _ { 0 } ^ { 1 } f ( x ) d x \right) .
$$

Moreover, if equality occurs then f is a constant function.

Solution.
Let $u = \int _ { 0 } ^ { 1 } f ( x ) d x$ Let L be the tangent line to the graph of $y \ : = \ : e ^ { x }$ at $x \ = \ u$ Say L has the equation $y = a x + b$ . Since exp is convex, we know that au $+ b = e ^ { u }$ and $a t + b < e ^ { t }$ for all $t \neq u$ . So we have

$$
a u + b ~ = ~ a \int _ { 0 } ^ { 1 } f ( x ) d x + b ~ = ~ \int _ { 0 } ^ { 1 } ( a f ( x ) + b ) d x ~ \leqslant ~ \int _ { 0 } ^ { 1 } e ^ { f ( x ) } d x
$$

by definition of the line $y = a x + b$ Furthermore, if equality holds in the last step, we must have $f ( x ) = u$ for all x. This is because $f$ is continuous, so if $f ( x ) \neq u$ somewhere, then $f \neq u$ on some open interval, and for all x in that interval we would have $a f ( x ) + b < e ^ { f ( x ) }$ , leading to a strict inequality above.
□

Problem 3. Consider the following sequence of functions:

$$
f _ { n } : [ 0 , 1 ] \to \mathbb { R } \quad \mathrm { b y } \quad f _ { n } ( x ) ~ = ~ \exp ( \sin ( 2 \pi n x ) ) .
$$

(a) Prove that $f _ { n }$ converges weakly in $L ^ { 1 } ( [ 0 , 1 ] )$

(b) Prove that $f _ { n }$ converges weak-˚ in $L ^ { \infty } ( [ 0 , 1 ] )$ , viewed as the dual of $L ^ { 1 } ( [ 0 , 1 ] )$

Solution.
(a) This requires showing the existence of some $f \in L ^ { 1 }$ with $\int f _ { n } g \  \ \int f g$ for all $g \in L ^ { \infty }$ Since $L ^ { \infty } ( [ 0 , 1 ] ) \subseteq L ^ { 1 } ( [ 0 , 1 ] )$ , this conclusion is implied by part (b) below.

(b) We need to find some $f \in L ^ { \infty }$ such that $\int f _ { n } g \  \ \int f g$ for all $g ~ \in ~ L ^ { 1 }$ . First note that each $f _ { n }$ is 1{n-periodic, so we have

$$
\int _ { 0 } ^ { 1 } { f _ { n } ( x ) d x } \ = \ \int _ { 0 } ^ { 1 } \exp ( \sin ( 2 \pi n x ) ) d x \ = \ n \int _ { 0 } ^ { 1 / n } \exp ( \sin ( 2 \pi n x ) ) \ = \ \int _ { 0 } ^ { 1 } \exp ( \sin ( 2 \pi u ) ) d u \ = \ \int _ { 0 } ^ { 1 } { f _ { 1 } ( u ) d u } .
$$

Thus the quantity $\int _ { 0 } ^ { 1 } f _ { n } ( x )$ dx is independent of n. By viewing this as the dual pairing with the constant function 1, we see that if the weak limit f exists it must be equal to the constant $C : = \int _ { 0 } ^ { 1 } \exp ( \sin ( 2 \pi u ) ) d u$

So we need to show that $\int _ { 0 } ^ { 1 } f _ { n } g  C \int _ { 0 } ^ { 1 } g$ for any $g \in L ^ { 1 }$ We do this with a standard density argument.
Suppose we knew the desired conclusion for all $\phi$ in some family $\mathcal { F }$ dense in $L ^ { 1 }$ . Then for any $g \in L ^ { 1 }$ , let $\phi _ { k }$ be a sequence in $\mathcal { F }$ converging to $^ { g , }$ then we have

$$
\left| \int f _ { n } g - C \int g { \Big | } \right. \leqslant \ \left| \int f _ { n } g - \int f _ { n } \phi _ { k } \right| + \left| \int f _ { n } \phi _ { k } - \int C \phi _ { k } \right| \ \leqslant \ e \cdot \| g - \phi _ { k } \| _ { L ^ { 1 } } + \left| \int f _ { n } \phi _ { k } - \int C \phi _ { k } \right| _ { L ^ { 1 } } .
$$

because each $f _ { n }$ is bounded uniformly by e. For a fixed $k ,$ take $n \to \infty$ and the second term on the right goes to zero by assumption on the $\phi _ { k }$ . Then take $k \to \infty$ and the first term also goes to zero by construction, so the desired result follows.
Now we just need to prove the desired result for a dense family ${ \mathcal F } .$ . We take $\mathcal { F }$ to be the set of linear combinations of characteristic functions of closed intervals.
Since the desired property is linear, it’s enough to verify for the characteristic function $g \ = \ \chi _ { [ a , b ] }$ We need to show that $\begin{array} { r } { \int _ { a } ^ { b } \exp ( \sin ( 2 \pi n x ) ) d x  C ( b - a ) ~ \mathrm { a s } ~ n  \infty } \end{array}$ . Let $a _ { n }$ be the least number of the form $q / n > a$ and $b _ { n }$ be the greatest number of the form $q / n < b$ . Then we write, using the periodicity,

$$
\begin{array} { r c l } { \displaystyle \int _ { a } ^ { b } \exp ( \sin ( 2 \pi n x ) ) d x } & { = } & { \displaystyle \left( \int _ { a } ^ { a _ { n } } + \int _ { b _ { n } } ^ { b } + \left( \left\lfloor ( b - a ) n \right\rfloor - 2 \right) \int _ { a _ { n } } ^ { a _ { n } + 1 / n } \right) \exp ( \sin ( 2 \pi n x ) ) d x } \\ & & { = } & { \displaystyle e ( a _ { n } - a ) + e ( b - b _ { n } ) + \left( \left\lfloor ( b - a ) n \right\rfloor - 2 \right) \int _ { 0 } ^ { 1 / n } \exp ( \sin ( 2 \pi n x ) ) d x } \\ & & { = \displaystyle e ( a _ { n } - a ) + e ( b - b _ { n } ) + \frac { \left\lfloor ( b - a ) n \right\rfloor - 2 } { n } C } \end{array}
$$

which tends to $( b - a ) C$ as $n \to \infty$ , so we’re done.

Problem 4. Let T be a linear transformation on $C _ { c } ( \mathbb { R } )$ (continuous functions with compact support) that has the following two properties:

$$
\left| \left| T f \right| \right| _ { L ^ { \infty } } \ \leqslant \ \left| \left| f \right| \right| _ { L ^ { \infty } } \quad { \mathrm { a n d } } \quad m \{ x \in \mathbb { R } : \left| T f ( x ) \right| > \lambda \} \ \leqslant \ { \frac { \left| \left| f \right| \right| _ { L ^ { 1 } } } { \lambda } }
$$

where m denotes Lebesgue measure.
Prove that

$$
\int | T f ( x ) | ^ { 2 } d x \ \leqslant \ C \int | f ( x ) | ^ { 2 } d x
$$

for all $f \in C _ { c } ( \mathbb { R } )$ and some fixed number C.

Solution.
We mimic the proof of the Hardy-Littlewood maximal theorem, with a few annoying things changed because $T$ is only defined for $C _ { c }$ functions.
First we will establish the result when f is a real-valued, non-negative function, and extend it at the end.
We use the identity

$$
\int | T f | ^ { 2 } \ = \ 2 \int _ { 0 } ^ { \infty } \lambda \cdot m \{ x : | T f ( x ) | > \lambda \} d \lambda .
$$

For each fixed λ, we have the decomposition $f = g + h$ where $h : = \operatorname* { m i n } ( f , \lambda / 2 )$ and $g : = f - h = 0 { \mathrm { ~ i f ~ } } f < \lambda / 2$ and $f - \lambda / 2 { \mathrm { ~ i f ~ } } f > \lambda / 2$ . Note that both g and h are continuous and non-negative with compact support.
Then we have $T f = T g + T h$ , so $| T f | \leqslant | T g | + | T h |$ , which implies that

$$
\{ x : | T f ( x ) | > \lambda \} \ \subseteq \ \{ x : | T g ( x ) | > \lambda / 2 \} \cup \{ x : | T h ( x ) | > \lambda / 2 \} .
$$

But we have $| | T h | | _ { L ^ { \infty } } \leqslant | | h | | _ { L ^ { \infty } } \leqslant \lambda / 2$ by construction, so the second set has measure zero and we just have (up to measure zero sets)

$$
\{ x : | T f ( x ) | > \lambda \} \ \subseteq \ \{ x : | T g ( x ) | > \lambda / 2 \} .
$$

Thus we have

$$
\begin{array} { r l } { \displaystyle \int | T f | ^ { 2 } \leqslant 2 \int _ { 0 } ^ { \infty } \lambda \cdot m \{ x : | T g ( x ) | > \lambda / 2 \} d \lambda } \\ { \leqslant \displaystyle \int _ { 0 } ^ { \infty } \lambda \frac { 2 \| g \| _ { L ^ { 1 } } } { \lambda } d \lambda \quad \mathrm { b y ~ t h e ~ w e a k \cdot t y p e ~ h y p o t h e s i s } } \\ { \displaystyle \lesssim \int _ { 0 } ^ { \infty } \int _ { \mathbb R } | g ( x ) | d x d \lambda } & { = \displaystyle \int _ { 0 } ^ { \infty } \int _ { \{ x : f ( x ) > \lambda / 2 \} } ( f ( x ) - \lambda / 2 ) d x d \lambda \leqslant \int _ { 0 } ^ { \infty } \int _ { \{ x : f ( x ) > \lambda / 2 \} } f ( x ) d x d \lambda } \\ { = \displaystyle \int _ { \mathbb R } | f ( x ) | \int _ { 0 } ^ { 2 | f ( x ) | } d \lambda d x \quad \mathrm { b y ~ T o n e l i } } \\ { \leqslant \displaystyle \int _ { \mathbb R } | f ( x ) | ^ { 2 } d x . } \end{array}
$$

This establishes the result for positive real-valued f. For general real-valued $f ,$ write $f = f _ { + } - f _ { - }$ . Then we have

$$
\begin{array} { r c l } { { \displaystyle \int | T f | ^ { 2 } } } & { { = } } & { { \displaystyle \int | T f _ { + } - T f _ { - } | ^ { 2 } \ = \ \int | T f _ { + } | ^ { 2 } + | T f _ { - } | ^ { 2 } + | T f _ { + } | | T f _ { - } | } } \\ { { \displaystyle } } & { { \leqslant } } & { { \displaystyle \int | T f _ { + } | ^ { 2 } + \int | T f _ { - } | ^ { 2 } \ \lesssim \ \| f _ { + } \| _ { L ^ { 2 } } ^ { 2 } + \| f _ { - } \| _ { L ^ { 2 } } ^ { 2 } \ = \ \| f | _ { L ^ { 2 } } ^ { 2 } } } \end{array}
$$

where the last equality is valid by the Pythagorean theorem because since $f _ { + } ( x ) f _ { - } ( x ) = 0$ for all $x , \ f _ { + }$ and $f _ { - }$ are orthogonal.
This establishes the result for general real-valued $f .$ . For complex-valued $f ,$ write $f = \operatorname { R e } ( f ) + i \operatorname { I m } ( f )$ , then we have

$$
\int | T f | ^ { 2 } ~ = ~ \int | T \operatorname { R e } ( f ) + i T \operatorname { I m } ( f ) | ^ { 2 } ~ = ~ \int | T \operatorname { R e } ( f ) | ^ { 2 } + | T \operatorname { I m } ( f ) | ^ { 2 } ~ \lesssim \int | \operatorname { R e } ( f ) | ^ { 2 } + | \operatorname { I m } ( f ) | ^ { 2 } ~ = ~ \int | f | ^ { 2 } ,
$$

so we’re done.

Problem 5. Let $\mathbb { R } / \mathbb { Z }$ denote the torus (whose elements we write as cosets) and fix an irrational $\alpha > 0$ (a) Show that

$$
\operatorname* { l i m } _ { N \to \infty } { \frac { 1 } { N } } \sum _ { n = 0 } ^ { N - 1 } f ( n \alpha + \mathbb { Z } ) \ = \ \int _ { 0 } ^ { 1 } f ( x + \mathbb { Z } ) d x
$$

for all continuous functions $f : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$

(b) Show that the conclusion is also true when f is the characteristic function of a closed interval.

Solution.
(a) Define $\begin{array} { r } { A _ { N } ( f ) ~ = ~ \frac { 1 } { N } \sum _ { n = 0 } ^ { N - 1 } f ( n \alpha + \mathbb { Z } ) } \end{array}$ and $I ( f ) = \int _ { 0 } ^ { 1 } f ( x + \mathbb { Z } ) d .$ x. First we show the conclusion when f is a trig polynomial.
By linearity, it’s enough to assume $f ( x ) = e ^ { 2 \pi i k x }$ for some $k \in \mathbb { Z }$ . If $k = 0$ then both sides are clearly equal to 1 so assume $k \neq 0$ . Then we have

$$
\begin{array} { r c l } { { } } & { { } } & { { { \cal A } _ { N } ( f ) ~ = ~ \displaystyle \frac { 1 } { N } \sum _ { n = 0 } ^ { N - 1 } ( e ^ { 2 \pi i k \alpha } ) ^ { n } ~ = ~ \displaystyle \frac { 1 } { N } \frac { 1 - e ^ { 2 \pi i k \alpha N } } { 1 - e ^ { 2 \pi i k \alpha } } ~  ~ 0 ~ \mathrm { a s } ~ N  \infty } } \\ { { } } & { { } } & { { } } \\ { { { \cal I } ( f ) ~ = ~ \displaystyle \int _ { 0 } ^ { 1 } e ^ { 2 \pi i k x } d x ~ = ~ 0 . } } \end{array}
$$

So the result is verified for trig polynomials.
Now for general $f \in C ( \mathbb { R } / \mathbb { Z } )$ , fix $\epsilon > 0$ and let P be a trig polynomial with $| | f - P | | _ { L ^ { \infty } } < \epsilon$ . Then we have

$$
\begin{array} { r } { \begin{array} { l } { | A _ { N } ( f ) - I ( f ) | \ \leqslant \ | A _ { N } ( f ) - A _ { N } ( P ) | + | A _ { N } ( P ) - I ( P ) | + | I ( P ) - I ( f ) | } \\ { \leqslant \ 2 \epsilon + | A _ { N } ( P ) - I ( P ) | . } \end{array} } \end{array}
$$

First take $N  \infty .$ then we see that $\begin{array} { r } { | \mathrm { l i m } _ { N  \infty } A _ { N } ( f ) - I ( f ) | < 2 \epsilon } \end{array}$ , and since this holds for arbitrary , the desired result follows.
□

(b) Let $f = \chi _ { [ a , b ] }$ Let $g _ { k }$ and $h _ { k }$ be sequences of continuous functions satisfying $0 \leqslant g _ { k } \leqslant f \leqslant h _ { k } \leqslant 1$ for all $k ,$ and $g _ { k }$ and $h _ { k }$ both converge almost everywhere to f as $k  \infty \ \mathrm { ( i t ^ { \prime } s }$ clear that such sequences exist by just taking the graph of $f$ and smoothing it out a bit).
Then for each N and k we have

$$
A _ { N } ( g _ { k } ) \ : \leqslant \ : A _ { N } ( f ) \ : \leqslant \ : A _ { N } ( h _ { k } ) , \quad I ( g _ { k } ) \ : \leqslant \ : I ( f ) \ : \leqslant \ : I ( h _ { k } ) .
$$

For k fixed, take $N  \infty$ . Since $g _ { k }$ and $h _ { k }$ are continuous, this implies that

$$
{ \cal I } ( g _ { k } ) \ \leqslant \ \operatorname* { l i m } _ { N \to \infty } \operatorname* { i n f } _ { { \cal A } _ { N } } ( f ) \ \leqslant \ \operatorname* { l i m } _ { N \to \infty } { \cal A } _ { N } ( f ) \ \leqslant \ I ( h _ { k } ) .
$$

Since everything is dominated by 1 and we have pointwise convergence almost everywhere, by the dominated convergence theorem we can take $k \to \infty$ and get

$$
{ \cal I } ( f ) \ \leqslant \ \operatorname* { l i m } _ { N \to \infty } \operatorname { i n f } _ { { \cal A N } } ( f ) \ \leqslant \ \operatorname* { l i m } _ { N \to \infty } { \cal A } _ { N } ( f ) \ \leqslant \ I ( f ) ,
$$

which implies the desired result.

Problem 6. Consider the complex Hilbert space

$$
H : = \left\{ f : \overline { { \mathbb { D } } } \to \mathbb { C } : f ( z ) = \sum _ { k = 0 } ^ { \infty } \widehat { f } ( k ) z ^ { k } \quad \mathrm { w i t h } \quad \lvert | f | | ^ { 2 } : = \sum _ { k = 0 } ^ { \infty } ( 1 + k ^ { 2 } ) \lvert \widehat { f } ( k ) \rvert ^ { 2 } < \infty \right\} .
$$

(a) Prove that the linear function $L : f \mapsto f ( 1 )$ is bounded.

(b) Find the element $g \in H$ representing L.

(c) Show that $f \mapsto \operatorname { R e } L ( f )$ achieves its maximal value on the set

$$
B : = \ \{ f \in H : | | f | | \leqslant 1 \quad { \mathrm { a n d } } \quad f ( 0 ) = 0 \} ,
$$

that this maximum occurs at a unique point, and determine this maximal value.

Solution.
(a) We have

$$
| f ( 1 ) | \leqslant \sum _ { k = 0 } ^ { \infty } | { \widehat { f } } ( k ) | = \sum _ { k = 0 } ^ { \infty } | { \widehat { f } } ( k ) | { \sqrt { 1 + k ^ { 2 } } } { \frac { 1 } { \sqrt { 1 + k ^ { 2 } } } } \leqslant \left( \sum _ { k = 0 } ^ { \infty } | { \widehat { f } } ( k ) | ^ { 2 } ( 1 + k ^ { 2 } ) \right) ^ { 1 / 2 } \left( \sum _ { k = 0 } ^ { \infty } { \frac { 1 } { 1 + k ^ { 2 } } } \right) ^ { 1 / 2 } = C \| f \|
$$

where $\begin{array} { r } { C ^ { 2 } = \sum _ { k = 0 } ^ { \infty } \frac { 1 } { 1 + k ^ { 2 } } < \infty . } \end{array}$

(b) We are implicitly assuming the inner product in H is given by

$$
\langle f , g \rangle = \sum _ { k = 0 } ^ { \infty } \widehat { f } ( k ) \overline { { { \widehat { g } ( k ) } } } ( 1 + k ^ { 2 } ) .
$$

If $g$ represents L then we must have

$$
\langle f , g \rangle ~ = ~ \sum _ { k = 0 } ^ { \infty } \widehat { f } ( k ) \overline { { { \widehat { g } ( k ) } } } ( 1 + k ^ { 2 } ) ~ = ~ f ( 1 ) ~ = ~ \sum _ { k = 0 } ^ { \infty } \widehat { f } ( k ) .
$$

It’s clear that if $\begin{array} { r } { \widehat { g } ( k ) = \frac { 1 } { 1 + k ^ { 2 } } } \end{array}$ then this would be satisfied.
So we can just define

$$
g ( z ) \ = \ \sum _ { k = 0 } ^ { \infty } { \frac { 1 } { 1 + k ^ { 2 } } } z ^ { k } .
$$

The series converges uniformly on $\overline { { \mathbb { D } } }$ so this definition actually makes sense (and in fact is holomorphic, but that’s not necessary).

(c) First we note that the maximum value of $\operatorname { R e } ( L ( f ) )$ on B must happen when $| | f | | \ = \ 1$ , otherwise we could normalize f and increase the value of $\operatorname { R e } ( L ( f ) )$ . The condition that $f ( 0 ) = 0$ corresponds to having ř ${ \widehat { f } } ( 0 ) = 0$ . So the problem is reduced to maximizing ${ \textstyle \sum _ { k = 1 } ^ { \infty } \operatorname { R e } ( \widehat { f } ( k ) ) }$ subject to the condition that $\begin{array} { r } { \sum _ { k = 1 } ^ { \infty } ( 1 + k ^ { 2 } ) | \widehat { f } ( k ) | ^ { 2 } = 1 } \end{array}$ . Note that the constraint only depends on $| { \widehat { f } } ( k ) |$ . Thus we can always increase $\operatorname { R e } ( f ( 1 ) )$ while keeping the norm constant if we assume that each ${ \widehat { f } } ( k )$ is real and positive.
So without loss of generality we can assume each ${ \widehat { f } } ( k ) \geqslant 0$ . Using the same Cauchy-Schwarz argument from part (a), we have

$$
\sum _ { k = 1 } ^ { \infty } \widehat { f } ( k ) \ \leqslant \ \left( \sum _ { k = 1 } ^ { \infty } | \widehat { f } ( k ) | ^ { 2 } ( 1 + k ^ { 2 } ) \right) ^ { 1 / 2 } \left( \sum _ { k = 1 } ^ { \infty } \frac { 1 } { 1 + k ^ { 2 } } \right) ^ { 1 / 2 } \ = \ \left( \sum _ { k = 1 } ^ { \infty } \frac { 1 } { 1 + k ^ { 2 } } \right) ^ { 1 / 2 }
$$

and equality holds if and only if $\textstyle { \widehat { f } } ( k ) { \sqrt { 1 + k ^ { 2 } } } = { \frac { \alpha } { \sqrt { 1 + k ^ { 2 } } } }$ for some $\alpha \in \mathbb { R }$ . This shows that that maximum on B is achieved at a unique point, i.e.

$$
f ( z ) \ = \ \sum _ { k = 1 } ^ { \infty } { \frac { \alpha } { 1 + k ^ { 2 } } } z ^ { k } .
$$

Also, this α is determined by the condition that $f$ has norm 1:

$$
1 ~ = ~ \sum _ { k = 1 } ^ { \infty } ( 1 + k ^ { 2 } ) | { \widehat f } ( k ) | ^ { 2 } ~ = ~ \sum _ { k = 1 } ^ { \infty } { \frac { \alpha ^ { 2 } } { 1 + k ^ { 2 } } } ,
$$

so $\begin{array} { r } { \alpha = \left( \sum _ { k = 1 } ^ { \infty } \frac { 1 } { 1 + k ^ { 2 } } \right) ^ { - 1 / 2 } } \end{array}$ . Thus the maximum value achieved is

$$
\begin{array}{c} \sum _ { k = 1 } ^ { \infty } { \frac { \alpha } { 1 + k ^ { 2 } } } ~ = ~ \left( \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { 1 + k ^ { 2 } } } \right) ^ { 1 / 2 } . ~ \boxed { \begin{array} { r } { { } } \\ { { } \\ { \end{array} } } } \end{array}
$$

Problem 7. Suppopse that $f : \mathbb { C } \to \mathbb { C }$ is continuous and holomorphic on $\mathbb { C } \backslash \mathbb { R }$ . Prove that $f$ is entire.

Solution.
By Morera’s theorem it’s enough to show that the integral around any rectangle with sides parallel to the axes is zero.
Let R be any rectangle.
If R doesn’t intersect the real axis, the integral is obviously zero by hypothesis.
If R does intersect the real axis, break up R into two pieces, one in the upper half plane and one in the lower, and by continuity the integral over R is equal to limit of the integrals as the two pieces approach the real axis, so you still get zero (this is a really standard argument).

Problem 8. Let $A ( \mathbb { D } )$ be the C-vector space of all holomorphic functions on D and suppose that $L :$ $A ( { \mathbb { D } } ) \to \mathbb { C }$ is a multiplicative linear functional.
If L is not identically zero, show that there is a $z _ { 0 } \in \mathbb { D }$ so that $L ( f ) = f ( z _ { 0 } )$ for all $f \in A ( \mathbb { D } )$

Solution.
Note that if this were true, then we would have to have $L ( z ) ~ = ~ z _ { 0 }$ So define $z _ { 0 } : = L ( z )$ and we want to show that $L ( f ) = f ( z _ { 0 } )$ for any $f \in A ( \mathbb { D } )$ . Since we are assuming that L is not identically zero, let f be such that $L ( f ) \neq 0$ . Then because L is multiplicative we can write $L ( f ) = L ( f \cdot 1 ) = L ( f ) L ( 1 )$ q so $L ( 1 ) = 1$ This, combined with the linear and multiplicative hypotheses again, imply that $L ( P ) = P ( z _ { 0 } )$ for any polynomial P . Now let $f$ be any element of ApDq.
We can write $f ( z ) - f ( z _ { 0 } ) = ( z - z _ { 0 } ) g ( z )$ for some other $g \in A ( \mathbb { D } )$ . Therefore we have

$$
L ( f ) - f ( z _ { 0 } ) \ = \ L ( ( z - z _ { 0 } ) g ( z ) ) \ = \ ( L ( z ) - z _ { 0 } ) L ( g ) \ = \ 0 ,
$$

which establishes the desired result.
The only thing left to check is that we actually have $z _ { 0 } \in \mathbb { D }$ . If not, then $1 / ( z - z _ { 0 } )$ would be in ApDq, and so we would have

$$
L ( 1 / ( z - z _ { 0 } ) ) ~ = ~ 1 / L ( z - z _ { 0 } ) ~ = ~ 1 / ( z _ { 0 } - z _ { 0 } ) ,
$$
