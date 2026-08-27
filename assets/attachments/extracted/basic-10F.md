# Basic Exam Fall 2010

## Test Instructions:

Write your university identification number at the top of each sheet of paper. Do not write your name!

Solve any 10 of the following 12 problems. You will not receive credit for more than 10 problems. Indicate which problems you wish to be graded by circling the corresponding numbers.

Each problem counts as 10 points. Not all parts of a problem have the same value.

<table><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>∑</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

1. Let F be a closed subset of a metric space X with metric $p .$

(a) Show that if $K \subset X$ is compact, then $K \cap F = \emptyset$ if and only if

$$
\operatorname* { i n f } _ { x \in K , y \in F } \rho ( x , y ) > 0 .
$$

(b) Is the statement in (a) true if K is only assumed to be closed, rather than compact? Give a proof if it is true, and a counterexample if it is false.

2. Suppose $f$ is a bounded function on $[ a , b ]$

(a) Define: "$f$ is Riemann integrable on $[ a , b ]$"

(b) Prove directly from the definition that if $f$ is continuous, then f is Riemann integrable.

3. Suppose $f : \mathbb { R } \to \mathbb { R }$ and $g : \mathbb { R } ^ { 2 } \to \mathbb { R }$ have continuous derivatives up to order three.

(a) State Taylor's Theorem with remainder for each of $f$ and $g .$

(b) Using the statement for $f ,$ prove the statement for $g .$

4. (a) Show that given a real-valued continuous function $f$ on $\{ 0 , 1 \} \times [ 0 , 1 ]$ and an $\epsilon > 0$ , there exist real-valued continuous functions $g _ { 1 } , \ldots , g _ { n }$ and $h _ { 1 } , . . . , h _ { n }$ on $\{ 0 , 1 \}$ for some finite $n \geq 1$ so that

$$
\left| f ( x , y ) - \sum _ { i = 1 } ^ { n } g _ { i } ( x ) h _ { i } ( y ) \right| \leq \epsilon , \quad 0 \leq x , y \leq 1 .
$$

(b) If $f ( x , y ) = f ( y , x )$ for all $0 \leq x , y \leq 1$ , can this be done with $h _ { i } = g _ { i }$ for each i? Explain.

5. Prove or disprove the following two statements: For any two subsets $S$ and $S ^ { \prime }$ of a vector space $V ,$

(a) $S p a n ( S ) \cap S p a n ( S ^ { \prime } ) = S p a n ( S \cap S ^ { \prime } ) .$

(b) $S p a n ( S ) + S p a n ( S ^ { \prime } ) = S p a n ( S \cup S ^ { \prime } )$

6. Let $T$ be an invertible linear operator on a finite dimensional vector space $V$ over a field $F$ Prove that there exists a polynomial $f$ over $F$ such that $T ^ { - 1 } = f ( T )$

7. Let V and W be inner product spaces over $\mathbb { C }$ such that dim $( V ) \leq$ dim $( W ) < \infty$ . Prove that there is a linear transformation $T : V \to W$ satisfying $\langle T ( v ) , T ( v ^ { \prime } ) \rangle _ { W } = \langle v , v ^ { \prime } \rangle _ { V }$ for all $v , v ^ { \prime } \in V$

8. Let $W _ { 1 }$ and $W _ { 2 }$ be subspaces of a finite dimensional inner product space $V$ Prove that $( W _ { 1 } \cap W _ { 2 } ) ^ { \perp } = ( W _ { 1 } ) ^ { \perp } + ( W _ { 2 } ) ^ { \perp }$ $( W ^ { \perp }$ is the orthogonal complement of a subspace W of $V . )$

9. Consider the following iterative method

$$
\vec { x } _ { k + 1 } = A ^ { - 1 } \{ B \vec { x } _ { k } + \vec { c } \}
$$

where $\vec { c }$ is the vector $( 1 , 1 ) ^ { t }$ and $A$ and B are the matrices

$$
A = { \left( \begin{array} { l l } { 2 } & { 0 } \\ { 0 } & { 2 } \end{array} \right) } \quad B = { \left( \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 2 } \end{array} \right) }
$$

(a) Assume the iteration converges; to what vector $\vec { x }$ does the iteration converge?

(b) Does this iteration converge for arbitrary initial vectors, $\vec { x } _ { 0 } ?$ Justify your answer.

10. Suppose $f : \mathbb { R } \to \mathbb { R }$ is bounded and Lipschitz continuous. For $k \in \mathbb { N }$ define $x _ { k } ( t ) : [ 0 , 1 ] \to \mathbb { R }$ by $x _ { k } ( 0 ) = 0$ and

$$
x _ { k } ( t ) = x _ { k } ( n 2 ^ { - k } ) + ( t - n 2 ^ { - k } ) f ( x _ { k } ( n 2 ^ { - k } ) )
$$

for

$$
n 2 ^ { - k } < t \leq ( n + 1 ) 2 ^ { - k } , \quad n \in \mathbb { N } .
$$

Explain why $x _ { k } ( t )$ uniformly converges to a solution $x ( t ) : [ 0 , 1 ] \to \mathbb { R }$ of the ODE

$$
x ^ { \prime } ( t ) = f ( x ( t ) ) , \quad x ( 0 ) = 0 ,
$$

as $k \to \infty .$

11. Find the function $g ( x )$ which minimizes

$$
\int _ { 0 } ^ { 1 } | f ^ { \prime } ( x ) | ^ { 2 } d x .
$$

among smooth functions $f : [ 0 , 1 ] \to \mathbb { R }$ with $f ( 0 ) = 0$ and $f ( 1 ) = 1$ Is the optimal solution $g ( x )$ unique?

12. Let us define $D ( t ) = \{ x ^ { 2 } + y ^ { 2 } \leq r ^ { 2 } ( t ) \} \subset \mathbb { R } ^ { 2 }$ , where $r ( t ) : \mathbb { R } \to \mathbb { R }$ is continuously differentiable. For given smooth, nonnegative function $u ( x , t ) : \mathbb { R } ^ { 2 } \times \mathbb { R } \to \mathbb { R }$, express the following quantity in terms of a surface integral:

$$
\frac { d } { d t } \Big ( \int _ { D ( t ) } u ( x , t ) d x \Big ) - \int _ { D ( t ) } u _ { t } ( x , t ) d x
$$

[You may use various theorems in Calculus without proof.]