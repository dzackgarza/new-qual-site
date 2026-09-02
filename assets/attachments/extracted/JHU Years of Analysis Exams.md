# Qualifying Exam in Analysis, September 4, 2019, 9am-12noon.

## Part I: Real Analysis

Choose three of four problems and show all work with each problem on a new page.

1. Assume that $f _ { 1 } , f _ { 2 } , \ldots$ . is a sequence of positive continuous functions defined on $[ 0 , 1 ]$ with

$$
f ( x ) = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) { \mathrm { ~ f o r ~ e v e r y ~ } } x \in [ 0 , 1 ]
$$

and

$$
\int _ { 0 } ^ { 1 } f _ { n } ( x ) d x = 1 .
$$

(a) Is it always true that $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ( x ) d x \leq 1 ? } \end{array}$ Provide a proof if it is true or provide a counter example if it is false.

(b) Is it always true that $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ( x ) d x \geq 1 ? } \end{array}$ Provide a proof if it is true or provide a counter example if it is false.

2. Prove that if a sequence $f _ { 1 } , f _ { 2 } , \ldots$ of functions in $L ^ { 1 } ( \mathbb { R } )$ converges to $f$ in $L ^ { 1 } ( \mathbb { R } )$ , then there exists a subsequence $f _ { n _ { 1 } } , f _ { n _ { 2 } } , \ldots$ . that converges a.e. to $f$

3. Define

$$
f \ast g ( x ) : = \int _ { - \infty } ^ { \infty } f ( y ) g ( x - y ) \ : d y .
$$

Prove that if $f , g \in L ^ { 2 } ( \mathbb { R } )$ , then $f * g$ is a continuous function on $\mathbb { R }$

4. Prove that every closed convex subset of a Hilbert space has a unique element of minimal norm.

## Part II. Complex Analysis

Choose three of four problems and show all work with each problem on a new page.

1. Evaluate $\int _ { 0 } ^ { \infty } { \frac { \log x } { x ^ { 2 } + 2 } } d x$ by contour integration using the positively oriented contour from −R to R on the real axis (indented at the origin) and the positively oriented semicircle $| z | = R$ , Im $z > 0$ . Choose an appropriate branch of logarithm.

2. Let $f ( z )$ be an entire function such that

$$
\operatorname* { m a x } _ { | z | = R } | f ( z ) | \leq A R ^ { k } + B ,
$$

for positive constants A, B and all $R > 1 0 0 0$ . Show that $f$ is a polynomial of degree at most k.

3a. Define what is meant by a normal family of holomorphic functions on an open (possibly unbounded) domain U.

b. Suppose $\mathcal { F }$ is a normal family of holomorphic functions on the open unit disk D. Show that the family

$$
{ \mathcal { F } } ^ { \prime } = \{ f ^ { \prime } : f \in { \mathcal { F } } \}
$$

is also a normal family on D.

4. Let f be a holomorphic function in the punctured disk $\{ z : 0 < | z | < 2 \}$ satisfying

$$
| f ( z ) | \leq ( \log { \frac { 1 } { | z | } } ) ^ { 1 0 0 } \mathrm { { i n } } \left\{ | z | \leq 1 / 2 \right\} ,
$$

$$
| f ( z ) | = 1 \ \mathrm { o n } \ | z | = 1 .
$$

a. Show that f has a removable singularity at the origin.

b. Show that if $f ( z ) \neq 0$ in $| z | < 1$ , then f is constant.

c. (Extra credit) True or false, explain.

$f = \alpha z ^ { n }$ for $\alpha \in \mathbb { C } , | \alpha | = 1$ and an integer $n \geq 0$

# ANALYSIS QUALIFYING EXAM: SPRING 2019

Please answer three questions from the real analysis section and three questions from the complex analysis section.

## 1. REAL ANALYSIS

Question 1.1. Suppose that $f _ { j } \in L ^ { 2 } ( \mathbb { R } ^ { d } ) , j = 1 , 2 , . . . ,$ and $f \in L ^ { 2 } (  { \mathbb { R } } ^ { d } )$ satisfy

$$
\operatorname* { l i m } _ { j \to \infty } \int _ { \mathbb { R } ^ { d } } f _ { j } g = \int _ { \mathbb { R } ^ { d } } f g
$$

for all $g \in L ^ { 2 } (  { \mathbb { R } } ^ { d } )$ . That is, $f _ { j }$ converges to f weakly in $L ^ { 2 } .$ . Suppose that the sequence satisfies the uniform bound

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } ( 1 + | x | ) ^ { d } | f _ { j } ( x ) | \leq M < \infty .\tag{A}
$$

Show that $\| f _ { j } \| _ { 2 } \to \| f \| _ { 2 }$ and conclude that $\| f _ { j } - f \| _ { 2 } \to 0 .$ . That is $f _ { j }$ converges to f strongly in $L ^ { 2 } ( \mathbb { R } ^ { d } )$ . Show by example that condition (A) is necessary.

Question 1.2. Fix a measurable function $f : \mathbb { R } ^ { 2 } $ R and, for every $x , y \in \mathbb { R } ,$ , let

$$
f _ { x } : \mathbb { R } \to \mathbb { R } a n d f _ { y } : \mathbb { R } \to \mathbb { R }
$$

be given by $f _ { x } ( z ) = f ( x , z )$ and $f _ { y } ( z ) = f ( z , y )$ . Show that there exists such an f so that $f _ { x } \in L ^ { 1 } ( \mathbb { R } )$ for a.e. x and $f _ { y } \in L ^ { 1 } ( \mathbb { R } )$ for a.e. y but

$$
\int _ { \mathbb { R } } \left( \int _ { \mathbb { R } } f _ { x } ( y ) d y \right) d x \neq \int _ { \mathbb { R } } \left( \int _ { \mathbb { R } } f _ { y } ( x ) d x \right) d y .
$$

What does Fubini’s theorem imply about such $f ?$ What about Tonelli’s theorem?

Question 1.3. Let $f _ { i } : [ 0 , 1 ] \to \mathbb { R } , i = 1 , 2 , . . . ,$ , be an increasing sequence of continuous functions that is uniformly bounded, i.e., for all $x \in [ 0 , 1 ]$ and $i \geq 1 , f _ { i } ( x ) \leq f _ { i + 1 } ( x ) \leq$ $M < \infty f o r$ some fixed M. Show that li $\mathfrak { a } _ { i \to \infty } f _ { i } ( x ) = g ( x )$ is continuous if and only $i f$ the $f _ { i }$ converge uniformly to g.

Question 1.4. Show that lim $\scriptstyle \cdot t \to \infty \int _ { 1 } ^ { t } { \frac { \sin ( x ) } { x } } d x$ exists. Does $\textstyle f ( x ) \ = \ { \frac { \sin ( x ) } { x } }$ belong to $L ^ { 1 } ( ( 1 , \infty ) ) ?$

## 2. COMPLEX ANALYSIS

Question 2.1. Determine all holomorphic automorphisms of the upper half plane $u =$ $\lbrace z : I m z > 0 \rbrace$

Question 2.2. Let $f ( z )$ be holomorphic on $\mathbb { C } \backslash$ R and continuous on $\mathbb { C } .$ Show that f extends to an entire analytic function.

Question 2.3. Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { x ^ { - { \frac { 1 } { 3 } } } } { 1 + x } } d x .$

Question 2.4. Show that the punctured unit disk $\{ z \ : \ 0 < \ | z | < 1 \}$ and the annulus $\{ z : 1 < | z | < 2 \}$ cannot be conformally equivalent.

Name:

Date:

## Problem 1

Let $I = [ 0 , 1 ]$ and for $n \in \mathbb { N } .$ , consider $0 \leq j \leq 2 ^ { n } - 1$ . Define

$$
I _ { n j } = [ j 2 ^ { - n } , ( j + 1 ) 2 ^ { - n } ] .
$$

Let $f \in L ^ { 1 } ( I )$ and define

$$
E _ { n } ( f ) ( x ) = \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } { \Big ( } 2 ^ { n } \int _ { I _ { n j } } f d t { \Big ) } \chi _ { I _ { n j } } ( x ) .
$$

Prove that li $\mathrm { a } _ { n  \infty } E _ { n } ( f ) ( x ) = f ( x )$ a.e. in I .

## Problem 2

Prove that the unit ball of $L ^ { 2 }$ endowed with its natural strong topology is not compact.

## Problem 3

Prove that a normed vector space (X, k.k) is Banach if and only if every normally (sometimes called also absolutely) convergent series is convergent.

## Problem 4

Suppose that $f , g$ are entire functions with $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbb { C }$ . Prove that there is a constant $c \in \mathbb { C }$ such that $f = c g$

## Problem 5

This problem is about the integral

$$
I = \int _ { - \infty } ^ { \infty } { \frac { \sin { x } } { x } } d x .
$$

• Show directly that I is a convergent improper Riemann integral.

• Use a contour integral to evaluate I.

## Problem 6

Let $f$ and $g$ be functions holomorphic defined on a domain $U \subseteq \mathbb { C } .$ . Set $\varphi ( z ) = | f ( z ) | + | g ( z ) |$ for $z \in U$ . If $\varphi$ assumes a maximum value on $U ,$ show that both f and g are constants on U.

## Problem 7

Let $U \subseteq \mathbb { C }$ be an open set and

$$
A ^ { 2 } ( U ) = \{ f { \mathrm { ~ h o m o l o r p h i c ~ o n ~ } } U : \int _ { U } | f ( z ) | ^ { 2 } d x d y < \infty \} .
$$

Define

$$
( f , g ) = \int _ { U } f ( z ) { \overline { { g ( z ) } } } d x d y , \quad \forall f , g \in A ^ { 2 } ( U ) .
$$

Prove that $A ^ { 2 } ( U )$ is a Hilbert space when equipped with this inner product.

Name: Date:

## Problem 1

Let $I = [ 0 , 1 ]$ and for $n \in \mathbb { N } .$ , consider $0 \leq j \leq 2 ^ { n } - 1$ . Define

$$
I _ { n j } = [ j 2 ^ { - n } , ( j + 1 ) 2 ^ { - n } ] .
$$

Let $f \in L ^ { 1 } ( I )$ and define

$$
E _ { n } ( f ) ( x ) = \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } { \Big ( } 2 ^ { n } \int _ { I _ { n j } } f d t { \Big ) } \chi _ { I _ { n j } } ( x ) .
$$

Prove that lim $1 _ { n \to \infty } E _ { n } ( f ) ( x ) = f ( x )$ a.e. in I .

## Problem 2

Let $L ^ { 2 } = L ^ { 2 } ( \mathbb R ^ { d } )$ be the real Hilbert space endowed with its natural norm k.k derived from the real inner product $( f , g ) = \textstyle \int f g$ dm (where dm is Lebesgue measure on $\mathbb { R } ^ { d } )$ . We say that $f _ { n } \in L ^ { 2 }$ converges weakly to $f \ \operatorname { i f } \ ( f _ { n } , g )  ( f , \overbrace { g } )$ for every $g \in L ^ { 2 }$

• Prove that if $f _ { n }$ converges weakly to f and $\| f _ { n } \| \to \| f \|$ then $f _ { n }$ converges to $f$ in the strong topology.

• Prove that there exists a sequence of bounded functions in $L ^ { 2 }$ which is not converging in $L ^ { 2 }$ but weakly converging up to a subsequence possibly. What do you conclude on the unit ball of $L ^ { 2 }$ endowed with the strong topology ?

## Problem 3

Let $I = [ 0 , 1 ]$ and denote $\| . \| _ { p }$ the p-norm $\begin{array} { r } { \| f \| _ { p } = \bigg ( \int _ { I } | f | ^ { p } \bigg ) ^ { 1 / p } } \end{array}$ for $1 \leq p < \infty$ (we admit this is a norm) and $\| f \| _ { \infty } = \csc \operatorname* { s u p } | f |$

• Show that the space of continuous functions on I endowed with the norm $\| . \| _ { p }$ for $1 \leq p < \infty$ is not a Banach space.

• Prove that the space of (Lebesgue) measurable functions on I such that their p-norm is finite is a Banach space for $1 \leq p \leq \infty$

• Prove that there is no smooth function h such that $f * h = f$ for every $f \in L ^ { 1 } ( I )$

• Prove the H¨older inequality: for $p , q \geq 1$ such that $\textstyle { \frac { 1 } { p } } + { \frac { 1 } { q } } = 1$

$$
\int _ { I } f g \leq \| f \| _ { p } \| g \| _ { q }
$$

One can use the inequality $\textstyle a b \leq { \frac { a ^ { p } } { p } } + { \frac { a ^ { q } } { q } }$ for any $a , b \geq 0$

• Deduce the Young inequality: $L ^ { p } * L ^ { q } \subset L ^ { r }$ for $\begin{array} { r } { \frac { 1 } { p } + \frac { 1 } { q } = 1 + \frac { 1 } { r } } \end{array}$

## Problem 4

Let f be an entire function. Suppose that for each $z _ { 0 } \in \mathbb { C }$ , the power series expansion

$$
f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } ( z - z _ { 0 } ) ^ { n }
$$

has at least one coefficient $c _ { n } = 0$ . Show that f is a polynomial.

## Problem 5

Let U be an open subset of C. Let $z _ { \mathrm { 0 } }$ be a point in U, and suppose that f is a meromorphic function on U with a pole at $z _ { \mathrm { 0 } }$ . Prove that there is no holomorphic function $g : U \setminus \{ z _ { 0 } \}  \mathbb { C }$ such that $e ^ { g ( z ) } = f ( z )$ for all $z \in U \setminus \{ z _ { 0 } \}$

## Problem 6

Suppose f is holomorphic in an annulus $r < | z | < R ,$ and there exists a sequence of holomorphic polynomials $p _ { n }$ converging to f uniformly on compact subset of the annulus. Show that f can be extended to the disc $\{ | z | < R \}$ as a holomorphic function.

## Problem 7

Let U be an open subset of C. We use the notion

$$
\| f \| _ { L ^ { 2 } ( U ) } = \left( \int _ { U } | f | ^ { 2 } d x d y \right) ^ { 1 / 2 } .
$$

• Let $f : U \to \mathbb { C }$ be a holomorphic function. Show that for any compact set $K \subset U$ , there is a constant $C _ { K } .$ , such that

$$
\operatorname* { s u p } _ { z \in K } | f ( z ) | \leq C _ { K } \| f \| _ { L ^ { 2 } ( U ) } .
$$

• Prove that {f is holomorphic on $U : \| f \| _ { L ^ { 2 } ( U ) } \leq 1 \}$ is a normal family.

• Suppose U is the punctured disc $D ( 0 , 1 ) - \{ 0 \}$ . If f is holomorphic on U and $\| f \| _ { L ^ { 2 } ( U ) } < \infty$ , prove that $z = 0$ is a removable singularity of f .

# Qualifying Exam - Analysis-Fall 2017

12:30-3:30pm, Sept 8, 2017

1. Let $f _ { n }$ be a sequence of continuous functions on R satisfying $0 \leq f _ { n } \leq f _ { n + 1 } \leq 1$ for all $x \in \mathbb { R }$ and $n \in \mathbb { Z } ^ { + }$ . Let $f ( x ) = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ . Show that if $f$ is continuous at x, then for any $\epsilon > 0$ there exist δ and N such that $| f _ { n } ( y ) - f _ { n } ( x ) | < \epsilon$ whenever $| y - x | < \delta$ and $n > N$

2. Let $f \in L ^ { p } ( \mathbb { R } ^ { n } )$ . Show that

$$
\operatorname* { l i m } _ { h \to 0 } \| f ( x - h ) - f ( x ) \| _ { L ^ { p } } = 0 .
$$

3. For a Radon measure $\mu ,$ with $\textstyle \int _ { \mathbb { R } ^ { n } } d \mu = C$ . Prove that for all $\epsilon > 0$ , there exists a set $E _ { \epsilon } \subset \mathbb { R } ^ { n }$ s.t. $\begin{array} { r } { \mathcal { M } ^ { 1 } ( E _ { \epsilon } ) : = \operatorname* { i n f } _ { E _ { \epsilon } \subset \cup B _ { i } } \{ \sum _ { i } \mathrm { d i a m } \tilde { B _ { i } } \} < } \end{array}$ 10 and for any x $: \notin E _ { \epsilon } , r > 0$

$$
\int _ { B _ { r } ( x ) } d \mu \leq \frac { C r } { \epsilon } .
$$

(Hint: use Vitali covering lemma.)

4. Let $f ( z )$ be a holomorphic function on $D : = \{ z \in \mathbb { C } : | z | < 1 \} , | f ( z ) | < 1 , f ( \alpha ) = 0$ for some $| \alpha | < 1$ . Show that for $z \in D$

$$
| f ( z ) | \leq | { \frac { z - \alpha } { 1 - { \bar { \alpha } } z } } | .
$$

5. Let $f$ be an entire function $| R e ( f ( z ) ) | \leq C ( 1 + | z | ) ^ { p }$ for some $p > 0 , C > 0$ . Show that $f$ is a polynomial.

6. Let u be a subharmonic function defined on $\mathbb { C } .$ Let $M ( r ) : = \operatorname* { m a x } _ { | z | = r } u ( z )$ . Prove that

