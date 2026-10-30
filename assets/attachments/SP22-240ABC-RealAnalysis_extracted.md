ID:

# Real Analysis Qualifying Exam (Spring, 2022)

Instructions: Clearly explain and justify your answers. You may cite theorems from the textbook or lecture. When doing so please cite the result by its name or explain concisely what it is, and explicitly verify any hypothesis. To apply results from homework exercises you must reprove them. In multi-part problems, you are allowed to use the results from prior parts even if you were unable to solve them.

<table><tr><td rowspan=1 colspan=1>Problem</td><td rowspan=1 colspan=1>Points</td></tr><tr><td rowspan=1 colspan=1>Problem 1(30 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 2(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 3(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 4(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 5(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 6(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 7(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Total(150 points)</td><td rowspan=1 colspan=1></td></tr></table>

Problem 1. Determine if each of the following statements is true or false. If you answer is true, then give a brief proof. If your answer is false, then give a counterexample or prove your assertion.

1. If $f , g : \mathbb { R }  \mathbb { R }$ belong to $L ^ { 1 } ( \mathbb { R } )$ and satisfy $\textstyle \int _ { - \infty } ^ { x } f ( t ) d t \leq \int _ { - \infty } ^ { x } g ( t ) d t$ for all $x \in \mathbb { R }$ , then $f \leq g$ almost-everywhere.

2. Let $( X , { \mathcal { M } } , \mu )$ be a finite measure space, and let $f _ { n } \in L ^ { 2 } ( X )$ be a sequence. If $\mathrm { s u p } _ { n \in \mathbb { N } } \| f _ { n } \| _ { 2 } <$ ∞ and $f _ { n } \to f$ almost-everywhere, then $\textstyle { \int _ { X } f _ { n } \ d \mu \to \int _ { X } f \ d \mu }$

3. Let $\mu$ be a Radon measure on a LCH space (a locally compact Hausdorff space) X and let A be an open subset of X. Define $\mu _ { A } ( E ) = \mu ( A \cap E )$ . Then $\mu _ { A }$ is a Radon measure.

Problem 2. Let $( f _ { n } ) _ { n \in \mathbb { N } }$ be a sequence of Lebesgue measurable functions defined on $[ 0 , 1 ]$ Assume there is a $C > 0$ such that $| f _ { n } ( x ) | \leq C$ for almost-every $x \in [ 0 , 1 ]$ and every n, and assume that $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { a } f _ { n } ( x ) \ d x = 0 } \end{array}$ for every $a \in ( 0 , 1 )$ . Prove that

$$
\operatorname* { l i m } _ { n \to 0 } \int _ { 0 } ^ { 1 } g ( x ) f _ { n } ( x ) \ d x = 0
$$

for every function $g \in L ^ { 1 } ( [ 0 , 1 ] )$

Problem 3. Let $f \in L ^ { 1 } ( ( 0 , \infty ) \times \mathbb { R } )$ and for $n \in \mathbb { N }$ define $g _ { n } : \mathbb { R } \to \mathbb { R }$ by the formula

$$
g _ { n } ( x ) = \int _ { 0 } ^ { \infty } e ^ { - \lambda } f ( n \lambda , x ) ~ d \lambda .
$$

Prove that $g _ { n }$ converges to 0 almost-everywhere and in $L ^ { 1 } ( \mathbb { R } )$

Problem 4. Let H be a Hilbert space and let $U \in L ( \mathcal { H } , \mathcal { H } )$ be unitary, meaning U is invertible and $\langle U x , y \rangle = \langle x , U ^ { - 1 } y \rangle$ for all $x , y \in { \mathcal { H } }$ •

1. Let Ran(I − U) denote the image of $I - U$ . Prove that $\overline { { \mathrm { R a n } ( I - U ) } } ^ { \perp } = \mathrm { K e r } ( I - U )$

2. Set $\begin{array} { r } { S _ { n } = \frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } U ^ { j } } \end{array}$ , and let P be the orthogonal projection map from H to $\mathrm { K e r } ( I - U )$ Prove that $S _ { n }  P$ in the strong operator topology. (This is von Neumann’s Mean Ergodic Theorem)

Problem 5. Let $X \subseteq \mathbb { R }$ be a Borel set, let $\mu$ be the restriction of Lebesgue measure to $X$ , and let $1 \leq p < q < \infty$ . Assume that $L ^ { q } ( X , \mu ) \subseteq L ^ { p } ( X , \mu )$ and let $T : L ^ { q } ( X , \mu ) \to L ^ { p } ( X , \mu )$ be the inclusion map. Prove that $T$ is bounded and that $\mu ( X ) < \infty$

Problem 6. Let X be a LCH (a locally compact Hausdorff space). Let $\mu$ be a σ-finite measure on X such that for any measurable set E, $\mu ( E ) = \operatorname* { i n f } \{ \mu ( U ) , E \subset U , U$ open}. Let $f \geq 0$ b e a bounded measurable function. Prove that if $\textstyle \mu ( U ) = \int _ { U } f d \mu$ whenever $U$ is open then $f = 1$ $\mu { - } \mathrm { a . e }$

## Problem 7.

1. Compute the 2nd and 3-rd (distributional) derivatives of $f ( | x | )$ , namely find the expression of $\textstyle { \frac { d ^ { 2 } } { d x ^ { 2 } } } f ( | x | )$ and ${ \frac { d ^ { 3 } } { d x ^ { 3 } } } f ( | x | )$ in an expression of locally integrable functions or measures and their derivatives, where $x \in \mathbb { R }$ and $f \in C ^ { n } ( \bar { \mathbb { R } } _ { + } )$ with $n \geq 3$ . (Hint: You may expressed your answers in terms of $f$ , its derivatives and the Delta measure.)

2. Find a formula for the n-th distributional derivative of $f ( | x | )$