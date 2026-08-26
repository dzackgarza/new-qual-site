# Math 8100 Assignment 1 Preliminaries

Due date: Tuesday the 27th of August 2019

1. The Cantor set C is the set of all $x \in [ 0 , 1 ]$ that have a ternary expansion $\textstyle x = \sum _ { k = 1 } ^ { \infty } a _ { k } 3 ^ { - k }$ with $a _ { k } \neq 1$ for all k. Thus C is obtained from [0, 1] by removing the open middle third $\left( { \frac { 1 } { 3 } } , { \frac { 2 } { 3 } } \right)$ , then removing the open middle thirds $\bigl ( { \frac { 1 } { 9 } } , { \frac { 2 } { 9 } } \bigr )$ and $\bigl ( \frac { 7 } { 9 } , \frac { 8 } { 9 } \bigr )$ of the two remaining intervals, and so forth.

(a) Find a real number x belonging to the Cantor set which is not the endpoint of one of the intervals used in its construction.

(b) Prove that C is both nowhere dense (and hence meager) and has measure zero.

(c) Prove that C is uncountable by showing that the function $\textstyle f ( x ) = \sum _ { k = 1 } ^ { \infty } b _ { k } 2 ^ { - k }$ where $b _ { k } = a _ { k } / 2 .$ maps C onto [0, 1].

2. A set $A \subseteq \mathbb { R } ^ { n }$ is called an $F _ { \sigma }$ set if it can be written as the countable union of closed subsets of $\mathbb { R } ^ { n }$ . A set $B \subseteq \mathbb { R } ^ { n }$ is called a $G _ { \delta }$ set if it can be written as the countable intersection of open subsets of $\mathbb { R } ^ { n }$

(a) Argue that a set is a $G _ { \delta }$ set if and only if its complement is an $F _ { \sigma }$ set.

(b) Show that every closed set is a $G _ { \delta }$ set and every open set is an $F _ { \sigma }$ set.

Hint: One approach is to prove that every open subset of $\mathbb { R } ^ { n }$ can be written as a countable union of closed cubes with disjoint interiors.
This approach is however very specific to open sets in $\mathbb { R } ^ { n }$

(c) Give an example of an $F _ { \sigma }$ set which is not a $G _ { \delta }$ set and a set which is neither an $F _ { \sigma }$ nor a $G _ { \delta }$ set.

3. (a) Let $\{ r _ { n } \} _ { n = 1 } ^ { \infty }$ be any enumeration of all the rationals in [0, 1] and define $f : [ 0 , 1 ] \to \mathbb { R }$ by setting

$$
f ( x ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { n } } } & { { \mathrm { i f ~ } } x = r _ { n } } \\ { 0 } & { { \mathrm { i f ~ } } x \in [ 0 , 1 ] \setminus \mathbb { Q } } \end{array} \right. } ~ .
$$

Prove that $\operatorname* { l i m } _ { x \to c } f ( x ) = 0$ for every $c \in [ 0 , 1 ]$ and conclude that set of all points at which f is discontinuous is precisely $[ 0 , 1 ] \cap \mathbb { Q }$

(b) Let $f : \mathbb { R } \to \mathbb { R }$ be bounded.

i. Recall that we defined the oscillation of f at x to be

$$
\omega _ { f } ( x ) : = \operatorname* { l i m } _ { \delta \to 0 ^ { + } } \operatorname* { s u p } _ { y , z \in B _ { \delta } ( x ) } | f ( y ) - f ( z ) | .
$$

Briefly explain why this is a well defined notion and prove that

$$
f { \mathrm { ~ i s ~ c o n t i n u o u s ~ a t ~ } } x \quad \Longleftrightarrow \quad \omega _ { f } ( x ) = 0 .
$$

ii.
Prove that for every $\varepsilon > 0$ the set $A _ { \varepsilon } = \{ x \in \mathbb { R } : \omega _ { f } ( x ) \geq \varepsilon \}$ is closed and deduce from this that the set of all points at which f is discontinuous is an $F _ { \sigma }$ set.

4. Let $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ be any enumeration of a given countable set $X \subseteq \mathbb { R }$ . For each $n \in \mathbb { N }$ define

$$
f _ { n } ( x ) = { \left\{ \begin{array} { l l } { 1 { \mathrm { ~ i f ~ } } x > x _ { n } } \\ { 0 { \mathrm { ~ i f ~ } } x \leq x _ { n } } \end{array} \right. } \quad .
$$

Prove that

$$
f ( x ) = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } f _ { n } ( x )
$$