$$
u ( z ) \leq { \frac { \log r _ { 2 } - \log | z | } { \log r _ { 2 } - \log r _ { 1 } } } M ( r _ { 1 } ) + { \frac { \log | z | - \log r _ { 1 } } { \log r _ { 2 } - \log r _ { 1 } } } M ( r _ { 2 } )
$$

for $0 < r _ { 1 } \le | z | \le r _ { 2 }$

## Qualifying Exam - Analysis - Spring 2017

Justify your answers to all problems.

1. Let $f : \mathbb { R } \to [ 0 , \infty )$ be a measurable function and $\varphi : [ 0 , \infty )  [ 0 , \infty )$ be a monotonic, absolutely continuous function on $[ 0 , T ]$ for every $T < \infty$ . Assume $\varphi ( 0 ) = 0$ . Prove

$$
\int _ { \mathbb { R } } \varphi \circ f \ d x = \int _ { 0 } ^ { \infty } m ( \{ x : f ( x ) > t \} ) \varphi ^ { \prime } ( t ) \ d t .
$$

2. Let H be a Hilbert space equipped with an inner product $( \cdot , \cdot )$ and a norm $| | \cdot | | = ( \cdot , \cdot ) ^ { \frac { 1 } { 2 } }$ Recall the following: A sequence $\{ f _ { k } \} \subset { \mathcal { H } }$ is said converge to $f \in \mathcal H$ if $\vert \vert f _ { k } - f \vert \vert  0$ . A sequence $\{ f _ { k } \} \subset { \mathcal { H } }$ is said converge weakly to $f \in { \mathcal { H } }$ if $( f _ { k } , g )  ( f , g )$ for any $g \in { \mathcal { H } }$ . Prove the following statements:

(a) $\{ f _ { k } \}$ converges to f if and only if $\vert \vert f _ { k } \vert \vert  \vert \vert f \vert \vert$ and $\{ f _ { k } \}$ converges weakly to $f .$

(b) If H is a finite dimensional Hilbert space, then the weak convergence implies convergence. Give a counter example to show that weak convergence does not necessarily imply convergence in an infinite dimensional Hilbert space.

(c) If a sequence $\{ f _ { k } \}$ converges weakly to $f ,$ then there exists a subsequence $\{ f _ { k _ { n } } \}$ such that

$$
\frac { f _ { k _ { 1 } } + \cdots + f _ { k _ { n } } } { n }
$$

converges to $f .$ (You may use the fact that a weakly convergent sequence is a bounded sequence.)

3. Let $\{ E _ { k } \}$ be a sequence of (Lebesgue) measurable sets in $\mathbb { R } ^ { k }$ such that

$$
\sum _ { k = 1 } ^ { \infty } m ( E _ { k } ) < \infty .
$$

Prove that almost every $\boldsymbol { x } \in \mathbb { R } ^ { k }$ lie in at most finitely many sets $E _ { k }$

4. Let $U \subset \mathbb { C }$ be an open set, $D = \{ z \in C : | z | < 1 \}$ and $\mathcal { F }$ be the set of all holomorphic functions $f : U  D$ . Given $z _ { 0 } \in U$ , show that there exists $f _ { 0 } \in \mathcal { F }$ such that

$$
| f _ { 0 } ^ { \prime \prime } ( z _ { 0 } ) | = \operatorname* { s u p } _ { f \in \mathcal { F } } | f ^ { \prime \prime } ( z _ { 0 } ) | .
$$

5. Describe all holomorphic functions on $\mathbb { C } \backslash \{ 0 \}$ with the property that

$$
| f ( z ) | \leq | z | ^ { 2 } + { \frac { 1 } { | z | ^ { { \frac { 1 } { 2 } } } } } , \quad \forall z \in \mathbb { C } \backslash \{ 0 \} .
$$

6. Let $f : U \to \mathbb { C }$ be a non-constant holomorphic function where $U \subset \mathbb { C }$ is an open set containing the closure D of the unit disk $D = \{ z \in C : | z | < 1 \}$ . If $| f ( z ) | = 1$ for all $z \in \partial D$ ， then prove that $D \subset f ( { \overline { { D } } } )$

# Qualifying Exam - Analysis - Fall 2016

## Justify your answers to all problems.

1. Assume $f , f _ { j } \subset L ^ { 2 } ( [ 0 , 1 ] )$ for $j = 1 , 2 , . . .$ . and $| | f _ { j } - f | | _ { L ^ { 2 } } \to 0$ . Prove there exists a subsequence $\{ f _ { j ^ { \prime } } \} \subset \{ f _ { j } \}$ such that $f _ { j ^ { \prime } } \to f { \mathrm { ~ a . e ~ } }$

2. Suppose A is a Lebesgue measurable set in R with $m ( A ) > 0$ Does there exists a sequence $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ such that the complement of $\textstyle { \bigsqcup _ { n = 1 } ^ { \infty } ( A + x _ { n } ) }$ in R has measure 0? Justify your answer. (We define $A + x _ { n } = \{ a + x _ { n } \in \mathbb { R } : a \in A \} . )$

3. Let H be an infinite dimensional Hilbert space. Determine if the following statements are true or false. If true, provide a proof. If false, provide a counter example.

(a) A sequence $\left\{ f _ { n } \right\}$ in H with $\left| \left| f _ { n } \right| \right| = 1$ for all n has a subsequence that converges in H.

(b) A sequence $\left\{ f _ { n } \right\}$ in H with $| | f _ { n } | | = 1$ for all n has a subsequence that converges weakly in H.

4. Prove that if a sequence of harmonic functions on the open disk converges uniformly on compact subset of the disk, then the limit is harmonic.

5. Let f be a one-to-one analytic function defined on the unit disk D centered at the origin and $f ( 0 ) = 0$ . Show that the function $g ( z ) = { \sqrt { f ( z ^ { 2 } ) } }$ has a single-valued branch and is also one-to-one.

6. Let $U \subset \mathbb { C }$ be an open set containing the closure $\overline { { D } }$ of a unit disk. If a sequence $\{ f _ { n } : U \to \mathbb { C } \}$ of holomorphic functions converges uniformly to $f$ on compact subsets of $U ,$ then show that there exists an integer N such that $f$ and $f _ { n }$ have the same number of zeros in D for $n \geq N$

1. Prove the absolute continuity of the Lebesgue integral; in other words, prove that if $f$ is integrable on $\mathbb { R } ^ { d }$ , then for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
\int _ { E } | f | < \epsilon \ \mathrm { w h e n e v e r } \ m ( E ) < \delta .
$$

2. Prove that the Hardy-Littlewood maximal function $f ^ { * }$ for an integrable function f satisfies

$$
m ( \{ x \in \mathbb { R } ^ { d } : f ^ { * } ( x ) > \alpha \} \leq \frac { 3 ^ { d } } { \alpha } | | f | | _ { L ^ { 1 } ( \mathbb { R } ^ { d } ) }
$$

where $\alpha > 0$ . Recall that

$$
f ^ { * } ( x ) = \operatorname* { s u p } _ { x \in B } { \frac { 1 } { m ( B ) } } \int _ { B } | f ( y ) | d y , \quad x \in \mathbb { R } ^ { d }
$$

where the supremum is taken over all balls containing the point x. You may assume the Vitali 3-times Covering Lemma. State it clearly if you use $i t .$

3. Let $f : [ 0 , 1 ]  [ 0 , 1 ]$ be a continuous function and $\phi : \mathbb { R }  \mathbb { R }$ be $\mathrm { ~ a ~ } C ^ { 1 }$ function with $\phi ( 0 ) = 0$ . Prove

$$
\int _ { 0 } ^ { 1 } \phi \circ f \ d x = \int m ( \{ x \in [ 0 , 1 ] : f ( x ) > t \} ) \phi ^ { \prime } ( t ) d t
$$

4. Let $U \subset \mathbb { C }$ be an open set and

$$
A ^ { 2 } ( U ) = \{ f { \mathrm { ~ h o l o m o r p h i c ~ o n ~ } } U : \int _ { U } | f ( z ) | ^ { 2 } d x d y < \infty \} .
$$

Define

$$
< f , g > = \int _ { U } f ( z ) { \overline { { g ( z ) } } } d x d y , \quad \forall f , g \in A ^ { 2 } ( U ) .
$$

Prove that $A ^ { 2 } ( U )$ is a Hilbert space when equipped with this inner product.

5. Let $f : D  D$ be a holomorphic function where $D = \{ z \in \mathbb { C } : | z | < 1 \}$ is the unit disk. Prove that if $f$ has at least 2 fixed points then $f$ is the identity map. (Note: A point a is said to be a fixed point of f if $f ( a ) = a . )$

6. Assume that $f : \mathbb { C } \to \mathbb { C }$ is an entire function, not identically equal to 0 and the let ${ \mathcal { Z } } = \{ z \in \mathbb { C } : f ( z ) = 0 \}$ . Prove that if $\mathcal { Z }$ is unbounded, then $f$ has an essential singularity at ∞.

7. Determine the number of zeroes of the polynomial

$$
2 z ^ { 5 } - 6 z ^ { 2 } + z + 1 = 0
$$

in the annulus $1 \leq | z | \leq 2$

# QUALIFYING EXAM - ANALYSIS - FALL 2015

## Justify your answers to all problems.

Notation: R is the real line, C is the complex plane and $D ( P , r ) \subset \mathbb { C }$ is the disk of radius r centered at point P .

1. Suppose $\{ f _ { n } \} _ { n = 1 } ^ { \infty } \subset L ^ { 2 } ( \mathbb { R } )$ is a sequence that converges to 0 in the $L ^ { 2 }$ norm; in other words,

$$
| | f _ { n } | | _ { L ^ { 2 } ( \mathbb { R } ) } = \left( \int _ { - \infty } ^ { \infty } | f _ { n } | ^ { 2 } \ d x \right) ^ { \frac { 1 } { 2 } } \to 0 .
$$

Prove that there exists a subsequence $\{ f _ { n _ { k } } \}$ such that $f _ { n _ { k } }  0$ almost everywhere.

2. Determine whether the following statements are true and false. If true, provide a proof. If false, prove a counter example.

(a) If $f ( x )$ is a increasing, continuous function on the interval $[ 0 , 1 ]$ such that $f ( 0 ) = 0$ and $f ( 1 ) = 1$ , then there exists a set $E \subset [ 0 , 1 ]$ of positive measure such that $f ^ { \prime } ( x ) > 0$

(b) If $f ( x )$ is a strictly increasing, absolutely continuous function on the interval [0, 1] with $f ( 0 ) = 0$ and $f ( 1 ) = 1$ , then the set $f ^ { - 1 } ( E ) \cap \{ x \in [ 0 , 1 ] : f ^ { \prime } ( x ) > 0 \}$ is measurable for any measurable set $E \subset [ 0 , 1 ]$

3. Let $\{ \varphi _ { k } \} _ { k = 1 } ^ { \infty }$ be an orthonormal basis for $L ^ { 2 } ( \mathbb { R } ^ { d } )$ and define $\varphi _ { k , j } ( x , y ) = \varphi _ { k } ( x ) \varphi _ { j } ( y )$ Prove that $\{ \varphi _ { k , j } \} _ { k , j = 1 } ^ { \infty }$ is an orthonormal basis of $L ^ { 2 } ( \mathbb R ^ { d } \times \mathbb R ^ { d } )$

4. Let $U \subset \mathbb { C }$ be an open set containing $\overline { { \boldsymbol { D } } } ( \boldsymbol { P } , \boldsymbol { r } )$ . Prove that if $f : U \to \mathbb { C }$ is a holomorphic function such that $f$ is nowhere zero on $\partial D ( P , r )$ and $g : U \to \mathbb { C }$ is a holomorphic function sufficiently uniformly close to $f$ on $\partial D ( P , r )$ , then the number of zeros of $f$ in $D ( P , r )$ equals the number of zeros of g in $D ( P , r )$ (counting multiplicity).

5. If $f = u + i v$ is an entire function with the property that $u ( z ) \leq 0$ for all $z \in \mathbb { C }$ , what can you say about $f ?$

6. If $D ( 0 , 1 ) \to \mathbb { C }$ is a function such that $f ^ { 2 }$ and $f ^ { 3 }$ are both holomorphic, prove $f$ is holomorphic.

7. Compute the integral

$$
\int _ { 0 } ^ { \infty } { \frac { ( \log x ) ^ { 2 } } { 1 + x ^ { 2 } } } d x .
$$

Justify your answers to all problems.

1. Assume $f , f _ { j } \subset L ^ { 2 } ( \mathbb { R } ^ { n } )$ for $j = 1 , 2 , . . . , f _ { j } \to f$ a.e. and $\textstyle \int f _ { j } ^ { 2 } d x \to \int f ^ { 2 } d x$ . Prove $\begin{array} { r } { \int | f _ { j } - f | ^ { 2 } d x  \mathrm { 0 } } \end{array}$

2. Let $\varphi : \mathbb { R }  \mathbb { R }$ be a non-negative, $C ^ { \infty }$ function with compact support such that

$$
\int _ { \mathbb { R } } \varphi ( x ) d x = 1 .
$$

Define

$$
\varphi _ { \sigma } ( x ) = \sigma ^ { - 1 } \varphi ( \frac { x } { \sigma } ) \mathrm { a n d } u _ { \sigma } ( x ) = \int \varphi _ { \sigma } ( x - y ) u ( y ) d y .
$$

For $u \in L ^ { 2 } ( \mathbb { R } )$ R), prove

$$
\int _ { \mathbb { R } } | u _ { \sigma } ( x ) | ^ { 2 } d x \leq \int _ { \mathbb { R } } | u ( x ) | ^ { 2 } d x .
$$

3. Assume $f : [ 0 , 1 ] \to \mathbb { R }$ is uniformly continuous, increasing and convex. Prove $f$ is differentiable almost everywhere and

$$
f ( 1 ) - f ( 0 ) = \int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) d x .
$$

4. Assume $f : [ 0 , 1 ] \ \to \ \mathbb { R }$ is a measurable function such that $f g \in L ^ { 1 } ( [ 0 , 1 ] )$ for all $g \in L ^ { 2 } ( [ 0 , 1 ] )$ . Prove ${ \dot { f } } \in L ^ { 2 } ( [ 0 , 1 ] )$

5. Let $U \subset \mathbb { C }$ be an open set. Assume $f , g : U \to \mathbb { C }$ are holomorphic function such that $\bar { f } g$ is holomorphic. Prove either f is constant or g is identically equal to 0.

6. Assume $f : \mathbb { C } \to \mathbb { C }$ is a non-constant entire function. Prove $f ( \mathbb { C } )$ is dense in C.

7. Prove that $z ^ { 5 } + 3 z ^ { 3 } + 7$ has all its zeros in the disk $D ( 0 , 2 ) = \{ z \in \mathbb { C } : | z | < 2 \}$

8. Let $D ( 0 , r ) = \{ z \in C : | z | < r \}$ . Assume $r > 1$ and $f : \overline { { { D ( 0 , r ) } } } \backslash D ( 0 , 1 )  \mathbb { C }$ is a continuous function, holomorphic on $D ( 0 , r ) \backslash \overline { { D ( 0 , 1 ) } }$ that satisfies

$$
\operatorname* { m a x } _ { \partial D ( 0 , 1 ) } | f ( z ) | = 1 \mathrm { a n d } \operatorname* { m a x } _ { \partial D ( 0 , r ) } | f ( z ) | = R .
$$

Prove log $| f ( z ) | \leq { \frac { \log R } { \log r } } \log | z |$

# Qualifying Exam - Analysis - Fall 2014

## Justify your answers to all problems.

1. Let Q be the unit square in $\mathbb { R } ^ { 2 }$ . Consider functions $f _ { n } \in L ^ { 1 } ( Q )$ such that

$f _ { n }  f$ almost everywhere in Q and $\int _ { Q } | f _ { n } | \to \int _ { Q } | f | < \infty .$

(a) Prove that $\textstyle \int _ { A } | f _ { n } | \to \int _ { A } | f |$ for every measurable subset A of $Q$

(b) Prove that $f _ { n }  f$ in $L ^ { 1 }$

2. Let $f \in L ^ { 1 } ( \mathbb { R } ^ { d } )$ and $M _ { f }$ denote the Hardy-Littlewood maximal function of $f ;$ in other words,

$$
M _ { f } ( x ) = \operatorname* { s u p } _ { B } { \frac { 1 } { m ( B ) } } \int _ { B } | f ( y ) | d y , \quad x \in \mathbb { R } ^ { d }
$$

where the supremum is taken over all balls containing the point x. Prove that

$$
m \big ( \{ x : M _ { f } ( x ) > \alpha \} \big ) \leq \frac { A } { \alpha } | | f | | _ { L ^ { 1 } ( \mathbb { R } ^ { d } ) } , \quad \forall \alpha > 0
$$

where A is a constant depending only on d and $\begin{array} { r } { | | f | | _ { L ^ { 1 } ( \mathbb { R } ^ { d } ) } = \int _ { \mathbb { R } ^ { d } } | f ( x ) | d x . } \end{array}$

