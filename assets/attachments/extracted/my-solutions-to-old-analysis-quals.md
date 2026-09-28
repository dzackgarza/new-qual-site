# My Solutions to Old Analysis Quals

Jacob S Townson

August-December 2017

## Prelude

This document is written in reference to qualifying exams given at the University of Louisville in past years. These solutions are not given from the University, but of my work alone as a way to study for my own qualifying exam. If any tips or recommendations come up and you feel you should share, feel free to raise an issue on GitHub where I have this document saved and open to the public here

(https://github.com/obewanjacobi/gradwork/tree/master/Classes/Old%20Qualifying%20Exams/My%20Solutions). To see the qualifying exams for yourself, visit this link (http://www.math.louisville.edu/GraduateFAQ/qualifiers/QualifierStudyGuides/). When referencing the Royden book, this is in reference to the Real Analysis; 4th Edition. Special thanks to Trevor Leach for sharing his solutions with me for reference on this document. Thank you for reading, and for all advice.

Jacob Townson

## What to Expect:

differentiation and Riemann integration of functions of one real variable, sequences of functions, uniform convergence, Lebesgue’s characterization of Riemann integrability

topology of the line, countable and uncountable sets, Borel sets, Cantor sets and Cantor functions, Baire category theorem

Lebesgue measure and integration on the line, measurable functions, convergence theorems

AC and BV functions, fundamental theorem of calculus, Lebesgue differentiation theorem

Hilbert spaces, Lp spaces, lp spaces, Hölder and Minkowski (like triangle) inequalities, completeness

There are a few types of problems that are consistently on exams as well, and may be good to know. These include that when asked to prove uniform convergence, using the Wierstass M-test is the easiest method; when a problem involves absolute continuity, it will often be used to imply bounded variation, which then implies that we can use the fundamental theorem of calculus; and finally, if we have two functions that are in conjugate $L ^ { p }$ spaces, Holder’s inequality will help us. Using these tricks and others contained in this document should guarantee a passing score on the qualifier!

## My Solutions from Quals

Spring 2017

Prove that if $A \subset \mathbb { R }$ has Lebesgue measure $0$ , then $m ( \{ e ^ { x } | x \in A \} ) = 0$

My Solution:

Let $m ( A ) = 0$ and $E = \{ \mathrm { e } ^ { x } | x \in A \}$ . First note that we know $f ( x ) = \mathbf { e } ^ { x }$ is continuous on . Let R $A _ { N } = [ - N , N ] \cap A$ , then

$$
A = \bigcup _ { N = 1 } ^ { \infty } A _ { N }
$$

Also, $m ( A ) = 0 \implies m ( A _ { N } ) = 0$ for all $N \in \mathbb { N } .$ . By definition of Lebesgue measure, for all $\epsilon > 0 .$ there exists a sequence of intervals $\{ I _ { n } \} _ { n = 1 } ^ { \infty }$ such that 1 $I _ { i } \cap I _ { j }$ is the empty set for all andi $j .$ . Also, $A _ { N } \subset \cup I _ { n }$ such that $\textstyle \sum _ { n } l ( I _ { n } ) < \epsilon$ since $m ( A _ { N } ) = 0$ . L e t ${ \cal I } _ { n } = ( a _ { n } , b _ { n } ) , { \cal I } _ { n } ^ { * } = [ a _ { n } , b _ { n } ]$ , then $m ( I _ { n } ) = m ( I _ { n } ^ { * } )$ . Then

$$
m ( f ( A _ { N } ) ) < \sum _ { n } m ( f ( I _ { n } ) ) = \sum _ { n } m ( f ( I _ { n } ^ { * } ) )
$$

Since $f$ is continuous, we know that $m ( f ( I _ { n } ^ { * } ) ) = \operatorname* { m a x } _ { x \in I _ { n } ^ { * } } f ( x ) - \operatorname* { m i n } _ { x \in I _ { n } ^ { * } } f ( x )$ . Since ${ { I } _ { n } ^ { * } }$ is a closed interval and $f$ is continuous, we can find $x _ { 1 }$ and $x _ { 2 } \in I _ { n } ^ { * }$ such that $f ( x _ { 1 } ) = \operatorname* { m a x } _ { x \in I _ { n } ^ { * } } f ( x )$ and $f ( x _ { 2 } ) = \operatorname* { m i n } _ { x \in I _ { n } ^ { * } } f ( x )$ . WLOG we can assume that $x _ { 1 } \leq x _ { 2 }$ . Then,

$$
m ( f ( I _ { n } ^ { * } ) ) = f ( x _ { 1 } ) - f ( x _ { 2 } ) \leq | f ^ { \prime } ( \alpha ) | ( x _ { 1 } - x _ { 2 } )
$$

$$
\leq \operatorname* { m a x } _ { x \in I _ { n } ^ { * } } f ^ { \prime } ( x ) \times l ( I _ { n } ) \leq \operatorname* { m a x } _ { x \in I _ { n } ^ { * } } f ^ { \prime } ( x ) \epsilon
$$

where $\alpha \in ( x _ { 1 } , x _ { 2 } )$

Since $\operatorname* { m a x } _ { x \in I _ { n } ^ { * } } f ^ { \prime } ( x ) < \infty$ and $\epsilon \to 0$ , we find that $m ( f ( I _ { n } ) ) = 0$ . This implies $m ( f ( A _ { N } ) ) = 0$ which implies

$$
m ( f ( A ) ) = m ( f ( \cup _ { N } ^ { \infty } A _ { N } ) ) \leq \sum _ { N } ^ { \infty } m ( f ( A _ { N } ) ) = 0
$$

Thus, $m ( f ( A ) ) = m ( E ) = 0 .$ QED

Prove that if $f : [ 0 , 1 ] \to ( 0 , \infty )$ is absolutely continuous, then so is $1 / f$

My Solution:

Given that $f$ is absolutely continuous, we know then that for all $\epsilon > 0 \AA$ , there exists a $\delta > 0$ such that if $\{ ( a _ { i } , b _ { i } ) \} _ { i = 1 } ^ { n }$ is a finite collection of disjoint intervals of $[ 0 , 1 ]$ with $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \left| b _ { i } - a _ { i } \right| < \delta } \end{array}$ implies that $\textstyle \sum _ { i = 1 } ^ { n } | f ( b _ { i } ) - f ( a _ { i } ) | < \epsilon$ . Also, because $f$ is absolutely continuous, we know then that it must also be continuous. Hence, must be bounded onf $[ 0 , 1 ]$ . Let $m = \operatorname* { m i n } ( f )$ on and choose [0, 1] $\delta \dot { }$ such that $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \left| b _ { i } - a _ { i } \right| < \delta } \end{array}$ gives us

$$
\sum _ { i = 1 } ^ { n } | f ( b _ { i } ) - f ( a _ { i } ) | < m ^ { 2 } \epsilon
$$

Then note that

$$
\sum _ { i = 1 } ^ { n } \left| { \frac { 1 } { f ( b _ { i } ) } } - { \frac { 1 } { f ( a _ { i } ) } } \right| = \sum _ { i = 1 } ^ { n } \left| { \frac { f ( b _ { i } ) - f ( a _ { i } ) } { f ( a _ { i } ) f ( b _ { i } ) } } \right|
$$

$$
\leq { \frac { 1 } { m ^ { 2 } } } \sum _ { i = 1 } ^ { n } | f ( b _ { i } ) - f ( a _ { i } ) | < { \frac { m ^ { 2 } \epsilon } { m ^ { 2 } } } = \epsilon
$$

Hence, $\textstyle { \frac { 1 } { f } }$ is absolutely continuous as well. QED

Prove that if $f$ is absolutely continuous on $\lceil 0 , 1 \rceil$ and there is a $g \in C ( [ 0 , 1 ] )$ such that $f ^ { \prime } = g \mathsf { a . e . }$ , then $f$ is differentiable on $[ 0 , \dot { 1 } ]$ and $f ^ { \prime } = g$

My Solution:

Using Lebesgue’s fundamental theorem of calculus, we know that

$$
f ( x ) = f ( 0 ) + \int _ { 0 } ^ { x } f ^ { \prime }
$$

Then, because $f ^ { \prime } = g \mathsf { a . e . }$

$$
f ( x ) = f ( 0 ) + \int _ { 0 } ^ { x } g
$$

This implies that $\textstyle { \int _ { 0 } ^ { x } f ^ { \prime } = \int _ { 0 } ^ { x } g }$ , thus by the fundamental theorem of calculus, if we take the derivative of both sides, we can see that $f ^ { \prime } ( x ) = g ( x )$ for all . Note, the reason that we can use the fundamental theorem of calculus here is because the function x $f$ is absolutely continuous, which implies it’s of bounded variation. QED

Prove that the series $\scriptstyle \sum _ { k = 0 } ^ { \infty } \sin ^ { k }$ converges uniformly fort $t \in [ - \pi / 4 , \pi / 4 ]$ and then evaluate the following series:

$$
\sum _ { k = 0 } ^ { \infty } \int _ { - \pi / 4 } ^ { \pi / 4 } \sin ^ { k } ( t ) d t
$$

My Solution:

Recall the Weierstrass M Test: Let $\textstyle \sum _ { n = 1 } ^ { \infty } f _ { n }$ be a series of real valued functions on a subset $A \subset \mathbb { R }$ . Suppose there exists a convergent series $\textstyle \sum _ { n = 1 } ^ { \infty } M _ { n }$ where $M _ { n } \geq 0$ such that for all $n \in \mathbb { N }$ and $x \in A , | f _ { n } ( x ) | \leq M _ { n }$ . Then $\textstyle \sum _ { n = 1 } ^ { \infty } f _ { n }$ converges uniformly.

Now, for $\begin{array} { r } { t \in [ - \pi / 4 , \pi / 4 ] , \sin ^ { k } ( t ) \leq \left( \frac { 1 } { \sqrt { 2 } } \right) ^ { k } } \end{array}$ for all . Note,  k $\scriptstyle \sum _ { k = 1 } ^ { \infty } \left( { \frac { 1 } { \sqrt { 2 } } } \right) ^ { k }$ converges because it is a geometric series. Thus by the Weierstrass M test, the series converges uniformly for $t \in [ - \pi / 4 , \pi / 4 ]$ . QED

Because the series converges uniformly on a compact set,

$$
\sum _ { k = 1 } ^ { \infty } \int _ { - \pi / 4 } ^ { \pi / 4 } \sin ^ { k } ( t ) d t = \int _ { - \pi / 4 } ^ { \pi / 4 } \sum _ { k = 1 } ^ { \infty } \sin ^ { k } ( t ) d t = \int _ { - \pi / 4 } ^ { \pi / 4 } { \frac { 1 } { 1 - \sin ( t ) } } d t
$$

$$
\begin{array} { l } { \displaystyle = \int _ { - \pi / 4 } ^ { \pi / 4 } \frac { 1 + \sin ( t ) } { \cos ^ { 2 } ( t ) } d t = \int _ { - \pi / 4 } ^ { \pi / 4 } \sec ^ { 2 } ( t ) d t + \int _ { - \pi / 4 } ^ { \pi / 4 } \tan ( t ) \sec ( t ) d t } \\ { \displaystyle \quad = \tan ( t ) | _ { - \pi / 4 } ^ { \pi / 4 } + \sec ( t ) | _ { - \pi / 4 } ^ { \pi / 4 } = 1 - ( - 1 ) + \sqrt { 2 } - \sqrt { 2 } = 2 } \end{array}
$$

QED

Let $\{ E _ { n } \} \subset { \mathcal { M } }$ be a sequence of Lebesgue measurable subsets of $\lceil 0 , 1 \rceil$ . Prove: (a) If $\sum { \bar { m } } ( E _ { n } ) <$ then  ∞ m(lim sup $E _ { n } ) = 0$ ; and (b) If $m ( E _ { n } )  0$ it may not be true that m(lim sup $E _ { n } ) = 0$

My Solution:

a. Let $\epsilon > 0 ,$ , since $\Sigma m ( E _ { n } ) < \infty ,$ , there exists an such that N $\sum m ( E _ { N } ) < \epsilon . \mathsf { S o }$

$$
\operatorname* { l i m } \operatorname* { s u p } ( E _ { n } ) = \bigcap _ { n = 1 } ^ { \infty } { \bigcup _ { k = n } ^ { \infty } { E _ { k } } } \subset { \bigcup _ { k = n } ^ { \infty } { E _ { k } } }
$$

Hence,

$$
m ( \operatorname* { l i m } \operatorname* { s u p } ( E _ { n } ) ) \leq m \left( \bigcup _ { k = N } ^ { \infty } E _ { k } \right) \leq \sum _ { k = n } ^ { \infty } m ( E _ { k } ) < \epsilon
$$

This implies that m(lim sup $E _ { n } ) = 0$

b. Let $\begin{array} { r } { E _ { 1 } = [ 0 , 1 ] , E _ { 2 } = [ 0 , \frac { 1 } { 2 } ] , E _ { 3 } = [ \frac { 1 } { 2 } , 1 ] , E _ { 4 } = [ 0 , \frac { 1 } { 4 } ] , E _ { 5 } = [ \frac { 1 } { 4 } , \frac { 1 } { 2 } ] , E _ { 6 } = [ \frac { 1 } { 2 } , \frac { 3 } { 4 } ] , E _ { 7 } = [ \frac { 3 } { 4 } , 1 ] , E _ { 8 } = [ 0 , \frac { 1 } { 8 } ] . } \end{array}$ … We repeat these definitions in this pattern, giving us that lim $\mathfrak { l } _ { n  \infty } m ( E _ { n } ) = 0$ . But for all $\textstyle n \in \mathbb { N } , \bigcup _ { k = n } ^ { \infty } E _ { k } = [ 0 , 1 ]$ implying that lim $\operatorname* { s u p } ( E _ { n } ) = [ 0 , 1 ]$ . Thus it may not be true that if $m ( { \dot { E } } _ { n } ) \to 0$ that $m ( \operatorname* { l i m } \operatorname* { s u p } ( E _ { n } ) ) = 0 .$ . QED

Prove that if $f \in L ^ { p } ( [ 0 , \infty ) ) , 1 \leq p \leq \infty$ , then $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { \infty } f ( x ) \mathrm { e } ^ { - n x } d x = 0 } \end{array}$ My Solution:

Let $A = \{ x | f ( x ) < 1 \}$ and $B = \{ x | f ( x ) \geq 1 \}$ . Note, since $f \in L ^ { p } , m ( B ) < \infty$ (because $f \in L ^ { p } , \left( \int | f | ^ { p } \right) ^ { 1 / p } < \infty$ , which implies that $m ( B )$ must be finite). So,

$$
\int _ { 0 } ^ { \infty } f ( x ) \mathrm { e } ^ { - n x } d x = \int ( f ( x ) \mathrm { e } ^ { - n x } \chi _ { A } + f ( x ) \mathrm { e } ^ { - n x } \chi _ { B } ) d x
$$

where

$$
\int _ { 0 } ^ { \infty } f ( x ) \mathrm { e } ^ { - n x } \chi _ { A } d x < \int _ { 0 } ^ { \infty } \mathrm { e } ^ { - x } = 1
$$

and

$$
\int f ( x ) \mathrm { e } ^ { - n x } \chi _ { B } d x \leq \int | f | ^ { p } \chi _ { B } < \infty
$$

since $f \in L ^ { p }$ . This argument works for any $1 \leq p < \infty$ . As for $p = \infty$ , this argument still works, however rather than saying the above, we argue $\begin{array} { r } { \int f ( x ) \mathrm { e } ^ { - n x } \chi _ { B } d x \leq } \end{array}$ ess sup $f \chi _ { B } < \infty$ . So for any such that p $1 \leq p \leq \infty$ , we can see that the integral is indeed bounded. Thus by the Lebesgue Dominated Convergence Theorem,

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { \infty } f ( x ) \mathrm { e } ^ { - n x } d x = \int _ { 0 } ^ { \infty } \operatorname* { l i m } _ { n \to \infty } f ( x ) \mathrm { e } ^ { - n x } d x = \int 0 d x = 0
$$

QED

Define the function $f : [ 0 , 1 ] \to \mathbb { R }$ by $f ( x ) = 0$ if is irrational, and by x $\textstyle f ( x ) = { \frac { 1 } { q } }$ if is rational andx $\textstyle { \boldsymbol { x } } = { \frac { p } { q } }$ when written in least terms. Decide whether or not $f$ is Riemann integrable on $[ 0 , 1 ]$ and if so, evaluate its integral.

My Solution:

Let $A = \{ x | \operatorname* { l i m } _ { x \to a } f ( x ) \neq f ( a ) \}$ , then} $A = \{ x | x \in \mathbb { Q } \}$ . Thus $m ( A ) = 0$ . Also is clearly measurable as f $\{ x | f ( x ) \geq a \} = \{ ( 0 , \infty ) \}$ . Hence is Lebesgue measurable and f $\textstyle \int f = R f$ with $\textstyle \int f = 0$ since a.e. QEDf = 0

Let $\left\{ p _ { n } \right\}$ be a sequence of polynomials. Suppose that for every point $x \in [ 0 , 1 ]$ there exists an index satisfyingn $p _ { n } ( x ) = 0$ . Prove at least one of the polynomials is identically zero.

My Solution:

Suppose there does not exist an such thatn $p _ { n } = 0$ for all $n \in \mathbb { N } .$ . Let’s define $S _ { n } = \{ x \in [ 0 , 1 ] | P _ { n } ( x ) = 0 \}$ . Note, $S _ { n }$ has to be finite since each polynomial can only have a finite number of zeros. Now consider $\textstyle \bigcup _ { n = 1 } ^ { \infty } S _ { n } \supseteq [ 0 , 1 ]$ since for each $x \in [ 0 , 1 ]$ there exists a polynomial such that $p _ { n } ( x ) = 0$ . But a countable collection of finite sets is countable. But $[ 0 , 1 ]$ is uncountable, thus giving us a contradiction. This implies that one of the polynomials must indeed be identically zero. QED

Let $A \subset \mathbb { R }$ . Prove that the following are equivalent to each other: (a) $A$ is not Lebesgue measurable; and (b) There is an $\epsilon > 0$ such that whenever $B$ is measurable and $A \subset B$ , then $m ^ { * } ( B / A ) \ge \epsilon$

My Solution:

Let not be Lebesgue measurable and suppose that for allA $\epsilon > 0$ there exists such thatB $A \subset B$ and $m ^ { * } ( B - A ) < \epsilon$ . So for $\mathsf { e v e r y } \ { \frac { 1 } { n } }$ let $B _ { n } \supset A$ and $\begin{array} { r } { m ^ { * } ( B _ { n } - A ) < \frac { 1 } { n } } \end{array}$ . Then $A \subset \cap B _ { n }$ and $m ^ { * } ( ( \cap B _ { n } ) - A ) = 0$ . Since $m ^ { * } ( ( \cap B _ { n } ) - A ) = 0$ which implies $\left( \cap B _ { n } \right) - A$ is measurable (because Lebesgue measure is complete). Hence, $A = [ ( \cup ( B _ { n } ^ { c } ) ) \cup ( \cap ( B _ { n } ) - A ) ] ^ { c }$ is measurable. This is a contradiction, thus we have proven the desired result. QED

