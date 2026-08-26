## Relevant information.

Definition. For a sequence of functions $\left\{ f _ { n } \right\}$ where $f _ { n } , f : E \to \mathbb { R }$ for all $n ,$ ,

i) $f _ { n }  f$ pointwise if lim $\mathfrak { i } _ { n \to \infty } f _ { n } ( x ) = f ( x )$ for each $x \in E$

ii) $f _ { n }  f$ uniformly if for every $\epsilon > 0$ there exists $N \in$ N such that $| f _ { n } ( x ) - f ( x ) | < \epsilon$ for all $n \geq N$ and all $x \in E$ . That is, $f _ { n }  f$ uniformly provided $\| f _ { n } - f \| _ { \infty } \to 0$

iii) $\begin{array} { r l } & { \sum _ { n = 1 } ^ { \infty } f _ { n } ( x ) \to f ( x ) } \\ & { \infty . } \end{array}$ provided the partial sums $\textstyle \sum _ { n = 1 } ^ { N } f _ { n } ( x )$ converge pointwise to f as $N $

iv) $\begin{array} { l } { { \sum _ { n = 1 } ^ { \infty } f _ { n } ( x ) \ \to \ f ( x ) } } \\ { { N \to \infty . } } \end{array}$ provided the partial sums $\textstyle \sum _ { n = 1 } ^ { N } f _ { n } ( x )$ converge uniformly to f as

Theorem 6.1 ([Rud76, Thm. 7.12]). $I f \left\{ f _ { n } \right\}$ is a sequence of continuous functions on E and $f _ { n }  f$ uniformly on E, then f is continuous on E.

Theorem 6.2 (Weierstrass M-test / [Rud76, Thm. 7.10]). Suppose $\{ f _ { n } \}$ is a sequence of functions on E and that there exists a real sequence $\{ M _ { n } \}$ such that $| f _ { n } ( x ) | \leq M _ { n }$ for all $x \in E$ $I f \sum _ { n = 1 } ^ { \infty } M _ { n }$ converges, then $\textstyle \sum _ { n = 1 } ^ { \infty } f _ { n }$ converges uniformly on E.

Theorem 6.3 ([Rud76, Thm. 7.16]). If α is monotonically increasing on $[ a , b ] , f _ { n } \in \mathcal { R } ( \alpha )$ for all $n ,$ and $f _ { n }  f$ uniformly on $[ a , b ]$ , then $f \in { \mathcal { R } } ( \alpha )$ , lim $\scriptstyle 1 _ { n \to \infty } \int _ { a } ^ { b } f _ { n }$ dα exists, and

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { a } ^ { b } f _ { n } d \alpha = \int _ { a } ^ { b } f d \alpha .
$$

Theorem 6.4 ([Rud76, Thm. 7.17]). Let $\left\{ f _ { n } \right\}$ be a sequence of functions differentiable on [a, b] for which $\{ f _ { n } ( x _ { 0 } ) \}$ converges at some $x _ { 0 } \in [ a , b ]$ $I f \left\{ f _ { n } ^ { \prime } \right\}$ converges uniformly on $[ a , b ]$ then $\{ f _ { n } \}$ converges uniformly on $[ a , b ]$ to a function f such that

$$
\operatorname* { l i m } _ { n \to \infty } f _ { n } ^ { \prime } ( x ) = f ^ { \prime } ( x ) .
$$

