# Math 4100/6100 Assignment 1 Some Preliminaries and a Review of Sequences and Series Due date: 5:00pm on Tuesday the 1st of September 2020

1. (Reverse Triangle Inequality). Use the triangle inequality to prove that if $x , y \in \mathbb { R }$ , then

$$
\left| | x | - | y | \right| \leq | x - y | .
$$

2. (a) Let $q \neq 0$ be rational and x be irrational. Prove that $q + x$ and $q x$ are both irrational.

(b) Use the Archimedean Property of R to prove that between any two distinct real numbers there is both a rational and irrational number.

3. (a) (De Morgan’s Laws). Let A and B be subsets of R. Verify the following:

i. $( A \cap B ) ^ { c } = A ^ { c } \cup B ^ { c }$

ii. $( A \cup B ) ^ { c } = A ^ { c } \cap B ^ { c }$

(b) i. Show how induction can be used to conclude that

$$
( A _ { 1 } \cup A _ { 2 } \cup \cdot \cdot \cdot \cup A _ { n } ) ^ { c } = A _ { 1 } ^ { c } \cap A _ { 2 } ^ { c } \cap \cdot \cdot \cdot \cap A _ { n } ^ { c }
$$

for any finite $n \in \mathbb { N }$

ii. Explain why induction cannot be used to conclude that

$$
\left( \bigcup _ { n = 1 } ^ { \infty } A _ { n } \right) ^ { c } = \bigcap _ { n = 1 } ^ { \infty } A _ { n } ^ { c } .
$$

iii. Is the statement in part (ii) above valid? Give either a proof or counterexample.

4. (a) Let $A \subseteq \mathbb { R }$ be non-empty and bounded below. Show that

i. inf $A = - \operatorname* { s u p } ( - A )$ where $- A = \{ - x : x \in A \}$

ii. inf $A = \operatorname* { s u p } ( B )$ where $B = \{ b : b$ is a lower bound for A}

(b) Let $A , B \subseteq \mathbb { R }$ which are non-empty, bounded above.

i. Show that if $A \subseteq B$ , then sup $A \leq \operatorname* { s u p } B$

ii. Show that if sup $A < \operatorname* { s u p } B$ , then there must exist a $b \in B$ that is an upper bound for A.

5. Verify, using the definition of convergence of a sequence, that the following sequences converge to the proposed limit.

(a) $\operatorname* { l i m } _ { n \to \infty } { \frac { 3 n + 1 } { 2 n + 5 } } = { \frac { 3 } { 2 } }$ (b) $\operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { 6 n ^ { 2 } + 1 } } = 0$ (c) $\operatorname* { l i m } _ { n \to \infty } { \frac { 2 } { \sqrt { n + 3 } } } = 0$

6. What happens if we reverse the order of the quantifiers in the definition of convergence of a sequence?

Definition: A sequence $\left\{ a _ { n } \right\}$ verconges to a if there exists an $\varepsilon > 0$ such that for all $N \in  { \mathbb { N } }$ it is true that $n \geq N$ implies $| a _ { n } - a | < \varepsilon$

Give an example of a vercongent sequence. Can you give an example a vercongent sequence that is divergent? What exactly is being described in this strange definition?

7. Verify the following using the definition of convergence of a sequence:

(a) If $a _ { n } \to a ,$ then $\left| a _ { n } \right| \to \left| a \right|$ . Is the converse true?

(b) If $a _ { n } \geq 0$ for all $n \in \mathbb { N }$ and $a _ { n } \to a$ , then ${ \sqrt { a _ { n } } }  { \sqrt { a } } .$

(c) If $\left\{ a _ { n } \right\}$ is a bounded but not necessarily convergent sequence and $\operatorname* { l i m } _ { n \to \infty } b _ { n } \ = \ 0$ , then $\operatorname* { l i m } _ { n \to \infty } a _ { n } b _ { n } = 0$

(d) If $0 \leq a _ { n } \leq b _ { n }$ for all $n \in \mathbb { N }$ , and if lim $b _ { n } = 0$ , then lim $a _ { n } = 0$ as well. n→∞ n→∞

Note that this immediately $( r i g h t ? )$ implies the following “Squeeze Theorem”:

$I f a _ { n } \leq b _ { n } \leq c _ { n }$ for all $n \in \mathbb N$ , and if lim $a _ { n } = \operatorname* { l i m } _ { n \to \infty } c _ { n } = L$ , then lim $b _ { n } = L$ n→∞ n→∞

8. Let $\left\{ a _ { n } \right\}$ be a convergent sequence with lim $a _ { n } = a$ . Prove the following two statements: n→∞

(a) If $a _ { n } \leq b$ for all $n \in \mathbb { N }$ , then $a \leq b$

(b) If $\left\{ a _ { n } \right\}$ is increasing, then $a _ { n } \leq a$ for all $n \in \mathbb { N } .$