Let $h \in L ^ { \infty } ( \mathbb { R } )$ . Define a functional $T : L ^ { 1 } ( \mathbb { R } ) \to \mathbb { R }$ by $\begin{array} { r } { T f = \int _ { \mathbb { R } } ( f h ) d m } \end{array}$ Prove that s $\begin{array} { r } { { 1 } \mathbb { P } _ { | | f | | _ { 1 } \leq 1 } T f = | | h | | _ { \infty } } \end{array}$

My Solution:

Will show $\leq :$

$$
\operatorname* { s u p } _ { | | f | | _ { 1 } \le 1 } T f = \operatorname* { s u p } _ { | | f | | _ { 1 } \le 1 } \int f h \le \operatorname* { s u p } _ { | | f | | _ { 1 } \le 1 } | | f | | _ { 1 } | | h | | _ { \infty }
$$

Note, by Holder’s since we have $1 , \infty .$

$$
\leq 1 \cdot \| h \| _ { \infty } = \| h \| _ { \infty }
$$

Will show $\geq :$

We may assume $| | h | | _ { \infty } = M > 0$ is -finite, so there existsR σ $F _ { n }$ increasing towards such that x m $( F _ { n } ) < a$ . Define $A _ { n } = \{ x \in F _ { n } | | h ( x ) | > a \}$ for $0 < a < M$ , to be fixed. Hence $m ( A _ { n } ) > 0$ . Define $\begin{array} { r } { g _ { n } ( x ) = \frac { \mathrm { s g n } ( h ) - \chi _ { A _ { n } } } { m ( A _ { n } ) } } \end{array}$ , which implies $| | g _ { n } | | _ { 1 } = 1$ for all andn $\textstyle \int h g _ { n } = a$ for all . Thus n $a < \int h g _ { n }$ for all . This implies n $\begin{array} { r } { \operatorname* { s u p } _ { 0 < a < M } a < \operatorname* { s u p } _ { | | g _ { n } | | _ { 1 } \leq 1 } \int h g _ { n } } \end{array}$

$$
| | f | | _ { \infty } = M < \operatorname* { s u p } _ { | | f | | _ { 1 } \le 1 } \int f h = \operatorname* { s u p } _ { | | f | | _ { 1 } \le 1 } T f
$$

Thus we have proven the desired result. QED

## August 2016

Let $C \subset [ 0 , 1 ]$ be a closed set. Prove that $\chi _ { C }$ is Riemann integrable iff $\partial C$ has Lebesgue measure zero.

My Solution:

Assume that $\partial C$ has Lesbegue measure zero. This implies that $m ( \{ x | \operatorname* { l i m } _ { x \to a } f ( x ) \neq f ( a ) \} ) = 0$ . Thus the Riemann integral exists and agrees with the Lebesgue integral.

Now assume that $\chi _ { C }$ is Riemann integrable. This is true iff the Lesbegue integral exists and $n ( \{ x | \operatorname* { l i m } _ { x \to a } f ( x ) \neq f ( a ) \} ) = 0 . \operatorname { s o } \chi _ { C } \lvert$ is discontinuous at its boundary points, which implies that $m ( \partial C ) = 0 . \mathsf { Q E D }$

Let $S \subset \mathbb { R }$ Prove the following statements are equivalent: (a) $S$ is Lebesgue measurable and (b) There is a $G _ { \delta }$ set $G$ and a set $N$ of measure zero such that $S = G - N$ .

My Solution:

$( b \implies a ) :$ Given $G$ is a $\mathbf { \Omega } _ { 1 } G _ { \delta }$ set, must then be Borel measurable. Thus it is also Lebesgue measurable.G $N$ must be Lebesgue measurable as well since the Lebesgue -algebra is complete. Thusσ $S = G - N$ is Lebesgue measurable.

$( a \implies b ) :$ This follows directly from a proposition stating that if $A \subset [ 0 , 1 ]$ is a Lebesgue measurable set, and is a Lebesgue measure, m then there exists a set which contains that is the countable intersection of a decreasing sequence of open sets andH A $m ( H - A ) = 0$ QED

If $f$ is nonnegative and integrable on $[ 0 , 1 ]$ , then

lim $\begin{array} { r } { \mathsf { l } _ { n \to \infty } \int _ { 0 } ^ { 1 } \sqrt [ n ] { f } = m \{ x | f ( x ) > 0 \} } \end{array}$

My Solution:

$$
\int _ { 0 } ^ { 1 } \sqrt [ n ] { f } \ d t = \int _ { 0 } ^ { 1 } \sqrt [ n ] { f } \ d t \cdot \chi _ { f = 0 } + \int _ { 0 } ^ { 1 } \sqrt [ n ] { f } \ d t \cdot \chi _ { f > 0 }
$$

where $\begin{array} { r } { \int _ { 0 } ^ { 1 } \sqrt [ n ] { f } \cdot \chi _ { f = 0 } = \int _ { 0 } ^ { 1 } \sqrt [ n ] { 0 } = 0 } \end{array}$ . Thus,

$$
\int _ { 0 } ^ { 1 } \sqrt [ n ] { f } = \int _ { 0 } ^ { 1 } \sqrt [ n ] { f } \cdot \chi _ { f > 0 }
$$

Since $f$ is integrable, we know that $\begin{array} { r } { \int _ { 0 } ^ { 1 } \sqrt [ n ] { f } \cdot \chi _ { f > 1 } < \int _ { 0 } ^ { 1 } f < \infty } \end{array}$ , and $\int _ { 0 } ^ { 1 } \sqrt [ n ] { f } \cdot \chi _ { 0 < f < 1 }$ must be bounded, thus $\sqrt [ n ] { f }$ is integrable as well. So,

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } { \sqrt [ [object Object] ] { \cdot } } \chi _ { f > 0 } = \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n \to \infty } { \sqrt [ [object Object] ] { \cdot } } \chi _ { f > 0 }
$$

by the D.C.T., and thus,

$$
= \int _ { 0 } ^ { 1 } 1 \cdot \chi _ { f > 0 } = m ( \{ x | f ( x ) > 0 \} )
$$

QED

Let $f \in L ^ { 1 } ( \mathbb { R } )$ . If $\textstyle \int _ { a } ^ { b } f = 0$ for all rational numbers and a $b$ with $a < b$ , then $\displaystyle f = 0 \mathsf { a } . \mathsf { e }$

My Solution:

We will claim here that $f$ integrates to over arbitrary open sets. Thus for any 0 $\epsilon > 0 \AA$ , choose an open set such that B $A = \{ f > 0 \} \subset B$ and $m ( B - A ) < \delta$ Hence

$$
\left| \int _ { A } f \right| \leq \left| \int _ { B } f - \int _ { A } f \right| = \left| \int _ { B - A } f \right| \leq \int _ { B - A } | f | < \epsilon
$$

because $m ( B - A ) < \delta .$ Thus the integral is since this is true for all .0 ϵ

We must now prove our claim in order to complete the problem. For any $( a , b ) \in \mathbb { R } \times \mathbb { R }$ , there exists $\{ a _ { n } \} , \{ b _ { n } \} \in \mathbb { Q }$ such that $a _ { n }$ decreases to anda $b _ { n }$ increases to as goes to infinity. Thusb n $\textstyle \int _ { ( a , b ) } f = \int _ { \bigcup ( a _ { n } , b _ { n } ) } f .$ Using this, and the dominated convergence theorem, we find that

$$
\int _ { \bigcup ( a _ { n } , b _ { n } ) } f = \operatorname* { l i m } _ { n \to \infty } \int _ { ( a _ { n } , b _ { n } ) } f = 0
$$

with $| f |$ as the majorant since $f \in L ^ { 1 }$ . Now let $\textstyle B = \bigcup _ { n = 1 } ^ { \infty } ( a _ { n } , b _ { n } )$ with $\left( a _ { n } , b _ { n } \right)$ being arbitrary disjoint intervals. Then

$$
\int _ { B } f = \int \sum _ { n = 1 } ^ { \infty } f \cdot \chi _ { ( a _ { n } , b _ { n } ) } 
$$

By the dominated convergence theorem,

$$
\int \sum _ { n = 1 } ^ { \infty } f \cdot \chi _ { ( a _ { n } , b _ { n } ) } = \sum _ { n = 1 } ^ { \infty } \int f \cdot \chi _ { ( a _ { n } , b _ { n } ) } = \sum 0 = 0
$$

with $| f |$ as the majorant because $f \in L ^ { 1 }$ . Thus $\textstyle \int _ { B } f = 0$ for any open set . A similar proof holds for B $m ( \{ x | f ( x ) < 0 \} ) = 0$ . Hence a.e. QEDf = 0

Suppose that $f \in L ^ { 2 } ( [ 0 , 1 ] )$ and $| | f | | _ { 2 } = 1$ . Define $g ( x ) = x f ( x )$ . Prove that $g \in L ^ { 1 } ( [ 0 , 1 ] )$ and that $\begin{array} { r } { \left| \left| g \right| \right| _ { 1 } \le \frac { 1 } { \sqrt { 3 } } } \end{array}$

My Solution:

For $x \in L ^ { 2 } ( [ 0 , 1 ] )$ , we have

$$
\left( \int _ { 0 } ^ { 1 } | f | ^ { 2 } \right) ^ { 1 / 2 } = \left( \frac { 1 } { 3 } x ^ { 3 } | _ { 0 } ^ { 1 } \right) ^ { 1 / 2 } < \infty
$$

So $x \in L ^ { 2 }$ . Given this, we can see that

$$
| | x \cdot f ( x ) | | _ { 1 } \leq | | x | | _ { 2 } | | f | | _ { 2 }
$$

by Holders’ because and are conjugate. Then,2 2

$$
| | x | | _ { 2 } | | f | | _ { 2 } \leq \left( { \frac { 1 } { 3 } } x ^ { 3 } | _ { 0 } ^ { 1 } \right) ^ { 1 / 2 } \cdot 1 \leq { \frac { 1 } { \sqrt { 3 } } }
$$

QED

Let $\{ a _ { k } \}$ be a sequence of real numbers with the property that $| a _ { k } | \leq 1$ for all $k .$ Prove that both series $\begin{array} { r } { f ( x ) = \sum _ { k = 1 } ^ { \infty } a _ { k } x ^ { k } , g ( x ) = \sum _ { k = 1 } ^ { \infty } \dot { k } a _ { k } x ^ { k - 1 } } \end{array}$ converge uniformly on every compact subinterval of $( - 1 , 1 )$ and that $\bar { f } ^ { \prime } ( x ) = g ( x )$ for all ${ \pmb x } \in ( - 1 , 1 )$

My Solution:

Since $\left| a _ { k } \right| \leq 1$

$$
\sum _ { k = 1 } ^ { \infty } a _ { k } x ^ { k } \leq \sum _ { k = 1 } ^ { \infty } x ^ { k }
$$

which converges uniformly because $| x | < 1$ by the Weirstrass-M test (and because it’s a geometric series). Let $C \subset [ 0 , 1 ]$ be a compact interval of $( - 1 , 1 )$ and let a = max $\{ | x | : x \in C \}$ . Then $\textstyle \sum \left| x \right| ^ { k } \leq \sum a ^ { k }$ which converges because it’s a geometric sequence. Now we apply the Weirstrass M-test to give us the desired result.

As for proving that $f ^ { \prime } ( x ) = g ( x )$ , we simply note that by definition of differentiation on power series that this is true (with simple calculus II logic). QED

Give an example of a continuous function $f : [ 0 , 1 ] \to \mathbb { R }$ with the property that $f ( 0 ) = 0 , f ( 1 ) = 1$ , yet $f ^ { \prime } ( x ) \leq - 1$ for almost every $x \in [ 0 , 1 ]$ .

My Solution:

Let $C ( x )$ be the Cantor function on $[ 0 , 1 ]$ . Consider $f ( x ) = 2 C ( x ) - x$ . Then $f ( 0 ) = 2 \cdot 0 - 0 = 0$ and $f ( 1 ) = 2 \cdot 1 - 1 = 1$ . Also, almost everywhere the derivative of the Cantor function is 0 (because almost everywhere it is constant). Then the derivative almost everywhere of $f ( x )$ would be $f ^ { \prime } ( x ) = - 1$ almost everywhere.

Let $E _ { 1 } , E _ { 2 } , E _ { 3 } , \dots$ be a sequence of measurable subsets of with the property. R that $\textstyle \sum _ { n = 1 } ^ { \infty } m ( E _ { n } ) < \infty$ . Show almost every $x \in \mathbb { R }$ is contained in only finitely many of the $E _ { n }$

My Solution:

By way of contradiction, suppose there exists an $I \subset \mathbb { R }$ such that $m ( I ) = c > 0$ . Also assume that $I \subset E _ { n } ^ { * }$ for all wheren $\{ E _ { n } ^ { * } \}$ is a subsequence of $\{ E _ { n } \}$ . Bu t

$$
\sum _ { n = 1 } ^ { \infty } m ( E _ { n } ^ { * } ) \geq \sum _ { n = 1 } ^ { \infty } m ( I ) = \sum _ { n = 1 } ^ { \infty } c
$$

which diverges because $c > 0 .$ . Thus by contradiction, we have proven the desired result. QED

Let $f : \lceil 0 , 1 \rceil  \mathbb { R }$ be Lebesgue measurable. Prove that if $p \leq f ( x ) \leq q$ for all $x \in [ 0 , 1 ]$ , then $\int _ { [ 0 , 1 ] } f$ exists and $\begin{array} { r } { p \leq \int _ { [ 0 , 1 ] } f \leq q } \end{array}$

My Solution:

First off, it is known that $\begin{array} { r } { \int _ { [ 0 , 1 ] } 1 = 1 } \end{array}$ . Since $p \leq f \leq q ,$ and since we’re integrating between and , we can easily see then that 0 1 $\begin{array} { r } { p \leq \int _ { [ 0 , 1 ] } f \leq q . \mathsf { L e t } a = \operatorname* { m a x } \{ | p | , | q | \} } \end{array}$ , then $| f | < a$ which implies that $\int _ { [ 0 , 1 ] } | f | < a$ . Thus is integrable. QED f

Define a sequence of functions $f _ { n } \in L ^ { 1 } [ 0 , 1 ]$ by $f _ { n } ( x ) = n \mathfrak { i } \mathfrak { x } \le \frac { 1 } { n }$ and $f ( x ) = 0 { \mathrm { ~ i f ~ } } x > { \frac { 1 } { n } }$ . Does $f _ { n }$ converge in $L ^ { 1 } ( [ 0 , 1 ] ) \ ?$ If so, to what function? My Solution:

Suppose $f _ { n } \to f \mathfrak { i n } L ^ { p }$ . Then $\vert \vert f _ { n } \vert \vert _ { 1 } \to \vert \vert f \vert \vert _ { 1 }$ . But $\begin{array} { r } { \int | f _ { n } | = \frac { 1 } { n } \cdot n = 1 } \end{array}$ for all . Hence n $| | f | | = 1$ . However, this is a contradiction because li $\scriptstyle \mathbf { 1 } _ { n \to \infty } f _ { n } = 0$ , thus it does not converge in $L ^ { 1 } ( [ 0 , 1 ] )$ . QED

## January 2016

Let $S$ be dense in $\mathbb { R }$ and $f : \mathbb { R } \to \mathbb { R }$ . Prove or give a counterexample: is f measurable iff $\{ x : f ( x ) \geq s \}$ is measurable for all $s \in S$

My Solution:

First assume $f$ is measurable. This implies that $\{ x | f ( x ) \geq a \}$ is Lebesgue measurable for all $a \in \mathbb { R }$ . Hence $\{ x | f ( x ) \geq s \}$ is Lebesgue measurable for all $s \in S .$

Now assume that $\{ x : f ( x ) \geq s \}$ is measurable for all $s \in S$ . It suffices to show that $\{ x : f ( x ) > s \}$ is measurable for all $s \in S ^ { c }$ . So , le t $t \in S ^ { c }$ , given that is dense in . Let S R $\{ t _ { n } \} \subset S$ such that $t _ { n }$ decreases to . Thus,t

$$
\{ x : f ( x ) > t \} = \bigcup _ { n = 1 } ^ { \infty } \{ x | f ( x ) \geq t _ { n } \}
$$

is the union of measurable sets. Hence $f$ is measurable. QED

Suppose $\lambda ( S )$ denotes the Lebesgue measure of the set $S \subset \mathbb { R }$ . Let $g : [ 0 , 1 ]  \mathbb { R }$ be absolutely continuous and $E \subset [ 0 , 1 ]$ be such that $\lambda ( E ) = 0$ Prove that $\lambda ( g ( E ) ) = 0$

My Solution:

Given $E \subset [ 0 , 1 ]$ with $\lambda ( E ) = 0 , \mathsf { l e t } \left\{ \left( a _ { i } , b _ { i } \right) \right\}$ be a collection of disjoint intervals covering withE ${ \textstyle \sum _ { i = 1 } ^ { n } | b _ { i } - a _ { i } | < \delta . g }$ is absolutely continuous, which implies that it must also be continuous. Thus for each $( a _ { i } , b _ { i } ) , \mathsf { l e t } \left( c _ { i } , d _ { i } \right) \subseteq ( a _ { i } , \overline { { b _ { i } } } )$ such that $\{ f ( c _ { i } ) , f ( d _ { i } ) \} \in \{ \operatorname* { m i n } ( f ) _ { ( a _ { i } , b _ { i } ) } , \operatorname* { m a x } ( f ) _ { ( a _ { i } , b _ { i } ) } \}$ . Also, recall that because is continuous, this implies that for allg $\epsilon > 0$ , there exists a  δ such that $| f ( a _ { i } ) - f ( b _ { i } ) | < \epsilon$ where $| a _ { i } - b _ { i } | < \delta$ . Now notice that

$$
\sum _ { i = 1 } ^ { n } | c _ { i } - d _ { i } | < \sum _ { i = 1 } ^ { n } | b _ { i } - a _ { i } | < \delta
$$

because $( c _ { i } , d _ { i } ) \subseteq ( a _ { i } , b _ { i } )$ . Thus

$$
\lambda ( g ( E ) ) \leq \lambda \left( g \left( { \bigcup _ { i = 1 } ^ { \infty } ( a _ { i } , b _ { i } ) } \right) \right) = \lambda \left( { \bigcup _ { i = 1 } ^ { \infty } g ( a _ { i } , b _ { i } ) } \right)
$$

