# Real Analysis Qualifying Examination Fall, 2016

Name

ID number

<table><tr><td rowspan=1 colspan=1>Problem</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>Total</td></tr><tr><td rowspan=1 colspan=1>Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

## Instructions

• This is a three-hour, closed-book, closed-note, and no-calculator exam. The test booklet has 11 pages, including this cover page. There are 10 problems of total 200 points. To get credit, you must show your work. Partial credit will be given to partial answers.

• You may use without proof any results proved in the textbook or covered in the lecture. If you use such a result, please cite it by its name (if it has one) or explain what it is concisely. Please also verify explicitly all the hypotheses in the statement.

• You need to re-prove any result given as a homework problem, unless it is a statement proved in the text or in the lecture.

• If the statement you are asked to prove is exactly a result in the text or covered in the class, you still need to re-construct the proof instead of just citing the result.

(The rest of this page is left blank.)

Problem 1 (15 points). Let $( X , M )$ be a measurable space. Suppose $A _ { 1 } , A _ { 2 } , . . .$ are a sequence of members of M such that $A _ { i } \neq \varnothing$ for any i, $A _ { i } \cap A _ { j } = \emptyset$ for any i and $j$ with $i \neq j ,$ and $\textstyle X = \bigcup _ { i = 1 } ^ { \infty } A _ { j }$ . Let A be the smallest σ-algebra of subsets of X that contains all $A _ { 1 } , A _ { 2 } , \ldots$ Prove that A consists exactly of $\varnothing , X .$ , and all finite or countably infinite unions of $A _ { j } \ ( j \geq 1 )$

## Problem 2 (30 points).

(1) Let $f \in C ( \mathbb { R } )$ with $f ( 0 ) = 1$ . Calculate with justification the limit $\operatorname* { l i m } _ { k \to \infty } \int _ { 0 } ^ { \pi } f \left( \sin ^ { k } x \right) d x$

(2) Let $( X , { \mathcal { M } } , \mu )$ be a measure space with $\mu ( X ) < \infty$ . Assume that f and $\widecheck { f } _ { k } \ ( k = 1 , 2 , \ldots )$ are all real-valued, µ-measurable functions on X, and $f _ { k }  f$ in measure. Let $F \in C ( \mathbb { R } )$ be uniformly continuous. Prove that $F ( f _ { k } ) \to F ( f )$ in measure.

(3) Let m denotes the Lebesgue measure on Rn. Assume $g _ { k } \ \to \ g$ weakly in $L ^ { 1 } ( m )$ . Prove that $\partial ^ { \alpha } g _ { k } \to \partial ^ { \alpha } g$ in ${ \mathcal { D } } ^ { \prime } ( \mathbb { R } ^ { n } )$ for any multi-index α.

Problem 3 (20 points). Use the fact that

$$
\frac { 1 } { x } = \int _ { 0 } ^ { \infty } e ^ { - x t } d t \quad ( x > 0 )
$$

and the Fubini–Tonelli Theorem to evaluate the integral

$$
\int _ { 0 } ^ { \infty } e ^ { - \alpha x } { \frac { \sin ( \beta x ) } { x } } d x ,
$$

where $\alpha$ and $\beta$ are positive numbers. Be sure to verify the assumption in the Fubini–Tonelli Theorem. You may find the following formula useful:

$$
\int e ^ { a x } \sin b x d x = { \frac { e ^ { a x } } { a ^ { 2 } + b ^ { 2 } } } \left( a \sin b x - b \cos b x \right) + C .
$$

Problem 4 (20 points). Let $( X , { \mathcal { M } } , \mu )$ be a measure space with $\mu ( X ) = 1 , { \mathcal { M } } _ { 0 }$ a sub-σ- algebra of $\mathcal { M } .$ , and $\nu = \mu | _ { \mathcal { M } _ { 0 } }$ (the restriction of $\mu$ onto $\mathcal { M } _ { 0 } )$ . Let $f \in L ^ { 1 } ( \mathcal { M } , \mu )$ be real-valued. Use the Radon–Nikodym Theorem to prove that there exists a unique $g \in L ^ { 1 } ( \mathcal { M } _ { 0 } , \nu )$ such that

