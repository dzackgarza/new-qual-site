## BASIC EXAM: FALL 2015

## Test instructions:

Write your UCLA ID number on the upper right corner of each sheet of paper you use. Do not write your name anywhere on the exam.

Work out 10 problems, including at least 4 of the first 6 problems and at least 4 of the last 6 problems. Clearly indicate which 10 problems you want us to grade.

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>12</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Problem 1. Let $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ be a sequence of positive numbers such that

$$
a _ { n + m } \leq a _ { n } + a _ { m } , \qquad m , n \geq 1 .
$$

Prove that $\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n } } { n } }$ exists by showing

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n } } { n } } = \operatorname* { i n f } _ { n \geq 1 } { \frac { a _ { n } } { n } }
$$

Hint: Treat separately liminf and limsup.

Problem 2. Let $a , b \in \mathbb { R }$ obey $a < b .$ Show that if $g , h \colon [ a , b ] \to \mathbb { R }$ are continuous with $h \geq 0 ,$ then there is $c \in [ a , b ]$ such that

$$
\int _ { a } ^ { b } g ( x ) h ( x ) \mathrm { d } x = g ( c ) \int _ { a } ^ { b } h ( x ) \mathrm { d } x
$$

Problem 3. Let $\{ f _ { n } \}$ be a sequence of continuous functions $f _ { n } \colon [ - 1 , 1 ] \to [ 0 , 1 ]$ such that, for each $x \in [ - 1 , 1 ]$

(1) the sequence of numbers $\{ f _ { n } ( x ) \} _ { n = 1 } ^ { \infty }$ is non-increasing, and

(2) $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) = 0 . } \end{array}$

Define

$$
g _ { n } ( x ) : = \sum _ { m = 1 } ^ { n } ( - 1 ) ^ { m } f _ { m } ( x ) .
$$

Prove that $g _ { n } ( x )$ converges to some $g ( x ) \in \mathbb { R }$ for each x $\in [ - 1 , 1 ]$ and that the function $g \colon [ - 1 , 1 ] \to \mathbb { R }$ thus defined is continuous on $[ - 1 , 1 ]$

Problem 4. Let $f _ { n } \colon [ 0 , \infty ) \to \mathbb { R }$ be functions defined recursively by $f _ { 1 } ( x ) : = 0$ and

$$
f _ { n + 1 } ( x ) : = \mathrm { e } ^ { - 2 x } + \int _ { 0 } ^ { x } f _ { n } ( t ) \mathrm { e } ^ { - 2 t } \mathrm { d } t , \qquad n \geq 1 .
$$

Show that $f ( x ) : = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ exists for all $x \geq 0$ and identify f explicitly.

Problem 5. Let $F ( x , y , z )$ be a continuously differentiable function with nonvanishing partial derivatives at point (0, 0, 0). Define functions

$$
x = x ( y , z ) , \quad y = y ( x , z ) \quad \text { and } \quad z = z ( x , y )
$$

as the solutions of the equation $F ( x , y , z ) = F ( 0 , 0 , 0 )$ in the neighborhood of point (0, 0) in the corresponding variables. Prove that

$$
\frac { \partial x } { \partial y } \frac { \partial y } { \partial z } \frac { \partial z } { \partial x } = - 1
$$

where the three partial derivatives are taken at the point (0, 0) in the corresponding pair of variables.

Problem 6. Let $X : = \mathbb { R } \setminus \{ 0 \}$ . Find a metric $\rho$ on $X$ with the following properties: (1) $( X , \rho )$ is a complete metric space, and

if $\{ x _ { n } \} _ { n = 1 } ^ { \infty } \subset X$ and $x \in X$ , then

$$
\operatorname* { l i m } _ { n \to \infty } | x _ { n } - x | = 0 \quad \Leftrightarrow \quad x _ { n } \to x \text { in } ( X , \rho ) .
$$

Prove both properties, as well as all of your other assertions, in full detail.

Problem 7. Let $A , B$ be two $4 \times 5$ matrices of rank $3 ,$ and let $C = A ^ { T } B$ (this is a $5 \times 5$ matrix). Find all possible values r for the rank of C. To be precise, if the rank r is possible, find an explicit example of such matrices. Then prove that all other values are impossible.

Problem 8. Find $M ^ { - 2 }$ where

$$
M = \left( \begin{array} { c c c c } { { 2 } } & { { 3 } } & { { 2 } } & { { 1 } } \\ { { 3 } } & { { 6 } } & { { 4 } } & { { 2 } } \\ { { 4 } } & { { 8 } } & { { 6 } } & { { 3 } } \\ { { 2 } } & { { 4 } } & { { 3 } } & { { 1 } } \end{array} \right) .
$$

Problem 9. Let A be a $n \times n$ real matrix such that $A ^ { T } = - A .$ Prove that $\operatorname* { d e t } ( A ) \geq 0 .$

Problem 10. Let $F , G : \mathbb { R } ^ { n } \to \mathbb { R } ^ { n }$ be two linear operators. Recall that

$$
\exp ( F ) = \sum _ { k = 0 } ^ { \infty } { \frac { 1 } { k ! } } F ^ { k } .
$$

Prove that when $F$ and $G$ are commuting, i.e. $F G = G F$ we have

$$
\exp ( F + G ) = \exp ( F ) \exp ( G ) .
$$

b) Give an example of non-commuting linear operators when this equality fails.

Problem 11. Let $T : V \to V$ be a linear operator such that $T ^ { 18 } = 0$ and $T ^ { 5 } \neq 0$ Suppose $V \simeq \mathbb { R } ^ { 6 }$ Prove that there is no linear operator $S : V \to V$ such that $S ^ { 2 } = T$ Does the answer change if $V \simeq \mathbb { R } ^ { 12 } ?$

Problem 12. Prove that the following $n \times n$ matrix M is positive definite:

$$
M = \left( \begin{array} { c c c c c } { { 2 } } & { { 1 } } & { { 1 } } & { { \cdots } } & { { 1 } } \\ { { 1 } } & { { 3 } } & { { 1 } } & { { \cdots } } & { { 1 } } \\ { { 1 } } & { { 1 } } & { { 4 } } & { { \cdots } } & { { 1 } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { 1 } } & { { 1 } } & { { 1 } } & { { \cdots } } & { { n + 1 } } \end{array} \right) .
$$