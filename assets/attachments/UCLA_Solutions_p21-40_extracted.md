a contradiction.

Problem 9. Let

$$
f ( z ) \ = \ \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }
$$

be a holomorphic function in D. Show that if

$$
\sum _ { n = 2 } ^ { \infty } n | a _ { n } | \ \leqslant \ | a _ { 1 } |
$$

with $a _ { 1 } \neq 0$ then f is injective.

Solution.
We have $\begin{array} { r } { f ^ { \prime } ( z ) = \sum _ { n = 1 } ^ { \infty } n a _ { n } z ^ { n - 1 } } \end{array}$ . Thus for any fixed $z \in \mathbb { D }$ we have

$$
| f ^ { \prime } ( z ) | ~ = ~ \left| \sum _ { n = 1 } ^ { \infty } n a _ { n } z ^ { n - 1 } \right| ~ \geqslant ~ | a _ { 1 } | - \sum _ { n = 2 } ^ { \infty } n | a _ { n } | | z | ^ { n } ~ > ~ | a _ { 1 } | - \sum _ { n = 2 } ^ { \infty } a | a _ { n } | ~ \geqslant ~ 0 ,
$$

so $f ^ { \prime }$ is nonvanishing in D.

Problem 10. Prove that the punctured disc $\{ z : 0 < | z | < 1 \}$ and the annulus $\{ z : 1 < | z | < 2 \}$ are not conformally equivalent.

Solution.
Let P be the punctured disc and A be the annulus.
Suppose $f : P  A$ is conformal.
Then, since A is bounded, the singularity of $f$ at 0 must be removable.
So we extend f to a holomorphic function $f : \mathbb { D }  A$ If we knew that $f$ were still conformal, this would be a contradiction because D is simply connected but A is not.
We already know $f$ is holomorphic and surjective, so to show f is conformal we just need to show that $f$ is still injective when we extend it to be defined at 0. Suppose $f ( 0 ) = f ( z )$ with $z \in P$ (this is the only possibility because $f$ is injective on $P )$ . Let $U$ and V be disjoint open balls around 0 and z respectively.
By the open mapping theorem, $f ( U )$ and $f ( V )$ are open.
They interset at $f ( 0 ) = f ( z )$ , so their intersection is open and non-empty, and therefore in particular there is some other point $w \in f ( U ) \cap f ( V )$ • So we have $z _ { 1 } \in U , z _ { 2 } \in V$ with $f ( z _ { 1 } ) = f ( z _ { 2 } )$ . But $z _ { 1 } \neq 0$ because $w \ne f ( 0 )$ , so this contradicts the fact that $f$ is injective on P .

Problem 11. Let $\Omega \subseteq \mathbb { C }$ be a non-empty open connected set.
If $f : \Omega \to \mathbb { C }$ is harmonic and $f ^ { 2 }$ is also harmonic, show that either f or $\overline { { f } }$ is holomorphic on Ω.

Solution.
Recall the Wirtinger derivates $\hat { \sigma } _ { z } = ( 1 / 2 ) ( \hat { \sigma } _ { x } - i \hat { \sigma } _ { y } )$ and $\hat { \sigma } _ { z } = ( 1 / 2 ) ( \hat { \sigma } _ { x } + i \hat { \sigma } _ { y } )$ . A straightforward computation verifies the identity $\Delta = 4 \hat { \sigma } _ { z } \hat { \sigma } _ { \overline { { z } } }$ . By hypothesis, $f ^ { 2 }$ is harmonic, so $\Delta f ^ { 2 } = 0$ . Putting this into the above identity and using the chain and product rules and the hypothesis that f is also harmonic, this reduces to $( \partial _ { z } f ) ( \bar { \partial } _ { \overline { { z } } } f ) = 0$ . Suppose $\overline { { f } }$ is not holomorphic.
Then there is a point in Ω at which $\partial _ { z } f \neq 0$ By continuity, $\partial _ { z } f$ is nonzero on an open ball, so $\partial _ { \overline { { z } } } f = 0$ on an open ball.
Since $f$ is harmonic, $\partial _ { \overline { { z } } }$ also is (because $\partial _ { x }$ and $\hat { \sigma } _ { y }$ both are).
But then we have a harmonic function on all of Ω which vanishes on an open ball.
In particular it has a local maximum on that open ball, so the maximum principle implies $\partial _ { \overline { { z } } } f$ is constant and therefore identically zero, so $f$ is holomorphic.

Problem 12. Let $\mathcal { F }$ be the family of functions $f$ holomorphic on D with

$$
\iint _ { x ^ { 2 } + y ^ { 2 } < 1 } | f ( x + i y ) | ^ { 2 } d x d y \ < \ 1 .
$$

Prove that for each compact subset $K \subseteq \mathbb { D }$ there is a constant A so that $| f ( z ) | < A$ for all $z \in K$ and all $f \in { \mathcal { F } }$

Solution.
See e.g. the first half of Fall 2014 $\# 1 0$

## 5 Spring 2011

Problem 1.

(a) Define what it means to say that $f _ { n }  f$ weakly in $L ^ { 2 } ( [ 0 , 1 ] )$ q.

(b) Suppose $f _ { n } \in L ^ { 2 } ( [ 0 , 1 ] )$ converge weakly to $f \in L ^ { 2 } ( [ 0 , 1 ] )$ and define ‘primitive’ functions

$$
F _ { n } ( x ) : = \int _ { 0 } ^ { x } f _ { n } ( t ) d t \quad { \mathrm { a n d } } \quad F ( x ) : = \int _ { 0 } ^ { x } f ( t ) d t .
$$

Show that $F _ { n } , F \in C ( [ 0 , 1 ] )$ and that $F _ { n } \to F$ uniformly on r0, 1s.

Solution.

(a) For every $\begin{array} { r } { g \in L ^ { 2 } ( [ 0 , 1 ] ) , \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f _ { n } ( x ) g ( x ) d x = \int _ { 0 } ^ { 1 } f ( x ) g ( x ) d x . } \end{array}$

(b) First, we know that weakly convergent sequences are bounded, so we can say $\| f _ { n } \| _ { L ^ { 2 } } \leqslant M$ for all $n .$ To show that $F _ { n }$ and $F$ are continuous, note that

$$
| F _ { n } ( x + h ) - F _ { n } ( x ) | \leqslant \int _ { x } ^ { x + h } | f _ { n } ( t ) | d t \leqslant \left( \int _ { x } ^ { x + h } | f _ { n } ( t ) | ^ { 2 } d t \right) ^ { 1 / 2 } \left( \int _ { x } ^ { x + h } 1 d t \right) ^ { 1 / 2 } \leqslant M | h | ^ { 1 / 2 } .
$$

Note that the above estimate for $| F _ { n } ( x + h ) - F _ { n } ( x ) |$ is independent of both n and $x ,$ so we have actually shown that $\left\{ F _ { n } \right\}$ is an equicontinuous family of functions.
A similar estimate shows $| F ( x + h ) - F ( x ) | \leq$ $| | \dot { f } | | _ { L ^ { 2 } } | h | ^ { 1 / 2 }$ , so F is also continuous.
Now we show $F _ { n } \to F$ uniformly.
First note that

$$
| F _ { n } ( x ) | \ \leqslant \ \int _ { 0 } ^ { x } | f _ { n } ( t ) | d t \ \leqslant \ \left( \int _ { 0 } ^ { x } | f _ { n } ( t ) | ^ { 2 } d t \right) ^ { 1 / 2 } x ^ { 1 / 2 } \ \leqslant \ M ,
$$

so $F _ { n }$ is also a uniformly bounded family.
To show that $F _ { n } \ \to \ F$ uniformly, it’s enough to show that any subsequence of $F _ { n }$ has a further subsequence converging uniformly to $F .$ . Let $F _ { n _ { k } }$ be any subsequence.
We have shown it is a uniformly bounded and equicontinuous family, so by Arzela-Ascoli it has a further subsequence converging uniformly to some function g. But note that for each $x ,$

$$
\operatorname* { l i m } _ { n \to \infty } F _ { n } ( x ) = \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { x } f _ { n } ( t ) d t = \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f _ { n } ( t ) \chi _ { [ 0 , x ] } ( t ) d t = \int _ { 0 } ^ { 1 } f ( t ) \chi _ { [ 0 , x ] } ( t ) d t = \int _ { 0 } ^ { x } f ( t ) d t = F ( x )
$$

by weak convergence because $\chi _ { [ 0 , x ] } \in L ^ { 2 } ( [ 0 , 1 ] )$ . Thus, since $F _ { n }$ converges pointwise to $F ,$ and $F _ { n _ { k } }$ has a subsequence converging uniformly to some $g _ { \mathrm { : } }$ , we must in fact have $g = F$ . Thus every subsequence $F _ { n _ { k } }$ has a further subsequence converging uniformly to $F ,$ so $F _ { n } \to F$ uniformly.
□

Problem 2. Let $f \in L ^ { 3 } ( \mathbb { R } )$ and $\phi ( x ) = \sin ( \pi x ) \cdot \chi _ { [ - 1 , 1 ] } ( x )$ . Show that

$$
f _ { n } ( x ) \ : = \ n \int f ( x - y ) \phi ( n y ) d y \to 0
$$

Lebesgue almost everywhere.

Solution.
Let $\phi _ { n } ( x ) = n \phi ( n x )$ . Let $g ( x ) = - \phi ( x ) \chi _ { [ - 1 , 0 ] }$ be the negative part of φ and let $h ( x ) = \phi ( x ) \chi _ { [ 0 , 1 ] }$ be the positive part.
Also define $g _ { n }$ and $h _ { n }$ similarly to $\phi _ { n }$ . Note that $\phi _ { n } ~ = ~ h _ { n } - g _ { n }$ so to show that $f * \phi _ { n } \to 0$ a.e. it’s enough to show that $f * g _ { n } , f * h _ { n } \to ( \pi / 2 ) f$ a.e. We show it for $h _ { n }$ and the argument

for $g _ { n }$ is exactly the same.
First note that $\displaystyle \int h _ { n } ( x ) d x = \int _ { 0 } ^ { 1 / n } \sin ( n \pi x ) d x = 2 / \pi$ . We have

$$
{ \begin{array} { r l } { \displaystyle { \Big | } ( f * h _ { n } ) ( x ) - { \frac { \pi } { 2 } } f ( x ) { \Big | } } & { = \ \displaystyle { \left| \int _ { 0 } ^ { 1 / n } f ( x - y ) n \sin ( n \pi y ) d y - \int _ { 0 } ^ { 1 / n } f ( x ) n \sin ( n \pi y ) d y \right| } } \\ & { \leqslant \ n \displaystyle { \int _ { 0 } ^ { 1 / n } | f ( x - y ) - f ( x ) | \sin ( n \pi y ) | d y } } \\ & { \leqslant \ n \displaystyle { \int _ { 0 } ^ { 1 / n } | f ( x - y ) - f ( x ) | d y } , } \end{array} }
$$

which goes to $0$ almost everywhere by the Lebesgue differentiation theorem $( f \in L _ { l o c } ^ { 1 }$ because $f \in L ^ { 3 } )$

Problem 3. Let $\mu$ be a Borel probability measure on R and define $f ( t ) = \int e ^ { i t x } d \mu ( x )$ . Suppose that

$$
\operatorname * { l i m } _ { t  0 } { \frac { f ( 0 ) - f ( t ) } { t ^ { 2 } } } ~ = ~ 0 .
$$

Show that $\mu$ is supported at 0.

Solution.
Rewrite the limit condition as

$$
\operatorname * { l i m } _ { t  0 } \int \frac { 1 - e ^ { i t x } } { t ^ { 2 } } d \mu ( x ) = 0 .
$$

Just looking at the real part of the above gives

$$
\operatorname * { l i m } _ { t \to 0 } \int \frac { 1 - \cos ( t x ) } { t ^ { 2 } } d \mu ( x ) \ = \ 0 .
$$

Since the integrand is positive for all $t , x ,$ by Fatou’s lemma we have

$$
0 ~ = ~ \operatorname* { l i m } _ { t \to 0 } \int { \frac { 1 - \cos ( t x ) } { t ^ { 2 } } } d \mu ( x ) ~ \geqslant ~ \int \operatorname* { l i m } _ { t \to 0 } { \frac { 1 - \cos ( t x ) } { t ^ { 2 } } } d \mu ( x ) ~ = ~ \int { \frac { 1 } { 2 } } x ^ { 2 } d \mu ( x ) ,
$$

