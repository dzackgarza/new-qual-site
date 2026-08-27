## BASIC EXAM: SPRING 2015

## Test instructions:

Write your UCLA ID number on the upper right corner of each sheet of paper you use. Do not write your name anywhere on the exam.

The final score will be the sum of the best FOUR analysis problems (Problems 1 through 6) and the best FOUR linear algebra problems (Problems 7 through 12).

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>12</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Problem 1. Let $f : [ 0 , \infty ) \to [ 0 , \infty )$ be continuous with $f ( 0 ) = 0$ . Show that if

$$
\begin{array} { r } { f ( t ) \leq 1 + \frac { 1 } { 10 } f ( t ) ^ { 2 } \qquad \text { for all } t \in [ 0 , \infty ) , } \end{array}
$$

then f is uniformly bounded throughout [0, ∞).

Problem 2. Let $f : [ 0 , 1 ] \to \mathbb { R }$ . We say that f is H¨older continuous of order $\alpha \in ( 0 , 1 )$ and write $f \in C ^ { \alpha } ( [ 0 , 1 ] )$ if

$$
\begin{array} { r } { \| f \| _ { C ^ { \alpha } } : = \operatorname* { s u p } \{ | f ( x ) | : x \in [ 0 , 1 ] \} + \operatorname* { s u p } \{ \frac { | f ( x ) - f ( y ) | } { | x - y | ^ { \alpha } } : x , y \in [ 0 , 1 ] \ \text { with } \ x \neq y \} < \infty . } \end{array}
$$

This defines a norm on $C ^ { \alpha } ( [ 0 , 1 ] )$ . Prove that any bounded sequence in $C ^ { 1 / 2 } ( [ 0 , 1 ] )$ admits a convergent subsequence in $C ^ { 1 / 3 } ( [ 0 , 1 ] )$

Problem 3. Let $f : \mathbb { R } \to \mathbb { R }$ be a Lipschitz function. Suppose that for every $x \in \mathbb { R }$

$$
\operatorname* { l i m } _ { n \to \infty } n \big [ f \big ( x + { \textstyle \frac { 1 } { n } } \big ) - f ( x ) \big ] = 0 .
$$

Prove that f is differentiable.

Problem 4. Let $f : [ 0 , 1 ] \to \mathbb { R }$ be a function satisfying the intermediate value property, namely, whenever $0 \leq a < b \leq 1$ and y lies between $f ( a )$ and $f ( b )$ , there exists $x \in ( a , b )$ such that $f ( x ) = y$ . Assume that for any $y \in \mathbb { R }$ , the preimage $f ^ { - 1 } ( \{ y \} )$ is closed. Prove that f is continuous.

Problem 5. Let $f : [ 1 , \infty ) \to [ 0 , \infty )$ be bounded and monotonically decreasing with $\operatorname* { l i m } _ { x \to \infty } f ( x ) = 0$ . Show that

$$
\int _ { 1 } ^ { N + 1 } f ( x ) d x - \sum _ { n = 1 } ^ { N } f ( n )
$$

converges to a finite limit as $N \to \infty$

Problem 6. Prove that the integral equation

$$
f ( t ) = e ^ { t ^ { 2 } } + { \textstyle \frac { 1 } { 2 } } \int _ { 0 } ^ { 1 } \cos ( s ) f ( s ) d s
$$

admits a unique continuous solution $f : [ 0 , 1 ] \to \mathbb { R }$

Problem 7. Let

$$
f ( x , y , z ) = 9 x ^ { 2 } + 6 y ^ { 2 } + 6 z ^ { 2 } + 12 x y - 10 x z - 2 y z .
$$

Does there exist a point $( x , y , z )$ such that $f ( x , y , z ) < 0 ?$

Problem 8. Prove or disprove the following claims:

(a) Matrices with determinant 1 are dense in the set of all $3 \times 3$ real matrices.

(b) Matrices with distinct eigenvalues are dense in the set of all $3 \times 3$ complex matrices.

Here, the distance between two matrices $A = ( a _ { i j } ) _ { 1 \leq i , j \leq 3 }$ and $B = ( b _ { i j } ) _ { 1 \leq i , j \leq 3 }$ is given by

$$
d ( A , B ) = \Bigl ( \sum _ { 1 \leq i , j \leq 3 } | a _ { i j } - b _ { i j } | ^ { 2 } \Bigr ) ^ { 1 / 2 } .
$$

Problem 9. Let $V = \mathbb { R } ^ { n }$ and let $U _ { 1 } , U _ { 2 } , W _ { 1 } , W _ { 2 } \subset V$ be subspaces of V of dimension $d ,$ such that dim $( U _ { 1 } \cap W _ { 1 } ) = \dim ( U _ { 2 } \cap W _ { 2 } ) = \ell , \ell \leq d \leq n$ . Prove that there exist a linear operator $T : V \to V$ such that $T ( U _ { 1 } ) = U _ { 2 }$ and $T ( W _ { 1 } ) = W _ { 2 }$

Problem 10. Let

$$
M = \left( \begin{array} { c c } { { A } } & { { B } } \\ { { C } } & { { D } } \end{array} \right) \qquad \text { and } \qquad M ^ { - 1 } = \left( \begin{array} { c c } { { P } } & { { Q } } \\ { { R } } & { { S } } \end{array} \right) ,
$$

where $A , \ldots , S$ are $k \times k$ matrices. Show that

$$
\operatorname* { d e t } M \cdot \operatorname* { d e t } S = \operatorname* { d e t } A .
$$

Problem 11. Two matrices A, B are called commuting if $A B = B A$ . The order of a matrix A is the smallest integer $k > 0$ such that $A ^ { k } = 1$ ; if no such k exists, the order is defined to be infinite. Prove that there exist 10 distinct real $2 \times 2$ matrices, which are pairwise commuting and all of the same finite order.

Problem 12. Let

$$
M = \left( \begin{array} { c c } { { 3 } } & { { 5 } } \\ { { 1 } } & { { - 1 } } \end{array} \right) .
$$

(a) Compute exp(M).

(b) Does there exist a real $2 \times 2$ matrix A such that $M = \exp ( A ) ?$