# Real Analysis Qual Prep Week 1: Preliminaries

D. Zack Garza

## Table of Contents

## Contents

Table of Contents 2\
1 Week 1: Preliminaries 3\
1.1 Topics 3\
1.2 Background / Warmup / Review 3\
1.2.1 Metric Spaces / Topology 4\
1.2.2 Sequences 4\
1.2.3 Series 5\
1.2.4 Continuity and Discontinuity 5\
1.3 Exercises 5\
1.4 Qual Questions 6

## 1

## Week 1: Preliminaries

<!-- image-->

## 1.1 Topics

<!-- image-->

• Concepts from Calculus

– Mean value theorem

– Taylor expansion

– Taylor’s remainder theorem

– Intermediate value theorem

– Extreme value theorem

– Rolle’s theorem

– Riemann integrability

• Continuity and uniform continuity

– Pathological functions and sequences of functions

• Convergence

– The Cauchy criterion

– Uniform convergence

– The M-Test

$F _ { \sigma }$ and $G _ { \delta }$ sets,

• Nowhere density,

• Baire category theorem,

• Heine-Borel

• Normed spaces

• Series and sequences,

– Convergence

– Small tails,

– limsup and liminf,

– Cauchy criteria for sums and integrals

• Basic inequalities (triangle, Cauchy-Schwarz)

• Weierstrass approximation

• Variation and bounded variation

<!-- image-->

## 1.2 Background / Warmup / Review

<!-- image-->

• Derive the reverse triangle inequality from the triangle inequality.

• Let $E \subseteq \mathbb { R }$ . Define sup E and inf E.

• What is the Archimedean property?

## 1.2.1 Metric Spaces / Topology

• What does it mean for a metric space to be complete?

• Give two or more equivalently definitions for compactness in a complete metric space.

• What is an interior point?
An isolated point?
A limit point?

• What does it mean for a set to be open?
Closed?

• What is the closure of a subspace $E \subseteq X ?$

• What does it mean for $E \subseteq X$ to be a dense subspace?

• What does it mean for a family of sets to form a basis for a topology?

– What is a basis for the standard topology on $\mathbb { R } ^ { d _ { ? } }$

• Let X be a subset of $\mathbb { R } ^ { d } .$ . Prove the Heine-Borel theorem:

– Show that X compact =⇒ X is closed

– Show that X compact =⇒ X is bounded

– Show that a closed subset of a compact set must be bounded.

– Show that if X closed and bounded =⇒ X is compact.

• Find an example of a metric space with a closed and bounded subspace that is not compact.

– How can this be modified to obtain a necessary and sufficient condition?

• Determine if the following subsets of R are opened, closed, both, or neither:

$$
- \ \mathbb { Q }
$$

$$
- \ \mathbb { Z }
$$

$$
- \ \{ 1 \}
$$

$$
- \ \left\{ p \in \mathbb { Z } ^ { \geq 0 } \ \Big | \ p \ \mathrm { i s \ p r i m e } \right\}
$$

$$
- \left\{ { \frac { 1 } { n } } \ \Big | \ n \in \mathbb { Z } ^ { \geq 0 } \right\}
$$

$$
- \{ { \frac { 1 } { n } } \ | \ n \in \mathbb { Z } ^ { \geq 0 } \} \cup \{ 0 \}
$$

## 1.2.2 Sequences

• Can a convergent sequence of real numbers have a subsequence converging to a different limit?

• What does it mean for a sequence of functions to converge pointwise and to converge uniformly?

– Give an example of a sequence that converges pointwise but not uniformly.

• Prove that every sequence admits a monotone subsequence.

• Prove the monotone convergence theorem for sequences.

• Prove the Bolzano-Weierstrass Theorem.

## 1.2.3 Series

$$
\sum _ { n \in \mathbb { N } } a _ { n } < \infty
$$

– What does it mean for a series to converge?
How can you check this?

- What does it mean for a series to converge uniformly?
  What do you have to show to prove it does not converge uniformly?

- Show that if converges, then

$$
a _ { n } \stackrel { n \to \infty } { \longrightarrow } 0
$$

. - Show that convergent sequences have small tails in the following sense:

$$
\sum _ { n > N } a _ { n } \overset { N \to \infty } { \longrightarrow } 0
$$

