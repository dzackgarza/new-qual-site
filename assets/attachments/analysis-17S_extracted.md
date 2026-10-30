## ANALYSIS QUAL: MARCH 30, 2017

Please be reminded that to pass the exam you need to show mastery of both real and complex analysis. Please choose at most 10 questions to answer, including at least 4 from problems 1–6 and 4 from problems 7–12. On the front of your paper indicate which 10 problems you wish to have graded.

Problem 1. Let $K \subset \mathbb { R }$ be a compact set of positive measure and let $f \in L ^ { \infty } ( \mathbb { R } )$ Show that the function

$$
F ( x ) = { \frac { 1 } { | K | } } \int _ { K } f ( x + t ) d t
$$

is uniformly continuous on R. Here $| K |$ denotes the Lebesgue measure of $K$

Problem 2. Let $f _ { n } : [ 0 , 1 ] \to [ 0 , \infty )$ be a sequence of functions, each of which is non-decreasing on the interval $[ 0 , 1 ] .$ . Suppose the sequence is uniformly bounded in $L ^ { 2 } ( [ 0 , 1 ] )$ . Show that there exists a subsequence that converges in $L ^ { 1 } ( [ 0 , 1 ] )$ .

Problem 3. Let $C ( [ 0 , 1 ] )$ denote the Banach space of continuous functions on the interval [0, 1] endowed with the sup-norm. Let $\mathcal { F }$ be a σ-algebra on $C ( [ 0 , 1 ] )$ so that for all $x \in [ 0 , 1 ]$ , the map defined via

$$
L _ { x } ( f ) = f ( x )
$$

is ${ \mathcal { F } } _ { - }$ measurable. Show that $\mathcal { F }$ contains all open sets.

Problem 4. For $n \geq 1$ , let $a _ { n } : [ 0 , 1 ) \to \{ 0 , 1 \}$ } denote the $n ^ { \mathrm { t h } }$ digit in the binary expansion of x, so that

$$
x = \sum _ { n \geq 1 } a _ { n } ( x ) 2 ^ { - n } \quad { \mathrm { f o r ~ a l l ~ } } x \in [ 0 , 1 ) .
$$

(We remove any ambiguity from this definition by requiring that lim inf $a _ { n } ( x ) = 0$ for all $x \in [ 0 , 1 ) . )$ Let $M ( [ 0 , 1 ) )$ denote the Banach space of finite complex Borel measures on [0, 1) and define linear functionals $L _ { n }$ on $M ( [ 0 , 1 ) )$ ) via

$$
L _ { n } ( \mu ) = \int _ { 0 } ^ { 1 } a _ { n } ( x ) d \mu ( x ) .
$$

Show that no subsequence of the sequence $L _ { n }$ converges in the weak-\* topology on $M ( [ 0 , 1 ) ) ^ { * }$

Problem 5. Let dµ be a finite complex Borel measure on [0, 1] such that

$$
\hat { \mu } ( n ) = \int _ { 0 } ^ { 1 } e ^ { 2 \pi i n x } d \mu ( x ) \to 0 \quad \mathrm { a s ~ } n \to \infty .
$$

Let dν be a finite complex Borel measure on [0, 1] that is absolutely continuous with respect to $d \mu$ . Show that

$$
{ \hat { \nu } } ( n ) \to 0 \quad { \mathrm { a s ~ } } n \to \infty .
$$

Problem 6. Let D be the closed unit disc in the complex plane, let $\left\{ p _ { n } \right\}$ be distinct points in the open disc D and let $r _ { n } > 0$ be such that the discs $D _ { n } = \{ z : | z - p _ { n } | \leq$ $r _ { n } \}$ satisfy

(i) $D _ { n } \subset \mathbb { D } ;$

(ii) $D _ { n } \cap D _ { m } = \emptyset$ if $n \neq m ;$ and

(iii) $\textstyle \sum r _ { n } < \infty .$

Prove ${ X } = { \overline { { \mathbb { D } } } } \setminus \bigcup _ { n } D _ { n }$ has positive area.

Hint: For $- 1 < x < 1$ consider $\# \{ n : D _ { n } \cap \{ R e z = x \} \neq \emptyset \}$

Problem 7. Let $f ( z )$ be a one-to-one continuous mapping from the closed annulus

$$
\{ 1 \leq | z | \leq R \}
$$

onto the closed annulus

$$
\{ 1 \leq | z | \leq S \}
$$

such that f is analytic on the open annulus $\{ 1 < | z | < R \}$ . Prove $S = R$

Problem 8. Let $a _ { 1 } , a _ { 2 } , . . . . , a _ { n }$ be $n \geq 1$ points in the disc $\mathbb { D } = \{ | z | < 1 \}$ (possibly with repetitions), so that the function

$$
B ( z ) = \prod _ { j = 1 } ^ { n } { \frac { z - a _ { j } } { 1 - { \overline { { a _ { j } } } } z } }
$$

has n zeros in D. Prove that the derivative $B ^ { \prime } ( z )$ has n − 1 zeros in D.

Problem 9. Let $f ( z )$ be an analytic function in the entire complex plane $\mathbb { C }$ and assume $f ( 0 ) \neq 0$ . Let $\left\{ a _ { n } \right\}$ be the zeros of $f ,$ repeated according to their multiplicities.

(a) Let $R > 0$ be such that $| f ( z ) | > 0$ on $| z | = R .$ . Prove

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } \log | f ( R e ^ { i \theta } ) | d \theta = \log | f ( 0 ) | + \sum _ { | a _ { n } | < R } \log { \frac { R } { | a _ { n } | } } .
$$

(b) Prove that if there are constants $C$ and λ such that $| f ( z ) | \leq C e ^ { | z | ^ { \lambda } }$ for all $z ,$ then

$$
\sum \left( { \frac { 1 } { | a _ { n } | } } \right) ^ { \lambda + \varepsilon } < \infty
$$

for all $\varepsilon > 0$ . Hint: Estimate # $\{ n : | a _ { n } | < R \}$ using (a) on $| z | \sim 2 R$

Problem 10. Let $a _ { 1 } , \ldots , a _ { n }$ be $n \geq 1$ distinct points in C and let $\Omega \ : = \ : \mathbb { C } \ : \backslash$ $\{ a _ { 1 } , \ldots , a _ { n } \}$ . Let $H ( \Omega )$ be the vector space of real-valued harmonic functions on Ω and let $R ( \Omega ) \subset H ( \Omega )$ be the space of real parts of analytic functions on Ω. Prove the quotient space $\frac { \dot { H } ( \Omega } { R ( \Omega ) }$ has dimension $n ,$ find a basis for this space, and prove it is a basis.

Problem 11. Let $1 \leq p < \infty$ and let $U ( z )$ be a harmonic function on the complex plane C such that

$$
\iint _ { \mathbb { R } \times \mathbb { R } } | U ( x + i y ) | ^ { p } d x d y < \infty .
$$

Prove $U ( z ) = 0$ for all $z = x + i y \in \mathbb { C }$

Problem 12. Let $0 < \alpha < 1$ and let $f ( z )$ be an analytic function on the unit disc D. Prove that if

$$
| f ( z ) - f ( w ) | \leq C | z - w | ^ { \alpha }
$$

for all $z , w \in \mathbb { D }$ and some constant $C \in \mathbb { R }$ , then there is constant $A = A ( C ) < \infty$ such that

$$
| f ^ { \prime } ( z ) | \leq A ( 1 - | z | ) ^ { \alpha - 1 } .
$$