and since the last term on the right is also non-negative, we have $\int x ^ { 2 } d \mu ( x ) \ = \ 0$ This immediately implies that $\mu$ is supported at 0 because if µ gave nonzero measure to $\mathbb { R } \backslash \{ 0 \}$ , it would have to give positive measure to some set of the form ş $\left( - \infty , - \delta \right] \cap \left[ \delta , \infty \right)$ for some $\delta > 0$ , and then we would have $\{ x ^ { 2 } d \mu ( x ) > \delta ^ { 2 } \mu ( ( - \infty , - \delta ] \cap [ \delta , \infty ) ) > 0 ,$ a contradiction.
□

Problem 4. Let $f _ { n } : [ 0 , 1 ] \to [ 0 , \infty )$ be Borel functions with

$$
\operatorname* { s u p } _ { n } \int _ { 0 } ^ { 1 } f _ { n } ( x ) \log ( 2 + f _ { n } ( x ) ) d x \ \leqslant \ M \ < \ \infty .
$$

Suppose $f _ { n }  f$ Lebesgue almost everywhere.
Show that $f \in L ^ { 1 }$ and $f _ { n }  f$ in $L ^ { 1 }$

Solution.
By Fatou’s lemma (since everything is positive) we have

$$
M \ \geqslant \ \operatorname* { l i m i n f } _ { n \to \infty } \int _ { 0 } ^ { 1 } f _ { n } ( x ) \log ( 2 + f _ { n } ( x ) ) d x \ \geqslant \ \int _ { 0 } ^ { 1 } f ( x ) \log ( 2 + f ( x ) ) d x \ \geqslant \ \log ( 2 ) \int _ { 0 } ^ { 1 } f ( x ) d x ,
$$

so $f \in L ^ { 1 }$ Now to show $f _ { n }  f$ in $L ^ { 1 }$ , we first want to establish the following claim: for all ş $\epsilon > 0$ there is $\delta > 0$ such that for any n and any $E \subseteq [ 0 , 1 ] , m ( E ) < \delta$ implies $\int _ { E } f ( x ) d x < \epsilon .$ Suppose this were not true,ş then there would be a sequence of sets $E _ { k }$ and functions $f _ { n _ { k } }$ with $m ( E _ { k } ) < 1 / k$ and $\int _ { E _ { k } } f _ { n _ { k } } \geqslant \epsilon$ . Then by Jensen’s inequality, since $t \mapsto t \log ( 2 + t )$ is convex, we would have

$$
\left( \frac { 1 } { m ( E _ { k } ) } \int _ { E _ { k } } f _ { n _ { k } } \right) \log { \left( 2 + \frac { 1 } { m ( E _ { k } ) } \int _ { E _ { k } } f _ { n _ { k } } \right) } \~ \leqslant ~ \frac { 1 } { m ( E _ { k } ) } \int _ { E _ { k } } f _ { n _ { k } } \log ( 2 + f _ { n _ { k } } ) \~ \leqslant ~ \frac { 1 } { m ( E _ { k } ) } M .
$$

Cancelling terms on both sides and using the fact that $t \mapsto t \log ( 2 + t )$ is also increasing, we $\mathrm { g e t }$

$$
M \ \geqslant \ \epsilon \log ( 2 + k \epsilon ) ,
$$

which is a contradiction for k large enough.
Thus the claim is established.
Now to finish the problem, fixş ş $\epsilon > 0$ By the previous claim we can pick $\delta > 0$ so that $m ( E ) < \delta$ implies $\int _ { E } f _ { n } < \epsilon$ for all n and $\int _ { E } f < \epsilon$ By Egorov’s theorem, we can find a set $E \subseteq [ 0 , 1 ]$ with $f _ { n }  f$ uniformly on $E ^ { c }$ and $m ( E ) < \delta$ . Then

$$
\int | f _ { n } - f | ~ \leqslant ~ \int _ { E ^ { c } } | f _ { n } - f | + \int _ { E } | f _ { n } | + \int _ { E } | f | ~ \leqslant ~ \int _ { E ^ { c } } | f _ { n } - f | + 2 \epsilon .
$$

First take $n \to \infty$ , then take $\epsilon  0$ , and we get the desired result.

Problem 5. (a) Show that $\ell ^ { \infty } ( \mathbb { Z } )$ contains continuum many functions $x _ { \alpha } : \mathbb { Z } \to$ R obeying $\| x _ { \alpha } \| _ { \ell ^ { \infty } } = 1$ and $| | x _ { \alpha } - x _ { \beta } | | _ { \rho \infty } \geqslant 1$ whenever $\alpha \neq \beta .$

(b) Deduce (assuming the axiom of choice) that the Banach space dual of $\ell ^ { \infty } ( \mathbb { Z } )$ cannot contain a countable dense subset.

(c) Deduce that $\ell ^ { 1 } ( \mathbb { Z } )$ is not reflexive.

Solution.
(a) For each subset $\alpha \subseteq \mathbb { Z } ,$ , let $x _ { \alpha } ( j ) = 1 \mathrm { ~ i f ~ } j \in \alpha$ and 0 otherwise.
Then each $| | x _ { \alpha } | | _ { \ell ^ { \infty } } = 1$ and for any two distinct subsets $\alpha \neq \beta$ , there is a point at which $x _ { \alpha }$ and $x _ { \beta }$ disagree, so $| | x _ { \alpha } - x _ { \beta } | | _ { \ell ^ { \infty } } \geqslant 1$ It’s standard that there are continuum many subsets of $\mathbb { Z } , \ \sqsupset$

(b) Part (a) shows that the dual of $\ell ^ { \infty }$ is not separable.
So it just follows from the general fact that if X is a Banach space and $X ^ { * }$ is separable, then X is also separable (see Fall 2014 $\# 6 )$ .

(c) Recall that the dual of $\ell ^ { 1 }$ is $\ell ^ { \infty }$ . If $\ell ^ { 1 }$ is separable, then $( \ell ^ { 1 } ) ^ { * * } \ = \ ( \ell ^ { \infty } ) ^ { * } \ = \ \ell ^ { 1 }$ , which is separable, so by part ${ \bf ( b ) } \ \ell ^ { \infty }$ is also separable, a contradiction.
□

Problem 6. Suppose $\mu$ and ν are finite positive (regular) Borel measures on $\mathbb { R } ^ { n }$ . Prove the existence and uniqueness of the Lebesgue decomposition: there are a unique pair of positive Borel measures $\mu _ { a }$ and $\mu _ { s }$ such that

$$
\mu \ = \ \mu _ { a } + \mu _ { s } , \mu _ { a } \ll \nu , \mu _ { s } \perp \nu .
$$

Solution.
First we show uniqueness.
Suppose that $\mu = \mu _ { a } + \mu _ { s } = \mu _ { a } ^ { \prime } + \mu _ { s } ^ { \prime }$ are two decompositions.
It’s enough to show that $\mu _ { s } = \mu _ { s } ^ { \prime }$ . Write $\mathbb { R } ^ { n } = X \cup Y = X ^ { \prime } \cup Y ^ { \prime }$ where $\nu ( Y ) = \nu ( Y ^ { \prime } ) = 0$ and $\mu _ { s } ( X ) = \mu _ { s } ^ { \prime } ( X ^ { \prime } ) 0 .$ By the absolute continuity of $\mu _ { a }$ and $\mu _ { a } ^ { \prime }$ , we see that $\mu _ { s } ( A ) = \mu _ { s } ^ { \prime } ( A )$ for any A satisfying $\nu ( A ) = 0$ . For a general set $E ,$ write

$$
E = ( E \cap X \cap X ^ { \prime } ) \cup ( E \cap Y \cap X ^ { \prime } ) \cup ( E \cap X \cap Y ^ { \prime } ) \cup ( E \cap Y \cap Y ^ { \prime } ) \ = : \ ( E \cap X \cap X ^ { \prime } ) \cup \tilde { E } .
$$

Note that since $\nu ( \tilde { E } ) = 0$ and $E \cap X \cap X ^ { \prime }$ is contained in both X and $X ^ { \prime }$ we have

$$
\mu _ { s } ( E ) \ = \ \mu _ { s } \big ( E \cap X \cap X ^ { \prime } \big ) + \mu _ { s } \big ( \widetilde { E } \big ) \ = \ \mu _ { s } ^ { \prime } \big ( E \cap X \cap X ^ { \prime } \big ) + \mu _ { s } ^ { \prime } \big ( \widetilde { E } \big ) \ = \ \mu _ { s } ^ { \prime } ( E ) .
$$

Thus the decomposition is unique.
Now we show existence.
Let $\lambda = \mu + \nu$ and note that since all of the measures involved are positive, ν is clearly absolutely continuous with respect to λ. Let $\textstyle f = { \frac { d \nu } { d \lambda } }$ be the Radon-Nikodym derivative, and note that $f \geqslant 0$ because the measures are positive.
Define $X = \{ x : f ( x ) \neq 0 \}$ and $Y = \{ x : f ( x ) = 0 \}$ . We define $\mu _ { s } ( E ) : = \mu ( E \cap Y )$ and $\mu _ { a } ( E ) : = \mu ( E \cap X )$ q. It’s clear that $\mu _ { s } + \mu _ { a } = \mu$ We need to show that $\mu _ { s }$ is singular to ν and $\mu _ { a }$ is absolutely continuous with respect to $\nu .$ For the singular part, note that $X , Y$ are disjoint, $\mathbb { R } ^ { n } = X \cup Y , \mu _ { s } ( X ) = 0$ by definition, and

$$
\nu ( Y ) ~ = ~ \int _ { Y } f d \lambda ~ = ~ 0
$$

by definition of X. This shows $\mu _ { s } \perp \nu .$ . For absolute continuity, suppose $\nu ( E ) = 0$ . Then we have

$$
0 ~ = ~ \nu ( E ) ~ = ~ \int _ { E } f d \lambda ~ = ~ \int _ { E } f d \mu + \int _ { E } f d \nu ~ = ~ \int _ { E } f d \mu ~ = ~ \int _ { E \cap X } f d \mu ~ = ~ \int _ { E \cap X } f d \mu ~ = ~ \int _ { E \cap X } f d \mu _ { a } ~
$$

because $\mu _ { s }$ vanishes on $X$ . But since $f$ is strictly positive on $E \cap X$ , the fact that $\int _ { E \cap X } f d \mu _ { a } = 0$ implies that $\mu _ { a } ( E \cap X ) = 0$ , which is the same as saying $\mu _ { a } ( E ) = 0$ by definition.
Thus $\mu _ { a } \ll \nu .$

Problem 7. Prove Goursat’s theorem: if $f : \mathbb { C } \to \mathbb { C }$ is complex differentiable, then for every triangle $T \subseteq \mathbb { C }$

$$
\oint _ { \partial T } f ( z ) d z \ = \ 0 .
$$

Solution.

Problem 10. Evaluate

$$
\operatorname* { s u p } \left\{ { \mathrm { R e } } f ^ { \prime } ( i / 2 ) : f : \mathbb { H } \to \mathbb { D } { \mathrm { ~ i s ~ h o l o m o r p h i c } } \right\} .
$$

Solution.
We can freely post-compose $f$ with a rotation, so it’s equivalent to find $| f ^ { \prime } ( i / 2 ) |$ instead of the real part.
Let f be any holmorphic function $\mathbb { H } \to \mathbb { D }$ . Let $\psi : \mathbb { D } \to \mathbb { D }$ be an automorphism sending $f ( i / 2 )$ to 0. Concretely, $\begin{array} { r } { \psi ( z ) = \frac { z - f ( i / 2 ) } { 1 - \overline { { f ( i / 2 ) } } z } } \end{array}$ . An easy calculation shows that

$$
\psi ^ { \prime } ( f ( i / 2 ) ) ~ = ~ \frac { 1 } { 1 - | f ( i / 2 ) | ^ { 2 } } .
$$

Let $\phi : \mathbb { D } $ H be a conformal map sending 0 to $i / 2$ Concretely we can take $\begin{array} { r } { \phi ( z ) = \frac { 1 } { 2 } \cdot \frac { - i ( z + 1 ) } { z - 1 } } \end{array}$ Another easy calculation shows that $\phi ^ { \prime } ( 0 ) = i$ . Now $\psi \circ f \circ \phi$ is a holomorphic function D to D sending 0 to 0, so by the Schwartz lemma we have

$$
1 \ \geqslant \ \left| ( \psi \circ f \circ \phi ) ^ { \prime } ( 0 ) \right| \ = \ \left| \psi ^ { \prime } ( f ( \phi ( 0 ) ) ) f ^ { \prime } ( \phi ( 0 ) ) \phi ^ { \prime } ( 0 ) \right| \ = \ \frac { 1 } { 1 - | f ( i / 2 ) | ^ { 2 } } | f ^ { \prime } ( i / 2 ) | \ \geqslant \ | f ^ { \prime } ( i / 2 ) | .
$$

Thus the supremum in question is at most 1. Finally note that taking $\begin{array} { r } { f ( z ) = \phi ^ { - 1 } ( z ) = \frac { 2 z - i } { 2 z + i } } \end{array}$ , a calculation shows that $f ^ { \prime } ( i / 2 ) = - i$ . So 1 is achieved and therefore is the desired supremum.

## 6 Fall 2011

Problem 1. Prove Egorov’s theorem, that is:

Consider a sequence of measurable functions $f _ { n } : [ 0 , 1 ] \to \mathbb { R }$ that converges Lebesgue almost everywhere to a measurable function $f : [ 0 , 1 ] \to \mathbb { R }$ Then for any $\epsilon > 0$ there exists a measurable set $E \subseteq [ 0 , 1 ]$ with measure $\lambda ( E ) < \epsilon$ such that $f _ { n }$ converges uniformly on $[ 0 , 1 ] \backslash E$

Solution.
Let Z be the measure zero set of x for which $f _ { n } ( x )  f ( x )$ and set $I = [ 0 , 1 ] \backslash Z$ . Define

$$
E _ { n } ( k ) \ : = \ \{ x \in I : | f _ { j } ( x ) - f ( x ) | < 1 / k { \mathrm { ~ f o r ~ a l l ~ } } j \geqslant n \} .
$$

Fix $\epsilon > 0$ . First we show a lemma: For each k there is an $N _ { k }$ such that Ť $\lambda ( E _ { N _ { k } } ( k ) ) > 1 - \epsilon 2 ^ { - k }$ . To see this, fix a k and note that by definition of pointwise convergence, we have $\begin{array} { r } { \bigcup _ { n = 1 } ^ { \infty } E _ { n } ( k ) = I . ~ \mathrm { S o } } \end{array}$ by continuity of measure from below we can pick $N _ { k }$ large enough so that $\lambda ( E _ { N _ { k } } ( k ) ) > \ddot { \lambda ( I ) } - \epsilon 2 ^ { - k } = 1 - \epsilon 2 ^ { - k }$ . This proves the lemma.

Now we upgrade to the full result.
Define $\begin{array} { r } { E : = \bigcup _ { k = 1 } ^ { \infty } E _ { N _ { k } } ( k ) ^ { c } } \end{array}$ . We have

$$
\lambda ( E ) ~ \leqslant ~ \sum _ { k = 1 } ^ { \infty } \lambda ( E _ { N _ { k } } ( k ) ^ { c } ) ~ < ~ \sum _ { k = 1 } ^ { \infty } \epsilon 2 ^ { - k } ~ = ~ \epsilon .
$$

We claim that $f _ { n }  f$ uniformly on $E ^ { c }$ . Fix $\alpha > 0$ . Pick k big enough so that $1 / k < \alpha$ . Then for any $x \in E ^ { c }$ , we have $x \in E _ { N _ { k } } ( k )$ , so n $\geqslant N _ { k }$ implies that $| f _ { n } ( x ) - f ( x ) | < 1 / k < \alpha$ for all $x \in E ^ { c }$ . Thus $f _ { n }  f$ uniformly on $E ^ { c } . \sqsupset$

## Problem 2.

(a) Let dσ denote surface measure on the unit sphere $S ^ { 2 } \subset \mathbb { R } ^ { 3 }$ . Note $\int d \sigma ( x ) = 4 \pi$ . For $\xi \in \mathbb { R } ^ { 3 }$ , compute

$$
\int _ { S ^ { 2 } } e ^ { i x \cdot \xi } d \sigma ( x ) ,
$$

where ¨ denotes the usual inner product on $\mathbb { R } ^ { 3 }$

(b) Using this, or otherwise, show that the mapping

$$
f \mapsto \int _ { S ^ { 2 } } \int _ { S ^ { 2 } } f ( x + y ) d \sigma ( x ) d \sigma ( y )
$$

extends uniquely from the space of all $C ^ { \infty }$ functions on $\mathbb { R } ^ { 3 }$ with compact support to a bounded linear functional on $L ^ { \dot { 2 } } ( \mathbb { R } ^ { 3 } )$ .

Solution.

(a) It is clear that the integral in question depends only on |ξ| (a simple proof could be given if necessary, using an orthogonal transformation and the change of variables formula).
Therefore, given the magnitude $c = | \xi |$ of ξ, we are free to choose $\xi$ so that the integral is as easy as possible to evaluate.
We choose $\xi = ( 0 , 0 , c )$ . Then

$$
\int _ { S ^ { 2 } } e ^ { i x \cdot \xi } d \sigma ( x ) = \int _ { S ^ { 2 } } \cos ( c x _ { 3 } ) d \sigma ( x ) + i \int _ { S ^ { 2 } } \sin ( c x _ { 3 } ) d \sigma ( x ) = \int _ { S ^ { 2 } } \cos ( c x _ { 3 } ) d \sigma ( x ) ,
$$

since sin is odd and $S ^ { 2 }$ is symmetric about the origin.
Using spherical coordinates, the last integral equals

$$
\begin{array} { l l l } { \displaystyle \int _ { S ^ { 2 } } \cos ( c x _ { 3 } ) d \sigma ( x ) = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { \pi } \cos ( c \cos \phi ) \cdot \sin \phi d \phi d \theta } \\ { \displaystyle \quad = - \frac { 2 \pi } { c } \sin ( c \cos \phi ) \Big | _ { 0 } ^ { \pi } } \\ { \displaystyle \quad = \frac { 4 \pi \sin c } { c } . } \\ { \displaystyle \quad = \frac { 4 \pi \sin | \xi | } { | \xi | } . } \end{array}
$$

(b) For $f \in C _ { c } ^ { \infty } ( \mathbb { R } ^ { 3 } )$ , define

$$
L ( f ) = \int _ { S ^ { 2 } } \int _ { S ^ { 2 } } f ( x + y ) d \sigma ( x ) d \sigma ( y ) .
$$

Since $C _ { c } ^ { \infty } ( \mathbb { R } ^ { 3 } )$ is dense in $L ^ { 2 } ( \mathbb { R } ^ { 3 } )$ , to show that L extends uniquely to a bounded linear functional on $L ^ { 2 } ( \mathbb { R } ^ { 3 } )$ it will be enough to prove a bound of the form $| L ( f ) | \leqslant C | | f | | _ { 2 }$ for all $f \in C _ { c } ^ { \infty } ( \mathbb { R } ^ { 3 } )$ (where $C$ is independent of $f )$ Since $f$ is smooth with compact support, it lies in the Schwartz space, and therefore Fourier inversion applies and gives

$$
f ( x ) = \int _ { \mathbb { R } ^ { 3 } } e ^ { 2 \pi i \xi \cdot x } { \hat { f } } ( \xi ) d \xi = \int _ { 0 } ^ { \infty } r ^ { 2 } \int _ { S ^ { 2 } } e ^ { 2 \pi i r x \cdot \xi } { \hat { f } } ( r \xi ) d \sigma ( \xi ) d r
$$

for all $x \in \mathbb { R } ^ { 3 }$ (Note that since $\hat { f }$ is in the Schwartz space as well, $\| \hat { f } \| _ { L ^ { \infty } ( r S ^ { 2 } ) }$ decays faster than any power of $r ,$ so the integral on the right is convergent.)
Therefore, by Fubini’s theorem and the calculation in (a),

$$
\begin{array} { r l } { \displaystyle L ( f ) = \int _ { S ^ { 2 } } \int _ { S ^ { 2 } } f ( x + y ) d \sigma ( x ) d \sigma ( y ) } \\ { \displaystyle } & { = \int _ { S ^ { 2 } } \int _ { S ^ { 2 } } \int _ { 0 } ^ { \infty } r ^ { 2 } \int _ { S ^ { 2 } } e ^ { 2 \pi i r ( x + y ) \cdot \xi } \hat { f } ( r \xi ) d \sigma ( \xi ) d r d \sigma ( x ) d \sigma ( y ) } \\ { \displaystyle } & { = \int _ { 0 } ^ { \infty } r ^ { 2 } \int _ { S ^ { 2 } } \hat { f } ( r \xi ) \int _ { S ^ { 2 } } e ^ { 2 \pi i r x \cdot \xi } d \sigma ( x ) \int _ { S ^ { 2 } } e ^ { 2 \pi i r y \cdot \xi } d \sigma ( y ) d \sigma ( \xi ) d r } \\ & { = \displaystyle \int _ { 0 } ^ { \infty } r ^ { 2 } \int _ { S ^ { 2 } } \hat { f } ( r \xi ) \left( \frac { \sin 2 \pi r } { r } \right) ^ { 2 } d \sigma ( \xi ) d r } \\ & { = \displaystyle \int _ { \mathbb { R } ^ { 3 } } \hat { f } ( \xi ) \left( \frac { \sin 2 \pi i | \xi | } { | \xi | } \right) ^ { 2 } d \xi . } \end{array}
$$

Now, by the Plancherel theorem, $\hat { f } \in L ^ { 2 } ( \mathbb { R } ^ { 3 } )$ and $| | { \hat { f } } | | _ { 2 } ~ = ~ | | f | | _ { 2 }$ . Moreover, $\begin{array} { r } { h ( \xi ) ~ = ~ \left( \frac { \sin 2 \pi | \xi | } { | \xi | } \right) ^ { 2 } } \end{array}$ is in $L ^ { 2 } ( \mathbb { R } ^ { 3 } )$ as well, since $h ( \xi ) ^ { 2 }$ is bounded near zero and decays like $| \xi | ^ { - 4 }$ near infinity.
Therefore, Cauchy-Schwarz implies

$$
| L ( f ) | \leqslant | | { \hat { f } } | | _ { 2 } | | h | | _ { 2 } = C | | f | | _ { 2 } ,
$$

as required.

Problem 3. Let $1 < p , q < \infty$ with $1 / p + 1 / q = 1$ . Let $f \in L ^ { p } ( \mathbb { R } ^ { 3 } )$ and $g \in L ^ { q } ( \mathbb { R } ^ { 3 } )$ . Show (a) that $f * g$ is continuous on $\mathbb { R } ^ { 3 }$ and (b) that $( f * g ) ( x ) \to 0 { \mathrm { ~ a s ~ } } | x | \to \infty$

Solution.
(a) Fix $\boldsymbol { x } \in \mathbb { R } ^ { 3 }$ . We estimate

$$
\begin{array} { r l } { | ( f * g ) ( x ) - ( f * g ) ( x + h ) | } & { = \ \displaystyle \left. \int _ { \mathbb { R } ^ { 3 } } ( f ( x - y ) g ( y ) - f ( x + h - y ) g ( y ) ) d y \right. } \\ & { \leqslant \ \displaystyle \int | g ( y ) | | f ( x + h - y ) - f ( x - y ) | d y } \\ & { \leqslant | | g | | _ { L ^ { q } } \left( \displaystyle \int | f ( x + h - y ) - f ( x - y ) | ^ { p } d y \right) ^ { 1 / p } } \\ & { = \ | | g | | _ { L ^ { q } } \left( \displaystyle \int | f ( y + h ) - f ( y ) | ^ { p } d y \right) ^ { 1 / p } . } \end{array}
$$

So it suffices to show that $\left( \int | f ( y + h ) - f ( y ) | ^ { p } d y \right) ^ { 1 / p } \to 0 { \mathrm { ~ a s ~ } } | h | \to 0$ . This is just the $L ^ { p }$ continuity of the translation operator, a proof of which is reproduced below.

For $f \in L ^ { p }$ define $\tau _ { h } f ( y ) \ = \ f ( y + h )$ . We want to show that $| | \tau _ { h } f - f | | _ { L ^ { p } } \to 0$ as $| h |  0$ First suppose that $\phi \in { \cal C } _ { c } ( \mathbb { R } ^ { 3 } )$ Let $S \ = \ \{ x \ \in \ \mathbb { R } ^ { 3 }$ : dist $( x , \operatorname { s u p p } ( \phi ) ) \leqslant 1 \}$ and let $M = \lambda _ { 3 } ( S ) < \infty$ . By uniform continuity of φ, let $| h | < 1$ be small enough so that $| \tau _ { h } \phi ( x ) - \phi ( x ) | < \epsilon$ for all $x \in \mathbb { R } ^ { 3 }$ . Then

$$
| | \tau _ { h } \phi - \phi | | _ { L ^ { p } } ^ { p } \ \leqslant \ \epsilon ^ { p } M ,
$$

so the result is true for $C _ { c } ( \mathbb { R } ^ { 3 } )$ functions.
For general $f \in L ^ { p } ( \mathbb { R } ^ { 3 } )$ q, a standard density argument works: fix $\epsilon > 0$ and pick $\phi \in C _ { c } ( \mathbb { R } ^ { 3 } )$ with $| | f - \phi | | _ { L ^ { p } } < \epsilon$ . Then

$$
\left. \left. \tau _ { h } f - f \right. \right. _ { L ^ { p } } \leqslant \left. \left. \tau _ { h } f - \tau _ { h } \phi \right. \right. _ { L ^ { p } } + \left. \left. \tau _ { h } \phi - \phi \right. \right. _ { L ^ { p } } + \left. \left. \phi - f \right. \right. _ { L ^ { p } } < 2 \epsilon + \left. \left. \tau _ { h } \phi - \phi \right. \right. _ { L ^ { p } } .
$$

Take $| h |  0$ and then $\epsilon \to 0$ and the result follows.

(b) Note that if $f , g$ have compact support then $f * g$ also does.
Pick sequences $f _ { n } , g _ { k }$ with $f _ { n }  f$ in $L ^ { p } , g _ { k } \to g$ in $L ^ { q } , \left| \left| f _ { n } \right| \right| _ { L ^ { p } } \leqslant \left| \left| f \right| \right| _ { L ^ { p } } , \left| \left| g _ { k } \right| \right| _ { L ^ { p } } \leqslant \left| \left| g \right| \right| _ { L ^ { p } }$ , and each $f _ { n } , g _ { k }$ has compact support (e.g. just cut off f and g at bigger and bigger balls).
Fix $\epsilon > 0$ and pick n, k big enough so that $\| f _ { n } - f \| _ { L ^ { p } } , \| g _ { k } - g \| _ { L ^ { p } } < \epsilon .$ Then for any $x \in \mathbb { R } ^ { 3 }$ we have

$$
\begin{array} { r c l } { | ( f * g ) ( x ) | } & { \leqslant } & { | ( f _ { n } * g _ { k } ) ( x ) | + | ( ( f - f _ { n } ) * g _ { k } ) ( x ) | + | ( f * ( g - g _ { k } ) ) ( x ) | } \\ & { \leqslant } & { | ( f _ { n } * g _ { k } ) ( x ) | + | | ( f - f _ { n } ) * g _ { k } | | _ { L ^ { \infty } } + | | f * ( g - g _ { k } ) | | _ { L ^ { \infty } } } \\ & { \leqslant } & { | ( f _ { n } * g _ { k } ) ( x ) | + \epsilon \left| | g | \right| _ { L ^ { q } } + \epsilon \left| | f | \right| _ { L ^ { p } } . } \end{array}
$$

Take $| x | \to \infty$ and conclude lim $_ { \cdot | x | \to \infty } ( f \ast g ) ( x ) \leqslant \epsilon ( | | f | | _ { L ^ { p } } + | | g | | _ { L ^ { q } } )$ , then take $\epsilon \to 0$ to get the desired result.
□

Problem 4. Let $f \in C ^ { \infty } ( [ 0 , \infty ) \times [ 0 , 1 ] )$ such that

$$
\int _ { 0 } ^ { \infty } \int _ { 0 } ^ { 1 } | \partial _ { t } f ( t , x ) | ^ { 2 } ( 1 + t ^ { 2 } ) d x d t < \infty .
$$

Prove that there exists a function $g \in L ^ { 2 } ( [ 0 , 1 ] )$ such that $f ( t , \cdot )$ converges to $g ( \cdot )$ in $L ^ { 2 } ( [ 0 , 1 ] )$ as $t \to \infty ,$

Solution.
(There may be ways to make this proof more efficient, but it seems correct as far as I can tell.)
For each $t , f ( \cdot , t )$ is in $L ^ { 2 } ( [ 0 , 1 ] )$ , so by Parseval’s theorem there exist complex numbers $a _ { n } ( t )$ such that

$$
f ( x , t ) = \sum _ { n \in \mathbb { Z } } a _ { n } ( t ) e ^ { 2 \pi i n x }
$$

in $L ^ { 2 } ( [ 0 , 1 ] )$ , where $\begin{array} { r } { \sum _ { n } | a _ { n } ( t ) | ^ { 2 } = | | f ( \cdot , t ) | | _ { 2 } < \infty } \end{array}$ . By Parseval again it is enough to prove the existence of a sequence $\{ b _ { n } \} _ { n \in \mathbb { Z } } \in l ^ { 2 } ( \mathbb { Z } )$ such that

$$
\sum _ { n \in \mathbb { Z } } | a _ { n } ( t ) - b _ { n } | ^ { 2 } \to 0
$$

as $t \to \infty ;$ the function $\begin{array} { r } { g ( x ) \sim \sum _ { n } b _ { n } e ^ { 2 \pi i n x } } \end{array}$ will then be the desired limit in $L ^ { 2 } ( [ 0 , 1 ] )$ q. By completeness of $l ^ { 2 } ( \mathbb { Z } )$ , this is the same as showing that $\{ a _ { n } ( t ) \}$ is Cauchy in $l ^ { 2 } ( \mathbb { Z } )$ as $t \to \infty$ . In other words, given $\epsilon > 0$ , we want to be able to find $T > 0$ so that $s , t > T$ implies

$$
\sum _ { n \in \mathbb { Z } } | a _ { n } ( t ) - a _ { n } ( s ) | ^ { 2 } < \epsilon .
$$

Assume for the moment that the coefficients $a _ { n } ( t )$ are continuously differentiable with respect to t and that

$$
\partial _ { t } f ( x , t ) = \sum _ { n \in \mathbb { Z } } a _ { n } ^ { \prime } ( t ) e ^ { 2 \pi i n x }
$$

in $L ^ { 2 } ( [ 0 , 1 ] )$ for each t. Then by assumption, we have

$$
\begin{array} { r } { \displaystyle \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { 1 } | \partial _ { t } f ( t , x ) | ^ { 2 } ( 1 + t ^ { 2 } ) d x d t = \int _ { 0 } ^ { \infty } \left( \sum _ { n \in \mathbb { Z } } | a _ { n } ^ { \prime } ( t ) | ^ { 2 } \right) \left( 1 + t ^ { 2 } \right) d t } \\ { \displaystyle = \sum _ { n \in \mathbb { Z } } \int _ { 0 } ^ { \infty } | a _ { n } ^ { \prime } ( t ) | ^ { 2 } ( 1 + t ^ { 2 } ) d t < \infty } \end{array}\tag{1}
$$

(using the monotone convergence theorem to interchange the sum and integral).
Since each $a _ { n } ( t )$ is $C ^ { 1 }$ , we have

$$
a _ { n } ( s ) - a _ { n } ( t ) = \int _ { t } ^ { s } a _ { n } ^ { \prime } ( \tau ) d \tau .
$$

Consequently, by Cauchy-Schwarz

$$
\begin{array} { r l } { \displaystyle \sum _ { n \in \mathbb { Z } } \vert a _ { n } ( s ) - a _ { n } ( t ) \vert ^ { 2 } = \displaystyle \sum _ { n \in \mathbb { Z } } \left. \int _ { t } ^ { s } a _ { n } ^ { \prime } ( \tau ) d \tau \right. ^ { 2 } } & { } \\ { \displaystyle \leqslant \sum _ { n \in \mathbb { Z } } \displaystyle \int _ { t } ^ { \infty } \tau ^ { 2 } \vert a _ { n } ^ { \prime } ( \tau ) \vert ^ { 2 } d \tau \displaystyle \int _ { t } ^ { \infty } \frac { d \tau } { \tau ^ { 2 } } } & { ( \mathrm { a s s u m i n g } \ s > t ) } \\ { \displaystyle } & { \displaystyle \lesssim \sum _ { n \in \mathbb { Z } } \displaystyle \int _ { t } ^ { \infty } \vert a _ { n } ^ { \prime } ( \tau ) \vert ^ { 2 } ( 1 + \tau ^ { 2 } ) d \tau . } \end{array}
$$

But by (1) above, this sum goes to 0 as $t  \infty$ . Hence, $\{ a _ { n } ( t ) \} _ { n }$ is Cauchy in $l ^ { 2 } ( \mathbb { Z } )$ as $t  \infty$ , and so $f ( \cdot , t )  g ( \cdot )$ in $L ^ { 2 } ( [ 0 , 1 ] )$ as $t \to \infty$

Now we just have to justify the continuous differentiability of the coefficients ř $a _ { n } ( t )$ and the fact that $\partial _ { t } f ( x , t )$ equals $\begin{array} { r } { \sum _ { n } a _ { n } ^ { \prime } ( t ) e ^ { 2 \pi i n \bar { x } } } \end{array}$ in $L ^ { 2 } ( [ 0 , 1 ] )$ . For any t, let $h > 0 ;$ then by smoothness of f on $[ 0 , \infty ) \times [ 0 , 1 ]$ ,

$$
{ \frac { f ( x , t + h ) - f ( x , t ) } { h } } = \sum _ { n \in \mathbb { Z } } { \frac { a _ { n } ( t + h ) - a _ { n } ( t ) } { h } } e ^ { 2 \pi i n x } \to { \hat { \sigma } } _ { t } f ( x , t )
$$

as $h  0$ , uniformly on $[ 0 , 1 ]$ , and hence also in $L ^ { 2 } ( [ 0 , 1 ] )$ . But $\partial _ { t } f ( x , t )$ is also in $L ^ { 2 } ( [ 0 , 1 ] )$ , and hence has an $L ^ { 2 } .$ -Fourier series

$$
\hat { \sigma } _ { t } f ( x , t ) = \sum _ { n \in \mathbb { Z } } \alpha _ { n } ( t ) e ^ { 2 \pi i n x } .
$$

Thus, by Parseval’s theorem,

$$
\sum _ { n \in \mathbb { Z } } \left| { \frac { a _ { n } ( t + h ) - a _ { n } ( t ) } { h } } - \alpha _ { n } ( t ) \right| ^ { 2 } \to 0
$$

as $h  0$ , which implies $\begin{array} { r } { \frac { a _ { n } ( t + h ) - a _ { n } ( t ) } { h } \ \to \ \alpha _ { n } ( t ) } \end{array}$ for each n. Thus, $a _ { n } ( t )$ is differentiable with derivative $a _ { n } ^ { \prime } ( t ) = \alpha ( t )$ , and

$$
\partial _ { t } f ( x , t ) = \sum _ { n \in \mathbb { Z } } a _ { n } ^ { \prime } ( t ) e ^ { 2 \pi i n x }
$$

in $L ^ { 2 } ( [ 0 , 1 ] )$ , as desired.
The same argument applied to $\begin{array} { r } { \sum _ { n } a _ { n } ^ { \prime } ( t ) e ^ { 2 \pi i n x } } \end{array}$ shows that the $a _ { n } ^ { \prime } ( t )$ are themselves differentiable, and hence continuous; so the $a _ { n } ( t )$ are continuously differentiable, as required.

Problem 5. For $f \in L ^ { 1 } ( \mathbb { R } )$ , recall the Hardy-Littlewood maximal function

$$
M f ( x ) : = \operatorname* { s u p } _ { h > 0 } { \frac { 1 } { 2 h } } \int _ { x - h } ^ { x + h } | f ( y ) | d y .
$$

Prove there is a constant A such that for any $\alpha > 0$

$$
\lambda \{ x \in \mathbb { R } : M f ( x ) > \alpha \} \ \leqslant \ \frac { A } { \alpha } \left. \vert f \vert \vert _ { L ^ { 1 } } . \right.
$$

If you use a covering lemma, you should prove it.

Solution.
Fix $\alpha > 0$ and let $E = \left\{ x \in \mathbb { R } : M f ( x ) > \alpha \right\}$ . For each $x \in E$ , by definition of $M f$ there is a radius $r _ { x }$ such that

$$
\int _ { x - r _ { x } } ^ { x + r _ { x } } | f | ~ > ~ 2 \alpha r _ { x } .
$$

Note the above implies we must have $r _ { x } < | | f | | _ { L ^ { 1 } } / ( 2 \alpha )$ for each $x \in E .$ . Set $I _ { x } = \left( x - r _ { x } , x + r _ { x } \right)$ . Since the radii are uniformly bounded, we may apply the Vitali covering lemma to Ť $\{ I _ { x } \} _ { x \in E }$ to obtain a countable disjoint subcollection $I _ { j } = ( x _ { j } - r _ { j } , x _ { j } + r _ { j } )$ with $E \subseteq \bigcup _ { j = 1 } ^ { \infty } 5 I _ { j }$ . Thus we have

$$
\lambda ( E ) \ \leqslant \ \sum _ { j = 1 } ^ { \infty } \lambda ( 5 I _ { j } ) \ = \ 5 \sum _ { j = 1 } ^ { \infty } 2 r _ { j } \ \leqslant \ \frac { 5 } { \lambda } \sum _ { j = 1 } ^ { \infty } \int _ { x _ { j } - r _ { j } } ^ { x _ { j } + r _ { j } } | f | \ \leqslant \ \frac { 5 } { \lambda } \left| | f | \right| _ { L ^ { 1 } }
$$

because the intervals $I _ { j }$ are pairwise disjoint.
All that remains is to prove the Vitali covering lemma.

Let $\left\{ I _ { \alpha } \right\}$ be a collection of open balls with uniformly bounded radius.
Let $R = \mathrm { s u p } _ { \alpha } \mathrm { r a d } ( I _ { \alpha } )$ Let $\mathcal { F } _ { 1 }$ be the collection of all balls $I _ { \alpha }$ with radii in $( R / 2 , R ]$ . Let $\boldsymbol { B } _ { 1 }$ be a maximal pairwise disjoint subcollection of $\mathcal { F } _ { 1 }$ (a standard Zorn’s lemma argument shows that this exists).
Now let $\mathcal { F } _ { 2 }$ be the subcollection of all balls $I _ { \alpha }$ which are disjoint from every element of $\boldsymbol { B } _ { 1 }$ and have radii in $( R / 4 , R / 2 ]$ , and let $B _ { 2 }$ be a maximal pairwise disjoint subcollection of $\mathcal { F } _ { 2 }$ (same deal with Zorn’s lemma).
Inductively, we may construct $\mathcal { F } _ { n }$ to be the collection of all balls $I _ { \alpha }$ which do not intersect any ball in $\smash { B _ { 1 } \cup . . . \cup B _ { n - 1 } }$ and have radii in $( R / 2 ^ { n } , R / 2 ^ { n - 1 } ]$ , and let $B _ { n }$ be a maximal disjoint subcollection of $\mathcal { F } _ { n }$ . Let $\textstyle B = \bigcup _ { n = 1 } ^ { \infty } B _ { n }$ . It’s clear that B is a pairwise disjoint (and therefore countable) subcollection of the $I _ { \alpha }$ . Consider some $I _ { \alpha } \notin B .$ We have rad $\lfloor ( I \alpha ) \in ( R / 2 ^ { n } , R / 2 ^ { n - 1 } ]$ for some n. By the maximality of $B _ { n }$ , it must be the case that $I _ { \alpha }$ intersects some $I _ { \beta } \in B _ { 1 } \cup . . . B _ { n }$ So rad $( I _ { \beta } ) > R / 2 ^ { n } \geqslant ( 1 / 2 )$ radpIαq.
Thus $\boldsymbol { B }$ has the property that any $I _ { \alpha } \notin B$ intersects some Ť $I _ { \beta } \in B$ with radŤ $. ( I _ { \beta } ) > R / 2 ^ { n } \geqslant ( 1 / 2 ) \operatorname { r a d } ( I _ { \alpha } )$ . Thus a simple triangle inequality shows that $I _ { \alpha } \subseteq 5 I _ { \beta }$ so $\textstyle \bigcup _ { \alpha } { \dot { I } } _ { \alpha } \subseteq \bigcup _ { I \in B } 5 I$

Problem 6. Let $( X , d )$ be a compact metric space.
Let $\mu _ { n }$ be a sequence of positive Borel measures on X that converge in the weak-˚ topology to a finite positive Borel measure $\mu ,$ that is

$$
\int _ { X } f d \mu _ { n } \ \to \ \int _ { X } f d \mu \quad { \mathrm { f o r ~ a l l ~ } } f \in C ( X ) .
$$

Show that

$$
\mu ( K ) \ \geqslant \ \operatorname* { l i m } _ { n \to \infty } \operatorname { \mu } _ { n } ( K ) \quad { \mathrm { f o r ~ a l l ~ c o m p a c t ~ s e t s ~ } } K \subseteq X .
$$

Solution.
Fix K compact.
First we show that the characteristic function $\chi _ { K }$ is upper semicontinuous.
We need to show

$$
\chi _ { K } ( x _ { 0 } ) ~ \geqslant ~ \operatorname* { l i m } _ { x  x _ { 0 } } \chi _ { K } ( x )
$$

for any $x _ { 0 } \in X$ . If $x _ { 0 } \in K$ , then the inequality obviously holds because $\chi _ { K } ( \boldsymbol { x } _ { 0 } )$ is equal to the maximum value χK can take.
If $x _ { 0 } \notin K$ , then since $K ^ { c }$ is open there is a neighborhood around $x _ { 0 }$ on which $\chi _ { K } = 0$ so $\begin{array} { r } { \chi _ { K } ( x _ { 0 } ) = 0 = \operatorname* { l i m } _ { x  x _ { 0 } } \chi _ { K } ( x ) } \end{array}$ . Thus $\chi _ { K }$ is upper semicontinuous.

Now we prove the inequality

$$
\int f d \mu \geqslant \operatorname* { l i m } _ { n \to \infty } f d \mu _ { n }
$$

for all upper semicontinuous $f : X \to \mathbb { R }$ . This finishes the problem by taking $f = \chi _ { K }$ . It’s equivalent to show

$$
\int f d \mu \leqslant \operatorname* { l i m i n f } _ { n \to \infty } f d \mu _ { n }
$$

whenever $f$ is lower semicontinuous (by just taking the negative).
Fix such an $f .$ Since X is compact, f achieves a minimum on X (this is a property of lower semicontinuous functions).
By an equivalent definition of lower semicontinuous, we have a sequence $\phi _ { k }$ of continuous functions with $\phi _ { k } ~ \leqslant ~ \phi _ { k + 1 }$ and $\phi _ { k } \ \to \ f$ pointwise.
By replacing $\phi _ { k }$ by ma $\overline { { \cdot } } ( \phi _ { k } , \operatorname* { m i n } ( f ) )$ if necessary, we may assume that all of the $\phi _ { k }$ are uniformly bounded from below.
We have

$$
\int _ { X } \phi _ { k } d \mu _ { n } \ \leqslant \ \int _ { X } f d \mu _ { n }
$$

for any $k , n$ . Taking the liminf as $n \to \infty$ , since $\phi _ { k }$ is continuous we $\mathrm { g e t }$

$$
\int _ { X } \phi _ { k } d \mu \ \leqslant \ \operatorname* { l i m } _ { n \to \infty } \int _ { X } f d \mu _ { n }
$$

for every k. Finally, since the right side is independent of $k ,$ apply the Monotone Convergence theorem to get the desired conclusion.
□

Problem 7. Compute $\int _ { 0 } ^ { \infty } { \frac { \cos ( x ) } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x$

Solution.
Let $\begin{array} { r } { f ( z ) = \frac { e ^ { i z } } { ( 1 + z ^ { 2 } ) ^ { 2 } } } \end{array}$ Integrate f around a semicircle of radius $R$ in the upper half plane.
It’s easy to show the contribution from the curved part of the contour vanishes as $R \to \infty$ . The real part of the integral over the straight part is twice the desired integral because the original function is even.
$f$ has a double pole at $z = i$ . Take the residue

$$
{ \mathrm { R e s } } ( f , i ) ~ = ~ \operatorname* { l i m } _ { z  i } { \frac { d } { d z } } [ ( z - i ) ^ { 2 } f ( z ) ] ~ = ~ { \frac { - i } { 2 e } } .
$$

Set the two things equal to each other using the residue theorem and solve.
The answer is $\pi / 2 e$

Problem 8. Determine the number of solutions to

$$
z - 2 - e ^ { - z } = 0
$$

with z in the right half-plane $H = \left\{ z \in \mathbb { C } : \mathrm { R e } z > 0 \right\}$

Solution.
Any such z satisfies $z = 2 + e ^ { - z }$ , and therefore $| z | = | 2 + e ^ { - z } | \leqslant 2 + | e ^ { - z } | < 3$ , since Re $z > 0$ Hence, we can restrict z to the half-disc $U = H \cap \left\{ | z | < 3 \right\}$ Consider the functions $f ( z ) = z - 2$ and $g ( z ) = - e ^ { - z }$ on $\partial U$ . It is easy to see that $\vert g \vert < \vert f \vert$ on $\partial U$ , since $| g | = e ^ { - x } < 1$ everywhere in H, whereas $| z - 2 | > 1$ for all $x \in \partial U$ except at $z = 3$ , at which point $| g ( z ) | = e ^ { - 3 } < 1$ Therefore, by Rouche’s theorem, $f$ and $f + g = z - 2 - e ^ { - z }$ have the same number of zeros in $U ;$ since $f$ clearly has one zero in $U _ { ; }$ , it follows that

$$
z - 2 - e ^ { - z } = 0
$$

has exactly one solution in $H . \quad \sqcup$

Problem 9. Suppose that $f$ is a holomorphic function in the punctured open unit disc $\mathbb { D } ^ { * } : = \mathbb { D } \backslash \{ 0 \}$ such that

$$
\int _ { \mathbb { D } ^ { * } } | f ( z ) | ^ { 2 } d A ( z ) < \infty
$$

where integration is with respect to two dimensional Lebesgue measure.
Show that f has a holomorphic extension to the unit disc D.

Solution.
Let $g ( z ) ~ = ~ z f ( z )$ . It’s clear that g is also holomorphic on $\mathbb { D } ^ { * }$ $\mathrm { B y }$ the mean value property, for $z \in \mathbb { D } ^ { * }$ fixed we have

$$
\begin{array} { r l } { | g ( z ) | \ : = \ : \frac { 1 } { \pi ( 1 / 2 | z | ) ^ { 2 } } \displaystyle \left| \int _ { B ( z , 1 / 2 | z | ) } w f ( w ) d A ( w ) \right| \lesssim } & { | z | ^ { - 2 } \left( \displaystyle \int _ { B ( z , 1 / 2 | z | ) } | w | ^ { 2 } d A ( w ) \right) ^ { 1 / 2 } \left( \displaystyle \int _ { B ( z , 1 / 2 | z | ) } | f ( w ) | ^ { 2 } d A ( w ) \right) ^ { 1 / 2 } } \\ { \lesssim } & { | z | ^ { - 2 } \left( \displaystyle \int _ { B ( 0 , 3 / 2 | z | ) } | w | ^ { 2 } d A ( w ) \right) ^ { 1 / 2 } \lesssim | z | ^ { - 2 } \left( \displaystyle \int _ { 0 } ^ { 3 / 2 | z | } \displaystyle \int _ { 0 } ^ { 2 \pi } r ^ { 2 } r d \theta d r \right) ^ { 1 / 2 } \lesssim | z | ^ { - 2 } \left( \displaystyle \int _ { 0 } ^ { 3 / 2 | z | } r ^ { 3 } d r \right) ^ { 1 / 2 } } \\ & { \lesssim | z | ^ { - 2 } \left( ( \frac { 3 } { 2 } | z | ) ^ { 4 } \right) ^ { 1 / 2 } \lesssim 1 . } \end{array}
$$

Thus $g$ is bounded and holomorphic in the punctured disc $\mathbb { D } ^ { * }$ , which means that the singularity at 0 must be removable.
$\mathrm { S o } ~ z f ( z )$ has a removable singularity at 0, which implies that the singularity of $f$ at 0 is either removable or a simple pole.
But if f has a simple pole at zero, then there is a constant ş $C > 0$ and a neighborhood of 0 on which $| f ( z ) | \geqslant C | z | ^ { - 1 }$ , which contradicts the fact that $\int _ { \mathbb { D } ^ { * } } | f ( z ) | ^ { 2 } d A ( z ) ~ < ~ \infty$ . So f has a removable singularity at 0 and therefore can be extended to a holomorphic function on D. □

Problem 10. Let $\Omega \subsetneq \mathbb { C }$ be a simply connected domain and $f : \Omega \to \Omega$ be a holomorphic mapping.\
Suppose there are points $z _ { 1 } \neq z _ { 2 }$ with $f ( z _ { 1 } ) = z _ { 1 }$ and $f ( z _ { 2 } ) = z _ { 2 }$ . Show that f is the identity on Ω.

Solution.
We need to assume f is conformal, otherwise it isn’t true (as a counterexample take $\Omega = B ( 0 , 2 )$ and $f ( z ) = z ^ { 2 }$ , then 0 and 1 are both fixed points).
By the Riemann mapping theorem, let $T : \Omega \to { \mathbb { D } }$ be a conformal map.
Then $\phi = T f T ^ { - 1 } : \mathbb { D } \to \mathbb { D }$ is a conformal map with $\phi ( \alpha _ { 1 } ) = \alpha _ { 1 } , \phi ( \alpha _ { 2 } ) = \alpha _ { 2 }$ and $\alpha _ { 1 } \neq \alpha _ { 2 }$ (take $\alpha _ { j } = T ( z _ { j } ) )$ . Let $\psi$ be an automorphism of D that sends α1 to 0. Then we have $\psi ( \phi ( \psi ^ { - 1 } ( 0 ) ) ) = 0 ;$ so the Schwartz lemma applies to $\psi \phi \psi ^ { - 1 }$ . But note also that $\psi ( \phi ( \psi ^ { - 1 } ( \psi ( \alpha _ { 2 } ) ) ) ) ) = \psi ( \alpha _ { 2 } )$ . So equality holds in the Schwartz lemma (actual equality, not just equality in absolute value), so $\psi \phi \psi ^ { - 1 }$ is the identity, which implies φ is the identity, which implies $f$ is the identity.

Problem 11. Let $f : \mathbb { C } \to \mathbb { C }$ be a holomorphic function with $f ( z ) ~ \neq ~ 0$ for all $z \in \mathbb { C }$ . Define $U =$ $\{ z \in \mathbb { C } : | f ( z ) | < 1 \}$ . Show that all connected components of U are unbounded.

Solution.
Since f is nonvanishing, $1 / f$ is also entire.
First note that U is clearly an open set because it’s the preimage of $( 0 , 1 )$ under the continuous function $| f ( z ) |$ . Suppose that Ω were a bounded connected component of $U .$ Note that Ω is also open: let $z \in \Omega$ and let B be an open ball centered at z contained in U. If B were not contained in $\Omega ,$ , then there would be $w \in B$ where w belongs to a different connected component of U. But z and w can be joined by a path lying in U, so they must be in the same connected component.
Thus Ω is a bounded connected open set, i.e. a region on which the maximum principle can be applied.
First note that by continuity and by the fact that $\partial \Omega$ is disjoint from Ω, we must have $| f | = 1$ on BΩ. Thus $| 1 / f | = 1$ on BΩ also.
So by the maximum principle, we have $| 1 / f | \leqslant 1$ throughout Ω, implying $| f | \geqslant 1$ throughout Ω. But $| f | < 1$ in Ω by definition, which is a contradiction.
□

Problem 12. A holomorphic function $f : \mathbb { C } \to \mathbb { C }$ is said to be of exponential type if there are constants $c _ { 1 } , c _ { 2 } > 0$ such that

$$
| f ( z ) | \ \leqslant \ c _ { 1 } e ^ { c _ { 2 } | z | } \quad { \mathrm { f o r ~ a l l ~ } } z \in \mathbb { C } .
$$

Show that f is of exponential type if and only if $f ^ { \prime }$ is of exponential type.

Solution.
First suppose f is of exponential type.
For any z, the Cauchy estimates give

$$
| f ^ { \prime } ( z ) | ~ \leqslant ~ \frac { 1 } { R } \operatorname* { s u p } _ { | w - z | = R } | f ( w ) | ~ \leqslant ~ \frac { 1 } { R } c _ { 1 } e ^ { c _ { 2 } ( | z | + R ) }
$$

for any $R > 0$ . Pick $R = 1$ , we get

$$
| f ^ { \prime } ( z ) | \ \leqslant \ c _ { 1 } e ^ { c _ { 2 } ( | z | + 1 ) } \ = \ c _ { 1 } e ^ { c _ { 2 } } e ^ { c _ { 2 } | z | } ,
$$

so $f$ is of exponential type.

Now suppose $f ^ { \prime }$ is of exponential type.
For any z we can write

$$
f ( z ) ~ = ~ f ( 0 ) + \int _ { \gamma } f ( w ) d w
$$

where $\gamma$ is a straight line from $0 \ \mathrm { t o } \ z . \ \mathrm { S o }$ we have

$$
| f ( z ) | \ \leqslant \ | f ( 0 ) | + | z | \operatorname* { s u p } _ { w \in \gamma } | f ^ { \prime } ( w ) | \ \leqslant \ | f ( 0 ) | + | z | c _ { 1 } e ^ { c _ { 2 } | z | } \ \leqslant \ ( | f ( 0 ) | + c _ { 1 } ) e ^ { ( c _ { 2 } + 1 ) | z | } ,
$$

so $f$ is of exponential type.

## 7 Spring 2012

Problem 1. $f _ { n } \in L ^ { 3 } ( [ 0 , 1 ] )$ . True or false:

(a) If $f _ { n }  f$ almost everywhere then a subsequence converges to $f$ in $L ^ { 3 }$

(b) $\mathrm { I f } \ f _ { n } \to f \ \mathrm { i n } \ L ^ { 3 }$ then a subsequence converges almost everywhere.

(c) If $f _ { n }  f$ in measure then the sequence converges to $f$ in $L ^ { 3 }$

(d) If $f _ { n } \to f \mathrm { ~ i n ~ } L ^ { 3 }$ then the sequence converges to $f$ in measure.

Solution.

(a) False.
Let $f _ { n } = n \cdot \chi _ { \lceil 0 , 1 / n \rceil }$ . Then $f _ { n } \to 0$ almost everywhere but $\int _ { 0 } ^ { 1 } | f _ { n } | ^ { 3 } = \int _ { 0 } ^ { 1 / n } n ^ { 3 } = n ^ { 2 }$ , so $f _ { n }$ doesn’t converge to 0 in $L ^ { 3 }$

(b) True.
$\mathrm { B y }$ part (d) we know that $f _ { n }  f$ in measure.
So for each $k ,$ we have

$$
\operatorname* { l i m } _ { n \to \infty } \{ x : | f _ { n } ( x ) - f ( x ) | > 1 / k \} = 0 .
$$

For each k, pick $n _ { k }$ large enough so that $\lambda \{ x : | f _ { n } ( x ) - f ( x ) | > 1 / k \} < 2 ^ { - k }$ . Let ř $E _ { k } = \{ x : | f _ { n } ( x ) -$ $f ( x ) | > 1 / k \}$ We claim that $f _ { n _ { k } } \ \to \ f$ almost everywhere.
Note that since $\textstyle \sum _ { k = 1 } ^ { \infty } \lambda ( E _ { k } ) < \infty$ , the Borel-Cantelli lemma implies that the set of x that lie in infinitely many $E _ { k }$ has measure zero.
Fix $\epsilon > 0$ and let x be one of the almost everywhere points lying in only finitely many $E _ { k }$ . Then, as long as k is big enough so that $1 / k < \epsilon$ and $x \notin E _ { k }$ , we have $| f _ { n _ { k } } ( x ) - f ( x ) | \leqslant 1 / k < \epsilon$ . This shows that $f _ { n _ { k } } ( x )  f ( x )$ for a.e. x.

(c) False.
The same counterexample from part (a) works again.

(d) True.
Fix $\alpha > 0$ . Then we have

$$
\int | f _ { n } - f | ^ { 3 } ~ \geqslant ~ \int _ { \{ x : | f _ { n } ( x ) - f ( x ) | > \alpha \} } | f _ { n } - f | ^ { 3 } ~ \geqslant ~ \alpha ^ { 3 } \cdot \lambda \{ x : | f _ { n } ( x ) - f ( x ) | > \alpha \} .
$$

The left side goes to 0 as $n  \infty ,$ , so the right side does as well.

Problem 2. Let X and Y be topological spaces and $X \times Y$ the Cartesian product endowed with the product topology.
BpXq denotes the Borel sets in X and similarly, BpY q and $B ( X \times Y )$

(a) Suppose $f : X \to Y$ is continuous.
Prove that $E \in B ( Y )$ implies $f ^ { - 1 } ( E ) \in { \mathcal { B } } ( X )$

(b) Suppose $A \in B ( X )$ and $E \in B ( Y )$ . Show that $A \times E \in B ( X \times Y )$

Solution.

(a) Let ${ \mathcal { F } } = \{ E \subseteq Y : f ^ { - 1 } ( E ) \in B ( X ) \}$ . We want to show that $B ( Y ) \subseteq { \mathcal { F } }$ . It’s enough to show that $\mathcal { F }$ is a σ-algebra containing all open sets of Y . It’s clear that $\mathcal { F }$ contains all open sets in Y by the definition of continuous functions.
Thus $\emptyset$ and Y are in $\mathcal { F }$ because they are open.
Suppose $A \in { \mathcal { F } }$ . Then we have $f ^ { - 1 } ( A ^ { c } ) = f ^ { - 1 } ( A ) ^ { c } \in { \mathcal { B } } ( X )$ , so F is closed under complementation.
Finally, suppose $A _ { n } \in { \mathcal { F } } .$ Then we have $f ^ { - 1 } \left( \bigcup A _ { n } \right) = \bigcup f ^ { - 1 } ( A _ { n } ) \in { \mathcal { B } } ( X )$ , so $\mathcal { F }$ is closed under countable unions.
Thus $\mathcal { F }$ is a σ-algebra, so we’re done.

(b) Fix an open set $U \subseteq X$ . We first show that $U \times E \in { \mathcal { B } } ( X \times Y )$ for any $E \in B ( Y )$ . Let ${ \mathcal { F } } _ { U } = \{ E \subseteq$ $Y : U \times E \in B ( X \times Y ) \}$ . To verify that claim, we just need to show $\mathcal { F } _ { U }$ is a σ-algebra containing all open sets of Y . It’s clear that $\mathcal { F } _ { U }$ contains all open sets because the product of open sets is open.
$\mathrm { S o }$ $\mathcal { F } _ { U }$ contains $\emptyset$ and Y . If $E \in { \mathcal { F } } _ { U }$ , then $U \times { \bar { E } } ^ { c } = ( U \times Y ) \backslash ( U \times { \bar { E } } ) \in { \mathcal { B } } ( X \times Y )$ , so $\mathcal { F } _ { U }$ is closed under complementation.
If $E _ { n } \in \mathcal { F } _ { U }$ , then $U \times \bigcup E _ { n } = \bigcup ( U \times E _ { n } ) \in { \mathcal { B } } ( X \times Y )$ , so $\mathcal { F } _ { U }$ is closed under countable unions, so it’s a σ-algebra.
This shows that $U \times E \in { \mathcal { B } } ( X \times Y )$ for any open $U \subseteq X$ and any Borel $E \subseteq Y$

Now fix a Borel set $E \subseteq Y$ and let ${ \mathcal { F } } _ { E } = \{ A \subseteq X : A \times E \in B ( X \times Y ) \}$ We want to show $\mathcal { F } _ { E }$ contains all Borel sets in X, so it’s enough to show $\mathcal { F } _ { E }$ is a σ-algebra containing all open sets of X. We know it contains all open sets of X by the above work.
The exact same argument as above shows that it’s a σ-algebra.
Thus we conclude that $A \times E \in B ( X \times Y )$ for any $A \in \mathcal { B } ( X ) , E \in \mathcal { B } ( Y )$ □

Alternate solution.
(b) Let $\pi _ { X } ~ ( \mathrm { r e s p . } ~ \pi _ { Y } )$ be the projection maps $X \times Y  X ( \mathrm { r e s p . ~ } Y )$ . They are both continuous.
Then by part (a),

$$
A \times E ~ = ~ \pi _ { X } ^ { - 1 } ( A ) \cap \pi _ { Y } ^ { - 1 } ( E ) ~ \in ~ { \mathcal { B } } ( X \times Y ) . ~ \sqsubseteq
$$

Problem 3. Given $f : [ 0 , 1 ] \to \mathbb { R }$ belonging to $L ^ { 1 }$ and $n \in \mathbb { N } .$ define

$$
f _ { n } ( x ) ~ = ~ n \int _ { k / n } ^ { ( k + 1 ) / n } f ( y ) d y \quad \mathrm { f o r } \ x \in [ k / n , ( k + 1 ) / n ) { \mathrm { ~ a n d ~ } } 0 \leqslant k \leqslant n - 1 .
$$

Prove $f _ { n }  f$ in $L ^ { 1 }$

Solution.
First suppose $f$ is the characteristic function of an interval $f = \chi _ { [ a , b ] }$ Then note that for n large enough, $f _ { n }$ is constant and equal to f on each subinterval except for possibly the two subintervals containing a and b. On these two subintervals, we still have $0 \leqslant f _ { n } \leqslant 1$ . Thus we have

$$
\int _ { 0 } ^ { 1 } | f _ { n } - f | \leqslant 2 \cdot \frac { 1 } { n } \cdot \operatorname* { m a x } | f _ { n } - f | \leqslant \frac { 2 } { n } ,
$$

which shows that $f _ { n }  f$ in $L ^ { 1 }$ . Next note that the map $f \mapsto f _ { n }$ is linear, so we also know that $f _ { n }  f$ in $L ^ { 1 }$ for any $f$ which is a linear combination of characteristic functions of intervals.
This class of functions is dense in $L ^ { 1 }$ . So for a general $f \in L ^ { 1 }$ , let $g _ { k }$ be a sequence of functions of the above form with $g _ { k }  f$ in $L ^ { 1 }$ Then for any n large enough we have

$$
\big \vert \big \vert f _ { n } - f \big \vert \big \vert _ { L ^ { 1 } } \ \leqslant \ \big \vert \big \vert f - g _ { k } \big \vert \big \vert _ { L ^ { 1 } } + \big \vert \big \vert g _ { k } - \big ( g _ { k } \big ) _ { n } \big \vert \big \vert _ { L ^ { 1 } } + \big \vert \big \vert \big ( g _ { k } \big ) _ { n } - f _ { n } \big \vert \big \vert _ { L ^ { 1 } } .
$$

We estimate

$$
\begin{array} { r l } { \displaystyle | | ( g _ { k } ) _ { n } - f _ { n } | | _ { L ^ { 1 } } } & { = \displaystyle \sum _ { k = 0 } ^ { n - 1 } \int _ { k / n } ^ { ( k + 1 ) / n } | g _ { k } ( x ) - f ( x ) | d x \ = \displaystyle \sum _ { k = 0 } ^ { n - 1 } \int _ { k / n } ^ { ( k + 1 ) / n } n | \int _ { k / n } ^ { ( k + 1 ) / n } ( g _ { k } ( y ) - f ( y ) ) d y | d x } \\ & { \leqslant \displaystyle \sum _ { k = 0 } ^ { n - 1 } n \int _ { k / n } ^ { ( k + 1 ) / n } | f ( y ) - g _ { k } ( y ) | \int _ { k / n } ^ { ( k + 1 ) / n } d x d y \quad \mathrm { b y ~ T o n e l l i } } \\ & { = \displaystyle \sum _ { k = 0 } ^ { n - 1 } \int _ { k / n } ^ { ( k + 1 ) / n } | f ( y ) - g _ { k } ( y ) | d y \ = \ \displaystyle | | f - g _ { k } | | _ { L ^ { 1 } } . } \end{array}
$$

Thus we have

$$
\left| \left| f _ { n } - f \right| \right| _ { L ^ { 1 } } \leqslant 2 \left| \left| f - g _ { k } \right| \right| _ { L ^ { 1 } } + \left| \left| g _ { k } - ( g _ { k } ) _ { n } \right| \right| _ { L ^ { 1 } } .
$$

This holds for any n, so taking $n \to \infty$ we get

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } \| f _ { n } - f \| _ { L ^ { 1 } } \ \leqslant \ 2 \| f - g _ { k } \| _ { L ^ { 1 } }
$$

since we already verified the desired property for each $g _ { k }$ . Now the above holds for any $k ,$ so we can take $k \to \infty$ and conclude lim $1 _ { n  \infty } | | f _ { n } - f | | _ { L ^ { 1 } } = 0 . \quad \bigsqcup$

Problem 4. Let $S = \{ f \in L ^ { 1 } ( \mathbb { R } ^ { 3 } ) : \int f ( x ) d x = 0 \}$

(a) Show that S is closed in the $L ^ { 1 }$ topology.

(b) Show that $S \cap L ^ { 2 } ( \mathbb { R } ^ { 3 } )$ is a dense subset of $L ^ { 2 } ( \mathbb { R } ^ { 3 } )$

Solution.

(a) Let $f _ { n } \in S$ and $f \in L ^ { 1 }$ with $f _ { n }  f$ in $L ^ { 1 }$ . Then for each n we have

$$
| \int f | ~ = ~ | \int f - \int f _ { n } | ~ \leqslant ~ \int | f - f _ { n } | ~  ~ 0 ,
$$

so $\quad \int f = 0 . \qquad \square$

(b) We know that the set of $L ^ { 2 }$ functions with compact support is dense in $L ^ { 2 }$ , so it suffices to show that for any f $f \in L ^ { 2 }$ with compact support and any $\epsilon > 0$ , there is some $g \in S \cap L ^ { 2 }$ with ş $| | g - f | | _ { L ^ { 2 } } < \epsilon .$ Fix $f \in L ^ { 2 }$ with compact support and $\epsilon > 0$ . Say supp $( f ) \subseteq B ( 0 , M )$ and let $I = \int f ( x ) { \big / }$ dx.
We know that $I < \infty$ because $L ^ { 2 }$ functions with compact support are also $L ^ { \mathrm { i } }$ (by Cauchy-Schwarz).
We may assume $I > 0$ because if $I = 0$ then we’re done, and if $I < 0$ then we can do the same argument with a negative sign on everything.
The idea is to let $g = f$ on the support of ş $f ,$ and then let $g$ be equal to a small negative value outside the support of $f$ so that $\int g ( x ) d x = 0$

Let $C > M$ be a solution to $4 \pi / 3 ( C ^ { 3 } - M ^ { 3 } ) = I ^ { 2 } / \epsilon$ . Let $g ( x ) = f ( x )$ for $| x | \leqslant M , g ( x ) = - \epsilon / I$ for $M < | x | \leqslant C$ , and $g ( x ) = 0$ otherwise.
It’s clear that $g \in L ^ { 2 }$ . We have

$$
\int g ( x ) d x = \int _ { | x | \leq M } f ( x ) d x + \int _ { M < | x | \leq C } - \epsilon / I = I - \epsilon / I \cdot \lambda _ { 3 } ( M < | x | \leqslant C ) = I - \epsilon / I \cdot { \frac { 4 } { 3 } } \pi ( C ^ { 3 } - M ^ { 3 } ) = 0 ,
$$

so $g \in S \cap L ^ { 2 }$ . Also we have

$$
| | g - f | | _ { L ^ { 2 } } \ = \ \int _ { M < | x | \leqslant C } \epsilon ^ { 2 } / I ^ { 2 } \ = \ \epsilon ^ { 2 } / I ^ { 2 } \cdot \lambda _ { 3 } ( M < | x | \leqslant C ) \ = \ \epsilon . \quad \varPi
$$

Problem 5. State and prove the Riesz representation theorem for linear functionals on a Hilbert space.

Solution.
Statement: let H be a Hilbert space and let $f$ be a bounded linear functional on H. Then there exists $z \in H$ such that $f ( x ) = \langle x , z \rangle$ for all $x \in H$

Proof: Let $f \in H ^ { * }$ Since $f$ is a continuous map into a 1-dimensional space, we know that ker $( f )$ is a closed, co-dimension 1 subspace of H. Fix a nonzero $u \in \ker ( f ) ^ { \perp }$ Then we have the decomposition $H = \ker ( f ) \oplus \operatorname { s p a n } ( u )$ . Let $\alpha = \overline { { f ( u ) } } / \left| | u | \right| ^ { 2 }$ . Then we claim that $f ( x ) = \langle x , \alpha u \rangle$ for all $x \in H$ . Since every $x \in H$ decomposes uniquely as the sum of something in $\ker ( f )$ and something in $\operatorname { s p a n } ( u )$ , we just need to show that $x \mapsto f ( x )$ and $x \mapsto \langle x , \alpha u \rangle$ agree on ker $( f )$ and spanpuq.
For $y \in \ker ( f )$ , we clearly have $f ( y ) = 0$ and $\langle y , \alpha u \rangle = 0$ because u was chosen to be in ker $( f ) ^ { \perp }$ . For z P span $. ( u )$ , we have $z = c u$ for some $c ,$ so we have $f ( z ) = f ( c u ) = c f ( u )$ and $\langle z , \alpha u \rangle = c { \overline { { \alpha } } } \left| \left| u \right| \right| ^ { 2 } = c f ( u )$ by choice of α. Thus $f ( x ) = \langle x , \alpha u \rangle$ for all $x \in H . \qquad \sqcup$

Problem 6. Suppose $f \in L ^ { 2 } ( \mathbb { R } )$ and that the Fourier transform obeys ${ \hat { f } } ( \xi ) > 0$ for almost every $\xi .$ Show that the set of finite linear combinations of translates of $f$ is dense in the Hilbert space $L ^ { 2 } ( \mathbb { R } )$ .

Solution.
Let $M = { \overline { { \operatorname { s p a n } \{ x \mapsto f ( x + a ) \} _ { a \in \mathbb { R } } } } }$ where the closure is with respect to the $L ^ { 2 }$ norm.
Suppose for contradiction that $M \neq L ^ { 2 }$ . Then there is some nonzero $\overline { { g } } \in M ^ { \perp }$ . In particular we have $\int _ { \mathbb { R } } f ( x + a ) g ( x ) d x = 0$ for all $a \in \mathbb { R }$ . By Plancherel, this implies that

$$
\int _ { \mathbb { R } } \mathcal { F } ( x \mapsto f ( x + a ) ( \xi ) ) \mathcal { F } ( g ) ( \xi ) d \xi \ = \ \int _ { \mathbb { R } } e ^ { - 2 \pi i a \xi } \mathcal { F } ( f ) ( \xi ) \mathcal { F } ( g ) ( \xi ) d \xi \ = \ \mathcal { F } ( \mathcal { F } ( f ) \mathcal { F } ( g ) ) ( a ) \ = \ 0
$$

for all $a \in \mathbb { R }$ , where $\mathcal { F }$ denotes the Fourier-Plancherel transform $L ^ { 2 } \to L ^ { 2 }$ This formula is valid because since $f , g \in L ^ { 2 } , \mathcal { F } ( f ) \mathcal { F } ( g ) \in L ^ { 1 }$ , and thus the Fourier-Plancherel transform agrees with the standard $L ^ { 1 }$ Fourier transform.
But since $\mathcal { F }$ is a bijection this implies that $\begin{array} { r } { \mathcal { F } ( f ) ( \xi ) \mathcal { F } ( g ) ( \xi ) = 0 } \end{array}$ for almost every ξ. And since $\mathcal { F } ( f ) ( \xi ) > 0$ almost everywhere, this implies $\mathcal { F } ( g ) = 0$ almost everywhere, so $g = 0$ almost everywhere, which is a contradiction.
□

Problem 7. Let $\{ u _ { n } ( z ) \}$ be a sequence of real-valued harmonic functions on D that obey

$$
u _ { 1 } ( z ) ~ \geqslant ~ u _ { 2 } ( z ) ~ \geqslant ~ \dots ~ \geqslant 0 ~ \mathrm { ~ f o r ~ a l l } z \in \mathbb { D } .
$$

Prove that $z \mapsto \operatorname { i n f } _ { n } u _ { n } ( z )$ is a harmonic function on D.

Solution.
Let $u ( z ) = \mathrm { i n f } _ { n } u _ { n } ( z ) = \mathrm { l i m } _ { n  \infty } u _ { n } ( z )$ (the limit exists and equals the inf because the sequence is monotonically decreasing and bounded for each z). First we show that $u _ { n } \to u$ uniformly on compact subsets of D. Fix a compact subset ${ \overline { { B ( 0 , r ) } } } \subseteq \mathbb { D }$ For any $n > m , u _ { m } - u _ { n }$ is a positive harmonic function on D, so we can apply Harnack’s inequality on the disc $B ( 0 , ( 1 + r ) / 2 )$ to get, for any $| z | \leqslant r$ ,

$$
| u _ { m } ( z ) - u _ { n } ( z ) | \leqslant \frac { ( 1 + r ) / 2 + | z | } { ( 1 + r ) / 2 - | z | } | u _ { m } ( 0 ) - u _ { n } ( 0 ) | \leqslant \frac { ( 1 + r ) / 2 + r } { ( 1 + r ) / 2 - r } | u _ { m } ( 0 ) - u _ { n } ( 0 ) | \to 0
$$

as $n , m  \infty$ uniformly in $| z | \leqslant r$ because $\{ u _ { n } ( 0 ) \}$ is a convergent sequence.

Since each $u _ { n }$ is continuous, the local uniform convergence implies that u is continuous.
Also, for any $B ( z _ { 0 } , r ) \subseteq \mathbb { D }$ , we have

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } u ( z _ { 0 } + r e ^ { i \theta } ) d \theta \ = \ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \operatorname* { l i m } _ { n  \infty } u _ { n } ( z _ { 0 } + r e ^ { i \theta } ) d \theta \ = \ \operatorname* { l i m } _ { n  \infty } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } u _ { n } ( z _ { 0 } + r e ^ { i \theta } ) d \theta \ = \ \operatorname* { l i m } _ { n  \infty } u _ { n } ( 0 ) \ = \ u ( 0 )
$$

