# Complex Analysis Qualifying exam. May 20, 2011

General instructions: 3 hours. No books or notes. Be sure to motivate all (nontrivial) claims and statements. You may use without proof any result proved in the text by Conway, unless the problem specifies otherwise. Either give the name of the theorem or give the statement of the theorem. You need to reprove any result given as an exercise. The following notation will be used. The complex plane is denoted C, the real line is R, and the set of all integers is written Z. For $r > 0 , B ( a ; r ) : = \{ z \in \mathbb { C } : | z - a | < r \}$ and $\mathbb { D } : = B ( 0 , 1 )$ For an open set $G \subset \mathbb { C } .$ $H ( G )$ will denote the space of all analytic functions in G, with the metric induced from $C ( G , \mathbb { C } )$ , the set of all continuous, complex-valued functions on G.

1. (100 pts.) For each of the following, determine if the statement is always true or if it is false. If true, give a proof. If false, give a counterexample or disprove it. Be brief!

(a) Let $G = \{ z \in \mathbb { C } : \operatorname { R e } z \not \in \mathbb { Z } \}$ . Suppose $f \in H ( G )$ such that $| f ( z ) | \leq 1$ for all $z \in G$ . Then f is constant.

(b) There exists $g \in H ( B ( 0 ; 2 ) )$ ) with $| g ( z ) | < 1$ for all $| z | < 2$ , with $z + g ( z ) \neq 0$ for all $z \in \mathbb { D }$

(c) There is an analytic function f on $\mathbb { D } \setminus \{ 0 \}$ with an essential singularity at $z = 0$ such that f can be extended as a continuous function from the whole disk D to the extended plane $\mathbb { C } _ { \infty }$

(d) Suppose that f is a continuous function on $\mathbb { D } \cap \left\{ z : \operatorname { I m } z \leq 0 \right\}$ and analytic in $\mathbb { D } \cap \{ z :$ Im $z < 0 \}$ . If Re $f ( x ) = 0$ for all x with $- 1 < x < 1$ , then $f$ admits an analytic extension to D.

(e) If $G \subset \mathbb { C }$ is a region and $G \cap B ( 0 ; r ) = \emptyset$ for some $r > 0$ , there is a $1 - 1$ analytic function f on G such that $f ( G ) \subset \mathbb { D } .$

(f) If $f \colon \mathbb { C } \to \mathbb { C }$ is analytic function and Re $f ( z ) \geq c$ for some real constant c , then f is constant.

(g) There is a polynomial $p ( z )$ such that $| p ( z ) - 1 / z | < 1$ for all z in the annulus $1 / 2 < | z | < 3 / 2$

2. (25 pts.) Let G be a bounded region and

$$
{ \mathcal { F } } = \{ f \in C ( { \overline { { G } } } , \mathbb { C } ) : f \ \mathrm { ~ a n a l y t i c ~ i n ~ } G \} ,
$$

and put $\| f \| = \operatorname* { s u p } _ { z \in \partial G } | f ( z ) |$ . Show that $\mathcal { F }$ is a complete metric space with $d ( f , g ) = \| f - g \|$ . (Here $\overline { G }$ is the closure of $G$ in $\mathbb { C } , C ( { \overline { { G } } } , \mathbb { C } )$ is the space of all complex-valued, continuous functions in ${ \overline { { G } } } ,$ , and ∂G is the boundary of G.)

3. (25 pts.) Let $a = 1 , b = 0$ , regarded as points in $\mathbb { C } .$

(a) Give an example of an analytic function element $( h , D )$ , with $a \in D$ , and analytic continuations $( f _ { t } , D _ { t } ) , ( g _ { t } , B _ { t } )$ of $( h , D )$ along two different paths $\gamma$ and $\sigma _ { : }$ , such that $\gamma ( 0 ) = \sigma ( 0 ) = a , \gamma ( 1 ) = \sigma ( 1 ) = b .$ but $[ g _ { 1 } ] _ { b } \neq [ f _ { 1 } ] _ { b }$ (Note that necessarily you have $[ g _ { 0 } ] _ { a } = [ f _ { 0 } ] _ { a } = [ h ] _ { a } . )$ Define the analytic continuations explicitly (i.e. be sure to define $D _ { t }$ and $B _ { t }$ as well as the germs $[ f _ { t } ] _ { \gamma ( t ) } , \ [ g _ { t } ] _ { \sigma ( t ) } )$ and explain briefly why these satisfy the definition of an analytic continuation.

(b) Explain why the Monodromy Theorem does not apply for your example in (a) to conclude that $[ g _ { 1 } ] _ { b } = [ f _ { 1 } ] _ { b }$

4. (25 pts.) (a) Let $( X , d )$ be a metric space, $\{ x _ { n } \}$ a sequence in X, and $x \in X$ Suppose that every subsequence of $\{ x _ { n } \}$ has a subsequence which converges to x. Show that $\{ x _ { n } \}$ converges to x.

(b) Let $\{ f _ { n } \}$ be a sequence of locally bounded analytic functions in an open region $G \subset \mathbb { C }$ . Let $\begin{array} { r } { A : = \{ z \in G \colon \operatorname* { l i m } _ { n \to \infty } f _ { n } ( z ) = 0 \} } \end{array}$ and assume that A has a limit point in G. Show that $\left\{ f _ { n } \right\}$ converges uniformly on compact subsets of G to $f \equiv 0$

5. (25 pts.) For $R > 1$ let $C _ { R }$ be the quarter circle parametrized by $z = R e ^ { i \theta }$ $0 \leq \theta \leq \pi / 2$ . Prove that

$$
\operatorname* { l i m } _ { R \to \infty } \int _ { C _ { R } } { \frac { e ^ { i z } } { \log z } } \ d z = 0 ,
$$

where log z is the principal branch of the logarithm. [Hint: You may use the inequality sin $\theta \geq c \theta$ for $0 \leq \theta \leq \pi / 2$ , with some constant $c > 0$ . Then evaluate an appropriate integral.]