$$
\leq \sum _ { i = 1 } ^ { \infty } \lambda ( g ( a _ { i } , b _ { i } ) ) \leq \sum _ { i = 1 } ^ { \infty } | f ( c _ { i } ) - f ( d _ { i } ) | < \epsilon
$$

because $\sum \left| c _ { i } - d _ { i } \right| < \delta .$ Thus $\lambda ( g ( E ) ) = 0 . \mathsf { Q E D }$

Let $f _ { n } ( x ) = x ^ { n }$ for each $n \geq 1$ . Prove that the sequence $\{ f _ { n } \}$ converges uniformly on $[ - \delta , \delta ]$ for each $0 < \delta < 1$ , and converges non-uniformly on $( - 1 , 1 )$

My Solution:

Before we begin, note that $\mathfrak { i } \left| x \right| ^ { n } < \epsilon ,$ then

$$
\ln ( | x | ^ { n } ) < \ln ( \epsilon ) \implies n \ln ( | x | ) < \ln ( \epsilon )
$$

$$
\implies n < \frac { \ln ( \epsilon ) } { \ln ( | x | ) }
$$

. This will be useful in our proof.

Let $\delta \in ( 0 , 1 )$ and $\epsilon > 0$ . Also let $\begin{array} { r } { N = \frac { \ln ( \epsilon ) } { \ln ( \delta ) } } \end{array}$ . Hence for $n \geq N$ (thus $\begin{array} { r } { n \ge \frac { \ln ( \epsilon ) } { \ln ( \delta ) } ) } \end{array}$ ), ϵ ) n ln $\ln ( \delta ) \leq \ln ( \epsilon )$ which implies that $\mathbf { n } ( \delta ^ { n } ) \leq \ln ( \epsilon )$ The reason that the inequality changes directions here is because for $\delta \in ( 0 , 1 )$ and for very small (specifically less than ), ϵ 1

$\ln ( \delta ) , \ln ( \epsilon ) < 0$ . Thus, we can see that $\delta ^ { n } \leq \epsilon$ , which implies that $x ^ { n } < \delta ^ { n } < \epsilon$ for all $\boldsymbol { x } \in ( - \delta , \delta )$ . Thus $\{ f _ { n } \}$ converges uniformly on $[ - \delta , \delta ]$

If we fix $x \in ( - 1 , 1 )$ , this implies that $x ^ { n } < \epsilon$ by our previous point in the proof. However, it is not uniform since depends on . Thus we N x have proven the desired result. QED

Let $m ( G )$ denote the Lebesgue measure of the set . Find an open set which is G G dense in $[ 0 , 1 ]$ such that $m ( G ) < 1$ and $m ( G \cap I ) > 0$ for any interval $I \subset [ 0 , \bar { 1 } ]$

My Solution:

Let $\{ q _ { i } \} _ { i = : } ^ { \infty }$ represent the rationals in1 $\mathbb { Q } \cap [ 0 , 1 ]$ . For each define n $I _ { n }$ as an interval containing $\begin{array} { r } { q _ { n } , m ( I _ { n } ) < \frac { 1 } { 4 \cdot 2 ^ { n } } } \end{array}$ and $I _ { n } \subset [ 0 , 1 ]$ . L e t $\textstyle G = \bigcup _ { i = 1 } ^ { \infty } I _ { n }$ with

$$
m ( G ) = m \left( \bigcup _ { i = 1 } ^ { \infty } I _ { n } \right) \leq \sum _ { i = 1 } ^ { \infty } m ( I _ { n } )
$$

$$
< \sum _ { i = 1 } ^ { \infty } { \frac { 1 } { 4 \cdot 2 ^ { n } } } = { \frac { 1 } { 4 } } \cdot { \frac { 1 } { 1 - ( 1 / 2 ) } } = { \frac { 1 } { 2 } }
$$

Since contains the rationals on , it is also dense on . is open because it is the countable union of open intervals on . letG [0, 1] [0, 1] G [0, 1] $I \subset [ 0 ,$ . It must contain a rational, which implies that it intersects any 1] $I _ { n }$ non-trivially, thus $m ( I \cap G ) > 0$ . Thus is a dense open set onG such that the measure of is less than and intersects any interval of[0, 1] G 1 $[ 0 , 1 ]$ non-trivially. QED

Is $L ^ { p } ( [ a , b ] )$ separable, where $1 < p < \infty ?$

My Solution:

Yes! First note that separable means that it contains a countable subset that is dense in .X

Let $S [ a , b ] \subset L ^ { p } ( [ a , b ] )$ be step functions on and let [a, b] $S _ { \mathbb { Q } } [ a , b ] \subset S [ a , b ]$ be step functions of $[ a , b ]$ with rational endpoints. Since $\mathbb { Q }$ is dense in $\mathbb { R } , S _ { \mathbb { Q } } [ a , b ]$ is dense in $S [ a , b ]$ thus it’s dense in $L ^ { \vec { p } } ( [ a , \dot { b } ] )$ . QED)

Suppose that $1 < p , q < \infty$ and that $\textstyle { \frac { 1 } { p } } + { \frac { 1 } { q } } = 1$ . Prove that if $f _ { n } \to f$ in $L ^ { p } ( \mathbb { R } )$ and $g _ { n } \to g$ in $L ^ { q } ( \mathbb { R } )$ , then $f _ { n } g _ { n } \to f g \mathsf { i n } L ^ { 1 } ( \mathbb { R } )$

My Solution:

Here it is sufficient to show that lim $\begin{array} { r } { \mathbf { 1 } _ { n  \infty } | | f _ { n } g _ { n } - f g | | = 0 . } \end{array}$ Well,

$$
\begin{array} { r l r } {  { \operatorname* { l i m } _ { n \to \infty } | | f _ { n } g _ { n } - f g | | _ { 1 } = \overset { \mathrm { l i m } } { n \to \infty } | | f _ { n } g _ { n } - f _ { n } g + f _ { n } g - f g | | _ { 1 } } } \\ & { } & { = \underset { n \to \infty } { \operatorname* { l i m } } | | f _ { n } g _ { n } - f _ { n } g | | _ { 1 } + | | f _ { n } g - f g | | _ { 1 } \quad } \\ & { } & { \leq \underset { n \to \infty } { \operatorname* { l i m } } | | f _ { n } | | _ { p } \cdot | | g _ { n } - g | | _ { q } + | | f _ { n } - f | | _ { p } \cdot | | g | | _ { q } = 0 } \end{array}
$$

by Holder’s Inequality, where lim $_ { n \to \infty } \left| \left| f _ { n } \right| \right| _ { p } \to \left| \left| f \right| \right| _ { p } < \infty , \left| \left| g _ { n } - g \right| \right| _ { q } \to 0 ,$ , and $\vert \vert f _ { n } - f \vert \vert _ { p } \to 0$ . Thus we have proven the desired result. QED

Assume that $f \in L ^ { \infty } ( [ 0 , 1 ] )$ . Prove that $f \in L ^ { p } ( [ 0 , 1 ] )$ for each $1 \leq p < \infty$ and that $\begin{array} { r } { | | \boldsymbol { f } | | _ { \infty } = \operatorname* { l i m } _ { p \to \infty } | | \boldsymbol { f } | | _ { p } } \end{array}$

My Solution:

To complete this proof, we will divide the problem into a group of lemmas and prove them to get the desired result.

Lemma 1: $f \in L ^ { \infty } ( [ 0 , 1 ] ) \implies f \in L ^ { 1 } ( [ 0 , 1 ] )$ Proof: Assume $f \in L ^ { \infty }$ . Then $f \leq m = \exp ( f )$ a.e. Then $\begin{array} { r } { \int _ { [ 0 , 1 ] } | f | \leq \int _ { [ 0 , 1 ] } m = m < \infty . } \end{array}$ Thus $f \in L ^ { 1 }$

Lemma 2: Assume $f \in L ^ { \infty } ( [ 0 , 1 ] )$ . Then $f \in L ^ { p } ( [ 0 , 1 ] )$ for $1 \le p \le$ . Proof: Consider∞ $\begin{array} { r } { \int | f | ^ { p } = \int _ { \{ | f | < 1 \} } | f | ^ { p } + \int _ { \{ | f | \geq 1 \} } | f | ^ { p } } \end{array}$

where for $\begin{array} { r } { p > 1 , \int _ { \{ | f | < 1 \} } | f | ^ { p } < \int _ { \{ | f | < 1 \} } | f | < } \end{array}$ since ∞ $f \in L ^ { 1 }$

where $\begin{array} { r } { \int _ { \{ | f | \geq 1 \} } | f | ^ { p } \leq \int _ { \{ | f | \geq 1 \} } m ^ { p } = m ^ { p } \cdot m ( \{ | f | \geq 1 \} ) < \infty } \end{array}$ . Thus $\int | f | ^ { p } < \infty$ , which implies $f \in L ^ { p }$

Lemma 3: lim sup $| | f | | \leq | | f | | _ { \infty }$ Proof: $| f | \leq | | f | | _ { \infty }$ a.e. This implies that $| f | ^ { p } \leq | | f | | _ { \infty } ^ { p }$ , which implies $\begin{array} { r } { ( \int _ { [ 0 , 1 ] } | f | ^ { p } ) ^ { 1 / p } \leq ( \int _ { [ 0 , 1 ] } | | f | | _ { \infty } ^ { p } ) ^ { 1 / p } = | | f | | _ { \infty } < \infty } \end{array}$ . Hence  lim sup $\| f \| _ { p } \leq \| f \| _ { \infty } .$

Lemma $\pmb { 4 } ; | | f | | _ { \infty } \leq$ lim inf $| | f | | _ { p }$ Proof: Let $t \in [ 0 , m = | | { \boldsymbol { f } } | | _ { \infty } )$ . Then $\textstyle { \int | f | = \int _ { \{ | f | < t \} } | f | + \int _ { \{ | f | \geq t \} } | f | }$ . Then $\textstyle \int | f | ^ { p } \geq \int _ { \{ | f | < 1 \} } | f | ^ { p } \geq \int _ { \{ | t | < 1 \} } t ^ { p }$ . Hence $\begin{array} { r } { ( \int | f | ^ { p } ) ^ { ( 1 / p ) } \ge ( \int _ { \{ | f | < t \} } t ^ { p } ) ^ { 1 / p } = t \cdot m ( \{ | f | < t \} ) ^ { 1 / p } } \end{array}$ . This implies that lim inf $| | f | | _ { p } \geq$ lim inf $t \cdot m ( \{ | f | < t \} ) ^ { 1 / p } = t \cdot 1$ . Thus lim inf $| | f | | _ { p } \geq t$ for all $t \in [ 0 , | | f | | _ { \infty } )$ . It follows that by our claims then that lim sup $| | f | | _ { p } \leq | | f | | _ { \infty } \leq \operatorname* { l i m i n f } | | f | | _ { p }$ . Thus we have proven the desired result. QED

## August 2015

Let $C \subset \mathbb { R }$ denote the Cantor set. Let $\chi _ { C } ( x ) = 1$ if $x \in C$ and otherwise. 0 Explain why $\chi _ { C }$ is Riemann integrable and compute $\textstyle \int _ { 0 } ^ { 1 } \chi _ { C } ( x ) d x$

My Solution:

Given that $m ( C ) = 0 , \chi _ { C } ( x ) = 0$ a.e. which implies that $\textstyle \int \chi _ { C } = 0$ and since $\chi _ { C } ( \boldsymbol { x } )$ is bounded with . Thus . QEDm({x| limx→a f(x) ≠ f(a)}) = m(C) = 0 Rf = ∫ f = 0

Let $E \subset \mathbb { R }$ be a Lebesgue measurable set with $m ( E ) = 1$ . Prove there exists a Lebesgue measurable set $F \subset E$ with $\begin{array} { r } { m ( F ) = \frac { 1 } { 2 } } \end{array}$

My Solution:

$\begin{array} { r } { E = \bigcup _ { n = 1 } ^ { \infty } E \cap [ n , n + 1 ] } \end{array}$ . This implies that  m $\begin{array} { r } { \ i ( E ) = \operatorname* { l i m } _ { n  \infty } { m } ( E \cap [ - n , n ] ) = 1 } \end{array}$ . Pick a sufficiently large $n \in \mathbb { N }$ such that $\begin{array} { r } { m ( E \cap [ - n , n ] ) > \frac { 1 } { 2 } } \end{array}$ . Consider $\begin{array} { r } { f ( x ) = \int _ { - n } ^ { x } \chi _ { E } \mathrm { f o r } x \in [ - n , n ] } \end{array}$ . Since is continuous with f $f ( - n ) = 0$ and $\begin{array} { r } { f ( n ) > \frac { 1 } { 2 } } \end{array}$ , there exists $c \in [ - n , n ]$ such that $\begin{array} { r } { \dot { \boldsymbol { f } } ( \boldsymbol { c } ) = \frac { 1 } { 2 } } \end{array}$ by the Intermediate Value Theorem. Thus $( - n , n ) \cap E$ is a Lebesgue measurable set with $m ( ( - n , c ) \cap E ) = { \frac { 1 } { 2 } }$ . QED

Let $( X , A , \mu )$ be a measure space. If $f _ { n } : X \to \mathbb { R }$ is a sequence of functions such that $\textstyle \sum _ { n = 1 } ^ { \infty } \int _ { X } | f _ { n } | d \mu$ converges, then prove that $f _ { n } \to 0$ almost everywhere. My Solution:

$$
\begin{array} { c } { { \displaystyle \sum _ { n = 1 } ^ { \infty } \int _ { X } | f _ { n } | d \mu = \operatorname* { l i m } _ { k \to \infty } \sum _ { n = 1 } ^ { k } \int _ { X } | f _ { n } | d \mu = \operatorname* { l i m } _ { k \to \infty } \int _ { X } \sum _ { n = 1 } ^ { k } | f _ { n } | d \mu } } \\ { { = \displaystyle \int _ { X } \operatorname* { l i m } _ { k \to \infty } \sum _ { n = 1 } ^ { k } | f _ { n } | d \mu = \displaystyle \int _ { X } \sum _ { n = 1 } ^ { \infty } | f _ { n } | d \mu < \infty } } \end{array}
$$

by the M.C.T. since $\textstyle \sum _ { i = 1 } ^ { k } | f _ { n } |$ is increasing. Thus $| f _ { n } | \to 0$ almost everywhere because it’s integrable when approaches . Hence  n ∞ $f _ { n } \to 0$ almost everywhere. QED

Prove that $f ( x ) = 0 { \mathfrak { i } } \mathfrak { r } x = 0$ and $\begin{array} { r } { f ( x ) = x ^ { 2 } \cos ( \frac { 1 } { x ^ { 2 } } ) } \end{array}$ if  x $\neq 0$ is continuous but not absolutely continuous on $[ - 1 , 1 ]$

My Solution:

Consider $\scriptstyle x ^ { 2 } \cos \left( { \frac { 1 } { x ^ { 2 } } } \right)$ , which is constructed of functions that are continuous everywhere on their domains. So it is continuous on excluding R . To show continuity at{0} $x = 0 _ { ; }$ consider that $\begin{array} { r } { - 1 \leq \cos \left( \frac { 1 } { x ^ { 2 } } \right) \leq 1 } \end{array}$ which implies that $\begin{array} { r } { - x ^ { 2 } \le x ^ { 2 } \cos \left( \frac { 1 } { x ^ { 2 } } \right) \le x ^ { 2 } } \end{array}$ with li $\begin{array} { r } { \mathbf { m } _ { x  0 } - x ^ { 2 } = \operatorname* { l i m } _ { x  0 } x ^ { 2 } = 0 } \end{array}$ Hence by the squeeze theorem,   lim $\begin{array} { r } { \mathfrak { l } _ { x \to 0 } x ^ { 2 } \cos \left( \frac { 1 } { x ^ { 2 } } \right) = f ( 0 ) = 0 . } \end{array}$

Suppose $f$ is absolutely continuous on $[ - 1 , 1 ]$ . Hence it is of bounded-variation on $[ - 1 , 1 ]$ , thus $V _ { f } [ 0 , 1 ] < \infty$ . Consider the partition with endpoints

$$
P = \{ - 1 \} \cup \left[ \{ \pm { \sqrt { \frac { 1 } { n \pi } } } : n \in \mathbb { N } \} \cap [ - 1 , 1 ] \right] \cup \{ 1 \}
$$

Hence for $x _ { i } , x _ { i + 1 } \in P _ $

$$
\begin{array} { c } { { \displaystyle \sum _ { n = 1 } ^ { \infty } | f ( x _ { i } ) - f ( x _ { i + 1 } ) | = \displaystyle \sum _ { n = 1 } ^ { \infty } \left| f \left( \sqrt { \frac { 1 } { n \pi } } \right) - f \left( \sqrt { \frac { 1 } { ( n + 1 ) \pi } } \right) \right| } } \\ { { \displaystyle = \sum _ { n = 1 } ^ { \infty } \left| \left[ \left( \sqrt { \frac { 1 } { n \pi } } \right) ^ { 2 } \cdot \cos \left( \frac { 1 } { \sqrt { \frac { 1 } { ( n + 1 ) \pi } } ^ { 2 } } \right) \right] - \left[ \left( \sqrt { \frac { 1 } { ( n + 1 ) \pi } } \right) ^ { 2 } \cdot \cos \left( \frac { 1 } { \sqrt { \frac { 1 } { ( n + 1 ) \pi } } ^ { 2 } } \right) \right] \right| } } \\ { { \displaystyle = \sum _ { n = 1 } ^ { \infty } \left| \left( \frac { 1 } { n \pi } \cos ( n \pi ) \right) - \left( \frac { 1 } { ( n + 1 ) \pi } \cos ( ( n + 1 ) \pi ) \right) \right| = \sum _ { n = 1 } ^ { \infty } \left| \frac { 1 } { n \pi } - \frac { - 1 } { ( n + 1 ) \pi } \right| } } \end{array}
$$

because is even andn $n + 1$ is odd. The above sum is equal to $\begin{array} { r } { { \frac { 1 } { \pi } } \sum _ { n = 1 } ^ { \infty } \left| { \frac { 2 n + 1 } { n ^ { 2 } + n } } \right| } \end{array}$ which diverges because it’s a harmonic series. Thus $V _ { f } [ 0 , 1 ] \not \prec \infty$ . This is a contradiction to the assumption of $f$ being absolutely continuous, thus we have proven the desired result. QED

Let $( X , A , \mu )$ be a finite measure space. If $f$ is -measurable andμ $p \leq f ( x ) \leq q$ for all $x \in X$ , then prove that $\int _ { X } f d \mu$ exists and $\begin{array} { r } { p \mu ( X ) \leq \int _ { X } f d \mu \leq q \mu ( X ) } \end{array}$

My Solution:

Since is finite, andX $p \leq f \leq q , \mu ( X ) = \textstyle \int _ { X }$ . This implies that1dμ $p \cdot \mu ( X ) \leq \int _ { X } f d \mu \leq q \mu ( X )$