where switching the limit and the integral is justified by uniform convergence on the compact set $\partial B ( z _ { 0 } , r )$ Thus u is continuous and satisfies the mean value property on every disc, so it’s harmonic.

Problem 8. Let $\Omega \ = \ \{ x + i y : x > 0 , y > 0 , x y < 1 \}$ Give an example of an unbounded harmonic function on Ω that extends continuously to BΩ and vanishes there.

Solution.
We want to conformally map Ω to a region where it will be easier to find such a function.
Motivated by the fact that $( x + i y ) ^ { 2 } = { \bar { ( } } x ^ { 2 } - y ^ { 2 } ) + { \bar { i } } ( 2 x y )$ , we see that the map $z \mapsto \pi z ^ { 2 }$ is a conformal map from Ω to the strip $S : = \{ z : 0 < \mathrm { I m } ( z ) < 2 \pi \}$ Now note that $z \mapsto \operatorname { I m } ( e ^ { z } )$ is an unbounded harmonic function in S which vanishes on the boundary of S: we have Im $( \exp ( x + 0 i ) ) = \operatorname { I m } ( \exp ( x ) ) = 0$ and Im $( \exp ( x + 2 \pi i ) ) = \mathrm { I m } ( \exp ( x ) ) = 0$ , and Im $( \exp ( x + i \pi / 2 ) ) = \operatorname { I m } ( i \exp ( x ) ) = \exp ( x )$ , which is unbounded in S. Therefore the function $u ( z ) = \operatorname { I m } ( \exp ( \pi z ^ { 2 } ) )$ is a function that works.
□