9. Let $a _ { 1 } = { \sqrt { 2 } }$ , and define $a _ { n + 1 } = { \sqrt { 2 + a _ { n } } }$ for all $n \geq 1$ . Prove that $\operatorname* { l i m } _ { n \to \infty } a _ { n }$ exists and equals 2.

10. (a) Investigate the behavior (convergence or divergence) of $\sum _ { n = 1 } ^ { \infty } a _ { n }$ if (i) $a _ { n } = { \sqrt { n + 1 } } - { \sqrt { n } }$ (ii) $a _ { n } = { \frac { { \sqrt { n + 1 } } - { \sqrt { n } } } { n } }$ (iii) $a _ { n } = { \bigl ( } { \sqrt [ { n } ] { n } } - 1 { \bigr ) } ^ { n } .$

(b) Let $a _ { n } > 0$ for all $n \in \mathbb { N } .$

i. Show that in $\operatorname* { l i m } _ { n \to \infty } n a _ { n }$ exists and is not equal to 0, then $\sum _ { n = 1 } ^ { \infty } a _ { n }$ diverges. ii. Show that in lim $n ^ { 2 } a _ { n }$ exists, then $\sum _ { n = 1 } ^ { \infty } a _ { n }$ converges. n→∞

(c) Prove that if $a _ { n } > 0$ for all $n \in \mathbb { N }$ , then the convergence of $\sum _ { n = 1 } ^ { \infty } a _ { n }$ implies the convergence of both (i) $\sum _ { n = 1 } ^ { \infty } a _ { n } ^ { 2 }$ (ii) $\sum _ { n = 1 } ^ { \infty } { \frac { \sqrt { a _ { n } } } { n } }$

## Math 6100/Bonus Problems

1. Suppose $\left\{ a _ { n } \right\}$ is a sequence of real numbers and $b _ { n } = { \frac { a _ { 1 } + \cdots + a _ { n } } { n } }$ Prove that if $a _ { n } \to 0$ , then $b _ { n } \to 0$ . Is the converse true? What if $a _ { n } \to L ?$

2. (a) Use Question 8 to deduce the Nested Interval Property from the Monotone Convergence Theorem.

(b) Show conversely that one can also deduce the Monotone Convergence Theorem from the Nested Interval Property.

3. Directly show the equivalence of the Bolzano-Weierstrass Theorem and the Nested Interval Property.

# Math 4100/6100 Assignment 2 Limit Superior and Limit Inferior

Due date: 5:00 pm on Wednesday the 9th of September 2020

1. Let $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence.

(a) Prove that $\left\{ a _ { n } \right\}$ is unbounded above if and only if it has a subsequence with limit $+ \infty$

(b) Prove that $\left\{ a _ { n } \right\}$ is unbounded below if and only if it has a subsequence with limit −∞.

2. Let $\{ x _ { n } \}$ be a bounded sequence. Prove statements (a) and (b) below twice, once each as quick consequences of the following equivalent definitions:

(i) li $\operatorname* { m s u p } x _ { n } : = \operatorname* { s u p } { \big \{ } x \in \mathbb { R } : x$ is a subsequential limit of $\{ x _ { n } \} \}$ n→∞

(ii) $\operatorname* { l i m } _ { n \to \infty } x _ { n } : = \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { k \geq n } x _ { k }$

(a) If $| x _ { n } | \leq M$ for all $n \in \mathbb { N } ,$ , then $| \operatorname* { l i m } _ { n \to \infty } x _ { n } | \leq M$ also.

(b) Prove that if $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ be a bounded sequences with $a _ { n } \leq b _ { n }$ for all $n \in \mathbb { N }$ , then

$$
\operatorname* { l i m } _ { n \to \infty } a _ { n } \leq \operatorname* { l i m } _ { n \to \infty } b _ { n }
$$

3. Let $\{ x _ { n } \}$ be a bounded sequence. Prove statements (a) and (b) below twice, once each as quick consequences of the following equivalent definitions:

(i) $\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } x _ { n } : = \operatorname* { i n f } _ { } \left\{ x \in \mathbb { R } \colon x \right.$ is a subsequential limit of $\{ x _ { n } \} \}$

(ii) $\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } x _ { n } : = \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { k \geq n } x _ { k }$

(a) If $| x _ { n } | \leq M$ for all $n \in \mathbb { N } ,$ , then $| \operatorname* { l i m } _ { n \to \infty } \operatorname { i n f } x _ { n } | \leq M$ also.

(b) If $\beta < \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { } x _ { n } .$ , then there exists a $N \in \mathbb N$ such that $x _ { n } > \beta$ for all $n \geq N .$

4. (a) Let $\{ x _ { n } \}$ be a bounded sequence. Prove that if $\operatorname* { i m } _ { n \to \infty } | x _ { n } | = 0$ , then $\operatorname* { l i m } _ { n \to \infty } x _ { n }$ exists and equals 0.

