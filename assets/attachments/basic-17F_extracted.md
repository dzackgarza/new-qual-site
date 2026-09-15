## BASIC EXAM: FALL 2017

## Test instructions:

Write your UCLA ID number on the upper right corner of each sheet of paper you use. Do not write your name anywhere on the exam!!!

All answers must be justified. If you wish to use a known theorem, make sure to give a full and precise statement.

Work out FIVE of the linear algebra problems (1-6) and FIVE of the analysis problems (7-12). Clearly indicate which 10 problems you want us to grade. To pass the exam successfully, candidates must fare satisfactorily in both parts.

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>12</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Problem 1. Let $V = \{ f ( X ) = a _ { 0 } + a _ { 1 } X + a _ { 2 } X ^ { 2 } + a _ { 3 } X ^ { 3 } | a _ { 0 } , \dots , a _ { 3 } \in \mathbb { C } \}$ be the complex vector space of polynomials in the variable X, of degree at most 3.

(a) [2 pts] Show that V is an inner product space with $\textstyle \langle f , g \rangle = \int _ { - 1 } ^ { 1 } f ( t ) { \overline { { g ( t ) } } } d t .$

(b) [8 pts] Find an orthonormal basis of V .

Problem 2. Let $n \geq 1$ be an integer and A and B be n × n-matrices.

(a) [5 pts] Show that AB and BA have the same characteristic polynomial if A is invertible.

(b) [5 pts] Is the result true without assuming invertibility? Prove your claim.

Problem 3. [10 pts] Solve the following linear system of differential equations, for two functions $x _ { i } : \mathbb { R }  \mathbb { R }$ , for i = 1 and 2, with derivatives $\begin{array} { r } { x _ { i } ^ { \prime } ( t ) = \frac { d x _ { i } } { d t } ( t ) ; } \end{array}$

$$
\left\{ \begin{array} { r c l l } { { x _ { 1 } ^ { \prime } } } & { { = } } & { { 6 x _ { 1 } } } & { { - \phantom { } x _ { 2 } } } \\ { { x _ { 2 } ^ { \prime } } } & { { = } } & { { 2 x _ { 1 } } } & { { + 3 x _ { 2 } } } \end{array} \right.
$$

Problem 4. Let V be a vector space over the field $F = \mathbb { R }$ and let $V ^ { * } = \mathrm { L i n } _ { F } ( V , F )$ be the dual space (of F -linear maps from V to F ). Let $\boldsymbol { B } = \{ e _ { i } \} _ { i \in I }$ be a basis of V . For each $i \in I .$ , define the dual forms $e _ { i } ^ { \# } \in V ^ { * }$ by the rule

$$
e _ { i } ^ { \# } ( e _ { j } ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } i = j , } \\ { 0 } & { { \mathrm { e l s e } } . } \end{array} \right. }
$$

(a) [2 pts] Show that the vectors $\{ e _ { i } ^ { \# } \} _ { i \in I }$ are linearly independent in $V ^ { * }$

(b) [8 pts] Give necessary and sufficient conditions on V for these vectors to form a basis of $V ^ { * }$ . Prove your claim.

Problem 5. Let V and W be two infinite-dimensional vector spaces over the field $F = \mathbb { C }$ . Let Lin $_ { F } ( V , W )$ be the F -vector space of F -linear maps from V to W .

(a) [4 pts] Is $X = \{ f \in \operatorname { L i n } _ { F } ( V , W ) | f$ has finite rank} a subspace of $\mathrm { L i n } _ { F } ( V , W ) ?$

(b) [4 pts] Same question for $Y = \{ f \in \operatorname { L i n } _ { F } ( V , W ) | \operatorname { K e r } ( f )$ is finite dimensional}.

(c) [2 pts] What is the intersection X ∩ Y ?

Prove all claims in full detail.

Problem 6. For each of the following three fields F (separately), is it true that every symmetric matrix $A \in \mathrm { M } _ { 2 \times 2 } ( F )$ is diagonalizable?

(a) [2 pts] For F = R.

(b) [3 pts] For $F = \mathbb { C }$

(c) [5 pts] For $F = \mathbb { F } _ { 3 } = \mathbb { Z } / 3 \mathbb { Z } .$ the field with 3 elements.

Supply proofs/counterexamples (or cite the relevant theorems) for all parts of this problem.

Problem 7. [10 pts] Let $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ be a non-increasing sequence of positive real numbers such that $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n } < \infty$ . Prove that

$$
\operatorname* { l i m } _ { n \to \infty } n a _ { n } = 0 .
$$

Problem 8. Let $a < b$ be real numbers and $f \colon [ a , b ]  \mathbb { R }$ a function such that $L ( x ) = \operatorname* { l i m } _ { y \to x } f ( y )$ exists for all $x \in [ a , b ]$ (with one-sided limits at $x = a , b )$ .

(a) [4 pts] Prove that L is continuous on [a, b].

(b) [3 pts] Prove that $\{ x \in [ a , b ] \colon f ( x ) \neq L ( x ) \}$ is countable.

(c) [3 pts] Prove that f is Riemann integrable.

Problem 9. [10 pts] Let $( X , \rho )$ be a complete metric space and $f \colon X \to X$ a function. Writing $f ^ { n }$ for the n-th iterate of f , denote

$$
c _ { n } : = \operatorname* { s u p } _ { x , y \in X \atop x \neq y } { \frac { \rho { \big ( } f ^ { n } ( x ) , f ^ { n } ( y ) { \big ) } } { \rho ( x , y ) } } .
$$

Assuming that $\textstyle \sum _ { n = 1 } ^ { \infty } c _ { n } < \infty$ , prove that f has a unique fixed point in X.

Problem 10. [10 pts] Let $a < b$ be real numbers and $f \colon [ a , b ]  \mathbb { R }$ a continuous function such that $\textstyle \int _ { a } ^ { b } f ( x ) x ^ { n } \mathrm { d } x = 0$ for each integer $n \geq 0$ . Prove that $f = 0$

Problem 11. [10 pts] Prove Young’s inequality: Let $p , q \in ( 1 , \infty )$ obey $\textstyle { \frac { 1 } { p } } + { \frac { 1 } { q } } = 1$ Then for each $a , b \geq 0$ ,

$$
a b \leq { \frac { a ^ { p } } { p } } + { \frac { b ^ { q } } { q } } .
$$

Problem 12. [10 pts] Let X be a compact metric space and $C ( X )$ the space of continuous real-valued functions on X endowed with the supremum norm. Let ${ \mathcal { F } } \subset C ( X )$ be non-empty. Prove the following version of Arzel\`a-Ascoli’s theorem:

F is compact $\Leftrightarrow \_ { \mathcal { F } }$ is closed, bounded and equicontinuous Give precise definitions of all terms used in this equivalence.