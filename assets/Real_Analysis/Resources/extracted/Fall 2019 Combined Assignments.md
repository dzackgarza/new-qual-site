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

# Math 8100 Assignment 2 Lebesgue measure and outer measure

Due date: Wednesday the 5th of September 2018

1. Prove that if $E \subseteq \mathbb { R }$ with $m _ { * } ( E ) = 0$ , then $E ^ { 2 } : = \{ x ^ { 2 } | x \in E \}$ also has Lebesgue outer measure zero.

Hint: First consider the case when E is a bounded subset of R.

[To what extent can you generalize this result? ]

2. Prove that if $E _ { 1 }$ and $E _ { 2 }$ are measurable subsets of $\mathbb { R } ^ { n }$ , then

$$
m ( E _ { 1 } \cup E _ { 2 } ) + m ( E _ { 1 } \cap E _ { 2 } ) = m ( E _ { 1 } ) + m ( E _ { 2 } ) .
$$

3. Suppose that $A \subseteq E \subseteq B$ , where A and B are Lebesgue measurable subsets on $\mathbb { R } ^ { n }$

(a) Prove that if $m ( A ) = m ( B ) < \infty ,$ , then E is measurable.

(b) Give an example showing that the same conclusion does not hold if A and B have infinite measure.

4. Suppose A and B are a pair of compact subsets of $\mathbb { R } ^ { n }$ with $A \subseteq B ,$ , and let $a = m ( A )$ and $b = m ( B )$ Prove that for any c with $a < c < b$ , there is a compact set E with $A \subseteq E \subseteq B$ and $m ( E ) = c .$

Hint: As a warm-up example, consider the one dimensional example where A a compact measurable subset of $B : = [ 0 , 1 ]$ and the quantity m $\ u ( A ) + t - m ( A \cap [ 0 , t ] )$ as a function of t.

5. Let N denote the non-measurable subset of [0, 1] that was constructed in lecture.

(a) Prove that if E is a measurable subset of ${ \mathcal { N } } _ { : }$ , then $m ( E ) = 0$

(b) Show that $m _ { * } ( [ 0 , 1 ] \setminus N ) = 1$

[Hint: Argue by contradiction and pick an open set G such that $[ 0 , 1 ] \setminus { \mathcal { N } } \subseteq G \subseteq [ 0 , 1 ]$ with $m _ { * } ( G ) \leq 1 - \varepsilon . ]$

(c) Conclude that there exists disjoint sets $E _ { 1 } \subseteq [ 0 , 1 ]$ and $E _ { 2 } \subseteq [ 0 , 1 ]$ for which

$$
m _ { * } ( E _ { 1 } \cup E _ { 2 } ) \neq m _ { * } ( E _ { 1 } ) + m _ { * } ( E _ { 2 } ) .
$$

6. (a) The Borel-Cantelli Lemma.
   Suppose $\{ E _ { j } \} _ { j = 1 } ^ { \infty }$ is a countable family of measurable subsets of $\mathbb { R } ^ { n }$ and that

$$
\sum _ { j = 1 } ^ { \infty } m ( E _ { j } ) < \infty .
$$

Let

$$
E = \operatorname* { l i m } _ { j \to \infty } \operatorname* { s u p } _ { } E _ { j } : = \{ x \in \mathbb { R } ^ { n } : x \in E _ { j } , { \mathrm { ~ f o r ~ i n f i n i t e l y ~ m a n y ~ } } j \} .
$$

Show that E is measurable and that m $( E ) = 0 ,$ . Hint: Write $E = \cap _ { k = 1 } ^ { \infty } \cup _ { j \geq k } E _ { j }$

(b) Given any irrational x one can show (using the pigeonhole principle, for example) that there exists infinitely many fractions $a / q$ , with a and q relatively prime integers, such that

$$
\left| x - { \frac { a } { q } } \right| \leq { \frac { 1 } { q ^ { 2 } } } .
$$

However, show that the set of those $x \in \mathbb { R }$ such that there exists infinitely many fractions $a / q ,$ with a and q relatively prime integers, such that

$$
\left| x - { \frac { a } { q } } \right| \leq { \frac { 1 } { q ^ { 3 } } }
$$

is a set of Lebesgue measure zero.

# Extra Challenge Problems Not to be handed in with the assignment

1. Prove that any $E \subset \mathbb { R }$ with $m _ { * } ( E ) > 0$ necessarily contains a non-measurable set.

2. The outer Jordan content $J _ { * } ( E )$ of a set E in R is defined by

$$
J _ { * } ( E ) = \operatorname* { i n f } \sum _ { j = 1 } ^ { N } | I _ { j } | ,
$$

where the infimum is taken over every finite covering $E \subseteq \cup _ { j = 1 } ^ { N } I _ { j }$ , by intervals $I _ { j }$

(a) Prove that $J _ { * } ( E ) = J _ { * } ( \bar { E } )$ for every set E (here E¯ denotes the closure of $E )$

(b) Exhibit a countable subset $E \subseteq [ 0 , 1 ]$ such that $J _ { * } ( E ) = 1$ while $m _ { * } ( E ) = 0$

3. If I is a bounded interval and $\alpha \in ( 0 , 1 )$ , let us call the open interval with the same midpoint as I and length equal to α times the length of I the “open middle $\alpha \mathrm { t h } ^ { \dag }$ of I . If $\{ \alpha _ { j } \} _ { j = 1 } ^ { \infty }$ is any sequence of numbers in (0, 1), then, we can define a decreasing sequence $\{ K _ { j } \}$ of closed sets as follows: $K _ { 0 } = [ 0 , 1 ]$ ], and $K _ { j }$ is obtained by removing the the open middle $\alpha _ { j }$ th from each of the intervals that make up $K _ { j - 1 }$ . The resulting limiting set $\begin{array} { r } { K = \bigcap _ { j = 1 } ^ { \infty } K _ { j } } \end{array}$ is called a generalized Cantor set.

(a) Suppose $\{ \alpha _ { j } \} _ { j = 1 } ^ { \infty }$ is any sequence of numbers in (0, 1).

i. Prove that $\textstyle \prod _ { j = 1 } ^ { \infty } ( 1 - \alpha _ { j } ) > 0$ if and only if $\textstyle \sum _ { j = 1 } ^ { \infty } \alpha _ { j } < \infty$

