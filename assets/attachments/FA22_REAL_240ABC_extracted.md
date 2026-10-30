Name:

ID:

# Real Analysis Qualifying Exam (Fall, 2022)

Instructions: Clearly explain and justify your answers. You may cite theorems from the textbook or lecture. When doing so please cite the result by its name or explain concisely what it is, and explicitly verify any hypothesis. To apply results from homework exercises you must reprove them. In multi-part problems, you are allowed to use the results from prior parts even if you were unable to solve them.

<table><tr><td rowspan=1 colspan=1>Problem</td><td rowspan=1 colspan=1>Points</td></tr><tr><td rowspan=1 colspan=1>Problem 1(30 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 2(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 3(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 4(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 5(20 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 6(10 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Problem 7(30 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Total(150 points)</td><td rowspan=1 colspan=1></td></tr></table>

Problem 1. Determine if each of the following statements is true or false. If you answer is true, then give a brief proof. If your answer is false, then give a counterexample or prove your assertion.

1. If $( X , { \mathcal { M } } , \mu )$ is a σ-finite measure space, then there exists a finite measure ν on $\mathcal { M }$ such that $\nu < < \mu$ and $\mu < < \nu$

2. Let m denote Lebesgue measure on $\mathbb { R } .$ . If $f \in L ^ { 1 } ( \mathbb { R } , m )$ and $\begin{array} { r } { \int _ { a } ^ { a + 1 } | f ( x ) | ^ { 2 } d x < \infty } \end{array}$ for every $a \in \mathbb { R }$ , then $f \in L ^ { 2 } ( \mathbb { R } , m )$

3. Let f be a tempered distribution on $\mathbb { R } ^ { n }$ , namely f is a distribution which belongs to the dual space of the Schwartz space $S \ ( { \mathrm { i . e . } } \ f \ \in \ S ^ { \prime } )$ . Define the Fourier transformation of $f , \ { \hat { f } } ( \phi )$ (or the pairing $\langle \hat { f } , \phi \rangle )$ by $\langle f , \hat { \phi } \rangle$ for $\phi \in { \mathcal { S } } \subset L ^ { 1 }$ (with $\hat { \phi } \in S )$ . Recall that for f a distribution, $\langle \tau _ { y } f , \phi \rangle = \langle f , \tau _ { - y } \phi \rangle$ for compact supported function φ. Then it must hold $( \tau _ { y } f ) \hat { ( } \xi ) = e ^ { - 2 \pi \sqrt { - 1 } \langle \xi , y \rangle } \hat { f } ( \xi ) , \forall y \in \mathbb { R } ^ { n }$

Recall that for a regular function $f , ( \tau _ { y } f ) ( x ) = f ( x - y )$ whenever the definition makes sense.

Problem 2. Let $( X , { \mathcal { M } } , \mu )$ be a measure space with $\mu ( X ) < \infty$ . Let $1 \leq p < \infty$ , let $f , f _ { n } \in$ $L ^ { p } ( X , \mu )$ for $n \in \mathbb { N }$ , and assume that $f _ { n }  f$ pointwise µ-almost-everywhere. Prove that $\| f _ { n } - f \| _ { p } \to 0$ if and only if $\| f _ { n } \| _ { p } \to \| f \| _ { p } .$

(Note: You are not allowed to use the generalized Dominated Convergence Theorem unless you prove it.)

Problem 3. Set $\begin{array} { r } { E = \bigcup _ { m \in \mathbb { Z } } [ 2 m , 2 m + 1 ) } \end{array}$ and $P = \chi _ { E } - \chi _ { \mathbb { R } \backslash E }$ , so that $P ( x )$ is 1 if the greatest integer less than or equal to x is even and is −1 if it is odd. Define $S _ { n } ( x ) = P ( 1 0 ^ { n } \cdot x )$ . Prove that for every $f \in L ^ { 1 } ( \mathbb { R } )$

$$
\int _ { \mathbb { R } } S _ { n } ( x ) f ( x ) \ d x \to 0 \quad { \mathrm { a s ~ } } n \to \infty .
$$

## Problem 4. Let $( X , d )$ be a compact metric space.

1. State the definition of what it means for a metric space to be separable, and what it means for a topological space to be second countable.

2. Prove that X is second countable.

3. Prove that C(X, R) equipped with the uniform norm is separable. (Hint: Use (2) and the Stone-Weierstrass Theorem)

Problem 5. Let H be a Hilbert space, let $T : { \mathcal { H } } \to { \mathcal { H } }$ be a bounded linear operator, and let $T ^ { * } : { \mathcal { H } } \to { \mathcal { H } }$ denote the adjoint of $T$ (which is the bounded linear operator defined by the relation $\langle T x , y \rangle = \langle x , T ^ { * } y \rangle$ for all $x , y \in { \mathcal { H } } )$ . Recall that a linear map $S : \mathcal { H } \to \mathcal { H }$ is bounded below if there is a constant $c > 0$ such that $\| S x \| \geq c \| x \|$ for all $x \in \mathcal H$ .

Prove that $T$ is invertible (with bounded inverse) if and only if both T and $T ^ { * }$ are bounded below.

Problem 6. Suppose that µ is a Radon measure on X (a locally compact Hausdorff space).   
Assume $\phi \in L ^ { 1 } ( \mu )$ and $\phi \geq 0$ . Prove that $\nu ( E ) \doteq \int _ { E } \phi d \mu$ is a Radon measure.

Problem 7. Let F be a distribution on $\mathbb { R } ^ { n }$ such that the support of $F , \operatorname { s u p p } ( F ) = \{ 0 \}$ . Let $\alpha = ( \alpha _ { 1 } , \cdots , \alpha _ { n } )$ with $\alpha _ { i }$ being nonnegative integers, and $\delta$ be the delta measure centered at 0, which can also be viewed as a distribution on $\mathbb { R } ^ { n }$

1. Prove that there exists a natural number N and $C > 0$ such that

$$
| \langle F , \phi \rangle | \leq C \sum _ { | \alpha | \leq N } \operatorname* { s u p } _ { | x | \leq 1 } | \partial ^ { \alpha } \phi ( x ) | , \forall \phi \in C _ { c } ^ { \infty } .
$$

Here $\langle \cdot , \cdot \rangle$ is the pairing of the distributions and smooth functions with compact supports.

2. If $\phi \in C _ { c } ^ { \infty }$ and $\partial ^ { \alpha } \phi ( 0 ) = 0 , \forall | \alpha | \leq N$ , then $\langle F , \phi \rangle = 0$

3. There exist constant $c _ { \alpha } \left( | \alpha | \leq N \right)$ such that $\begin{array} { r } { F = \sum _ { | \alpha | \leq N } c _ { \alpha } \partial ^ { \alpha } \delta } \end{array}$