Now, we must show that $\textstyle { \int _ { X } f d \mu }$ is integrable. Consider $| f | \leq \operatorname* { m a x } \{ | p | , | q | \} = M$ Hence $| f | \leq M$ . This implies that $\begin{array} { r } { \int _ { X } | f | d \mu \leq \mu ( X ) \cdot M < \infty } \end{array}$ . Hence is integrable. QED f

Suppose that $1 < q , p < \infty$ and that $\textstyle { \frac { 1 } { p } } + { \frac { 1 } { q } } = 1$ . Prove that if $f _ { n } \to f$ in $L ^ { p } ( \mathbb { R } )$ and $g _ { n }  g$ in $L ^ { q } ( \mathbb { R } )$ , then $f _ { n } g _ { n } \to f g$ in $L ^ { 1 } ( \mathbb { R } )$

My Solution:

It is sufficient to show that the lim $_ { \cdot n  \infty } | | f _ { n } g _ { n } - f g | | _ { 1 } = 0$ . Well,

$$
\begin{array} { r l r } {  { \operatorname* { l i m } _ { n \to \infty } | | f _ { n } g _ { n } - f g | | _ { 1 } = \operatorname* { l i m } _ { n \to \infty } | | f _ { n } g _ { n } - f _ { n } g | | _ { 1 } + | | f _ { n } g - f g | | _ { 1 } } } \\ & { } & { \leq \operatorname* { l i m } _ { n \to \infty } | | f _ { n } | | _ { p } | | g _ { n } - g | | _ { q } + | | g | | _ { q } | | f _ { n } - f | | _ { p } } \end{array}
$$

by Holder’s Inequality where lim $1 _ { n \to \infty } | | f _ { n } | | _ { p } \to | | f | | _ { p } < \infty$ . Thus $\vert \vert g _ { n } - g \vert \vert _ { q } \to 0$ and $\vert \vert f _ { n } - f \vert \vert _ { p } \to 0$ . So the above limit does in fact imply that $f _ { n } g _ { n } \to f g \mathrm { i n } L ^ { 1 } ( \mathbb { R } )$ . QED

Evaluate $\begin{array} { r } { { \frac { d } { d t } } \int _ { 0 } ^ { 1 } { \frac { \sin ( x t ) } { x } } } \end{array}$ . Justify your computations.dx

My Solution:

Here we will use Leibniz’s integral rule, stating that

$$
{ \frac { d } { d t } } \biggl ( \int _ { a } ^ { b } f ( x , t ) d x \biggr ) = \int _ { a } ^ { b } { \frac { \partial } { \partial t } } f ( x , t ) d x
$$

Thus we find that

$$
{ \frac { d } { d t } } \int _ { 0 } ^ { 1 } { \frac { \sin ( x t ) } { x } } d x = \int _ { 0 } ^ { 1 } x \cdot { \frac { \cos ( x t ) } { x } } d x = \int _ { 0 } ^ { 1 } \cos ( x t ) d x = { \frac { \sin ( t ) } { t } }
$$

where $t > 0 .$ . QED

If $f \in L ^ { 1 } ( \mathbb { R } ) \cap L ^ { \infty } ( \mathbb { R } )$ and $p \geq 1$ , then prove that $f \in L ^ { p } ( \mathbb { R } )$

My Solution:

Given $f \in L ^ { 1 } ( \mathbb { R } ) \cap L ^ { \infty } ( \mathbb { R } )$ . This implies that $m = \exp ( f ) < \infty$ and $\int | f | < \infty . 5 0$

$$
\int | f | ^ { p } = \int _ { \{ x : | f | < 1 \} } | f | ^ { p } + \int _ { \{ x : | f | > 1 \} } | f | ^ { p }
$$

For $\begin{array} { r } { p > 0 , \int _ { \{ x : | f ( x ) < 1 \} } | f | ^ { p } < \int _ { \{ x : | f ( x ) < 1 \} } | f | } \end{array}$ . Thus

$$
\int _ { \{ x : | f | < 1 \} } | f | ^ { p } + \int _ { \{ x : | f | > 1 \} } | f | ^ { p } \leq \int _ { \{ x : | f | < 1 \} } | f | + \int _ { \{ x : | f | > 1 \} } m ^ { p }
$$

where $\textstyle \int _ { \{ x : | f | < 1 \} } | f | < \infty$ and $\begin{array} { r } { \int _ { \{ x : | f | > 1 \} } { m ^ { p } } = { m ^ { p } } \cdot { m ( \{ x : | f ( x ) > 1 \} ) } < \infty } \end{array}$ thus the entire equation is less than . So ∞ $( \int | f | ^ { p } ) ^ { 1 / p } < \infty$ for all . Thus p $f \in L ^ { p }$ . QED

If $f : \mathbb { R } \to [ 0 , \infty )$ is measurable, then $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \int _ { - n } ^ { n } f = \int _ { \mathbb { R } } f . } \end{array}$

My Solution:

Since is positive,f $f \cdot \chi _ { [ - n , n ] }$ is a sequence of increasing positive functions. Thus

$$
\operatorname* { l i m } _ { n \to \infty } \int f \cdot \chi _ { [ - n , n ] } = \int \operatorname* { l i m } _ { n \to \infty } f \cdot \chi _ { [ - n , n ] } = \int _ { \mathbb { R } } f
$$

with the step of moving the limit inside the integral is by the Monotone Convergence Theorem. QED

## January 2013

Show that every dense subset of $L ^ { \infty } ( [ 0 , 1 ] )$ is uncountable.

My Solution:

Let $A = \left\{ \chi _ { ( 0 , t ) } : t \in ( 0 , 1 ) \right\}$ . Then for any $\chi _ { ( 0 , t _ { 1 } ) } , \chi _ { ( 0 , t _ { 2 } ) } \in A$ such that $t _ { 1 } \neq t _ { 2 }$ . So,  2

$$
\| \chi _ { ( 0 , t _ { 1 } ) } - \chi _ { ( 0 , t _ { 2 } ) } \| _ { \infty } = 1
$$

Without loss of generality, $t _ { 1 } < t _ { 2 }$ , then $\chi _ { ( 0 , t _ { 1 } ) } - \chi _ { ( 0 , t _ { 2 } ) } = 0 , 1 , 0 \mathrm { o n } ( 0 , t _ { 1 } ) , ( t _ { 1 } , t _ { 2 } ) , ( t _ { 2 } , 1 )$ respectively. This is where we get the above equality, as

$$
\left\| \chi _ { ( 0 , t _ { 2 } ) } - \chi _ { ( 0 , t _ { 1 } ) } \right\| _ { \infty } = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } \left| \chi _ { ( 0 , t _ { 2 } ) } ( x ) - \chi _ { ( 0 , t _ { 1 } ) } ( x ) \right| = 1
$$

Consider $\left\{ B _ { \left( \chi _ { \left( 0 , t \right) } , \frac { 1 } { 3 } \right) } \right\}$ which is an uncountable collection of disjoint balls. And given any dense set $S \subset L ^ { \infty } ( [ 0 , 1 ] )$ has elements in each ball by definition of density. Thus $S$ is uncountable. QED

Let $f$ be a Lebesgue measurable function on with the property that R $\begin{array} { r } { \mathbf { s u p } _ { \{ g \in L ^ { 2 } ( \mathbb { R } ) : | | g | | _ { 2 } \leq 1 \} } \int _ { \mathbb { R } } | f g | d \lambda \leq 1 } \end{array}$ . Prove that $f \in L ^ { 2 } ( \mathbb { R } )$ and $| | f | | _ { 2 } \leq 1$

My Solution:

For every $n \in \mathbb { N } ,$ , le t

$$
A _ { n } = \{ x \in [ - n , n ] : | f ( x ) | \leq n \}
$$

and let $f _ { n } = f \chi _ { A _ { n } }$ . Also define the linear functional $T _ { n } : L ^ { 2 } \to$ such that  R

$$
T _ { n } ( g ) = \int _ { \mathbb { R } } f _ { n } g
$$

Clearly $T _ { n }$ is a bounded functional in $L ^ { 2 }$ , since, by Holder’s inequality,

$$
| T _ { n } ( g ) | \leq \int _ { \mathbb { R } } | f _ { n } g | \leq | | f _ { n } | | _ { 2 } | | g | | _ { 2 }
$$

Since

$$
\left| T _ { n } ( f _ { n } ) \right| = \left| \int _ { \mathbb { R } } f ^ { 2 } \chi _ { A _ { n } } \right| = \int _ { \mathbb { R } } f _ { n } ^ { 2 } = | | f _ { n } | | _ { 2 } ^ { 2 }
$$

we can thus conclude that $\vert \vert T _ { n } \vert \vert = \vert \vert f _ { n } \vert \vert _ { 2 }$ . Moreover, $| f _ { n } g |$ increases to $\left| f g \right| \mathsf { a s } n \to \infty .$ So

$$
\operatorname* { s u p } _ { n } | T _ { n } ( g ) | \leq \int _ { \mathbb { R } } | f g | < \infty
$$

By the uniform boundedness principle, we can conclude that the sequence $\left( T _ { n } \right)$ converges to a bounded linear functional and that  T

$$
| | T | | \leq \operatorname* { l i m } _ { n } \operatorname* { i n f } _ { } \left| | T _ { n } | \right| < \infty
$$

On the other hand, by the monotone convergence theorem,

$$
\operatorname* { l i m i n f } _ { n } \left| \left| T _ { n } \right| \right| = \operatorname* { l i m i n f } _ { n } \left| \left| f _ { n } \right| \right| _ { 2 } = \left( \int _ { \mathbb { R } } \left| f \right| ^ { 2 } \right) ^ { 1 / 2 }
$$

hence $f \in L ^ { 2 }$ . Finally, taking $\begin{array} { r } { g = \frac { f } { | | f | | _ { 2 } } } \end{array}$ in the assumption, we find that

$$
\int _ { \mathbb { R } } | f g | = | | f | | _ { 2 } \leq 1
$$

Thus we have proven the desired result. QED

Let $f \geq 0$ and $f \in L ^ { p } [ 0 , 1 ]$ for all $p \in [ 1 , \infty )$ . If $| | f | | _ { p } ^ { p } = | | f | | _ { 1 }$ for all $p \in [ 1 , \infty )$ , then there is a set $S$ such that $\pmb { f } = \chi _ { S } \mathsf { a . e }$

My Solution:

We know $| | f | | _ { 1 } = \textstyle \int | f | ^ { p }$ for all $p \in [ 1 , \infty )$ . Suppose  m $( \{ x | f > 1 \} ) \neq 0$ . Pick $\epsilon \in ( 1 , \infty )$ such that $1 < \epsilon \leq f < \infty$ . Then

$$
| | f | | _ { 1 } = \int | f | ^ { p } \geq \int _ { \{ 1 < | f | \} } | f | ^ { p } \geq \int \epsilon ^ { p }  \infty
$$

since $\epsilon > 1$

Consider $m ( \{ x | 0 < f < 1 \} )$ , which we claim is equal to zero. To prove this, pick $0 < | f | \le \epsilon < 1$ . Then

$$
| | f | | _ { 1 } = \int | f | ^ { p } \leq \int _ { \{ 0 < | f | \leq \epsilon < 1 \} } \epsilon ^ { p } \to 0
$$

as $p \to \infty$ . Hence $f = 0 \circ \mathsf { r } 1$ almost everywhere. If we use this to define $S = \{ x | f ( x ) = 1 \}$ , then $f = \chi _ { S }$ almost everywhere. QED

If $E$ is a measurable subset of $\mathbb { R }$ , then there is an interval such that I

$$
\begin{array} { r } { m ( E \cap I ) > \frac { 9 } { 1 0 } m ( I ) \mathrm { o r } m ( E ^ { c } \cap I ) > \frac { 9 } { 1 0 } m ( I ) . } \end{array}
$$

My Solution:

Suppose not! Then for all $\begin{array} { r } { I , m ( E \cap I ) \leq \frac { 9 } { 1 0 } m ( I ) } \end{array}$ and $\begin{array} { r } { m ( E ^ { c } \cap I ) \leq \frac { 9 } { 1 0 } m ( I ) } \end{array}$ . Suppose has finite measure and let E $E \subset \textstyle \bigcup _ { n = 1 } ^ { \infty } I _ { n }$ Then

$$
m ( E ) = m \left( E \cap \bigcup _ { n = 1 } ^ { \infty } I _ { n } \right) = m \left( \bigcup _ { n = 1 } ^ { \infty } E \cap I _ { n } \right) \leq \sum _ { n = 1 } ^ { \infty } m ( E \cap I _ { n } ) \leq { \frac { 9 } { 1 0 } } \sum _ { n = 1 } ^ { \infty } m ( I _ { n } )
$$

Thus for all covers of $\begin{array} { r } { E , m ( E ) \leq \frac { 9 } { 1 0 } \sum _ { n = 1 } ^ { \infty } m ( I _ { n } ) } \end{array}$ . But, by definition

$$
m ( E ) = \operatorname* { i n f } \{ \sum _ { n } m ( I _ { n } ) : E \subset \bigcup _ { n = 1 } ^ { \infty } I _ { n } \}
$$

Hence

$$
m ( E ) \leq { \frac { 9 } { 1 0 } } m ( E ) \implies m ( E ) = 0
$$

Now for with any measure,E

$$
m ( E \cap ( - n , n ) \cap I _ { n } ) \leq m ( E \cap I _ { n } ) \leq { \frac { 9 } { n } } m ( I _ { n } )
$$

Hence $m ( E \cap ( - n , n ) ) = 0$ for all where n

$$
m ( E ) = m \left( \bigcup _ { n = 1 } ^ { \infty } ( E \cap ( - n , n ) ) \right) \leq \sum _ { n = 1 } ^ { \infty } m ( E \cap ( - n , n ) ) = 0
$$

Note the same proof works for $m ( E ^ { c } ) = 0$ . Thus the desired result is proven. QED

A measure space $( X , \mu )$ is -finite iff there is an σ $f : X \to ( 0 , \infty )$ such that $f \in L ^ { 1 } ( X , \mu )$

My Solution:

Assume that $f : X \to ( 0 , \infty )$ such that $f \in L ^ { 1 } ( X , \mu )$ . Then

$$
X = \{ f > 0 \} = \bigcup _ { n = 1 } ^ { \infty } \left\{ f > { \frac { 1 } { n } } \right\}
$$

where

$$
\mu \left( \left\{ f > { \frac { 1 } { n } } \right\} \right) \leq \int { \frac { | f | } { { \frac { 1 } { ( 1 / n ) } } } } d \mu \leq n \cdot \int | f | < \infty
$$

since $f \in L ^ { 1 }$ and by Chebyshev’s Inequality.

Now assume is -finite. We haveX σ $\textstyle X = \bigcup _ { i = 1 } ^ { \infty } A _ { n }$ , a union of disjoint sets with $\mu ( A _ { n } < \infty )$ . Define $\textstyle f = \sum _ { n = 1 } ^ { \infty } a _ { n }$ where $\begin{array} { r } { { a } _ { n } = \frac { 1 } { { \mu } \left( A _ { n } \right) \cdot n ^ { 2 } } \cdot \chi _ { A _ { n } } } \end{array}$ when $\mu ( A _ { n } ) > 0$ and $\begin{array} { r } { a _ { n } = \frac { 1 } { n ^ { 2 } } \chi _ { A _ { n } } } \end{array}$ when $\mu ( A _ { n } ) = 0 $ . Then

$$
\int f = \sum _ { n = 1 } ^ { \infty } \int { \frac { 1 } { \mu ( A _ { n } ) \cdot n ^ { 2 } } } \cdot \chi _ { A _ { n } } = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { \mu ( A _ { n } ) \cdot n ^ { 2 } } } \int \chi _ { A _ { n } } = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } < \infty
$$

Thus proving the desired result. QED

(a) Find a sequence $f _ { n } : [ 0 , 1 ] \to \mathbb { R }$ such that $\begin{array} { r } { \int _ { 0 } ^ { 1 } | f _ { n } ( x ) | = 2 } \end{array}$ for all $n \in \mathbb { N }$ and $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) = 1 } \end{array}$ for all $x \in [ 0 , 1 ]$ . (b) If the $f _ { n }$ are as in part (a), then prove $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } \int _ { 0 } ^ { 1 } | f _ { n } ( x ) - 1 | d x = 1 } \end{array}$

My Solution:

$$
\begin{array} { r } { \mathsf { a . } f _ { n } ( x ) : = 4 n ^ { 2 } x + 1 \mathrm { f o r } x \in \left[ 0 , \frac { 1 } { 2 n } \right] } \end{array}
$$

fn(x) := −4n x + 1 + 4n for2 $\textstyle x \in \left[ { \frac { 1 } { 2 n } } , { \frac { 1 } { n } } \right]$ and f(x) = 1 otherwise.

b. Given $f _ { n }$ as defined above, we can simply integrate to get this answer. So, given $f _ { n }$ defined as in part (a),

$$
f _ { n } ( x ) - 1 = 4 n ^ { 2 } x { \mathrm { ~ f o r ~ } } x \in \left[ 0 , { \frac { 1 } { 2 n } } \right]
$$

$$
f _ { n } ( x ) - 1 = - 4 n ^ { 2 } x + 4 n { \mathrm { ~ f o r ~ } } x \in \left[ { \frac { 1 } { 2 n } } , { \frac { 1 } { n } } \right] { \mathrm { ~ a n d ~ } } f ( x ) = 0 { \mathrm { ~ o t h e r w i s e . } }
$$

Thus

$$
\begin{array} { l } { { \displaystyle \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } | f _ { n } - 1 | d x = \operatorname* { l i m } _ { n \to \infty } \left[ \int _ { 0 } ^ { 1 / 2 n } 4 n ^ { 2 } x d x + \int _ { 1 / 2 n } ^ { 1 / n } ( - 4 n ^ { 2 } x + 4 n ) d x \right] } } \\ { { \displaystyle \quad \quad = \operatorname* { l i m } _ { n \to \infty } \left[ \frac { 2 n ^ { 2 } } { 4 n ^ { 2 } } - 0 - \frac { 2 n ^ { 2 } } { n ^ { 2 } } + \frac { 4 n } { n } + \frac { 2 n ^ { 2 } } { 4 n ^ { 2 } } - \frac { 4 n } { 2 n } \right] = \operatorname* { l i m } _ { n \to \infty } 1 = 1 } } \end{array}
$$

QED

Show that $\mathcal { G } = \{ f \in C [ 0 , 1 ] : \int _ { 0 } ^ { 1 } f ^ { 2 } > 1 \}$ is open in $C [ 0 , 1 ]$ . (Assume $C [ 0 , 1 ]$ has the uniform metric.)

My Solution:

The function $\textstyle \phi ( f ) = \int _ { 0 } ^ { 1 } f ^ { 2 }$ is continuous. Thus $\phi ^ { - 1 } ( ( 1 , \infty ) )$ must be open. QED