ii.
Given $\beta \in ( 0 , 1 )$ , exhibit a sequence $\{ \alpha _ { j } \}$ such that $\begin{array} { r } { \prod _ { j = 1 } ^ { \infty } ( 1 - \alpha _ { j } ) = \beta _ { } } \end{array}$

(b) Given $\beta \in ( 0 , 1 )$ , construct an open set G in [0, 1] whose boundary has Lebesgue measure $\beta .$

Hint: Every closed nowhere dense set is the boundary of an open set.

# Math 8100 Assignment 3 Lebesgue measurable sets and functions

Due date: 5:00 pm Friday the 20th of September 2019

1. (a) Prove that for every $E \subseteq \mathbb { R } ^ { n }$ there exists a Borel set $B \supseteq E$ with the property that $m ( B ) = m _ { * } ( E )$

(b) Prove that if $E \subseteq \mathbb { R } ^ { n }$ is Lebesgue measurable, then there exists a Borel set $B \subseteq E$ with the property that $m ( B ) = m ( E )$

(c) Prove that if $E \subseteq \mathbb { R } ^ { n }$ is Lebesgue measurable with $m ( E ) < \infty$ , then for every $\varepsilon > 0$ there exists a set A that is a finite union of closed cubes such that $m ( E { \triangle } A ) < \varepsilon$

[Recall that $E \triangle A$ stands for the symmetric difference, defined by $E \triangle A = ( E \setminus A ) \cup ( A \setminus E ) ]$

2. Let E be a Lebesgue measurable subset of $\mathbb { R } ^ { n }$ with $m ( E ) > 0$ and $\varepsilon > 0$

(a) Prove that E “almost” contains a closed cube in the sense that there exists a closed cube $Q$ such that $m ( E \cap Q ) \geq ( 1 - \varepsilon ) m ( Q )$

(b) Prove that the so-called difference set $E - E : = \{ d : d = x - y$ with $x , y \in E \}$ necessarily contains an open ball centered at the origin.

Hint: It may be useful to observe that $d \in E - E \Longleftrightarrow E \cap ( E + d ) \neq \emptyset$

3. We say that a function $f : \mathbb { R } ^ { n }  \mathbb { R }$ is upper semicontinuous at a point x in $\mathbb { R } ^ { n }$ if

$$
f ( x ) \geq \operatorname* { l i m } _ { y \to x } f ( y ) .
$$

Prove that if $f$ is upper semicontinuous at every point x in $\mathbb { R } ^ { n }$ , then $f$ is Borel measurable.

4. Let $\left\{ f _ { n } \right\}$ be a sequence of measurable functions on $\mathbb { R } ^ { n }$ . Prove that $\{ x \in \mathbb { R } ^ { n } : \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ exists} defines a measurable set.

5. Recall that the Cantor set $\mathcal { C }$ is the set of all $x \in [ 0 , 1 ]$ that have a ternary expansion $\textstyle x = \sum _ { k = 1 } ^ { \infty } a _ { k } 3 ^ { - k }$ with $a _ { k } \neq 1$ for all k. Consider the function

$$
f ( x ) = \sum _ { k = 1 } ^ { \infty } b _ { k } 2 ^ { - k } \mathrm { w h e r e } b _ { k } = a _ { k } / 2 .
$$

(a) Show that f is well defined and continuous on ${ \mathcal { C } } ,$ and moreover $f ( 0 ) = 0$ as well as $f ( 1 ) = 1$

(b) Prove that there exists a continuous function that maps a measurable set to a non-measurable set.