Problem 9. Prove Jordan’s lemma: $\operatorname { I f } f ( z ) : \mathbb { C } \to \mathbb { C }$ is meromorphic, $R > 0$ , and $k > 0$ , then

$$
\left| \int _ { \Gamma } f ( z ) e ^ { i k z } d z \right| \ \leqslant \ { \frac { 1 0 0 } { k } } \operatorname* { s u p } _ { z \in \Gamma } | f ( z ) |
$$

where Γ is the quarter circle $z = R e ^ { i \theta }$ with $0 \leqslant \theta \leqslant \pi / 2$

Solution.
We have

$$
\begin{array} { r l r } { \left| \displaystyle \int _ { \Gamma } f ( z ) e ^ { i k z } d z \right| } & { = } & { \left| \displaystyle \int _ { 0 } ^ { \pi / 2 } f ( R e ^ { i \theta } ) e ^ { i k R e ^ { i \theta } } i R e ^ { i \theta } d \theta \right| ~ \leqslant ~ R \cdot \operatorname* { s u p } _ { z \in \Gamma } | f ( z ) | \cdot \displaystyle \int _ { 0 } ^ { \pi / 2 } \left| e ^ { i k R ( \cos \theta + i \sin \theta ) } \right| d \theta } \\ & { = } & { R \cdot \operatorname* { s u p } _ { z \in \Gamma } | f ( z ) | \cdot \displaystyle \int _ { 0 } ^ { \pi / 2 } e ^ { - k R \sin \theta } d \theta . ~ } \end{array}
$$

