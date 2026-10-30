## MATH 220: Complex Analysis Qualifying Exam. May 30, 2007

General instructions: 3 hours. No books or notes. Be sure to motivate all (nontrivial) claims and statements. You may use without proof any result proved in the text (Conway up to Ch X). You need to reprove any result given as an exercise.

Notation: G denotes an open region in C, and ${ \mathcal { O } } ( G )$ denotes the space of analytic functions in G. $B ( \alpha , r )$ denotes the disk $\left\{ z \colon \left| z - a \right| < r \right\}$ . D denotes the unit disk $B ( 0 , 1 ) . ~ f ^ { ( n ) } ( z )$ denotes the nth derivative of $\pmb { f } ( z )$

1. (50p) Determine if the statements below are True or False. If True, give a brief proof. If False, give a counterexample (or prove your assertion in another way, if you prefer). If you claim an assertion follows from a theorem in the text, name the theorem (or describe it otherwise) and explain carefully how the conclusion follows.

(a) (10p) Let $( X , d )$ be a metric space, $x \in X$ , and $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ a sequence in X. If every subsequence of $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ has a subsequence that converges to x, then $\{ x _ { n } \} _ { n = 1 } ^ { \infty }$ converges to x.

<!-- image-->

(b) (10p) Let $\alpha \neq b$ be positive real numbers. There exists a Möbius (linear fractional) transformation sending the circular sector

$$
G _ { 1 } : = \left\{ x + i y \colon : x ^ { 2 } + y ^ { 2 } < 1 , \ x > 0 , \ y > 0 \right\}
$$

to the ellipsoidal sector

$$
G _ { 2 } : = \left\{ x + i y \colon \colon { \frac { x ^ { 2 } } { a ^ { 2 } } } + { \frac { y ^ { 2 } } { b ^ { 2 } } } < 1 , \ x > 0 , \ y > 0 \right\} .
$$

(c) (10p) Let D be a discrete subset of C (i.e. a set without limit points in C).   
Every bounded analytic function in $\mathbb { C } \backslash D$ is constant.

(d) (10p) Suppose that f (z) is analytic in $G : = \mathbb { D } \backslash \{ 0 \}$ and that $\begin{array} { r } { \int _ { \gamma } z ^ { p } f ( z ) d z = 0 } \end{array}$ for every closed curve $\gamma \colon [ 0 , 1 ] \to G$ and every nonnegative integer p. Then, $f ( z )$ has a removable singularity at O.

(e) (10p) Let a be a complex number with $| a | > 1$ . There exists $\epsilon > 0$ such that if a polynomial $p ( z )$ satisfies $| p ( z ) | < \epsilon$ on the closed unit disk ${ \widehat { \mathbb { D } } } ,$ then $| p ( a ) | < 1$

2. (30p) Let $f ( z )$ be analytic with $| f ( z ) | \leq M$ in D and $f ( 0 ) = \alpha > 0$

(a) (15p) Show that. $f ( z )$ has no zeros in the disk $| z | < \alpha / M .$

b) (15p) Find all functions $\pmb { f } ( z )$ (satisfying the above) such that $f ( z )$ has a zero on the circle $| z | = \alpha / M$

<!-- image-->

<!-- image-->

3. (30p) Let $f ( z )$ be analytic in the disk $B ( 0 , 2 )$ . Show that there is a function $g \{ z \}$ , analytic in the unit disk D, such that the series

$$
\sum _ { n = 1 } ^ { \infty } f ^ { ( n ) } ( z )
$$

converges to g in ${ \mathcal { O } } ( { \mathbb { D } } )$

4. (30p) Let n and m be positive integers. Fix w with $| w \rangle \leq 1$ and consider the equation

$$
z ^ { n } + { \frac { 1 } { z ^ { m } } } = w .
$$

How many roots (counting multiplicities) are there in B(0, 2)?

5. (30p) Let $\{ \alpha _ { n } \} _ { n = 1 } ^ { \infty }$ be positive numbers such that

$$
\operatorname* { l i m } _ { n \to \infty } \alpha _ { n } ^ { 1 / n } = \lambda .
$$

Define $q _ { n } ( z ) : = 1 - \alpha _ { n } z ^ { n }$ and $r = 1 / \lambda$ Show that the infinite product

<!-- image-->

$$
\prod _ { n = 1 } ^ { \infty } q _ { n } ( z )
$$

converges in $\mathcal { O } ( B ( 0 , r ) )$ to an analytic function whose zeros (counting multiplicities) inside $B ( 0 , r )$ are precisely those of the $q _ { n } ( z )$