$$
\int _ { E } f d \mu = \int _ { E } g d \nu \qquad \forall E \in { \mathcal { M } } _ { 0 } .
$$

(Note that $g$ is, but $f$ may not be, measurable with respect to $\mathcal { M } _ { 0 } . \big )$

Problem 5 (15 points). Let X be a topological space. Suppose it is a sequentially compact (i.e., any sequence has a convergent subsequence). Prove that it is countably compact (i.e., any countable open cover of X has a finite subcover).

Problem 6 (20 points). Let $f \in C ^ { 1 } ( [ 0 , 1 ] )$ be such that f (1) = 0. Assume

$$
\int _ { 0 } ^ { 1 } x ^ { k } f ^ { \prime } ( x ) d x = 0 \qquad \forall k = 1 , 2 , \ldots .
$$

Prove that $f = 0$ identically on [0, 1].

Problem 7 (20 points). Recall that $c _ { 0 } = \{ ( a _ { 1 } , a _ { 2 } , \dots ) :$ : all $a _ { k } \in \mathbb { R }$ and $\scriptstyle \operatorname* { l i m } _ { k \to \infty } a _ { k } = 0 \}$ is a Banach space with respect to the usual component-wise addition and scalar multiplication, and the norm $\| ( a _ { 1 } , a _ { 2 } , \dotsc ) \| = \operatorname* { s u p } _ { k \geq 1 } \left| a _ { k } \right|$ . Let $\xi _ { k } \in \mathbb { R } \ ( k = 1 , 2 , . . . )$ . Assume that $\textstyle \sum _ { k = 1 } ^ { \infty } a _ { k } \xi _ { k }$ converges for any $( a _ { 1 } , a _ { 2 } , \ldots ) \in c _ { 0 }$ . Use the Principle of Uniform Boundedness to prove that $\begin{array} { r } { \sum _ { k = 1 } ^ { \infty } \left| \xi _ { k } \right| < \infty } \end{array}$

Problem 8 (20 points). Let H be a real Hilbert space and M a nonempty, closed subspace of H. Suppose $x _ { 0 } \in H \setminus M$ . Prove that

$$
\operatorname* { m i n } \{ \| x - x _ { 0 } \| : x \in M \} = \operatorname* { m a x } \{ \langle x _ { 0 } , y \rangle : y \in M ^ { \perp } , \| y \| = 1 \} .
$$

Problem 9 (20 points). Let $( X , { \mathcal { M } } , \mu )$ be a measure space with $\mu ( X ) < \infty$ . Let $f \in L ^ { \infty } ( \mu )$ with $\| f \| _ { \infty } > 0$ . Define

$$
\alpha _ { k } = \int _ { X } | f | ^ { k } d \mu \qquad { \mathrm { f o r ~ } } k = 1 , 2 , \ldots .
$$

Prove that

$$
\operatorname* { l i m } _ { k \to \infty } { \frac { \alpha _ { k + 1 } } { \alpha _ { k } } } = \| f \| _ { \infty } .
$$

Problem 10 (20 points). Let $\mu$ be a Radon measure on a locally compact Hausdorff space X .

(1) Let V be the union of all open subsets $U \subseteq X$ such that $\mu ( U ) = 0$ . Prove that V is open and $\mu ( V ) = 0$ . The complement of V is called the support of $\mu$ and is denoted by supp $( \mu )$

(2) Assume in addition that X is compact and $\mu ( X ) = 1$ . Denote $K = \operatorname { s u p p } \left( \mu \right)$ . Prove that K is compact, $\mu ( K ) = 1$ , and $\mu ( H ) < 1$ for every proper compact subset H of K.