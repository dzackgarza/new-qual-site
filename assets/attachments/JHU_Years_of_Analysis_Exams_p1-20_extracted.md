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

6. Let $f : U \to \mathbb { C }$ be a non-constant holomorphic function where $U \subset \mathbb { C }$ is an open set containing the closure D of the unit disk $D = \{ z \in C : | z | < 1 \}$ . If $| f ( z ) | = 1$ for all $z \in \partial D$ , then prove that $D \subset f ( { \overline { { D } } } )$

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