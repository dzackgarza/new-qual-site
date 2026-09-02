## Day 4: Continuity of functions

Proposition 3.1 ([KRD10, Thm. 5.3.1]). For a function f : $E \subset \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ the following are equivalent:

1) f is continuous on E

2) For any $x \in E$ and $\epsilon > 0$ there exists some $\delta > 0$ such that $| | f ( y ) - f ( x ) | | < \epsilon$ for all $y \in E$ with $| | x - y | | < \delta$

3) For every convergent sequence $\{ x _ { n } \} \subset E$ with $\quad \operatorname* { l i m } _ { n \to \infty } x _ { n } = x \in E$ , li $\mathrm { n } _ { n \to \infty } f ( x _ { n } ) = f ( x )$

4) For every open set $G \subset \mathbb { R } ^ { m }$ the set $f ^ { - 1 } ( G )$ is open in E (with the subspace topology).

Theorem 3.2 (Extreme Value Theorem / c.f. [Rud76, Thms. 4.14,15]). $I f f : K \subset \mathbb { R } ^ { n } \to \mathbb { R } ^ { m }$ is continuous and K is compact, then $f ( K )$ is compact. In particular, given any continuous function $f : [ a , b ] \subset \mathbb { R } $ R there exist points $p , q \in [ a , b ]$ so that $f ( p ) = \operatorname* { s u p } _ { [ a , b ] } f ( x )$ and $f ( q ) = \operatorname* { i n f } _ { [ a , b ] } f ( x )$

Theorem 3.3 (c.f. [Rud76, Thm. 4.19]). $I f f : K \subset \mathbb { R } ^ { n } \to \mathbb { R } ^ { m }$ is continuous and K is compact, then f is uniformly continuous on K.

Theorem 3.4 (Intermediate Value Theorem / c.f. [Rud76, Thm. 4.23]). $I f f : [ a , b ] \subset \mathbb { R } \to \mathbb { R }$ is continuous and $f ( a ) < f ( b )$ , then for any real number x such that $f ( a ) < x < f ( b )$ there exists some $c \in ( a , b )$ such that $f ( c ) = x$

Theorem 3.5 (c.f. [Rud76, Thms. 4.29,30]). $I f f : ( a , b ) \to \mathbb { R }$ is monotonic then f is discontinuous on a set $E \subset \left( a , b \right)$ which is at most countable. Further, each point where f is discontinuous is a jump discontinuity in that the limits $f ( x _ { i } - )$ and $f ( x _ { i } + )$ both exist for each $x _ { i } \in E$

In showing continuity directly from the -δ definition it is often helpful to recall the factorizations

$$
x ^ { 2 } - y ^ { 2 } = ( x - y ) ( x + y )
$$

$$
x ^ { 3 } - y ^ { 3 } = ( x - y ) ( x ^ { 2 } + x y + y ^ { 2 } ) .
$$

Often, these will need to be manipulated to fit the problem at hand.

## Warm-up problems.

1) State the definition of uniform continuity. Give an example of a function $f : ( 0 , 1 ) $ R which is continuous but not uniformly continuous.

2) (c.f. June 2012 #1b) If $f : [ 0 , 1 ] \to [ 0 , 1 ]$ is continuous, show that $f ( x ) = x$ for some $x \in [ 0 , 1 ]$

3) Give an -δ proof that $f ( x ) = x ^ { 1 / 3 }$ is continuous on [0, 1].

(You may also wish to try this for $f ( x ) = { \sqrt { x } }$ and/or on the interval $[ 0 , \infty )$ as in June 2011 and others.)

4) (June 2013 #1b) Prove that $\begin{array} { r } { \operatorname* { l i m } _ { x \to - \infty } \frac { x - 1 } { x } = 1 } \end{array}$

5) A useful lemma: Let $\{ x _ { n } \}$ be a real sequence with lim in $\mathrm { f } _ { n  \infty } x _ { n }$ , lim $\textstyle \operatorname* { s u p } _ { n \to \infty } x _ { n } \in \mathbb { R }$ . Show that for any $\epsilon > 0$ there exists some $N \in \mathbb N$ so that

$$
\left( \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } x _ { n } \right) - \epsilon < x _ { n } < \left( \operatorname* { l i m } _ { n \to \infty } x _ { n } \right) + \epsilon \quad { \mathrm { ~ f o r ~ a l l ~ } } n \geq N .
$$

What does this result imply if lim s $\begin{array} { r } { \operatorname { l p } _ { n \to \infty } x _ { n } < L ? } \end{array}$

Problems.

6) (January 2009 $\# 2 \mathrm { a }$ , obfuscated) Is f (x) = ln x uniformly continuous on $( 0 , 1 ] ?$ Prove your answer.

(You may also wish to try the same question with $f ( x ) = \sin ( 1 / x )$ on $( 0 , \pi ] . )$

7) (c.f. January 2007 #3a, June 2010 #2a) Prove Theorem 3.2 for a function $f : K \subset \mathbb { R } \to \mathbb { R }$ (The proof is nearly unchanged when n or m is greater than 1.)

8) (June 2009 #1) Give an -δ proof that $f ( x ) = { \frac { x ^ { 2 } } { 1 - x ^ { 2 } } }$ is continuous on (0, 1). Is f uniformly continuous on $( 0 , 1 ) ?$ Prove your answer.

9) Suppose that $f : [ a , b ]  \mathbb { R }$ is continuous and define $M : [ a , b ] \to \mathbb { R }$ by

$$
M ( x ) = \operatorname* { s u p } \{ f ( y ) : a \leq y \leq x \} .
$$

Show that M is continuous on $[ a , b ]$

10) ([KRD10, 5.6.H]) Show that a continuous function $f : \mathbb { R }  \mathbb { R }$ cannot take on every real value exactly twice.

11) (June 2013 #5b) Let (X, d) be a complete metric space, $A \subset X$ be a bounded set, and $F : X \to X$ . Assume there exists some $k > 0$ such that $d ( F ( a ) , F ( b ) ) \leq k d ( a , b )$ for all $a , b \in X$ and that $A \subset F ( A )$ . Provide a description of A if $k < 1$ . Can anything be said about A if $k \geq 1 ?$

## More problems.

12) (January 2012 #1b) Let $y \in \mathbb { R }$ and $f : \mathbb { R } $ R be given. Suppose that for every sequence $\{ x _ { n } \}$ we have lim i $\begin{array} { r } { \operatorname* { m f } _ { n \to \infty } | f ( x _ { n } ) - f ( y ) | \leq \operatorname* { l i m } \operatorname* { i n f } _ { n \to \infty } | x _ { n } - y | } \end{array}$ . Prove that $f$ is continuous at y.

13) Prove Theorem 3.3.

14) Prove Theorem 3.4.

## References

[KRD10] Allan P. Donsig Kenneth R. Davidson. Real analysis and applications. Springer, 2010.

[Rud76] Walter Rudin. Principles of mathematical analysis. McGraw-Hill, Inc., USA, third edition, 1976.