(b) Prove that a bounded sequence that does not converge always has at least two subsequences that converge to different limits.

(c) Find the limit inferior and limit superior of the sequence $\left\{ a _ { n } \right\}$ if $a _ { n } = \lfloor \sin n \rfloor$ for all $n \in \mathbb { N } .$

(d) Find the set of all subsequential limits for the sequence $\{ x _ { n } \}$ if for all $n \in \mathbb { N }$

$$
{ \mathrm { ( i ) ~ } } x _ { n } = 4 + 5 ( - 1 ) ^ { \lfloor n / 2 \rfloor } \qquad { \mathrm { ( i i ) ~ } } x _ { n } = \cos ( n \pi / 3 ) \qquad { \mathrm { ( i i i ) ~ } } x _ { n } = ( - 1 ) ^ { \lfloor n / 2 \rfloor } + 2 ( - 1 ) ^ { \lfloor n / 3 \rfloor }
$$

5. (a) Explain why there is no sequence whose set of subsequential limits is $\{ 1 / n \ : \ n \in \mathbb { N } \}$

(b) Give an example of a sequence whose set of subsequential limits is $\lbrace 1 / n : n \in \mathbb { N } \rbrace \cup \lbrace 0 \rbrace$

6. For any two bounded sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ of real numbers, prove that

$$
\operatorname* { l i m } _ { n \to \infty } ( a _ { n } + b _ { n } ) \leq \operatorname* { l i m } _ { n \to \infty } a _ { n } + \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { } b _ { n } .
$$

## Math 6100/Bonus Problems

1. (a) Let $\left\{ a _ { n } \right\}$ denote a bounded sequence of positive reals. Prove that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { a _ { n } } \frac { a _ { n + 1 } } { a _ { n } } \leq \operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { \sqrt { a _ { n } } } \sqrt [ n ] { a _ { n } } \leq \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { \sqrt [ n ] { a _ { n } } } ^ { \ast } \leq \operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { a _ { n } } \frac { a _ { n + 1 } } { a _ { n } }
$$

(b) Can you define a sequnence $\left\{ a _ { n } \right\}$ for which the inequalities above are all strict?

(c) Use the result in part (a) above to prove that lim $\sqrt [ n ] { n } = 1$ n→∞

# Math 4100/6100 Assignment 3

Due date: 5:00 pm on Wednesday the 16th of September 2020

1. (a) Give an example of a countable collection of disjoint open intervals in R.

(b) Give an example of an uncountable collection of disjoint open intervals in R, or argue that no such collection exists.

2. Let A be a countable set, and An denote the collection of all n-tuples $( a _ { 1 } , \ldots , a _ { n } )$ with each $a _ { j } \in A$ for $1 \leq j \leq n$ (these elements need not be distinct). Prove that $A _ { n }$ is countable for each $n \in \mathbb { N }$

3. A real number $x \in \mathbb { R }$ is called algebraic if there exist integers $a _ { 0 } , a _ { 1 } , \ldots , a _ { n } \in \mathbb { Z } .$ , not all zero, such that

$$
a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 } = 0 .
$$

Said another way, a real number is algebraic if it is the root of a polynomial with integer coefficients.   
Real numbers that are not algebraic are called transcendental numbers.

(a) Show that ${ \sqrt { 2 } } , \ { \sqrt [ 3 ] { 2 } } ,$ , and ${ \sqrt { 2 } } + { \sqrt { 3 } }$ are algebraic.

(b) Prove that the set of all algebraic numbers is countable. What may we conclude from this regarding the set of all transcendental numbers?

Hint: First show that the set of all polynomials with integer coefficients of degree n is countable.

4. (a) Let $C \subseteq [ 0 , 1 ]$ be uncountable. Show that there exists $a \in ( 0 , 1 )$ such that ${ \cal C } \cap [ a , 1 ]$ is uncountable.

(b) Now let A be the set of all $a \in ( 0 , 1 )$ such that $C \cap [ a , 1 ]$ is uncountable, and set $\alpha = \operatorname* { s u p } A .$ . Is $C \cap [ \alpha , 1 ]$ uncountable?

(c) Does the statement in (a) remain true if “uncountable” is replaced with “infinite”?

5. (a) Let A be a given set and $P ( A )$ denote the power set of A, namely the collection of all subsets of A. Prove that there does not exist a function $f : A \to P ( A )$ that is onto.

Hint: Assume that such a function does exist and arrive at a contradiction by considering the set

$$
B = \{ a \in A : a \notin f ( a ) \} .
$$

(b) Prove that the set of all infinite subsets of N is uncountable.

Hint: Show directly that the set of all finite subsets of N is countable.

## Math 6100/Bonus Problems