Let $( X , \rho )$ be a metric space and suppose and K $F$ are nonempty disjoint subsets of with compact andX K $F$ closed. (a) Prove there is a $\delta > 0$ such that $\rho ( x , y ) \ge \delta$ for all $x \in K$ and $y \in F$ . (b) Show that part (a) may fail if is closed, K but not compact.

My Solution:

a. By way of contradiction, assume for every we can find ann $x _ { n } \in K$ and $y _ { n } \in F$ such that $\begin{array} { r } { \rho ( x _ { n } , y _ { n } ) < \frac { 1 } { n } } \end{array}$ . Since is compact, K there is a convergent subsequence $x _ { n _ { k } }$ whose limit is . By the triangle inequality,x $\rho ( x , y _ { n _ { k } } ) \leq \rho ( x , x _ { n _ { k } } ) + \rho ( x _ { n _ { k } } , y _ { n _ { k } } )$ . If we juggle the ’s around a bit, we find thatϵ ${ \bf { \dot { x } } } \in F$ giving us a contradiction, thus we have proven the desired result. The problem here is that this question is not written that well in regards to our qualifying exam, so for the most part this one should be ignored. It leaves out important details of what exactly $\rho$ is. However, if you would like to check out other solutions on this, follow these links:

[https://math.stackexchange.com/questions/185656/show-that-exists-delta-0-such-thatdx-y-geq-delta

(https://math.stackexchange.com/questions/185656/show-that-exists-delta-0-such-thatdx-y-geq-delta)]

[http://www.math.ucsd.edu/\~benchow/F16/HW7-140A-F16-ans.pdf (http://www.math.ucsd.edu/\~benchow/F16/HW7-140A-F16-ans.pdf)] (check #8)

b. Consider an example in $\mathbb { R } ^ { 2 }$ with the standard metric. Take as the -axis and as the graph of the exponential function K x F $\mathrm { e } ^ { x }$ , that is, $F = \{ ( x , y ) \in \mathbb { R } ^ { 2 } | y = \mathrm { e } ^ { x } \}$ . These are clearly non-empty and mutually disjoint. Both and are closed, but neither is compact  K F because they are both unbounded. It is easy then to see that their distance is zero and a strictly positive of the desired result does notδ exist. Thus we can see then that if is not compact and still closed that our proof in part (a) may not hold.K

The limit superior of a sequence of sets $\{ E _ { k } \}$ is defined as   
lim sup $\begin{array} { r } { E _ { k } = \bigcap _ { i = 1 } ^ { \infty } \bigcup _ { k = j } ^ { \infty } E _ { k } } \end{array}$ . Let $\{ \vec { E _ { k } } : \bar { k } \in \mathbb { N } \}$ be a sequence of sets in $\mathcal { L }$ . (a) 'J J   
Prove that if $\textstyle \sum _ { k \in \mathbb { N } } \lambda ( E _ { k } ) < \infty$ , then $\lambda ( \operatorname* { l i m } \operatorname* { s u p } ( E _ { k } ) ) = 0$ . (b) Is it true in   
general that λ(lim sup(Ek)) = lim sup $\lambda ( E _ { k } ) \colon$

My Solution:

(a): Let . Givenϵ > 0 $\textstyle \sum _ { k = 1 } ^ { \infty } m ( E _ { k } ) < \infty$ , there exists such that N $\begin{array} { r } { \sum _ { k = N } ^ { \infty } m ( E _ { k } ) < \epsilon } \end{array}$

$$
\operatorname* { l i m } \operatorname* { s u p } ( E _ { k } ) = \bigcap _ { n = 1 } ^ { \infty } \bigcup _ { k = n } ^ { \infty } E _ { k } \subset \bigcup _ { k = N } ^ { \infty } E _ { k }
$$

Hence

$$
m ( \operatorname* { l i m } \operatorname* { s u p } ( E _ { k } ) ) \leq m \left( \bigcup _ { k = N } ^ { \infty } E _ { k } \right) \leq \sum _ { k = N } ^ { \infty } m ( E _ { k } ) < \epsilon
$$

which implies that $m ( \operatorname* { l i m } \operatorname* { s u p } ( E _ { k } ) ) = 0$ . QED

(b): Consider the sequence of functions:

$\begin{array} { r } { E _ { 1 } = [ 0 , 1 ] , E _ { 2 } = [ 0 , \frac { 1 } { 2 } ] , E _ { 3 } = [ \frac { 1 } { 2 } , 1 ] , E _ { 4 } = [ 0 , \frac { 1 } { 4 } ] , E _ { 5 } = [ \frac { 1 } { 4 } , \frac { 1 } { 2 } ] , E _ { 6 } = [ \frac { 1 } { 2 } , \frac { 3 } { 4 } ] , E _ { 7 } = [ \frac { 3 } { 4 } , 1 ] } \end{array}$ , and so on. Then $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } m ( E _ { k } ) = 0 } \end{array}$ but for all $\textstyle n \in \mathbb { N } , \bigcup _ { k = n } ^ { \infty } E _ { k } = [ 0 , 1 ]$ . This implies that  lim sup $\left( E _ { n } \right) = \left[ 0 , 1 \right]$ . Thus it may not be true that . QEDλ(lim sup(Ek)) = lim sup λ(Ek)

Show that $\begin{array} { r } { f ( x ) = x ^ { 2 } \sin \left( \frac { 1 } { x } \right) } \end{array}$ where $x \neq 0$ and $f ( x ) = 0$ where $x = 0$ is in $B V [ - 1 , 1 ]$ , but $\begin{array} { r } { g ( x ) = x ^ { 2 } \sin \left( \frac { 1 } { x ^ { 2 } } \right) } \end{array}$ where $x \neq 0$ and $g ( x ) = 0$ where $x = 0$ is not.

My Solution:

Because $f ( - x ) = - f ( x )$ , it is sufficient to show this is true for as follows from it. Well,(0, 1) (−1, 0)

$$
T . V . ( f ) = \int _ { 0 } ^ { 1 } | f ^ { \prime } ( x ) | d x = \int _ { 0 } ^ { 1 } { \frac { { \bigl | } \cos \left( { \frac { 1 } { x } } \right) - 2 x \sin \left( { \frac { 1 } { x } } \right) { \bigr | } \ln ( x ) } { \frac { 1 } { x ^ { 2 } } } } d x
$$

Then if we let $\textstyle u = { \frac { 1 } { x } }$ and $d u = \ln ( x ) d x$ , then

$$
T . V . \left( f \right) = \int _ { 1 } ^ { \infty } \frac { \left| \cos ( u ) - \frac { 2 } { u } \mathrm { s i n } ( u ) \right| } { u ^ { 2 } } d u \leq \int _ { 1 } ^ { \infty } \frac { d u } { u ^ { 2 } } = 1 < \infty
$$

Thus the total variation is finite, thus proving that $f ( x )$ is of bounded variation.

Now we must show that $g ( x )$ is not of bounded variation.

Well, let

$$
P = \{ - 1 \} \cup \left[ \{ \pm { \sqrt { \frac { 1 } { n \pi } } } : n \in \mathbb { N } \} \cap [ - 1 , 1 ] \right] \cup \{ 1 \}
$$

. Hence for $x _ { n } , x _ { n + 1 } \in P ,$

$$
\begin{array} { l } { { \displaystyle \sum _ { n = 1 } ^ { \infty } | f ( x _ { n } ) - f ( x _ { n + 1 } ) | = \sum _ { n = 1 } ^ { \infty } \left| f \left( \sqrt { \frac { 1 } { n \pi } } \right) - f \left( \sqrt { \frac { 1 } { ( n + 1 ) \pi } } \right) \right| } } \\ { { \displaystyle \qquad = \sum _ { n = 1 } ^ { \infty } \left| \left( \frac { 1 } { n \pi } \sin ( n \pi ) - \frac { 1 } { n \pi + \pi } \sin ( n \pi + \pi ) \right) \right| } } \\ { { \displaystyle \qquad = \sum _ { n = 1 } ^ { \infty } \left| \left( \frac { 1 } { ( n + 1 ) \pi } + \frac { 1 } { n \pi } \right) \sin ( n \pi ) \right| \le \frac { 1 } { \pi } \sum _ { n = 1 } ^ { \infty } \left| \frac { 2 n + 1 } { n ^ { 2 } + n } \right| } } \end{array}
$$

Notice that this is a harmonic series, thus it diverges, implying that $V _ { g } [ 0 , 1 ] \not \ll \infty$ , thus it cannot be of bounded variation. QED

## Extra Problems

Let $\mu ^ { * }$ be an outer measure on a set $X$ . Prove that if $\{ E _ { k } \}$ is a sequence of subsets of andX $\textstyle \sum _ { k = 1 } ^ { \infty } \mu ^ { * } ( E _ { k } ) < \infty$ , then $\textstyle \mu ^ { * } ( \bigcap _ { k = 1 } ^ { \infty } \bigcup _ { n = k } ^ { \infty } { \bar { E _ { n } } } ) = 0$

My Solution:

Since $\textstyle \sum _ { k = 1 } ^ { \infty } \mu ^ { * } ( E _ { k } ) < \infty$ , for any $\epsilon > 0$ there exists an $N$ such that $\textstyle \sum _ { k = N } ^ { \infty } \mu ^ { * } ( E _ { k } ) <$ from sub-additivity. Thus ϵ

$$
\mu ^ { * } \left( \bigcup _ { n = N } ^ { \infty } E _ { n } \right) \leq \sum _ { k = N } ^ { \infty } \mu ^ { * } ( E _ { k } ) < \epsilon
$$

But by monotonicity,

$$
\mu ^ { * } \left( \bigcap _ { k = 1 } ^ { \infty } \bigcup _ { n = k } ^ { \infty } E _ { n } \right) \leq \mu ^ { * } \left( \bigcup _ { n = N } ^ { \infty } E _ { n } \right) < \epsilon
$$

Since is arbitrary, we see thatϵ $\begin{array} { r } { \mu ^ { * } \left( \bigcap _ { k = 1 } ^ { \infty } { \bigsqcup _ { n = k } ^ { \infty } { E _ { n } } } \right) = 0 } \end{array}$ . QED

Let $( X , A , \mu )$ be a measure space and let $f : X \to ( 0 , \infty )$ be measurable. Prove that $1 / f$ is measurable.

My Solution:

Let $\textstyle g = { \frac { 1 } { f } }$ and note that for $a \leq 0 , \{ g > a \} = X$ which is in ${ \cal A } .$ So assume $a > 0$ , and note that $\{ g > a \}$ is equivalent to $\textstyle \left\{ 0 < f < { \frac { 1 } { a } } \right\}$ . But since $\textstyle { \frac { 1 } { a } } \in \mathbb { R }$ this is also a measurable set. QED

Let $\mu _ { n }$ and $\mu$ be finite measures on a measurable space $( X , A )$ with the property that $\mu _ { n } ( A ) \to \mu ( A )$ for all $A \in A$ . Prove that $\textstyle \int _ { X } f d \mu _ { n } \to \int _ { X } f d \mu$ for every bounded measurable function $f : X \to \mathbb { R }$

My Solution:

Let $f$ be a simple non-negative measurable function. Then

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { X } f d \mu _ { n } = \operatorname* { l i m } _ { n \to \infty } \int _ { X } \sum _ { i = 1 } ^ { L } a _ { i } \chi _ { A _ { i } } ( x ) d \mu _ { n } = \operatorname* { l i m } _ { n \to \infty } \sum _ { i = 1 } ^ { L } a _ { i } \mu _ { n } ( A _ { i } ) = \sum _ { i = 1 } ^ { L } a _ { i } \mu ( A _ { i } ) = \int _ { X } f d \mu _ { n } ( \mu _ { n } ) .
$$

QED

Suppose that $f \in L ^ { 1 } ( \mathbb { R } )$ with Lebesgue measure. Prove that $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \frac { 1 } { 2 n } \int _ { - n } ^ { n } f d m = 0 . } \end{array}$

My Solution:

We note that $\begin{array} { r } { \left| \frac { 1 } { 2 n } f ( x ) \chi _ { \{ | x | \leq n \} } ( x ) \right| \leq | f ( x ) | } \end{array}$ for| $x \in \mathbb { R }$ . Since $f \in L ^ { 1 }$ , we may apply the DCT with $| f ( x ) |$ as the majorant. Thus

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { \mathbb { R } } \frac { 1 } { 2 n } f ( x ) \chi _ { \{ | x | \leq n \} } d m = \int _ { \mathbb { R } } \operatorname* { l i m } _ { n \to \infty } \frac { f ( x ) } { 2 n } \chi _ { \{ | x | \leq n \} } d m = \int _ { \mathbb { R } } 0 d m = 0
$$

. QED

Let $\mu$ and be finite (positive) measures on a measurable space ν $( X , A )$ . Define $\rho = \mu - \nu .$ . Prove that $| \rho | ( E ) \leq \mu ( E ) + \nu ( E )$ for every set $E \in A .$

My Solution:

Let $P _ { \rho }$ and $N _ { \rho }$ be a Hahn decomposition with respect to $\rho .$ So

$$
| \rho | ( A ) = \rho ( A \cap P _ { \rho } ) - \rho ( A \cap N _ { \rho } ) = \mu ( A \cap P _ { \rho } ) - \nu ( A \cap P _ { \rho } ) - \mu ( A \cap N _ { \rho } ) + \nu ( A \cap N _ { \rho } )
$$

But $\mu ( A ) + \nu ( A ) = \mu ( A \cap P _ { \rho } ) + \nu ( A \cap P _ { \rho } ) + \mu ( A \cap N _ { \rho } ) + \nu ( A \cap N _ { \rho } )$ . Since all of these terms are non-negative and finite by comparisons of signs, we can clearly see that $| \rho | ( E ) \leq \mu ( E ) + \nu ( E )$ for all $E \in { \mathcal { A } } .$ QED

Let be a normed vector space and letV $L : V \to \mathbb { R }$ be linear. Define what is meant by $| | L | |$ and prove that $| | L | | < \infty$ if and only if $L$ is continuous.

My Solution:

First off, $\begin{array} { r } { | | L | | = \operatorname* { s u p } _ { | | V | | \leq 1 } \{ | L ( V ) | \} } \end{array}$

Now we just need to prove that $| | L | | <$ implies continuity, or that if it’s not continuous that< ∞ $| | L | | = \infty$ . Let $X \in V$ be such that there exists $\epsilon > 0$ such that in any $B ( x , r _ { n } )$ there exists $y _ { n }$ such that

$$
| L ( x ) - L ( y _ { n } ) | = | L ( x - y _ { n } ) | > \epsilon
$$

This implies that $\begin{array} { r } { \left| \left| L \right| \right| \geq \frac { \epsilon } { r _ { n } } } \end{array}$ . Take $\begin{array} { r } { r _ { n } ^ { \prime } = \left( \frac { 1 } { 2 } \right) ^ { n } } \end{array}$ . Clearly, $| | L | |$ is unbounded here.

Now to prove that continuous implies bounded. Let $\epsilon > 0$ , then there exists a $\delta > 0$ such that $y \in B ( x , \delta )$ so that $| L ( x ) - L ( y ) | < \epsilon .$ . We see $\begin{array} { r } { \left| L \left( \frac { x - y } { \delta } \right) \right| < \frac { \epsilon } { \delta } } \end{array}$ for all $y \in B ( x , \delta )$ . Since any $v \in B ( 0 , 1 )$ can be expressed as $\frac { x - y } { \delta }$ , we then see our desired result, that $\begin{array} { r } { \operatorname* { s u p } _ { | | v | | \leq 1 } | L ( \dot { v } ) | < \frac { \epsilon } { \delta } . \mathsf { Q E D } } \end{array}$

## Important Notes

## Undergrad

For reference, these notes are gathered from the book Real Analysis; A First Course by Russell A. Gordon. These notes consist of basic real analysis ideas based off of my past undergraduate class taught by Dr. Christine Leverenz at Georgetown College.

## Gordon Chapter 1 (Real Numbers)

A field is a nonempty set of objects that has two operations defined on it. These operations are usually defined as addition andF multiplication. These operations follow a set of properties which will not be listed here as you should know them.

Triangle Inequality: $| a + b | \leq | a | + | b |$ . It follows from this that $| | a | - | b | | \leq | a - b |$

If a $\neq 0$ and $r \neq 1$ are real numbers, then

$$
a + a r + a r ^ { 2 } + a r ^ { 3 } + \ldots + a r ^ { n } = a \cdot { \frac { 1 - r ^ { n + 1 } } { 1 - r } }
$$

Cauchy-Schwarz Inequality: Let be a positive integer. Ifn $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ and $b _ { 1 } , b _ { 2 } , \ldots , b _ { n }$ are real numbers, then

$$
\left( \sum _ { k = 1 } ^ { n } a _ { k } b _ { k } \right) ^ { 2 } \leq \left( \sum _ { k = 1 } ^ { n } a _ { k } ^ { 2 } \right) \left( \sum _ { k = 1 } ^ { n } b _ { k } ^ { 2 } \right)
$$

Equality occurs iff there is a constant such thatc $a _ { k } = c b _ { k }$ for all integers k

The set $S$ is bounded if there is a number such that M $| x | \le M$ for all $x \in S$ . The number is called a bound for S. M

Suppose that $S$ is bounded above. A number $\beta$ is the supremum of $S \mathfrak { i f } \beta$ is an upper bound of and any number less than S $\beta$ is not an upper bound of . We writeS $\beta = \operatorname* { s u p } ( S )$

Suppose that $S$ is bounded below. A number is the infimum of α $S$ if is an lower bound of α $S$ and any number greater than is not an α lower bound of . We writeS $\alpha = \operatorname { i n f } ( S )$

Archimedean Property of the Real Numbers: If and are positive real numbers, then there exists a positive integer such that a b n $n a > b$

Between any two distinct real numbers, there exists a rational and an irrational number.

A countable union of countable sets is countable.

Let be an interval and be a function such thatI f $f : I \to \mathbb { R } .$ , and let be a subinterval of . The function is increasing on J I f $J \dag$ $f ( x ) \leq f ( y )$ for all $x , y \in J$ such that  x $\mathrel { \mathop { \cdot } } < y$ ; and strictly increasing on $J { \mathfrak { i } } \mathfrak { f } \left( x \right) < f ( y )$ for all $x , y \in J$ such that $x < y .$ . The function is decreasing on iff J $f ( x ) \geq f ( y )$ for all $x , y \in J$ that satisfy $x < y ,$ and strictly decreasing on $J { \mathfrak { i } } \mathfrak { f } \left( x \right) > f ( y )$ f o r all $x , y \in J$ such that $x < y .$ The function $f$ is monotone on if it is either increasing or decreasing on J $J$ and strictly monotone on if it is either strictly increasing or decreasing on .J J

## Gordon Chapter 2 (Sequences)

