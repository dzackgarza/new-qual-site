## Qualifying Examination in Real Variables, August 2015

## General Instructions:

(1) For each problem, use a new sheet.

(2) All vector spaces are over $\mathbb { R }$ and all functions are R-valued.

(3) Unless otherwise stated, you may use results from Folland’s book, but you need to state them carefully (it is not necessary to remember their names).

## Problems:

(1) Let $f : \mathbb { R } \to \mathbb { R }$ be a Borel measurable function. For each $t \in \mathbb { R }$ define

$$
f _ { t } ( x ) = f ( t + x ) , \quad x \in \mathbb { R } .
$$

Prove that $f _ { t } ( x )$ is a Borel measurable function $( { \mathrm { i n ~ } } x )$ for each fixed $t \in \mathbb { R }$

(2) Justify the statement that

$$
\int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } { \frac { ( x - y ) \sin ( x y ) } { x ^ { 2 } + y ^ { 2 } } } d x d y = \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } { \frac { ( x - y ) \sin ( x y ) } { x ^ { 2 } + y ^ { 2 } } } d y d x .
$$

(3) Assume that $\left( f _ { n } \right)$ is a sequence in $C [ 0 , 1 ]$

a) Show that $\left( f _ { n } \right)$ converges weakly to 0 if and only if $\left( f _ { n } \right)$ is bounded in $C [ 0 , 1 ]$ and $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } f _ { n } ( t ) = 0 } \end{array}$ for all $t \in [ 0 , 1 ]$

b) Show that if $\left( f _ { n } \right)$ converges weakly in $C [ 0 , 1 ]$ , then it converges in norm in $L _ { p } [ 0 , 1 ]$ for all $1 \leq p < \infty$

(4) Let A be a Lebesgue null set in R. Prove that

$$
B : = \{ e ^ { x } : x \in A \}
$$

is also a null set.

(5) a) Define absolute continuity of a function $f : \mathbb { R } \to \mathbb { R }$ and of a function $f : [ a , b ]  \mathbb { R }$

b) Show that if f and g are absolutely continuous on $[ a , b ]$ $a , b \in \mathbb { R } , a < b ,$ then $f \cdot g$ is absolutely continuous on $[ a , b ]$

c) Give an example to show that (b) is false if $[ a , b ]$ is replaced by R.

(6) Let X and Y be Banach spaces and $T : X  Y$ be a one-toone, bounded and linear operator for which the range $T ( X )$ is closed in Y . Show that for each continuous linear functional $\phi$ on X there is a continuous linear functional $\psi$ on $Y .$ , so that $\phi = \psi \circ T$

(7) State the Open Mapping Theorem and the Closed Graph Theorem for Banach spaces. Derive the Open Mapping Theorem from the Closed Graph Theorem.

(8) Let Y be a closed subspace of a Banach space X, with norm $\| \cdot \|$ . Let $\| \cdot \|$ be a norm on Y which is equivalent to $\| \cdot \|$ meaning that there is a $C \geq 1$ so that

$$
{ \frac { 1 } { C } } \| y \| \leq \| y \| \leq C \| y \| { \mathrm { ~ f o r ~ a l l ~ } } y \in Y .
$$

Let S be the set of all linear functionals $\phi : X  \mathbb { R }$ , so that

(a) $| \phi ( y ) | \leq \| y \|$ for all $y \in Y$ , and

(b) $| \phi ( x ) | \leq C \| x \|$ for all $x \in X$

Prove the following statements

i) $\begin{array} { r } { \| x \| : = \operatorname* { s u p } _ { \phi \in S } | \phi ( x ) | , x \in X } \end{array}$ , defines a norm on $X$

ii) $\| y \| = \| y \| { \mathrm { ~ f o r ~ } } y \in Y .$

iii) The norms $\| \cdot \|$ and $\| \cdot \|$ are equivalent on X.

(9) Let f be increasing on [0, 1] and let

$$
g ( x ) = \operatorname* { l i m } _ { h \to 0 } \operatorname* { s u p } _ { } \frac { f ( x + h ) - f ( x - h ) } { 2 h } , \quad \mathrm { ~ f o r ~ } 0 < x < 1 .
$$

Prove that if $A = \{ x \in ( 0 , 1 ) : g ( x ) > 1 \}$ then

$$
f ( 1 ) - f ( 0 ) \geq m ^ { * } ( A ) .
$$

(10) a) State a version of the Stone-Weierstrass Theorem.

b) Let A be a uniformly dense subspace of $C [ 0 , 1 ]$ and let

$$
B = { \Big \{ } F ( x ) : F ( x ) = \int _ { 0 } ^ { x } f ( t ) d t , \quad 0 \leq x \leq 1 , f \in A { \Big \} } .
$$

Prove that B is uniformly dense in

$$
C _ { 0 } [ 0 , 1 ] : = \{ g \in C [ 0 , 1 ] : g ( 0 ) = 0 \} .
$$

c) Prove that the span of $\{ \sin ( n x ) : n \in \mathbb { N } \}$ is dense in $C _ { 0 } [ 0 , 1 ]$