So we just need to show that $\int _ { 0 } ^ { \pi / 2 } e ^ { - k R \sin \theta } d \theta \leqslant \frac { 1 0 0 } { k R }$ . We break the integral in two:

$$
\int _ { 0 } ^ { \pi / 2 } e ^ { - k R \sin \theta } d \theta \ = \ \int _ { 0 } ^ { \pi / 4 } e ^ { - k R \sin \theta } d \theta + \int _ { \pi / 4 } ^ { \pi / 2 } e ^ { - k R \sin \theta } d \theta \ = : \ A + B .
$$

Now we estimate

$$
\begin{array} { r l } { A } & { = \displaystyle \int _ { 0 } ^ { \pi / 4 } e ^ { - k R \sin \theta } d \theta \ = \ \displaystyle \int _ { 0 } ^ { \sqrt { 2 } / 2 } e ^ { - u } \frac { d u } { k R \cos \theta } \ \leqslant \ \displaystyle \frac { 1 } { k R \sqrt { 2 } / 2 } \displaystyle \int _ { 0 } ^ { \sqrt { 2 } / 2 } e ^ { - u } d u \ \leqslant \ \frac { \sqrt { 2 } } { k R } } \\ { B } & { = \displaystyle \int _ { \pi / 4 } ^ { \pi / 2 } e ^ { - k R \sin \theta } d \theta \ \leqslant \ \displaystyle \int _ { \pi / 4 } ^ { \pi / 2 } e ^ { - k R \sqrt { 2 } / 2 } d \theta \ = \ \displaystyle \frac { \pi } { 4 } e ^ { - k R \sqrt { 2 } / 2 } \ \leqslant \ \frac { \pi \sqrt { 2 } } { 4 } \cdot \frac { 1 } { k R } \quad \mathrm { b e c a u s e } \ e ^ { - x } \leqslant 1 / x \ \mathrm { f o r } \ x > 0 . } \end{array}
$$