A sequence is a function whose domain is the set of positive integers. A sequence of real numbers is a sequence whose codomain is the set . Although a sequence is a function, the standard notation for a sequence of real numbers is R $\{ x _ { n } \}$ where the subscript  n denotes the index of the sequence.

A sequence $\{ x _ { n } \}$ converges to a number if for allL $\epsilon > 0$ there exists a positive integer $N$ such that $| x _ { n } - L | < \epsilon$ for all $n \geq N$ The sequence is convergent if there exists a number that the sequence converges to, otherwise it is divergent.L

The limit of a convergent sequence is unique.

Suppose that $\left\{ a _ { n } \right\}$ converges to and a $\left\{ b _ { n } \right\}$ converges to . Then:  b

$$
- \{ c a _ { n } \}  c a
$$

$$
- \{ a _ { n } \pm b _ { n } \}  a \pm b
$$

$$
- \left\{ a _ { n } b _ { n } \right\} \to a b
$$

A monotone sequence converges iff it is bounded

A sequence $\{ x _ { n } \}$ is a Cauchy Sequence if for all $\epsilon > 0$ there exists a positive integer such that N $| x _ { m } - x _ { n } | < \epsilon$ for all $m , n \geq N$

A sequence of real numbers converges iff it is a Cauchy sequence

Let $\{ x _ { n } \}$ be a sequence and let $\{ p _ { n } \}$ be a strictly increasing sequence of positive integers. The sequence $\{ x _ { p _ { n } } \}$ is called a subsequence of $\{ x _ { n } \}$

If a sequence $\{ x _ { n } \}$ converges to , then every subsequence must converge to L $L$ as well.

Bolzano-Weierstrass Theorem: Every bounded sequence has a convergent subsequence.

## Gordon Chapter 3 (Limits and Continuity)

Let be an open interval that contains the point and suppose thatI c $f$ is a function that is defined on except possibly at . The function I c $f$ has limit at point if for all L c $\epsilon > 0$ there exists $\delta > 0$ such that $| f ( x ) - L | <$ for all ϵ $x \in I$ such that $| x - c | < \delta$ . We then write lim $_ { \cdot x \to c } f ( x ) = L$ .

We have linearity for limits.

Let be an interval andI $f : I  \mathbb { R }$ , and let $c \in I$ . The function is continuous at if for eachf c $\epsilon > 0$ there exists a $\delta > 0$ such that $| f ( x ) - f ( c ) | < \epsilon$ for all $x \in I$ such that $| x - c | < \delta$ . The function is continuous on $I \mathfrak { i f } f$ is continuous on every point of . I

Intermediate Value Theorem: Suppose that $f : [ a , b ] $ is continuous on R $[ a , b ]$ . If is a number between v $f ( a )$ and $f ( b )$ , then there is a point $c \in ( a , b )$ such that $f ( c ) = v$

Extreme Value Theorem: If $f : [ a , b ]  \mathbb { R }$ is continuous on $[ a , b ]$ , then there exist points and in c d $[ a , b ]$ such that $f ( c ) \leq f ( x ) \leq f ( d )$ for all $x \in [ a , b ]$

Let be an interval. A functionI $f : I $ is uniformly continuous on if for each R I $\epsilon > 0$ there exists a $\delta > 0$ such that $| f ( y ) - f ( x ) | < \epsilon$ for all $x , y \in I$ such that $\left| y - x \right| < \delta .$

If $f : [ a , b ]  \mathbb { R }$ is continuous on $[ a , b ]$ , then is uniformly continuous on f $[ a , b ]$

A partition of an intervalP $[ c , d ]$ is a finite set of points $\{ x _ { i } | 0 \leq i \leq n \}$ such that

$$
c = x _ { 0 } < x _ { 1 } < x _ { 2 } < . . . < x _ { n - 1 } < x _ { n } = d
$$

Let $f : [ a , b ]  \mathbb { R }$ be a function and let $[ c , d ]$ be any closed subinterval of $[ a , b ]$ . The variation of $f \circ n \ [ c , d ]$ is defined by $V ( f , [ c , d ] ) = \textstyle \operatorname* { s u p } \{ \sum _ { i = 1 } ^ { n } | f ( x _ { i } ) - f ( x _ { i - 1 } ) | \}$ . Note that the integer is not fixed; the supremum is over all possible partitions of  n $[ c , d ]$ . The function is of bounded variation on f $[ c , d ] { \mathfrak { i f } } V ( f , [ c , d ] )$ is finite.

## Gordon Chapter 4 (Differentiation)

Let be an interval, letI $f : I  \mathbb { R }$ , and let $c \in I .$ The function id differentiable at provided that the limitf c

$$
\operatorname* { l i m } _ { v \to c } { \frac { f ( v ) - f ( c ) } { v - c } }
$$

exists. The derivative of at is the value of the aforementioned limit denoted byf c $f ^ { \prime } ( c )$

Rolle’s Theorem: Let $f : [ a , b ] $ be continuous on R $[ a , b ]$ and differentiable on $( a , b ) . \nmid { \mathfrak { f } } ~ f ( a ) = f ( b )$ , then there exists a point $c \in ( a , b )$ such that $f ^ { \prime } ( c ) = \bar { 0 }$

Mean Value Theorem: If $f : [ a , b ]  \mathbb { R }$ is continuous on $[ a , b ]$ and differentiable on $( a , b )$ , then there exists a point $c \in ( a , b )$ such that

$$
f ^ { \prime } ( c ) = { \frac { f ( b ) - f ( a ) } { b - a } }
$$

## Gordon Chapter 5 (Integration)

A tagged partition $^ t P$ of an interval $[ a , b ]$ consists of a partition $P = \{ x _ { i } | 0 \leq i \leq n \}$ of along with a set [a, b] $\{ t _ { i } | 1 \le i \le n \}$ of points, known as tags, that satisfy $x _ { i - 1 } \leq t _ { i } \leq x _ { i }$ for $1 \leq i \leq n$

Let $f : [ a , b ]  \mathbb { R }$ and let $^ { t } P = \{ ( t _ { i } , [ x _ { i - 1 } , x _ { i } ] ) | 1 \leq i \leq n \}$ be a tagged partition of $[ a , b ]$ . The Riemann sum $S ( f , ^ { t } P ) \circ \mathsf { f } \ f$ associated with $^ t P$ is defined by

$$
S ( f , ^ { t } P ) = \sum _ { i = 1 } ^ { n } f ( t _ { i } ) ( x _ { i } - x _ { i - 1 } )
$$

A function $f : [ a , b ]  \mathbb { R }$ is Riemann integrable on $[ a , b ]$ if there exists a number with the following property: for all L $\epsilon > 0$ there exists $\delta > 0$ such that $| S ( f , ^ { t } P ) - L | < \epsilon$ for all tagged partitions ${ } ^ { t } P \circ \mathsf { f } \left[ a , b \right]$ that satisfy $| | ^ { t } P | | < \delta .$ The number is called theL Riemann integral of $f \circ \mathsf { n } \left[ a , b \right]$

Cauchy Criterion for Riemann Integrability: A bounded function $f$ is Riemann integrable on $[ a , b ]$ iff for each $\epsilon > 0$ there exists $\delta > 0$ such that $| S ( f , ^ { t } P _ { 1 } ) - S ( f , ^ { t } P _ { 2 } ) | < \epsilon$ for all tagged partitions ${ } ^ { t } P _ { 1 }$ and ${ } ^ { t } P _ { 2 }$ of $[ a , b ]$ with norms less than . δ

Fundamental Theorem of Calculus is a thing

Integration by Parts:

$$
\int _ { a } ^ { b } f ^ { \prime } g = f ( b ) g ( b ) - f ( a ) g ( a ) - \int _ { a } ^ { b } g ^ { \prime } f
$$

## Gordon Chapter 6 (Infinite Series)

A power series is an expression of the form

$$
a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + a _ { 3 } x ^ { 3 } + . . .
$$

where the $\boldsymbol { a } _ { k } \ ' \boldsymbol { \mathsf { s } }$ are constants

A Fourier series is an expression of the form

$$
a _ { 0 } + a _ { 1 } \cos ( x ) + b _ { 1 } \sin ( x ) + a _ { 2 } \cos ( 2 x ) + b _ { 2 } \sin ( 2 x ) + . . .
$$

where the $\arcsin ^ { \prime } { \tt s }$ and $b _ { k }$ ’s are constants

An infinite series of real numbers is an expression of the form

$$
\sum _ { k = 1 } ^ { \infty } a _ { k } = a _ { 1 } + a _ { 2 } + \ldots .
$$

A partial sum of an infinite series is represented by $\scriptstyle \sum _ { k = 1 } ^ { n } a _ { k }$

An infinite series converges if its corresponding sequence $\left\{ s _ { n } \right\}$ of partial sums converges. If is the limit of the previous sequence, S then we say the series converges to $S .$ If the sequence does not converge, we say that the series diverges.

If the series $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k }$ converges, then the sequence $\left\{ a _ { k } \right\}$ converges to zero.

The series $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k }$ converges iff for all $\epsilon > 0$ there exists a positive integer $N$ such that $\textstyle { \big | } \sum _ { k = m + 1 } ^ { n } a _ { k } { \big | } < \epsilon$ for all positive integers and that satisfym n $n > m \ge N$

A series with nonnegative terms converges iff its sequence of partial sums is bounded

Linearity is preserved

Geometric Series: Suppose that $a \neq 0$ . The geometric series $\scriptstyle \sum _ { k = 0 } ^ { \infty } a r ^ { k }$ converges $| \mathsf { f } | r | < 1$ and diverges if $| r | \geq 1 . | { \mathfrak { f } } | r | < 1$

$$
\sum _ { k = 0 } ^ { \infty } a r ^ { k } = { \frac { a } { 1 - r } }
$$

The -seriesp $\scriptstyle \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { k ^ { p } } }$ converges $\mathsf { i f } p > 1$ and diverges if $p \leq 1$

Let $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k }$ be a series of real numbers. If the series $\textstyle \sum _ { k = 1 } ^ { \infty } | a _ { k } |$ converges, then so does $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k }$

Rearrangement stuff is cool, but unnecessary for this study guide.

## Gordon Chapter 7 (Sequences and Series of Functions)

Let $\{ f _ { n } \}$ be a sequence of functions defined on an interval and let be a function defined on . The sequence I f I $\{ f _ { n } \}$ converges pointwise to $f$ on if the sequence I $\{ f _ { n } ( x ) \}$ converges to $f ( x )$ for each $x \in I .$ . In other words, $f ( x ) = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ for all $x \in I .$

Let $\{ f _ { k } \}$ be a sequence of functions defined on an interval and let I $f$ be a function defined on . The series I $\textstyle \sum _ { k = 1 } ^ { \infty } f _ { k }$ converges pointwise to $f$ on if the sequence I $\textstyle \left\{ s _ { n } \right\} = \left\{ \sum _ { k = 1 } ^ { n } f _ { k } \right\}$ of partial sums converges pointwise to $f$ on . I

Let $\{ f _ { n } \}$ be a sequence of functions defined on an interval and let be a function defined on . The sequence I f I $\{ f _ { n } \}$ converges uniformly to on if for allf I $\epsilon > 0$ there exists a positive integer such that N $| f _ { n } ( x ) - f ( x ) | < \epsilon$ for all $x \in I$ and for all $n \geq N$

A lot more information is here, may add later. I just don’t think it will help much for the Qual

## Gordon Chapter 8 (Point-Set Topology)

A point is an interior point of if there exists a positive number such thatx E r $( x - r , x + r ) \subseteq E$

A point is an isolated point of if there exists a positive number such thatx E r $( x - r , x + r ) \cap E = \{ x \}$

A point is a limit point ofx $E$ if for each positive number , the set r $( x - r , x + r ) \cap E$ contains a point of other than  E x

The set is open if all of its points are interior pointsE

The set $E$ is closed if it contains all of its limit points

Every open interval is an open set and every closed interval is a closed set

Let $E$ be a set of real numbers. A collection $\mathcal { G }$ of sets is an open cover of $E$ if each set in $\mathcal { G }$ is open and $E$ is contained in the union of all the sets in ${ \mathcal { G } } .$ The open cover $\mathcal { G }$ has a finite subcover if $E$ is contained in the union of a finite number of sets in $\mathcal { G }$

A set is compact if every open cover ofE $E$ has a finite subcover

A compact set is closed and bounded

A closed subset of a compact set is compact

A set of real numbers is compact iff it is closed and bounded

More is in this section. Possibly going to add more, but I don’t find it necessary for the Qual.

## Graduate Notes/Royden Book

## Royden Chapter 1 (Sets, Sequences, and Functions)

A nonempty set of real numbers is said to be bounded above provided that there is a real numberE $b$ such that $x \leq b$ for all $x \in E$ is known as an upper bound for . We define bounded below similarly.b E

The Completeness Axiom: Let be a nonempty set of real numbers that is bounded above. Then among the set of upper bounds forE there is a smallest, or least, upper bound.E

The least upper bound of is called the supremum ofE $E$ and denoted by . We define the infimum similarly as the greatest lower supE bound and denote it by .infE

Triangle Inequality:

$$
| a + b | \leq | a | + | b |
$$

A set of real numbers is said to be inductive provided it contains and if the numberE 1 $x \in E ,$ , the number $x + 1 \in E$ as well.

Every nonempty set of natural numbers has a smallest member.

Archimedean Property: For each pair of positive real numbers anda $b ,$ there is a natural number for which n na $> b .$

A set of real numbers is said to be dense in provided between any two real numbers there lies a member of .E R E

The rational numbers are dense in .R

A set is said to be finite provided either it is empty or there is a natural number such that is equipotent toE n E $\{ 1 , 2 , 3 , \ldots , n \}$

We say that is countably infinite provided is equipotent to the setE E $\mathbb { N }$ (the natural numbers). A set that is either finite or countably finite is said to be countable. A set that is not countable is uncountable.

A subset of a countable set is countable.

A nonempty set is countable iff it is the image of a function whose domain is a nonempty countable set.

The union of countable sets is countable.

A set of real numbers is called open provided for eachO $x \in \mathcal { O }$ , there is $\mathsf { a } r > 0$ for which the interval $( x - r , x + r )$ is contained in .O

The set of real numbers and the empty set are open; the intersection of any finite collection of open sets is open; and the union of any collection of open sets is open.

Every nonempty open set is the disjoint union of a countable collection of open intervals.

For a set of real numbers, a real number is called a point of closure of provided every open interval that contains alsoE x E x contains a point in . The collection of points of closure of is called the closure of .E E E

A set of real numbers is open iff its complement in is closed.R

A collection of sets $\{ E _ { \lambda } \} _ { \lambda \in \Lambda }$ is said to be a cover of a set providedE $E \subseteq \cup _ { \lambda \in \Lambda } E _ { \lambda }$ . By a subcover of a cover of $E$ we mean a subcollection of the cover that itself also is a cover of . If each setE $E _ { \lambda }$ in a cover is open, then we call $\{ E _ { \lambda } \} _ { \lambda \in \Lambda }$ an open cover of $E$ If the cover $\{ E _ { \lambda } \} _ { \lambda \in \Lambda }$ contains only a finite number of sets, we call it a finite cover.

Let $F$ be a closed and bounded set of real numbers. Then every open cover of has a finite subcover. F

We say that a countable collection of sets $\{ E _ { n } \} _ { n = 1 } ^ { \infty }$ is descending or nested provided that $E _ { n + 1 } \subseteq E _ { n }$ for every natural number . n It is said to be ascending provided $E _ { n } \subseteq E _ { n + 1 }$ for every natural number .n

-algebra: Given a set , a collectionσ x $\boldsymbol { A }$ of subsets of $X$ is called a -algebra provided σ

– the empty set belongs to A

– the complement in of a set in also belongs to X A A

– the union of a countable collection of sets in also belongs toA ${ \cal { A } } .$

Let $\mathcal { F }$ be a collection of subsets of a set . Then the intersection of all -algebras of subsets of that contain X A σ X $\mathcal { F }$ is a -algebra that σ contains ${ \mathcal F } .$ Moreover, it is the smallest -algebra of subsets that contains σ X $\mathcal { F }$ in the sense that any -algebra that contains σ $\mathcal { F }$ also contains .A

The collection of Borel sets of real numbers is the smallest -algebra of sets of real numbers that contains all of the open sets of realB σ numbers. (every open set is a Borel set)

## Royden Chapter 2 (Lebesgue Measure)

The measure of an interval is its length. Each nonempty interval is Lebesgue measurable andI

$$
m ( I ) = l ( I )
$$

Measure is translation invariant. If $E$ is Lebesgue measurable and is any number, then the translate of y $E$ by ,  y $E + y = \{ x + y | x \in E \}$ , also is Lebesgue measurable and

$$
m ( E + y ) = m ( E )
$$

Measure is countably additive over countable disjoint unions of sets. If $\{ E _ { k } \} _ { k = 1 } ^ { \infty }$ is a countable disjoint collection of Lebesgue measurable sets, then

$$
m \left( \bigcup _ { k = 1 } ^ { \infty } E _ { k } \right) = \sum _ { k = 1 } ^ { \infty } m ( E _ { k } )
$$

The outer measure of an interval is its length, it is translation invariant, however the outer measure is not finitely additive. Instead:

$$
m ^ { * } \left( \bigcup _ { k = 1 } ^ { \infty } E _ { k } \right) \leq \sum _ { k = 1 } ^ { \infty } m ^ { * } ( E _ { k } )
$$

Let be a nonempty interval of real numbers. For a set of real numbers, consider the countable collectionsI A $\{ I _ { k } \} _ { k = 1 } ^ { \infty }$ of nonempty open, bounded intervals that cover , that is, collections for whichA $A \subseteq \textstyle \bigcup _ { k = 1 } ^ { \infty } I _ { k }$ . We define the outer measure of $A , m ^ { * } ( A )$ , to be

$$
m ^ { * } ( A ) = \operatorname* { i n f } \{ \sum _ { k = 1 } ^ { \infty } l ( I _ { k } ) | A \subseteq \bigcup _ { k = 1 } ^ { \infty } I _ { k } \}
$$

A measure is monotone if for all $A \subseteq B ,$ then $m ^ { * } ( A ) \leq m ^ { * } ( B )$

A set $E$ is said to be measurable provided for any set $A$ that

$$
m ^ { * } ( A ) = m ^ { * } ( A \cap E ) + m ^ { * } ( A \cap E ^ { C } )
$$

Any set of outer measure zero is measurable. In particular, any countable set is measurable.

The union of a finite collection of measurable sets is measurable.

The union of a countable collection of measurable sets is measurable.

Every interval is measurable.

The collection of measurable sets is a -algebra that contains the -algebraM σ σ $_ B$ of Borel sets. Each interval, each open set, each closed set, and each clopen set is measurable.

The translate of a measurable set is measurable.

If is a measurable set of finite outer measure that is contained inA $B ,$ then

