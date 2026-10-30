September 10, 2008

## Qualifying Exam in Complex Analysis

Instructions. You may use without proof anything which is proved in the text by Conway, unless otherwise stated. Either state the theorem by name, if it has one, or say what the theorem says. However, you must reprove items which were given as exercises.

Notation: For $a \in \mathbb { C } , B ( a ; r )$ denotes the open disk of radius $r > 0$ centered at $a \in \mathbb { C } ,$ . If $G \subset \mathbb { C }$ is open, then $H ( G )$ denotes the space of all analytic functions on G with the usual notion of convergence.

1. (20 pts.) Let u be a nonnegative real-valued harmonic function defined in B(1;2)with $u ( 1 ) = 1 / 3$ Prove that

$$
u ( i ) \leq 1 + ( 2 / 3 ) \sqrt { 2 } .
$$

2. (75 pts.) True or false. For each part, determine if it is always true or sometimes false. If true give a brief proof. If false give a counterexample or disprove it. No credit if reason or counterexample is missing or incorrect. It's OK to be brief here, but "This is a theorem in Conway." is never a completely correct answer.

(a) If f  H(B(1; 1) \ {1}) with

$$
| f ( z ) | \leq { \frac { 1 } { | z - 1 | } } \quad \forall z \in B ( 1 ; 1 ) \setminus \{ 1 \} ,
$$

then f extends to a meromorphic (or possibly analytic) function on $B ( 1 ; 1 )$ (b) Suppose that $f \in H ( \{ z \in B ( 0 ; 1 ) : \Re z > 0 \} )$ and extends continuously to the line $I = \{ i t : - 1 < t < 1 \}$ .I $\ell f ( I ) \subset i \mathbb { R }$ , then f extends to an analytic function in $B ( 0 ; 1 )$

(c) If $G \subset \mathbb { C }$ is open, connected, and simply connected, and $f \in H ( G )$ with $f ^ { \prime } ( z ) \neq 0$ for all $z \in G$ , then $f ( G )$ is also open, connected, and simply connected.

() Let $G \subset \mathbb { C }$ be connected and open and $f \in H ( G )$ nonconstant. If $f ( z ) \neq 0$ for all $z \in G$ , then $\vert f \vert$ does not reach a minimum at any point in G.

(e) Let f be an analytic function element defined in $B ( 1 / 2 ; 1 / 4 )$ . Suppose that f continues analytically along any path $\gamma$ from $\gamma ( 0 ) \in B ( 1 / 2 ; 1 / 4 )$ to $\gamma ( 1 ) \in B ( 0 ; 1 ) \setminus \{ 0 \}$ . Then there is a function $F \in H ( B ( 0 ; 1 ) \setminus \{ 0 \} )$ such that $F | _ { B ( 1 / 2 ; 1 / 4 ) } = f$

3. (20 pts.) Let $G \subset \mathbb { C }$ be open and connected, and let $h \in H ( G )$ Suppose that $\{ f _ { n } ( z ) \} \subset H ( G )$ is a sequence of analytic functions for which $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( z )$ exists (and is finite) for every $z \in G$ Put $f ( z ) : = \operatorname* { l i m } _ { n \to \infty } f _ { n } ( z )$ Suppose that $| f _ { n } ^ { \prime } ( z ) | \leq | h ( z ) |$ for all $z \in G .$ Prove that $f \in H ( G )$

4. (40 pts.) Let $\begin{array} { r } { f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } , \ a _ { n } \geq 0 } \end{array}$ for all n, where the series is absolutely convergent for $| z | < 1$

(a) For any $r , 0 \leq r < 1$ , any $\theta \in \mathbb { R }$ , and any nonnegative integer $k ,$ prove that

$$
| f ^ { ( k ) } ( r e ^ { i \theta } ) | \leq | f ^ { ( k ) } ( r ) |
$$

Hint: This part is easy, but be careful!

(b) If f (z) extends analytically to $B ( 1 - \delta ; 2 \delta )$ for some $\delta , 0 < \delta < 1$ , prove that $f ( z )$ extends analytically to $B ( ( 1 - \delta ) e ^ { i \theta } ; 2 \delta )$ for any $\theta \in \mathbb { R } .$

(c) Prove that if $f ( z )$ extends analytically to an open neighborhood of $z = 1$ , then the radius of convergence of the series $\sum \limits _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ is strictly greater than 1.

Caution: The hypothesis that the $a _ { n }$ are nonnegative is needed for all parts of this problem. Be sure to indicate how you are using it.

5. (20 pts.) Suppose that $f ( z )$ is an entire function satisfying $f ( z ) = f ( z + 1 )$ for all z. If there exists a real number c, with c ≠ 2πk, $k \in \mathbb { Z } .$ such that

$$
| f ( z ) | \leq e ^ { c \Im z } \quad \forall z \in \mathbb { C }
$$

prove that $f \equiv 0 .$

Hint: Prove it first for the case $G = B ( 0 ; 1 )$

6. (25 pts.) Let $G \subset \mathbb { C }$ be open, connected, and simply connected, $G \neq \mathbb { C }$ Let $f \in H ( G )$ with $f ( G ) \subset G$ Suppose there exist $a , b \in \mathbb { C } , a \neq b$ such that $f ( a ) = a$ and $f ( b ) = b .$ Prove that $f ( z ) = z$ for all $z \in G$