Theorem 6.5 (Arzel\`a-Ascoli $/ \ [ \mathrm { K R D 1 0 }$ , Thm. 8.6.9]). Let $K \subset \mathbb { R } ^ { n }$ be compact. A collection of functions $\mathcal { F } \subset C ( K , \mathbb { R } ^ { m } )$ is compact if and only if F is closed, bounded, and (pointwise) equicontinuous.

Remark 6.6. Compare this to [Rud76, Thm. 7.25]. There are two common definitions of “equicontinuous.” Rudin’s defintion in 7.22 is sometimes called uniformly equicontinuous as δ does not depend on x or y.

Theorem 6.7 (Stone-Weierstrass / [Rud76, Thms. 7.26, 7.32]). $_ { I f f }$ is a continuous function on [a, b] then there exists a sequence of polynomials $\{ P _ { n } \}$ which converge uniformly to $f$

More generally: If A is a self-adjoint algebra of continuous functions on a compact set K which separates points of K and vanishes at no point of K, then given any $f \in C ( K )$ there exists a sequence $f _ { n } \subset \mathcal { A }$ such that $f _ { n }  f$ uniformly on K.

## Warm-up problems.

1) Give a precise statement of the Stone-Weierstrass theorem for real-valued continuous functions. Then, verify that the set of all polynomials of the form

$$
\left\{ \sum _ { j = 2 0 1 7 } ^ { N } a _ { j } x ^ { j } : N \in \mathbb { N } , N \geq 2 0 1 7 , a _ { j } \in \mathbb { R } \right\}
$$

along with the zero function is an algebra over $[ - 2 , 2 ] \subset \mathbb { R }$

2) To clarify Remark 6.6: A family of functions $\mathcal { F } \subset C ( K , \mathbb { R } ^ { m } )$ mapping a set $K \subset \mathbb { R } ^ { n }$ into $\mathbb { R } ^ { m }$ is pointwise equicontinuous on K provided for every $x \in K$ and $\epsilon > 0$ there exists some $\delta > 0$ (which may depend on x) such that $| | f ( x ) - f ( y ) | | < \epsilon$ for all $f \in \mathcal F$ and $y \in K$ with $| | x - y | | < \delta$ . The family F is uniformly equicontinuous if for every $\epsilon > 0$ there exists some $\delta > 0$ such that $| | f ( x ) - f ( y ) | | < \epsilon$ for all $f \in \mathcal F$ and $x , y \in K$ with $| | x - y | | < \delta$ . Prove that these definitions are equivalent when K is compact.

3) Assume that $\left\{ f _ { n } \right\}$ is a sequence of continuous functions $f _ { n } : E \subset \mathbb { R } \to \mathbb { R }$ which converges uniformly to f . Prove the results of Theorem 6.1 directly.

4) Find the pointwise limit f of the sequence of functions $\left\{ f _ { n } \right\}$ given by $f _ { n } ( x ) = x ^ { n }$ on $[ 0 , 1 ]$ . Is the convergence of $f _ { n }$ to $f$ uniform? ([KRD10, 8.6.A]) Why is $B = \{ f \in C ( [ 0 , 1 ] ) : | | f | | _ { \infty } \leq$ 1} not compact?

5) Show that if $\{ f _ { n } \}$ is an equicontinuous sequence of functions on a compact set K and $f _ { n }  f$ pointwise on K, then $f _ { n }  f$ uniformly on K.

## Problems.

6) (June 2010 #6a) Let $f : [ 0 , 1 ] \to$ R be continuous with $f ( 0 ) \neq f ( 1 )$ and define $f _ { n } ( x ) = f ( x ^ { n } )$ Prove that $f _ { n }$ does not converge uniformly on [0, 1].

7) (January 2008 5a) Let $\textstyle f _ { n } ( x ) = { \frac { x } { 1 + n x ^ { 2 } } }$ for $n \in \mathbb { N } .$ . Let ${ \mathcal { F } } : = \{ f _ { n } : n = 1 , 2 , 3 , . . . \}$ and [a, b] be any compact subset of R. Is $\mathcal { F }$ equicontinuous? Justify your answer.

8) (January 2005 #4, June 2010 #6b) If $f : [ 0 , 1 ] \to \mathbb { R }$ is continuous, prove that

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 0 } ^ { 1 } f ( x ^ { n } ) d x = f ( 0 ) .
$$

9) (January 2020 4a) Let $M < \infty$ and ${ \mathcal { F } } \subseteq C [ a , b ]$ . Assume that each $f \in { \mathcal { F } }$ is differentiable on $( a , b )$ and satisfies $| f ( a ) | \leq M$ and $| f ^ { \prime } ( x ) | \leq$ M for all $x \in ( a , b )$ . Prove that $\mathcal { F }$ is equicontinuous on $[ a , b ]$

10) (June 2005 #5) Suppose that $f \in C ( [ 0 , 1 ] )$ and that $\int _ { 0 } ^ { 1 } f ( x ) x ^ { n } d x = 0$ for all $n = 9 9 , 1 0 0 , 1 0 1 , . . . .$ Show that $f \equiv 0$

Note: Many variations on this problem exist. See June 2012 #6b and others.

11) (January 2005 #3b) Suppose $f _ { n } : [ 0 , 1 ] \to$ R are continuous functions converging uniformly to $f : [ 0 , 1 ] \to \mathbb { R }$ . Either prove that lim $\int _ { 1 / n } ^ { 1 } f _ { n } ( x ) d x = \int _ { 0 } ^ { 1 } f ( x )$ dx or give a counterexample. n→∞

## More problems.

12) (January 2006 $\# 7 \mathrm { a } )$ Let f be continuous on [0, 1] and $f ( 0 ) = f ( 1 ) = 0$ . Show that there is a sequence of polynomials $\{ P _ { n } \}$ such that $x ( 1 - x ) P _ { n } ( x )$ converges to f uniformly.

13) (June 2007 #4b part i) Evaluate lim $\int _ { \pi / 2 } ^ { \pi } { \frac { n \sin ( x / n ) } { x } } d x$ and justify your reasoning. n→∞

14) (June 2009 #4a) Let $\left\{ f _ { n } \right\}$ be a sequence of real-valued continuous functions such that $f _ { n }  f$ uniformly on $[ 0 , 1 ]$ , and let $\{ x _ { n } \} \subset [ 0 , 1 ]$ be a sequence which converges to x. Show that lim $f _ { n } ( x _ { n } ) = f ( x )$ n→∞

15) (June 2009 #4b) Prove that the series

$$
x ^ { 2 } + { \frac { x ^ { 2 } } { 1 + x ^ { 2 } } } + { \frac { x ^ { 2 } } { ( 1 + x ^ { 2 } ) ^ { 2 } } } + { \frac { x ^ { 2 } } { ( 1 + x ^ { 2 } ) ^ { 3 } } } + \cdot \cdot \cdot
$$

converges uniformly on $[ a , \infty )$ for every $a > 0 ;$ but not uniformly on [0, b] for any $b > 0$

## References

[KRD10] Allan P. Donsig Kenneth R. Davidson. Real analysis and applications. Springer, 2010.

[Rud76] Walter Rudin. Principles of mathematical analysis. McGraw-Hill, Inc., USA, third edition, 1976.