$$
m ^ { * } ( B / A ) = m ^ { * } ( B ) - m ^ { * } ( A )
$$

and

$$
m ^ { * } ( B ) = m ^ { * } ( A ) + m ^ { * } ( B / A )
$$

The restriction of the set function outer measure to the class of measurable sets is called Lebesgue Measure. It is denoted by $m ,$ so that if is a measurable set, its Lebesgue measure will beE $m ( E )$ , defined by

$$
m ( E ) = m ^ { * } ( E )
$$

The Lebesgue measure defined on the -algebra of Lebesgue measurable sets assigns length to any interval, is translation invariant,σ and is countably additive.

The Continuity of Measure: Lebesgue measure possesses the following continuity properties:

a. If $\{ A _ { k } \} _ { k = 1 } ^ { \infty }$ is an ascending collection of measurable sets, then,

$$
m \left( \bigcup _ { k = 1 } ^ { \infty } A _ { k } \right) = \operatorname* { l i m } _ { k \to \infty } m ( A _ { k } )
$$

b. If $\{ B _ { k } \} _ { k = 1 } ^ { \infty }$ is a descending collection of measurable sets and $m ( B _ { 1 } ) < \infty$ , then

$$
m \left( \bigcap _ { k = 1 } ^ { \infty } B _ { k } \right) = \operatorname* { l i m } _ { k \to \infty } m ( B _ { k } )
$$

For a measurable set $E ,$ we say that a property holds almost everywhere on $E ,$ or it holds for almost all $x \in E ,$ , provided there is a subset $E _ { 0 }$ of for whichE $m ( E _ { 0 } ) = 0$ and the property holds for all $x \in E \sim E _ { 0 }$

Let $\{ E _ { k } \} _ { k = 1 } ^ { \infty }$ be a countable collection of measurable sets for which $\textstyle \sum _ { k = 1 } ^ { \infty } m ( E _ { k } ) < \infty$ . Then almost all $x \in \mathbb { R }$ belong to at most finitely many of the $E _ { k } { ' }$ s.

Let $E$ be a bounded measurable set of real numbers. Suppose there is a bounded, countably infinite set of real numbers $\Lambda$ for which the collection of translates of $E , \{ \lambda + E \} _ { \lambda \in \Lambda } .$ , is disjoint. Then $m ( E ) = 0$

Any set $E$ of real numbers with positive outer measure contains a subset that fails to be measurable.

There are disjoint sets of real numbers and for whichA B

$$
m ^ { * } ( A \cup B ) < m ^ { * } ( A ) + m ^ { * } ( B )
$$

The Cantor set $C$ is a closed, uncountable set of measure zero

The Cantor-Lebesgue function $\phi$ is an increasing continuous function that maps onto [0, 1] $[ 0 , 1 ]$ . Its derivative exists on the open set ${ \mathcal { O } } ,$ the complement in of the Cantor set [0, 1] $\phi ^ { \prime } = 0 \mathsf { o n } \mathcal { O }$ while $m ( \mathcal { O } ) = 1$

There is a measurable set, a subset of the Cantor set, that is not a Borel set.

## Royden Chapter 3 (Lebesgue Measurable Functions)

Let the function $f$ have a measurable domain . Then the following statements are equivalent: E

i. For all $c \in \mathbb { R }$ , the set $\{ x \in E | f ( x ) > c \}$ is measurable

ii. For all $c \in \mathbb { R }$ , the set $\{ x \in E | f ( x ) \geq c \}$ is measurable

iii. For all $c \in \mathbb { R }$ , the set $\{ x \in E | f ( x ) < c \}$ is measurable

iv. For all $c \in \mathbb { R } ,$ the set $\{ x \in E | f ( x ) \leq c \}$ is measurable

An extended real-valued function $f$ defined on $E$ is said to be Lebesgue measurable, or simply measurable, provided its domain $E { \mathrm { i s } }$ measurable and it satisfies one of the four above statements.

Let the function be defined on a measurable setf $E .$ Then $f$ is measurable iff for all open sets ${ \mathcal { O } } ,$ the inverse image of $\mathcal { O }$ under $f ,$ $f ^ { - 1 } ( \mathcal { O } ) = \{ x \in E | f ( x ) \in \mathcal { O } \}$ , is measurable

A real valued function that is continuous on its measurable domain is measurable

A monotone function that is defined on an interval is measurable

Let $f$ be an extended real-valued function $E .$ Then if $f$ is measurable on $E$ and $f = g \mathsf { a . e }$ . on $E ,$ then is measurable on g $E .$ For a measurable subset ofD $E , f$ is measurable on iff the restrictions ofE $f$ to andD $E { \sim } D$ are measurable.

Let $f$ and be measurable functions ong $E$ that are finite a.e. on $E .$ For any andα $\beta , \alpha f + \beta g$ is measurable on $E$ and $f g$ is measurable on .E

Let be a measurable real-valued function defined ong $E$ and a continuous real-valued function on all of f $\mathbb { R } .$ Then the composition $f \circ g$ is a measurable function on  E

For a sequence $\{ f _ { n } \}$ of functions with common domain , a function on and a subset of E f E A $E ,$ we say that the sequence $\{ f _ { n } \}$ converges to $f$ pointwise on provided  A lim $1 _ { n \to \infty } f _ { n } ( x ) = f ( x )$ for all $x \in A$ ; and the sequence $\{ f _ { n } \}$ converges to $f$ pointwise a.e. on provided it converges toA $f$ pointwise on $A { \sim } B$ where $m ( B ) = 0 ;$ and the sequence $\{ f _ { n } \}$ converges to $f$ uniformly on A provided for each $\epsilon > 0 ,$ , there is an index $N$ for which $| f - f _ { n } | < \epsilon \ o n \ A$ for all $n \geq N$

Let $\{ f _ { n } \}$ be a sequence of measurable functions on $E$ that converges pointwise a.e. on $E$ to the function $f .$ Then $f$ is measurable.

If $A$ is any set, the characteristic function of $A , \chi _ { A }$ , is the function on $\mathbb { R }$ defined by

$$
\chi _ { A } = \{ 1 | x \in A \& 0 | x \not \in A \}
$$

A real-valued function $\phi$ defined on a measurable set is called simple provided it is measurable and takes only a finite number ofE values

Let $f$ be a measurable real-valued function on . AssumeE $f$ is bounded on $E ,$ that is there exists an $M \geq 0$ for which $| f | \leq M$ on $E .$ Then for all $\epsilon > 0$ , there are simple functions $\phi _ { \epsilon }$ and $\psi _ { \epsilon }$ defined on which have the following approximation properties onE $E \mathrm { : }$

$$
\phi _ { \epsilon } \le f \le \psi _ { \epsilon } ; 0 \le \psi _ { \epsilon } - \phi _ { \epsilon } < \epsilon
$$

An extended real-valued function $f$ on a measurable set $E$ is measurable iff there is a sequence $\{ \phi _ { n } \}$ of simple functions on $E$ which converges pointwise on toE $f$ and has the property that $| \phi _ { n } | \leq | f$ on for all . If is nonnegative, we may choose| E n f $\left\{ \phi _ { n } \right\}$ to be increasing

Egoroff’s Theorem: Assume has finite measure. LetE $\{ f _ { n } \}$ be a sequence of measurable functions on that converges pointiwse on E $E$ to the real-valued function $f .$ Then for all $\epsilon > 0$ , there is a closed set contained inF $E$ for which $\left\{ f _ { n } \right\} \to f$ uniformly on $F$ and m ${ \left( E { \sim } F \right) } < \epsilon$

Under the assumptions of Egoroff’s Thm, for all $\nu > 0$ and $\delta > 0$ , there is a measurable subset ofA $E$ and an index $N$ for which $\left| f _ { n } - f \right| <$ on ν $A$ for all $n \geq N$ and $m ( E { \sim } A ) < \delta$

Let $f$ be a simple function defined on . Then for each E $\epsilon > 0$ , there is a continuous function ong $\mathbb { R }$ and a closed set $F$ contained in  E for which $f = g$ on $F$ and $m ( E { \sim } F ) < \epsilon$

Let $f$ be a real-valued measurable function on . Then for all E $\epsilon > 0$ , there is a continuous function on and a closed setg R $F$ contained in for whichE $f = g \circ \mathsf { n } F$ and $m ( E { \sim } F ) < \epsilon$

## Royden Chapter 4 (Integration)

The upper and lower sums for $f$ with respect to a partition $P$ are

$$
L ( f , P ) = \sum _ { i = 1 } ^ { n } m _ { i } \times ( x _ { i } - x _ { i - 1 } )
$$

$$
U ( f , P ) = \sum _ { i = 1 } ^ { n } M _ { i } \times ( x _ { i } - x _ { i - 1 } )
$$

where $m _ { i }$ is the infimum on the given partition, and $M _ { i }$ is the supremum

The lower and upper Riemann integrals of overf $[ a , b ]$ are defined by (respectively)

$$
\int _ { a } ^ { b } f = \operatorname* { s u p } \{ L ( f , P ) \}
$$

$$
\int _ { a } ^ { b } f = \operatorname* { i n f } \{ U ( f , P ) \}
$$

where $P$ is a partition of $[ a , b ]$

If the two above mentioned integrals are equal, then we say that $f$ is Riemann integrable over $[ a , b ] ^ { 2 }$

For a simple function $\psi$ defined on a set of finite measure $E ,$ we define the integral of $\psi$ over $E$ by

$$
\int _ { E } \psi = \sum _ { i = 1 } ^ { n } a _ { i } \times m ( E _ { i } )
$$

where $\textstyle \psi = \sum _ { i = 1 } ^ { n } a _ { i } \times \chi _ { E _ { i } }$ and each $E _ { i } = \{ x \in E | \psi ( x ) = a _ { i } \}$

Let $\{ E _ { i } \} _ { i = 1 } ^ { n }$ be a finite disjoint collection of measurable subsets of a set of finite measure $E .$ For $1 \leq i \leq n ,$ let $a _ { i }$ be a real number. If $\begin{array} { r } { \phi = \sum _ { i = 1 } ^ { n } a _ { i } \times \chi _ { E _ { i } } } \end{array}$ on $E _ { : }$ then

$$
\int _ { E } \phi = \sum _ { i = 1 } ^ { n } a _ { i } \times m ( E _ { i } )
$$

Linearity and Monotonicity of Integration: Let and be simple functions defined on a set of finite measureϕ ψ $E .$ Then for any and α $\beta ,$

$$
\int _ { E } ( \alpha \phi + \beta \psi ) = \alpha \int _ { E } \phi + \beta \int _ { E } \psi
$$

Moreover, ${ \mathfrak { f } } \phi \leq \psi$ on $E ,$ then

$$
\int _ { E } \phi \leq \int _ { E } \psi
$$

A bounded function on a domainf $E$ of finite measure is said to be Lebesgue integrable over $E$ provided its upper and lower Lebesgue integrals over $E$ are equal. The common value of the upper and lower integrals is called the Lebesgue integral.

Let $f$ be a bounded function defined on the closed, bounded interval $[ a , b ] . 1 9 f$ is Riemann integrable over $[ a , b ]$ , then it is Lebesgue integrable over $[ a , b ]$ and the two integrals are equal.

Let $f$ be a bounded measurable function on a set of finite measure . Then is integrable over E f $E .$

Let $f$ and be bounded measurable functions on a set of finite measure . Then for any and g E α $\beta ,$

$$
\int _ { E } ( \alpha f + \beta g ) = \alpha \int _ { E } f + \beta \int _ { E } g
$$

Moreover, if $f \leq g$ on $E ,$ then

$$
\int _ { E } f \leq \int _ { E } g
$$

Let $f$ be a bounded measurable function on a set of finite measure . Suppose and are disjoint measurable subsets of E A B $E .$ Then

$$
\int _ { A \cup B } f = \int _ { A } f + \int _ { B } f
$$

Let $f$ be a bounded measurable function on a set of finite measure $E .$ Then,

$$
\left| \int _ { E } f { \big | } \leq \int _ { E } | f | \right.
$$

Let $\{ f _ { n } \}$ be a sequence of bounded measurable functions on a set of finite measure $E . \mathsf { I f } \left\{ f _ { n } \right\} \to f$ uniformly on $E ,$ then lim $\begin{array} { r } { { \bf { 1 } } _ { n  \infty } \int _ { E } f _ { n } = \int _ { E } f } \end{array}$

The Bounded Convergence Theorem: Let $\{ f _ { n } \}$ be a sequence of measurable functions on a set of finite measure $E .$ Suppose $\{ f _ { n } \}$ is uniformly pointwise bounded on $E ,$ that is, there exists a number $M \geq 0$ for which $| f _ { n } | \leq M$ on for all . If E n $\left\{ f _ { n } \right\} \to f$ pointwise on $E ,$ then $\textstyle \operatorname* { l i m } _ { n \to \infty } \int _ { E } f _ { n } = \int _ { E } f$

Chebychev’s Inequality: Let $f$ be a nonnegative measurable function on $E .$ Then for any $\lambda > 0 ,$

$$
m ( \{ x \in E | f ( x ) \geq \lambda \} ) \leq { \frac { 1 } { \lambda } } \int _ { E } f
$$

Let $f$ be a nonnegative measurable function on $E .$ . Then $\begin{array} { r } { \int _ { E } f = 0 \ d \mathfrak { i } \mathfrak { f } f = 0 \mathsf { a . e . o n } E . } \end{array}$

Linearity and Monotonicity follow for nonnegative measurable functions.

Fatou’s Lemma: Let $\{ f _ { n } \}$ be a sequence of nonnegative measurable functions on . If pointwise a.e. on E {fn} → f $E ,$ then $\textstyle \int _ { E } f \leq$ liminf $\int _ { E } f _ { n }$

Monotone Convergence Theorem: Let $\{ f _ { n } \}$ be an increasing sequence of nonnegative measurable functions on $E . \mathsf { I f } \left\{ f _ { n } \right\} \to f$ pointwise a.e. on $E ,$ then

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { E } f _ { n } = \int _ { E } f
$$

A nonnegative measurable function $f$ on a measurable set $E$ is said to be integrable over $E$ provided $f _ { E } f < \infty$

Let the nonnegative function be integrable overf $E .$ Then $f$ is finite a.e. on $E .$

Let $f$ be a measurable function on . Then E $f ^ { + }$ and $f ^ { - }$ are integrable over iff E $| f |$ is integrable over $E .$

A measurable function $f$ on is said to be integrable over provided E E $\textstyle \int _ { E } | f | < \infty$ . When this is so, we define the integral by

$$
\int _ { E } f = \int _ { E } f ^ { + } - \int _ { E } f ^ { - }
$$

Let $f$ be integrable over . Then is finite a.e. on and E f E $\textstyle \int _ { E } f = \int _ { E / E _ { 0 } } f { \mathfrak { i } } \mathfrak { f } E _ { 0 } \subseteq E$ such that $m ( E _ { 0 } ) = 0 .$

The Integral Comparison Test: Let be a measurable function on . Suppose there is a nonnegative function that is integrable overf E g and dominatesE $f$ in the sense that $| f | \le g$ on . Then  E $f$ is integrable over and E

$$
\left| \int _ { E } f { \big | } \leq \int _ { E } | f | \right.
$$

$\mid \textsf { f } f$ and are integrable functions on , then linearity and monotonicity follow. g E

Let be integrable over . Assume and are disjoint measurable subsets of . Thenf E A B E

$$
\int _ { A \cup B } f = \int _ { A } f + \int _ { B } f
$$

Dominated Convergence Theorem: Let $\{ f _ { n } \}$ be a sequence of measurable functions on $E .$ Suppose there is an integrable function  g on and dominates E $\{ f _ { n } \}$ on in the sense thatE $| f _ { n } | \leq g$ on for all . IfE n $\left\{ f _ { n } \right\} \to f$ pointwise a.e. on $E ,$ then $f$ is integrable over and E lim $\begin{array} { r } { { } \cdot n \to \infty \int _ { E } f _ { n } = \int _ { E } f . } \end{array}$

General Dominated Convergence Theorem: Let $\{ f _ { n } \}$ be a sequence of measurable functions on $E$ that converges pointwise a.e. on toE $f .$ Suppose there is a sequence $\left\{ g _ { n } \right\}$ of nonnegative measurable functions on that converges pointwise a.e. on E $E$ to and g dominates $\{ f _ { n } \}$ on in the sense that E $| f _ { n } | \leq g _ { n }$ on for all . If E n

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { E } g _ { n } = \int _ { E } g < \infty
$$

then,

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { E } f _ { n } = \int _ { E } f
$$

Let be a set of finite measure andE $\delta > 0 .$ Then is the disjoint union of a finite collection of sets, each of which has measure lessE than . δ

A family $\mathcal { F }$ of measurable functions on is said to be uniformly integrable over E $E$ provided for each $\epsilon > 0$ , there is a $\delta > 0$ such that for each $f \in { \mathcal { F } } , { \mathfrak { i f } } A \subseteq E$ is measurable and $m ( A ) < \delta ,$ then $\int _ { A } | f | < \epsilon$

Let $\{ f _ { n } \} _ { k = 1 } ^ { n }$ be a finite collection of functions, each of which is integrable over $E .$ Then $\{ f _ { n } \} _ { k = 1 } ^ { n }$ is uniformly integrable.

Vitali COnvergence Theorem: Let be of finite measure. Suppose the sequence of functions E $\{ f _ { n } \}$ is uniformly integrable over $E .$ . I f $\left\{ f _ { n } \right\} \to f$ a.e. on , then  E $f$ is integrable over and E

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { E } f _ { n } = \int _ { E } f
$$

Let $f$ be a bounded function on a set of finite measure $E .$ Then $f$ is Lebesgue integrable over iff it is measurable. E

Let $f$ be a bounded function on the closed, bounded interval of $[ a , b ]$ . Then $f$ is Riemann integrable over $[ a , b ]$ iff the set of points in $[ a , \dot { b } ]$ at which fails to be continuous has measure zero. f

## Royden Chapter 6 (Differentiation)

Let $f$ be a monotone function on the open interval . Then (a, b) $f$ is continuous except possibly at a countable number of points in $( a , b )$

If the function $f$ is monotone on the open interval $( a , b )$ , then it is differentiable almost everywhere on $( a , b )$

https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dff 45fead17af37236a76c8.html

Define the variation of $f$ with respect to $P$ (a partition) by $\begin{array} { r } { V ( f , P ) = \sum _ { i = 1 } ^ { k } | f ( x _ { i } ) - f ( x _ { i - 1 } ) | } \end{array}$ , and the total variation of| $f$ on $[ a , b ]$ by $T V ( f ) = \operatorname* { s u p } \{ V ( f , P ) \}$ where $P$ is a partition on $[ a , b ]$

A real valued function $f$ on the closed and bounded interval $[ a , b ]$ is said to be of bounded variation on $[ a , b ]$ provided $T V ( f ) < \infty$

Jordan’s Thm: A function $f$ is of bounded variation on the closed, bounded interval $[ a , b ]$ iff it is the difference of two increasing functions on $[ a , b ]$

If the function is of bounded variation on the closed and bounded intervalf $[ a , b ]$ then it is differentiable almost everywhere on the open interval $( a , b )$ and $f ^ { \prime }$ is integrable over  [a, b]

A real valued function on a closed and bounded intervalf $[ a , b ]$ is said to be absolutely continuous on $[ a , b ]$ provided for each $\epsilon > 0$ there is a $\delta > 0$ such that for every finite disjoint collection $\{ ( a _ { k } , b _ { k } ) \} _ { k = 1 } ^ { n }$ of open intervals in $\begin{array} { r } { ( a , b ) , \mathfrak { i } \mathfrak { f } \sum _ { k = 1 } ^ { n } [ b _ { k } - a _ { k } ] < \delta , } \end{array}$ then

$$
\sum _ { k = 1 } ^ { n } | f ( b _ { k } ) - f ( a _ { k } ) | < \epsilon
$$

If the function is Lipschitz on a closed, bounded intervalf $[ a , b ]$ , then it is absolutely continuous on $[ a , b ]$

Let the function be absolutely continuous on the closed, bounded intervalf $[ a , b ]$ . Then is the difference of increasing absolutely f continuous functions and, in particular, is of bounded variation

Let the function $f$ be absolutely continuous on the closed, bounded interval $[ a , b ]$ . Then $f$ is differentiable almost everywhere on $( a , b )$ its derivative $f ^ { \prime }$ is integrable over $[ a , b ]$ and

$$
\int _ { b } ^ { a } f ^ { \prime } = f ( b ) - f ( a )
$$

We call a function $f$ on a closed, bounded interval $[ a , b ]$ the indefinite integral of over g $[ a , b ]$ provided that is Lebesgue integrable g over $[ a , b ]$ and for all $x \in [ a , b ]$

$$
f ( x ) = f ( a ) + \int _ { a } ^ { x } g
$$

A function on a closed, bounded intervalf $[ a , b ]$ is absolutely continuous on $[ a , b ]$ iff it is an indefinite integral over $[ a , b ]$

Let the function be monotone on the closed, bounded intervalf $[ a , b ]$ . Then $f$ is absolutely continuous on $[ a , b ]$ iff

$$
\begin{array} { r } { \int _ { a } ^ { b } f ^ { \prime } = f ( b ) - f ( a ) } \end{array}
$$

Let $f$ be integrable over the closed, bounded interval $[ a , b ]$ . Then $f ( x ) = 0$ for almost all $\begin{array} { r } { x \in [ a , b ] \mathfrak { H } \int _ { x _ { 1 } } ^ { x _ { 2 } } f = 0 } \end{array}$ for all $( x _ { 1 } , x _ { 2 } ) \subseteq [ a , b ]$

Let $f$ be integrable over the closed, bounded interval $[ a , b ]$ . Then for almost all $x \in ( a , b )$

$$
{ \frac { d } { d x } } \left[ \int _ { a } ^ { x } f \right] = f ( x )
$$

## Royden Chapter $7 ( L ^ { p }$ Spaces)

For most of this section, unless otherwise stated, define $E$ to be a measurable set of real numbers, and $\mathcal { F }$ to be the collection of all measurable extended real-valued functions on $E$ that are finite a.e. on . Define E $f$ and $g \in { \mathcal { F } }$ to be equivalent and $f \cong g$ iff $f ( x ) = g ( x )$ for almost all $x \in E$

We call a function $f \in { \mathcal { F } }$ essentially bounded provided there is some $M \geq 0$ called an essential upper bound for $f$ for which $| f ( \boldsymbol { x } ) | \leq M$ for almost all $x \in E$

functionals are real-valued functions that have as their domain linear spaces of functions

Let be a linear space. A real-valued functionalX $| | \cdot | |$ on $X$ is called a norm provided for each $f$ and $g \sin X ,$ and each real number , c $| | f | | \geq 0 \mathsf { a n d } | | f | | = 0 \mathsf { i f f } f = 0$

$$
| | f + g | | \leq | | f | | + | | g | |
$$

$$
| | c f | | = | c | | | f | |
$$

By a normed linear space we mean a linear space together with a norm. If is a linear space normed byX $| | \cdot | |$ we say that a function in is a unit function providedX $| | f | | = 1$

For any $f \in X , f \neq 0$ , the function $\frac { f } { | | f | | }$ is a unit function: it is a scalar multiple of $f$ which we call the normalization of $f$

The Normed Linear Space $L ^ { 1 } ( E )$

$$
| | f | | _ { 1 } = \int _ { E } | f |
$$

The Normed Linear Space $L ^ { \infty } ( E )$ : For a function $f \in L ^ { \infty } ( E )$ , define $| | f | | _ { \infty }$ to be the infimum of the essential upper bounds for $f .$ We call $| | f | | _ { \infty }$ the essential supremum of $f$ and claim that $| | \cdot | |$ is a norm on $L ^ { \infty } ( E )$

$\vert \vert f \vert \vert _ { \mathrm { m a x } } = \mathrm { m a x } _ { x \in [ a , b ] } \vert f ( x ) \vert$ is a norm and is called the maximum norm

For a measurable set $E$ where $1 < p <$ and a function in ∞ f $L ^ { p } ( E )$ , define

$$
\| f \| _ { p } = \left[ \int _ { E } | f | ^ { p } \right] ^ { 1 / p }
$$

The conjugate of a number $p \in ( 1 , \infty )$ is the number $\begin{array} { r } { q = \frac { p } { p - 1 } } \end{array}$ , which is the unique number $q \in ( 1 , \infty )$ for which

$$
\frac { 1 } { p } + \frac { 1 } { q } = 1
$$

Note, the conjugate of is defined to be and vice versa.1 ∞

Young’s Inequality: For $1 < p < \infty , q$ is the conjugate of and any two positive numbers and p a $b ,$

$$
a b \leq { \frac { a ^ { p } } { p } } + { \frac { b ^ { q } } { q } }
$$

Let $E$ be a measurable set $1 \leq p < \infty$ , and be the conjugate of . If q p $f$ belongs to $L ^ { p } ( E )$ and belongs to g $L ^ { q } ( E )$ , then their product $f \cdot g$ is integrable over and E

$$
\int _ { E } | f \cdot g | \leq | | f | | _ { p } \cdot | | g | | _ { q }
$$

This is known as Holder’s Inequality.

Let $E$ be a measurable set and $1 \leq p < \infty$ . If the functions $f$ and belong to g $L ^ { p } ( E )$ , then so does their sum $f + g$ and moreover,

$$
| | f + g | | _ { p } \leq | | f | | _ { p } + | | g | | _ { p }
$$

Cauchy-Schwarz Inequality: Let be a measurable set andE $f$ and measurable functions on g $E$ for which $f ^ { 2 }$ and $g ^ { 2 }$ are integrable over $\dot { E _ { ☉ } }$ . Then their product $f \cdot g$ is also integrable over and E

$$
\int _ { E } | f g | \leq { \sqrt { \int _ { E } f ^ { 2 } } } \cdot { \sqrt { \int _ { E } g ^ { 2 } } }
$$

Let $E$ be a measurable set and $1 < p < \infty$ . Suppose $\mathcal { F }$ is a family of functions in $L ^ { p } ( E )$ that is bounded in $L ^ { p } ( E )$ in the sense that there is a constant for whichM $| | f | | _ { p } \leq M$ for all in . Then the family f F $\mathcal { F }$ is uniformly integrable over . E

Let $E$ be a measurable set of finite measure and $1 \leq p _ { 1 } < p _ { 2 } \leq \infty$ . Then $L ^ { p _ { 2 } } ( E ) \subseteq L ^ { p _ { 1 } } ( E )$ . Furthermore $| | f | | _ { p _ { 1 } } \leq c | | f | | _ { p _ { 2 } }$ for all $f$ in $L ^ { p _ { 2 } } ( E )$ where $c = [ m ( E ) ] ^ { \frac { p _ { 2 } - p _ { 1 } } { p _ { 1 } p _ { 2 } } } { \mathrm { ~ i f ~ } } p _ { 2 } < \infty$ and $c = \left[ m ( E ) \right] ^ { \frac { 1 } { p _ { 1 } } } { \mathrm { ~ i f ~ } } p _ { 2 } = \infty$

A sequence $\{ f _ { n } \}$ in a linear space that is normed by X $| | \cdot | |$ is said to converge to in provided f X $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } | | f - f _ { n } | | = 0 } \end{array}$ . T his can also be written as $\{ f _ { n } \} \to f \mathfrak { i n } X$ or  lim $_ { \cdot n \to \infty } f _ { n } = f$ in .  X