3. Let X and Y be Hilbert spaces and $L : X \to Y$ be a bounded linear operator. Prove that the following two conditions are equivalent:

(a) The image $L ( \mathbf { B } )$ of the unit ball in X has compact closure in $Y .$

(b) There is a sequence of bounded linear operators $\{ L _ { n } : X \to Y \}$ such that the image of $L _ { n } ( X )$ is finite dimensional and such that $| | L _ { n } - L | |  0$ . (Here, || · || is the operator norm.)

4. Let $\Omega \subset \mathbb { C }$ be a bounded region and $\left\{ f _ { n } \right\}$ be a sequence of continuous functions on Ω which are holomorphic in Ω. If $\{ f _ { n } \}$ converges uniformly on the boundary of Ω, then prove that $f _ { n }$ converges uniformly on Ω.

## 5. Compute

$$
\int _ { 0 } ^ { \infty } { \frac { \cos a x } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x = { \frac { \pi ( a + 1 ) e ^ { - a } } { 4 } } , \quad a > 0 .
$$

6. Assume that f and g are entire functions and that g never vanishes. If $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbb { C }$ , then prove that there is a constant C such that $f ( z ) = C g ( z )$

7. Let $D \subset \mathbb { C }$ be the unit disk. Prove that every one-to-one conformal mapping of D to D is given by a linear fractional transformation.

1. Prove the following statement without using Ergoroff’s Theorem: Suppose $\{ f _ { k } \} _ { k = 1 } ^ { \infty }$ is a sequence of measurable functions defined on a measurable set $E ,$ $f _ { k }  f$ a.e. on E and there exists $g \in L ^ { 1 } ( E )$ such that $| f _ { k } | \le g$ for all k. Given $\epsilon > 0$ , there exists a closed set $A _ { \epsilon }$ such that $m ( E \backslash A _ { \epsilon } ) < \epsilon$ and $f _ { k }  f$ uniformly on $A _ { \epsilon }$

2. Let $f \in L ^ { 1 } ( \mathbb { R } )$ and define $E _ { \alpha } = \{ x : | f ( x ) | > \alpha \}$ . Prove that

$$
\int _ { \mathbb { R } } | f ( x ) | d x = \int _ { 0 } ^ { \infty } m ( E _ { \alpha } ) d \alpha .
$$

3. Let $f : \mathbb { R } \to \mathbb { R }$ be a measurable function. Prove the following statement: There exists $M > 0$ such that $| f ( x ) - f ( y ) | \leq M | x - y |$ for all $x , y \in \mathbb { R }$ if and only if $f$ is absolutely continuous and $| f ^ { \prime } | \le M$

4. (a) Prove that the operator $T \ : \ L ^ { 2 } ( [ 0 , 1 ] ) \ \to \ L ^ { 2 } ( [ 0 , 1 ] )$ defined by setting $T [ f ] ( x ) = x f ( x )$ is continuous and symmetric (self-adjoint).

(b) Prove that T is not compact.

5. Let $D = \{ z \in \mathbb { C } : | z | < 1 \}$ and $f : D  D$ be a holomorphic function. Prove

$$
{ \frac { | f ( 0 ) | - | z | } { 1 + | f ( 0 ) | | z | } } \leq | f ( z ) | \leq { \frac { | f ( 0 ) | + | z | } { 1 - | f ( 0 ) | | z | } } , \forall z \in D .
$$

6. For $t \in \mathbb { R }$ , compute

$$
\operatorname* { l i m } _ { A  \infty } \int _ { - A } ^ { A } { \frac { \sin x } { x } } e ^ { i x t } d x .
$$

7. Let $U \subset \mathbb { C }$ be an open set, $f : U \to \mathbb { C }$ be a holomorphic function and $z _ { 0 } \in U$ Prove that if $f ^ { \prime } ( z _ { 0 } ) = 0$ , then f is not one-to-one in any neighborhood of $z _ { \mathrm { 0 } }$

8. Prove that if f is an entire function and $| f ( z ) | \leq a + b | z | ^ { k }$ for all $z ~ \in ~ \mathbb { C }$ where $a , b$ and k are positive real numbers, then f is a polynomial.

Justify your answers to all problems.

1. Let I denote the interval (0, 1). Suppose that $f : I  \mathbb { R }$ with $\textstyle \int _ { 0 } ^ { 1 } | f ( t ) | d t < + \infty$ Define $g : I  \mathbb { R }$ by

$$
g ( x ) = \int _ { x } ^ { 1 } \frac { f ( t ) } { t } d t .
$$

Show that $g \in L ^ { 1 } ( I )$

2. Does there exist a nonempty measurable set $E \subset \mathbb { R }$ satisfying the following two properties:

(a) given $x , y \in E$ , there exists $z \not \in E$ that lies between x and $y ;$

(b) E has no isolated points?

3. Prove that smooth compactly supported functions are dense in $L ^ { 2 } ( \mathbb { R } ^ { n } )$

4. Determine whether there is a nonzero smooth compactly supported function on R whose Fourier transform is also compactly supported?

5. This problem is about the integral

$$
I = \int _ { 0 } ^ { \infty } { \frac { \cos u d u } { u ^ { 4 } + 1 } } .
$$

(a) Show directly that I is a convergent improper Riemann integral.

(b) Is

$$
\int _ { [ 0 , \infty ) } { \frac { \cos u } { u ^ { 4 } + 1 } } d \mu ( u )
$$

a well-defined Lebesgue integral, where µ denotes the Lebesgue measure on R?

(c) (main part) Evaluate the integral in (a).

6. Determine the number of distinct solutions of the equation

$$
e ^ { z ^ { 2 } } = 5 z ^ { 5 }
$$

in the unit disk $\{ z \in \mathbb { C } : | z | \leq 1 \}$

7. Determine all entire functions $f \ ( \mathrm { i . e . } , f ( z )$ is holomorphic on the whole z-plane) that satisfy the inequality

$$
| f ( z ) | \leq | z | ^ { 2 } | \mathrm { I m } z | ^ { 2 }
$$

for |z| sufficiently large.

## Qualifying Exam - Analysis

May, 2013

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Problem 1 Let $U \subset \mathbb { C }$ be an open set and let f be a continuous function on U. If $f ^ { 2 }$ is holomorphic on $U _ { : }$ , prove that f is holomorphic on U .

Problem 2 Prove that there is only one solution in the unit disc $\{ z : | z | < 1 \}$ and there are three solutions on the annulus $\{ z : 1 < | z | < 2 \}$ (counting multiplicities) for the equation $z ^ { 4 } - 6 z + 3 = 0$

Problem 3 Let f be a holomorphic function on the unit disc $\{ z : | z | < 1 \}$ satisfying $f ( 0 ) = 0$ and $R e f ( z ) \leq A$ for some positive number $A > 0$ . Prove:

$$
| f ( z ) | \leq { \frac { 2 A | z | } { 1 - | z | } } .
$$

Problem 4 Calculate the following integral:

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { \frac { 1 } { 2 } } } { 4 + x ^ { 2 } } } d x .
$$

Problem 5 Suppose that E and F are Lebesgue measurable sets of R, and their Lebesgue measures $m ( E ) > 0 , m ( F ) > 0$ . Prove that

$$
E + F = \{ x + y : x \in E , y \in F \}
$$

contains a nonempty open interval.

Problem 6(a) Prove the Riemann-Lebesgue Lemma: if $f \in L ^ { 1 } ( \mathbb { R } ^ { d } )$ , then the Fourier transform of $f ,$

$$
\hat { f } ( \xi ) = \int _ { \mathbb { R } ^ { d } } f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x \to 0 , \ \mathrm { a s } \ | \xi | \to \infty .
$$

(b) Use part (a) to justify whether there exists a function $h \in L ^ { 1 } (  { \mathbb { R } } ^ { d } )$ such that

$$
f \ast h = f \mathrm { ~ f o r ~ a l l ~ } f \in L ^ { 1 } ( \mathbb R ^ { d } ) .
$$

Here $f * h$ is the convolution of f and h defined by

$$
( f * h ) ( x ) = \int _ { \mathbb { R } ^ { d } } f ( x - y ) h ( y ) d x .
$$

Problem 7 If the sequence of Lebesgue measurable functions $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ on $\mathbb { R } ^ { d }$ satisfying that

$$
\operatorname* { l i m } _ { n  \infty } \int _ { \mathbb { R } ^ { d } } | f _ { n } ( x ) | ^ { 2 } d x = 0 ,
$$

show that there exists a subsequence of functions $\{ f _ { n _ { j } } \} _ { j = 1 } ^ { \infty }$ such that

$$
f _ { n _ { j } } ( x ) \to 0 { \mathrm { ~ a . e . ~ } } x .
$$

Problem 8 Recall that the inner product on $L ^ { 2 } ( \mathbb { R } ^ { d } )$ is given by

$$
( f , g ) = \int _ { \mathbb { R } ^ { d } } f ( x ) { \overline { { g ( x ) } } } d x , { \mathrm { ~ f o r ~ } } f , g \in L ^ { 2 } ( \mathbb { R } ^ { d } ) ,
$$

which induces the $L ^ { 2 } .$ -norm

$$
\| f \| _ { L ^ { 2 } } = ( f , f ) ^ { 1 / 2 } .
$$

(a) If the sequence of functions $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ in $L ^ { 2 } ( \mathbb R ^ { d } )$ satisfy that $\| f _ { n } \| _ { L ^ { 2 } } = 1$ , show that there exists a subsequence of functions $\{ f _ { n _ { j } } \} _ { j = 1 } ^ { \infty }$ such that $f _ { n _ { j } }$ converges weakly to some function f in $L ^ { 2 } ( \mathbb R ^ { d } )$ , i.e.,

$$
( f _ { n _ { j } } , g ) \to ( f , g ) { \mathrm { ~ f o r ~ a l l ~ } } g \in L ^ { 2 } ( \mathbb { R } ^ { d } ) .
$$

(b) If $f _ { n }  f$ weakly in $L ^ { 2 } ( \mathbb R ^ { d } )$ and $\| f _ { n } \| _ { L ^ { 2 } } \to \| f \| _ { L ^ { 2 } }$ as n → ∞, show that $\| f _ { n } - f \| _ { L ^ { 2 } } \to 0$ as $n \to \infty$ .

# ANALYSIS QUALIFYING EXAM, FALL 2012

## Part I. Complex Analysis.

1. How many zeros does the polynomial

$$
z ^ { 9 } + z ^ { 6 } + 3 0 z ^ { 5 } - 3 z + 2
$$

have in the annulus $\{ 1 \leq | z | \leq 3 \}$ . Justify your answer.

2. Let $\textstyle f ( x ) = { \frac { 1 } { x ^ { 2 } + 1 } }$ . Use residues to compute the Fourier transform

$$
{ \widehat { f } } ( t ) = \int _ { - \infty } ^ { + \infty } f ( x ) e ^ { - i t x } d x ~ .
$$

3. Let $D = \{ z \in \mathbb { C } : | z | < 1 \}$ denote the unit disk.

What is the maximum possible value of $\left| f ^ { \prime } ( \frac { 1 } { 2 } ) \right|$ for a holomorphic function $f : D  D$ with $\begin{array} { r } { f ( \frac { 1 } { 2 } ) = \frac { 3 } { 4 } ? } \end{array}$ Find all such functions f that attain this maximum value.

4. Let $I = \{ t \in \mathbb { R } : 0 \leq t \leq 1 \} \subset \mathbb { C }$ . Suppose that $f : \mathbb { C } \to \mathbb { C }$ is a continuous function such that f is holomorphic on $\mathbb { C } \setminus I$ . Prove that f is an entire function $( \mathrm { i . e . , ~ } f$ is holomorphic on all of C).

## Part II. Real Analysis.

5. For each natural number n, let $f _ { n } : [ 0 , 1 ] \to \mathbb { R }$ be a sequence of absolutely integrable functions, and let $f : [ 0 , 1 ] \to$ R be another absolutely integrable function such that

$$
\int _ { 0 } ^ { 1 } { \big | } f _ { n } ( x ) - f ( x ) { \big | } d x \to 0 , \qquad { \mathrm { a s } } \quad n \to \infty .
$$

(a) Show that there exists a subsequence $f _ { n _ { j } }$ of $f _ { n }$ which converges to $f$ pointwise almost everywhere.

(b) Give a counterexample to show that the assertion fails if ”pointwise almost everywhere” is replaced by ”uniformly”.

6. For this problem, consider just Lebesgue measurable functions $f : [ 0 , 1 ] \to \mathbb { R }$ . together with the Lebesgue measure.

(a) State Fatou’s lemma (no proof required).

(b) State and prove the Dominated Convergence Theorem.

(c) Give an example where $f _ { n } ( x )  0 { \mathrm { ~ a . e . } }$ , but $\textstyle \int _ { - \infty } ^ { + \infty } f _ { n } ( x ) d x \to 1$

7. Let

$$
f \ast g ( x ) : = \int _ { - \infty } ^ { + \infty } f ( y ) g ( x - y ) d y
$$

denote the convolution of f and $g .$

(a) Let $f , g \in L ^ { 2 } ( \mathbb { R } )$ be two square-integrable functions on R (with the usual Lebesgue measure). Show that the convolution $f * g$ bounded continuous function on R.

(b) Instead let $h \in L ^ { 1 } ( \mathbb { R } )$ be fixed. Show that $A ( f ) = f * h$ is a bounded operator $L ^ { 1 } ( \mathbb { R } ) \to L ^ { 1 } ( \mathbb { R } )$

8. Let T be a linear transformation on $C _ { 0 } ( \mathbb { R } )$ , the space of continuous functions of compact support, that has the following two properties:

$$
\| T f \| _ { L ^ { \infty } } \leq \| f \| _ { L ^ { \infty } } , \qquad \mathrm { a n d } \qquad \left| \{ x \in \mathbb { R } : | T f ( x ) | > \lambda \} \right| \leq \frac { \| f \| _ { L ^ { 1 } } } { \lambda } .
$$

(Here $| A |$ denotes the Lebesgue measure of the set A.) Prove that

$$
\int _ { - \infty } ^ { + \infty } | T f ( x ) | ^ { 2 } d x \leq C \int _ { - \infty } ^ { + \infty } | f ( x ) | ^ { 2 } d x
$$

for all $f \in C _ { 0 } ( \mathbb { R } )$ and some fixed number $C$

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

## Time: 3 hours

## Part I. Complex Analysis

1. Use residues to calculate the integral $\textstyle \int _ { 0 } ^ { \infty } { \frac { 1 } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x$

2. Suppose f is holomorphic on the open unit disc $D ( 0 , 1 )$ and continuous on $\overline { { D ( 0 , 1 ) } }$ . Assume $| f ( \xi ) | < 1$ for $\xi \in \partial D ( 0 , 1 )$ . Show that there exists an unique point $a \in D ( 0 , 1 )$ such that $f ( a ) = a$

3. Suppose f is holomorphic on $U : = D ( 0 , 1 ) \setminus \{ 0 \}$ . Assume that the real part $\operatorname { R e } ( f )$ is bounded from below on U. Prove that $z = 0$ is a removable singularity.

4. Let $\begin{array} { r } { U = \left\{ z \in \mathbb { C } \mid \operatorname { I m } ( z ) \leq { \frac { \pi } { 2 } } \right\} } \end{array}$ and f be an entire function satisfying $f ( U ) \subset U , f ( - 1 ) = 0 , f ( 0 ) = \mathbf { \bar { 1 } }$ . Prove that $f ( z ) = z + 1$

## Part II. Real Analysis

5. Justify or give a counterexample to the following assertions:   
a. If $\{ f _ { i } \}$ is a sequence in $L ^ { 2 } ( [ 0 , 1 ] )$ converging weakly to f in $L ^ { 2 } ( [ 0 , 1 ] )$ then $f _ { i } ^ { 2 }$ converges weakly to $f ^ { 2 }$ in $L ^ { 1 } ( [ 0 , 1 ] )$ .   
b. If $\{ f _ { i } \}$ is a sequence in $L ^ { 2 } ( [ 0 , 1 ] )$ converging strongly to f in $L ^ { 2 } ( [ 0 , 1 ] )$ , then $f _ { i } ^ { 2 }$ converges strongly to $f ^ { 2 }$ in $L ^ { 1 } ( [ 0 , 1 ] )$ .

6. Let $\{ g _ { k } \} _ { k = 1 } ^ { \infty }$ be a sequence in $L ^ { 1 } ( \mathbb { R } ^ { n } )$ with $\sum \left| \left| g _ { k } \right| \right| _ { L ^ { 1 } ( \mathbb { R } ^ { n } ) } < \infty$

a. Show that $\textstyle \sum _ { k = 1 } ^ { \infty } g _ { k }$ converges a.e. to a function $g \in L ^ { 1 } ( \mathbb { R } ^ { n } )$

b. Show that lim $\begin{array} { r } { { \bf \Phi } _ { N  \infty } \vert \vert g - \sum _ { k = 1 } ^ { N } g _ { k } \vert \vert _ { L ^ { 1 } ( \mathbb { R } ^ { n } ) } = 0 . } \end{array}$

7. Let $f \in L ^ { 1 } ( \mathbb { R } )$ and set $\begin{array} { r } { h ( x ) = \int _ { [ x , x + 1 ] } f ( t ) \ d t } \end{array}$

a. Show that $h ( x )$ is absolutely continuous.

b. Show that $\scriptstyle \operatorname* { l i m } _ { x \to \infty } h ( x ) = 0$

8. Let $f \in L ^ { 1 } ( \mathbb { R } )$ . Define its Fourier transform $\begin{array} { r } { \hat { f } ( \xi ) = \int f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x } \end{array}$ Show that $\hat { f } ( \xi ) \in C _ { 0 } ( \mathbb { R } )$ , that is the Fourier transform is continuous and vanishes at infinity. You may not quote the Riemann-Lebesgue lemma without sketching a proof.

# ANALYSIS QUALIFYING EXAM SEPTEMBER 2011

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Time: 3 hours.

Part I. Complex Analysis.

Notation: $D = \{ z \in \mathbb { C } : | z | < 1 \}$

1. Determine the value of the integral

$$
\int _ { \gamma } \frac { d z } { z ^ { 3 } \cos z } ,
$$

where $\gamma$ is the circle $\{ | z - 1 | < 2 \}$ traversed counterclockwise.

2. Let $h : \mathbb { C } \to \mathbb { R }$ be a harmonic function such that h is bounded below. Prove that h is constant.

3. Let f be a holomorphic function on $D \setminus \{ 0 \}$ . Suppose that there exists a positive integer n such that $f ^ { - 1 } ( w )$ contains at most n points for all $w \in \mathbb { C }$ . Prove that 0 is a removable singularity or pole.

4. Suppose that U is a simply connected bounded domain in $\mathbb { C } .$ and let $P \in U$ . Prove that for all $t \in \mathbb { R }$ , there exists a unique holomorphic function $f : U \to U$ such that $f ( P ) = P$ and $f ^ { \prime } ( P ) = e ^ { i t }$

## Part II. Real Analysis.

Notation: |A| denotes the Lebesgue measure of a measurable set $A \subset \mathbb { R } ^ { n }$

5. Give an example of a sequence of functions $\{ f _ { j } \}$ satisfying $\| f _ { j } \| _ { L ^ { 2 } ( \mathbb { R } ) } = 1$ for which $\{ f _ { j } \}$ has no convergent subsequence in $L ^ { 2 } ( \mathbb { R } )$ .

6. a) Let $f _ { j } \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ and suppose that