Thus we conclude

$$
\int _ { 0 } ^ { \pi / 2 } e ^ { - k R \sin \theta } d \theta \ \leqslant \ \left( { \sqrt { 2 } } + { \frac { \pi { \sqrt { 2 } } } { 4 } } \right) { \frac { 1 } { k R } } \ \leqslant \ { \frac { 1 0 0 } { k R } } . \quad \boxed { 1 }
$$

Alternate solution.
Same up to the bound

$$
\left| \int _ { \Gamma } f ( z ) d z \right| \ \leqslant \ R \cdot \operatorname* { s u p } _ { z \in \Gamma } \left| f ( z ) \right| \cdot \int _ { 0 } ^ { \pi / 2 } e ^ { - k R \sin ( \theta ) } d \theta .
$$

Now note that on $[ 0 , \pi / 2 ]$ , sin $\iota ( \theta ) \geqslant ( 2 / \pi ) \theta$ , so we have

$$
\left| \int _ { \Gamma } f ( z ) d z \right| \leqslant R \operatorname* { s u p } _ { z \in \Gamma } | f ( z ) | \cdot \int _ { 0 } ^ { \pi / 2 } e ^ { - k R ( 2 / \pi ) \theta } d \theta = \frac { \pi / 2 } { k } \operatorname* { s u p } _ { z \in \Gamma } | f ( z ) | \cdot \int _ { 0 } ^ { \pi / 2 } e ^ { - \theta } d \theta \leqslant \frac { \pi / 2 } { k } \operatorname* { s u p } _ { z \in \Gamma } | f ( z ) | \cdot \int _ { 0 } ^ { \infty } e ^ { - \theta } d \theta \leqslant \frac { \pi / 2 } { k } \operatorname* { s u p } _ { z \in \Gamma } | f ( z ) | .
$$