1. (Schr¨oder–Bernstein Theorem). Assume there exists a 1–1 function $f : X \to Y$ and another 1–1 function $g : Y  X$ . Follow the steps to show that there exists a 1–1, onto function $h : X \to Y$ and hence $X \sim Y$

The strategy is to partition X and Y into components $X = A \cup A ^ { \prime }$ and $Y = B \cup B ^ { \prime }$ with $A \cap A ^ { \prime } = \varnothing$ and $B \cap B ^ { \prime } = \varnothing$ , in such a way that f maps A onto B, and g maps $B ^ { \prime }$ onto A′.

(a) Explain how achieving this would lead to a proof that $X \sim Y$

(b) Set $A _ { 1 } = X \setminus g ( Y ) = \{ x \in X : x \notin g ( Y ) \}$ (what happens if $A _ { 1 } = \varnothing ? )$ and inductively define a sequence of sets by letting $A _ { n + 1 } = g ( f ( A _ { n } ) )$ . Show that $\{ A _ { n } : n \in \mathbb { N } \}$ is a pairwise disjoint collection of subsets of X, while $\{ f ( A _ { n } ) : n \in \mathbb { N } \}$ is a similar collection in Y .

(c) Let $A = \textstyle \bigcup _ { n = 1 } ^ { \infty } A _ { n }$ and $\textstyle B = \bigcup _ { n = 1 } ^ { \infty } f ( A _ { n } )$ . Show that f maps A onto B.

(d) Let $A ^ { \prime } = X \setminus A$ and $B ^ { \prime } = Y \setminus B$ . Show that g maps $B ^ { \prime }$ onto $A ^ { \prime } .$

2. Prove that the set of all subsets of N, namely $P ( \mathbb { N } )$ , has the same cardinality as R.

# Math 4100/6100 Assignment 4 Basic Topology of R

Due date: 5:00 pm on Friday the 25th of September 2020

\* In Questions 1-6 below all sets are assumed to be in R with R equipped with its usual Euclidean metric.

1. Let

$$
E = \left\{ { \frac { ( - 1 ) ^ { n } n } { n + 1 } } : n \in \mathbb { N } \right\} .
$$

(a) Find the limit points of E.

(b) Is E a closed set? Is E an open set?

(c) Does E contain any isolated points? A point in E is called isolated if it is not a limit point.

(d) Find E, the closure of E.

2. Construct a bounded set of real numbers with exactly three limit points.

3. Decide which of the following subsets of R are open, closed, or neither (with respect to the usual metric on R). If the set is not open, find a point in the set for which there is no ε-neighborhood contained in the set. If the set is not closed, find a limit point that is not contained in the set.

(a) Q

(b) N

(c) (0, ∞)

(d) (0, 1]

(e) $\{ 1 + 1 / 4 + \cdots + 1 / n ^ { 2 } : n \in \mathbb { N } \}$

4. Decide whether the following sets are compact. For those which are not compact, show how the definitions of both sequentially compact and compact break down. In other words, give an example of (i) a sequence contained in the set that does not possess a subsequence converging to a limit in the set, and (ii) an open cover for which there is no finite subcover.

(a) Q

(b) $\mathbb { Q } \cap [ 0 , 1 ]$

(c) R

(d) Z ∩ [0, 10]

(e) $\{ 1 , 1 / 2 , 1 / 3 , 1 / 4 , 1 / 5 , . . . \}$

(f) $\{ 1 , 1 / 2 , 2 / 3 , 3 / 4 , 4 / 5 , . . . \}$

5. Decide whether the following statements are true or false. Provide counterexamples for those that are false, and supply proofs for those that are true.

(a) For any set $E \subseteq \mathbb { R } , { \overline { { E } } } ^ { c }$ is open.

(b) If a set has an isolated point (a point that is not a limit point), then it cannot be an open set.

(c) If $E \subseteq \mathbb { R }$ is a non-empty and bounded, then $s = \mathrm { s u p }$ E is a limit point of E.

(d) Every non-empty compact subset of R has a largest member.

(e) An open set in R that contains every rational number must be all of R

(f) An arbitrary intersection of compact subsets of R is compact.

(g) If $F _ { 1 } \supseteq F _ { 2 } \supseteq F _ { 3 } \supseteq \cdots$ is a nested sequence of non-empty closed sets, then the intersection

$$
\bigcap _ { n = 1 } ^ { \infty } F _ { n } \neq \varnothing .
$$

(h) A finite set is always compact.

(i) A countable set is always compact.

## Math 6100/Bonus Problems

1. Show directly that compact subsets of R are always both closed and bounded (without using the notion of sequential compactness).

2. Construct a compact set of real numbers whose limit points form a countable set.

# Math 4100/6100 Assignment 5 More Basic Topology

Due date: 5:00 pm on Friday the 2nd of October 2020

1. (a) Prove that every bounded sequence in $\mathbb { R } ^ { n }$ contains a convergent subsequence, using the fact that we know this to be true in the case $n = 1$

