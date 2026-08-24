Then integrating both sides from 0 to 1 we get

$$
K ^ { 2 } ~ \geqslant ~ \sum _ { j = 1 } ^ { N } \int _ { 0 } ^ { 1 } | f _ { j } ( x ) | ^ { 2 } d x ~ = ~ \sum _ { j = 1 } ^ { N } | | f _ { j } | | _ { 2 } ^ { 2 } ~ = ~ N .
$$

This shows that a linearly independent set in $\overline { S }$ can have at most $K ^ { 2 }$ elements and thus dim $( \overline { { S } } ) \leqslant K ^ { 2 } < \infty$ □

Problem 12(a). Let $f : [ 0 , 1 ] \to \mathbb { R }$ be a continuous function that is absolutely continuous on each interval r, 1s with $0 < \epsilon \leqslant 1$ . Show that $f$ is not necessarily absolutely continuous on r0, 1s.

Solution. Let $f ( x ) = x \sin ( 1 / x )$ for $x > 0$ and fp0q “ 0. For any $x > 0 .$ , f is differentiable and

$$
f ^ { \prime } ( x ) \ = \ \sin ( 1 / x ) - { \frac { c o s ( 1 / x ) } { x } } .
$$

So for a fixed $\epsilon > 0$ and any $x \in [ \epsilon , 1 ]$ , we have

$$
| f ^ { \prime } ( x ) | ~ \leqslant ~ | s i n ( 1 / x ) | + \left| \frac { \cos ( 1 / x ) } { x } \right| ~ \leqslant ~ 1 + \frac { 1 } { \epsilon } .
$$

Thus $f ^ { \prime }$ is bounded on r, 1s, so f is Lipschitz and thus f is absolutely continuous on r, 1s.

Let $x _ { n } = 1 / 2 \pi n$ and $y _ { n } = 1 / ( \pi + 2 \pi n )$ . Note that we have

$$
\begin{array} { r c l } { { | x _ { n } - y _ { n } | } } & { { = } } & { { \displaystyle \left| \frac { \pi } { 4 \pi ^ { 2 } n ^ { 2 } + 2 \pi ^ { 2 } n } \right| < \frac { 1 } { n ^ { 2 } } } } \\ { { | f ( x _ { n } ) - f ( y _ { n } ) | } } & { { = } } & { { | x _ { n } + y _ { n } | ~ = ~ \displaystyle \left| \frac { \pi + 4 \pi n } { 4 \pi ^ { 2 } n ^ { 2 } + 2 \pi ^ { 2 } n } \right| . } } \end{array}
$$

In particular, $\textstyle \sum _ { n = 1 } ^ { \infty } | x _ { n } - y _ { n } | < \infty$ and $\textstyle \sum _ { n = 1 } ^ { \infty } | f ( x _ { n } ) - f ( y _ { n } ) | = \infty$ Suppose that f were absolutely con-ř tinuous on r0, 1s. Then pick  “ 1 and let δ be such that for any ř $\begin{array} { r } { N , M , \sum _ { n = N } ^ { M } | x _ { n } - y _ { n } | < \delta } \end{array}$ implies $\begin{array} { r } { \sum _ { n = N } ^ { M } | f ( x _ { n } ) - f ( y _ { n } ) | < 1 } \end{array}$ . But by the convergence and divergence of the above series, we can pick an N such that $\begin{array} { r } { \sum _ { n = N } ^ { \infty } \left| x _ { n } - y _ { n } \right| < \delta } \end{array}$ and then we can pick an M such that $\begin{array} { r } { \sum _ { n = N } ^ { M } | f ( x _ { n } ) - f ( y _ { n } ) | > 1 } \end{array}$ , which is a contradiction. Thus f is not absolutely continuous on r0, 1s.

Problem 12(b). Show that if f is of bounded variation on r0, 1s, then f is absolutely continuous on r0, 1s.

Solution. Let $T V _ { [ a , b ] }$ denote the total variation of f on the interval ra, bs. Since f is continuous and of bounded variation on r0, 1s, we can show that $T V _ { [ 0 , x ] }$ is a continuous function of x. Fix $\epsilon > 0$ . Since $f$ is of bounded variation, pick a partition $\{ 0 = t _ { 0 } < t _ { 1 } < \cdots < t _ { n } = 1 \}$ such that

$$
\sum _ { j = 1 } ^ { n } | f ( t _ { j } ) - f ( t _ { j - 1 } ) | ~ > ~ T V _ { [ 0 , 1 ] } - \epsilon .
$$

Since f is continuous, we can pick an $h \in ( 0 , t _ { 1 } )$ such that $| f ( h ) - f ( 0 ) | < \epsilon$ . By adding h into the original partition, the variation can only increase. Furthermore, $\{ h , t _ { 1 } , \ldots , t _ { n } \}$ is a partition of $[ h , 1 ]$ , so we get

$$
\epsilon + T V _ { [ h , 1 ] } ~ > ~ | f ( h ) - f ( 0 ) | + | f ( t _ { 1 } ) - f ( h ) | + \sum _ { j = 2 } ^ { n } | f ( t _ { j } ) - f ( t _ { j - 1 } ) | ~ > ~ T V _ { [ 0 , 1 ] } - \epsilon ,
$$

which implies $T V _ { [ 0 , h ] } = T V _ { [ 0 , 1 ] } - T V _ { [ h , 1 ] } < 2 \epsilon$ . Since $T V [ 0 , x ]$ is an increasing function, this shows that it is continuous at 0.

