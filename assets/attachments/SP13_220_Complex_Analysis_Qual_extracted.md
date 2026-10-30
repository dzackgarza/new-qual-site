# Math 220: Spring 2013 Qualifying Exam

<table><tr><td>Wedne</td><td>4:00p 1:00p</td><td>AP&amp;M 6402</td></tr></table>

Instructions: This is a 3-hour exam. No notes or textbooks are allowed. There are two parts to this exam. In Part I, you are asked to reiterate statements and proofs of some results from this course, and to anwer some true and false questions. In Part II, you are asked to solve several problems similar to those you’ve seen in homework sets and exams in 220ABC. Make sure to state all results and hypotheses used, and present your solutions clearly, with appropriate detail.

Notation: $\mathbb { D } = \{ z \in \mathbb { C } \colon | z | < 1 \}$ denotes the open unit disk; $\mathbb { D } ( z _ { 0 } , r ) = \{ z \in \mathbb { C } \colon | z - z _ { 0 } | < r \}$   
denotes an open disk; $\mathbb { A } ( z _ { 0 } ; r _ { 1 } , r _ { 2 } ) = \{ z \in \mathbb { C } : r _ { 1 } < | z - z _ { 0 } | < r _ { 2 } \}$ denotes an open annulus;   
and $\mathbb { C } _ { + } = \{ z \in \mathbb { C } \colon \operatorname { I m } ( z ) > 0 \}$ denotes the upper half-plane.

## Part I

1. (40 points) Choose 4 of the following theorems covered in this course, and write out their statements carefully and completely (5 points each). From among these, choose 2, and sketch their proofs (10 points each).

<table><tr><td>The Cauchy Estimates and Liouville&#x27;s Theorem t the Open Mapping Theorem</td><td>the Mittag-Leffler Theorem the Poisson Integral Formula</td></tr><tr><td>Rouché&#x27;s Theorem</td><td>the Maximum Modulus Principle</td></tr><tr><td>Hurwitz&#x27;s Theorem</td><td>the Monodromy Theorem</td></tr><tr><td>the Riemann Mapping Theorem</td><td>the Great Picard Theorem</td></tr><tr><td>Runge&#x27;s Theorem</td><td>Carathéodory&#x27;s Theorem</td></tr></table>

2. (20 points) Determine if the following statements are True or False. If True, give a brief proof. If False, give a counterexample or prove your assertion otherwise.

(a) (5 points) Let $U \subseteq \mathbb { C }$ be an open set, and let u: U → R be a non-constant harmonic function. Set

$$
Z = \left\{ z \in U \colon u _ { x } ( z ) = u _ { y } ( z ) = 0 \right\} .
$$

It is possible for Z to have an accumulation point in U.

(b) (5 points) There is a meromorphic function f on $\mathbb { C } \setminus ( 2 \mathbb { Z } ) ^ { 2 }$ such that, if $n , m \in 2  { \mathbb { Z } }$ are even integers, then f has a pole of order $n ^ { 2 } + m ^ { 2 }$ at $( n , m )$ , and if $( n , m ) \in \mathbb { Z } \times \mathbb { Z }$ with at least one odd, then f has a zero of order $n ^ { 2 } + m ^ { 2 }$ at $( n , m )$

(c) (5 points) Let $\{ u _ { n } \}$ be a sequence of harmonic functions in D. If $u _ { n }$ converges to u uniformly on compact subsets, then u is harmonic on D.

(d) (5 points) There is a sequence of holomorphic polynomials $p _ { n }$ such that

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { s u p } _ { 2 \leq | z | \leq 3 } \left| { \frac { 1 } { z ^ { 2 } ( z - 5 ) ^ { 3 } } } - p _ { n } ( z ) \right| = 0 .
$$

## Part II

3. (10 points) Determine the Laurent series expansions of the function $f \colon \mathbb { C } \setminus \{ 0 , \pm 2 \}  \mathbb { C }$ given by

$$
f ( z ) = { \frac { 1 } { z ^ { 3 } - 4 z } }
$$

in the annuli $\mathbb { A } ( 0 ; 0 , 2 )$ and $\mathbb { A } ( 0 ; 2 , \infty )$

4. (10 points) How many zeroes (counted with multiplicity) does the polyonmial

$$
f ( z ) = z ^ { 7 } - 2 z ^ { 5 } + 6 z ^ { 3 } - z + 1
$$

have in the unit disk D?

5. (10 points) Let $x _ { n }$ be a sequence of distinct real numbers. Show that there exists a function holomorphic on the upper half-plane, $f \in { \mathrm { H o l } } ( \mathbb { C } _ { + } )$ , such that $f ( i + x _ { n } ) = 0$ for all n if and only if

$$
\sum _ { n } { \frac { 1 } { x _ { n } ^ { 2 } + 4 } } < \infty .
$$

6. (10 points) Let $U \subset \mathbb { C }$ be the “rounded square” given by the intersection of the four open disks

$$
U = { \mathbb D } ( 1 , 2 ) \cap { \mathbb D } ( - 1 , 2 ) \cap { \mathbb D } ( i , 2 ) \cap { \mathbb D } ( - i , 2 ) .
$$

Let $S \subset \partial U$ be the curve $S = \{ - i + 2 e ^ { i t } \colon t \in ( { \textstyle { \frac { \pi } { 4 } } } , { \textstyle { \frac { \pi } { 2 } } } ) \}$ . Suppose that $f \in { \mathrm { H o l } } ( U )$ , and that for any sequence $z _ { n } \in U$ such that l $\mathrm { i m } _ { n \to \infty } z _ { n } \in S $ , it follows that $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } f ( z _ { n } ) = 0 } \end{array}$ Prove that $f \equiv 0$ .