# Math 8100 Assignment 5 Repeated Integration

Due date: Friday the 18th of October 2019

1. Prove that if $\{ a _ { j k } \} _ { ( j , k ) \in \mathbb { N } \times \mathbb { N } }$ is a “double sequence” with $a _ { j k } \geq 0$ for all $( j , k ) \in \mathbb { N } \times \mathbb { N }$ , then

$$
\sum _ { j = 1 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } a _ { j k } = \operatorname* { s u p } { \Bigl \{ } \sum _ { ( j , k ) \in B } a _ { j k } : B { \mathrm { ~ i s ~ a ~ f i n i t e ~ s u b s e t ~ o f ~ N } } \times \mathbb { N } { \Bigr \} }
$$

and deduce from this that

$$
\sum _ { j = 1 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } a _ { j k } = \sum _ { k = 1 } ^ { \infty } \sum _ { j = 1 } ^ { \infty } a _ { j k } .
$$

This conclusion holds more generally provided $\sum _ { j = 1 } ^ { \infty } \sum _ { k = 1 } ^ { \infty } \left| a _ { j k } \right| < \infty ,$ , see Theorem 8.3 in “Baby Rudin”.

2. Let $f \in L ^ { 1 } ( [ 0 , 1 ] )$ , and for each $x \in [ 0 , 1 ]$ define

$$
g ( x ) = \int _ { x } ^ { 1 } { \frac { f ( t ) } { t } } d t .
$$

Show that $g \in L ^ { 1 } ( [ 0 , 1 ] )$ and that

$$
\int _ { 0 } ^ { 1 } g ( x ) d x = \int _ { 0 } ^ { 1 } f ( x ) d x .
$$

3. Carefully prove that if we define

$$
f ( x , y ) : = \left\{ { \begin{array} { l l } { \displaystyle { \frac { x ^ { 1 / 3 } } { \left( 1 + x y \right) ^ { 3 / 2 } } } } & { { \mathrm { ~ i f ~ } } 0 \leq x \leq y } \\ { 0 } & { { \mathrm { ~ o t h e r w i s e } } } \end{array} } \right.
$$

for each $( x , y ) \in \mathbb { R } ^ { 2 }$ , then f defines a function in $L ^ { 1 } ( \mathbb { R } ^ { 2 } )$

4. Let $A , B \subseteq \mathbb { R } ^ { n }$ be bounded measurable sets with positive Lebesgue measure.
   For each $t \in \mathbb { R } ^ { n }$ define the function

$$
g ( t ) = m \left( A \cap ( t - B ) \right)
$$

where $t - B = \{ t - b : b \in B \}$

(a) Prove that g is a continuous function and

$$
\int _ { \mathbb { R } ^ { n } } g ( t ) d t = m ( A ) m ( B ) .
$$

(b) Conclude that the sumset

$$
A + B = \left\{ a + b : a \in A { \mathrm { ~ a n d ~ } } b \in B \right\}
$$

contains a non-empty open subset of $\mathbb { R } ^ { n }$

5. Let $f , g \in L ^ { 1 } ( [ 0 , 1 ] )$ and for each $0 \leq x \leq 1$ define

$$
F ( x ) : = \int _ { 0 } ^ { x } f ( y ) d y \quad { \mathrm { a n d } } \quad G ( x ) : = \int _ { 0 } ^ { x } g ( y ) d y .
$$

Prove that

$$
\int _ { 0 } ^ { 1 } F ( x ) g ( x ) d x = F ( 1 ) G ( 1 ) - \int _ { 0 } ^ { 1 } f ( x ) G ( x ) d x .
$$

6. Let $f \in L ^ { 1 } ( \mathbb { R } )$ ). For any $h > 0$ we define

$$
A _ { h } ( f ) ( x ) : = { \frac { 1 } { 2 h } } \int _ { x - h } ^ { x + h } f ( y ) d y
$$

(a) Prove that for all $h > 0$

$$
\int _ { \mathbb { R } } \left| A _ { h } ( f ) ( x ) \right| d x \leq \int _ { \mathbb { R } } \left| f ( x ) \right| d x .
$$

(b) Prove that

$$
\operatorname* { l i m } _ { h \to 0 ^ { + } } \int _ { \mathbb { R } } | A _ { h } ( f ) ( x ) - f ( x ) | d x = 0 .
$$

One can in fact show that lim $\begin{array} { r } { { 1 } _ { h \to 0 ^ { + } } A _ { h } ( f ) = f } \end{array}$ almost everywhere.
This result is actually equivalent to the Lebesgue Density Theorem in R and we will establish this later in the course.

## Extra Challenge Problems

Not to be handed in with the assignment

1. (a) Prove that

$$
\int _ { 0 } ^ { \infty } \left| { \frac { \sin { x } } { x } } \right| d x = \infty .
$$

(b) By considering the iterated integral

$$
\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { \infty } x e ^ { - x y } ( 1 - \cos y ) d y \right) d x
$$

show (with justification) that

$$
\operatorname* { l i m } _ { A  \infty } \int _ { 0 } ^ { A } { \frac { \sin x } { x } } d x = { \frac { \pi } { 2 } } .
$$

2. Suppose that $F$ is a closed subset of R whose complement has finite measure.
   Let $\delta ( x )$ denote the distance from x to $F ,$ namely

$$
\delta ( x ) = d ( x , F ) = \operatorname* { i n f } \left\{ | x - y | : y \in F \right\}
$$

and

$$
I _ { F } ( x ) = \int _ { - \infty } ^ { \infty } { \frac { \delta ( y ) } { | x - y | ^ { 2 } } } d y .
$$

(a) Prove that δ is continuous, by showing that it satisfies the Lipschitz condition $| \delta ( x ) - \delta ( y ) | \leq | x - y |$

(b) Show that $I _ { F } ( x ) = \infty$ if x /∈ F .

(c) Show that $I _ { F } ( x ) < \infty$ for a.e. $x \in F$ , by showing that $\textstyle \int _ { F } I _ { F } ( x ) d x < \infty$