Now we want to show that f is absolutely continuous on r0, 1s. Fix $\epsilon > 0$ and let $h > 0$ be such that $T V _ { [ 0 , h ] } < \epsilon$ By hypothesis, f is absolutely continuous on $[ h , 1 ]$ , so let $\delta > 0$ be as in the definition of absolute continuity on rh, 1s. Let $a _ { 1 } < b _ { 1 } \leqslant a _ { 2 } < \cdot \cdot \cdot \leqslant a _ { n } < b _ { n }$ be such that $\begin{array} { r } { \sum _ { k = 1 } ^ { n } b _ { k } - a _ { k } < \delta } \end{array}$ . By dividing one of the intervals into two subintervals, the variation can only increase, so without loss of generality we may assume that $h \not \in \left( a _ { k } , b _ { k } \right)$ for any k. Let \` be the index such that $b _ { \ell } \leqslant h \leqslant a _ { \ell + 1 }$ . Since $\{ a _ { 1 } , b _ { 1 } , \ldots , a _ { \ell } , b _ { \ell } \}$ is a partition of r0, hs, by the choice of h we have

$$
\sum _ { j = 1 } ^ { \ell } | f ( b _ { j } ) - f ( a _ { j } ) | \ \leqslant \ T V _ { [ 0 , h ] } \ < \ \epsilon .
$$

By absolute continuity on rh, 1s, we have

$$
\sum _ { j = \ell + 1 } ^ { n } | f ( b _ { j } ) - f ( a _ { j } ) | ~ < ~ \epsilon
$$

and hence

$$
\sum _ { j = 1 } ^ { n } | f ( b _ { j } ) - f ( a _ { j } ) | ~ < ~ 2 \epsilon ,
$$

which establishes that f is absolutely continuous on r0, 1s.

## 11 Spring 2014

Problem 1. Let $( X , A , \mu )$ be a σ-finite measure space. For each $t ~ \in ~ \mathbb { R }$ let $e _ { t }$ be the characteristic function of the interval $( t , \infty )$ . Prove that if $f , g \ : \ X \ \to \ \mathbb { R }$ are A-measurable, then $| | f - g | | _ { L ^ { 1 } ( X ) } =$ $\int _ { \mathbb { R } } | | e _ { t } \circ f - e _ { t } \circ g | | _ { L ^ { 1 } ( X ) } \ d t$

Solution. We have

$$
\begin{array} { r } { \displaystyle \int _ { \mathbb R } | | e _ { t } \circ f - e _ { t } \circ g | | _ { L ^ { 1 } } d t = \int _ { \mathbb R } ( \int _ { \mathbb R } | e _ { t } \circ f ( x ) - e _ { t } \circ g ( x ) | d x ) d t } \\ { = \displaystyle \int _ { \mathbb R } ( \int _ { \mathbb R } | e _ { t } \circ f ( x ) - e _ { t } \circ g ( x ) | d t ) d x , } \end{array}
$$

where we are justified in switching the order of integration by Tonelli’s theorem since µ is σ-finite. Now observe that $| e _ { t } \circ f ( x ) - e _ { t } \circ g ( x ) |$ is equal to 1 if either $f ( x ) < t \leqslant g ( x )$ or $g ( x ) < t \leqslant f ( x )$ and 0 otherwise. Thus the inner integral evaluates to $| f ( x ) - g ( x ) |$ , which gives the desired result.

Problem 2. Let $f \in L ^ { 1 } ( \mathbb { R } , d x )$ and $\beta \in ( 0 , 1 )$ . Prove that

$$
\int _ { \mathbb { R } } { \frac { | f ( x ) | } { | x - a | ^ { \beta } } } d x < \infty
$$

for (Lebesgue) a.e. $a \in \mathbb { R } .$

Solution. Write $\begin{array} { r } { F ( a ) \ = \ \int _ { \mathbb { R } } { \frac { | f ( x ) | } { | x - a | ^ { \beta } } } d x } \end{array}$ . We would be done if we could show that $\int _ { \mathbb { R } } F ( a ) d a < \infty$ . Unfortunately this isn’t true. However it is enough to show that $\int _ { \mathbb { R } } u ( a ) F ( a ) d a < \infty$ for some strictly positive u.

We take $u ( a ) = \operatorname* { m i n } ( a ^ { - 2 } , 1 )$ , with the convention that $u ( 0 ) = 1 . \mathrm { B y }$ Tonelli’s theorem, we write

$$
\begin{array} { r l } { \displaystyle \int _ { \mathbb R } u ( a ) F ( a ) d a = \int _ { \mathbb R } u ( a ) \left( \int _ { \mathbb R } \frac { | f ( x ) | } { | x - a | ^ { \beta } } d x \right) d a } & { } \\ { \displaystyle \qquad } & { = \int _ { \mathbb R } | f ( x ) | \left( \int _ { \mathbb R } \frac { u ( a ) } { | a - x | ^ { \beta } } d a \right) d x . } \end{array}
$$

Let I be the interval $[ x - 1 , x + 1 ]$ . We bound the inner integral as follows:

$$
\begin{array} { l } { \displaystyle \int _ { \mathbb R } \frac { u ( a ) } { | a - x | ^ { \beta } } d a = \int _ { I } \frac { u ( a ) } { | a - x | ^ { \beta } } d a + \int _ { \mathbb R \backslash I } \frac { u ( a ) } { | a - x | ^ { \beta } } d a } \\ { \displaystyle \qquad \leqslant \int _ { I } \frac { 1 } { | a - x | ^ { \beta } } d a + \int _ { \mathbb R \backslash I } u ( a ) d a } \\ { \displaystyle \qquad \leqslant \int _ { I } \frac { 1 } { | a - x | ^ { \beta } } d a + \int _ { \mathbb R } u ( a ) d a } \\ { \displaystyle \qquad = \int _ { [ - 1 , 1 ] } \frac { 1 } { | a | ^ { \beta } } d a + \int _ { \mathbb R } u ( a ) d a , } \end{array}
$$

where we applied a linear change of variables in the last step. But $\beta \in ( 0 , 1 )$ so the first integral is finite, and it’s clear the second integral integral is finite. So there is a constant C, independent of x such thatş $\int _ { \mathbb { R } } { \frac { u ( a ) } { | a - x | ^ { \beta } } } < C$ . Returning to the original integral, we have

$$
\int _ { \mathbb { R } } u ( a ) F ( a ) d a \leqslant \int _ { \mathbb { R } } C | f ( x ) | d x = C \left| | f | \right| _ { L ^ { 1 } } ,
$$

which is finite by hypothesis. It follows that $F ( a ) < \infty$ for a.e. $a \in \mathbb { R } . \quad \sqcup$

Problem 3.1. Let $[ a , b ]$ be a finite interval and let $f : [ a , b ]  \mathbb { R }$ be a bounded Borel measurable function.   
Prove that $\{ x \in [ a , \bar { b } ] : \bar { f }$ is continuous at xu is Borel measurable.

Solution. Let

$E _ { n } ~ : = ~ \{ x \in [ a , b ]$ : there exists a $\delta > 0$ such that $| f ( a ) - f ( b ) | < 1 / n$ for any $a , b \in ( x - \delta , x + \delta ) \}$

Note that f is continuous at x if and only if $x \in \bigcap _ { n = 1 } ^ { \infty } E _ { n }$ . So to show the set of continuities of f is Borel it suffices to show that each $E _ { n }$ is an open set. Let x $\in ~ E _ { n }$ and let δ be as in the definition of $E _ { n }$ . We show that $( x - \delta / 2 , x + \delta / 2 ) \subseteq E _ { n }$ . Indeed, $\mathrm { i f ~ } | y - x | < \delta / 2$ , then for any $a , b \in ( y - \delta / 2 , y + \delta / 2 )$ we have $| a - x | , | b - x | < \delta ,$ so $| f ( a ) - f ( b ) | < 1 / n$ . Thus $y \in E _ { n }$ with the choice $\delta / 2 ,$ so $E _ { n }$ is open.

Problem 3.2. Prove that f is Riemann integrable if and only if it is continuous almost everywhere.

Solution. Let $\overline { I }$ be the upper Riemann integral of f and I be the lower Riemann integral of $f .$ We know that we can find a sequence of nested partitions $P _ { 1 } \subseteq P _ { 2 } \subseteq . . . \mathrm { o f } \ [ a , b ]$ such that the mesh size of $P _ { n }$ tends to 0 as $n  \infty$ and $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } U ( f , P _ { n } ) = \overline { { I } } } \end{array}$ and lim $\operatorname { l } _ { n \to \infty } { \cal L } ( f , P _ { n } ) = \underline { { { I } } } .$ Denote by $E _ { k , n }$ the kth subinterval of the partition $P _ { n }$ and let $m _ { k , n }$ and $M _ { k , n }$ be the infimum and supremum respectively of $f$ on $E _ { k , n }$ . Define the functions $U _ { n }$ and $L _ { n }$ by

$$
\begin{array} { r c l } { { } } & { { } } & { { L _ { n } ~ : = ~ \displaystyle \sum _ { k } m _ { k , n } \chi _ { E _ { k , n } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { U _ { n } ~ : = ~ \displaystyle \sum _ { k } M _ { k , n } \chi _ { E _ { k , n } } . } } \end{array}
$$

By construction we have $\int _ { a } ^ { b } U _ { n } = U ( f , P _ { n } )$ and $\int _ { a } ^ { b } { \cal L } _ { n } = { \cal L } ( f , P _ { n } )$ . Also, since the partitions are nested, we have

$$
L _ { 1 } \ \leqslant \ L _ { 2 } \ \leqslant \ . . . \ \leqslant \ f \ \leqslant \ . . . \ \leqslant \ U _ { 2 } \ \leqslant \ U _ { 1 } .
$$

Since $\left\{ U _ { n } \right\}$ and $\left\{ L _ { n } \right\}$ are both monotone, they converge pointwise to functions U and L respectively such that $L \leqslant f \leqslant U$ . By applying the Dominated Convergence Theorem to both ş ş $L _ { n }$ and $U _ { n }$ with $U _ { 1 }$ as the dominating function, we see that $\int _ { a } ^ { b } L = \underline { { { I } } }$ and $\int _ { a } ^ { b } U = { \overline { { I } } }$ . Now we have that f is Riemann intergrable if and only if ${ \overline { { I } } } \ = \ { \underline { { I } } } .$ , which happens if and only if $\int _ { a } ^ { b } L = \int _ { a } ^ { b } U$ , which since $L \leqslant U$ happens if and only if $L = U$ almost everywhere, and since $L \leqslant f \leqslant U$ this happens if and only if $L ( x ) = f ( x ) = U ( x )$ almost everywhere. Note that the set of x which appear as a partition point of some $P _ { n }$ is at most countable, and thus has measure zero and can be ignored. For other $x ,$ the statement that $L ( x ) = f ( x ) = U ( x )$ is exactly the statement that $f$ is continuous at x (because the mesh size of the partition tends to 0). Thus we conclude that f is Riemann integrable if and only if f is continuous almost everywhere. □

Problem 4a. Consider a sequence $\{ a _ { n } \} \subseteq [ 0 , 1 ]$ . For $f \in C ( [ 0 , 1 ] )$ , let us denote

$$
\phi ( f ) \ = \ \sum _ { n = 1 } ^ { \infty } 2 ^ { - n } f ( a _ { n } ) .
$$

Prove that there is no $g \in L ^ { 1 } ( [ 0 , 1 ] )$ such that $\phi ( f ) = \int f ( x ) g ( x )$ dx is true for all $f \in C ( [ 0 , 1 ] )$

Solution. Suppose there was such a $g .$ Let $f _ { k }$ be the function which is zero outside $[ a _ { 1 } - 1 / k , a _ { 1 } + 1 / k ]$ equal to 1 at $a _ { 1 } .$ , and linear in between (the graph is a triangle of height 1 and width $2 / k$ centered at $a _ { 1 } )$ Then for each k we have $\phi ( f _ { k } ) \geqslant 1 / 2$ . But we also have $f _ { k }  0$ pointwise almost everywhere and $| f _ { k } | \leqslant 1$ so by the dominated convergence theorem, $\int _ { 0 } ^ { 1 } f _ { k } g \to 0$ , which is a contradiction. □

Problem 4b. Each $g \in L ^ { 1 } ( [ 0 , 1 ] )$ defines a continuous functional $T _ { g }$ on $L ^ { \infty } ( [ 0 , 1 ] )$ by

$$
T _ { g } ( f ) \ = \ \int f ( x ) g ( x ) d x .
$$

Prove that there are continuous functionals on $L ^ { \infty } ( [ 0 , 1 ] )$ that are not of this form.

Solution. Suppose not, i.e. that every element of $( L ^ { \infty } ) ^ { * }$ is of the form $T _ { g }$ for some $g \in L ^ { 1 }$ Then the map $g \mapsto T _ { g }$ is a normed vector space isomorphism ${ \cal L } ^ { 1 } \stackrel { . } {  } ( { \cal L } ^ { \infty } ) ^ { * }$ . Indeed, it is surjective by assumption, injective because $T _ { g } = 0$ implies $\int _ { 0 } ^ { 1 } f g = 0$ for all $f \in C ( [ 0 , 1 ] )$ , which implies $g = 0$ , and bounded because

$$
\big | | T _ { g } | | _ { o p } \ = \ \operatorname* { s u p } _ { | | f | | _ { L ^ { \infty } } = 1 } \left| \int _ { 0 } ^ { 1 } f g \right| \ \leqslant \ \left| \int _ { 0 } ^ { 1 } g \right| \ \leqslant \ | | g | | _ { L ^ { 1 } } .
$$

Thus by the open mapping theorem, it’s inverse is also bounded and therefore it’s an isomorphism. Thus $L ^ { 1 } \simeq ( \dot { L } ^ { \infty } ) ^ { * }$ . Since $L ^ { 1 }$ is separable, this implies $( L ^ { \infty } ) ^ { * }$ is separable, which implies $L ^ { \infty }$ is separable. But this is a contradiction: $\{ \chi _ { [ 0 , r ] } \} _ { 0 < r < 1 }$ is an uncountable discrete set in $L ^ { \infty } . \sqsupset$

Alternate Solution (using part a). Note that $\phi$ is a bounded linear functional on the space $C ( [ 0 , 1 ] )$ , so by Hahn-Banach $\phi$ extends to a bounded linear functional $\widetilde { \phi }$ on $L ^ { \infty } ( [ 0 , 1 ] )$ q. If $\widetilde { \phi }$ was of the form $T _ { g }$ then its restriction $\phi$ would also be of this form, which contradicts part (a).

Problem 5a. Prove that $\ell ^ { 1 } ( \mathbb { N } )$ and $\ell ^ { 2 } ( \mathbb { N } )$ are separable Banach spaces but $\ell ^ { \infty } ( \mathbb { N } )$ is not.

Solution. Let X be either $\ell ^ { 1 } ( \mathbb { N } )$ or $\ell ^ { 2 } ( \mathbb { N } )$ (the proof that follows works for both). Define the set

$$
S _ { n } \ : = \ \left\{ f \in X : f ( k ) \in \mathbb { Q } + i \mathbb { Q } { \mathrm { ~ f o r ~ a l l ~ } } k { \mathrm { ~ a n d ~ } } f ( k ) = 0 { \mathrm { ~ f o r ~ } } k > n \right\}
$$

and let $\textstyle S = \bigcup _ { n = 1 } ^ { \infty } S _ { n }$ Note that each $S _ { n }$ can be identified with $( \mathbb { Q } + i \mathbb { Q } ) ^ { n }$ , which is countable, so $S$ is countable as well. We now show that S is dense in X. Let ř $f \in X$ and fix $\epsilon > 0$ Let e be either 1 or 2ř depending on if X is $\ell ^ { 1 } ( \mathbb { N } )$ or $\ell ^ { 2 } ( \mathbb { N } )$ . Since $\begin{array} { r } { \sum _ { k = 1 } ^ { \infty } | f ( k ) | ^ { e } < \infty } \end{array}$ , there is an N such that $\begin{array} { r } { \sum _ { k = N + 1 } ^ { \infty } | f ( k ) | ^ { e } < \epsilon . } \end{array}$ For each $k \leqslant N$ , since $\mathbb { Q } + i \mathbb { Q }$ is dense in $\mathbb { C } ,$ pick $q _ { k } \in \mathbb { Q } + i \mathbb { Q }$ such that $| q _ { k } - f ( k ) | < ( \epsilon / N ) ^ { 1 / e }$ . Now define g by $g ( k ) = q _ { k }$ for $k \leqslant N$ and $g ( k ) = 0$ for $k > N$ . Then we see that $g \in S _ { N } \subseteq S$ and

$$
\| f - g \| _ { X } \ = \ \sum _ { k = 1 } ^ { \infty } | f ( k ) - g ( k ) | ^ { e } \ = \ \sum _ { k = 1 } ^ { N } | f ( k ) - q _ { k } | ^ { e } + \sum _ { k = N + 1 } ^ { \infty } | f ( k ) | ^ { e } \ < \ \epsilon + \epsilon \ = \ 2 \epsilon .
$$

Thus S is dense in $X ,$ so X is separable.

For $\ell ^ { \infty } ( \mathbb { N } )$ , for any subset $A \subseteq \mathbb { N } .$ define $f _ { A } \in \ell ^ { \infty } ( \mathbb { N } )$ by $f _ { A } ( k ) ~ = ~ 1 ~ \mathrm { i f } ~ k ~ \in ~ A$ and 0 otherwise. Note that for any two subsets A and B, if $A \neq B$ then $\| f _ { A } - f _ { B } \| _ { \ell ^ { \infty } } = 1$ . But since there are uncountably many subsets of N, the collection $\{ f _ { A } \} _ { A \subseteq \mathbb { N } }$ is an uncountable discrete subset of $\ell ^ { \infty } ( \mathbb { N } )$ , which means $\ell ^ { \infty } ( \mathbb { N } )$ can’t be separable.

Problem 5b. Prove that there exists no bounded linear surjective map $T : \ell ^ { 2 } ( \mathbb { N } ) \to \ell ^ { 1 } ( \mathbb { N } )$

Solution. If such a map existed then it would induce a bounded injective map $T ^ { * } : l ^ { \infty } ( \mathbb { N } ) \to l ^ { 2 } ( \mathbb { N } )$ between the dual spaces. Taking duals again, we obtain a surjective bounded linear map $T ^ { * * } : l ^ { 2 } ( \mathbb { N } ) \to ( l ^ { \infty } ( \mathbb { N } ) ) ^ { * }$ But the image of a separable space under a bounded linear map is separable, so $( l ^ { \infty } ( \mathbb { N } ) ) ^ { * }$ must be separable. But then $l ^ { \infty } ( \mathbb { N } )$ is separable, which is a contradiction.

Problem 6a. Given a Hilbert space $\mathcal { H } ,$ let $\left\{ a _ { n } \right\}$ be a sequence with $\left| \left| a _ { n } \right| \right| = 1$ for all n. Recall that the closed convex hull of $\left\{ a _ { n } \right\}$ is the closure of the set of all convex combinations of elements in $\left\{ a _ { n } \right\}$ . Show that if $\left\{ a _ { n } \right\}$ spans H linearly, then H is finite dimensional.

Solution. Suppose $\left\{ a _ { n } \right\}$ linearly spans H and suppose that H is infinite-dimensional. By inductively removing any elements $a _ { n }$ which are in the span of $\left\{ a _ { 1 } , \ldots , a _ { n - 1 } \right\}$ , we may assume that $\left\{ a _ { n } \right\}$ is a linearly independent set in H. Define $S _ { N } : = \operatorname { s p a n } ( a _ { 1 } , \dots , a _ { N } )$ . We know that $S _ { N }$ is a finite-dimensional subspace of H and is therefore closed. We also know that $S _ { N }$ does not contain any open sets because if $S _ { N }$ contained the open ball $B ( x , r )$ , then since S is a subspace it would also contain the set $B ( x , r ) - x = B ( 0 , r )$ , and then it would also have to contain the set $n \cdot B ( 0 , r ) = B ( 0 , n r )$ for all integers $n ,$ implying that $S _ { N }$ would be equal to all of H. But since H is infinite dimensional this is not the case. Hence $S _ { N }$ has empty interior and sinceŤ $S _ { N }$ is closed, $S _ { N }$ is nowhere dense. By the assumption that $\left\{ a _ { n } \right\}$ spans $\mathcal { H } .$ we see that $\begin{array} { r } { \mathcal { \dot { H } } = \bigcup _ { N = 1 } ^ { \infty } S _ { N } } \end{array}$ . But this is a countable union of nowhere dense sets, and since Hilbert spaces are complete, this contradicts the Baire category theorem. Thus $\mathcal { H }$ must be finite dimensional. □

Problem 6b. Show that if $\langle a _ { n } , \xi \rangle \to 0$ for all $\xi \in \mathcal H$ , then 0 is in the closed convex hull of $\left\{ a _ { n } \right\}$

Solution. Fix $\epsilon > 0$ It suffices to show the existence of a convex combination of the $a _ { n }$ with norm less than . Set $a _ { N _ { 1 } } ~ = ~ a _ { 1 }$ Since $\langle a _ { n } , a _ { N _ { 1 } } \rangle  0$ as $n  \infty$ 8, pick $a _ { N _ { 2 } }$ so that $| \langle a _ { N _ { 2 } } , a _ { N _ { 1 } } \rangle | < \epsilon .$ . Now since $\left. { a _ { n } , a _ { N _ { 1 } } } \right.$ and $\left. { a _ { n } , a _ { N _ { 2 } } } \right.$ both tend to 0 as $n  \infty$ , we can pick $a _ { N _ { 3 } }$ so that $\left| \left. a _ { N _ { 3 } } , a _ { N _ { 1 } } \right. \right| , \left| \left. a _ { N _ { 3 } } , a _ { N _ { 2 } } \right. \right| < \epsilon .$ Continuing this construction inductively we get a subsequence $a _ { N _ { k } }$ with the property that every pairwise inner product in the subsequence has absolute value less than . Now let $r$ be big enough so that $1 / r < \epsilon$ and consider the convex combination $( 1 / r ) a _ { N _ { 1 } } + . . . + ( 1 / r ) a _ { N _ { r } }$ . We have

$$
\begin{array} { r c l } { \displaystyle \left\| \frac { 1 } { r } a _ { N _ { 1 } } + \ldots + \frac { 1 } { r } a _ { N _ { r } } \right\| ^ { 2 } } & { = } & { \displaystyle \frac { 1 } { r ^ { 2 } } \left. a _ { N _ { 1 } } + \ldots a _ { N _ { r } } , a _ { N _ { 1 } } + \ldots a _ { N _ { r } } \right. } \\ & { = } & { \displaystyle \frac { 1 } { r ^ { 2 } } \left( \sum _ { j = 1 } ^ { r } \left\| a _ { N _ { j } } \right\| ^ { 2 } + \sum _ { i \neq j } \left. a _ { N _ { i } } , a _ { N _ { j } } \right. \right) ~ < ~ \frac { 1 } { r ^ { 2 } } \left( r + r ^ { 2 } \epsilon \right) ~ < ~ \frac { 3 } { 2 } \epsilon . ~ \Omega } \end{array}
$$

Problem 7. Characterize all entire functions f with $| f ( z ) | > 0$ for z large and

$$
\operatorname* { l i m } _ { z \to \infty } \operatorname* { s u p } _ { | z | } \frac { | \log | f ( z ) | | } { < \infty . }
$$

Solution. The condition that $| f ( z ) | > 0$ for $| z |$ large implies that all of the zeros of f lie in some bounded set, and since the zeros have to be discrete, f has only finitely many zeros. Let $p ( z )$ be the polynomial with the same zeros as $f ,$ counting multiplicity. Then $f ( z ) / p ( z )$ is a nonvanishing entire function, so we can write $f ( z ) / p ( z ) = e ^ { h ( z ) }$ for some entire function h. So we have the representation $f ( z ) = p ( z ) e ^ { h ( z ) }$ where $p$ is a polynomial and h is entire. We have

$$
\operatorname* { l i m s u p } _ { z \to \infty } \frac { | \log | f ( z ) | | } { | z | } \ = \ \operatorname* { l i m s u p } _ { z \to \infty } \frac { | \log | p ( z ) | | } { | z | } + \frac { | \log | \operatorname { R e } ( h ( z ) ) | | } { | z | } \ = \ \operatorname* { l i m s u p } _ { z \to \infty } \frac { | \log | \operatorname { R e } ( h ( z ) ) | | } { | z | } \ < \ \infty .
$$

Thus we have $| \operatorname { R e } ( h ( z ) ) | \leqslant C | z |$ for some constant C and all z. We claim this implies that h is a degree 1 polynomial. It would be obvious if the bound had $| h ( z ) |$ instead of $| \operatorname { R e } ( h ( z ) ) |$ , but it doesn’t, so we have to do more work. Write $h = u + i v$ and also write

$$
h ( z ) = h ( r e ^ { i \theta } ) = \sum _ { n = 0 } ^ { \infty } a _ { n } r ^ { n } e ^ { i n \theta } .
$$

Then we have $\begin{array} { r } { u ( r e ^ { i \theta } ) = \sum _ { n = 0 } ^ { \infty } r ^ { n } ( \operatorname { R e } ( a _ { n } ) \cos ( n \theta ) - \operatorname { I m } ( a _ { n } ) \sin ( n \theta ) ) } \end{array}$ . Using various orthonormality properties and the fact the the power series converges uniformly on compact sets, one can compute

$$
\int _ { 0 } ^ { 2 \pi } u ( r e ^ { i \theta } ) e ^ { - i k \theta } d \theta \ = \ \pi r ^ { k } a _ { k }
$$

for each fixed k. Thus

$$
| a _ { k } | r ^ { k } \leqslant \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } | u ( r e ^ { i \theta } ) | d \theta .
$$

Combining this with the mean value property for u, we have

$$
| a _ { k } | r ^ { k } + 2 u ( 0 ) \ \leqslant \ \frac { 1 } { \pi } \int _ { 0 } ^ { 2 \pi } ( | u ( r e ^ { i \theta } ) | + u ( r e ^ { i \theta } ) ) d \theta \ \leqslant \ \frac { 1 } { \pi } \cdot 2 \pi \cdot 2 C r \ = \ 4 C r
$$

by the estimate on $| \mathrm { R e } ( h ) |$ from above. Thus we have $\left| a _ { k } \right| \leqslant 4 C r ^ { 1 - k } - 2 u ( 0 ) r ^ { - k }$ . This holds for any r, so we can take $r \to \infty$ to conclude that $a _ { k } = 0$ for any $k > 1$ . This implies that h is a degree 1 polynomial.

So we conclude that if $f$ satisfies the given conditions, then $f ( z ) = p ( z ) e ^ { a z + b }$ for some polynomial p and $a , b \in \mathbb { C }$ . It’s clear that every function of this form satisfies the conditions, so this is a complete characterization. □

Problem 8. Construct a non-constant entire function $f ( z )$ such that the zeros of $f$ are simple and coincide with the set of all (positive) natural numbers.

Solution. Use the canonical product representation. Let

$$
f ( z ) \ = \ \prod _ { n = 1 } ^ { \infty } \left( 1 - { \frac { z } { n } } \right) e ^ { z / n } .
$$

This clearly has the right zeros. We just need to show $f$ is entire. It’s enough to show that the product converges uniformly and absolutely on compact sets. Equivalently, we need to show that

$$
\sum _ { n = 1 } ^ { \infty } | \log ( 1 - z / n ) + z / n |
$$

converges uniformly on compact sets. Examining the power series expansion of $\log ( 1 - x )$ around 0, we see that there exists $\delta > 0$ such that $| x | < \delta$ implies $| \log ( 1 - x ) + x | \leqslant | x | ^ { 2 }$ . Fix a compact set $\overline { { B ( 0 , R ) } }$ . Pick n big enough so that $R / n < \delta$ and also so that $n > R$ . Then for any $| z | \leqslant R$ , we have $| z | / n < \delta ,$ so

$$
| \log ( 1 - z / n ) + z / n | \ \leqslant \ { \frac { | z | ^ { 2 } } { n ^ { 2 } } } \ \leqslant \ { \frac { R ^ { 2 } } { n ^ { 2 } } } .
$$

Thus the series in question is eventually majorized by the convergent series $\textstyle \sum _ { n = 1 } ^ { \infty } R ^ { 2 } / n ^ { 2 }$ for all $| z | \leqslant R ,$ which shows that it converges uniformly and absolutely on $B ( 0 , R )$ □

Problem 9. Prove Hurwitz’ Theorem: Let $\Omega \subseteq \mathbb { C }$ be a connected open set and $f _ { n } , f : \Omega \to \mathbb { C }$ holomorphic functions. Assume that $f _ { n } ( z )$ converges uniformly to $f ( z )$ on compact subsets of Ω. Prove that if $f _ { n } ( z ) \neq 0$ for all $z \in \Omega$ and all $n ,$ then either $f$ is identically zero or $f ( z ) \neq 0$ for all $z \in \Omega$

Solution. Since $f _ { n }  f$ uniformly on compact sets, we also know that $f _ { n } ^ { \prime }  f ^ { \prime }$ uniformly on compact sets. Suppose that $f$ is not identically zero. Then the zeros of $f$ are isolated. Fix any $z _ { 0 } \in \Omega$ Choose an $r > 0$ small enough so that $f$ has no zeros in $B ( z _ { 0 } , r )$ except for possibly at $z _ { \mathrm { 0 } }$ and $| f ( z ) | \geqslant \delta > 0$ for $\left. z - z _ { 0 } \right. = r$ Because $\partial B ( z _ { 0 } , r )$ is compact and each $f _ { n }$ is nonvanishing, each $f _ { n }$ is bounded away from 0 on $\partial B ( z _ { 0 } , r )$ and since $f$ is also bounded away from zero on it, we have $1 / f _ { n } \to 1 / f$ uniformly on $\partial B ( z _ { 0 } , r )$ Therefore by the argument principle, we have

$$
0 = \operatorname* { l i m } _ { n \to \infty } \left( \# \mathrm { z e r o s ~ o f ~ } f _ { n } \operatorname* { i n s i d e } B ( z _ { 0 } , r ) \right) = \operatorname* { l i m } _ { n \to \infty } \int _ { \partial B [ z _ { 0 } , r ] } \frac { f _ { n } ^ { \prime } ( z ) } { f _ { n } ( z ) } d z = \int _ { \partial B [ z _ { 0 } , r ] } \frac { f ^ { \prime } ( z ) } { f ( z ) } d z = \left( \# \mathrm { z e r o s ~ o f ~ } f \operatorname* { i n s i d e } B ( z _ { 0 } , r ) \right) .
$$

Therefore $f ( z _ { 0 } ) \neq 0$ , and since this argument can be applied at any point $z _ { 0 }$ , we conclude that $f$ is nonvanishing in $\Omega . \sqsupset$

Problem 10. Let $\alpha \in [ 0 , 1 ] \backslash \mathbb { Q }$ and let $\{ a _ { n } \} \in \ell ^ { 1 } ( \mathbb { N } )$ with $a _ { n } \neq 0$ for all $n .$ Show that

$$
f ( z ) ~ = ~ \sum _ { n \geq 1 } { \frac { a _ { n } } { z - e ^ { i \alpha n } } }
$$

converges and defines a function that is analytic in D which does not admit an analytic continuation to any domain larger than D.

Solution. Each of the summands is analytic in D, so to show that f is analytic in D it suffices to show that the sum converges uniformly on compact sets. Note that it is enough to show that sum converges uniformly on $\mathbb { D } _ { r } = \left\{ z : | z | < r \right\}$ For $z \in D _ { r }$ we have

$$
\left| \sum _ { n = k } ^ { \infty } \frac { a _ { n } } { z - e ^ { i \alpha n } } \right| \leqslant \sum _ { n = k } ^ { \infty } \frac { \left| a _ { n } \right| } { \left| z - e ^ { i \alpha n } \right| } < \frac { 1 } { 1 - r } \sum _ { n = k } ^ { \infty } \left| a _ { n } \right| ,
$$

which converges to 0 as $k  \infty .$ . Thus the sequence of partial sums for $f$ is uniformly Cauchy on $\mathbb { D } _ { r }$ . This establishes that the, sum converges everywhere in D, and defines an analytic function in D.

Let Ω be any region containing D. Then Ω contains an open arc of the unit circle. Since α is irrational, the points $\{ e ^ { i \alpha n } \}$ are dense in the unit circle, so there is some $e ^ { i \alpha k } \in \Omega$ . The intuition is that this is a contradiction because f will blow up near $e ^ { i \alpha k }$ , but it’s hard to show this directly. Instead let $g ( z ) = ( z - e ^ { i \alpha k } ) f ( z )$ . Since f is analytic in Ω by assumption, $g ( e ^ { i \alpha k } ) = 0$ . Consider for $0 < r < 1$

$$
g ( r e ^ { i \alpha k } ) ~ = ~ a _ { k } + \sum _ { n \neq k } \frac { a _ { n } ( r - 1 ) e ^ { i \alpha k } } { r e ^ { i \alpha k } - e ^ { i \alpha n } }
$$

where changing the order of summation is allowed because the series converges absolutely on each circle $| z | = r$ for $r < 1$ . Now note that we have

$$
\left| \frac { a _ { n } ( r - 1 ) e ^ { i \alpha k } } { r e ^ { i \alpha k } - e ^ { i \alpha n } } \right| \ \leqslant \ | a _ { n } | \frac { 1 - r } { 1 - r } \ \leqslant \ | a _ { n } |
$$

for all $r < 1$ , so by the Dominated Convergence theorem we have

$$
g ( e ^ { i \alpha k } ) ~ = ~ \operatorname* { l i m } _ { r  1 ^ { - } } g ( r e ^ { i \alpha k } ) ~ = ~ a _ { k } + \sum _ { n \neq k } \operatorname* { l i m } _ { r  1 ^ { - } } \frac { a _ { n } ( r - 1 ) e ^ { i \alpha k } } { r e ^ { i \alpha k } - e ^ { i \alpha n } } ~ = ~ a _ { k } ~ \neq ~ 0 ,
$$

which is a contradiction.

Problem 11. For each $p \in ( - 1 , 1 )$ , compute the improper Riemann integral

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { p } } { x ^ { 2 } + 1 } } d x .
$$

Solution. Define $\log ( z )$ to be the branch with the negative imaginary axis removed, i.e. Im $\big ( \log ( r e ^ { i \theta } ) \big ) =$ $\theta \in \left( { - \pi / 2 , 3 \pi / 2 } \right)$ . Then define

$$
f ( z ) : = \frac { z ^ { p } } { z ^ { 2 } + 1 } = \frac { \exp ( p \log z ) } { z ^ { 2 } + 1 } .
$$

Integrate f over the contour which consists of a half circle in the upper half plane from ´R to R, then along the negative real axis from ´R to ´, then a half circle in the upper half plane from ´ to , then along the positive real axis from  to R. The contributions from the two half circles go to 0 as $\epsilon \to 0 , R \to \infty$ and you are left with

$$
( 1 + \exp ( p \pi i ) ) \int _ { 0 } ^ { \infty } { \frac { x ^ { p } } { x ^ { 2 } + 1 } } d x \ = \ 2 \pi i \cdot \mathrm { R e s } _ { z = i } \ f ( z ) \ = \ \pi \cdot \exp ( p \pi i / 2 )
$$

(I left out the computation of the residue). After rearranging you get that the answer is $\frac { \pi } { 2 \cos ( p \pi / 2 ) }$

Problem 12. Compute the number of zeros, including multiplicity, of $f ( z ) = z ^ { 6 } + i z ^ { 4 } + 1$ in the upper half plane.

Solution. Since the polynomial is even, z is a root of multiplicity m if and only if ´z is a root of multiplicity m. Therefore the roots in the open upper half plane are in bijection with the roots in the open lower half plane. $ { \mathrm { I f } } {  { \boldsymbol { r } } } \neq 0$ is real, then Im $\bar { ( f ( r ) ) } \stackrel { - } { = } r ^ { 4 }$ which is nonzero. Since $f ( 0 ) \neq 0$ we see that f has no real roots. Since z has 6 total roots (counting multiplicity), exactly 3 of them must lie in the upper half plane. □

## 12 Fall 2014

Problem 1. Show that

$$
A : = \ \{ f \in L ^ { 3 } ( \mathbb { R } ) : \int _ { \mathbb { R } } | f ( x ) | ^ { 2 } d x < \infty \}
$$

is a Borel subset of $L ^ { 3 } ( \mathbb { R } )$

Solution. Define the functional $\phi _ { n }$ on $L ^ { 3 } ( \mathbb { R } )$ q by

$$
\phi _ { n } ( f ) ~ = ~ \int _ { - n } ^ { n } | f | ^ { 2 } .
$$

Note that we have

$$
A \ = \ \bigcup _ { m = 1 } ^ { \infty } \bigcap _ { n = 1 } ^ { \infty } \{ f \in L ^ { 3 } ( \mathbb { R } ) : \phi _ { n } ( f ) \leqslant m \} .
$$

So to show A is Borel it suffices to prove that $\phi _ { n }$ is a continuous function from $L ^ { 3 } ( \mathbb { R } ) \to \mathbb { R } .$ . For $f , g \in L ^ { 3 }$ we have

$$
\begin{array} { r l } { \displaystyle | \phi _ { n } ( f ) - \phi _ { n } ( g ) | } & { \leqslant \displaystyle \int _ { - n } ^ { n } | f ^ { 2 } - g ^ { 2 } | } & { \leqslant \displaystyle \int _ { - n } ^ { n } | f - g | ( | f | + | g | ) } \\ & { \leqslant \displaystyle \int _ { - n } ^ { n } | f - g | | f | + \displaystyle \int _ { - n } ^ { n } | f - g | | g | } \\ & { \leqslant \displaystyle ( \displaystyle \int _ { - n } ^ { n } | f - g | ^ { 3 } ) ^ { 1 / 3 } ( \displaystyle \int _ { - n } ^ { n } | f | ^ { 3 } ) ^ { 1 / 3 } ( \displaystyle \int _ { - n } ^ { n } 1 ^ { 3 } ) ^ { 1 / 3 } + ( \displaystyle \int _ { - n } ^ { n } | f - g | ^ { 3 } ) ^ { 1 / 3 } ( \displaystyle \int _ { - n } ^ { n } | g | ^ { 3 } ) ^ { 1 / 3 } ( \displaystyle \int _ { - n } ^ { n } | g | ^ { 3 } ) ^ { 1 / 3 } } \\ & { \leqslant \displaystyle ( 2 n ) ^ { 1 / 3 } \| f - g \| _ { L ^ { 3 } } ( \| f \| _ { L ^ { 3 } } + \| g \| _ { L ^ { 3 } } ) . } \end{array}
$$

Fix $\epsilon > 0 . \mathrm { ~ I f ~ } | | f - g | | _ { L ^ { 3 } } < \epsilon \cdot ( 3 ( 2 n ) ^ { 1 / 3 } | | f | | _ { L ^ { 3 } } ) ^ { - 1 }$ and $\| f - g \| _ { L ^ { 3 } } < \| f \| _ { L ^ { 3 } }$ , then

$$
| \phi _ { n } ( f ) - \phi _ { n } ( g ) | ~ < ~ ( 2 n ) ^ { 1 / 3 } ( 3 \left| | f | \right| | _ { L ^ { 3 } } ) \left| | f - g | \right| _ { L ^ { 3 } } ~ < ~ \epsilon .
$$

Thus $\phi _ { n } ( f )$ is continuous at f for every $f \in L ^ { 3 } ( \mathbb { R } )$ , so we’re done.

Problem 2. Construct an $f \in L ^ { 1 } ( \mathbb { R } )$ so that $f ( x + y )$ does not converge almost everywhere to $f ( x )$ as $y \to 0$ . Prove that your f has this property.

Solution. Let K be a fat Cantor set contained in r0, 1s. Recall that K is closed, has positive measure, and that each point in K is a boundary point. Take $f = \chi _ { K }$ . Since K is closed, f is measurable, and since K has finite measure, f lies in $L ^ { 1 }$ . But for each $x \in K$ every neighborhood U of x contains a point u which lies outside K and hence has $f ( u ) = 0$ . Therefore for each $x \in K , f ( x + y )$ does not converge to $f ( x )$ as $y \to 0$ . This is enough, since K has positive measure. □

Problem 3. Let $\left( f _ { n } \right)$ be a bounded sequence in $L ^ { 2 } ( \mathbb { R } )$ and suppose that $f _ { n } \to 0$ Lebesgue almost everywhere. Show that $f _ { n } \to 0$ in the weak topology on $L ^ { 2 } ( \mathbb { R } )$

Solution. To show that $f _ { n } \to 0$ in the weak topology on $L ^ { 2 } ( \mathbb { R } )$ , we need to show that $\phi ( f _ { n } ) \to 0$ for every bounded linear functional φ on $L ^ { 2 } ( \mathbb { R } )$ . Since $L ^ { 2 } ( \mathbb { R } )$ is a Hilbert space, by the Riesz representationş theorem we know that every bounded linear functional φ is of the form ş $\phi ( f ) ~ = ~ \int f ( x ) g ( x )$ dx for some $g \in L ^ { 2 } ( \mathbb { R } )$ . So it suffices to show that for any $g \in L ^ { 2 } ( \mathbb { R } )$ , we have $\int f _ { n } ( x ) g ( x ) d x \ \stackrel { \cdot } {  } \ 0$ as $n  \infty$ . Since $f _ { n } \to 0$ pointwise almost everywhere, we also have that ş $f _ { n } g \to 0$ pointwise almost everywhere. By the Vitali Convergence Theorem, to conclude that $\int f _ { n } g  0$ , it suffices to show that the sequence $\left\{ f _ { n } g \right\}$ is both uniformly integrable and tight.

As a reminder, uniformly integrable means that for every ş $\epsilon > 0$ there exists a $\delta > 0$ such that for any $n ,$ $m ( A ) < \delta$ implies $\int _ { A } | f _ { n } g | < \epsilon .$ Tight means that for any $\epsilon > 0 .$ , there exists a subset $E \subseteq \mathbb { R }$ such that for

any $n , \int _ { E ^ { c } } | f _ { n } g | < \epsilon .$

We know that $\left\{ f _ { n } \right\}$ is a bounded sequence in $L ^ { 2 } ( \mathbb { R } )$ , so let $\vert \vert f _ { n } \vert \vert _ { L ^ { 2 } } \leqslant M$ for all $n .$ . First we show uni-ş form integrability. Fix $\epsilon > 0$ . Since $| g | ^ { 2 }$ is integrable, there is a $\delta$ so that $m ( A ) < \delta$ implies $\int _ { A } | g | ^ { 2 } < \epsilon / M$ Now for any n, we have by Cauchy-Schwarz that if $m ( A ) < \delta _ { \mathrm { \scriptsize { : } } }$ 7

$$
\int _ { A } | f _ { n } g | \leqslant \left( \int _ { A } | f _ { n } | ^ { 2 } \right) ^ { 1 / 2 } \left( \int _ { A } | g | ^ { 2 } \right) ^ { 1 / 2 } \leqslant | | f _ { n } | | _ { L ^ { 2 } } { \frac { \epsilon } { M } } \leqslant \epsilon ,
$$

so the family $\left\{ f _ { n } g \right\}$ is uniformly integrable.

For tightness, fix $\epsilon > 0$ . Since $| g | ^ { 2 }$ is integrable, there is a set $E$ such that $\int _ { E ^ { c } } | g | ^ { 2 } < \epsilon / M$ . Then for any n, by the same Cauchy-Schwarz argument we have

$$
\int _ { A } | f _ { n } g | \ \leqslant \ \epsilon .
$$

Thus $\left\{ f _ { n } g \right\}$ is tight, so we conclude that $\int f _ { n } g \to 0 { \mathrm { ~ a s ~ } } n \to \infty . \quad \boxed { }$

Problem 4. Given $f \in L ^ { 2 } ( [ 0 , \pi ] )$ , we say that $f \in \mathcal { G } \mathrm { ~ i f ~ } f$ admits a representation of the form

$$
f ( x ) ~ = ~ \sum _ { n = 0 } ^ { \infty } c _ { n } \cos ( n x ) \quad \mathrm { w i t h } \quad \sum _ { n = 0 } ^ { \infty } ( 1 + n ^ { 2 } ) | c _ { n } | ^ { 2 } ~ < ~ \infty .
$$

Show that if $f \in { \mathcal { G } }$ and $g \in { \mathcal { G } }$ then $f g \in { \mathcal { G } }$

Solution. The motivation for this is that the $c _ { n }$ are basically the Fourier coefficients of $f ,$ so the condition for membership in $\mathcal { G }$ translates as $( 1 + n ^ { 2 } ) ^ { 1 / 2 } { \widehat { f } } ( n ) \in \ell ^ { 2 }$ . So $\mathcal { G }$ is basically a “Fourier series version” of the Sobolev space $H ^ { \bar { 1 } }$

First we want to make a technical modification so that we can work directly with the regular Fourier coefficients (it makes stuff easier later). It’s clear that $L ^ { 2 } ( [ 0 , \pi ] )$ is in bijection with the space $L _ { e } ^ { 2 } : =$ the subspace of $L ^ { 2 } ( [ - \pi , \pi ] )$ consisting of even functions. So we identify each $f \in { \mathcal { G } }$ with its even extension to $[ - \pi , \pi ]$ . For $f \in { \mathcal { G } }$ , the given condition implies that

$$
\sum _ { n = 0 } ^ { \infty } | c _ { n } | ~ = ~ \sum _ { n = 0 } ^ { \infty } | c _ { n } | ( 1 + n ^ { 2 } ) ^ { 1 / 2 } ( 1 + n ^ { 2 } ) ^ { - 1 / 2 } ~ \leqslant ~ \left( \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } ( 1 + n ^ { 2 } ) \right) ^ { 1 / 2 } \left( \sum _ { n = 0 } ^ { \infty } ( 1 + n ^ { 2 } ) ^ { - 1 } \right) ^ { 1 / 2 } ~ < ~ \infty .
$$

Thus by the Weierstrass M-test, we know that the given series representation for $f$ converges absolutely and uniformly on $[ - \pi , \pi ]$ . Recall that $\{ \cos ( n x ) \} _ { n = 0 } ^ { \infty }$ is an orthonormal basis for the Hilbert space $L _ { e } ^ { 2 }$ . For a fixed $n ,$ we calculate in two different ways the inner product

$$
{ \begin{array} { r l } { \langle f , \cos ( n x ) \rangle \ = \ \left. f , { \frac { 1 } { 2 } } ( e ^ { i n x } + e ^ { - i n x } ) \right. \ = \ { \frac { 1 } { 2 } } ( { \hat { f } } ( n ) + { \hat { f } } ( - n ) ) \ = \ { \hat { f } } ( n ) { \mathrm { ~ b e c a u s e ~ } } f { \mathrm { ~ i s ~ e v e n } } } \\ { \langle f , \cos ( n x ) \rangle \ = \ { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( x ) \cos ( n x ) d x \ = \ { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \sum _ { m = 1 } ^ { \infty } c _ { m } \cos ( m x ) \cos ( n x ) d x } \\ { \displaystyle = \ \sum _ { m = 1 } ^ { \infty } c _ { m } { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \cos ( m x ) \cos ( n x ) d x \ = \ { \left\{ \begin{array} { l l } { { \frac { 1 } { 2 } } c _ { n } } & { n \neq 0 } \\ { c _ { 0 } } & { n = 0 } \end{array} \right. } } \end{array} }
$$

where switching the order is justified because of the uniform convergence. Thus we conclude that for $f \in { \mathcal { G } }$ the coefficients $c _ { n }$ are exactly equal to $2 { \widehat { f } } ( n )$ for $n \neq 0$ and ${ \widehat { f } } ( 0 )$ for $n = 0$ . So the problem is equivalent to showing that for $f , g \in { \mathcal { G } }$ , we have $( 1 + n ^ { 2 } ) ^ { 1 / 2 } { \widehat { f g } } ( n ) \in \ell ^ { 2 }$

Let $f , g \in { \mathcal { G } }$ The same argument from above that showed the uniform convergence of the series repre-ř sentations also shows that the representations f or $\begin{array} { r } { g ( x ) = \sum _ { n = - \infty } ^ { \infty } \widehat { f \mathrm { ~ o r ~ } g } ( n ) e ^ { i n x } } \end{array}$ converge uniformly, so we can compute the Fourier coefficients

$$
\begin{array} { r c l } { { \widehat { f g } ( n ) ~ = ~ \displaystyle \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } f ( x ) g ( x ) e ^ { - i n x } d x ~ = ~ \displaystyle \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \displaystyle \sum _ { k = - \infty } ^ { \infty } \widehat { f } ( k ) e ^ { i k x } \displaystyle \sum _ { \ell = - \infty } ^ { \infty } \widehat { g } ( \ell ) e ^ { i \ell x } e ^ { - i n x } d x } } \\ { { ~ } } & { { ~ = ~ \displaystyle \sum _ { k , \ell = - \infty } ^ { \infty } \widehat { f } ( k ) \widehat { g } ( \ell ) \displaystyle \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } e ^ { i ( k + \ell - n ) x } d x ~ = ~ \displaystyle \sum _ { k = - \infty } ^ { \infty } \widehat { f } ( k ) \widehat { g } ( n - k ) ~ = ~ ( \widehat { f } * \widehat { g } ) ( n ) . } } \end{array}
$$

Also note the elementary estimate

$$
\begin{array} { r l r } { ( 1 + n ^ { 2 } ) ^ { 1 / 2 } } & { = } & { ( 1 + ( n - k + k ) ^ { 2 } ) ^ { 1 / 2 } = ( 1 + ( n - k ) ^ { 2 } + k ^ { 2 } + 2 ( n - k ) k ) ^ { 1 / 2 } \leqslant ( 1 + 2 ( n - k ) ^ { 2 } + 2 k ^ { 2 } ) ^ { 1 / 2 } } \\ & { \leqslant } & { ( 2 + 2 ( n - k ) ^ { 2 } + 2 + 2 k ^ { 2 } ) ^ { 1 / 2 } \leqslant ( 1 + ( n - k ) ^ { 2 } ) ^ { 1 / 2 } + ( 1 + k ^ { 2 } ) ^ { 1 / 2 } , } \end{array}
$$

valid for any $k \in \mathbb { R }$ . So we estimate

$$
\begin{array} { r c l } { ( 1 + n ^ { 2 } ) ^ { 1 / 2 } \widehat f g ( n ) } & { \lesssim } & { \displaystyle \sum _ { k = - \infty } ^ { \infty } ( 1 + k ^ { 2 } ) ^ { 1 / 2 } \widehat f ( k ) \widehat g ( n - k ) + \displaystyle \sum _ { k = - \infty } ^ { \infty } ( 1 + ( n - k ) ^ { 2 } ) ^ { 1 / 2 } \widehat g ( n - k ) \widehat f ( k ) } \\ & { = } & { \displaystyle ( ( 1 + k ^ { 2 } ) ^ { 1 / 2 } \widehat f ( k ) * \widehat g ) ( n ) + ( ( 1 + k ^ { 2 } ) ^ { 1 / 2 } \widehat g ( k ) * \widehat f ) ( n ) . } \end{array}
$$

Thus we have

$$
\begin{array} { r l } { \Big \| ( 1 + n ^ { 2 } ) ^ { 1 / 2 } \widehat f g ( n ) \Big \| _ { \ell ^ { 2 } } \lesssim } & { \Big \| ( 1 + k ^ { 2 } ) ^ { 1 / 2 } \widehat f ( k ) * \widehat g \Big \| _ { \ell ^ { 2 } } + \Big \| ( 1 + k ^ { 2 } ) ^ { 1 / 2 } \widehat g ( k ) * \widehat f \Big \| _ { \ell ^ { 2 } } } \\ { \lesssim } & { \Big \| ( 1 + k ^ { 2 } ) ^ { 1 / 2 } \widehat f ( k ) \Big \| _ { \ell ^ { 2 } } \| \widehat g \| _ { \ell ^ { 1 } } + \Big \| ( 1 + k ^ { 2 } ) ^ { 1 / 2 } \widehat g ( k ) \Big \| _ { \ell ^ { 2 } } \Big \| \widehat f \Big \| _ { \ell ^ { 1 } } \quad \mathrm { ~ b y ~ Y o u n g ' s ~ c o n v o l u t i o n ~ i n e q u a l i t y } } \\ { \lesssim } & { \infty \quad } \end{array}
$$

because we showed at the very beginning that $f \in { \mathcal { G } }$ implies $\widehat { f } \in \ell ^ { 1 }$ . Thus $( 1 + n ^ { 2 } ) ^ { 1 / 2 } { \widehat { f g } } ( n ) \in \ell ^ { 2 }$ so we’re done.

Problem 5. Let $\phi : [ 0 , 1 ]  [ 0 , 1 ]$ be continuous and let $d \mu$ be a Borel probability measure on r0, 1s. Suppose $\mu ( \phi ^ { - 1 } ( E ) ) = 0$ for every Borel set $E \subseteq [ 0 , 1 ]$ with $\mu ( E ) = 0$ . Show that there is a Borel measurable function $w : [ 0 , 1 ] \to [ 0 , \infty )$ so that

$$
\int f \circ \phi ( x ) d \mu ( x ) \ = \ \int f ( y ) w ( y ) d \mu ( y )
$$

for all continuous $f : [ 0 , 1 ] \to \mathbb { R }$

Solution. Since $\phi$ is continuous, it is Borel measurable. The condition that $\mu ( \phi ^ { - 1 } ( { \cal E } ) ) = 0$ whenever $\mu ( E ) = 0$ says that the measure $\phi _ { * } \mu$ is absolutely continuous with respect to $\mu .$ . Both $\mu$ and $\phi _ { * } \mu$ are finite measures on r0, 1s, so by the Radon-Nikodym theorem there is a Borel measurable function w such that

$$
( \phi _ { * } \mu ) ( A ) \ = \ \int _ { A } w ( x ) d \mu ( x )
$$

for all Borel sets A. Since $\phi _ { * } \mu$ is a positive measure, we know that w is a nonnegative function. Also, if $f$ is any continuous function on r0, 1s, then it is also integrable on r0, 1s, so by a well-known property of the Radon-Nikodym derivative,

$$
\int _ { 0 } ^ { 1 } f ( \phi ( x ) ) d \mu ( x ) \ = \ \int _ { 0 } ^ { 1 } f ( x ) d ( \phi _ { * } \mu ) ( x ) \ = \ \int _ { 0 } ^ { 1 } f ( x ) w ( x ) d \mu ( x ) . \quad \bigtriangledown
$$

Problem 6. Let X be a Banach space and let $X ^ { * }$ be its dual space. Suppose $X ^ { * }$ is separable; show that X is separable (you should assume the Axiom of Choice).

Solution. Let $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ be a countable dense subset of $X ^ { * }$ . By definition of operator norm, for each n pick $x _ { n } \in X$ with $\left| \left| x _ { n } \right| \right| = 1$ such that $| f _ { n } ( x _ { n } ) | > ( 1 / 2 ) \left| | f _ { n } \right| |$ . Let $M = \operatorname { s p a n } \{ x _ { n } \}$ We first want to show that M is dense in $X .$ , i.e. ${ \overline { { M } } } = X$ . Suppose that $y \notin { \overline { { M } } }$ Then by the Hahn-Banach theorem, there is a linear functional $f \in X ^ { * }$ such that $f = 0$ on M and $f ( y ) \neq 0$ By the separability of $X ^ { * }$ , there is a subsequence $\left\{ f _ { n _ { k } } \right\}$ that converges to f in the operator norm topology. We have

$$
| | f _ { n _ { k } } - f | | ~ \geqslant ~ | f _ { n _ { k } } ( x _ { n _ { k } } ) - f ( x _ { n _ { k } } ) | ~ = ~ | f _ { n _ { k } } ( x _ { n _ { k } } ) | ~ > ~ \frac { 1 } { 2 } | | f _ { n _ { k } } | | ,
$$

and since $\vert \vert f _ { n _ { k } } - f \vert \vert  0$ as $k  \infty$ , this implies that $| | f _ { n _ { k } } | |  0$ as $k  \infty$ as well, which implies that $f _ { n _ { k } }  0$ . But $f _ { n _ { k } }  f ,$ and f is not identically zero, so this is a contradiction. Thus ${ \overline { { M } } } = X$ , so M is dense in X .

Now to show X is separable, it suffices to find a countable set which is dense in M. Let S be the subset of M which consists only of linear combinations with coefficients in Ť $\mathbb { Q } + i \mathbb { Q } . \ S$ is a countable set because it can be put in bijection with $\textstyle \bigcup _ { n = 1 } ^ { \infty } ( \mathbb { Q } + i \mathbb { Q } ) ^ { n }$ , which is countable. Since $\mathbb { Q } + i \mathbb { Q }$ is dense in $\mathbb { C } ,$ it follows that S is dense in M, so S is dense in X and hence X is separable.

Problem 7. Find an explicit conformal mapping from the upper half plane slit along the vertical segment

$$
\{ z \in \mathbb { C } : \operatorname { I m } ( z ) > 0 \} \backslash ( 0 , 0 + i h ] , \quad h > 0
$$

to the unit disk.

Solution. Start with $\Omega _ { 1 } = \{ z \in \mathbb { C } : \operatorname { I m } ( z ) > 0 \} \backslash ( 0 , 0 + i h ]$ Let $f _ { 1 } ( z ) = i ( h / z )$ . This is a conformal map $\Omega \to \Omega _ { 2 } : = \{ z : \operatorname { R e } ( z ) > 0 \} \backslash [ 1 , \infty )$ . Let $f _ { 2 } ( z ) = z ^ { 2 }$ . This is a conformal map $\Omega _ { 1 } \to \Omega _ { 2 } : = \mathbb { C } \backslash [ 1 , \infty ) \backslash ( - \infty , 0 ]$ Let $f _ { 3 } ( z ) = 1 / z - 1$ . This is a conformal map $\Omega _ { 2 }  \Omega _ { 3 } : = \mathbb { C } \backslash ( - \infty , 0 ]$ . Let $f _ { 4 } ( z )$ be the branch of $\sqrt { z }$ that you get by removing the negative real axis. Then this is a conformal map $\Omega _ { 3 } \ \to \ \mathbb { H }$ Finally let $f _ { 5 } ( z ) = ( z - i ) / ( z + i )$ ; this is a conformal map $\mathbb { H } \to \mathbb { D }$ . Thus $f : = f _ { 5 } \circ f _ { 4 } \circ f _ { 3 } \circ f _ { 2 } \circ f _ { 1 }$ is a conformal map $\Omega  \mathbb { D } . \quad \bigsqcup$

Problem 8. Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Show that

$$
| f ( z ) | \ \leqslant \ C e ^ { a | z | }
$$

for some constants C and a if and only if we have

$$
| f ^ { ( n ) } ( 0 ) | ~ \leqslant ~ M ^ { n + 1 }
$$

for some constant M.

Solution. First suppose that $| f ( z ) | \leqslant C e ^ { a | z | }$ for all $z \in \mathbb { C }$ . Then by applying the Cauchy estimates to a disk of radius R centered at 0, we get

$$
| f ^ { ( n ) } ( 0 ) | ~ \leqslant ~ \frac { n ! } { R ^ { n } } C e ^ { a R } .
$$

Since $f$ is entire, the above inequality is valid for any $R > 0 ,$ , so we choose $R = n / a$ to get

$$
| f ^ { ( n ) } ( 0 ) | ~ \leqslant ~ \frac { n ! a ^ { n } } { n ^ { n } } C e ^ { n } ~ \leqslant ~ C \cdot ( e a ) ^ { n } ~ \leqslant ~ M ^ { n + 1 }
$$

for some constant M.

Conversely, suppose that $| f ^ { ( n ) } ( 0 ) | \leqslant M ^ { n + 1 }$ for all n. Then, since f is entire, we can write $f$ as a power series

$$
f ( z ) \ = \ \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }
$$

and it is valid for all $z \in \mathbb { C }$ . We know that the power series coefficients are given by

$$
a _ { n } ~ = ~ { \frac { f ^ { ( n ) } ( 0 ) } { n ! } } ,
$$

so we have

$$
| f ( z ) | \ \leqslant \ \sum _ { n = 0 } ^ { \infty } | a _ { n } | | z | ^ { n } \ \leqslant \ \sum _ { n = 0 } ^ { \infty } { \frac { M ^ { n + 1 } } { n ! } } | z | ^ { n } \ = \ M e ^ { M | z | }
$$

for all $z \in \mathbb { C } . \quad \bigsqcup$

Problem 9. Let $\Omega \subseteq \mathbb { C }$ be open and connected. Suppose $\left( f _ { n } \right)$ is a sequence of injective holomorphic functions defined on Ω such that $f _ { n }  f$ locally uniformly in Ω. Show that if $f$ is not constant, then $f$ is also injective in Ω.

Solution. Since $f _ { n }  f$ locally uniformly, we know that f is also holomorphic. We first prove the following variation of Hurwitz’s theorem: If each $f _ { n }$ has at most one zero in Ω, then either f is identically zero or f has at most one zero in Ω.

Suppose that $f$ is not identically zero. Then the zeros of $f$ are isolated. Suppose that $f ( z _ { 0 } ) = 0$ Pick $r > 0$ small enough so that f has no other zeros in $\overline { { B ( z _ { 0 } , r ) } }$ . Since f is nonzero on $\partial B ( z _ { 0 } , r )$ , which is compact, we have $| f ( z ) | \geqslant \delta > 0$ for $\left. z - z _ { 0 } \right. = r$ . This shows that $1 / f _ { n } \to 1 / f$ uniformly on $\partial B ( z _ { 0 } , r )$ . We also know that $f _ { n } ^ { \prime }  f ^ { \prime }$ uniformly on compact sets. Thus we conclude that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { \hat { \sigma } B ( z _ { 0 } , r ) } \frac { f _ { n } ^ { \prime } ( z ) } { f _ { n } ( z ) } d z \ = \ \int _ { \hat { \sigma } B ( z _ { 0 } , r ) } \frac { f ^ { \prime } ( z ) } { f ( z ) } d z .
$$

By the argument principle, the right side of this equation is equal to the number of zeros of $f$ inside $B ( z _ { 0 } , r )$ which is one. Similarly, the left side is equal to the number of zeros of $f _ { n }$ inside $B ( z _ { 0 } , r )$ . Thus the above equation implies that for sufficiently large $n , f _ { n }$ has exactly one zero inside $B ( z _ { 0 } , r )$ . So we have shown that given a zero of $f$ and a sufficiently small ball around that zero, then n can be made sufficiently large so that $f _ { n }$ has zero inside that ball. Thus, if $f$ had two zeros, we could put two disjoint balls around them, then the previous statement would imply that $f _ { n }$ would eventually have to have two zeros, which is a contradiction. Thus we conclude that $f$ has only one zero.

Now, for any $w \in \mathbb { C } .$ , we have that $f _ { n } - w$ converges locally uniformly to $f - w$ Since each $f _ { n }$ is injective, $f _ { n } - w$ has at most one zero in Ω. Thus $f - w$ is either identically zero or has at most one zero. Since this is true for every $w \in \mathbb { C } .$ , it implies that $f$ is either constant or injective.

Problem 10. Let us introduce a vector space B as follows.

$$
\mathcal B = \left\{ u : \mathbb C \to \mathbb C : u \mathrm { ~ i s ~ h o l o m o r p h i c ~ a n d ~ } \iint _ { \mathbb C } | u ( x + i y ) | ^ { 2 } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y < \infty \right\} .
$$

Show that B becomes a complete vector space when equipped with the norm

$$
\left| \left| u \right| \right| ^ { 2 } = \int _ { \mathbb { C } } \int _ { \mathbb { C } } \left| u ( x + i y ) \right| ^ { 2 } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y .
$$

Solution. Define a measure µ on C by $d \mu = e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y$ , i.e.

$$
\mu ( A ) : = \int _ { A } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y .
$$

Note that $\mu$ is a finite measure on $\mathbb { C } ,$ and $L ^ { 2 } ( \mu )$ is a complete vector space. Thus B is simply the subspace of $L ^ { 2 } ( \mu )$ consisting of holomorphic functions, so to show that B is complete it suffices to show that B is closed with respect to the $L ^ { 2 } ( \mu )$ norm.

Let $\left\{ f _ { n } \right\}$ be a sequence in $\boldsymbol { B }$ converging to $f \in L ^ { 2 } ( \mu )$ We need to show that f is holomorphic. To do that, it suffices to show that $f _ { n }  f$ uniformly on compact subsets of C. Let $K \subseteq \mathbb { C }$ be compact. Then $K ^ { \prime } : = \{ z \in \mathbb { C } : \mathrm { d i s t } ( z , K ) \leqslant 1 \}$ is also compact, so in particular, we have $e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } \geqslant c > 0$ on $K ^ { \prime }$ and $\lambda ( K ^ { \prime } ) < \infty$ where λ denotes Lebesgue measure on $\mathbb { C }$ . For any $z \in K$ , we use the mean value property of holomorphic functions to write

$$
f _ { n } ( z ) - f _ { m } ( z ) \ = \ \frac { 1 } { \pi } \int _ { B ( z , 1 ) } ( f _ { n } ( w ) - f _ { m } ( w ) ) d \lambda ( w ) ,
$$

thus we have by Cauchy-Schwarz

$$
\begin{array} { r l } { | f _ { n } ( z ) - f _ { m } ( z ) | \leqslant } & { \displaystyle \frac { 1 } { \pi } \int _ { R ( z , 1 ) } | f _ { n } ( w ) - f _ { m } ( w ) | d \lambda ( w ) } \\ { \leqslant } & { \displaystyle \frac { 1 } { \pi } \lambda ( B ( z , 1 ) ) ^ { 1 / 2 } \left( \int _ { B ( z , 1 ) } | f _ { n } ( w ) - f _ { m } ( w ) | ^ { 2 } d \lambda ( w ) \right) ^ { 1 / 2 } } \\ { \leqslant } & { \displaystyle \frac { 1 } { \pi } \lambda ( K ^ { \prime } ) ^ { 1 / 2 } \left( \frac { 1 } { c } \int _ { B ( z , 1 ) } | f _ { n } ( w ) - f _ { m } ( w ) | ^ { 2 } c d \lambda ( w ) \right) ^ { 1 / 2 } } \\ { \leqslant } & { M _ { K } \left( \displaystyle \int _ { B ( z , 1 ) } | f _ { n } ( w ) - f _ { m } ( w ) | ^ { 2 } e ^ { - ( z ^ { 2 } + y ^ { 2 } ) } d \lambda ( w ) \right) } \\ { \leqslant } & { M _ { K } \left( \displaystyle \int _ { B ( z , 1 ) } | f _ { n } ( w ) - f _ { m } ( w ) | ^ { 2 } e ^ { - ( z ^ { 2 } + y ^ { 2 } ) } d \lambda ( w ) \right) } \\ { \leqslant } & { M _ { K } \left| | f _ { n } - f _ { m } | \right| _ { L ^ { 2 } ( \mu ) } . } \end{array}
$$

Since $\left\{ f _ { n } \right\}$ converges in the $L ^ { 2 } ( \mu )$ norm, the above inequality implies that $\| f _ { n } - f _ { m } \| _ { L ^ { \infty } ( K ) } \to 0$ as $n , m  \infty$ , meaning that $\left\{ f _ { n } \right\}$ is uniformly Cauchy on K. Since $L ^ { \infty }$ is complete, this means that $f _ { n }$ converges uniformly on K to some function $g .$ In particular, $f _ { n }$ converges pointwise to g on $K$ . But we know that $f _ { n }$ converges to $f$ in $L ^ { 2 } ( \mu )$ , and thus (by passing to a subsequence if necessary) we also know that $f _ { n }$ converges to $f$ pointwise. Thus we must have $f = g ,$ , so we conclude that $f _ { n }$ converges uniformly to $f$ on K. This holds for any compact set $K \subseteq \mathbb { C }$ and thus we know that f must be holomorphic, so $\boldsymbol { B }$ is a closed subspace of $L ^ { 2 } ( \mu )$ and therefore complete.

Problem 11. Let $\Omega \subseteq \mathbb { C }$ be open, bounded, and simply connected. Let u be harmonic in Ω and assume that $u \geqslant 0$ . Show the following: for each compact set $K \subseteq \Omega$ , there exists a constant $C _ { K } > 0$ such that

$$
\operatorname* { s u p } _ { x \in K } u ( x ) \ \leqslant \ C _ { K } \operatorname* { i n f } _ { x \in K } u ( x ) .
$$

Solution. Since Ω is open, simply connected and not all of C, by the Riemann mapping theorem there is a conformal map $\phi : \mathbb { D }  \Omega$ Then the function $v ( z ) = u ( \phi ( z ) )$ is a harmonic function on D. Let K be any compact subset of Ω. Then $\phi ^ { - 1 } ( K )$ is a compact subset of D, so there is some $r \in ( 0 , 1 )$ such that $\phi ^ { - 1 } ( K ) \subseteq B ( 0 , r ) \subseteq { \overline { { B ( 0 , r ) } } } \subseteq \mathbb { D }$ . Since u is nonnegative, so is v, and thus by Harnack’s inequality, for any $z \in \phi ^ { - 1 } ( K )$ we have

$$
{ \frac { 1 - r } { 1 + r } } v ( 0 ) \ \leqslant \ { \frac { 1 - | z | } { 1 + | z | } } v ( 0 ) \ \leqslant \ v ( z ) \ \leqslant \ { \frac { 1 + | z | } { 1 - | z | } } v ( 0 ) \ \leqslant \ { \frac { 1 + r } { 1 - r } } v ( 0 ) .
$$

The left inequality shows that in $\begin{array} { r } { \mathfrak { i } \mathtt { f } _ { z \in \phi ^ { - 1 } ( K ) } v ( z ) \geqslant \frac { 1 - r } { 1 + r } v ( 0 ) } \end{array}$ , which implies $\begin{array} { r } { v ( 0 ) \leqslant \frac { 1 + r } { 1 - r } \operatorname* { i n f } _ { z \in \phi ^ { - 1 } ( K ) } v ( z ) } \end{array}$ . Then by putting this into the right inequality we get

$$
v ( z ) ~ \leqslant ~ \left( \frac { 1 + r } { 1 - r } \right) ^ { 2 } \operatorname* { i n f } _ { z \in \phi ^ { - 1 } ( K ) } v ( z )
$$

for any $z \in \phi ^ { - 1 } ( K )$ , so $\begin{array} { r } { \operatorname* { s u p } _ { z \in \phi ^ { - 1 } \left( K \right) } v ( z ) \leqslant \left( \frac { 1 + r } { 1 - r } \right) ^ { 2 } \operatorname* { i n f } _ { z \in \phi ^ { - 1 } \left( K \right) } v ( z ) } \end{array}$ . The constant $\scriptstyle \left( { \frac { 1 + r } { 1 - r } } \right) ^ { 2 }$ depends only on the set $K ,$ , so we conclude

$$
\operatorname* { s u p } _ { z \in \phi ^ { - 1 } ( K ) } u ( \phi ( z ) ) \ \leqslant \ C _ { K } \operatorname* { i n f } _ { z \in \phi ^ { - 1 } ( K ) } u ( \phi ( z ) ) ,
$$

and since $\phi$ is a bijection this is the same as saying $\begin{array} { r } { \operatorname* { s u p } _ { w \in K } u ( w ) \ \leqslant \ C _ { K } \operatorname* { i n f } _ { w \in K } u ( w ) } \end{array}$

Problem 12. Let $\Omega = \left. z \in \mathbb { C } : | z | > 1 \right.$ Suppose u $\colon \overline { { \Omega } }  \mathbb { R }$ is bounded and continuous on $\overline { { \Omega } }$ and subharmonic on Ω. Prove the following: if $u ( z ) \leqslant 0$ for all $| z | = 1$ then $u ( z ) \leqslant 0$ for all $z \in \Omega$

Solution. Let $v ( z ) = u ( 1 / z )$ Then v is subharmonic on $A : = \mathbb { D } \backslash \{ 0 \}$ and bounded and continuous on ${ \overline { { A } } } \backslash \{ 0 \}$ because $z \mapsto 1 / z$ is a conformal map from $A  \Omega$ . Fix $\epsilon > 0$ and let $f ( z ) = v ( z ) - \epsilon \log | 1 / z |$ Since log |z| is harmonic on A, we know that f does not have a local maximum in A. Also, since u is bounded, v also is, and thus $f ( z ) \to - \infty { \mathrm { ~ a s ~ } } | z | \to 0$ . So there exists an $r > 0$ such that $f ( z ) \leqslant 0$ for $| z | \leqslant r$ . Now f is continuous on the compact set $\left\{ z \in \mathbb { C } : r \leqslant | z | \leqslant 1 \right\}$ , so it achieves a maximum somewhere. But since $f ( z ) \leqslant 0$ for all $| z | = r$ and all $| z | = 1$ , if that maximum were positive then it would have to be achieved on the interior of A, which contradicts the maximum principle. Thus the maximum is at most zero, so $f ( z ) \leqslant 0$ for all $r \leqslant | z | \leqslant 1$ , and by choice of r this implies that $f \leqslant 0$ on A. Thus we have $v ( z ) \leqslant \epsilon \log \left| 1 / z \right|$ for all $z \in A$ . Since  is arbitrary, this means $v ( z ) = u ( 1 / z ) \leqslant 0$ for all $z \in A$ , which means that $u ( w ) \leqslant 0$ for all $w \in \Omega$

## 13 Spring 2015

Problem 1. Let $f \in L ^ { 1 } ( \mathbb { R } )$ . Show that

$$
\operatorname* { l i m } _ { n \to \infty } \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x \right| \ = \ \int \left| f ( x ) \right| d x .
$$

Solution. Let V be the set of functions which are finite linear combinations of characteristic functions of closed intervals. First we show that the result holds for elements of V . Let $g \in V$ and write

$$
g \ = \ \sum _ { j = 1 } ^ { M } \alpha _ { j } \cdot \chi _ { [ a _ { j } , b _ { j } ] } .
$$

Let n be sufficiently large so that for each $- n ^ { 2 } \leqslant k \leqslant n ^ { 2 }$ , the interval $[ k / n , ( k + 1 ) / n ]$ does not intersect more than one of the intervals $[ a _ { j } , b _ { j } ]$ . Then in particular, on each subinterval $[ k / n , ( k + 1 ) / n ]$ , f is either non-negative or non-positive, depending on the sign of $\alpha _ { j }$ . Thus we have, for such sufficiently large $n ,$

$$
\displaystyle \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x \right| ~ = ~ \displaystyle \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \int _ { k / n } ^ { ( k + 1 ) / n } | f ( x ) | d x ~ = ~ \int _ { - n } ^ { n } | f ( x ) | d x ,
$$

so

$$
\operatorname* { l i m } _ { n \to \infty } \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x \right| \ = \ \int \left| f ( x ) \right| d x .
$$

Thus the result holds for functions in $V .$

We know that V is dense in $L ^ { 1 } ( \mathbb { R } )$ . Let $f \in L ^ { 1 } ( \mathbb { R } )$ and fix $\epsilon > 0$ . We need to show that when n is sufficiently large, we have

$$
\left| \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x \right| - \int | f ( x ) | d x \right| \ < \ \epsilon .
$$

Let $g$ be an element of V such that $| | f - g | | _ { L ^ { 1 } } < \epsilon / 3$ . We have the estimate

$$
\begin{array} { r l } { \displaystyle \left| \displaystyle \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \displaystyle \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x \right| - \displaystyle \int | f ( x ) | d x \right| \leqslant } & { \displaystyle \left| \displaystyle \int | f ( x ) | d x - \displaystyle \int | g ( x ) | d x \right| + \displaystyle \left| \displaystyle \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \displaystyle \int _ { k / n } ^ { ( k + 1 ) / n } g ( x ) d x \right| - \displaystyle \int | g ( x ) | d x \right| } \\ & { + \displaystyle \left| \displaystyle \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \displaystyle \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x \right| - \displaystyle \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \displaystyle \int _ { k / n } ^ { ( k + 1 ) / n } g ( x ) d x \right| \right| } \\ { = : } & { I + I I + I I I . } \end{array}
$$

By choice of $^ { g , }$ we have $I < \epsilon / 3$ Since we have already proved the result for elements of $V ,$ let n be large enough so that $I I < \epsilon / 3$ . Finally, by taking absolute values inside multiple times we have

$$
\begin{array} { r l r } { { I I I } \leqslant } & { \displaystyle \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x - \int _ { k / n } ^ { ( k + 1 ) / n } g ( x ) d x \right| \leqslant } & { \displaystyle \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \int _ { k / n } ^ { ( k + 1 ) / n } | f ( x ) - g ( x ) | d x = \int _ { - n } ^ { n } | f ( x ) - g ( x ) | d x } \\ { \leqslant } & { | | f - g | | _ { L ^ { 1 } } < \epsilon / 3 . } \end{array}
$$

Thus we conclude that

$$
\left| \sum _ { k = - n ^ { 2 } } ^ { n ^ { 2 } } \left| \int _ { k / n } ^ { ( k + 1 ) / n } f ( x ) d x \right| - \int | f ( x ) | d x \right| \ < \ \epsilon
$$

for all sufficiently large n and thus the result holds for all $f \in L ^ { 1 } ( \mathbb { R } )$

Problem 2. Let $f \in L _ { l o c } ^ { 2 } ( \mathbb { R } ^ { n } ) , g \in L _ { l o c } ^ { 3 } ( \mathbb { R } ^ { n } )$ . Assume that for all real $r \geqslant 1$ , we have

$$
\int _ { r \leqslant | x | \leqslant 2 r } | f ( x ) | ^ { 2 } d x \leqslant r ^ { a } , \quad \int _ { r \leqslant | x | \leqslant 2 r } | g ( x ) | ^ { 3 } d x \leqslant r ^ { b } .
$$

Here a and b are such that $3 a + 2 b + n < 0$ . Show that $f g \in L ^ { 1 } ( \mathbb { R } ^ { n } )$

Solution. Let $E _ { 0 } \ = \ \{ x \in \mathbb { R } ^ { n } \ : \ | x | \ \leqslant \ 1 \}$ and for $k \geqslant 1$ let $E _ { k } \ = \ \left\{ x \in \mathbb { R } ^ { n } : 2 ^ { k - 1 } \leqslant | x | \leqslant 2 ^ { k } \right\}$ Since each $E _ { k }$ is compact for $k \geqslant 0 , | f | ^ { 2 }$ and $| \boldsymbol g | ^ { 3 }$ are integrable on each $E _ { k }$ , which also implies by compactness that $| f |$ and |g| are integrable on each $E _ { k }$ . To show that $f g \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ it suffices to show that

$$
\sum _ { k = 1 } ^ { \infty } \int _ { E _ { k } } | f ( x ) g ( x ) | d x \ < \ \infty .
$$

For each $k \geqslant 1$ , by H¨older’s inequality using $1 / 6 + 1 / 2 + 1 / 3 = 1$ , we have

$$
\begin{array} { r l r } {  { \int _ { E _ { k } } | f ( x ) g ( x ) | d x \ \leqslant } } & { ( \int _ { E _ { k } } 1 ^ { 6 } d x ) ^ { 1 / 6 } ( \int _ { E _ { k } } | f ( x ) | ^ { 2 } d x ) ^ { 1 / 2 } ( \int _ { E _ { k } } | g ( x ) | ^ { 3 } d x ) ^ { 1 / 3 } } \\ & { \leqslant } & { ( \lambda _ { n } ( E _ { k } ) ) ^ { 1 / 6 } ( ( 2 ^ { k - 1 } ) ^ { a } ) ^ { 1 / 2 } ( ( 2 ^ { k - 1 } ) ^ { b } ) ^ { 1 / 3 } . } \end{array}
$$

Since $E _ { k } \subseteq [ - 2 ^ { k } , 2 ^ { k } ]$ , we have $\lambda _ { n } ( E _ { k } ) \leqslant ( 2 ^ { k + 1 } ) ^ { n }$ . Thus we have

$$
\int _ { E _ { k } } | f ( x ) g ( x ) | d x \ \leqslant \ ( 2 ^ { k + 1 } ) ^ { n / 6 } ( 2 ^ { k - 1 } ) ^ { a / 2 } ( 2 ^ { k - 1 } ) ^ { b / 3 } \ = \ 4 ^ { n / 6 } \cdot ( 2 ^ { k - 1 } ) ^ { n / 6 + a / 2 + b / 3 } .
$$

By hypothesis, $n / 6 + a / 2 + b / 3 < 0 .$ , so let $- \delta \in ( n / 6 + a / 2 + b / 3 , 0 )$ . Then we have

$$
\sum _ { k = 1 } ^ { \infty } \int _ { E _ { k } } | f ( x ) g ( x ) | d x \ \leqslant \ 4 ^ { n / 6 } \sum _ { k = 1 } ^ { \infty } ( 2 ^ { k - 1 } ) ^ { - \delta } \ = \ 4 ^ { n / 6 } \sum _ { k = 1 } ^ { \infty } \left( { \frac { 1 } { 2 ^ { \delta } } } \right) ^ { k - 1 } \ < \ \infty
$$

because $2 ^ { \delta } > 1$ . Thus $f g \in L ^ { 1 } ( \mathbb { R } ^ { n } )$

Problem 3a. Let $f \in L _ { l o c } ^ { 1 } (  { \mathbb { R } } ^ { n } )$ and let

$$
M f ( x ) ~ = ~ \operatorname* { s u p } _ { r > 0 } { \frac { 1 } { m ( B ( r , x ) ) } } \int _ { B ( r , x ) } \left| f ( y ) \right| d y
$$

be the Hardy-Littlewood maximal function. Show that

$$
m ( \{ x : M f ( x ) > s \} ) \ \leqslant \ { \frac { C _ { n } } { s } } \int _ { | f ( x ) | > s / 2 } | f ( x ) | d x , \quad s > 0 ,
$$

where the constant $C _ { n }$ depends on n only. The Hardy-Littlewood maximal theorem may be used.

Solution. Suppose that $B \subseteq \mathbb { R } ^ { n }$ is a ball and that $\frac { 1 } { m ( B ) } \int _ { B } | f ( y ) | d y > s$ . Then we have

$$
\begin{array} { c l c } { \displaystyle { s \cdot m ( B ) < \int _ { B \cap \{ x : | f ( x ) | \leqslant s / 2 \} } | f ( y ) | d y + \int _ { B \cap \{ x : | f ( x ) | > s / 2 \} } | f ( y ) | d y } } \\ { \displaystyle { \leqslant \frac { s } { 2 } \cdot m ( B ) + \int _ { B \cap \{ x : | f ( x ) | > s / 2 \} } | f ( y ) | d y . } } \end{array}
$$

Define $\tilde { f } ( x )$ to be $f ( x ) { \mathrm { ~ i f ~ } } | f ( x ) | > s / 2$ and 0 otherwise. It follows from the work above that

$$
\int _ { B } | { \tilde { f } } ( y ) | d y > { \frac { s } { 2 } } .
$$

Thus if $M f ( x ) > s$ , then $M \tilde { f } ( x ) > s / 2$ . Applying the Hardy-Littlewood maximal inequality to $\tilde { f }$ gives

$$
\begin{array} { l } { \displaystyle { m ( \{ x : M f ( x ) > s \} ) \leqslant m ( \{ x : M \tilde { f } ( x ) > s / 2 \} ) } } \\ { \displaystyle { \leqslant \frac { C _ { n } } { s } \int \lvert \tilde { f } ( y ) \rvert d y } } \\ { \displaystyle { = \frac { C _ { n } } { s } \int _ { \lvert f ( x ) \rvert > s / 2 } \lvert f ( y ) \rvert d y , } } \end{array}
$$

for some constant $\mathbf { \quad } C _ { n } . \mathbf { \quad } \sqcup$

Problem 3b. Prove that if $\phi \in C ^ { 1 } ( \mathbb { R } ) , \phi ( 0 ) = 0$ , and $\phi ^ { \prime } > 0$ , then

$$
\int \phi ( M f ( x ) ) d x \ \leqslant \ C _ { n } \int | f ( x ) | \left( \int _ { 0 < t < 2 | f ( x ) | } { \frac { \phi ^ { \prime } ( t ) } { t } } d t \right) d x .
$$

Solution. Using part (a), we estimate the integral on the right by

$$
\begin{array} { r l } { C _ { n } \displaystyle \int | f ( x ) | \left( \displaystyle \int _ { 0 < s < 2 / t ( s ) } \frac { \phi ( f ( x ) } { t } + d t \right) d x - C _ { n } \left( \displaystyle \int _ { 0 < t ( s ) \leq t < 2 / t ( s ) } | f ( x ) | \frac { \phi ( f ( x ) ) } { t } \right) d x + d t } & { \mathrm { ~ b y ~ T o n e l l ~ b e c a u s e ~ } \phi ^ { \prime } > 0 } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle \int _ { 0 } \frac { \phi ( f ( t ) ) } { t } \left\{ \frac { \phi ( f ( t ) ) } { t } \int _ { | f ( t ) | < t } | f ( x ) | < d t \right\} } d x + d t  \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle \int _ { 0 } ^ { \infty } \displaystyle \phi ^ { \prime } ( t ) \int _ { \mathbb { M } / ( s ) < d t } d x + d t } \\ & { = \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad  \end{array}
$$

Problem 4. Let $f \in L _ { l o c } ^ { 1 } (  { \mathbb { R } } )$ be 2π-periodic. Show that the linear combinations of the translates $f ( x { - } a ) , a \in$ R, are dense in $L ^ { 1 } ( ( 0 , 2 \pi ) )$ if and only if each Fourier coefficient of $f { \mathrm { ~ i s ~ } } \neq 0$

Solution. For a function $u \in L ^ { 1 } ( [ 0 , 2 \pi ] )$ , denote by ${ \hat { u } } ( n )$ the nth Fourier coefficient of u. First suppose that $\hat { f } ( n ) = 0$ for some n. Then note that for any linear combination of translates of $f , h ( x ) \ : =$ $\alpha _ { 1 } f ( x - a _ { 1 } ) + \ldots + \alpha _ { m } f ( x - a _ { m } )$ , we have $\hat { h } ( n ) = \alpha _ { 1 } e ^ { - i n a _ { 1 } } \hat { f } ( n ) + . . . + \alpha _ { m } e ^ { - i n a _ { m } } \hat { f } ( n ) = 0$ . But then the span of the linear translates of f can’t possibly be dense in $L ^ { 1 }$ , because if we let $g ( x ) = e ^ { i n x }$ , then ${ \hat { g } } ( n ) = 1$ , and since the map $u \mapsto { \hat { u } }$ is a continuous mapping $L ^ { 1 } \to \ell ^ { \infty }$ , there can’t be a sequence of linear combinations of translates of $f$ converging to g in $L ^ { 1 }$

Conversely, suppose that $\hat { f } ( n ) \ne 0$ for every n. Let M be the closure (with respect to the $L ^ { 1 }$ norm) of span $\{ f ( x - a ) : a \in \mathbb { R } \}$ and suppose that $M \ne L ^ { 1 }$ . Then by the Hahn-Banach theorem, there is a nonzero bounded linear functional $\phi \in ( L ^ { 1 } ) ^ { * }$ which is zero on M. Since $( L ^ { 1 } ) ^ { * } \simeq L ^ { \infty }$ , we get that there exists a nonzero $g \in L ^ { \infty }$ such that

$$
\int _ { 0 } ^ { 2 \pi } g ( x ) f ( x - a ) d x \ = \ 0
$$

for every $a \in \mathbb { R }$ If we consider the above integral as a function of $^ { a , }$ call it $h ( a )$ , then $h$ is identically zero, so in particular it is 2π-periodic, so we can look at its Fourier coefficients. A standard computation

shows that ${ \hat { h } } ( n ) = { \hat { g } } ( n ) { \overline { { { \hat { f } } ( n ) } } }$ for all $n ,$ and since h is identically zero, $\hat { h } ( n ) = 0$ for all n. Since ${ \hat { f } } ( n ) \neq 0$ for all $n _ { \colon }$ , this implies that ${ \hat { g } } ( n ) = 0$ for all $n ,$ but this contradicts the fact that g is nonzero, so we’re done.

Problem 5. Let $u \in L ^ { 2 } ( \mathbb { R } )$ and let us set

$$
U ( x , \xi ) ~ = ~ \int e ^ { - ( x + i \xi - y ) ^ { 2 } / 2 } u ( y ) d y , \quad x , \xi \in \mathbb { R } .
$$

Show that $U ( x , \xi )$ is well-defined on $\mathbb { R } ^ { 2 }$ and that there exists a constant $C > 0$ such that for all $u \in L ^ { 2 } ( \mathbb { R } )$ , we have

$$
\iint | U ( x , \xi ) | ^ { 2 } e ^ { - \xi ^ { 2 } } d x d \xi \ = \ C \int | u ( y ) | ^ { 2 } d y .
$$

Determine C explicitly.

Solution. To show that $U ( x , \xi )$ is well-defined, note that by Cauchy-Schwarz

$$
\int \left| e ^ { - ( x + i \xi - y ) ^ { 2 } / 2 } u ( y ) \right| d y \leqslant \left( \int e ^ { - ( x + i \xi - y ) ^ { 2 } } d y \right) ^ { 1 / 2 } \left( \int | u ( y ) | ^ { 2 } d y \right) ^ { 1 / 2 } < \infty .
$$

Now we expand

$$
U ( x , \xi ) ~ = ~ e ^ { - x ^ { 2 } / 2 } e ^ { \xi ^ { 2 } / 2 } e ^ { - i x \xi } \int e ^ { x y - y ^ { 2 } / 2 } u ( y ) e ^ { i \xi y } d y .
$$

For a fixed $x ,$ let

$$
f _ { x } ( y ) ~ = ~ u ( y ) e ^ { x y - y ^ { 2 } / 2 } .
$$

Then we see that

$$
{ \hat { f } } _ { x } ( \xi ) ~ = ~ \int e ^ { x y - y ^ { 2 } / 2 } u ( y ) e ^ { - 2 \pi i \xi y } d y ,
$$

so

$$
U ( x , \xi ) ~ = ~ e ^ { - x ^ { 2 } / 2 } e ^ { \xi ^ { 2 } / 2 } e ^ { - i x \xi } \hat { f } _ { x } ( - \xi / ( 2 \pi ) ) .
$$

Therefore, by Plancherel and Tonelli since everything is non-negative, we have

$$
\begin{array} { r l r } { \displaystyle \iint | U ( x \xi ) | ^ { 2 } e ^ { - \xi ^ { 2 } } d x d \xi } & { = } & { \displaystyle \iint e ^ { - x ^ { 2 } } | \hat { f } _ { x } ( - \xi / ( 2 \pi ) ) | ^ { 2 } d x d \xi \ = \ 2 \pi \int e ^ { - x ^ { 2 } } \displaystyle \int \left| \hat { f } _ { x } ( \xi ) \right| ^ { 2 } d \xi d x \ } \\ & { = } & { \displaystyle 2 \pi \int e ^ { - x ^ { 2 } } \displaystyle \int | f _ { x } ( y ) | ^ { 2 } d y d x \ = \ 2 \pi \iint e ^ { - x ^ { 2 } + 2 x y - y ^ { 2 } } | u ( y ) | ^ { 2 } d y d x } \\ & { = } & { \displaystyle 2 \pi \int | u ( y ) | ^ { 2 } \left( \displaystyle \int e ^ { - ( x - y ) ^ { 2 } } d x \right) d y \ = \ 2 \pi ^ { 3 / 2 } \int | u ( y ) | ^ { 2 } d y . \quad \bigtriangledown } \end{array}
$$

Problem 6. When $B _ { 1 }$ and $B _ { 2 }$ are Banach spaces, we say a linear operator $T : B _ { 1 } \to B _ { 2 }$ is compact if for any bounded sequence $\left( x _ { n } \right)$ in $B _ { 1 }$ , the sequence $\left( T x _ { n } \right)$ has a convergent subsequence. Show that if $T$ is compact then ImpT q has a dense countable subset.

Solution. Since T is a compact operator, we know that for any bounded set $A \subseteq B _ { 1 } , { \cal T } ( A )$ is a relatively compact subset of $B _ { 2 }$ . Let $A _ { n } = \left\{ x \in B _ { 1 } : \left. \left. x \right. \right. _ { B _ { 1 } } \leqslant n \right\}$ . Then we can write $\textstyle B _ { 1 } = \bigcup _ { n = 1 } ^ { \infty } A _ { n }$ , so we have Im $\textstyle { 1 ( T ) = \bigcup _ { n = 1 } ^ { \infty } T ( A _ { n } ) }$ . Since each $A _ { n }$ is a bounded set, each $T ( A _ { n } )$ is relatively compact. This means that $\overline { { T ( A _ { n } ) } }$ is compact. Since compact sets are separable (this follows from the totally bounded definition of compactness), it follows that $\overline { { T ( A _ { n } ) } }$ has a countable dense subset. We need to upgrade this to a countable dense subset of $T ( A _ { n } )$ . Let E be a countable dense subset of $\overline { { T ( A _ { n } ) } }$ . Start with ${ \tilde { E } } : = E \cap T ( A _ { n } )$ . For any $x \in E \backslash T ( A _ { n } )$ , there is a sequence $\{ x _ { k } \} \in T ( A _ { n } )$ converging to x. Add the sequence $\{ x _ { k } \}$ to $\widetilde { E }$ . Repeating this process for every $x \in E \backslash T ( A _ { n } )$ , we see that $\tilde { E }$ is at most a countable union of countable sequences and is thus countable, and it’s clear that it is dense in $T ( A _ { n } )$ . Thus $T ( A _ { n } )$ also has a countable dense subset forŤ each n. Thus by taking the (countable) union of these dense subsets, we see that Im $\textstyle ( T ) = \bigcup _ { n = 1 } ^ { \infty } T ( A _ { n } )$ has

a countable dense subset.

Problem 7. Suppose $f _ { n } : \mathbb { D } \to \mathbb { H }$ is a sequence of holomorphic functions and $f _ { n } ( 0 ) \to 0 { \mathrm { ~ a s ~ } } n \to \infty$ Show that $f _ { n } ( z ) \to 0$ uniformly on compact subsets of D.

Solution. Any compact subset of D is contained in $\overline { { B ( 0 , r ) } }$ for some $0 \textless r \textless 1$ , so it suffices to show that $f _ { n } \to 0$ uniformly on $\overline { { B ( 0 , r ) } }$ for each $0 < r < 1$ . Fix such an $r .$ Note that since each $f _ { n }$ takes values only in H, we can define a single-valued analytic branch of $g _ { n } ( z ) : = { \sqrt { f _ { n } ( z ) } }$ on D. Each $g _ { n }$ is a holomorphic function from D to $\Omega : = \{ z \in \mathbb { C } : \operatorname { R e } ( z ) , \operatorname { I m } ( z ) > 1 \}$ and it is still true that $g _ { n } ( 0 ) \to 0$ as $n  \infty$ . Let $u _ { n } = \operatorname { R e } ( g _ { n } )$ and $v _ { n } = \operatorname { I m } ( g _ { n } )$ . We also have $u _ { n } ( 0 ) , v _ { n } ( 0 ) \to 0$ as $n \to \infty$ . Since $g _ { n }$ is holomorphic and takes values in $\Omega , u _ { n }$ and $v _ { n }$ are both positive harmonic functions on D. Thus for any $z \in B ( 0 , r )$ , we can apply Harnack’s inequality to get

$$
| u _ { n } ( z ) | \ \leqslant \ { \frac { 1 + | z | } { 1 - | z | } } | u _ { n } ( 0 ) | \ \leqslant \ { \frac { 1 + r } { 1 - r } } | u _ { n } ( 0 ) | ,
$$

which shows that $u _ { n } \to 0$ uniformly on ${ \overline { { B ( 0 , r ) } } } .$ . The same argument holds for $v _ { n }$ . Thus since $\operatorname { R e } ( g _ { n } )$ and Im $\left( g _ { n } \right)$ both converge uniformly to 0 on $B ( 0 , r ) , ~ g _ { n }$ also does. Finally, since $| f _ { n } ( z ) | = | g _ { n } ( z ) | ^ { 2 }$ , this also shows that $f _ { n } \to 0$ uniformly on $\overline { { B ( 0 , r ) } }$ , so we are done. □

Alternate solution. Let $\begin{array} { r } { g _ { n } \ = \ \frac { f _ { n } - i } { f _ { n } + i } } \end{array}$ The relation $\begin{array} { r } { f _ { n } ~ = ~ \frac { ( - i ) ( g _ { n } + 1 ) } { g _ { n } - 1 } } \end{array}$ shows that it suffices to show that the $g _ { n }$ converge locally uniformly $\mathrm { t o } \mathrm { ~ - 1 ~ }$ . Note the $g _ { n }$ are holomorphic maps $\mathbb { D }  \mathbb { D }$ . Let $\psi _ { n } ^ { - 1 }$ be an automorphism of D which takes $g _ { n } ( 0 )$ to 0 and let $h _ { n } = \psi _ { n } ^ { - 1 } \circ g _ { n }$ Then $h _ { n }$ is holomorphic with $h _ { n } ( 0 ) = 0$ Write $g _ { n } ~ = ~ \psi _ { n } \circ h _ { n }$ We want to show that $g _ { n }$ converges locally uniformly to ´1. Fix a compact set $K : = { \overline { { B ( 0 , r ) } } } \subseteq { \mathbb { D } }$ . By the Schwarz lemma, $h _ { n } ( K ) \subseteq K$ . So to show $g _ { n }  - 1$ uniformly on K, it’s enough to show $\psi _ { n }  - 1$ uniformly on K. This is just a calculation: for any $| z | \leqslant r .$ , we have

$$
\left| \psi _ { n } ( z ) - g _ { n } ( 0 ) \right| ~ = ~ \left| { \frac { z + g _ { n } ( 0 ) } { 1 + \overline { { g _ { n } ( 0 ) } } z } } - g _ { n } ( 0 ) \right| ~ = ~ { \frac { | z | } { \left| 1 + \overline { { g _ { n } ( 0 ) } } z \right| } } ( 1 - | g _ { n } ( 0 ) | ^ { 2 } ) ~ \leqslant ~ { \frac { 2 r } { 1 - r } } ( 1 - | g _ { n } ( 0 ) | ^ { 2 } )
$$

for sufficiently large n (where “sufficiently large” here only depends on the convergence of $g _ { n } ( 0 ) \ \mathrm { t o \ - 1 }$ , so this is uniform in $| z | \leqslant r )$ Since $g _ { n } ( 0 ) \to - 1$ by hypothesis (because $f _ { n } ( 0 ) \to 0 )$ , this shows $\psi _ { n }  - 1$ uniformly on $K .$ , so we’re done. □

Problem 8. Let $f : \mathbb { C } \to \mathbb { C }$ be holomorphic and suppose

$$
\operatorname* { s u p } _ { x \in \mathbb { R } } \{ | f ( x ) | ^ { 2 } + | f ( i x ) | ^ { 2 } \} < \infty { \mathrm { ~ a n d ~ } } | f ( z ) | \leqslant e ^ { | z | } { \mathrm { ~ f o r ~ a l l ~ } } z \in \mathbb { C } .
$$

Deduce that $f$ is constant.

Solution. By Liouville’s theorem, to show f is constant it is enough to show that f is bounded. The first given condition implies that there is some $M < \infty$ such that $| f ( z ) | \leqslant M$ for all z with either $\mathrm { R e } ( z ) = 0$ or $\operatorname { I m } ( z ) = 0$ . First we show that f is bounded in the first quadrant $A : = \{ z : \mathrm { R e } ( z ) > 0 , \mathrm { I m } ( z ) > 0 \}$

We use the Phragmen-Lindel¨of method. Fix $\epsilon > 0 .$ , and define

$$
g ( z ) ~ = ~ f ( z ) \cdot \exp ( - \epsilon ( e ^ { - i \pi / 4 } z ) ^ { 3 / 2 } )
$$

where $w \mapsto w ^ { 3 / 2 }$ is defined by removing the branch cut along the negative real axis, so that $( r e ^ { i \theta } ) ^ { 3 / 2 } =$ $r ^ { 3 / 2 } e ^ { i 3 \theta / 2 }$ . We wish to show that $| g ( z ) | \to 0 { \mathrm { ~ a s ~ } } | z | \to \infty$ in A. Writing $z = r e ^ { i \theta }$ , we have

$$
\begin{array} { r l } { | g ( z ) | ~ = ~ | f ( z ) | \exp ( \operatorname { R e } ( - \epsilon ( e ^ { - i \pi / 4 } z ) ^ { 3 / 2 } ) ) ~ \leqslant ~ \exp ( r ) \exp ( - \epsilon r ^ { 3 / 2 } \operatorname { R e } ( e ^ { - i 3 \pi / 8 } e ^ { i 3 \theta / 2 } ) ) } \\ & { \leqslant \exp ( r ) \exp ( - \epsilon r ^ { 3 / 2 } \cos ( 3 \theta / 2 - 3 \pi / 8 ) ) . } \end{array}
$$

On A, since $\theta \in ( 0 , \pi / 2 )$ , we have $3 \theta / 2 \mathrm { - } 3 \pi / 8 \in ( - 3 \pi / 8 , 3 \pi / 8 )$ , and thus cos $( 3 \theta / 2 \mathrm { - } 3 \pi / 8 ) > \cos ( 3 \pi / 8 ) = : \delta > 0 .$ So we have

$$
| g ( z ) | \ \leqslant \ \exp ( r - \epsilon \delta r ^ { 3 / 2 } )
$$