(b) Prove that every closed and bounded subset of $\mathbb { R } ^ { n }$ is necessarily sequentially compact.

2. Let X be a infinite set. For $x , y \in X$ , define

$$
d _ { 0 } ( x , y ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } x \neq y } \\ { 0 } & { { \mathrm { i f ~ } } x = y . } \end{array} \right. }
$$

(a) Prove that this is a metric.

(b) Which subsets of the resulting metric space are open? Which are closed? Which are compact?

(c) Show that in this setting ${ \overline { { B _ { \varepsilon } ( x ) } } } \neq \{ y \in X : d _ { 0 } ( x , y ) \leq \varepsilon \}$ in general.

3. Determine which of the following are metrics on R.

(a) $d _ { 1 } ( x , y ) = ( x - y ) ^ { 2 }$

(b) $d _ { 2 } ( x , y ) = { \sqrt { | x - y | } }$

(c) $d _ { 3 } ( x , y ) = | x ^ { 2 } - y ^ { 2 } |$

(d) $d _ { 4 } ( x , y ) = | x - 2 y |$

(e) $d _ { 5 } ( x , y ) = { \frac { | x - y | } { 1 + | x - y | } }$

4. Let B denote the set of all Bernoulli sequences, i.e., sequences $\{ x _ { n } \}$ with $x _ { n } \in \{ 0 , 1 \}$ for all $n \in \mathbb { N }$

(a) Prove that $\begin{array} { r } { \rho ( ( x _ { n } ) , ( y _ { n } ) ) = \sum _ { n = 0 } ^ { \infty } 2 ^ { - n } | x _ { n } - y _ { n } | } \end{array}$ defines a metric on B.

(b) Prove that the set of all sequences in B which begin 0, 1 (in that order) is both open and closed.

5. A set $A \subseteq \mathbb { R }$ is called nowhere-dense if A contains no non-empty open intervals.

(a) Show that a set E is nowhere-dense in R if and only if the complement of E is dense in $\mathbb { R }$

(b) Decide whether teh following sets are dense in R, nowhere-dense in $\mathbb { R } ,$ , or somewhere in between:

i. $\mathbb { Q } \cap [ 0 , 1 ]$

ii. $\{ 1 / n : n \in \mathbb { N } \}$

iii. the irrationals R \ Q

iv. the Cantor set

6. A set $A \subseteq \mathbb { R }$ is called an $F _ { \sigma }$ set if it can be written as the countable union of closed sets. A set $B \subseteq \mathbb { R }$ is called a $G _ { \delta }$ set if it can be written as the countable intersection of open sets R.

(a) Argue that a set A is a $G _ { \delta }$ set if and only if its complement is an $F _ { \sigma }$ set.

(b) i. Show that a closed interval [a, b] is a $G _ { \delta }$ set.

ii. Show that a half-open interval $[ a , b )$ is both a $G _ { \delta }$ set and an $F _ { \sigma }$ set.

iii. Show that $\mathbb { Q }$ is an $F _ { \sigma }$ set and the irrationals R \ Q is a $G _ { \delta }$ set.

(c) i. Show that every closed set is $\mathrm { ~ a ~ } G _ { \delta }$ set and every open set is an $F _ { \sigma }$ set.

ii. Give an example of an $F _ { \sigma }$ set which is not a $G _ { \delta }$ set.

Hint: Use the fact that R cannot be written as a countable union of nowhere-dense sets. Can you recall the proof of this fact?

iii. Give an example of a set which is neither an $F _ { \sigma }$ nor a $G _ { \delta }$ set.

## Math 6100/Bonus Problems

1. Prove that R cannot be written as the disjoint union of two non-empty closed sets.

2. Prove that $\mathcal { C } + \mathcal { C } = [ 0 , 2 ]$ , where C denotes the usual (middle-third) Cantor set and

$$
{ \mathcal { C } } + { \mathcal { C } } = \{ x + y \ : \ x , y \in { \mathcal { C } } \} .
$$

Hint: Consider the intersection of the set $\mathcal { C } \times \mathcal { C } \subset \mathbb { R } ^ { 2 }$ and the family of lines $\{ x + y = c | c \in [ 0 , 2 ] \}$ and use the property of nested compact sets.

## Challenge Problems

1. Construct a bijection from R to its proper subset R $\backslash \mathbb { Q }$ of irrationals.

# Math 4100/6100 Assignment 6 Continuity

Due date: 5:00 pm on Tuesday the 20th of October 2020

Definition 1. Let $A \subseteq \mathbb { R }$ and $f : A  \mathbb { R }$ . We say that f is continuous at $c \in A$ if for every $\varepsilon > 0$ , there exists $a \delta > 0$ such that whenever $x \in A$ with $| x - c | < \delta$ it follows that $| f ( x ) - f ( c ) | < \varepsilon$