. - Is this a necessary and sufficient condition for convergence?

- State the ratio, root, integral, and alternating series tests.

- Prove that the harmonic series diverges - Derive a formula for the sum of a geometric series.

- State and prove the p-test.

- What does it mean for a series to converge absolutely?

- Find a sequence that converges but not absolutely.

## 1.2.4 Continuity and Discontinuity

• What does it mean for a function to be uniformly continuous on a set?

• Is it possible for a function $f : \mathbb { R } $ R to be discontinuous precisely on the rationals $\mathbb { Q } ?$ If so, produce such a function, if not, why?

– Can the set of discontinuities be precisely the irrationals R $\setminus \mathbb { Q } ?$

• Find a sequence of continuous functions that does not converge uniformly, but still has a pointwise limit that is continuous.

## 1.3 Exercises

• Find a function that is differentiable but not continuously differentiable.

• Prove the uniform limit theorem: a uniform limit of continuous function is continuous.

• Show that the uniform limit of bounded functions is uniformly bounded.

• Construct sequences of functions $\{ f _ { n } \} _ { n \in \mathbb { N } }$ and $\{ g _ { n } \} _ { n \in \mathbb { N } }$ which converge uniformly on some set E, and yet their product sequence $\{ h _ { n } \} _ { n \in \mathbb { N } }$ with $h _ { n } : = f _ { n } g _ { n }$ does not converge uniformly.

– Show that if $f _ { n } , g _ { n }$ are additionally bounded, then $h _ { n }$ does converge uniformly.

• Find a sequence of functions such that

$$
{ \frac { d } { d x } } \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) \neq \operatorname* { l i m } _ { n \to \infty } { \frac { d } { d x } } f _ { n } ( x )
$$

• Find a uniform limit of differentiable functions that is not differentiable.

• Prove that the Cantor set is a Borel set.

• Show the Cantor ternary set is totally disconnected; that is show it contains no nonempty open interval.

(a) Show the set of irrational numbers is a $G _ { \delta }$ set but is not an $F _ { \sigma }$ set.
Hint: Show Q is not a $G _ { \delta }$ , for otherwise you could obtain a decreasing sequence $G _ { n }$ of dense open sets that have empty intersection.
Then use the decomposition of each $G _ { n }$ into a disjoint countable union of open intervals.

(b) Using the fact that the set of rational numbers in any closed interval $a \leq x \leq b$ where $a < b$ is not a $G _ { \delta }$ set, give an example of a Borel subset of R which is neither an $F _ { \sigma }$ or a $G _ { \delta }$ set.

(c) Let f be any function from R to R. Prove that the set of points of discontinuity of f is of type $F _ { \sigma }$

(d) Can a function from R to R be continuous on the rationals and discontinuous on the irrationals?
What if the roles of the rationals and irrationals are interchanged?

I.7 Let $( x _ { n } ) _ { n \in \mathbb { N } }$ be a sequence of real numbers.
Prove that the following are equivalent.

(a) lin $\operatorname { l } _ { n \to \infty } x _ { n } = a .$

(b) Every subsequence of $( x _ { n } ) _ { n \in \mathbb { N } }$ contains a subsequence that converges to a.

## 1.4 Qual Questions

I.8 Prove: If $f \in C [ 0 , 1 ]$ and $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ( x ) e ^ { - n x } d x = 0 } \end{array}$ for all $n \in  { \mathbb { N } } _ { 0 }$ , then $f = 0$

I.14 Let f : R → R be an infinitely differentiable function.

(a) Use Taylor's formula with remainder to show that, given x and $h , f ^ { \prime } ( x ) =$ $( f ( x + 2 h ) - f ( x ) ) / 2 h - h f ^ { \prime \prime } ( \xi )$ for some ξ.

(b) Assume $f ( x ) \to 0 \mathrm { a s } x \to \infty$ , and that $f ^ { \prime \prime }$ is bounded.
Show that $f ^ { \prime } ( x )  0$ as $x \to \infty$

## 2.4 Spring 2017 # 4

Let $f ( x , y )$ on $[ - 1 , 1 ] ^ { 2 }$ be defined by