defines an increasing function f on R that is continuous on R $\backslash X$

5. Let $C ( [ 0 , 1 ] )$ denote the collection of all real-valued continuous functions with domain $[ 0 , 1 ]$

(a) Show that $d _ { \infty } ( f , g ) = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | f ( x ) - g ( x ) |$ defines a metric on $C ( [ 0 , 1 ] )$ and that with the “uniform” metric $C ( [ 0 , 1 ] )$ is in fact a complete metric space.

(b) Prove that the unit ball $\{ f \in C ( [ 0 , 1 ] ) : d _ { \infty } ( f , 0 ) \leq 1 \}$ is closed and bounded, but not compact.

(c) \*\* Challenge: Can you show that $C ( [ 0 , 1 ] )$ with the metric $d _ { \infty }$ is not totally bounded.

A set is totally bounded if, for every $\varepsilon > 0$ , it can be covered by finitely many balls of radius ε.

6. Let

$$
g ( x ) = \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { 1 + n ^ { 2 } x } } .
$$

(a) Show that the series defining g does not converge uniformly on $( 0 , \infty )$ , but none the less still defines a continuous function on $( 0 , \infty )$ Hint for the first part: Show that $\textstyle i f \sum _ { n = 0 } ^ { \infty } g _ { n } ( x )$ converges uniformly on a set X, then the sequence of functions $\left\{ g _ { n } \right\}$ must converge uniformly to 0 on X.

(b) Is g differentiable on $( 0 , \infty ) ?$ If so, is the derivative function $g ^ { \prime }$ continuous on $( 0 , \infty ) ?$

7. Let $h _ { n } ( x ) = \frac { x } { ( 1 + x ) ^ { n + 1 } } .$

(a) Prove that $h _ { n }$ converges uniformly to 0 on $[ 0 , \infty )$

(b) i. Verify that

$$
\sum _ { n = 0 } ^ { \infty } h _ { n } ( x ) = { \left\{ \begin{array} { l l } { 1 { \mathrm { ~ i f ~ } } x > 0 } \\ { 0 { \mathrm { ~ i f ~ } } x = 0 } \end{array} \right. }
$$

ii.
Does $\textstyle \sum _ { n = 0 } ^ { \infty } h _ { n }$ converge uniformly on $\lbrack 0 , \infty ) ?$

(c) Prove that $\textstyle \sum _ { n = 0 } ^ { \infty } h _ { n }$ converges uniformly on $[ a , \infty )$ for any $a > 0$

## Extra Challenge Problems Not to be handed in with the assignment

1. Given an arbitrary $F _ { \sigma }$ set $V ,$ can you produce a function whose discontinuities lie precisely in $V ?$ Hint: First try to do this for an arbitrary closed set.

2. (Baire Category Theorem) Prove that if X is a non-empty complete metric space, then X cannot be written as a countable union of nowhere dense sets.

Hint: Modify the proof given in class of the special case $X = \mathbb { R }$ replacing the use of the nested interval property with the following fact (which you should prove):

If $F _ { 1 } \supseteq F _ { 2 } \supseteq \cdots$ is a nested sequence of closed non-empty and bounded sets in a complete metric space X with lim diam $F _ { n } = 0$ , then $\bigcap _ { n = 1 } ^ { \infty } F _ { n }$ contains exactly one point.
n→∞

3. Complete the proof, sketched in class, of the so-called Lebesgue Criterion: A bounded function on an interval $[ a , b ]$ is Riemann integrable if and only if its set of discontinuities has measure zero.

(a) Prove that if the set of discontinuities of f has measure zero, then f is Riemann integrable.
[Hint: Let $\varepsilon > 0$ . Cover the compact set $A _ { \varepsilon }$ (defined in $Q \mathcal { B } ( b ) i i .$ . above) by a finite number of open intervals whose total length $i s \le \varepsilon$ . Select and appropriate partition of $[ a , b ]$ and estimate the difference between the upper and lower sums of f over this partition.]

(b) Prove that if f is Riemann integrable on $[ a , b ]$ , then its set of discontinuities has measure zero.
[Hint: The set of discontinuities of f is contained in $\cup _ { n } A _ { 1 / n }$ . Given $\varepsilon > 0$ , choose a partition P such that $U ( f , P ) - L ( f , P ) < \varepsilon / n$ . Show that the total length of the intervals in P whose interiors intersect $A _ { 1 / n } \ i s \leq \varepsilon . \ ]$