$$
\int _ { \mathbb { R } ^ { n } } | f _ { j } ( x ) - f ( x ) | ^ { 2 } d x \to 0 .
$$

If $\Omega \subset \mathbb { R } ^ { n }$ has finite Lebesgue measure, i.e., $| \Omega | < \infty$ , show that the Fourier transforms satisfy

$$
\int _ { \Omega } { \widehat { f } } _ { j } ( \xi ) d \xi \to \int _ { \Omega } { \widehat { f } } ( \xi ) d \xi .\tag{1}
$$

b) If $| \Omega | = \infty$ , is (1) still always valid? Give a proof or counterexample.

7. Let $\omega ( \alpha ) = | \{ x : | f ( x ) | > \alpha \} | , \alpha > 0$ , be the distribution function of a given $f \in$ $L ^ { p } ( \mathbb { R } ^ { n } )$ , where $p > 0$ Does $\alpha ^ { p } \omega ( \alpha )$ tend to a limit as $\alpha  0 + ?$ Give a proof or counterexample.

8. Show that there does not exist a function $I \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ such that

$$
f * I = f \qquad { \mathrm { f o r ~ a l l ~ } } f \in L ^ { 1 } ( \mathbb { R } ^ { n } ) .
$$

(Here $\begin{array} { r } { ( f * I ) ( x ) = \int f ( y ) I ( x - y ) } \end{array}$ dy is the convolution of f and I.)

# ANALYSIS QUALIFYING EXAM MAY 2011

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Time: 3 hours.

Part I. Complex Analysis.

Notation: $D = \{ z \in \mathbb { C } : | z | < 1 \}$

1. Find all entire functions f such that $| f ( z ) | = 1$ whenever $| z | = 1$ . Give explicit formulas for the functions and give a proof for your answer. (An entire function is a holomorphic function on C.)

2. Let $f : D \to \mathbb { C }$ be a holomorphic function with simple zeros at the points $1 / 3 , 2 / 3 , i / 4$ and no other zeros. Determine the value of the integral

$$
\int _ { \{ | z | = 1 / 2 \} } ( z ^ { 2 } - 1 ) e ^ { z } { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z ,
$$

where the direction of integration is counterclockwise.

3. Let U be a bounded domain in C, and let $f : U \to U$ such that f is holomorphic. Let $P \in U$ and suppose that $f ( P ) = P$ . Prove that $| f ^ { \prime } ( P ) | \leq 1$

Hint: Consider the sequence of iterates $f _ { n } = f \circ f \circ \cdot \cdot \cdot \circ f \ ( n { \mathrm { ~ t i m e s } } )$

4. Suppose that $u : \mathbb { C } \to \mathbb { R }$ is a harmonic function such that

$$
u ( z ) \leq 1 0 \log ( | z | + 2 ) ,
$$

for all $z \in \mathbb { C }$ . Prove that u is constant.## Part II. Real Analysis.

5. Let $f _ { n } : [ 0 , 1 ] \to \mathbb { R }$ , for $n = 1 , 2 , \ldots ,$ , be a sequence of $\mathcal { C } ^ { 1 }$ functions such that $f _ { n } ( t ) \leq 5$ and $| f _ { n } ^ { \prime } ( t ) | \leq 1$ for all $n , t$ . Define the functions $g _ { n } : [ 0 , 1 ] \to \mathbb { R }$ by

$$
g _ { n } ( t ) = \operatorname* { m a x } \{ f _ { 1 } ( t ) , \ldots , f _ { n } ( t ) \}
$$

for $n = 1 , 2 , \dots$ . Prove that the sequence $\left\{ g _ { n } \right\}$ converges uniformly on [0, 1].

6. Let $f \in L ^ { 1 } ( S ^ { 1 } )$ such that ${ \widehat { f } } \in \ell ^ { 1 } ( \mathbb { Z } )$ . Prove that $f \in { \mathcal { C } } ( S ^ { 1 } )$ (continuous functions on the circle S1).

7. Suppose that $f \in L ^ { \infty } ( [ 0 , 1 ] )$

a) Prove that if 1 $< p < \infty$ then $\| f \| _ { p } \leq \| f \| _ { \infty }$

b) Show that $\begin{array} { r } { \| f \| _ { \infty } \leq \operatorname* { l i m } _ { p \longrightarrow \infty } \| f \| _ { p } } \end{array}$ and therefore conclude that $\begin{array} { r } { \operatorname* { l i m } _ { p \to \infty } \| f \| _ { p } = \| f \| _ { \infty } } \end{array}$ Hint: Given $\varepsilon > 0$ , consider $A _ { \varepsilon } = \{ x \in [ 0 , 1 ] : | f ( x ) | > \| f \| _ { \infty } - \varepsilon \}$

8. a) Let $f _ { j } : \mathbb { R } ^ { n } \longrightarrow \mathbb { R }$ , for $j = 1 , 2 , \dots$ , be a sequence of $L ^ { 2 }$ functions. Suppose that there is a function $f \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ such that

$$
\int _ { \mathbb { R } ^ { n } } f _ { j } g \to \int _ { \mathbb { R } ^ { n } } f g , \quad \forall g \in L ^ { 2 } ( \mathbb { R } ^ { n } ) .
$$

Show that

$$
\| f \| _ { 2 } \leq \operatorname* { l i m } _ { j \to \infty } \| f _ { j } \| _ { 2 } .
$$

Also, give an example showing that strict inequality can occur.

b) Suppose also that $\| f _ { j } \| _ { 2 } \to \| f \| _ { 2 }$ . Show that in this case $\| f _ { j } - f \| _ { 2 } \to 0 { \mathrm { ~ a s ~ } } j \to \infty .$

Instructions: Do all eight problems. Each problem will be scored out of 10 points.

1. Suppose that $f _ { j } \in L ^ { 2 } ( \mathbb { R } ^ { n } ) , j = 1 , 2 , 3 , . .$ . and that $f _ { j } \to f$ in $L ^ { 2 }$ . Suppose further that there is a constant $M < \infty$ so that

$$
\int e ^ { 1 0 0 | x | ^ { 2 } } | f _ { j } ( x ) | ^ { 2 } d x \leq M , \quad j = 1 , 2 , 3 , \ldots .
$$

Is it true that $\begin{array} { r } { \int e ^ { 9 9 | x | ^ { 2 } } | f ( x ) | ^ { 2 } d x < \infty ? } \end{array}$ Give a proof or counterexample.

2. Let $E , F \subset \mathbb { R }$ be two Lebesgue-measurable subsets of R, each of finite measure, and let $\chi _ { E }$ and $\chi _ { F }$ denote their respective characteristic functions.

(a) Prove that the convolution $\chi _ { E } * \chi _ { F }$ defined by

$$
\chi _ { E } * \chi _ { F } ( x ) = \int _ { \mathbb { R } } \chi _ { E } ( y ) \chi _ { F } ( x - y ) d y
$$

is a continuous function of $x .$

(b) Show that as $n \to \infty$

$$
n \big ( \chi _ { E } * \chi _ { [ 0 , 1 / n ] } \big ) \longrightarrow \chi _ { E }
$$

pointwise almost everywhere.

3. Let $\begin{array} { r } { T f ( x ) = \int _ { \mathbb { R } ^ { n } } K ( x , y ) f ( y ) d y } \end{array}$ , where $K ( x , y )$ is a nonnegative measurable function on $\mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ . Suppose that there are measurable functions $p ( x ) > 0$ and $q ( x ) > 0$ o n $\mathbb { R } ^ { n }$ and real numbers $\alpha , \beta > 0$ for which

$$
\int K ( x , y ) q ( y ) d y \leq \alpha p ( x ) ,
$$

for almost all x and

$$
\int p ( x ) K ( x , y ) d x \leq \beta q ( y )
$$

for almost all y. Show that for $f \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ we have

$$
\| T f \| _ { L ^ { 2 } } \leq \sqrt { \alpha \beta } \| f \| _ { L ^ { 2 } } .
$$

(This is called Schur’s test.)

4. Define $U : L ^ { 2 } ( \mathbb { R } ) \to L ^ { 2 } ( \mathbb { R } )$ by

$$
U f ( x ) = f ( x - 1 ) .
$$

Show that if $f \in L ^ { 2 }$ satisfies $U f = \lambda f$ , for some $\lambda \in \mathbb { R } \ ( \mathrm { i . e . , } \ f$ is an eigenvector of U ) then f must be the zero element, i.e., $f = 0$ almost everywhere.

[cont’d on other side]

5. Let $\gamma$ be the closed curve in the complex plane that is given in polar coordinates by $r = 2 + 3$ cos θ, $0 \leq \theta \leq 4 \pi$ , oriented in the direction of increasing θ. Let

$$
f ( z ) = \frac { e ^ { z } } { 2 z - 1 } + \frac { \sin ( 2 z ) } { ( z - 2 ) ^ { 2 } } + \frac { \cos ( 5 z ) } { ( z + 5 i ) ^ { 3 } } .
$$

Calculate $\int _ { \gamma } f ( z ) d z$

[Recall that in polar coordinates, $( - r , \theta )$ and $( r , \theta + \pi )$ give the same point in the plane.]

6. Let D denote the open unit disc in C. Let $f : D  \mathbb { C }$ be a $C ^ { 1 }$ function, and consider the property: $f$ has a double zero at $\textstyle z = { \frac { 1 } { n } }$ for all natural numbers n.

(a) Determine all holomorphic functions f with this property. [The terms “holomorphic” and “complex analytic” have the same meaning.]

(b) Give an example of a non-holomorphic $C ^ { 1 }$ function with this property. (You must explain why your example has this property.)

7. Determine all entire functions $f \ ( \mathrm { i . e . } , \ f ( z )$ is holomorphic and is defined for all $z \in \mathbb { C } )$ that satisfy the inequality:

$$
| f ( z ) | \leq | \mathrm { R e } z | ^ { 2 } + | z | ^ { \frac { 3 } { 2 } } \quad \mathrm { w h e n e v e r ~ } | z | > 1 .
$$

8. Let D denote the open unit disc, as in $\# 6$ . Let $g : D  D$ be a surjective holomorphic mapping for which $g ( 0 ) = 0$ . Suppose that $z = g ( w )$ gives a two-sheeted branched covering of the image with exactly one branch point at $w = 0$ . An example of such a function g is $g ( w ) = \bar { w ^ { 2 } }$

(a) Express the given conditions explicitly in terms of $g$ and its derivatives.

(b) Show that $| g ( w ) | \leq | w | ^ { 2 }$ for all $| w | < 1$

(c) Suppose that $g ( 1 / 2 ) = i / 4$ . What is the strongest statement about $g ( w )$ that follows from the assertion in (b)? Explain.

# ANALYSIS QUALIFYING EXAM MAY 2010

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Time: 3 hours.

## Part I. Complex Analysis.

1. Let f be a holomorphic function on the punctured disk

$$
U : = \left\{ z \in \mathbb { C } : 0 < | z | < 1 \right\} .
$$

Suppose that $| f ( z ) | \leq | z | ^ { - 1 / 2 }$ for all $z \in U$ . Prove that f has a removable singularity at 0.

2. Find all possible values of

$$
\int _ { \gamma } { \frac { e ^ { \pi z } } { ( z - 1 ) ( z - i ) ^ { 2 } } } d z
$$

where γ ranges over all simple closed smooth curves contained in $\mathbb { C } \setminus \{ 1 , i \}$ . (A simple closed curve is a closed curve that does not intersect itself; i.e., it is a homeomorphic image of the circle.)

You do not need to give a proof for your answer to this problem, but show all your work.

3. Let $\mathcal { O } ( D )$ denote the space of holomorphic functions on the unit disk D and let

$$
{ \mathcal H } = { \mathcal O } ( D ) \cap L ^ { 2 } ( D ) = \left\{ f \in { \mathcal O } ( D ) : \int _ { D } | f | ^ { 2 } d x d y < + \infty \right\} .
$$

a) Show that for all compact sets $K \subset D$ , there is a constant $C _ { K } \in \mathbb { R } ^ { + }$ such that

$$
\operatorname* { s u p } _ { z \in K } | f ( z ) | \leq C _ { K } \| f \| _ { L ^ { 2 } ( D ) } .
$$

b) Show that H is a closed subspace of $L ^ { 2 } ( D )$ and hence is a Hilbert space.

4. Let h be a harmonic function on the domain

$$
U : = \left\{ z \in \mathbb { C } : | z | > 1 \right\} .
$$

Show that there exists a constant $c \in \mathbb { R }$ and a holomorphic function $f$ on $U$ such that $\mathrm { R e } f ( z ) = h ( z ) + c \log | z |$ for all $z \in U$

5. Let $f _ { j } \in L ^ { 2 } ( \mathbb { R } ^ { n } )$ , and ${ \widehat { f } } _ { j }$ denote its Fourier transform for $j = 1 , 2 , 3 \ldots$ . Suppose that $f _ { j } \to f$ in $L ^ { 2 }$ and that there is a finite constant M so that

$$
\| f _ { j } \| _ { H ^ { \sigma } } \leq M , \quad j = 1 , 2 , 3 , \ldots ,
$$

for some $\sigma \in \mathbb { R }$ , where $\begin{array} { r } { \| g \| _ { H ^ { \sigma } } = \left( \int _ { \mathbb { R } ^ { n } } ( 1 + | \xi | ^ { 2 } ) ^ { \sigma } | \widehat { g } ( \xi ) | ^ { 2 } d \xi \right) ^ { 1 / 2 } } \end{array}$ denotes the $H ^ { \sigma }$ Sobolev norm of g. Is it necessarily true that $\| f \| _ { H ^ { \sigma } } < \infty ?$ Give a proof or counterexample.

6. Let $\varphi : \mathbb { R }  \mathbb { R }$ be a continuous function with compact support.

a) Prove that if $1 \leq p \leq q \leq \infty$ are fixed then there is a constant A such that

$$
\| f * \varphi \| _ { L ^ { q } } \leq A \| f \| _ { L ^ { p } } , \quad { \mathrm { f o r ~ a l l } } \quad f \in L ^ { p } .
$$

If you use Young’s (convolution) inequality, you should prove it.

b) Show by example that such a general inequality cannot hold for $p > q$

## 7. Suppose that

$$
f : [ 0 , 1 ] \times [ 0 , 1 ] \to \mathbb { R }
$$

is continuous and has the property that for each x the map $t \to f ( x , t )$ is differentiable and that $\begin{array} { r } { \left| \frac { \partial f } { \partial t } ( x , t ) \right| \le g ( x ) } \end{array}$ for some measurable function statisfying $\textstyle \int _ { 0 } ^ { 1 } g ( x ) d x < \infty$ Carefully prove that $\textstyle F ( t ) = \int _ { 0 } ^ { 1 } f ( x , t )$ dx satisfies

