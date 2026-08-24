## Bounded Variation.

1) (January 2018) Let $f \colon [ a , b ]  \mathbb { R }$ . Suppose $f \in \mathrm { B V } [ a , b ]$ . Prove f is the difference of two increasing functions.

2) (January 2007, 6a) Let f be a function of bounded variation on [a, b]. Furthermore, assume that for some $c > 0 , | f ( x ) | \geq c \mathrm { o n } [ a , b ]$ . Show that $g ( x ) = 1 / f ( x )$ is of bounded variation on $[ a , b ]$

3) (January 2017, 2a) Define $f \colon [ 0 , 1 ]  [ - 1 , 1 ]$ by

$$
f ( x ) : = { \left\{ \begin{array} { l l } { x \sin \left( { \frac { 1 } { x } } \right) } & { 0 < x \leq 1 } \\ { 0 } & { x = 0 } \end{array} \right. }
$$

Determine, with justification, whether f is if bounded variation on the interval [0, 1].

4) (January 2020, 6a) Let $\{ a _ { n } \} _ { n = 1 } ^ { \infty } \subseteq \mathbb { R }$ and a strictly increasing sequence $\{ x _ { n } \} _ { n = 1 } ^ { \infty } \subseteq ( 0 , 1 )$ b e given. Assume that $\textstyle \sum _ { n = 1 } ^ { \infty } a _ { n }$ is absolutely convergent, and define $\alpha \colon [ 0 , 1 ] \to \mathbb { R }$ by

$$
\alpha ( x ) : = { \left\{ \begin{array} { l l } { a _ { n } } & { x = x _ { n } } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. } .
$$

Prove or disprove: α has bounded variation on [0, 1].

## Metric Spaces and Topology.

1) Find an example of a metric space X and a subset $E \subseteq X$ such that E is closed and bounded but not compact.

2) (May 2017 6) Let $( X , d )$ be a metric space. A function $f \colon X \to \mathbb { R }$ is said to be lower semi-continuous (l.s.c) if $f ^ { - 1 } ( a , \infty ) = \{ x \in X : f ( x ) > a \}$ is open in X for every $a \in \mathbb { R }$ Analogously, f is upper semi-continuous (u.s.c) if $f ^ { - 1 } ( - \infty , b ) = \{ x \in X : f ( x ) < b \}$ is open in X for every $b \in \mathbb { R }$

(a) Prove that a function $f \colon X \to \mathbb { R }$ is continuous if and only if $f$ is both l.s.c. and u.s.c.

(b) Prove that f is lower semi-continuous if and only if lim in $\operatorname { f } _ { n \to \infty } f ( x _ { n } ) \geq f ( x )$ whenever $\{ x _ { n } \} _ { n = 1 } ^ { \infty } \subseteq X$ such that $x _ { n } \to x$ in X .

3) (January 2017 3) Let $( X , d )$ be a compact metric space. Suppose that $f _ { n } \colon X \to [ 0 , \infty )$ is a sequence of continuous functions with $f _ { n } ( x ) \geq f _ { n + 1 } ( x )$ for all $n \in \mathbb N$ and $x \in X$ , and such that $f _ { n } \to 0$ pointwise on X. Prove that $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ converges uniformly on X.

## Integral Calculus.

1) (June 2014 1)Define $\alpha \colon [ - 1 , 1 ] \to \mathbb { R }$ by

$$
\alpha ( x ) : = { \left\{ \begin{array} { l l } { - 1 } & { x \in [ - 1 , 0 ] } \\ { 1 } & { x \in ( 0 , 1 ] . } \end{array} \right. }
$$

Let $f \colon [ - 1 , 1 ] \to \mathbb { R }$ be a function that is uniformly bounded on [−1, 1] and continuous at $x = 0$ , but not necessarily continuous for $x \neq 0$ . Prove that f is Riemann-Stieltjes integrable

with respect to α over [−1, 1] and that

$$
\int _ { - 1 } ^ { 1 } f ( x ) d \alpha ( x ) = 2 f ( 0 ) .
$$

2) (June 2017 2) Prove : $f \in { \mathcal { R } } ( \alpha )$ on $[ a , b ]$ if and only if for any $a < c < b , f \in \mathcal { R } ( \alpha )$ on $[ a , c ]$ and on [c, b]. In addition, if either condition holds, then we have that

$$
\int _ { a } ^ { c } f d \alpha + \int _ { c } ^ { b } f d \alpha = \int _ { a } ^ { b } f d \alpha .
$$

3) (Spring 2017 7) Prove that if $f \in \mathcal R$ on $[ a , b ]$ and $\alpha \in C ^ { 1 } [ a , b ]$ , then the Riemann integral $\textstyle \int _ { a } ^ { b } f ( x ) \alpha ^ { \prime } ( x ) d x$ exists and

$$
\int _ { a } ^ { b } f ( x ) d \alpha ( x ) = \int _ { a } ^ { b } f ( x ) \alpha ^ { \prime } ( x ) d x .
$$

Sequences and Series (and of Functions).

1) (January 2006 1) Let the power series series $\scriptstyle \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }$ and $\textstyle \sum _ { n = 0 } ^ { \infty } b _ { n } x ^ { n }$ have radii of convergence $R _ { 1 }$ and $R _ { 2 }$ , respectively.

(a) If $R _ { 1 } \neq R _ { 2 }$ , prove that the radius of convergence, R, of the power series $\scriptstyle \sum _ { n = 0 } ^ { \infty } ( a _ { n } + b _ { n } ) x ^ { n }$ is min $\{ R _ { 1 } , R _ { 2 } \}$ . What can be said about R when $R _ { 1 } = R _ { 2 } ?$

(b) Prove that the radius of convergence, R, of $\scriptstyle \sum _ { n = 0 } ^ { \infty } a _ { n } b _ { n } x ^ { n }$ satisfies $R \ge R _ { 1 } R _ { 2 }$ . Show by means of example that this inequality can be strict.

2) Show that the infinite series $\scriptstyle \sum _ { n = 0 } ^ { \infty } x ^ { n } 2 ^ { - n x }$ converges uniformly on $[ 0 , B ]$ for any $B > 0$ Does this series converge uniformly on $\lbrack 0 , \infty ) ?$

3) (January 2006 4a) Let

$$
f _ { n } ( x ) = { \left\{ \begin{array} { l l } { { \frac { 1 } { n } } } & { x \in ( { \frac { 1 } { 2 ^ { n + 1 } } } , { \frac { 1 } { 2 ^ { n } } } ] } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Show that $\textstyle \sum _ { n = 1 } ^ { \infty } f _ { n }$ does not satisfy the Weierstrass M-test but that it nevertheless converges uniformly on R.

4) Let $f _ { n } \colon [ 0 , 1 ) \to  { \mathbb { R } }$ be the function defined by

$$
f _ { n } ( x ) : = \sum _ { k = 1 } ^ { n } { \frac { x ^ { k } } { 1 + x ^ { k } } } .
$$

(a) Prove that $f _ { n }$ converges to a function $f \colon [ 0 , 1 )  \mathbb { R }$

(b) Prove that for every $0 < a < 1$ the convergence is uniform on $[ 0 , a ]$

(c) Prove that f is differentiable on (0, 1).