$$
f ( x , y ) = { \left\{ \begin{array} { l l } { \displaystyle { \frac { x y } { \left( x ^ { 2 } + y ^ { 2 } \right) ^ { 2 } } } } & { ( x , y ) \neq ( 0 , 0 ) } \\ { 0 } & { ( x , y ) = ( 0 , 0 ) } \end{array} \right. }
$$

Determine if f is integrable.

## 2.5 Spring 2015 # 1

Let $( X , d )$ and $( Y , \rho )$ be metric spaces, $f : X \to Y$ , and $x _ { 0 } \in X$

Prove that the following statements are equivalent:

$\varepsilon > 0 \quad \exists \delta > 0$ such that $\rho ( f ( x ) , f ( x _ { 0 } ) ) < \varepsilon$ whenever $d ( x , x _ { 0 } ) < \delta$

2The sequence $\{ f ( x _ { n } ) \} _ { n = 1 } ^ { \infty } \to f ( x _ { 0 } )$ for every sequence $\{ x _ { n } \} \to x _ { 0 }$ in  X.

## 2.1 Fall 2018 # 1

Let $f ( x ) = { \frac { 1 } { x } } .$ . Show that f is uniformly continuous on $( 1 , \infty )$ but not on $( 0 , \infty )$

$$
f _ { n } ( x ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { n } } } & { x \in ( { \frac { 1 } { 2 ^ { n + 1 } } } , { \frac { 1 } { 2 ^ { n } } } ] } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Show that $\textstyle \sum _ { n = 1 } ^ { \infty } f _ { n }$ does not satisfy the Weierstrass M-test but that it nevertheless converges uniformly on R.

4. Let $f _ { n } \colon [ 0 , 1 ) \to$ R be the function defined by

$$
f _ { n } ( x ) : = \sum _ { k = 1 } ^ { n } { \frac { x ^ { k } } { 1 + x ^ { k } } } .
$$

1. Prove that $f _ { n }$ converges to a function $f \colon [ 0 , 1 ) \to { \mathbb { R } }$

2. Prove that for every $0 < a < 1$ the convergence is uniform on $[ 0 , a ]$

3. Prove that f is differentiable on (0, 1).

$\{ r _ { n } \} _ { n = 1 } ^ { \infty }$ be any enumeration of all the rationals in [0, 1] and define $f : [ 0 , 1 ] \to \mathbb { R }$ by setting

$$
f ( x ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { n } } } & { { \mathrm { i f ~ } } x = r _ { n } } \\ { 0 } & { { \mathrm { i f ~ } } x \in [ 0 , 1 ] \setminus \mathbb { Q } } \end{array} \right. } ~ .
$$

Prove that lim $f ( x ) = 0$ for every $c \in [ 0 , 1 ]$ and conclude that set of all points at which f is x→c\
discontinuous is precisely $[ 0 , 1 ] \cap \mathbb { Q }$

6. Let

$$
g ( x ) = \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { 1 + n ^ { 2 } x } } .
$$

(a) Show that the series defining g does not converge uniformly on $( 0 , \infty )$ , but none the less still defines a continuous function on $( 0 , \infty )$ Hint for the first part: Show that $\textstyle i f \sum _ { n = 0 } ^ { \infty } g _ { n } ( x )$ converges uniformly on a set $X _ { i }$ , then the sequence of functions $\left\{ g _ { n } \right\}$ must converge uniformly to 0 on X.

(b) Is g differentiable on $( 0 , \infty ) ?$ If so, is the derivative function $g ^ { \prime }$ continuous on $( 0 , \infty ) ?$

7. Let $h _ { n } ( x ) = { \frac { x } { ( 1 + x ) ^ { n + 1 } } } .$

(a) Prove that $h _ { n }$ converges uniformly to 0 on $[ 0 , \infty )$

(b) i. Verify that

$$
\sum _ { n = 0 } ^ { \infty } h _ { n } ( x ) = { \left\{ \begin{array} { l l } { 1 { \mathrm { ~ i f ~ } } x > 0 } \\ { 0 { \mathrm { ~ i f ~ } } x = 0 } \end{array} \right. }
$$

ii.
Does $\textstyle \sum _ { n = 0 } ^ { \infty } h _ { n }$ converge uniformly on $\lbrack 0 , \infty ) ?$