$$
F ^ { \prime } ( t ) = \int _ { 0 } ^ { 1 } { \frac { \partial f } { \partial t } } ( x , t ) d x .
$$

## 8. Let E be a measurable subset of the line.

a) Let $\chi _ { E } : \mathbb { R } \to \mathbb { R }$ be the characteristic function of $E ~ ( \mathrm { i . e . } ~ \chi _ { E } ( x ) = 1$ when $x \in E$ and $\chi _ { E } ( x ) = 0$ when $x \notin E )$ . If E has finite Lebesgue measure, show that the function $f : \mathbb { R } \to \mathbb { R }$ defined by

$$
f ( x ) = \int _ { \mathbb { R } } \chi _ { E } ( y ) \chi _ { E } ( y - x ) d y
$$

is continuous.

b) Suppose instead that E has positive Lebesgue measure $0 < | E | \le \infty$ . Using a), show that the set $E - E = \{ x - y : x , y \in E \}$ contains an open interval $( - \varepsilon , \varepsilon )$ for some $\varepsilon > 0$

# ANALYSIS QUALIFYING EXAM SEPTEMBER 2009

All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Time: 3 hours.

Part I. Real Analysis. Do 3 out of the following 4 problems.

1. Suppose $f _ { n }$ is a sequence of continuous functions on [0, 1] which converges to a continuous function $f$ on [0, 1]. Does it follow that $f _ { n }$ converge uniformly? Give a proof or provide a counterexample.

2. For which values of $\sigma \in \mathbb { R }$ does there exist a constant $C _ { \sigma } < + \infty$ such that

$$
\left| \sum _ { j , k = 1 } ^ { \infty } ( 1 + | j - k | ) ^ { \sigma } a _ { j } b _ { k } \right| \leq C _ { \sigma } ( \sum _ { j = 1 } ^ { \infty } | a _ { j } | ^ { 2 } ) ^ { 1 / 2 } ( \sum _ { k = 1 } ^ { \infty } | b _ { k } | ^ { 2 } ) ^ { 1 / 2 }
$$

Prove your assertion.

3. Let I be the unit interval [0, 1], and for $n = 1 , 2 , 3 , . . .$ . and $0 \leq j \leq 2 ^ { n } - 1$ let

$$
I _ { n , j } = [ j 2 ^ { - n } , ( j + 1 ) 2 ^ { - n } ] .
$$

For $f \ \in \ L ^ { 1 } ( I , d x )$ define $\begin{array} { r } { E _ { n } f ( x ) \ = \ \sum _ { j = 0 } ^ { 2 ^ { n } - 1 } ( 2 ^ { n } \int _ { I _ { n , j } } f d t ) \chi _ { I _ { n , j } } ( x ) } \end{array}$ , where $\chi _ { I _ { n , j } }$ is the characteristic function of $I _ { n , j }$ . Prove that if $f \in L ^ { 1 } ( \bar { I } , d x )$ then lim $\mathfrak { l } _ { n \to \infty } E _ { n } f ( x ) = f ( x )$ almost everywhere in I.

4. Let $f ( x )$ be a non-decreasing function on [0, 1]. You may assume that f is differentiable almost everywhere. Prove that

$$
\int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) d x \leq f ( 1 ) - f ( 0 ) .
$$

## Part II. Complex Analysis. Do 3 out of the following 4 problems.

5. Let

$$
f ( x + i y ) = x ^ { 3 } - 3 x y ^ { 2 } + i y ^ { 3 } .
$$

State whether each of the following is true or false and give proofs for your answers:

a) the complex derivative $f ^ { \prime } ( 0 )$ exists;

b) f is holomorphic in a neighborhood of 0.

6. Let

$$
f ( z ) = { \frac { z } { \tan z } } \qquad { \mathrm { f o r } } ~ z \neq 0 .
$$

a) Prove that f has a removable singularity at 0.

b) What is the radius of convergence of the power series for f centered at 0? Justify your answer.

7. Let $f : H  D$ be a holomorphic map from the upper half plane

$H = \left\{ z \in \mathbb { C } : \operatorname { I m } z > 0 \right\}$ to the unit disk $D = \{ z \in \mathbb { C } : | z | < 1 \}$

Suppose that $f ( i ) = 1 / 2$ . Determine the maximal possible value of $| f ^ { \prime } ( i ) |$

8. Let h be a harmonic function on the punctured disk

$$
U : = \left\{ z \in \mathbb { C } : 0 < | z | < 1 \right\} .
$$

Show that there exists a constant $c \in \mathbb { R }$ and a holomorphic function f on U such that $\mathrm { R e } f ( z ) = h ( z ) + c \log | z |$ for all $z \in U$

# ANALYSIS QUALIFYING EXAM MAY 2009

Do all 8 problems. All problems are equally weighted. Show all your work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

## Time: 3 hours.

1. Find all meromorphic functions f on C such that

$$
| f ( z ) | \leq { \frac { \log ( 2 + | z | ^ { 2 } ) } { | z | } } \qquad { \mathrm { f o r ~ a l l ~ } } z \neq 0 .
$$

Give explicit formulas for the functions and give a proof for your answer.

2. How many solutions does the equation

$$
z + e ^ { - z } = 2 + i
$$

have in the half-plane Re $z > 0 ?$ Prove that your answer is correct.

3. Let $f _ { n } : U \to \mathbb { C } , n = 1 , 2 , 3 , . . . ,$ be a sequence of holomorphic functions such that $f _ { n } ^ { - 1 } ( 0 ) = \{ c _ { n } \}$ , where $c _ { n } \in U$ , and U is a connected open set. Suppose that $f _ { n }  f _ { 0 }$ uniformly, where $f _ { 0 }$ is not constant.

a) Prove that $f _ { 0 }$ has at most one zero in $U$

b) Can $f _ { 0 }$ have no zeros? If so, give a necessary and sufficient condition on the $c _ { n }$ for this to happen.

4. Let $f ( x ) = { \frac { 1 } { x ^ { 2 } + 1 } }$ . Use a contour integral consisting of the interval $[ - R , R ] \subset \mathbb { R }$ and a semicircle of radius R to compute the Fourier transform

$$
{ \widehat { f } } ( 1 ) = \int _ { \mathbb { R } } f ( x ) e ^ { - i x } d x ~ .
$$

Show that the contour integral converges to your answer as $R \to + \infty$

5. Let $f , g \in L ^ { 2 } ( \mathbb { R } )$ be two square-integrable functions on R (with the usual Lebesgue measure). Show that the convolution

$$
f * g ( x ) = \int _ { \mathbb { R } } f ( y ) g ( x - y ) d y
$$

of $f$ and g is a bounded continuous function on $\mathbb { R } .$

6. Let $\mathbb { R } / \mathbb { Z }$ be the unit circle with the usual Lebesgue measure. For each $n = 1 , 2 , 3 , . . .$ let $K _ { n } : \mathbb { R } / \mathbb { Z } \to \mathbb { R } _ { + }$ be a nonnegative integrable function such that $\begin{array} { r } { \int _ { \mathbb { R } / \mathbb { Z } } K _ { n } ( t ) d t = 1 } \end{array}$ and lim $\begin{array} { r } { { \bf \delta } _ { \cdot n \longrightarrow \infty } \int _ { \varepsilon \le | t | \le 1 / 2 } K _ { n } ( t ) d t = 0 } \end{array}$ for every $0 < \varepsilon < 1 / 2$ , where we identify R $/ \mathbb { Z }$ with $( - 1 / 2 , 1 / 2 ]$ in the usual way. (Such a sequence of $K _ { n }$ are called approximations to the identity.) Let $f : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$ be continuous, and define the convolutions $f * K _ { n } : \mathbb { R } / \mathbb { Z } \to$ R by

$$
f * K _ { n } ( x ) = \int _ { \mathbb { R } / \mathbb { Z } } f ( x - t ) K _ { n } ( t ) d t .
$$

Show that $f * K _ { n }$ converges uniformly to $f$ .

7. Fix $1 \leq p < \infty$ and let $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of Lebesgue measurable functions $f _ { n } : [ 0 , 1 ] \to \mathbb { C }$ . Suppose there exists $f \in L ^ { p } ( [ 0 , 1 ] )$ such that $f _ { n }  f$ in $L ^ { p }$ , that is,

$$
\int _ { [ 0 , 1 ] } | f _ { n } ( x ) - f ( x ) | ^ { p } d x \to 0 .
$$

a) Show that $f _ { n } \to f$ in measure, that is,

$$
\operatorname* { l i m } _ { n \to \infty } \mu ( \{ x \in [ 0 , 1 ] : | f _ { n } ( x ) - f ( x ) | \geq \varepsilon \} ) = 0
$$

for all $\varepsilon > 0$ . (Here $\mu = \mathrm { L e b e s g u e }$ measure.)

b) Show that there is a subsequence $f _ { n _ { k } }$ such that $f _ { n _ { k } } ( x )  f ( x )$ almost everywhere.

8. Consider [0, 1] with Lebesgue measure. Let $f \in L ^ { \infty } ( [ 0 , 1 ] )$ and define

$$
a _ { n } = \int _ { [ 0 , 1 ] } | f | ^ { n } d x .
$$

Show that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n + 1 } } { a _ { n } } } = \| f \| _ { \infty } .
$$

# PROBLEMS FOR ANALYSIS QUALIFYING EXAM Fall 2008

Do all seven problems. Show all work and state any theorems you are using.   
Time: 3 hours.

1) (15 points) Consider the mapping $F : [ 0 , 1 ]  [ 0 , 1 ]$ given by $F ( s ) = s ^ { 2 }$

Let $F ^ { - j } ( A )$ be the inverse image of j iterates of F applied to a measurable subset $A \subset [ 0 , 1 ]$ . That is, if $F = F ^ { 1 }$ and $F ^ { j } , j = 2 , 3 , . .$ . is defined inductively as $F ^ { j } = F ^ { j - 1 } \circ F$ ， then $F ^ { - j } ( A ) = \{ x : F ^ { j } x = y$ , some $y \in A \}$

a) Given $N = 1 , 2 , \dots$ show that $\begin{array} { r } { \mu _ { N } ( A ) = N ^ { - 1 } \sum _ { j < N } | F ^ { - j } ( A ) | } \end{array}$ is a measure which is absolutely continuous with respect to Lebesgue measure. Here |B| denotes the Lebesgue measure of a measurable set.

b) Show that $\mu _ { N } ( [ a , b ] ) \to 0 { \mathrm { ~ i f ~ } } 0 < a < b \leq 1$

c) If f is a continuous function on [0, 1] does lim $\begin{array} { r } { \int _ { [ 0 , 1 ] } f ( s ) d \mu _ { N } ( s ) } \end{array}$ tend to a limit? If so, what is the limit?

2) (10 points) Let $( X , { \mathcal { M } } , \mu )$ and $( Y , \mathcal { N } , \nu )$ be σ-finite measure spaces and let $K ( x , y )$ be a measurable function with respect to the product σ-algebra $\mathcal { M } \times \mathcal { N }$ . Assume that there is a constant $0 < A <$ ∞ so that for all $x \in X$

$$
\int _ { Y } | K ( x , y ) | d \nu ( y ) \leq A ,
$$

and for all $y \in Y$

$$
\int _ { X } | K ( x , y ) | d \mu ( x ) \leq A .
$$

Let $1 \leq p \leq \infty$ and for $f \in L ^ { p } ( X , \mathcal { M } , \mu )$ define

$$
T f ( y ) = \int _ { X } f ( x ) K ( x , y ) d \mu ( x ) .
$$

Prove that

$$
\| T F \| _ { L ^ { p } ( \nu ) } \leq A \| f \| _ { L ^ { p } ( \mu ) } .
$$

3) (10 points) Is the Banach space $\ell ^ { \infty }$ of bounded complex sequences $a = \{ a _ { n } \} _ { n = 1 } ^ { \infty }$ with the supremum norm $\left\| a \right\| _ { \infty } = \operatorname* { s u p } _ { n } \left| a _ { n } \right|$ separable? Prove your assertion.

4) (10 points) Use residues to verify that

$$
\int _ { 0 } ^ { \infty } \frac { \ln x } { ( x ^ { 2 } + 4 ) ^ { 2 } } d x = \frac { \pi } { 3 2 } ( \ln 2 - 1 ) .
$$

5) (10 points) How many solutions does the equation

$$
e ^ { z } = 3 z ^ { 7 }
$$

have in the unit disk $D = \{ x \in \mathbb { C } : | z | < 1 \} ?$ Justify your answer.

6) (10 points) Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function. Prove that if there exists some real number C and some positive integer k so that

$$
| f ( z ) | \leq C | z | ^ { k }
$$

for all z with $| z | > 1$ , then f is a polynomial in z of degree at most $k .$

7) (10 points) Let $D \subset \mathbb { C }$ be the unit disk and $\Omega \subset \mathbb { C }$ a bounded, simply connected domain. If $f _ { 1 } : D \to \Omega$ and $f _ { 2 } : D \to \Omega$ are holomorphic bijections so that $f _ { 1 } ( 0 ) = f _ { 2 } ( 0 )$ ， then how are $f _ { 1 }$ and $f _ { 2 }$ related to each other?

# PROBLEMS FOR ANALYSIS QUALIFYING EXAM SPRING 2008

Do all eight problems. Show all work and state any theorems you are using. Time: 3 hours.

1) Let $E , F$ be two Lebesgue measurable subsets of R of finite measure, and let $\chi _ { E } , \chi _ { F }$ be their respective characteristic functions.

a) Show that the convolution $\chi _ { E } * \chi _ { F }$ defined by

$$
\chi _ { E } * \chi _ { F } ( x ) = \int _ { \mathbb { R } } \chi _ { E } ( y ) \chi _ { F } ( x - y ) d y
$$

is a continuous function.

b) Show that

$$
n \big ( \chi _ { E } * \chi _ { [ 0 , 1 / n ] } \big ) \to \chi _ { E }
$$

as $n \to \infty$ pointwise almost everywhere.

2) Consider $L ^ { \infty } ( [ 0 , 1 ] )$

a) If f belongs to this space prove that

$$
\operatorname* { l i m } _ { p \to \infty } \left( \int _ { 0 } ^ { 1 } | f | ^ { p } d x \right) ^ { 1 / p } = \| f \| _ { \infty } .
$$

b) Give an example showing that this is false if we replace $L ^ { \infty } ( [ 0 , 1 ] )$ by $L ^ { \infty } ( \mathbb { R } )$

3) Assume that $f$ is a continuously differentiable 2π periodic function on R. Show that the Fourier series

$$
\sum _ { n = - \infty } ^ { \infty } \hat { f } ( n ) e ^ { i n t }
$$

is absolutely convergent for every t (here $\begin{array} { r } { { \hat { f } } ( n ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( t ) e ^ { - i n t } d t ) } \end{array}$

4) Let $\ell ^ { 2 }$ be the space of all square-summable sequences of complex numbers, and let $T : \ell ^ { 2 } \to \ell ^ { 2 }$ be a linear operator. Let $e _ { n }$ be the sequence

$$
e _ { n } = ( 0 0 \cdot \cdot \cdot 0 1 0 \cdot \cdot \cdot ) ,
$$

where 1 is in the n-th position. Let $\boldsymbol { a } _ { m n } = \langle T \boldsymbol { e } _ { m } , \boldsymbol { e } _ { n } \rangle$ be the “matrix coefficients” of T .

a) Assume that $\begin{array} { r } { \sum _ { n , m = 1 } ^ { \infty } | a _ { m n } | ^ { 2 } < \infty } \end{array}$ . Show that T is a bounded operator on $\ell ^ { 2 }$

b) Assume instead that sup $\left\{ \left| a _ { m n } \right| : 1 \leq n , m < \infty \right\}$ is finite. Must T be bounded? Explain.

5) Prove the following statement: If f and g are entire functions, $g ( z ) \neq 0$ and $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbf { C } .$ , then $f ( z ) = C g ( z )$ for some constant C.

6) Let $D = \{ z \in \mathbf { C } : | z | < 1 \}$ and P and Q be distinct points in D. Prove the following statement: If f and g are conformal (or equivalently biholomorphic) self-maps of D, $f ( P ) = g ( P )$ and $f ( Q ) = g ( Q )$ , then $f \equiv g$

7) Let $U \subset \mathbf { C }$ be an open set, $P \in U$ and f a holomorphic function defined on U so that $f ( P ) = f ^ { \prime } ( P ) = 0$ . Use the Argument Principle to prove the following statement: There exists $\delta > 0$ so that if $0 < | Q | < \delta ,$ , then $f ^ { - 1 } ( Q )$ contains at least two points.

8) Let $U \subset \mathbf { C }$ be an open set and $P \in U$ . Let F be a family of holomorphic functions from U into the unit disc $D = \{ z \in \mathbf { C } : | z | < 1 \}$ that take P to 0.

(a) Show that sup $\{ | f ^ { \prime } ( P ) | : f \in { \mathcal { F } } \} < \infty$