and I think this is the optimal constant.

Problem 10. Let us define the Gamma function via

$$
\Gamma ( z ) ~ = ~ \int _ { 0 } ^ { \infty } t ^ { z - 1 } e ^ { - t } d t
$$

when the integral is absolutely convergent.
Show that this function extends to a meromorphic function in the whole complex plane.

Solution.
Note that for $\mathrm { R e } ( z ) > 0$ , we have

$$
\int _ { 0 } ^ { \infty } \left| t ^ { z - 1 } \right| e ^ { - t } d t \ = \ \int _ { 0 } ^ { \infty } t ^ { \mathrm { R e } ( z ) - 1 } e ^ { - t } d t \ < \ \infty .
$$

So the integral is absolutely convergent for all $\mathrm { R e } ( z ) > 0$ . First we show that it defines an analytic function for $\mathrm { R e } ( z ) > 1$ . We have

$$
\frac { \Gamma ( z + h ) - \Gamma ( z ) } { h } \ = \ \int _ { 0 } ^ { \infty } e ^ { - t } t ^ { z - 1 } \left( \frac { t ^ { h } - 1 } { h } \right) .
$$

We estimate

$$
\begin{array} { r l } { | e ^ { - t } t ^ { z - 1 } ( \displaystyle \frac { t ^ { h } - 1 } { h } ) | } & { =  e ^ { - t } t ^ { \mathrm { R e } ( z ) - 1 } | \displaystyle \frac { e ^ { h \log t } - 1 } { h } |  \leqslant  e ^ { - t } t ^ { \mathrm { R e } ( z ) - 1 } \displaystyle \sum _ { n = 1 } ^ { \infty } \displaystyle \frac { | h | ^ { n - 1 } | \log t | ^ { n } } { n ! } } \\ { \leqslant  e ^ { - t } t ^ { \mathrm { R e } ( z ) - 1 } \displaystyle \sum _ { n = 1 } ^ { \infty } \displaystyle \frac { | \log t | ^ { n } } { n ! } \quad \mathrm { f o r ~ } | h | \leqslant 1  } \\ { \leqslant  e ^ { - t } t ^ { \mathrm { R e } ( z ) - 1 } e ^ { | \log t | } . } \end{array}
$$

If $\mathrm { R e } ( z ) > 1$ , then $e ^ { - t } t ^ { \mathrm { R e } ( z ) - 1 } e ^ { | \log t | }$ is integrable on $[ 0 , \infty )$ , so by the Dominated Convergence theorem we see that the above difference quotient converges as $h  0 .$ , so Γ is analytic.
So far we have that Γ is analytic in $\mathrm { R e } ( z ) > 1$ . By integrating by parts we get, for any $\mathrm { R e } ( z ) > 0$

$$
\Gamma ( z + 1 ) ~ = ~ \int _ { 0 } ^ { \infty } t ^ { z } e ^ { - t } d t ~ = ~ z \int _ { 0 } ^ { \infty } t ^ { z - 1 } e ^ { - t } d t ~ = ~ z \Gamma ( z ) .
$$

So we can extend the definition of Γ by setting $\begin{array} { r } { \Gamma ( z ) : = \frac { 1 } { z } \Gamma ( z + 1 ) = \frac { 1 } { z ( z + 1 ) } \Gamma ( z + 2 ) } \end{array}$ for all $- 1 < \operatorname { R e } ( z ) \leqslant 0$ except for $z = 0$ . This definition makes Γ analytic in $- 1 < \operatorname { R e } ( z ) \leqslant 0$ except at 0 because for any nonzero point in that strip, we can take a neighborhood around that point on which $\begin{array} { r } { z \mapsto \frac { 1 } { z ( z + 1 ) } } \end{array}$ and $z \mapsto \Gamma ( z + 2 )$ are both analytic.
There is no problem even when taking neighborhoods around points with $\mathrm { R e } ( z ) = 0$ because in $0 < \operatorname { R e } ( z ) \leqslant 1$ , the two definitions of Γ agree because of the functional equation.

We can extend this definition to all of C. In general, for non-negative integers n, define Γ on the strip $- n - 1 < \mathrm { R e } ( z ) \leqslant - n$ (except not at $z = - n )$ by

$$
\Gamma ( z ) = { \frac { 1 } { z ( z + 1 ) \cdots ( z + n + 1 ) } } \Gamma ( z + n + 2 ) .
$$

By the same reasoning, this definition makes Γ analytic everywhere except for at all of the non-positive integers.
To show that Γ is meromorphic, we just need to show that it has poles at each non-positive integer.
Fix a non-positive integer ´n. In any neighborhood of $z = - n$ , the representation

$$
\Gamma ( z ) = { \frac { 1 } { z ( z + 1 ) \cdots ( z + n + 1 ) } } \Gamma ( z + n + 2 ) .
$$

is valid regardless of whether $\mathrm { R e } ( z ) \leqslant - n$ or $\operatorname { R e } ( z ) > - n$ , because of the functional equation which is valid in the right half plane.
Since $\Gamma ( 2 ) \neq 0$ , it’s clear that $\Gamma ( z ) \to \infty { \mathrm { a s ~ } } z \to - n .$ , and thus Γ has a pole at ´n.

Problem 11. Let $P ( z )$ be a polynomial.
Show that there is an integer n and a second polynomial $Q ( z )$ so that

