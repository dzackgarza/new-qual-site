## Basic Exam Fall 08

## Instructions

Solve any 10 of the following 12 problems.
You will not receive credit for more than 10 problems.
Indicate which problems you wish to be graded by circling the corresponding numbers.

(1) For which of the values $a = 0 , 1 , 2$ is the function $f ( t ) = t ^ { a }$ uniformly continuous on $\lbrack 0 , \infty ) \ ?$ Prove your assertions.

(2) Suppose that A is a non-empty connected subset of $\mathbb { R } ^ { 2 }$ (a) Prove that if A is open, then it is path connected.

(b) Is (a) true if A is closed?
Prove your assertion.

(3) Give an example of a sequence of continuous real-valued functions $f _ { n }$ on [0, 1] such that $f ( t ) = \operatorname* { l i m } f _ { n } ( t )$ is continuous, but $\textstyle \int _ { 0 } ^ { 1 } f _ { n } ( t ) d t$ does not converge to $\textstyle \int _ { 0 } ^ { 1 } f ( t ) d t$

(4) (a) Suppose that K and F are subsets of $\mathbb { R } ^ { 2 }$ with K closed and bounded and F closed.
Prove that if $K \cap F = \emptyset$ , then $d ( K , F ) >$ 0. Recall that

$$
d ( K , F ) = \operatorname* { i n f } \{ d ( x , y ) : x \in K , y \in F \} .
$$

(b) Is (a) true if K is just closed?
Prove your assertion.

(5) A rearrangement of a series $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n }$ is a series of the form $\scriptstyle \sum _ { k = 1 } ^ { \infty } a _ { n ( k ) }$ , where n : $\mathbb { N } \to \mathbb { N }$ is a bijection (i.e. one-to-one and onto).
Show that there is a rearrangement of the series $\scriptstyle \sum _ { n = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { n } } { n } }$ which converges to π.

(6) Suppose that V is an n-dimensional vector space $( n \in \mathbb { N } )$ and that $T : V \to V$ is a linear mapping.
Prove that

$$
\mathrm { d i m \ k e r } T + \mathrm { d i m \ r a n g e } T = n
$$

Note: Do not just quote a standard theorem.

(7) Suppose that $T = [ t _ { i j } ]$ is a complex n × n matrix, and that $\lambda _ { 1 } , \ldots , \lambda _ { r }$ are distinct eigenvalues of $T ,$ with corresponding non-zero eigenvectors $v _ { 1 } , \ldots , v _ { r }$ Show that $v _ { 1 } , \ldots , v _ { r }$ are linearly independent.

(8) Must the eigenvectors of a linear transformation $T : \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$ span $\mathbb { C } ^ { n }$?
Prove your assertion.

(9) (a) Prove that any linear transformation $T : \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$ must have an eigenvector.

(b) Is (a) true for any linear transformation $T : \mathbb { R } ^ { n } \to \mathbb { R } ^ { n } ?$

(10) Given $v = ( v _ { 1 } , \ldots , v _ { n } ) \in \mathbb { R } ^ { n }$ , we let $\| v \| = ( \sum | v _ { j } | ^ { 2 } ) ^ { 1 / 2 }$ . If $f =$ $( f _ { 1 } , \ldots , f _ { n } ) : [ a , b ] \to \mathbb { R } ^ { n }$ is a continuous function, we define

$$
\int _ { a } ^ { b } f ( t ) d t = \left( \int _ { a } ^ { b } f _ { 1 } ( t ) d t , \dots , \int _ { a } ^ { b } f _ { n } ( t ) d t \right) .
$$

Prove that

$$
\| \int _ { a } ^ { b } f ( t ) d t \| \leq \int _ { a } ^ { b } \| f ( t ) \| d t .
$$

(11) Consider the Poisson equation with periodic boundary conditions on [0, 1]

$$
\begin{array} { c } { { \displaystyle { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = f , x \in ( 0 , 1 ) } } } \\ { { u ( 0 ) = u ( 1 ) . } } \end{array}
$$

A second order accurate approximation to the problem is given by the solution to the following system of equations

$$
\mathbf { A u } = \Delta x ^ { 2 } \mathbf { f }
$$

where

$$
\mathbf { A } = { \left[ \begin{array} { l l l l l l l } { - 2 } & { 1 } & { 0 } & { \ldots } & { 0 } & { 1 } \\ { 1 } & { - 2 } & { 1 } & { 0 } & { \ldots } & { 0 } \\ { 0 } & { 1 } & { - 2 } & { 1 } & { 0 } & { \ldots } \\ & & { \ddots } & { \ddots } & { \ddots } & \\ { 0 } & { \ldots } & { 0 } & { 1 } & { - 2 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { \ldots } & { 1 } & { - 2 } \end{array} \right] }
$$

$\mathbf { u } = [ u _ { 0 } , u _ { 1 } , . . . , u _ { n - 1 } ] , \mathbf { f } = [ f _ { 0 } , f _ { 1 } , . . . , f _ { n - 1 } ]$ and $u _ { i } \approx u ( x _ { i } )$ with $x _ { i } =$ $i \Delta x , \Delta x = 1 / n$ and $f _ { i } = f ( x _ { i } )$ for $i = 0 , \ldots , n - 1$

a. Show that the matrix A is singular.

b. What condition must f satisfy so that a solution exists?

(12) Consider the least squares problem

$$
\operatorname* { m i n } _ { \mathbf { x } \in \mathbb { R } ^ { n } } \| \mathbf { A x } - \mathbf { b } \| _ { 2 }
$$

where $\mathbf { A } \in \mathbb { R } ^ { m \times n }$ with $m \geq n ,$ Prove that $\mathrm { i f } \ \mathbf { x }$ and $\mathbf { x } + \alpha \mathbf { z } \ ( \alpha \neq 0 )$ are minimizers then ${ \pmb z } \in$ null(A).