(b) Show that there exists a sequence $\{ f _ { n } \} \subset \mathcal { F }$ and a holomorphic function $f _ { 0 } : U \to D$ so that $\left\{ f _ { n } \right\}$ converges uniformly to $f _ { 0 }$ on every compact subset of U and $f _ { 0 } ^ { \prime } ( P ) = \operatorname* { s u p } \{ | f ^ { \prime } ( P ) | : f \in \mathcal { F } \}$ .

# ANALYSIS QUALIFYING EXAM FALL 2007

(1) Is the function

$$
f ( x , y ) = x ^ { 3 } + 3 x y ^ { 2 } - 3 x ^ { 2 } y - 1 0 + i ( y ^ { 3 } + 3 x ^ { 2 } y - 3 y ^ { 2 } x + 5 )
$$

complex analytic? Prove that your answer is correct.

(2) Find all entire analytic functions satisfying $| f ( z ) | \leq | e ^ { z } |$ for all $z \in \mathbb { C }$

(3) Let A be the annulus $A = \left\{ z \in \mathbb { C } : 1 < | z | < 2 \right\}$ Let f be a non-constant holomorphic function in a neighborhood of A, and suppose that $| f ( z ) | = 1$ on ∂A (the boundary of A). Prove that f has at least 2 zeros in A.

(4) Use the residue calculus to compute $\int _ { 0 } ^ { \infty } { \frac { d x } { 1 + x ^ { n } } }$

(5) Give examples of functions f and g on R so that $f \in L ^ { 1 } \setminus L ^ { 2 }$ and $g \in L ^ { 2 } \setminus L ^ { 1 }$

(6) Does there exist an open dense subset of R with Lebesgue measure equal to one? Either construct an example or prove that one does not exist.

(7) Let $f _ { n }$ be a sequence of measurable real-valued functions on [0, 1] with

$$
\sum _ { n = 1 } ^ { \infty } \left( \int _ { 0 } ^ { 1 } | f _ { n } | \right) \leq 1 .
$$

Prove that $f _ { n }$ converges to zero almost everywhere.

(8) Suppose that f and g are R $L ^ { 1 } ( \mathbb { R } )$ functions with compact support and let h be the convolution $\begin{array} { r } { f \star g \ ( \mathrm { i . e . , \ } h ( x ) = \int f ( x - y ) g ( y ) d y ) } \end{array}$ . Prove that h is uniformly continuous.# PROBLEMS FOR ANALYSIS QUALIFYING EXAM SPRING 2007

(1） How many zeros does the polynomial $z ^ { 6 } - 2 z ^ { 5 } + 7 z ^ { 4 } + z ^ { 3 } - z + 1$ have in the open unit disc $D = \{ z : | z | < 1 \} ?$

(2） Calculate the integral $\textstyle \int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 a \cos \theta + a ^ { 2 } } }$ ，where $0 < a < 1$

(3) Let $f : D  D$ be a holomorphic map of the unit disc with $f ( 0 ) = 0$ ，and suppose that $f$ is not a rotation (a rotation is a map $r _ { \theta } ( z ) = e ^ { i \theta } z )$ .Let $w \in D$ and consider the sequence $\{ w _ { n } \}$ defined by ${ w _ { n + 1 } } = f ( w _ { n } )$ . Show: $\scriptstyle \operatorname* { l i m } _ { n \to \infty } w _ { n } = 0$

(4) Does there exist a surjective holomorphic map $f : D \to \mathbb { C }$ from the unit disc to the whole complex plane? Prove that your answer is correct.

(5） For which $p \mathrm { ^ s }$ is the function $1 / x$ in $L ^ { p } ( 0 , \infty ) ?$

(6） Suppose that $f _ { n } : [ 0 , 1 ] \to \mathbb { R }$ is a sequence of $L ^ { 4 }$ functions with $\textstyle \int f _ { n } ^ { 4 } \leq 1$ for every n and so that $\begin{array} { r } { \operatorname* { l i m } _ { n \longrightarrow \infty } \int \left| f _ { n } \right| = 0 } \end{array}$ . Show that $f _ { n }$ goes to O weakly in $L ^ { 4 }$

（7） Suppose that $f _ { n }$ is a sequence of functions in $L ^ { 2 } ( \mathbb { R } )$ that converges weakly in $L ^ { 2 }$ to a function $f \in L ^ { 2 } ( \mathbb { R } )$ . Is it possible to have

$$
\operatorname* { l i m } _ { n \to \infty } | | f _ { n } | | _ { L ^ { 2 } } = \infty ?
$$

(8） Suppose that $f \in L ^ { 1 } ( \mathbb { R } )$ and $\begin{array} { r } { \widehat { f } ( z ) = \int _ { \mathbb { R } } e ^ { - i x z } f ( x ) } \end{array}$ dx. Show that $f$ and $\widehat { f }$ cannot both have compact support (except if $f$ is identically zero).

# ANALYSIS QUALIFYING EXAM SEPTEMBER 2006

Do all 8 problems. All problems are equally weighted. Time: 3 hours.

Show all work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Notation: $D = \{ z \in \mathbb { C } : | z | < 1 \}$

1. Use residues to calculate the integral

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { x ^ { 4 } + 4 } } .
$$

2.Let $f _ { n } : D \to \mathbb { C } , n = 1 , 2 , 3 , . . . ,$ be a sequence of holomorphic functions on the unit disk D such that $f _ { n } ^ { - 1 } ( 0 ) = \{ c _ { n } \}$ ，where $c _ { n } \in D$ .Suppose that $f _ { n }  f _ { 0 }$ uniformly, where $f _ { 0 }$ is not constant.

a) Prove that $f _ { 0 }$ has at most one zero in $D$

b) Can $f _ { 0 }$ have no zeros? If so, give a necessary and sufficient condition on the $c _ { n }$ for this to happen.

3. State whether each of the following two statements is true or false, and give either a proof or counterexample for each.

a） All holomorphic functions $f : \mathbb { C } \setminus \{ 0 \} \to H$ are constant, where $H = \{ z \in \mathbb { C }$ Im $z > 0 \}$ denotes the upper half plane.

b) All harmonic functions $h : \mathbb { C } \setminus [ 0 , + \infty ) \to [ 0 , 1 ]$ are constant.

4.Let $f : D  H$ be a holomorphic map from the unit disk D to the upper half plane $H = \left\{ z \in \mathbb { C } : \operatorname { I m } z > 0 \right\}$

Suppose that $f ( 0 ) = 3 i$ . Find the maximal possible value of $\left| f ^ { \prime } ( 0 ) \right|$

5. Let X be the Banach space of continuous real-valued functions on [0,π] that vanish at O and $\pi ,$ equipped with the sup norm. Suppose that Y is a closed subspace of X where every element of $Y$ can be written as a trigonometric polynomial, i.e., as a finite linear combination of the functions sin(kx) and $\cos ( k x )$ ，for $k = 0 , 1 , 2 , 3 , \ldots$ . Prove that $Y$ is finite dimensional.

CONTINUED ON NEXT PAGE

6. Suppose that f is a $C ^ { 1 }$ function on $[ 0 , 2 ]$ and $f ( 0 ) = f ^ { \prime } ( 0 ) = f ( 2 ) = f ^ { \prime } ( 2 ) = 0$ . Prove that for any $\varepsilon > 0$ there exists $T _ { \varepsilon }$ so that for all $t > T _ { \varepsilon }$

$$
\left| \int _ { 0 } ^ { 2 } f ( x ) e ^ { i t x } d x \right| \leq { \frac { \varepsilon } { t } } .
$$

7. Suppose that $f _ { j }$ is a sequence of $L ^ { 2 }$ functions on [0,1] with

$$
\int _ { 0 } ^ { 1 } | f _ { j } | \leq 1 / j \quad \mathrm { a n d } \quad \int _ { 0 } ^ { 1 } f _ { j } ^ { 2 } \leq 1 .
$$

Prove that $f _ { j }$ goes to zero weakly in $L ^ { 2 } ( [ 0 , 1 ] )$

8. Suppose that X is a real Banach space and, for all $x , y \in X$ , the norm $\| \cdot \|$ satisfies

$$
\| x + y \| ^ { 2 } + \| x - y \| ^ { 2 } \leq 2 \| x \| ^ { 2 } + 2 \| y \| ^ { 2 } .
$$

Suppose also that $f : X \to \mathbb { R }$ is a linear functional with norm 1; that is,

$$
\operatorname* { s u p } _ { \| \boldsymbol { x } \| = 1 } | f ( \boldsymbol { x } ) | = 1 .
$$

Prove that there exists a unique point $x \in X$ with $\| { \boldsymbol x } \| = 1$ and $f ( x ) = 1$

# ANALYSIS QUALIFYING EXAM MAY 2006

All problems are equally weighted. Time: 3 hours.

Show all work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

Part I. Complex Analysis. Do 5 out of the following 6 problems.

1. Let P be a point in an open set U in C,and suppose that f is a meromorphic function on U with a pole at P. Prove that there is no holomorphic function $g : U \setminus \{ P \} \to \mathbb { C }$ such that $e ^ { g ( z ) } = f ( z )$ for all $z \in U \setminus \{ P \}$

2. How many zeros does the polynomial

$$
z ^ { 7 } - 4 z ^ { 3 } + z - { \textstyle { \frac { 1 } { 2 } } }
$$

have in the unit disk $\{ | z | < 1 \} \stackrel { . } { : }$ How many zeros does it have in the disk $\{ | z | < 2 \}$ of radius 2? Justify your answers.

3.Find all entire functions f such that $| f ( z ) | \le | z | ^ { 3 / 2 }$ whenever $| z | \geq 1$ . Give explicit formulas for the functions and give a proof for your answer. (An entire function is a holomorphic function on C.)

4.Let $f _ { n } : D \to ( - \infty , 1 ) , n = 1 , 2 , . . . ,$ be an increasing sequence of harmonic functions on the unit disk D such that $f _ { n } ( 0 ) \to 1$ as $n \to \infty$ . (I.e., $f _ { n } ( z ) \leq f _ { n + 1 } ( z ) < 1 , \forall n \geq 1 . )$ Prove that $f _ { n } ( z ) \to 1$ as $n \to \infty$ , for all $z \in D$

5. Let H denote the upper half plane $\{ z \in \mathbb { C } : \operatorname { I m } z > 0 \}$ . Suppose that $f : H \to H$ is holomorphic,and $f ( 3 + 1 7 i ) = 3 + 1 7 i$ What is the maximum possible value of $f ^ { \prime } ( 3 { + } 1 7 i )$ . Give a reason for your answer (and try not to do any lengthy computations).

6.Find all the poles of the function

$$
f ( z ) = \frac { e ^ { \pi z } } { ( z ^ { 2 } + 1 ) ^ { 2 } } .
$$

Determine the residue of f at each pole.

Part II. Real Analysis.Do 5 out of the following 6 problems.

7. Quickies:

a) Give an example of a function that is in $L ^ { 2 } ( \mathbb { R } )$ but not in $L ^ { 1 } ( \mathbb { R } )$

b) Give an example of a function that is in $L ^ { 1 } ( ( 0 , 1 ) )$ but not in $L ^ { 2 } ( ( 0 , 1 ) )$

8. Prove that any function $f \in L ^ { 1 } ( I ) \cap L ^ { 2 } ( I )$ for any interval $I \subset \mathbb { R }$ must be in $L ^ { p } ( I )$ for all $p$ between 1 and 2.

9. Suppose that f is in $L ^ { 1 } ( \mathbb { R } )$ . Prove directly (i.e., without citing properties of the Fourier transform) that the function

$$
\widehat { f } ( t ) = \int _ { \mathbb { R } } e ^ { - i x t } f ( x ) d x
$$

is uniformly continuous and ${ \widehat { f } } ( t ) \to 0 { \mathrm { ~ a s ~ } } t \to \infty$

10.Suppose that $f$ is in $L ^ { 1 } ( \mathbb { R } )$ . Prove that

$$
\operatorname* { l i m } _ { h \to 0 } \int _ { \mathbb { R } } | f ( x + h ) - f ( x ) | = 0 .
$$

11. Suppose that $f _ { n }$ is a sequence of functions in $L ^ { 2 } ( [ 0 , 1 ] )$ that converges weakly to a function $f \in L ^ { 2 } ( [ 0 , 1 ] )$ ．Either prove that lim $\begin{array} { r } { \operatorname* { s u p } _ { n  \infty } \vert \vert f _ { n } \vert \vert _ { L ^ { 2 } ( [ 0 , 1 ] ) } < \infty } \end{array}$ or give a counter-example.

12.Let $f _ { j }$ be an orthonormal sequence in $L ^ { 2 } ( [ 0 , 1 ] )$ . Prove that

$$
S _ { n } = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } f _ { j }
$$

converges to zero a.e.

# ANALYSIS QUALIFYING EXAM SEPTEMBER 2005

Do all 8 problems. All problems are equally weighted. Time: 3 hours.

Show all work. In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

1. Let $\left\{ f _ { n } \right\}$ be a sequence of Lebesgue measurable functions on [0,1], and assume that

$$
\int _ { 0 } ^ { 1 } | f _ { n } ( x ) | ^ { 2 } d x \leq { \frac { 1 } { n ^ { 2 } } } .
$$

Show that:

$$
\operatorname * { l i m } _ { n  \infty } f _ { n } ( x ) = 0 \quad \mathrm { a . e . ~ o n } [ 0 , 1 ] .
$$

2.Let $f \in L ^ { 1 } ( \mathbb { R } , d x )$ . Prove that

$$
\operatorname* { l i m } _ { h \to 0 } \int _ { \mathbb { R } } | f ( x + h ) - f ( x ) | d x = 0 .
$$

3.Let $g _ { n }$ be a sequence of functions in $L ^ { 1 } ( S ^ { 1 } , d \theta )$ where $S ^ { 1 }$ is the unit circle $\{ e ^ { i \theta } : 0 \leq \theta \leq 2 \pi \}$ We say that $g _ { n } \ \to \ 0$ weakly if $\begin{array} { r } { \int _ { S ^ { 1 } } g _ { n } ( e ^ { i \theta } ) f ( e ^ { i \theta } ) d \theta  0 } \end{array}$ as $n \to \infty$ for all $f \in C ( S ^ { 1 } )$

Question: Suppose that $\left\{ g _ { n } \right\}$ is a sequence in $L ^ { 1 } ( S ^ { 1 } , d \theta )$ and $\begin{array} { r } { \int _ { S ^ { 1 } } e ^ { i k \theta } g _ { n } ( e ^ { i \theta } ) d \theta  0 } \end{array}$ as $n \to \infty$ for all $k \in \mathbb { Z }$ . Need $g _ { n } \to 0$ weakly? Give either a proof or a counterexample.

4. Suppose that $\left\{ f _ { n } \right\}$ is a sequence of elements of a Hilbert space X and that $f _ { n } \to f$ weakly $( \mathrm { i . e . , } ( f _ { n } , g )  ( f , g )$ for all $g \in X )$

(a) Show that

$$
\| f \| \leq \operatorname* { l i m } _ { n \to \infty } { \big \| } f _ { n } { \big \| } .
$$

Give an example showing that strict inequality can occur.