$$
P ( z ) Q ( z ) \ = \ z ^ { n } | P ( z ) | ^ { 2 } { \mathrm { ~ w h e n e v e r ~ } } | z | = 1 .
$$

Solution.
Write $P ( z ) = ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { m } )$ . Define $Q ( z ) = ( 1 - \overline { { a _ { 1 } } } z ) \cdot \cdot \cdot ( 1 - \overline { { a _ { m } } } z )$ . It’s clear $Q$ is a polynomial.
On $| z | = 1$ , we have

$$
{ \begin{array} { r l } { | P ( z ) | ^ { 2 } \ = \ P ( z ) { \overline { { P ( z ) } } } \ = \ ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { m } ) ( { \overline { { z } } } - { \overline { { a _ { 1 } } } } ) \cdot \cdot \cdot ( { \overline { { z } } } - { \overline { { a _ { m } } } } ) } \\ { \ = \ ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { m } ) ( 1 / z - { \overline { { a _ { 1 } } } } ) \cdot \cdot \cdot ( 1 / z - { \overline { { a _ { m } } } } ) } \\ { \ = \ ( z - a _ { 1 } ) \cdot \cdot \cdot ( z - a _ { m } ) ( 1 / z ) ^ { m } ( 1 - { \overline { { a _ { 1 } } } } z ) \cdot \cdot \cdot ( 1 - { \overline { { a _ { m } } } } z ) \ = \ { \frac { 1 } { z ^ { m } } } P ( z ) Q ( z ) . } \end{array} }
$$

So $P ( z ) Q ( z ) = z ^ { m } | P ( z ) | ^ { 2 } \mathrm { o n } | z | = 1 .$

Problem 12. Show that the only entire function fpzq obeying both

$$
| f ^ { \prime } ( z ) | \ \leqslant \ e ^ { | z | } \quad { \mathrm { a n d } } \quad f \left( { \frac { n } { \sqrt { 1 + | n | } } } \right) \ = \ 0 \quad { \mathrm { f o r ~ a l l ~ } } n \in \mathbb { Z }
$$

is the zero function.

Solution.
Suppose f is not identically zero.
Then since its zeros are discrete, it has countable many.
Enu-a ř merate them $\left\{ a _ { k } \right\}$ . By hypothesis $f$ vanishes at every $n / { \sqrt { 1 + | n | } }$ for $n \in \mathbb { Z } .$ , so we know that $\textstyle \sum _ { k } | a _ { k } | ^ { - 2 } = \infty$ This implies that the genus of $f$ is at least 2 (proof below).
By Hadamard’s theorem, this also implies the order of $f$ is at least 2. But by hypothesis, we have $f ( 0 ) = 0$ , and so for any z we can write

$$
| f ( z ) | \ = \ \left| \int _ { \gamma _ { z } } f ^ { \prime } ( w ) d x \right| \ \leqslant \ | z | \operatorname* { s u p } _ { w \in \gamma _ { z } } | f ^ { \prime } ( w ) | \ \leqslant \ | z | e ^ { | z | } \ \leqslant \ e ^ { 2 | z | }
$$

where $\gamma _ { z }$ is a straight line from 0 to z. But this shows that the order of $f$ is $\leqslant 1$ , a contradiction.

Here is a proof that $\textstyle \sum _ { k } | a _ { k } | ^ { - 2 } = \infty$ implies the genus of $f$ is at least 2. It follows from the more gen-ř eral claim: ${ \mathrm { I f ~ g e n u s } } ( f ) \leqslant h$ and $\left\{ a _ { k } \right\}$ are the zeros of $f ,$ then $\textstyle \sum _ { k } | a _ { k } | ^ { - ( h + 1 ) } < \infty$ . If the genus is $\leqslant h ,$ then we know that the product

$$
\prod _ { k = 1 } ^ { \infty } \left( 1 - { \frac { z } { a _ { k } } } \right) \exp \left( { \frac { z } { a _ { k } } } + { \frac { 1 } { 2 } } \left( { \frac { z } { a _ { k } } } \right) ^ { 2 } + \ldots + { \frac { 1 } { h } } \left( { \frac { z } { a _ { k } } } \right) ^ { h } \right)
$$

converges uniformly on compact sets.
In particular, fix some z which is not a zero of $f ,$ then we know the series

$$
\sum _ { k = 1 } ^ { \infty } \log { \left( 1 - { \frac { z } { a _ { k } } } \right) } + { \frac { z } { a _ { k } } } + { \frac { 1 } { 2 } } \left( { \frac { z } { a _ { k } } } \right) ^ { 2 } + \ldots + { \frac { 1 } { h } } \left( { \frac { z } { a _ { k } } } \right) ^ { h }
$$

convergs absolutely.
For all $| a _ { k } | > 3 | z |$ , we have the estimate

$$
\begin{array} { r l } { \log \left( 1 - \frac { z } { a _ { k } } \right) + \frac { z } { a _ { k } } + \frac { 1 } { 2 } \left( \frac { z } { a _ { k } } \right) ^ { 2 } + \dots + \frac { 1 } { \hbar } \left( \frac { z } { a _ { k } } \right) ^ { k } \Bigg | = \Bigg | \displaystyle \sum _ { j = h + 1 } ^ { \infty } \frac { 1 } { j } \left( \frac { z } { a _ { k } } \right) ^ { j } \Bigg | } & { } \\ { = } & { \frac { 1 } { \hbar + 1 } \left| \frac { z } { a _ { k } } \right| ^ { \hbar + 1 } \Bigg | \displaystyle \sum _ { j = h + 1 } ^ { \infty } \frac { h + 1 } { j } \left( \frac { z } { a _ { k } } \right) ^ { i - ( k + 1 ) } \Bigg | } & { } \\ { \geqslant } & { \frac { 1 } { \hbar + 1 } \left| \frac { z } { a _ { k } } \right| ^ { \hbar + 1 } \left( 1 - \displaystyle \sum _ { j = h + 2 } ^ { \infty } \frac { h + 1 } { j } \left| \frac { z } { a _ { k } } \right| ^ { j - ( k + 1 ) } \right) } & { } \\ { \geqslant } & { \frac { 1 } { \hbar + 1 } \left| \frac { z } { a _ { k } } \right| ^ { \hbar + 1 } \left( 1 - \displaystyle \sum _ { j = h + 2 } ^ { \infty } ( 1 / 3 ) ^ { j - ( k + 1 ) } \right) } & { } \\ { \geqslant } & { \frac { 1 } { 2 ( \hbar + 1 ) } ^ { \left| a \right| ^ { k + 1 } } \left| a _ { k } \right| ^ { - ( k + 1 ) } . } \end{array}
$$

Thus

$$
\sum _ { | a _ { k } | > 3 | z | } | a _ { k } | ^ { - ( h + 1 ) } \leqslant \frac { 2 ( h + 1 ) } { | z | ^ { h + 1 } } \sum _ { | a _ { k } | > 3 | z | } \left| \log \left( 1 - \frac { z } { a _ { k } } \right) + \frac { z } { a _ { k } } + \frac { 1 } { 2 } \left( \frac { z } { a _ { k } } \right) ^ { 2 } + . . . + \frac { 1 } { h } \left( \frac { z } { a _ { k } } \right) ^ { h } \right| \leqslant \infty .
$$

This establishes the desired claim because there are only finitely many $a _ { k }$ with $| a _ { k } | \leqslant 3 | z |$

Alternate solution.
By the same argument as in the other solution we have $| f ( z ) | \leqslant e ^ { 2 | z | }$ We want to use Jensen’s formula.
First multiply f by a power of z so that $f ( 0 ) \neq 0$ This preserves an inequality of the form $| f ( z ) | \leqslant e ^ { c | z | }$ . For any R (assuming f has no zeros on $| z | = R )$ , Jensen’s formula gives (enumerating the zeros of f as $a _ { n } )$

$$
\begin{array} { r l } { | \log | f ( 0 ) | - } & { - \displaystyle \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \log | f ( T ( R e ^ { s } ) | \boldsymbol { \partial } \boldsymbol { \partial } \boldsymbol { \partial } + \sum _ { | \alpha | \leq \delta } \log | \frac { l _ { \alpha } } { R } | \boldsymbol { \partial } \boldsymbol { \partial } | } \\ & { \lesssim \log e ^ { \delta R } + \displaystyle \sum _ { | \alpha | > \delta \in \mathcal { K } _ { \delta } ^ { 1 + 1 } \operatorname* { l i m } \times R } \log \left| \frac { \alpha } { R } \right| \frac { n } { \delta \sqrt { 1 + | \alpha | } } \biggr | } \\ & { \lesssim \ R + \displaystyle \sum _ { \substack { n \leq \delta \pi ^ { 2 } } } \log \left| \frac { \nabla n } { R } \right| } \\ & { \lesssim \ R - \displaystyle \sum _ { \substack { n \leq \delta \pi ^ { 2 } } } ^ { \infty } \log R + \sum _ { \substack { n \leq \delta \pi ^ { 2 } } } ^ { \infty } \log \sqrt { n } } \\ & { \lesssim \ R - H ^ { 2 } \log R + \frac { 1 } { 2 } \int _ { 0 } ^ { R } \log \alpha d \alpha } \\ & { \lesssim \ R - H ^ { 2 } \log R + \frac { 1 } { 2 } \log R } \\ & { \lesssim \ R - H ^ { 2 } \log R + H ^ { 2 } \log R - \frac { 1 } { 2 } \hat { H } ^ { 2 } } \end{array}
$$

which goes to $- \infty$ as $R \to \infty$ , a contradiction.

## 8 Fall 2012

Problem 1. Let $1 < p < \infty$ and let $f _ { n } : \mathbb { R } ^ { 3 } \to \mathbb { R }$ be a sequence of functions such that lim sup ${ | | f _ { n } | | } _ { L ^ { p } } < \infty$ Show that if $f _ { n }$ converges almost everywhere, then $f _ { n }$ converges weakly in $L ^ { p }$

Solution.
Let λ denote Lebesgue measure on $\mathbb { R } ^ { 3 }$ Say that $f _ { n }  f$ pointwise almost everywhere and also that $| | f _ { n } | | _ { L ^ { p } } \leqslant M$ for all $n .$ To show that $f _ { n }  f$ weakly in $L ^ { p }$ , we need to show that $\phi ( f _ { n } ) \to \phi ( f )$ for every bounded linear functional ş $\phi \in ( L ^ { p } ) ^ { * }$ . By $L ^ { p } – L ^ { q }$ duality, we know that every $\phi \in ( L ^ { p } ) ^ { * }$ is of the form $\phi ( f ) = \int f g d \lambda$ for some $g \in L ^ { q }$ . So let $g$ be any $L ^ { q }$ function; it suffices to show that

$$
\int f _ { n } g \  \ \int f g .
$$

Since $f _ { n }  f$ almost everywhere, we also know that ş ş $f _ { n } g \to f g$ almost everywhere.
By the Vitali Convergence Theorem, to show $\int f _ { n } g \dot { d } \lambda  \int f g d \lambda$ it suffices to show that the sequence $\left\{ f _ { n } g \right\}$ is uniformly integrable and tight.

For uniform integrability, let ş $\epsilon > 0$ . Since $| g | ^ { q }$ is integrable, let $\delta > 0$ be such that whenever $\lambda ( A ) < \delta$ we have $\int _ { A } | g | ^ { q } d \lambda < \epsilon$ . Then for any n and any $\lambda ( A ) < \delta .$ we have by H¨older’s inequality

$$
\int _ { A } | f _ { n } g | d \lambda \ \leqslant \ \left( \int _ { A } | f _ { n } | ^ { p } d \lambda \right) ^ { 1 / p } \left( \int _ { A } | g | ^ { q } d \lambda \right) ^ { 1 / q } \ < \ M \epsilon ^ { 1 / q } ,
$$

which shows that $\left\{ f _ { n } g \right\}$ is a uniformly integrable family.

For tightness, let $\epsilon > 0$ and let $E$ be a subset of $\mathbb { R } ^ { 3 }$ such that $\int _ { E ^ { c } } | g | ^ { q } d \lambda < \epsilon$ . Then for any n, we have by the same argument

$$
\int _ { E ^ { c } } | f _ { n } g | d \lambda \ \leqslant \ \left( \int _ { E ^ { c } } | f _ { n } | ^ { p } d \lambda \right) ^ { 1 / p } \left( \int _ { E ^ { c } } | g | ^ { q } d \lambda \right) ^ { 1 / q } \ < \ M \epsilon ^ { 1 / q } ,
$$

so $\left\{ f _ { n } g \right\}$ is a tight family, so we are done.

Problem 2. Suppose $d \mu$ is a Borel probability measure on the unit circle in the complex plane such that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { | z | = 1 } z ^ { n } d \mu ( z ) \ = \ 0 .
$$

For $f \in L ^ { 1 } ( d \mu )$ show that

$$
\operatorname* { l i m } _ { n  \infty } \int _ { | z | = 1 } z ^ { n } f ( z ) d \mu ( z ) \ = \ 0 .
$$

Solution.
By linearity, it is clear that the desired result holds for any trigonometric polynomial on theř unit circle, i.e. any function of the form $\begin{array} { r } { P ( z ) = \sum _ { n = - N } ^ { N } a _ { n } z ^ { n } } \end{array}$ . Since $\mu$ is a Borel measure and the unit circle is compact, we know that the set of continuous functions on $S ^ { 1 }$ is dense in $L ^ { 1 } ( \mu )$ with respect to the norm $\left| \left| \cdot \right| \right| _ { L ^ { 1 } \left( \mu \right) }$ . We also know by the Stone-Weierstrass theorem that the set of trigonometric polynomials on $S ^ { 1 }$ is dense in the set of continuous functions on $S ^ { 1 }$ with respect to the norm $\| \cdot \| _ { L ^ { \infty } ( \mu ) }$

So let $f \in L ^ { 1 } ( \mu )$ and fix $\epsilon > 0 .$ . Let g be a continuous function on $S ^ { 1 }$ such that $| | f - g | | _ { L ^ { 1 } ( \mu ) } < \epsilon$ and let $P$ be a trigonometric polynomial such that $\| g - P \| _ { L ^ { \infty } ( \mu ) }$ . Since the result holds for trigonometric polynomials, we can pick n large enough so that

$$
\left| \int _ { | z | = 1 } z ^ { n } P ( z ) d \mu ( z ) \right| \ < \ \epsilon .
$$