A sequence $\{ f _ { n } \}$ in a linear space that is normed by is said to be Cauchy in X || ⋅ || $X$ provided for each $\epsilon > 0 ,$ , there is a natural number $N$ such that $| | f _ { n } - f _ { m } | | < \epsilon$ for all $m , n \geq N$

A normed linear space is said to be complete provided every Cauchy sequence inX $X$ converges to a function in $X .$ A complete normed linear space is called a Banach space

Let $X$ be a normed linear space. Then every convergent sequence in is Cauchy. Moreover, a Cauchy sequence in X $X$ converges if it has a convergent subsequence.

Let be a linear space normed by X $| | \cdot | | . \mathsf { A }$ sequence $\{ f _ { n } \}$ in is said to be rapidly Cauchy provided there is a convergent series of X positive numbers $\textstyle \sum _ { k = 1 } ^ { \infty } \epsilon _ { k }$ for which $| | f _ { k + 1 } - f _ { k } | | \leq \epsilon _ { k } ^ { 2 }$ for all  k

Let be a normed linear space. Then every rapidly Cauchy sequence in is Cauchy. Furthermore, every Cauchy sequence has aX X rapidly Cauchy subsequence.

Let $E$ be a measurable set and $1 \leq p \leq \infty$ . Then every rapidly Cauchy sequence in $L ^ { p } ( E )$ converges both wrt the $L ^ { p } ( E )$ norm and pointwise a.e. on $E$ to a function in $L ^ { p } ( E )$

Let $E$ be a measurable set and $1 \leq p \leq \infty$ . Then $L ^ { p } ( E )$ is a Banach space. Moreover, ${ \textsf { f } } \{ f _ { n } \} \to f \mathsf { i n } L ^ { p } ( E )$ , a subsequence of $\left\{ f _ { n } \right\}$ converges pointwise a.e. on to  E f

Let $E$ be a measurable set and $1 \leq p < \infty$ . Suppose $\{ f _ { n } \}$ is a sequence in $L ^ { p } ( E )$ that converges pointwise a.e. on $E$ to the function $f$ which belongs to $L ^ { p } ( E )$ . Then in iff  {fn} → f L (E) p  limn→∞ ∫ | = |f fn| p ∫ | p

Let $E$ be a measurable set and $1 \leq p < \infty$ . Suppose $\{ f _ { n } \}$ is a sequence in $L ^ { p } ( E )$ that converges pointwise a.e. on $E$ to the function $f$ which belongs to $L ^ { p } ( E )$ . Then $\left\{ f _ { n } \right\} \to f$ in $L ^ { p } ( E )$ iff $\{ | f | ^ { p } \}$ is uniformly integrable and tight over $E .$

https://rstudio-pubs-static.s3.amazonaws.com/342389_1cad63f68dff 45fead17af37236a76c8.html

Let be a normed linear space with normX $| | \cdot | |$ . Given two subsets and of withF G X ${ \mathcal { F } } \subseteq { \mathcal { G } }$ , we say that $\mathcal { F }$ is dense in ${ \mathcal { G } } ,$ provided for each function $g \in { \mathcal { G } }$ and $\epsilon > 0$ , there is a function $f \in { \mathcal { F } }$ for which $| | f - g | | < \epsilon$

Let be a measurable set andE $1 \leq p \leq \infty$ . Then the subspace of simple functions in $L ^ { p } ( E )$ is dense in $L ^ { p } ( E )$

Let $[ a , b ]$ be a closed, bounded interval and $1 \leq p < \infty$ . Then the subspace of step functions on $[ a , b ]$ is dense in $L ^ { p } [ a , b ]$

A normed linear space is said to be separable provided there is a countable subset that is dense in .X X

Let be a measurable set andE $1 \leq p < \infty$ . Then the normed linear space $L ^ { p } ( E )$ is separable.

## Royden Chapter 8 $( L ^ { p }$ Spaces Continued)

A linear functional on a linear space is a real-valued function on such that for and inX T X g h $X$ and and α $\beta$ real numbers,

$$
T ( \alpha \cdot g + \beta \cdot h ) = \alpha \cdot T ( g ) + \beta \cdot T ( h )
$$

For a normed linear space , a linear functional on is said to be bounded provided there is anX T X $M \geq 0$ for which $| T ( f ) | \leq M \cdot | | f | |$ for all $f \in X .$ The infimum of all such is called the norm of and denoted M T $\mathsf { b y } | | T | |$ ∗

Let be a normed linear space. Then the collection of bounded linear functionals on is a linear space on whichX X $| | \cdot | |$ is a norm. This∗ normed linear space is called the dual space of and denoted byX $X ^ { * }$

Let be a measurable set,E $1 \leq p < \infty$ , be the conjugate of , and belong to q p g $L ^ { q } ( E )$ . Define the functional onT $L ^ { p } ( E )$ by $\begin{array} { r } { T ( f ) = \int _ { E } g \cdot f } \end{array}$ for all $f \in L ^ { p } ( E )$ . Then $T$ is a bounded linear functional on $L ^ { p } ( E )$ and $| | T | | _ { * } = | | g | | _ { 4 }$ q

Let andT $S$ be bounded linear functionals on a normed linear space . If X $T = S$ on a dense subset $X _ { 0 }$ of , then X $T = S$

Let $I = [ a , b ]$ be a closed, bounded interval and $1 \leq p < \infty$ . Suppose us a bounded linear functional on T $L ^ { p } [ a , b ]$ . Then there is a function ing $L ^ { q } [ a , b ]$ , where is the conjugate of for which q p $\begin{array} { r } { T ( f ) = \int _ { I } g \cdot f } \end{array}$ for all $f \in L ^ { p } [ a , b ]$

Let be a measurable set,E $1 \le p < \infty$ and the conjugate of . For each q p $g \in L ^ { q } ( E )$ , define the bounded linear functional $\mathcal { R } _ { g }$ on $L ^ { p } ( E )$ by $\begin{array} { r } { \mathcal { R } _ { g } ( f ) = \int _ { E } g \cdot f } \end{array}$ for all in f $L ^ { p } ( E )$ . Then for each bounded linear functional on T $L ^ { p } ( E )$ , there is a unique function $g \in L ^ { q } ( E )$ for which $\mathcal { R } _ { g } = T$ and $| | T | | _ { * } = | | g | | _ { q }$ q

Let be a normed linear space. A sequenceX $\{ f _ { n } \}$ in is said to converge weakly in to in provided X X f X $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } T ( f _ { n } ) = T ( f ) } \end{array}$ for all $T \in X ^ { * }$

Let be a measurable set,E $1 \leq p < \infty$ , and the conjugate of . Then q p $\{ f _ { n } \}$ converges weakly in to in X f $L ^ { p } ( E )$ if f

lim $\begin{array} { r } { { 1 } _ { n \to \infty } \int _ { E } \boldsymbol { g } \cdot \boldsymbol { f } _ { n } = \int _ { E } \boldsymbol { g } \cdot \boldsymbol { f } } \end{array}$ for all $g \in L ^ { q } ( E )$

Let be a measurable set andE $1 \leq p < \infty$ . Suppose $\{ f _ { n } \}$ converges weakly in $L ^ { p } ( E )$ to . Then f $\{ f _ { n } \}$ is bounded in $L ^ { p } ( E )$ and $| | f | | _ { p } \leq \operatorname* { l i m i n f } | | f _ { n } | | _ { p }$

Let be a measurable set,E $1 \leq p < \infty$ , and the conjugate of . Suppose q p $\{ f _ { n } \}$ converges weakly to in f $L ^ { p } ( E )$ and $\left\{ g _ { n } \right\}$ converges strongly to ing $L ^ { q } ( E )$ . Then $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \int _ { E } g _ { n } \cdot f _ { n } = \int _ { E } g \cdot f } \end{array}$

The linear span of a subset of a linear space is the linear space consisting of all linear combinations of functions in , that is, theS X S linear space of functions of the form $\textstyle f = \sum _ { k = 1 } ^ { n } \alpha _ { k } \cdot f _ { k }$ where each $\alpha _ { k }$ is a real number and each $f _ { k }$ belongs to S

Let be a measurable set andE $1 \leq p < \infty$ . Suppose $\{ f _ { n } \}$ is a bounded sequence in $L ^ { p } ( E )$ and belongs to f $L ^ { p } ( E )$ . Then $\{ f _ { n } \}$ converges weakly to inf $L ^ { p } ( E )$ iff for every measurable subset of ,  A E lim $\begin{array} { r } { \mathfrak { i } _ { n \to \infty } \int _ { A } f _ { n } = \int _ { A } f . \mathfrak { H } p > 1 } \end{array}$ , it is sufficient to consider sets of finite measure.A

Let $[ a , b ]$ be a closed and bounded interval and $1 < p < \infty$ . Suppose $\{ f _ { n } \}$ is a bounded sequence in $L ^ { p } [ a , b ]$ and $f$ belongs to ${ \cal L } ^ { p } [ \dot { a } , b ]$ . Then $\{ f _ { n } \}$ converges weakly to in f $L ^ { p } [ a , b ]$ if f

$$
\operatorname* { l i m } _ { n \to \infty } \left[ \int _ { a } ^ { x } f _ { n } \right] = \int _ { a } ^ { x } f
$$

for all $x \in [ a , b ]$ . This theorem is false for $p = 1$

Let be a measurable set andE $1 < p < \infty$ . Suppose $\{ f _ { n } \}$ converges weakly to in f $L ^ { p } ( E )$ . Then $\{ f _ { n } \} \to f \mathfrak { i n } L ^ { p } ( E )$ iff lim $1 _ { n \to \infty } | | f _ { n } | | _ { p } = | | f | | _ { p }$

Let be a measurable set andE $1 < p < \infty$ . Suppose $\{ f _ { n } \}$ converges weakly in f $L ^ { p } ( E )$ . Then a subsequence of $\{ f _ { n } \}$ converges strongly in $L ^ { p } ( E )$ to $f { \mathfrak { i f f } } | | f | | _ { p } =$ liminf $| f _ { n } | | _ { p }$

Let be a measurable set andE $1 < p < \infty$ . Then every bounded sequence in $L ^ { p } ( E )$ has a subsequence that converges weakly in $L ^ { p } ( E )$ to a function in $L ^ { p } ( E )$