(b） Suppose in addition that $\left. f \right. = \operatorname* { l i m } _ { n \to \infty } \left. f _ { n } \right.$ . Show that $f _ { n } \to f$ in norm.

5. Use contour integration to evaluate

$$
\int _ { 0 } ^ { + \infty } { \frac { d x } { x ^ { 1 / 3 } ( 1 + x ) } } .
$$

Hint: Consider the contour beginning with the segment from $\varepsilon$ to $R ,$ then traversing a circle of large radius $R ,$ then going back to $\varepsilon ,$ and finally traversing a circle of small radius ε.

CONTINUED ON NEXT PAGE

6.(a) Describe all the automorphisms of the upper half plane $H = \left\{ z \in \mathbb { C } : \mathrm { R e } \ z > 0 \right\}$ (holomorphic bijective maps from H onto H).

(b) Describe all the automorphisms of C (holomorphic bijective maps from C onto C).

7. How many zeros does the polynomial

$$
z ^ { 9 } + z ^ { 5 } - 8 z ^ { 3 } - z + 2
$$

have between the circles $\{ | z | = 1 \}$ and $\{ | z | = 2 \}$ . Justify your answer.

8.Let $H = \left\{ z \in \mathbb { C } : \mathrm { R e } \ z > 0 \right\}$ denote the upper half plane.

(a) Does there exist a surjective holomorphic map $f : H \to \mathbb { C } ?$ Either give an example or prove that one does not exist.

(b) Does there exist a surjective holomorphic map $f : \mathbb { C } \to H ?$ Either give an example or prove that one does not exist.

# ANALYSIS QUALIFYING EXAM SPRING 2005

## Notation:

${ \mathcal { C } } ^ { \infty } ( \mathbb { R } )$ : complex-valued ${ \mathcal { C } } ^ { \infty }$ functions on $\mathbb { R } .$

$\mathcal { C } _ { c } ^ { \infty } ( \mathbb { R } )$ : compactly supported functions in ${ \mathcal { C } } ^ { \infty } ( \mathbb { R } )$

$L ^ { p } ( \mathbb { R } ) , \ L ^ { p } ( [ 0 , 1 ] ) : \ L ^ { p }$ functions with respect to Lebesgue measure on R,[0,1], respectively ${ \widehat { f } } :$ Fourier transform of $f$

$$
D = \{ z \in \mathbb { C } : | z | < 1 \}
$$

$$
\mathbb { R } ^ { + } = \{ x \in \mathbb { R } : x > 0 \}
$$

Do all 8 problems. Show all work.In each solution, state which theorems from 110.605 and 1o.6o7 you are applying and verify that the hypotheses are satisfied.

(1）Let $f ( x ) = e ^ { - \lvert x \rvert } \mathrm { ~ f o r ~ } x \in \mathbb { R } .$

(a）Is ${ \widehat { f } } \in { \mathcal { C } } ^ { \infty } ( \mathbb { R } ) ?$ Prove that your answer is correct.

(b） Show that $| { \widehat { f } } ( \xi ) | \to 0 { \mathrm { ~ a s ~ } } | \xi | \to \infty$

(2） Suppose that $f \in L ^ { 1 } [ 0 , 1 ]$ and let $g ( x ) = \int _ { x } ^ { 1 } \frac { f ( t ) } { t } d t$ Show that $g \in L ^ { 1 } [ 0 , 1 ]$ and that

$$
\int _ { 0 } ^ { 1 } g ( x ) d x = \int _ { 0 } ^ { 1 } f ( x ) d x .
$$

(3） Prove or find a counterexample to each of the following statements:

(a) $L ^ { 2 } ( \mathbb { R } ) \subset L ^ { 1 } ( \mathbb { R } )$

(b) $L ^ { 1 } ( \mathbb { R } ) \subset L ^ { 2 } ( \mathbb { R } )$

（c） $L ^ { 2 } ( [ 0 , 1 ] ) \subset L ^ { 1 } ( [ 0 , 1 ] ) ;$

(d） $L ^ { 1 } ( [ 0 , 1 ] ) \subset L ^ { 2 } ( [ 0 , 1 ] ) ;$

(4） Let $\{ e _ { n } \}$ be an orthonormal basis for a Hilbert space $H$

(a） Show that $e _ { n } \to 0$ weakly. (Explain what weak convergence means.)

(b） Show that $e _ { n }$ does not tend to zero strongly. (Explain what strong convergence means.)

(c）Let $\begin{array} { r } { v _ { n } = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } e _ { j } } \end{array}$ . Show that $v _ { n } \to 0$ strongly.

(5）Do there exist functions $f \in { \mathcal { C } } _ { c } ^ { \infty } ( \mathbb { R } )$ such that f is not identically zero and ${ \widehat { f } } \in { \mathcal { C } } _ { c } ^ { \infty } ( \mathbb { R } ) ?$ If $\mathrm { s o } ,$ find one. If not, prove that none exist.

$$
{ \widehat { f } } ( \xi )
$$

$$
\xi \in \mathbb { C }
$$

(6) Use residues to evaluate the integral

$$
\int _ { - \infty } ^ { \infty } { \frac { x \sin x d x } { ( x ^ { 2 } + 1 ) ( x ^ { 2 } + 4 ) } } \ .
$$

(7） Find a bijective holomorphic map f from the quadrant

$$
Q = \{ x + i y \in \mathbb { C } : x > 0 , \ y > 0 \}
$$

onto the unit disk D in C with $f ( 1 + i ) = 0 .$

(8） Let U be an open set in C containing the closed unit disk ${ \overline { { D } } } .$ Suppose f is a meromorphic function on U such that $f ( \partial D ) \subset \mathbb { R } ^ { + }$ . (In particular, f has no zeros or poles on dD.) Show that f has the same number of zeros as poles in $D$ (counting multiplicities).

Directions: This is a closed book exam. You have two and a half hours to do all seven problems. $\# 7$ is worth 10 points; the others are worth 20 points each.

1.a) Let $C ( [ 0 , 1 ] )$ denote the space of continuous functions on $[ 0 , 1 ]$ ，endowed with the $^ { 6 6 } \mathrm { { s u p } ^ { , \dag } }$ norm. Show that $C ( [ 0 , 1 ] )$ is a Banach space.

b)Let $B _ { p } = L ^ { p } ( [ 0 , 1 ] )$ ，with $1 < p < \infty$ . Define weak and strong convergence in $B _ { p }$ . Then,show that the sequence $f _ { n } ( x ) =$ sin nx converges weakly to O,but not strongly to O, in $B _ { 2 }$

2.a) Let f be integrable over a set A and suppose $A = \cup _ { n = 1 } ^ { \infty } A _ { n }$ ,where the $A _ { n }$ are pairwise disjoint. Show that

$$
\int _ { A } f \ = \ \sum _ { n = 1 } ^ { \infty } \int _ { A _ { n } } f
$$

and that the sum on the right-hand side is absolutely convergent.

b）Let $\mu$ be Lebesgue measure on $\mathbb { R } ^ { 2 }$ and let $f \in L ^ { 1 } ( \mathbb { R } ^ { 2 } )$ . Show there is a Borel measure X for which $d \lambda = f d \mu$ (verify that it is a measure).

c)For $f = x ^ { 2 } + y ^ { 2 }$ and D the unit disc,compute $\lambda ( D )$

3.Let $f \in L ^ { 1 } ( \mathbb { R } )$ Show directly (i.e.， do not cite properties of the Fourier transform) that the function

$$
{ \widehat { f } } ( \xi ) = \int _ { \mathbb { R } } e ^ { - i x \xi } f ( x ) d x
$$

is uniformly continuous and ${ \widehat { f } } ( \xi ) \to 0 { \mathrm { ~ a s ~ } } | \xi | \to \infty$

4. Show that $f ( x ) = { \frac { \cos x } { 1 + x ^ { 2 } } }$ is an $L ^ { 1 }$ function on the real line (with respect to Lebesgue measure). Then evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { \cos x \ d x } { 1 + x ^ { 2 } } } .
$$

5. Determine whether the equation $z ^ { 3 } + z ^ { 4 } = 2$ in the complex variable z has any non-real solutions with $| z | < 2$

6.Let $f$ be an entire function with $| f ( z ) | \leq 3 \log | z |$ when $| z | > 2$ Either verify that f must be constant, or give a counterexample.

7. Let $\gamma$ denote the curve $| z - 1 | = 2$ , oriented counterclockwise. Evaluate

$$
\int _ { \gamma } { \frac { e ^ { z } d z } { z ^ { 3 } } } .
$$

Instructions: Do all problems. Show all details in your solutions. Unless statcd otherwise, you nay cite any of the theorems mentioncd in the syllabus.

1. Consider the sequence of functions $g _ { n } ( x ) = [ \sin ( n x ) ] ^ { 2 }$ on $[ 0 , 2 \pi ]$ . Define each of the following notions of convergence and determine whether the sequcnce converges in that sense: if so, determinc the limit:

a) Converges pointwise

b) Converges strongly in $L ^ { 1 }$

c) Converges weakly in $L ^ { 1 }$

2. Consider the set of positive continuous periodic functions $f$ on $[ 0 , 2 \pi ]$ satisfying $\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f d \theta = 1$ . What is the largest possible value of $\exp \left( { \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log f d \theta \right)$ for such functions? Prove that your answer is correct.

3.Let $\alpha > 1 / 2$ and consider $f _ { \alpha } ( x ) = \int _ { \mathbb { R } } ( 1 + \xi ^ { 2 } ) ^ { - \alpha } e ^ { 2 \pi i x \xi } d \xi .$

Without doing the integration, determinc, for each α, which of the following properties holds for $f _ { \alpha }$ ， and prove that your answcr is correct:

a) i) lim|a丨→∞|fa(x)|=0, ii) $f _ { \alpha } \in L ^ { 2 } ( \mathbb { R } )$

b) Without appealing to thc properties of thc Fourier transform, show that i) fα ∈ C(R), i) $f _ { \alpha }$ is boundcd on IR.

4. In problem $\# 3$ ,take $\alpha = 1$ . Calculate $f _ { 1 } ( x )$ , as defined in $\# 3$ ，by the method of residues.

5.a)Let $f ( z )$ be complex analytic in the disc $| z | < \pi$ . Assume that the only zero of $f$ in the closcd unit disc $\overline { { D } } = \{ z : | z | \leq 1 \}$ is a simple zero at thc origin. Let C be the unit circle, oriented counterclockwise. Evaluatc

$$
\int _ { C } { \frac { d z } { f ( z ) } } ,
$$

in the sense that no integration symbols should appcar in the answer.

$| \ u _ { ) } \}$ Lct $f$ be as in part $\mathrm { \Pi ^ { \ a } } )$ : except assume that $f$ has a 2nd-order (i.e., double) zero at the origin. Verify or give a counterexample:

$$
\mathrm { A s s c r t i o n : } \quad \int _ { C } { \frac { d z } { f ( z ) } } = 0 .
$$

6.Let $f ( z )$ be holomorphic in an open sct containing the closed unit disc $\overrightharpoon { D }$ Suppose that $| f ( z ) | < 1$ for all z on the unit circle. Show that there is exactly one point $z \in D$ (the intcrior of $\overline { { D } } )$ for which $f ( z ) = z$

7. Determinc a one-to-one complex analytic mapping $f .$ other than $f ( z ) = z$ that takcs $D$ (notation as above) onto itself and satisfics $\begin{array} { r } { f ( \frac { 1 } { 3 } ) = \frac { 1 } { 3 } } \end{array}$ ·

Directions: This is a closed book exam. You have two hours to do all six of the (equally weighted） problems.

Question 1. Suppose that $f \in L ^ { 1 } ( \mathbf { R } )$ . Prove that given $\epsilon > 0$ ，there exists $\delta > 0$ so that $\int _ { A } | f | < \epsilon$ for every measurable set A with $| A | < \delta$ ，

where |A| denotes the measure of A.

Question 2. Suppose that $f \in C ^ { 1 } ( [ 0 , \pi ] ) )$ and $f ( 0 ) = f ( \pi ) = 0$ . Prove that

$$
\int _ { 0 } ^ { \pi } f ^ { 2 } \leq \int _ { 0 } ^ { \pi } ( f ^ { \prime } ) ^ { 2 } .
$$

Question 3. Suppose that $1 < p <$ O and the linear mapping $T$ is defined by

$$
T f ( x ) = x ^ { - 1 / p } \int _ { 0 } ^ { x } f ( t ) d t .
$$

Show that $T$ is a bounded map from $L ^ { q } ( ( 0 , \infty ) )$ to $C ^ { 0 } ( ( 0 , \infty ) )$ , where q satisfies $1 / p + 1 / q = 1$

Question 4. Determine the number of zeros the function $f ( z ) = 2 z ^ { 5 } + 8 z - 1$ has in the annulus $1 < | z | < 2$

Question 5. Suppose that f is holomorphic on the punctured disk $0 < | z | < 2$

(A) Prove that if there is a real constant C such that $| f ( z ) | \le C$ then

$$
\int _ { | z | < 1 } | f ^ { \prime } ( z ) | ^ { 2 } d z < \infty .
$$

(B） What happens when $| f |$ is unbounded?

Question 6. Suppose that $u > 0$ is a positive harmonic function on the punctured plane $0 < | z |$ . Prove that u is constant.

## SPRING 20O3 COMPLEX ANALYSIS QUALIFYING EXAM

Please atempt all the problems and show all your work. In the following, “holomorphic” is synonymous with “analytic.” Also, $\Delta$ will denote the open unit disk in $\mathbb { C }$

(1）(a)Let $f : \mathbb { C } \to \mathbb { C }$ be meromorphic with a pole at infinity. Show that $f$ must be a rational function.

(b) Use the above to prove the following: if $f : \Delta  \mathbb { C }$ is holomorphic with a continuous extension to the boundary of $\Delta$ such that $| f ( z ) | = 1$ for all $| z | = 1$ ，then $f ( z )$ is the restriction of a rational function.

(2)Let $f : \Delta  \Delta$ be a holomorphic function with $f ( 0 ) = 0$ and $\left| f ^ { \prime } ( 0 ) \right| = M$ If $0 \neq w \in \Delta$ is any other zero of $f ( z )$ , show that:

$$
\frac { M } { 1 + M } \leq | w | ~ .
$$

(3)Let C be the closed curve defined by two pieces: the first piece is given by the set of all $z$ satisfying $| z - 1 | = 3$ and $\operatorname { R e } ( z - 1 ) \geq 0$ . The second piece is the straight line segment from $1 + 3 i$ to $1 - 3 i$ . Orient C in the counterclockwise direction,and let Ω be the region enclosed by C. Suppose f is holomorphic in a neighborhood of $\overline { { \Omega } }$ with no zeros on $C .$ Suppose also that:

$$
{ \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { z f ^ { \prime } ( z ) } { f ( z ) } } d z = 3 \qquad \mathrm { a n d } \qquad { \frac { 1 } { 2 \pi i } } \int _ { C } { \frac { z ^ { 2 } f ^ { \prime } ( z ) } { f ( z ) } } d z = { \frac { 5 } { 2 } } \ .
$$

Determine all the zeros of $f$ in Ω explicitly.

(4）(a) State Rouché's Theorem.

(b）Let $\varphi : \Omega \to \mathbb { C }$ be holomorphic on an open convex set Ω. Show that for z, $w \in \Omega$

$$
| \varphi ( z ) - \varphi ( w ) | \leq \operatorname* { m a x } _ { \xi \in L } | \varphi ^ { \prime } ( \xi ) | | z - w | ~ ,
$$

where L is the straight line segment from z to w.

(c）Use the above to prove the following: suppose

$$
f ( z ) = z + \sum _ { n = 2 } ^ { \infty } a _ { n } z ^ { n }
$$

where

$$
\sum _ { n = 2 } ^ { \infty } n | a _ { n } | \leq 1 ~ .
$$

Show that $f ( z )$ is a 1-1 holomorphic function on $\Delta$# Real Analysis Qualifying Exam, Fall 2002

Instructions: You have 2 hours to do all problems as completely as posible.

1. Let $\psi ( x ) = x$ on $[ 0 , \frac { 1 } { 2 } ] \ , \ \psi ( x ) = 1 - x$ on $[ \textstyle { \frac { 1 } { 2 } } , 1 ]$ and extended periodically of period 1.Define $\begin{array} { r } { f ( x ) = \sum _ { n = 0 } ^ { \infty } 2 ^ { - n } \psi ( 8 ^ { n } x ) } \end{array}$

i. Show that $f ( x )$ is continuous everywhere.

ii. Show that $f ( x )$ is differentiable nowhere.

Hint:Consider the difference quotients

$$
\Delta _ { h } f ( x ) \equiv { \frac { f ( x + h ) - f ( x ) } { h } }
$$

where $h = \pm 8 ^ { - k }$ and the sign is chosen so that x and $x + h$ lie on the same linear segment of the graph of $\psi ( 8 ^ { k - 1 } x )$ . Then

a. $\begin{array} { r } { \Delta _ { h } f ( x ) = \sum _ { n = 0 } ^ { k - 1 } 2 ^ { - n } \Delta _ { h } \psi ( 8 ^ { n } x ) } \end{array}$

b. $\begin{array} { r } { | \Delta _ { h } f ( x ) | \geq 4 ^ { k - 1 } - \sum _ { n = 0 } ^ { k - 2 } 4 ^ { n } } \end{array}$

2.Let $f _ { 1 } ( x ) \leq f _ { 2 } ( x ) \leq . . . \leq f _ { n } ( x ) \leq . . .$ 、on a set A,where the functions $f _ { n }$ are integrable and $\textstyle \int _ { A } f _ { n } ( x ) \ d x \leq M$ for some constant M. Show that the limit

$$
f ( x ) = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )
$$

exists and is finite almost everywhere on A and that

$$
\operatorname* { l i m } _ { n  \infty } \int _ { A } f _ { n } ( x ) \ d x = \int _ { A } f ( x ) \ d x \ .
$$

3.i.Define equicontinuity and state the Arzela-Ascoli theorem.

ii. Let $\mathcal { F }$ be the family of real valued functions on_[0,1] satisfying $f ( 0 ) = 0$ and $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) ^ { 2 } \ d x \leq 1 } \end{array}$ Show that any sequence in $\mathcal { F }$ has a subsequence that converges uniformly.

4.Let K be a closed convex subset of a Hilbert space H. Show that for each $x \in H$ , there is a unique $y \in K$ such that

$$
| | x - y | | = i n f _ { z \in K } | | x - z | |
$$

5.i.Find the sum of the series $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } \frac { \sin { ( 2 n - 1 ) x } } { 2 n - 1 } \mathrm { o n } \left( 0 , 2 \pi \right) } \end{array}$

ii. Show that $\begin{array} { r } { \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { ( 2 n - 1 ) ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 8 } } } \end{array}$

## Complex Analysis Core Qualifying Exam, Fall 2002

Do 5 of the 6 problems. Indicate clearly which 5 you want graded; if it is not clear, we will grade $\# 1 \mathrm { - } 5$ . Each problem counts for 20 points. In the case where there are two parts, the score is subdivided as indicated. Note: for the purposes of the exam, holomorphic is the same as complex analytic.

