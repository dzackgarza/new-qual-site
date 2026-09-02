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
