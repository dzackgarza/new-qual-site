# Complex Analysis Qualifying Exam

May 25, 2012

Instructions: 3 hours. No books or notes. You may use without proof all results proved in Conway, unless the problem specifically asks you to reprove a result stated in the text. When using a result from the text, be sure to explicitly verify all hypotheses in it. Present your solutions clearly, with appropriate detail.

There are two sections in this exam. In Section 1, each problem is worth 10 points and consists of a mathematical statement. Your primary task is to decide if the statement is true or false. If you declare it to be false, provide a counterexample. If you declare it to be true, give a brief proof. Section 2 contains more difficult problems worth 20 points. C denotes the set of complex numbers, $\mathbb { D } = \{ z \in \mathbb { C } | | z | < 1 \}$ , and $\mathbb { T } = \{ z \in \mathbb { C } | | z | = 1 \}$ . If $G \subseteq \mathbb { C }$ is open, H(G) denotes the space of analytic functions on G.

## Section 1

1. If f is an entire function satisfying $f ( 0 ) = 1$ and $f ^ { \prime } ( 1 / n ) ~ = ~ f ( 1 / n )$ for all integers $n \geq 1$ , then $f ( z ) = e ^ { z }$ for all $z \in \mathbb { C }$

2. If f is an entire function satisfying $f ( 0 ) = 1$ and $f ^ { \prime } ( n ) ~ = ~ f ( n )$ for all integers $n \geq 1$ , then $f ( z ) = e ^ { z }$ for all $z \in \mathbb { C }$

3. If f and g are analytic functions defined on a neighborhood of $| z | \le 1$ $g \neq 0 \ \mathrm { o n } \ | z | \leq 1$ , and $| f | \leq | g | \mathrm { o n } | z | = 1$ , then $\left| f \right| \leq \left| g \right|$ on $| z | \le 1$

4. There exists a nonconstant analytic function f on C such that ran $f \cap \mathbb { D } =$ ∅.

5. If f is analytic on a neighborhood of $| z | \leq 1$ and $| f ( z ) | < 1$ for $| z | \le 1$ then f when viewed as a mapping of $\mathbb { D } ^ { - }$ into $\mathbb { D } ^ { - }$ has a unique fixed point.

6. There is no complex structure on $\mathbb { R } ^ { 2 }$ (i.e. an atlas of analytic charts making $\mathbb { R } ^ { 2 }$ a complex analytic manifold) such that the function $f : \mathbb { R } ^ { 2 } \to \mathbb { C }$ defined by $f ( x , y ) = x - i y$ is analytic.

## Section 2

1. Let ${ \mathcal { F } } \subseteq \operatorname { H } ( { \mathbb { D } } )$ . Prove that $\mathcal { F }$ is normal if and only if there exists a sequence of nonnegative constants $\{ M _ { n } \}$ such that

$$
\operatorname* { l i m } _ { n \to \infty } M _ { n } ^ { 1 / n } \leq 1
$$

and

$$
\operatorname* { s u p } _ { f \in \mathcal { F } } | \frac { f ^ { ( n ) } ( 0 ) } { n ! } | \leq M _ { n }
$$

for each $n \geq 0$

2. Let $f : \mathbb { D }  \mathbb { D }$ be an analytic function satisfying $f ( 0 ) = 0$ . Prove that

$$
| f ( z ) + f ( - z ) | \leq 2 | z | ^ { 2 }
$$

for all $z \in \mathbb { D }$ . Further, show that this inequality is strict for all $z \in \mathbb { D } \backslash$ {0} unless $f ( z ) + f ( - z ) = 2 c z ^ { 2 }$ for some $c \in \mathbb { C }$ with $| c | = 1$

3. (i) Prove that if $\textstyle f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ is analytic on D and $f ( z ) \in \mathbb { R }$ whenever $z \in [ 0 , 1 )$ , then $a _ { n } \in \mathbb { R }$ for all n.

(ii) Find necessary and sufficient conditions on a constant $\omega$ with $| \omega | = 1$ for there to exist a nonconstant analytic function f on D that is real valued on the radii [0, 1) and $[ 0 , \omega )$

4. Let $f ( e ^ { i t } )$ be a piecewise continuous, real-valued function on $\mathbb { T } ,$ and consider the harmonic function in the unit disk D given by

$$
u ( z ) : = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } P _ { r } ( \theta - t ) f ( e ^ { i t } ) d t ,
$$

where $P _ { r } ( \theta )$ denotes the Poisson kernel and $z = r e ^ { i \theta }$ . Suppose that $A \subset \mathbb { T }$ is an open sub-arc on which $f$ is continuous. Show that

$$
\operatorname* { l i m } _ { z \to a } u ( z ) = f ( a )
$$

for every $a = e ^ { i \theta } \in A$