1. (a)(5 points) Give a counterexample to the assertion: If f is holomorphic on the annulus $\{ z : 1 < | z | < 3 \}$ ，then f extends holomorphically to the disc $\{ z : | z | < 3 \}$

(b)(15 points) Determine whether the following is true: If f is holomorphic on the annulus $\{ z : 1 < | z | < 3 \}$ ，then f extends meromorphically to the disc $\{ z : | z | < 3 \}$

2. (a) (15 points) Show that there is no one-to-one holomorphic map-ping of the open annulus $\{ z : 1 < | z | < 2 \}$ ：onto the punctured unit disc $\{ z : 0 < | z | < 1 \}$ . (HINT: consider the inverse mapping)

(b) (5 points) Give an example of a one-to-one $C ^ { \infty }$ mapping of the open annulus $\{ z : 1 < | z | < 2 \}$ onto the punctured unit disc $\{ z : 0 < | z | < 1 \}$

3.(20 points) Determine all entire functions f for which $| f ( z ) | \leq | z | ^ { 2 }$ for all $z \in \mathbb { C }$

4.(20 points) Let D denote the unit disc $\{ z : | z | < 1 \}$ .Determine a holomorphic mapping f of D onto itself for which $\begin{array} { r } { f ( \frac { 1 } { 2 } ) = - \frac { 1 } { \pi } } \end{array}$

5.Let $\begin{array} { r } { P ( z ) = z ^ { 7 } + z ^ { 3 } + \frac { 1 } { 1 6 } } \end{array}$

(a)(5 points) Show that P has no multiple zeros.

(b)(15 points) Determine the number of zeros of P that lie in the closed disc $| z | \leq { \frac { 1 } { 2 } }$ ·

6.(20 points) Evaluate the integral:

$$
\int _ { 0 } ^ { \infty } { \frac { u ^ { 2 } d u } { u ^ { 6 } + 1 } }
$$

## Real Analysis Qualifying Exam

Time: 2 hours

Instructions: Do five of the following 6 problems. (If you attempt all6 problems,clearly indicate which problems you want graded.） Each problem is worth 2O points.

1. Let $f : [ 0 , 2 ] $ Rbe $\mathrm { ~ a ~ } \mathcal { C } ^ { 1 }$ function such that $f ( x )$ and $f ^ { \prime } ( x )$ vanish at $x = 0$ and at $x = 2 .$ Prove that for all $\varepsilon > 0$ there exists $t _ { \varepsilon } \in \mathbb { R } ^ { + }$ such that

$$
\left| \int _ { 0 } ^ { 2 } f ( x ) e ^ { i t x } d x \right| \leq { \frac { \varepsilon } { t } } \qquad { \mathrm { f o r } } t \geq t _ { \varepsilon } .
$$

2.Let $\left\{ c _ { n } \right\}$ be a sequence of positive real numbers,and let $f _ { n } : \mathbb { R } \to \mathbb { R }$ be given by

$$
f _ { n } ( x ) = \sin ( x + c _ { n } ^ { 2 } ) + { \frac { 1 } { c _ { n } } } \sin ( c _ { n } x ) .
$$

Prove that the sequence $\{ f _ { n } \}$ has a subsequence converging pointwise to a continuous function.

3. Let X denote the set of functions $f : [ 0 , 1 ] \to \mathbb { R }$ such that $\| f \| < \infty$ ，where

$$
\| f \| : = | f ( 0 ) | + \operatorname* { s u p } \left\{ { \frac { | f ( x ) - f ( y ) | } { | x - y | ^ { 1 / 5 } } } : x \neq y \right\} ~ .
$$

Prove that $( X , \parallel \cdot \parallel )$ is a Banach space; i.e., show that X is a vector space, $\| \cdot \|$ is a norm, and X is complete.

4. Suppose that $f \in L ^ { 1 } ( \mathbb { R } ^ { n } , m )$ satisfies

$$
\left| \int _ { E } f d m \right| \leq m ( E )
$$

for all Lebesgue measurable sets E (where m denotes Lebesgue measure on $\mathbb { R } ^ { n } )$ . Prove that $| f | \le 1$ almost everywhere.

5.Let $( X , { \mathcal { M } } , \mu )$ be a measure space, and let $f \in L ^ { 1 } ( \mu ) \cap L ^ { \infty } ( \mu )$ .Prove that

$$
\operatorname* { l i m } _ { p \to \infty } \| f \| _ { p } = \| f \| _ { \infty } .
$$

6.Let $u \in \mathcal { D } ^ { \prime } ( \mathbb { R } )$ be given by

$$
( u , \varphi ) = \operatorname* { l i m } _ { \varepsilon \to 0 ^ { + } } \left[ \int _ { - \infty } ^ { - \varepsilon } \frac { \varphi ( x ) } { x } d x + \int _ { \varepsilon } ^ { + \infty } \frac { \varphi ( x ) } { x } d x \right] \ , \qquad \forall \ \varphi \in \mathcal { D } ( \mathbb { R } ) = \mathcal { C } _ { c } ^ { \infty } ( \mathbb { R } ) \ .
$$

Show that the above limit exists and that u is the distribution derivative of the function $f \in L _ { \mathrm { l o c } } ^ { 1 } ( \mathbb { R } )$ given by $f ( x ) = \log | x |$ ·

# Complex Analysis Core Qualifying Exam Spring 2002 Instruction: Answer any FOUR questions

1.Let f be an entire function such that the image of f does not intersect $\{ z \in \mathbb { R } : z \geq 5 \}$ .Prove that $f$ is a constant.

2.Evaluate the integral

$$
\int _ { 0 } ^ { 2 \pi } { \frac { d x } { a ^ { 2 } + \cos ^ { 2 } x } } .
$$

Where $a > 1$

3. Classify all simply connected regions in the extended complex plane up to biholomorphic equivalence. i.e,give a list of simply connected region, prove that every simply connected region in the extended complex plane is biholomorphic equivalent to a member in your list.Prove also that no two members in your list are biholomorphic equivalent.

4.Let f be a holomorphic function which maps the unit disk into the unit disc. Show that

$$
| f ( z ) + f ( - z ) | \leq 2 | z | ^ { 2 }
$$

for all z in the unit disc,and if the equality holds for some z, then,

$$
f \left( z \right) = e ^ { i \theta } z ^ { 2 }
$$

for some real 0.

5.Let $\scriptstyle \sum _ { n = - \infty } ^ { \infty } a _ { n } z ^ { n }$ be the Laurent series expansion of $\scriptstyle { \frac { 1 } { \sin z } }$ on the annulus $\left\{ z \in \mathbb { C } : \pi < | z | < 2 \pi \right\}$ .Evaluate the coefficients $a _ { n }$ for $n < 0$

6. Show that a Mobius transformation maps a straight line or circle onto a straight line or circle.

## Real Analysis Qualifying Exam,Fall 2001

Instructions: Attempt to do all problems.Each is worth 20 points.All the measures involved are Lebesgue measure.

1.）Let f be a continuous function on $[ 0 , \infty )$ such that lim $_ { 1 _ { X \to \infty } } f ( x )$ exists (finitely). Prove that f is uniformly continuous.

2.） Let f and g be continuous real valued functions on

R such that lim $\scriptstyle { \mathrm { 1 } } | x | \to \infty , f ( x ) = 0$ and

$\textstyle \int _ { - \infty } ^ { \infty } | g ( x ) | d x < \infty$ . Define the function h

on R by

$$
h ( x ) = \int _ { - \infty } ^ { \infty } f ( x - y ) g ( y ) d y .
$$

Prove that $\scriptstyle \operatorname* { l i m } _ { | x | \to \infty } h ( x ) = 0$

3.）Let $\left\{ f _ { n } \right\}$ be a sequence of real valued functions in

$L ^ { 4 / 3 } ( 0 , 1 )$ such that $f _ { n } \to 0$ in measure as $n \to \infty$

and $\begin{array} { r } { \int _ { 0 } ^ { 1 } | f _ { n } ( x ) | ^ { 4 / 3 } d x \leq 1 } \end{array}$ . Show that $\begin{array} { r } { \int _ { 0 } ^ { 1 } | f _ { n } ( x ) | d x \to 0 { \mathrm { ~ a s ~ } } n \to \infty } \end{array}$

4.）Let $f \in L ^ { 1 } ( [ 0 , 1 ] )$ .For $k \in \mathbb N$ let $f _ { k }$ be

the step function defined on $[ 0 , 1 ]$ by

$$
f _ { k } ( x ) = k \int _ { j / k } ^ { ( j + 1 ) / k } f ( t ) d t , \quad { \mathrm { f o r ~ } } { \frac { j } { k } } \leq x < { \frac { j + 1 } { k } } .
$$

Show that $f _ { k }$ tends to $f$ in

$L ^ { 1 }$ norm as k tends to +o.

Hint: Treat first the case where f is

continuous,and use approximation.

5.）Let $1 \leq p < q < \infty$ . Which of the following statements

(i)-(vi) are true,and which are false? Justify all the negative

answers by a counterexample, but you do not have to justify the

positive answers.

(i) $L ^ { { \boldsymbol { p } } } ( \mathbb { R } ) \subset L ^ { q } ( \mathbb { R } )$

(ii) $L ^ { q } ( \mathbb { R } ) \subset L ^ { p } ( \mathbb { R } )$

(ii) $L ^ { p } ( [ 0 , 1 ] ) \subset L ^ { q } ( [ 0 , 1 ] )$

(iv) $L ^ { q } ( [ 0 , 1 ] ) \subset L ^ { p } ( [ 0 , 1 ] )$

(v） $\ell ^ { p } ( \mathbb { Z } ) \subset \ell ^ { q } ( \mathbb { Z } )$

(vi) $\ell ^ { q } ( \mathbb { Z } ) \subset \ell ^ { p } ( \mathbb { Z } )$

Justify your answer to the following question:

(vii) For which $s \geq 1$ is $L ^ { p } ( \mathbb { R } ) \cap L ^ { q } ( \mathbb { R } ) \subset L ^ { s } ( \mathbb { R } ) ?$

## COMPLEX ANALYSIS CORE QUALIFYING EXAM,FALL 2001

Instructions: Attempt FOUR of the following problems. Each is worth 25 points. Please label clearly which four of the five problems you want graded. Show all your work.

Notation: C denotes the complex numbers. For $z \in \mathbb { C } , \operatorname { R e } ( z )$ denotes the real part of $z .$ For each $r \geq 0 , D _ { r } ( 0 ) = \{ z \in \mathbb { C } : | z | < r \}$ ：

Problem 1.A meromorphic function on $\mathbb { C } \cup \{ \infty \}$ is a meromorphic function $f ( z )$ on C such that $g ( z ) = f ( 1 / z )$ is also meromorphic. Show that a meromorphic function on $\mathbb { C } \cup \{ \infty \}$ must be rational, i.e. one can express it as the quotient of two polynomials.

Problem 2. Fix a real number $\alpha > 1$ . Show that the equation $z - \alpha = e ^ { - z }$ has precisely one solution in the half plane $\mathrm { R e } ( z ) > 0$ and that this solution must be real.

Problem 3. Compute: $\int _ { 0 } ^ { \infty } { \frac { d x } { 1 + x ^ { 3 } } } .$

Problem 4. Suppose that $f : D _ { 1 } ( 0 ) \to \mathbb { C }$ is a one-to-one holomorphic function with $\Omega = f \left( D _ { 1 } ( 0 ) \right)$ Let $g : D _ { 1 } ( 0 ) \to \Omega$ be another holomorphic function with $g ( 0 ) = f ( 0 )$ . Show that for each $0 \leq r < 1$ $g \left( D _ { r } ( 0 ) \right) \subset f \left( D _ { r } ( 0 ) \right)$ ：

Problem 5. Use the result in Problem 4 to prove the following: If $g$ is a holomorphic function on $D _ { 1 } ( 0 )$ with $g ( 0 ) = 0$ and $| \mathrm { R e } ( g ( z ) ) | < 1$ for all $z \in D _ { 1 } ( 0 )$ ,then

$$
| g ( z ) | \leq { \frac { 2 } { \pi } } \log \left\{ { \frac { 1 + | z | } { 1 - | z | } } \right\}
$$

for all $z \in D _ { 1 } ( 0 )$

# REAL ANALYSIS QUALIFYING EXAM,SPRING 2001

Instructions: Attempt to do all of the problems. Each is worth 20 points. All the measures involved are Lebesgue measure.

1.） Suppose that $\phi \in C _ { 0 } ^ { \infty } ( \mathbb { R } ^ { n } )$ has ʃΦdx = 1. If $\phi _ { \varepsilon } ( x ) = \varepsilon ^ { - n } \phi ( x / \varepsilon )$ )，prove that if $1 \leq p <$ 8and $f \in L ^ { p } ( \mathbb { R } ^ { n } )$ then $f * \phi _ { \varepsilon } \to f$ in $L ^ { p } ( \mathbb { R } ^ { n } )$ .Prove that this is not true for $p = \infty$

2.）Suppose that $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ . Prove that for every $\varepsilon > 0$ there is a $\delta > 0$ such that if A is measurable with measure $< \delta$ then

$$
| \int _ { A } f d x | < \varepsilon .
$$

3.）Recall that $f : [ 0 , 1 ] \to \mathbb { R }$ is lower semicontinuous if lim ini $\operatorname { f } _ { x \to x _ { 0 } } f ( x ) \geq f ( x _ { 0 } )$ for every $x _ { 0 } \in [ 0 , 1 ]$ .Prove that if $f$ is a nonnegative lower semicontinuous function then one always has $\begin{array} { r } { S _ { + } ( f , P ) \to \int _ { 0 } ^ { 1 } } \end{array}$ f(x)dx as $| P | \to 0$ if $S _ { + } ( f , P )$ is the lower Riemann sum associated with a partition $\dot { P }$ of $[ 0 , 1 ]$ and $| P |$ is the smallest interval of the partition. Here $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x$ is the Lebesgue integral of $f .$

Here,if $0 = t _ { 0 } < t _ { 1 } < \cdots < t _ { n } = 1$ , is the partition $P ,$ then

$$
S _ { + } ( f , P ) = \sum _ { j = 1 } ^ { n } \operatorname* { i n f } _ { x \in [ t _ { j - 1 } , t _ { j } ) } f ( x ) ( t _ { j } - t _ { j - 1 } ) .
$$

Hint: To prove $\begin{array} { r } { S _ { + } ( f , P )  \int _ { 0 } ^ { 1 } f ( x ) d x } \end{array}$ as $| P | \to 0 ,$ ,it suffices to show that $S _ { + } ( f , P _ { n } ) $ $\textstyle \int _ { 0 } ^ { 1 } f ( x ) d x { \mathrm { ~ i f ~ } } P _ { n }$ is a nested sequence of partitions whose lengths goes to zero.

4.）For which values of α and $\beta$ does the following inequality hold?

$$
\| f \| _ { 2 } \leq \| f \| _ { 4 / 3 } ^ { \alpha } \| f \| _ { 4 } ^ { \beta } .
$$

Prove your assertion.

5.）Let $K \in C ( [ 0 , 1 ] \times [ 0 , 1 ] )$ .For $f \in C ( [ 0 , 1 ] )$ define

$$
T f ( x ) = \int _ { 0 } ^ { 1 } K ( x , y ) f ( y ) d y .
$$

Prove that $T f \in C ( [ 0 , 1 ] )$ .Moreover, prove that $\Omega = \{ T f : \| f \| _ { s u p } \leq 1 \}$ is precompact in $C ( [ 0 , 1 ] )$ . Here,we are using the sup-norm $\| \cdot \| _ { s u p }$ on $C ( [ 0 , 1 ] )$ and Ω being precompact means that every sequence in Ω must have a subsequence that converges with respect to this norm to an element of $C ( [ 0 , 1 ] )$

## COMPLEX ANALYSIS CORE QUALIFYING EXAM,SPRING 2001

Directions: Do FIVE of the following six questions; they are weighted equally. Label clearly which five that you want graded (otherwise only first five will be). Show your work.

Question 1. Suppose that $f , g$ are entire holomorphic functions with $| f ( z ) | \leq | g ( z ) |$ for all $z \in \mathbf { C }$ . Prove that there is a constant $c \in \mathbf { C }$ so that $f = c g$

Question 2. Find the number of zeros of the function $f ( z ) = 2 z ^ { 5 } + 8 z - 1$ in the annulus $1 < | z | < 2$

Question 3. Assume that $f _ { n }$ is holomorphic in $| z | < 1$ and $| f _ { n } | \leq 1 0$ . Assume also that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } \left( 2 ^ { - j } \right)$ exists for each $j = 1 , 2 , \dots$ .Prove that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( z )$ exists for all z with $| z | < 1$

Question 4. Let $u ( z ) > 0$ be a positive harmonic function in the punctured plane $0 < | z |$ Show that u must be constant.

Question 5. Let f be a non-constant holomorphic function in the annulus $1 < | z | < 2$ with $| f | \equiv 5$ on the boundary. Show that f has at least two zeros.

Question 6. Let $P ( z )$ be a polynomial. Show that all zeros of $P ^ { \prime } ( z )$ lie in the convex hull of the zeros of $P ( z )$