Note that this definition (unlike that of a functional limit) requires c to be an element in the domain of $f ,$ namely A. If this point c is an isolated point of A, then f is automatically continuous at $c ,$ while if this point c is a limit point of A, then being continuous at c is equivalent to $\operatorname* { l i m } _ { x \to c } f ( x ) = f ( c )$

1. (a) Prove (from the definition of functional limits) that $\operatorname* { l i m } _ { x \to 2 } x ^ { 3 } = 8 .$

(b) Prove (from the definition of continuity above) that $f ( x ) = { \frac { x ^ { 2 } + 2 x - 5 } { x - 2 } }$ is continuous at $x = 1$

(c) Prove (from the sequential characterization of limit) that $\operatorname* { l i m } _ { x \to 0 } x / | x |$ does not exist.

2. Suppose $f : \mathbb { R } \to \mathbb { R }$ satisfies

$$
\operatorname* { l i m } _ { h \to 0 } \left( f ( x + h ) - f ( x - h ) \right) = 0
$$

for every $x \in \mathbb { R }$ . Does this imply that $f$ is continuous?

3. (a) Define Dirichlet’s function $g : \mathbb { R }  \mathbb { R }$ , by

$$
\begin{array} { r } { g ( x ) : = { \left\{ \begin{array} { l l } { 1 } & { \mathrm { i f ~ } x \in \mathbb { Q } } \\ { 0 } & { \mathrm { i f ~ } x \not \in \mathbb { Q } } \end{array} \right. } . } \end{array}
$$

Prove that g is discontinuous at all $x \in \mathbb { R }$

(b) Define a modified Dirichlet’s function $h : \mathbb { R }  \mathbb { R } .$ , by

$$
h ( x ) : = { \left\{ \begin{array} { l l } { x } & { { \mathrm { i f ~ } } x \in \mathbb { Q } } \\ { 0 } & { { \mathrm { i f ~ } } x \not \in \mathbb { Q } } \end{array} \right. } .
$$

Prove that h is continuous at $x = 0$ , but discontinuous at all $x \neq 0$

(c) Define Thomae’s function $t : \mathbb { R }  \mathbb { R }$ , by

$$
t ( x ) : = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } x = 0 } \\ { { \frac { 1 } { n } } } & { { \mathrm { i f ~ } } x = { \cfrac { m } { n } } \in \mathbb { Q } \setminus \{ 0 \} { \mathrm { ~ i n ~ l o w e s t ~ t e r m s ~ w i t h ~ } } n > 0 . } \\ { 0 } & { { \mathrm { i f ~ } } x \notin \mathbb { Q } } \end{array} \right. }
$$

Prove that t is continuous at every $x \notin \mathbb { Q }$ , but has a removable simple discontinuity at every $x \in \mathbb { Q } .$ . Hint: Show that $\operatorname* { l i m } _ { x \to c } t ( x ) = 0 ~ f o r ~ a l l ~ c \in \mathbb { R }$

4. Decide if the following claims are true or false, providing either a short proof or counterexample to justify each conclusion. Assume throughout that $f$ is defined and continuous on all of R.

(a) If $f ( x ) \geq 0$ for all $x < 1$ , then $f ( 1 ) \geq 0$ as well.

(b) If $f ( r ) = 0$ for all $r \in \mathbb { Q }$ , then $f ( x ) = 0$ for all $x \in \mathbb { R }$

(c) If $f ( x _ { 0 } ) > 0$ for a single point $x _ { 0 } \in \mathbb { R }$ , then $f ( x )$ is in fact strictly positive for uncountably many points.

# Math 4100/6100 Assignment 7 More on Continuity

Due date: By 5:00 pm on Tuesday the 27th of October 2020

1. Let $f : \mathbb { R } \to \mathbb { R } .$

(a) Prove that f is continuous on R if and only if $f ^ { - 1 } ( G )$ is open whenever $G \subseteq \mathbb { R }$ is an open set.

(b) Prove that if f be continuous, then

$$
Z ( f ) : = \{ x \in \mathbb { R } : f ( x ) = 0 \}
$$

defines a closed set.

2. (a) i. Show that $f ( x ) = x ^ { 3 }$ is continuous on all of R.

ii. Argue that f is however not uniformly continuous on R.

(b) Show that $g ( x ) = 1 / x ^ { 2 }$ is uniformly continuous on $[ 1 , \infty )$ , but not on the set (0, 1].

(c) Show that $h ( x ) = { \sqrt { x } }$ is uniformly continuous on $[ 0 , \infty )$

3. (a) Let $f : [ 0 , 1 ]  [ 0 , 1 ]$ be continuous. Prove that f must have a fixed point; that is, show that there must exist $x \in [ 0 , 1 ]$ with the property that $f ( x ) = x$

(b) Let $f : [ 0 , 1 ] \to \mathbb { R }$ be continuous with $f ( 0 ) = f ( 1 )$