6. Let us examine the map f defined in Question 5 even more closely.
   One readily sees that if $x , y \in { \mathcal { C } }$ and $x < y .$ , then $f \left( x \right) < f \left( y \right)$ unless x and y are the two endpoints of one of the intervals removed from [0, 1] to obtain C. In this case $f ( x ) = \ell 2 ^ { m }$ for some integers \` and m, and $f ( x )$ and $f ( y )$ are the two binary expansions of this number.
   We can therefore extend f to a map $F : [ 0 , 1 ]  [ 0 , 1 ]$ by declaring it to be constant on each interval missing from C. F is called the Cantor-Lebesgue function.

(a) Prove that F is non-decreasing and continuous.

(b) Let $G ( x ) = F ( x ) + x$ . Show that G is a bijection from [0, 1] to [0, 2].

(c) i. Show that $m ( G ( \mathcal { C } ) ) = 1$

ii.
By considering rational translates of $\mathcal { N }$ (the non-measurable subset of [0, 1] that we constructed in class), prove that $G ( \mathcal { C } )$ necessarily contains a (Lebesgue) non-measurable set $\mathcal { N } ^ { \prime }$ iii.
Let $E = G ^ { - 1 } ( \mathcal { N } ^ { \prime } )$ . Show that E is Lebesgue measurable, but not Borel.

(d) Give an example of a measurable function ϕ such that $\varphi \circ G ^ { - 1 }$ is not measurable.

Hint: Let $\varphi$ be the characteristic function of a null set whose image under G is not measurable.

## Extra Challenge Problems Not to be handed in with the assignment

1. Let $\chi _ { [ 0 , 1 ] }$ be the characteristic function of [0, 1]. Show that there is no function f satisfying $f = \chi _ { [ 0 , 1 ] }$ almost everywhere which is also continuous on all of R.

2. Question 6d above supplies us with an example that if f and g are Lebesgue measurable, then it does not necessarily follow that $f \circ g$ will be Lebesgue measurable, even if $g$ is assumed to be continuous.
   Prove that if f is Borel measurable, then $f \circ g$ will be Lebesgue or Borel measurable whenever g is.

3. Let f be a measurable function on [0, 1] with $| f ( x ) | < \infty$ for a.e. x. Prove that there exists a sequence of continuous functions $\left\{ g _ { n } \right\}$ on [0, 1] such that $g _ { n }  f$ for a.e. $x \in [ 0 , 1 ]$

# Math 8100 Assignment 4 Lebesgue Integration

Due date: Tuesday the 1st of October 2019

Definition.
Let E be a Lebesgue measurable subset of $\mathbb { R } ^ { n }$

We say that a measurable function $f : E \to \mathbb { C }$ is integrable on E if $\int _ { E } \left| f ( x ) \right| d x < \infty ,$

1. (a) Give an example of a continuous integrable function f on R for which $f ( x ) \not \to 0 { \mathrm { ~ a s ~ } } | x | \to \infty$

(b) Prove that if $f$ is integrable on R and uniformly continuous, then $\operatorname* { l i m } _ { | x | \to \infty } f ( x ) = 0$

2. Let f be an integrable function on $\mathbb { R } ^ { n }$

(a) Prove that $\{ x : | f ( x ) | = \infty \}$ has measure equal to zero.

(b) Let $\varepsilon > 0$ . Prove that there exists a measurable set E with $m ( E ) < \infty$ for which

$$
\int _ { E } | f | > \left( \int | f | \right) - \varepsilon .
$$

3. Let f be a function in $L ^ { + } ( \mathbb { R } ^ { n } )$ that is finite almost everywhere.

Let $E _ { 2 ^ { k } } = \{ x : f ( x ) > 2 ^ { k } \} { \mathrm { , ~ } } F _ { k } = \{ x : 2 ^ { k } < f ( x ) \leq 2 ^ { k + 1 } \}$ , and note that since f is finite almost everywhere it follows that $\bigcup _ { k = - \infty } ^ { \infty } F _ { k } = \{ x : f ( x ) > 0 \}$ , and the sets $F _ { k }$ are disjoint.
Prove that

$$
\int f ( x ) < \infty \iff \sum _ { k = - \infty } ^ { \infty } 2 ^ { k } m ( F _ { k } ) < \infty \iff \sum _ { k = - \infty } ^ { \infty } 2 ^ { k } m ( E _ { 2 ^ { k } } ) < \infty .
$$

4. Prove the following:

(a)

$$
\int _ { \{ x \in \mathbb { R } ^ { n } : | x | \leq 1 \} } | x | ^ { - p } d x < \infty \quad { \mathrm { i f ~ a n d ~ o n l y ~ i f } } \quad p < n .
$$

(b)

$$
\int _ { \{ x \in \mathbb { R } ^ { n } : | x | \geq 1 \} } | x | ^ { - p } d x < \infty \quad { \mathrm { i f ~ a n d ~ o n l y ~ i f } } \quad p > n .
$$

Hint: One possible approach is to use the first equivalence in Question 3 above.
I suggest however that in this case you also try simply writing $\mathbb { R } ^ { n }$ as a disjoint union of the annuli $A _ { k } = \{ \bar { 2 } ^ { k } < | x | \leq 2 ^ { k + 1 } \}$

5. Given any integrable function f on $\mathbb { R } ^ { n }$ , the Fourier transform of f is defined by

$$
{ \widehat { f } } ( \xi ) = \int _ { \mathbb { R } ^ { n } } f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x
$$

where $x \cdot \xi = x _ { 1 } \xi _ { 1 } + \cdot \cdot \cdot + x _ { n } \xi _ { n }$ . Show that $\widehat { f }$ is a bounded continuous function of $\xi .$ .

6. Let $\{ f _ { k } \}$ be a sequence of integrable functions on $\mathbb { R } ^ { n } , f$ be integrable on $\mathbb { R } ^ { n }$ , and $\operatorname* { l i m } _ { k \to \infty } f _ { k } = f { \mathrm { ~ a . e } }$

(a) Suppose further that

$$
\operatorname* { l i m } _ { k \to \infty } \int | f _ { k } ( x ) | d x = A < \infty \qquad { \mathrm { a n d } } \qquad \int | f ( x ) | d x = B .
$$

i. Prove that

$$
\operatorname* { l i m } _ { k \to \infty } \int | f _ { k } ( x ) - f ( x ) | d x = A - B .
$$

Hint: Use the fact that

$$
| f _ { k } ( x ) | - | f ( x ) | \leq | f _ { k } ( x ) - f ( x ) | \leq | f _ { k } ( x ) | + | f ( x ) | .
$$

ii.
Give an example of a sequence $\{ f _ { k } \}$ of such functions for which $A \neq B .$

(b) Deduce that

$$
\int | f - f _ { k } | \to 0 \quad \Longleftrightarrow \quad \int | f _ { k } | \to \int | f | .
$$

7. (a) Suppose that $f ( x )$ and $x f ( x )$ are both integrable functions on R. Prove that the function

$$
F ( t ) = \int _ { \mathbb { R } } f ( x ) \cos ( t x ) d x .
$$

is differentiable at every t and find a formula for $F ^ { \prime } ( t )$

(b) Giving complete justification, evaluate

$$
\operatorname* { l i m } _ { t \to 0 } \int _ { 0 } ^ { 1 } { \frac { e ^ { t { \sqrt { x } } } - 1 } { t } } d x .
$$

## Extra Challenge Problems

## Not to be handed in with the assignment

1. Assume Fatou’s theorem and deduce the monotone convergence theorem from it.

2. A sequence $\{ f _ { k } \}$ of integrable functions on $\mathbb { R } ^ { n }$ is said to converge in measure to f if for every $\varepsilon > 0 .$

$$
\operatorname* { l i m } _ { k \to \infty } m ( \{ x \in \mathbb { R } ^ { n } : | f _ { k } ( x ) - f ( x ) | \geq \varepsilon \} ) = 0 .
$$

(a) Prove that if $f _ { k }  f$ in $L ^ { 1 }$ then $f _ { k }  f$ in measure.

(b) Give an example to show that the converse of Question 2a is false.

(c) Prove that if we make the additional assumption that there exists an integrable function g such that $| f _ { k } | \le g$ for all k, then $f _ { k }  f$ in measure implies that

i. \* (Bonus points) $f \in L ^ { 1 }$

Hint: First show that $\{ f _ { k } \}$ contains a subsequence which converges to f almost everywhere.
ii.
$f _ { k }  f$ in L 1 .

Hint: Try using absolute continuity and “small tails property” of the Lebesgue integral.

3. Let $\Omega \subseteq \mathbb { R } ^ { n }$ be measurable with $m ( \Omega ) < \infty$ . A set $\Phi \subseteq L ^ { 1 } ( \Omega )$ is said to be uniformly integrable if, for any $\varepsilon > 0$ there exists $\delta > 0$ such that whenever $f \in \Phi$ and $E \subseteq \Omega$ is measurable with $m ( E ) < \delta _ { \mathrm { { \scriptsize { i } } } }$ , then

$$
\int _ { E } \left| f ( x ) \right| d x < \varepsilon .
$$

(a) Prove that if $f \in L ^ { 1 } ( \Omega )$ and $\{ f _ { k } \}$ is a uniformly integrable sequence of functions in $L ^ { 1 } ( \Omega )$ such that $f _ { k }  f$ almost everywhere on Ω, then $f _ { k }  f$ in $L ^ { 1 } ( \Omega )$ .

(b) Is it necessary to assume that $f \in L ^ { 1 } ( \Omega ) \colon$

# Math 8100 Assignment 5 Repeated Integration

Due date: Friday the 18th of October 2019

1. Prove that if $\{ a _ { j k } \} _ { ( j , k ) \in \mathbb { N } \times \mathbb { N } }$ is a “double sequence” with $a _ { j k } \geq 0$ for all $( j , k ) \in \mathbb { N } \times \mathbb { N }$ , then

$$
\sum _ { j = 1 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } a _ { j k } = \operatorname* { s u p } { \Bigl \{ } \sum _ { ( j , k ) \in B } a _ { j k } : B { \mathrm { ~ i s ~ a ~ f i n i t e ~ s u b s e t ~ o f ~ N } } \times \mathbb { N } { \Bigr \} }
$$

and deduce from this that

$$
\sum _ { j = 1 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } a _ { j k } = \sum _ { k = 1 } ^ { \infty } \sum _ { j = 1 } ^ { \infty } a _ { j k } .
$$

This conclusion holds more generally provided $\sum _ { j = 1 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } \left| a _ { j k } \right| < \infty ,$ , see Theorem 8.3 in “Baby Rudin”.

2. Let $f \in L ^ { 1 } ( [ 0 , 1 ] )$ , and for each $x \in [ 0 , 1 ]$ define

$$
g ( x ) = \int _ { x } ^ { 1 } { \frac { f ( t ) } { t } } d t .
$$

Show that $g \in L ^ { 1 } ( [ 0 , 1 ] )$ and that

$$
\int _ { 0 } ^ { 1 } g ( x ) d x = \int _ { 0 } ^ { 1 } f ( x ) d x .
$$

3. Carefully prove that if we define

$$
f ( x , y ) : = \left\{ { \begin{array} { l l } { \displaystyle { \frac { x ^ { 1 / 3 } } { \left( 1 + x y \right) ^ { 3 / 2 } } } } & { { \mathrm { ~ i f ~ } } 0 \leq x \leq y } \\ { 0 } & { { \mathrm { ~ o t h e r w i s e } } } \end{array} } \right.
$$

for each $( x , y ) \in \mathbb { R } ^ { 2 }$ , then f defines a function in $L ^ { 1 } ( \mathbb { R } ^ { 2 } )$

4. Let $A , B \subseteq \mathbb { R } ^ { n }$ be bounded measurable sets with positive Lebesgue measure.
   For each $t \in \mathbb { R } ^ { n }$ define the function

$$
g ( t ) = m \left( A \cap ( t - B ) \right)
$$

where $t - B = \{ t - b : b \in B \}$

(a) Prove that g is a continuous function and

$$
\int _ { \mathbb { R } ^ { n } } g ( t ) d t = m ( A ) m ( B ) .
$$

(b) Conclude that the sumset

$$
A + B = \left\{ a + b : a \in A { \mathrm { ~ a n d ~ } } b \in B \right\}
$$

contains a non-empty open subset of $\mathbb { R } ^ { n }$

5. Let $f , g \in L ^ { 1 } ( [ 0 , 1 ] )$ and for each $0 \leq x \leq 1$ define

$$
F ( x ) : = \int _ { 0 } ^ { x } f ( y ) d y \quad { \mathrm { a n d } } \quad G ( x ) : = \int _ { 0 } ^ { x } g ( y ) d y .
$$

Prove that

$$
\int _ { 0 } ^ { 1 } F ( x ) g ( x ) d x = F ( 1 ) G ( 1 ) - \int _ { 0 } ^ { 1 } f ( x ) G ( x ) d x .
$$

6. Let $f \in L ^ { 1 } ( \mathbb { R } )$ ). For any $h > 0$ we define

$$
A _ { h } ( f ) ( x ) : = { \frac { 1 } { 2 h } } \int _ { x - h } ^ { x + h } f ( y ) d y
$$

(a) Prove that for all $h > 0$

$$
\int _ { \mathbb { R } } \left| A _ { h } ( f ) ( x ) \right| d x \leq \int _ { \mathbb { R } } \left| f ( x ) \right| d x .
$$

(b) Prove that

$$
\operatorname* { l i m } _ { h \to 0 ^ { + } } \int _ { \mathbb { R } } | A _ { h } ( f ) ( x ) - f ( x ) | d x = 0 .
$$

One can in fact show that lim $\begin{array} { r } { { 1 } _ { h \to 0 ^ { + } } A _ { h } ( f ) = f } \end{array}$ almost everywhere.
This result is actually equivalent to the Lebesgue Density Theorem in R and we will establish this later in the course.

## Extra Challenge Problems

Not to be handed in with the assignment

1. (a) Prove that

$$
\int _ { 0 } ^ { \infty } \left| { \frac { \sin { x } } { x } } \right| d x = \infty .
$$

(b) By considering the iterated integral

$$
\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { \infty } x e ^ { - x y } ( 1 - \cos y ) d y \right) d x
$$

show (with justification) that

$$
\operatorname* { l i m } _ { A  \infty } \int _ { 0 } ^ { A } { \frac { \sin x } { x } } d x = { \frac { \pi } { 2 } } .
$$

2. Suppose that $F$ is a closed subset of R whose complement has finite measure.
   Let $\delta ( x )$ denote the distance from x to $F ,$ namely

$$
\delta ( x ) = d ( x , F ) = \operatorname* { i n f } \left\{ | x - y | : y \in F \right\}
$$

and

$$
I _ { F } ( x ) = \int _ { - \infty } ^ { \infty } { \frac { \delta ( y ) } { | x - y | ^ { 2 } } } d y .
$$

(a) Prove that δ is continuous, by showing that it satisfies the Lipschitz condition $| \delta ( x ) - \delta ( y ) | \leq | x - y |$

(b) Show that $I _ { F } ( x ) = \infty$ if x /∈ F .

(c) Show that $I _ { F } ( x ) < \infty$ for a.e. $x \in F$ , by showing that $\textstyle \int _ { F } I _ { F } ( x ) d x < \infty$

# Math 8100 Assignment 6 The Fourier Transform

Due date: Thursday the 31st of October 2019

Recall that we have defined the Fourier transform of an integrable function f on $\mathbb { R } ^ { n }$ by

$$
{ \widehat { f } } ( \xi ) = \int _ { \mathbb { R } ^ { n } } f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x
$$

where $x \cdot \xi = x _ { 1 } \xi _ { 1 } + \cdot \cdot \cdot + x _ { n } \xi _ { n }$ and the convolution of two integrable functions f and g on $\mathbb { R } ^ { n }$ by

$$
f * g ( x ) = \int _ { \mathbb { R } ^ { n } } f ( x - y ) g ( y ) d y .
$$

1. Prove that if $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ , then ${ \widehat { f } } ( \xi ) \to 0 { \mathrm { ~ a s ~ } } | \xi | \to \infty$ . (This is called the Riemann-Lebesgue lemma.)

Hint: Write $\begin{array} { r } { \widehat { f } ( \xi ) = \frac { 1 } { 2 } \int [ f ( x ) - f ( x - \xi ^ { \prime } ) ] e ^ { - 2 \pi i x \cdot \xi } d x } \end{array}$ , where $\begin{array} { r } { \xi ^ { \prime } = \frac { \xi } { 2 | \xi | ^ { 2 } } } \end{array}$

2. (a) Prove that if $f , g \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ , then ${ \widehat { f * g } } ( \xi ) = { \widehat { f } } ( \xi ) { \widehat { g } } ( \xi )$ for all $\xi \in \mathbb { R } ^ { n }$

(b) Conclude from part (a) that

i. if $f , g , h \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ , then $f * g = g * f$ and $( f * g ) * h = f * ( g * h )$ almost everywhere.

ii.
there does not exist $I \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ such that $f * I = f$ almost everywhere for all $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$

3. Let $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$

(a) Show that if $y \in \mathbb { R } ^ { n }$ and

i. $g ( x ) = f ( x - y )$ for all $x \in \mathbb { R } ^ { n }$ , then ${ \widehat { g } } ( \xi ) = e ^ { - 2 \pi i y \cdot \xi } { \widehat { f } } ( \xi )$ for all $\xi \in \mathbb { R } ^ { n }$

ii.
$h ( x ) = e ^ { 2 \pi i x \cdot y } f ( x )$ for all $x \in \mathbb { R } ^ { n }$ , then ${ \widehat { h } } ( \xi ) = { \widehat { f } } ( \xi - y )$ for all $\xi \in \mathbb { R } ^ { n }$

(b) Show that if T be a non-singular linear transformation of $\mathbb { R } ^ { n }$ and $S = ( T ^ { * } ) ^ { - 1 }$ denote its inverse transpose, then

$$
{ \widehat { f \circ T } } ( \xi ) = { \frac { 1 } { | \operatorname* { d e t } T | } } { \widehat { f } } ( S \xi )
$$

for all $\xi \in \mathbb { R } ^ { n }$

4. (a) Let $f \in L ^ { 1 } ( \mathbb { R } )$

i. Let $g ( x ) = x f ( x )$ . Show that if $g \in L ^ { 1 }$ , then $\widehat { f }$ is differentiable and $\begin{array} { r } { \frac { d } { d \xi } \widehat { f } ( \xi ) = - 2 \pi i \widehat { g } ( \xi ) } \end{array}$

ii.
Let $f \in C _ { 0 } ^ { 1 } ( \mathbb { R } )$ and $\textstyle h ( x ) = { \frac { d } { d x } } f ( x )$ . Show that if $h \in L ^ { 1 }$ , then ${ \widehat { h } } ( \xi ) = 2 \pi i \xi { \widehat { f } } ( \xi )$

Recall that $C _ { 0 } ^ { 1 } ( \mathbb { R } )$ is the collection of functions in $C ^ { 1 } ( \mathbb { R } )$ which vanishes at infinity.

(b) Let $G ( x ) = e ^ { - \pi x ^ { 2 } }$ . By considering the derivative of ${ \widehat { G } } ( \xi ) / G ( \xi )$ , show that ${ \widehat { G } } ( \xi ) = G ( \xi )$

Hint: You may also want to use the fact that $\begin{array} { r } { \int _ { \mathbb { R } } G ( x ) d x = 1 } \end{array}$ (see “challenge” problem).

5. The functions D, F , and P defined below are all bounded $L ^ { + } ( \mathbb { R } )$ functions with integrals equal to 1.

(a) Show that if

$$
D ( x ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { ~ i f ~ } } | x | \leq 1 / 2 } \\ { 0 } & { { \mathrm { ~ o t h e r w i s e } } } \end{array} \right. }
$$

then

$$
\widehat { D } ( \xi ) = \frac { \sin \pi \xi } { \pi \xi } .
$$

This gives, in light of Assignment 5 Challenge Problem $1 ( a )$ , an explicit example of a function which is not in $L ^ { 1 } ( \mathbb { R } )$ , but yet is the Fourier transform of an $L ^ { 1 }$ function.
See Question 6 for additional higher dimensional examples.

(b) Let

$$
F ( x ) = { \left\{ \begin{array} { l l } { 1 - | x | } & { { \mathrm { ~ i f ~ } } | x | \leq 1 } \\ { 0 } & { { \mathrm { ~ o t h e r w i s e } } } \end{array} \right. } .
$$

i. Show that

$$
\widehat { F } ( \xi ) = \left( \frac { \sin \pi \xi } { \pi \xi } \right) ^ { 2 } .
$$

Hint: It may help to write ${ \widehat { F } } ( \xi ) = h ( \xi ) + h ( - \xi )$ where $\begin{array} { r } { h ( \xi ) = e ^ { 2 \pi i \xi } \int _ { 0 } ^ { 1 } y e ^ { - 2 \pi i y \xi } d y } \end{array}$

ii.
Find the Fourier transform of the function

$$
f ( x ) = \left( \frac { \sin \pi x } { \pi x } \right) ^ { 2 } .
$$

Be careful to fully justify your answer.

(c) Show that if

$$
P ( x ) = { \frac { 1 } { \pi } } { \frac { 1 } { 1 + x ^ { 2 } } } .
$$

then

$$
\int _ { - \infty } ^ { \infty } e ^ { - 2 \pi | \xi | } e ^ { 2 \pi i x \xi } d \xi = P ( x )
$$

and hence that

$$
{ \widehat { P } } ( \xi ) = e ^ { - 2 \pi | \xi | } .
$$

Be careful to fully justify your answer.

Remark: In Questions $\mathit { 4 0 }$ and 5 above D is for Dirichlet, F is for Fej´er, P is for Poisson, and G is for Gauss-Weierstrass.
The respective “approximate identities”, namely $\{ ( \widehat { D } ) _ { t } \} _ { t > 0 } , \ \{ ( \widehat { F } ) _ { t } \} _ { t > 0 } , \ \{ P _ { t } \} _ { t > 0 } ,$ and $\{ G _ { \sqrt { t } } \} _ { t > 0 } .$ , are generally referred to as Dirichlet, Fej´er, Poisson, and Gauss-Weierstrass kernels.

6. Show that for any $\varepsilon > 0$ the function $F ( \xi ) = ( 1 + | \xi | ^ { 2 } ) ^ { - \varepsilon }$ is the Fourier transform of an $L ^ { 1 } ( \mathbb { R } ^ { n } )$ function.
   Hint: Consider the function

$$
f ( x ) = \int _ { 0 } ^ { \infty } G _ { t } ( x ) e ^ { - \pi t ^ { 2 } } t ^ { 2 \varepsilon - 1 } d t ,
$$

where $G _ { t } ( x ) = t ^ { - n } e ^ { - \pi | x | ^ { 2 } / t ^ { 2 } }$ . Now use Fubini/Tonelli to prove that $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ with ${ \widehat { f } } ( \xi ) = F ( \xi ) \| f \| _ { 1 }$

## Extra Challenge Problems

Not to be handed in with the assignment

1. By considering the iterated integral

$$
\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { \infty } x e ^ { - x ^ { 2 } ( 1 + y ^ { 2 } ) } d x \right) d y
$$

show (with justification) that

$$
\int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \frac { \sqrt { \pi } } { 2 } }
$$

and hence that

$$
\int _ { - \infty } ^ { \infty } e ^ { - \pi x ^ { 2 } } d x = 1 .
$$

# Math 8100 Assignment 7 Hilbert Spaces

Due date: Thursday 14th of November 2019

1. (a) Prove that $\ell ^ { 2 } ( \mathbb { N } )$ is complete.

Recall that $\ell ^ { 2 } ( \mathbb { N } ) : = \{ x = \{ x _ { j } \} _ { j = 1 } ^ { \infty } : \| x \| _ { \ell ^ { 2 } } < \infty \}$ , where $\| x \| _ { \ell ^ { 2 } } : = \Big ( \sum _ { j = 1 } ^ { \infty } | x _ { j } | ^ { 2 } \Big ) ^ { 1 / 2 } .$

(b) Let H be a Hilbert space.
Prove the so-called polarization identity, namely that for any $x , y \in H$

$$
\langle x , y \rangle = { \frac { 1 } { 4 } } \left( \| x + y \| ^ { 2 } - \| x - y \| ^ { 2 } + i \| x + i y \| ^ { 2 } - i \| x - i y \| ^ { 2 } \right)
$$

and conclude that any invertible linear map from H to $\ell ^ { 2 } ( \mathbb { N } )$ is unitary if and only if it is isometric.

Recall that if $H _ { 1 }$ and $H _ { 2 }$ are Hilbert spaces with inner products $\langle \cdot , \cdot \rangle _ { 1 }$ and $\langle \cdot , \cdot \rangle _ { 2 }$ , then a mapping $U : H _ { 1 } \to H _ { 2 }$ is said to be unitary if it is an invertible linear map that preserves inner products, namely $\langle U x , U y \rangle _ { 2 } = \langle x , y \rangle _ { 1 }$ , and an isometry if it preserves “lengths”, namely $\| U x \| _ { 2 } = \| x \| _ { 1 }$

2. Let E be a subset of a Hilbert space H.

(a) Show that $E ^ { \perp } : = \{ x \in H : \langle x , y \rangle = 0$ for all $y \in E \}$ is a closed subspace of $H$

(b) Show that $( E ^ { \bot } ) ^ { \bot }$ is the smallest closed subspace of H that contains E.

3. In $L ^ { 2 } ( [ 0 , 1 ] )$ let $e _ { 0 } ( x ) = 1 , e _ { 1 } ( x ) = { \sqrt { 3 } } ( 2 x - 1 )$ for all $x \in ( 0 , 1 )$

(a) Show that $e _ { 0 } , e _ { 1 }$ is an orthonormal system in $L ^ { 2 } ( 0 , 1 )$

(b) Show that the polynomial of degree 1 which is closest with respect to the norm of $L ^ { 2 } ( 0 , 1 )$ to the function $f ( x ) = x ^ { 2 }$ is given by $g ( x ) = x - 1 / 6$ . What is $\| f - g \| _ { 2 } ?$

4. (a) Verify that the following systems are orthogonal in $L ^ { 2 } ( [ 0 , 1 ] )$

$$
\{ 1 / \sqrt { 2 } , \cos ( 2 \pi x ) , \sin ( 2 \pi x ) , \ldots , \cos ( 2 \pi k x ) , \sin ( 2 \pi k x ) , \ldots \}
$$

ii.
$\{ e ^ { 2 \pi i k x } \} _ { k = - \infty } ^ { \infty }$

(b) Let $f \in L ^ { 1 } ( [ 0 , 1 ] )$

i. Show that for any $\epsilon > 0$ we can write $f = g + h$ , where $g \in L ^ { 2 }$ and $\| h \| _ { 1 } < \epsilon$

ii.
Use this decomposition of f to prove the so-called Riemann-Lebesgue lemma:

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { 1 } f ( x ) \cos ( 2 \pi k x ) d x = \operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { 1 } f ( x ) \sin ( 2 \pi k x ) d x = 0
$$

5. (a) The first three Legendre polynomials are

$$
P _ { 0 } ( x ) = 1 , \quad P _ { 1 } ( x ) = x , \quad P _ { 2 } ( x ) = ( 3 x ^ { 2 } - 1 ) / 2 .
$$

Show that the orthonormal system in $L ^ { 2 } ( [ - 1 , 1 ] )$ obtained by applying the Gram-Schmidt process to $1 , x , x ^ { 2 }$ are scalar multiples of these.

(b) Compute

$$
\operatorname* { m i n } _ { a , b , c } \int _ { - 1 } ^ { 1 } | x ^ { 3 } - a - b x - c x ^ { 2 } | ^ { 2 } d x
$$

(c) Find

$$
\operatorname* { m a x } \int _ { - 1 } ^ { 1 } x ^ { 3 } g ( x ) d x
$$

where g is subject to the restrictions

$$
\int _ { - 1 } ^ { 1 } g ( x ) d x = \int _ { - 1 } ^ { 1 } x g ( x ) d x = \int _ { - 1 } ^ { 1 } x ^ { 2 } g ( x ) d x = 0 ; \ \int _ { - 1 } ^ { 1 } | g ( x ) | ^ { 2 } d x = 1 .
$$

6. Let

$$
{ \mathcal { C } } = \left\{ f \in L ^ { 2 } ( [ 0 , 1 ] ) : \int _ { 0 } ^ { 1 } f ( x ) d x = 1 \ { \mathrm { ~ a n d ~ } } \ \int _ { 0 } ^ { 1 } x f ( x ) d x = 2 \right\}
$$

(a) Let $g ( x ) = 1 8 x ^ { 2 } - 5$ . Show that $g \in { \mathcal { C } }$ and that

$$
\mathcal { C } = g + \mathcal { S } ^ { \perp }
$$

where $\mathcal { S } ^ { \perp }$ denotes the orthogonal complement of $S = \operatorname { S p a n } \left( \{ 1 , x \} \right)$

(b) Find the function $f _ { 0 } \in { \mathcal { C } }$ for which

$$
\int _ { 0 } ^ { 1 } | f _ { 0 } ( x ) | ^ { 2 } d x = \operatorname* { i n f } _ { f \in { \mathcal C } } \int _ { 0 } ^ { 1 } | f ( x ) | ^ { 2 } d x .
$$

## Extra Challenge Problems

Not to be handed in with the assignment

1. Prove that every closed convex set K in a Hilbert space has a unique element of minimal norm.

2. The Mean Ergodic Theorem: Let U be a unitary operator on a Hilbert space H.

Prove that if $M = \{ x \ : \ U x = x \}$ and $\begin{array} { r } { S _ { N } = \frac { 1 } { N } \sum _ { n = 0 } ^ { N - 1 } U ^ { n } } \end{array}$ , then lim $\| S _ { N } x - P x \| = 0$ N→∞ for all $x \in H$ , where P x denotes the orthogonal projection of x onto M.

# Math 8100 Assignment 8 Basic Function Spaces

Due date: Tuesday the 26th of November 2019

1. Prove the following basic properties of $L ^ { \infty } = L ^ { \infty } ( X )$ , where X is a measurable subset of $\mathbb { R } ^ { n }$

(a) $\| \cdot \| _ { \infty }$ is a norm on $L ^ { \infty }$ and when equipped with this norm $L ^ { \infty }$ is a Banach space.

(b) $\| f _ { n } - f \| _ { \infty } \to 0$ iff there exists $E \in \mathbb { R } ^ { n }$ such that $m ( E ^ { c } ) = 0$ and $f _ { n }  f$ uniformly on $E .$

(c) Simple functions are dense in $L ^ { \infty }$ , but continuous functions with compact support are not.

Recall that $i f X \subseteq \mathbb { R } ^ { n }$ is measurable and f is a measurable function on $X$ , then we define

$$
\| f \| _ { \infty } = \operatorname* { i n f } \{ a \geq 0 : m ( \{ x \in X : | f ( x ) | > a \} ) = 0 \} ,
$$

with the convention that inf $\varnothing = \infty ,$ and

$$
L ^ { \infty } = L ^ { \infty } ( X ) = \{ f : X \to \mathbb { C } \ m e a s u a r a b l e : \ \lVert f \rVert _ { \infty } < \infty \} ,
$$

with the usual convention that two functions that are equal a.e. define the same element of $L ^ { \infty }$ . Thus $f \in L ^ { \infty }$ if and only if there is a bounded function g such that $f = g$ almost everywhere; we can take $g = f \chi _ { E }$ where $E = \{ x : | f ( x ) | \leq \| f \| _ { \infty } \}$

2. Let $X \subseteq \mathbb { R } ^ { n }$ be measurable.

(a) i. Prove that if $m ( X ) < \infty$ , then

$$
L ^ { \infty } ( X ) \subset L ^ { 2 } ( X ) \subset L ^ { 1 } ( X )\tag{1}
$$

with strict inclusion in each case, and that for any measurable $f : X \to \mathbb { C }$ one in fact has

$$
\| f \| _ { L ^ { 1 } ( X ) } \leq m ( X ) ^ { 1 / 2 } \| f \| _ { L ^ { 2 } ( X ) } \leq m ( X ) \| f \| _ { L ^ { \infty } ( X ) } .
$$

ii.
Give examples to show that no such result of the form (1) can hold if one drops the assumption that $m ( x ) < \infty$ . Prove, furthermore, that if $L ^ { 2 } ( X ) \subseteq L ^ { 1 } ( X )$ , then $m ( X ) < \infty$

(b) Prove that

$$
\underset { ( \star ) } { \underbrace { L ^ { 1 } ( X ) \cap L ^ { \infty } ( X ) \subset L ^ { 2 } ( X ) } } \subset L ^ { 1 } ( X ) + L ^ { \infty } ( X )
$$

and that in addition to (?) one in fact has

$$
\| f \| _ { L ^ { 2 } ( X ) } \leq \| f \| _ { L ^ { 1 } ( X ) } ^ { 1 / 2 } \| f \| _ { L ^ { \infty } ( X ) } ^ { 1 / 2 }
$$

for any measurable function $f : X \to \mathbb { C }$

3. Prove that

$$
\ell ^ { 1 } ( \mathbb { Z } ) \subset \ell ^ { 2 } ( \mathbb { Z } ) \subset \ell ^ { \infty } ( \mathbb { Z } )
$$

with strict inclusion in each case, and that for any sequence $a = \{ a _ { j } \} _ { j \in \mathbb { Z } }$ of complex numbers one in fact has

$$
\| a \| _ { \ell ^ { \infty } ( \mathbb { Z } ) } \leq \| a \| _ { \ell ^ { 2 } ( \mathbb { Z } ) } \leq \| a \| _ { \ell ^ { 1 } ( \mathbb { Z } ) } .
$$

Recall that for $p = 1 , 2 , \infty$ we define

$$
\ell ^ { p } ( \mathbb { Z } ) = \{ a = \{ a _ { j } \} _ { j \in \mathbb { Z } } \subseteq \mathbb { C } : \| a \| _ { \ell ^ { p } ( \mathbb { Z } ) } < \infty \}
$$

where

$$
\| a \| _ { \ell ^ { 1 } ( \mathbb { Z } ) } = \sum _ { j = - \infty } ^ { \infty } | a _ { j } | , \quad \| a \| _ { \ell ^ { 2 } ( \mathbb { Z } ) } = \Big ( \sum _ { j = - \infty } ^ { \infty } | a _ { j } | ^ { 2 } \Big ) ^ { 1 / 2 } , a n d \| a \| _ { \ell ^ { \infty } ( \mathbb { Z } ) } = \operatorname* { s u p } _ { j } | a _ { j } | .
$$

4. Let $C ( [ 0 , 1 ] )$ denote the space of all continuous real-valued functions on [0, 1].

(a) Prove that $C ( [ 0 , 1 ] )$ is complete under the uniform norm $\| f \| _ { u } : = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | f ( x ) |$

(b) Prove that $C ( [ 0 , 1 ] )$ is not complete under the L1-norm $\| f \| _ { 1 } = \int _ { 0 } ^ { 1 } | f ( x ) | d x$

5. Let H be a Hilbert space with orthonormal basis $\{ u _ { n } \} _ { n = 1 } ^ { \infty }$

(a) Let $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of complex numbers.
Prove that

$\sum _ { n = 1 } ^ { \infty } a _ { n } u _ { n }$ converges in H $\iff \sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } < \infty ,$

and moreover that if $: \sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } < \infty$ , then $\Big \| \sum _ { n = 1 } ^ { \infty } a _ { n } u _ { n } \Big \| = \Big ( \sum _ { n = 1 } ^ { \infty } | a _ { n } | ^ { 2 } \Big ) ^ { 1 / 2 } .$

(b) i. Is there a continuous linear functional L on H such that $L ( u _ { n } ) = n ^ { - 1 }$ for all $n \in \mathbb { N } ?$ If L exists, find its norm.

ii.
Is there a continuous linear functional L on H such that $L ( u _ { n } ) = n ^ { - 1 / 2 }$ for all $n \in \mathbb { N } ?$ If L exists, find its norm.

6. For each $1 \leq p \leq \infty$ , define $\Lambda _ { p } : L ^ { p } ( [ 0 , 1 ] ) \to \mathbb { R }$ by

$$
\Lambda _ { p } ( f ) = \int _ { 0 } ^ { 1 } x ^ { 2 } f ( x ) d x .
$$

Explain why $\Lambda _ { p }$ is a continuous linear functional and compute its norm (in terms of $p )$

## Extra Practice Problems Not to be handed in with the assignment

1. Let f and g be two non-negative Lebesgue measurable functions on $[ 0 , \infty )$ . Suppose that

$$
A : = \int _ { 0 } ^ { \infty } f ( y ) y ^ { - 1 / 2 } d y < \infty \qquad \mathrm { a n d } \qquad B : = \left( \int _ { 0 } ^ { \infty } | g ( y ) | ^ { 2 } d y \right) ^ { 1 / 2 } < \infty
$$

Prove that

$$
\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { x } f ( y ) d y \right) { \frac { g ( x ) } { x } } d x \leq A B
$$

2. Let $\{ f _ { k } \}$ be any sequence of functions in $L ^ { 2 } ( [ 0 , 1 ] )$ satisfying $\| f _ { k } \| _ { 2 } \leq 1$ for all $k \in \mathbb N$

(a) i. Prove that if $f _ { k }  f$ either a.e. on [0, 1] or in $L ^ { 1 } ( [ 0 , 1 ] )$ , then $f \in L ^ { 2 } ( [ 0 , 1 ] )$ ) with $\| f \| _ { 2 } \leq 1$

ii.
Do either of the above hypotheses guarantee that $f _ { k }  f$ in $L ^ { 2 } ( [ 0 , 1 ] ) ?$

(b) Prove that if $f _ { k } \to f { \mathrm { ~ a . e . } }$ . on [0, 1], then this in fact implies that $f _ { k }  f$ in $L ^ { 1 } ( [ 0 , 1 ] )$ ).

3. Let $1 \leq p \leq \infty$ . Prove that if $\{ f _ { k } \} _ { k = 1 } ^ { \infty }$ is a sequence of functions in $L ^ { p } ( \mathbb { R } ^ { n } )$ with the property that

$$
\sum _ { k = 1 } ^ { \infty } \| f _ { k } \| _ { p } < \infty ,
$$

then $\sum f _ { k }$ converges almost everywhere to an $L ^ { p } ( \mathbb { R } ^ { n } )$ function with

$$
\left\| \sum _ { k = 1 } ^ { \infty } f _ { k } \right\| _ { p } \leq \sum _ { k = 1 } ^ { \infty } \| f _ { k } \| _ { p } .
$$