(c) Prove that $\textstyle \sum _ { n = 0 } ^ { \infty } h _ { n }$ converges uniformly on $[ a , \infty )$ for any $a > 0$

exisus.

I.19 Define a function f on R by

$$
f ( x ) = \left\{ { \begin{array} { l l } { e ^ { - 1 / x ^ { 2 } } , { \mathrm { i f ~ } } x > 0 } \\ { \ 0 \quad , { \mathrm { i f ~ } } x \leq 0 } \end{array} } \right.
$$

(a) Check whether f is infinitely differentiable at 0, and, if so, find $f ^ { ( n ) } ( 0 )$ , $n = 1 , 2 , 3 , \cdots$ . Show details.

(b) Does f have a power series expansion at $0 ?$

c) Let $g ( x ) = f ( x ) f ( 1 - x )$ . Show that g is a nontrivial infinitely differentiable function on R which vanishes outside (0, 1).

A real-valued function f on an interval I for which there exists a constant C such that

$$
| f ( x ) - f ( y ) | \leq C | x - y |
$$

for all x and y in I is called a Lipschitz function.

(a) Show that a Lipschitz function is absolutely continuous.

(b) Show that an absolutely continuous function f on an interval is Lipschitz if and only if $f ^ { \prime }$ is essentially bounded.

If f is nonnegative and integrable on $[ 0 , 1 ]$ , then $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } \int _ { 0 } ^ { 1 } \sqrt [ n ] { f } = m \{ x | f ( x ) > 0 \} } \end{array}$

14. $| \textsf { f } \{ s _ { n } \}$ is a complex sequence, define its arithmetic means $\sigma _ { n }$ by

$$
\sigma _ { n } = { \frac { s _ { 0 } + s _ { 1 } + \cdot \cdot \cdot + s _ { n } } { n + 1 } } \quad ( n = 0 , 1 , 2 , \ldots )
$$

(a) If lim $s _ { n } = s ,$ prove that lim $\sigma _ { n } = s .$

(b) Construct a sequence $\left\{ s _ { n } \right\}$ which does not converges, although lim $\sigma _ { n } = 0$

Can it happen that $s _ { n } > 0$ for all n and that lim sup $s _ { n } = \infty$ , although lim $\sigma _ { n } = 0 ?$

d) Put $a _ { n } = s _ { n } - s _ { n - 1 } ,$ for $n \geq 1$ Show that

$$
s _ { n } - \sigma _ { n } = { \frac { 1 } { n + 1 } } \sum _ { k = 1 } ^ { n } k a _ { k }
$$

Assume that lim $( n a _ { n } ) = 0$ and that $\left\{ \sigma _ { n } \right\}$ converges.
Prove that $\left\{ s _ { n } \right\}$ converges.
[This gives a\
converse of (a), but under the additional assumption that $n a _ { n }  0 . ]$\
(e) Derive the last conclusion from a weaker hypothesis: Assume $M < \infty , \left| n a _ { n } \right| \leq M$ for all $n _ { \ell }$\
and lim $\sigma _ { n } = \sigma$ .Prove that lim $s _ { n } = \sigma _ { i }$ , by completing the following outline:\
If th

– Note: outline omitted!

## 3.1 Spring 2020 # 1

Prove that if $f : [ 0 , 1 ] \to \mathbb { R }$ is continuous then

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { 1 } k x ^ { k - 1 } f ( x ) d x = f ( 1 ) .
$$

## 3.4 Fall 2017 # 4

Let

$$
f _ { n } ( x ) = n x ( 1 - x ) ^ { n } , \quad n \in \mathbb { N } .
$$

a.Show that $f _ { n }  0$ pointwise but not uniformly on [0, 1].

b.Show that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } n ( 1 - x ) ^ { n } \sin { x } d x = 0
$$

Hint for (a): Consider the maximum of $f _ { n } .$

## 3.11 Fall 2020 # 1

Show that if $x _ { n }$ is a decreasing sequence of positive real numbers such that $\sum _ { n = 1 } ^ { \infty } x _ { n }$ converges, then

$$
\operatorname* { l i m } _ { n \to \infty } n x _ { n } = 0 .
$$