Show that there must exist $x \in [ 0 , 1 / 2 ]$ with the property that $f ( x ) = f ( x + 1 / 2 )$

4. Give an example of each of the following, or provide a short argument for why the request is impossible.

(a) A continuous function defined on [0, 1] with range (0, 1).

(b) A continuous function defined on (0, 1) with range [0, 1].

(c) A continuous function defined on (0, 1] with range (0, 1).

## Math 6100/Bonus Problems

1. (a) If A is a non-empty subset of R, we define the distance from $x \in \mathbb { R }$ to A by

$$
\rho _ { A } ( x ) = \operatorname* { i n f } _ { y \in A } | x - y | .
$$

i. Prove that $\rho _ { A } ( x ) = 0$ if and only if $x \in { \overline { { A } } }$

ii. Prove that $\rho _ { A }$ is uniformly continuous on R, by showing that

$$
| \rho _ { A } ( x ) - \rho _ { A } ( y ) | \leq | x - y |
$$

for all $x , y \in \mathbb { R } .$

(b) Let A and B be disjoint non-empty closed subsets of R, and define

$$
f ( x ) : = \frac { \rho _ { A } ( x ) } { \rho _ { A } ( x ) + \rho _ { B } ( x ) }
$$

for each $x \in \mathbb { R }$ . Show that f is a continuous function from R into [0, 1] such that $f ( x ) = 0$ for all $x \in A$ A, and $f ( x ) = 1$ for all $x \in B$

Note that this in particular establishes a converse to Q1b: Every closed set in R is $Z ( f )$ for some continuous function $f : \mathbb { R }  \mathbb { R }$ . It also gives a proof (but bot the easiest one) that R cannot be written as a disjoint union of two non-empty closed subsets.

# Math 4100/6100 Assignment 8 Continuity and Differentiation

Due date: By 5:00 pm on Tuesday the 3rd of November 2020

1. Suppose $f : \mathbb { R } \to \mathbb { R }$ has the property that

$$
| f ( x ) - f ( y ) | \leq | x - y | ^ { 2 }
$$

for all $x , y \in \mathbb { R }$ . Prove that $f$ is a constant.

2. Construct a function $f : \mathbb { R } $ R that is differentiable at a single point.

3. (a) Let

