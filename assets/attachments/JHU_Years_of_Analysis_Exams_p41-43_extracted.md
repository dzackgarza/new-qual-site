8. Prove that any function $f \in L ^ { 1 } ( I ) \cap L ^ { 2 } ( I )$ for any interval $I \subset \mathbb { R }$ must be in $L ^ { p } ( I )$ for all $p$ between 1 and 2.

9. Suppose that f is in $L ^ { 1 } ( \mathbb { R } )$ . Prove directly (i.e., without citing properties of the Fourier transform) that the function

$$
\widehat { f } ( t ) = \int _ { \mathbb { R } } e ^ { - i x t } f ( x ) d x
$$

is uniformly continuous and ${ \widehat { f } } ( t ) \to 0 { \mathrm { ~ a s ~ } } t \to \infty$

10. Suppose that $f$ is in $L ^ { 1 } ( \mathbb { R } )$ . Prove that

$$
\operatorname* { l i m } _ { h \to 0 } \int _ { \mathbb { R } } | f ( x + h ) - f ( x ) | = 0 .
$$

11. Suppose that $f _ { n }$ is a sequence of functions in $L ^ { 2 } ( [ 0 , 1 ] )$ that converges weakly to a function $f \in L ^ { 2 } ( [ 0 , 1 ] )$ . Either prove that lim $\begin{array} { r } { \operatorname* { s u p } _ { n  \infty } \vert \vert f _ { n } \vert \vert _ { L ^ { 2 } ( [ 0 , 1 ] ) } < \infty } \end{array}$ or give a counter-example.

12. Let $f _ { j }$ be an orthonormal sequence in $L ^ { 2 } ( [ 0 , 1 ] )$ . Prove that

$$
S _ { n } = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } f _ { j }
$$

converges to zero a.e.

# ANALYSIS QUALIFYING EXAM SEPTEMBER 2005

Do all 8 problems.
All problems are equally weighted.
Time: 3 hours.

Show all work.
In each solution, state any theorems you are applying and verify that the hypotheses are satisfied.

1. Let $\left\{ f _ { n } \right\}$ be a sequence of Lebesgue measurable functions on [0, 1], and assume that

$$
\int _ { 0 } ^ { 1 } | f _ { n } ( x ) | ^ { 2 } d x \leq { \frac { 1 } { n ^ { 2 } } } .
$$

Show that:

$$
\operatorname * { l i m } _ { n  \infty } f _ { n } ( x ) = 0 \quad \mathrm { a . e . ~ o n } [ 0 , 1 ] .
$$

2. Let $f \in L ^ { 1 } ( \mathbb { R } , d x )$ . Prove that

$$
\operatorname* { l i m } _ { h \to 0 } \int _ { \mathbb { R } } | f ( x + h ) - f ( x ) | d x = 0 .
$$

3. Let $g _ { n }$ be a sequence of functions in $L ^ { 1 } ( S ^ { 1 } , d \theta )$ where $S ^ { 1 }$ is the unit circle $\{ e ^ { i \theta } : 0 \leq \theta \leq 2 \pi \}$ We say that $g _ { n } \ \to \ 0$ weakly if $\begin{array} { r } { \int _ { S ^ { 1 } } g _ { n } ( e ^ { i \theta } ) f ( e ^ { i \theta } ) d \theta  0 } \end{array}$ a s $n \to \infty$ for all $f \in C ( S ^ { 1 } )$

Question: Suppose that $\left\{ g _ { n } \right\}$ is a sequence in $L ^ { 1 } ( S ^ { 1 } , d \theta )$ and $\begin{array} { r } { \int _ { S ^ { 1 } } e ^ { i k \theta } g _ { n } ( e ^ { i \theta } ) d \theta  0 } \end{array}$ a s $n \to \infty$ for all $k \in \mathbb { Z }$ . Need $g _ { n } \to 0$ weakly?
Give either a proof or a counterexample.

4. Suppose that $\left\{ f _ { n } \right\}$ is a sequence of elements of a Hilbert space X and that $f _ { n } \to f$ weakly $( \mathrm { i . e . , } ( f _ { n } , g )  ( f , g )$ for all $g \in X )$

(a) Show that

$$
\| f \| \leq \operatorname* { l i m } _ { n \to \infty } { \big \| } f _ { n } { \big \| } .
$$

Give an example showing that strict inequality can occur.

(b) Suppose in addition that $\left. f \right. = \operatorname* { l i m } _ { n \to \infty } \left. f _ { n } \right.$ . Show that $f _ { n } \to f$ in norm.

5. Use contour integration to evaluate

$$
\int _ { 0 } ^ { + \infty } { \frac { d x } { x ^ { 1 / 3 } ( 1 + x ) } } .
$$

Hint: Consider the contour beginning with the segment from $\varepsilon$ to $R ,$ then traversing a circle of large radius $R ,$ then going back to $\varepsilon ,$ and finally traversing a circle of small radius ε.

CONTINUED ON NEXT PAGE

6. (a) Describe all the automorphisms of the upper half plane $H = \left\{ z \in \mathbb { C } : \mathrm { R e } \ z > 0 \right\}$ (holomorphic bijective maps from H onto H).

(b) Describe all the automorphisms of C (holomorphic bijective maps from C onto C).

7. How many zeros does the polynomial

$$
z ^ { 9 } + z ^ { 5 } - 8 z ^ { 3 } - z + 2
$$

have between the circles $\{ | z | = 1 \}$ and $\{ | z | = 2 \}$ . Justify your answer.

8. Let $H = \left\{ z \in \mathbb { C } : \mathrm { R e } \ z > 0 \right\}$ denote the upper half plane.

(a) Does there exist a surjective holomorphic map $f : H \to \mathbb { C } ?$ Either give an example or prove that one does not exist.

(b) Does there exist a surjective holomorphic map $f : \mathbb { C } \to H ?$ Either give an example or prove that one does not exist.
