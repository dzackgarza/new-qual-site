# Real Analysis Qualiftying Exam January 2016

Do as many problems as you can. Start each problem on a separate sheet of paper. Unless otherwise specified, the measure involved in each problem is the Lebesgue measure.

#1. Let E be a measurable subset of [0, 1]. Suppose there exists $\alpha \in ( 0 , 1 )$ such that

$$
m ( E \cap J ) \geq \alpha \cdot m ( J )
$$

for all subintervals J of [0, 1]. Prove that $m ( E ) = 1$

#2. Let $f , g \in L ^ { 1 } ( [ 0 , 1 ] )$ . Suppose

$$
\int _ { 0 } ^ { 1 } x ^ { n } f ( x ) d x = \int _ { 0 } ^ { 1 } x ^ { n } g ( x ) d x
$$

for all integers $n \geq 0$ . Prove that $f ( x ) = g ( x ) { \mathrm { ~ a . e ~ } }$

#3. Let $f , g \in L ^ { 1 } ( [ 0 , 1 ] )$ . Assume for all functions $\varphi \in C ^ { \infty } [ 0 , 1 ]$ with $\varphi ( 0 ) = \varphi ( 1 )$

$$
\int _ { 0 } ^ { 1 } f ( t ) \varphi ^ { \prime } ( t ) d t = - \int _ { 0 } ^ { 1 } g ( t ) \varphi ( t ) d t .
$$

Show that f is absolutely continuous and $f ^ { \prime } = g { \mathrm { ~ a . e ~ } }$

#4. Let $\left\{ g _ { n } \right\}$ be a sequence of measurable functions on [0, 1] such that

(i) $| g _ { n } ( x ) | \leq C$ , for a.e. $x \in [ 0 , 1 ]$

(ii) and $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { a } g _ { n } ( x ) d x = 0 } \end{array}$ for every $a \in [ 0 , 1 ]$

Prove that for each $f \in L ^ { 1 } ( [ 0 , 1 ] )$ , we have

$$
\operatorname* { l i m } _ { n  \infty } \int _ { 0 } ^ { 1 } f ( x ) g _ { n } ( x ) d x = 0 .
$$

#5. (a) Let X be a normed vector space and Y be a closed linear subspace of X. Assume Y is a proper subspace, that is, $Y \neq X$ Show that, for $\forall 0 < \varepsilon < 1$ , there is an element $x \in X$ such that $\| x \| = 1$ and

$$
\operatorname* { i n f } _ { y \in Y } \| x - y \| > 1 - \varepsilon
$$

(b) Use part (a) to prove that, if X is an infinite dimensional normed vector space, then the unit ball of X is not compact.

$\# 6 .$ Let $\{ f _ { k } \}$ be a sequence of increasing functions on [0, 1]. Suppose

$$
\sum _ { k = 1 } ^ { \infty } f _ { k } ( x )
$$

converges for all $x \in [ 0 , 1 ]$ . Denote the limit function by $f ,$ , that is,

$$
f ( x ) = \sum _ { k = 1 } ^ { \infty } f _ { k } ( x ) .
$$

Prove that

$$
f ^ { \prime } ( x ) = \sum _ { k = 1 } ^ { \infty } f _ { k } ^ { \prime } ( x ) , \mathrm { a . e . } x \in [ 0 , 1 ] .
$$

$\# 7 .$ . Suppose $f , g : [ a , b ] \to \mathbb { R }$ are both continuous and of bounded variation. Show that the set

$$
\{ ( f ( t ) , g ( t ) ) \in \mathbb { R } ^ { 2 } : t \in [ a , b ] \}
$$

cannot cover the entire unit square $[ 0 , 1 ] \times [ 0 , 1 ]$

#8. Prove the following two statements:

(a) suppose f is a measurable function on [0, 1], then

$$
\| f \| _ { L ^ { \infty } } = \operatorname* { l i m } _ { p \to \infty } \| f \| _ { L ^ { p } }
$$

(b) If $f _ { n } \geq 0$ and $f _ { n }  f$ in measure, then $\begin{array} { r } { \int f \le } \end{array}$ lim inf $\int f _ { n }$

#9. Suppose $\left\{ f _ { n } \right\}$ is a sequence of functions in $L ^ { 2 } ( [ 0 , 1 ] )$ such that $\| f _ { n } \| _ { L ^ { 2 } } \leq 1$ . If f is measurable and $f _ { n }  f$ in measure, then

(a) $f \in L ^ { 2 } ( [ 0 , 1 ] )$

(b) $f _ { n } \to f$ weakly in $L ^ { 2 } ;$

(c) $f _ { n }  f$ with respect to norm in Lp for $1 \le p < 2$

Hint for part (b): Use Vitali convergence theorem, that is, if $g _ { n }  g$ pointwise a.e. on [0, 1] and $\left\{ g _ { n } \right\}$ is uniformly integrable, then

$$
\operatorname* { l i m } _ { n  \infty } \int _ { 0 } ^ { 1 } g _ { n } = \int _ { 0 } ^ { 1 } g
$$

Recall that $\left\{ g _ { n } \right\}$ being uniformly integrable means that for each $\varepsilon > 0$ , there exists a $\delta > 0$ such that

$$
\int _ { A } \left| g _ { n } \right| < \varepsilon
$$

for all n and all measurable $A \subseteq [ 0 , 1 ]$ with $m ( A ) < \delta$

Hint for part (c): use the fact that, if $g _ { n }$ is a sequence in $L ^ { p } ( [ 0 , 1 ] )$ that converges pointwise a.e. to $g \in L ^ { p } ( [ 0 , 1 ] )$ , then $g _ { n }$ converges to g in norm if and only if $\left\{ \left| g _ { n } \right| ^ { p } \right\}$ is uniformly integrable.

#10. Suppose $E$ is a measurable subset of [0, 1] with Lebesgue measure $\begin{array} { r } { m ( E ) = \frac { 9 9 } { 1 0 0 } } \end{array}$ Show that there exists a number $x \in [ 0 , 1 ]$ such that for all $r \in ( 0 , 1 )$

$$
m ( E \cap ( x - r , x + r ) ) \geq { \frac { r } { 4 } } .
$$

Hint: Use the Hardy-Littlewood maximal inequality:

$$
m ( \{ x \in \mathbb { R } : M f ( x ) \geq \alpha \} ) \leq \frac { 3 } { \alpha } \| f \| _ { 1 }
$$

for all $f \in L ^ { 1 } ( \mathbb { R } )$ . Here $M f$ denotes the Hardy-Littlewood Maximal function of $f$ .