$$
f _ { a } ( x ) = { \left\{ x ^ { a } \begin{array} { l l } { x ^ { a } } & { { \mathrm { i f ~ } } x > 0 } \\ { 0 } & { { \mathrm { i f ~ } } x \leq 0 } \end{array} \right. }
$$

i. For which values of a is $f _ { a }$ continuous at $0 ?$

ii. For which values of a is $f _ { a }$ differentiable at 0? In this case is the derivative function continuous?

iii. For which values of a is $f _ { a }$ twice-differentiable?

(b) Let

$$
g _ { a } ( x ) = { \left\{ \begin{array} { l l } { x ^ { a } \sin ( 1 / x ) } & { { \mathrm { i f ~ } } x \neq 0 } \\ { 0 } & { { \mathrm { i f ~ } } x = 0 } \end{array} \right. }
$$

Find particular non-negative (and potentially non-integral) values of a for which:

i. $g _ { a }$ is differentiable on $\mathbb { R } ,$ but $g _ { a } ^ { \prime }$ is unbounded on [0, 1].

ii. $g _ { a }$ is differentiable on R with $g _ { a } ^ { \prime }$ continuous but not differentiable at 0.

iii. $g _ { a }$ and $g _ { a } ^ { \prime }$ are differentiable on R, but $g _ { a } ^ { \prime \prime }$ is not continuous at 0.

4. Exactly one of the following requests is impossible. Decide which it is, and provide examples for the other three. In each case, lets assume that the functions are defined on all of R.

(a) Function $f$ and g not differentiable at $x _ { 0 } = 0$ , but where $f g$ is differentiable at $x _ { 0 } = 0$

(b) A function f not differentiable at $x _ { 0 } = 0$ and a function g differentiable at $x _ { 0 } = 0$ where $f g$ is differentiable at $x _ { 0 } = 0$

(c) A function f not differentiable at $x _ { 0 } = 0$ and a function $g$ differentiable at $x _ { 0 } = 0$ where $f + g$ is differentiable at $x _ { 0 } = 0$

(d) A function $f$ differentiable at $x _ { 0 } = 0$ , but not differentiable at any other point.

5. (a) Suppose $f$ is continuous on $[ a , b ]$ , twice differentiable on $( a , b )$ , and $f ^ { \prime \prime } ( x ) \neq 0$ for all $x \in ( a , b )$ Prove carefully that $f$ has at most 2 distinct zeros in $[ a , b ]$

(b) Prove that the function $f ( x ) = x ^ { 2 } -$ sin x has precisely two roots.

6. (a) How accurately does $1 + x + x ^ { 2 } / 2$ approximate $e ^ { x }$ for $- 1 \leq x \leq 1 ?$ Can you find a polynomial that approximates $e ^ { x }$ to within 0.01 on this interval?

(b) Use the Lagrangian Remainder Estimate to determine how well the polynomial $1 + x / 2$ approximates $\sqrt { 1 + x }$ on $[ 0 , 1 / 1 0 ]$

## Math 6100/Bonus Problems

1. Let f be a differentiable function on $[ a , b ]$ . We say that f is uniformly differentiable on $[ a , b ]$ if for every $\varepsilon > 0$ there exists a $\delta > 0$ such that

$$
\left| { \frac { f ( x ) - f ( y ) } { x - y } } - f ^ { \prime } ( y ) \right| < \varepsilon
$$

whenever $| x - y | < \delta$ with $x , y \in [ a , b ]$

(a) Prove that $f$ is uniformly differentiable on [a, b] if and only if $f ^ { \prime }$ is continuous on $[ a , b ]$

(b) Give an example of a function that is differentiable on $[ a , b ]$ but fails to be uniformly differentiable on [a, b] (no proofs required).

2. Let $f : [ 0 , 1 ] \to$ R be continuous with $f ( 0 ) = f ( 1 )$

(a) Show that for each $n \in \mathbb { N }$ there exist $x , y \in [ 0 , 1 ]$ satisfying $| x - y | = 1 / n$ and $f ( x ) = f ( y )$

(b) Show that if $h \in ( 0 , 1 / 2 )$ , but not of the form $1 / n$ for some $n \in \mathbb { N }$ , then there does not necessarily exist $x , y \in [ 0 , 1 ]$ satisfying $| x - y | = h$ and $f ( x ) = f ( y )$

# Math 4100/6100 Assignment 9 Uniform Convergence

Due date: By 5:00 pm on Thursday the 12th of November 2020

1. For each $n \in \mathbb { N }$ and $x \in [ 0 , \infty )$ , let

$$
f _ { n } ( x ) = { \frac { x } { 1 + x ^ { n } } } \qquad { \mathrm { a n d } } \qquad g _ { n } ( x ) = \left\{ { 1 \atop n x } ~ { \mathrm { i f } } ~ x \geq 1 / n \right. \quad .
$$

Answer the following questions for the sequences $\left\{ f _ { n } \right\}$ and $\left\{ g _ { n } \right\}$

(a) Find the pointwise limit on $[ 0 , \infty )$

(b) Explain how we know that the convergence cannot be uniform on $[ 0 , \infty )$

(c) Choose a small set over which the convergence is uniform and prove that this is the case.

2. (a) Consider the sequence of functions

$$
F _ { n } ( x ) = { \frac { x } { 1 + n x ^ { 2 } } } .
$$

Find the points on R where each $F _ { n } ( x )$ attains it maximum and minimum value. Use this to prove that $\{ F _ { n } \}$ converges uniformly on R.

(b) Prove that $G _ { n } ( x ) = x ^ { n } ( 1 - x )$ converges uniformly to 0 on [0, 1].

3. Let

$$
f _ { n } ( x ) = { \frac { n x + x ^ { 2 } } { 2 n } } \qquad { \mathrm { a n d } } \qquad g _ { n } ( x ) = { \frac { n x ^ { 2 } + 1 } { 2 n + x } }
$$

for each $x \in \mathbb { R }$ and $f ( x ) : = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ and $g ( x ) : = \operatorname* { l i m } _ { n  \infty } g _ { n } ( x )$ . Show that f and g are both differentiable on R in two ways: (i) by computing $f$ and g, and (ii) using theorems on uniform convergence.

4. (a) Show that $f ( x ) = \sum _ { n = 1 } ^ { \infty } { \frac { \cos ( 2 ^ { n } x ) } { 2 ^ { n } } }$ is continuous on all of R.

(b) Show that $g ( x ) = \sum _ { n = 1 } ^ { \infty } { \frac { x ^ { n } } { n ^ { 2 } } }$ is continuous on $[ - 1 , 1 ]$

5. Let

$$
f ( x ) = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { x ^ { 2 } + n ^ { 2 } } } .
$$

(a) Show that $f$ is a continuous function on R.

(b) Is $f$ differentiable? If so, is the derivative function $f ^ { \prime }$ continuous?

## Math 6100/Bonus Problems

1. Prove that if $\scriptstyle \sum _ { n = 0 } ^ { \infty } f _ { n } ( x )$ converges uniformly on a set A, then the sequence of functions $\left\{ f _ { n } \right\}$ must converge uniformly to 0 on A.

2. Let

$$
g ( x ) = \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { 1 + n ^ { 2 } x } } .
$$

(a) Prove that the series defining g does not converge uniformly on $( 0 , \infty )$

(b) Prove that g is however a continuous function on $( 0 , \infty )$

(c) Is g differentiable? If so, is the derivative function $g ^ { \prime }$ continuous?