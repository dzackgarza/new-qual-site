## Day 5: Differential calculus

## Relevant information.

Theorem 4.1 ([Rud76, Thm. 5.8]). $I f f : [ a , b ] \to$ R has a local maximum or minimum at $c \in ( a , b )$ and $f ^ { \prime } ( c )$ exists, then $f ^ { \prime } ( c ) = 0$

Theorem 4.2 (Mean value theorem / [Rud76, Thms. 5.9,10]). If f is a real valued function which is continuous on [a, b] and differentiable on $( a , b )$ , then there exists a point $\xi \in ( a , b )$ so that

$$
{ \frac { f ( b ) - f ( a ) } { b - a } } = f ^ { \prime } ( \xi ) .
$$

Theorem 4.3 (Taylor’s Theorem / [Rud76, Thm. 5.15], [KRD10, Thm. 10.1.3]). Suppose $f$ $[ a , b ] \to \mathbb { R }$ is n times continuously differentiable on [a, b], f (n+1) exists on $( a , b )$ , and $c \in [ a , b ]$ Then, for any $x \in [ a , b ]$ with $x \neq c$ there exists some ξ between c and x so that

$$
f ( x ) = \underbrace { f ( c ) + f ^ { \prime } ( c ) ( x - c ) + \cdots + { \frac { f ^ { ( n ) } ( c ) } { n ! } } ( x - c ) ^ { n } } _ { P _ { n } ( x ) } + { \frac { f ^ { ( n + 1 ) } ( \xi ) } { ( n + 1 ) ! } } ( x - c ) ^ { n + 1 } .
$$

In particular, $i f \mid f ^ { ( n + 1 ) } ( x ) \mid \leq M$ on [a, b] then

$$
| f ( x ) - P _ { n } ( x ) | \leq { \frac { M | x - c | ^ { n + 1 } } { ( n + 1 ) ! } }
$$

for all $x \in [ a , b ]$

## Warm-up problems.

1) (June 1999 #10) Show that if f is differentiable on $( a , b )$ with f 0(x) = 0 on (a, b), then f is constant on $( a , b )$

2) ([Rud76, Exercise 5.1]) If $f : \mathbb { R } \to \mathbb { R }$ satisfies $| f ( x ) - f ( y ) | \leq ( x - y ) ^ { 2 }$ for all $x , y ,$ , then f is constant.

3) ([KRD10, Exercise 6.2.B]) If $f : ( a , b )  \mathbb { R }$ is continuously differentiable and $f ^ { \prime } ( x _ { 0 } ) \neq 0$ for some $x _ { 0 } \in \left( a , b \right)$ , then f is injective on some interval $( c , d )$ containing $x _ { 0 }$

## Problems.

4) (June $2 0 0 5 \# 1 \mathrm { a } )$ Use the definition of the derivative to prove that if f and g are differentiable at $x ,$ then $f g$ is differentiable at x.

5) (January 2006 #2b) Assume that f is differentiable at a. Evaluate

$$
\operatorname* { l i m } _ { x \to a } { \frac { a ^ { n } f ( x ) - x ^ { n } f ( a ) } { x - a } } , \quad n \in \mathbb { N } .
$$

6) (June 2007 #3a) Suppose that $f , g : \mathbb { R } \to \mathbb { R }$ are differentiable, that $f ( x ) \leq g ( x )$ for all $x \in \mathbb { R }$ , and that $f ( x _ { 0 } ) = g ( x _ { 0 } )$ for some $x _ { 0 }$ . Prove that $f ^ { \prime } ( x _ { 0 } ) = g ^ { \prime } ( x _ { 0 } )$

7) (June 2008 #3a) Prove that if f0 exists and is bounded on $( a , b ]$ , then $\scriptstyle \operatorname* { l i m } _ { x \to a ^ { + } } f ( x )$ exists.

8) (January 2012 #4b, extended) Let $f : \mathbb { R } \to \mathbb { R }$ be a differentiable function with $f ^ { \prime } \in C ( \mathbb { R } )$ Assume that there are $a , b \in \mathbb { R }$ with lim $\iota _ { x \to \infty } f ( x ) = a$ and lim $_ { x \to \infty } f ^ { \prime } ( x ) = b$ . Prove that $b = 0$ . Then, find a counterexample to show that the assumption $\scriptstyle \operatorname* { l i m } _ { x \to \infty } f ^ { \prime } ( x )$ exists is necessary.

9) (June 2012 #1a) Suppose that $f : \mathbb { R } \to \mathbb { R }$ satisfies $f ( 0 ) = 0$ . Prove that f is differentiable at $x = 0$ if and only if there is a function $g : \mathbb { R } \to \mathbb { R }$ which is continuous at $x = 0$ and satisfies $f ( x ) = x g ( x )$ for all $x \in \mathbb { R }$

More problems.

10) (January 2005 #6) Suppose that $f : [ 0 , 1 ] \to \mathbb { R }$ is a differentiable function with $f ( 0 ) = 0$ and that there exists some $K > 0$ so that $| f ^ { \prime } ( x ) | \leq K | f ( x ) |$ for all $x \in [ 0 , 1 ]$ . Prove that $f ( x ) = 0 \mathrm { o n } \ [ 0 , 1 ]$ Note: See [Rud76, Chap 5, #26] for a significant hint.

11) Assume that $f : [ 0 , 1 ] \to$ R is continuous on [0, 1] and differentiable on (0, 1) with $f ( 0 ) =$ $f ( 1 ) = 0$ and $f ( c ) = 1$ for some $c \in ( 0 , 1 )$ . Prove that there exists some $s \in ( 0 , 1 )$ such that $\left| f ^ { \prime } ( s ) \right| > 2$

12) (January 2010 #4) Suppose that $f : \mathbb { R } $ R is differentiable at $a \in \mathbb { R } . \ \operatorname { I f } \left\{ x _ { n } \right\}$ is an increasing sequence of real numbers converging to a and $\left\{ y _ { n } \right\}$ is a decreasing sequence of real numbers converging to a, prove that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { f ( y _ { n } ) - f ( x _ { n } ) } { y _ { n } - x _ { n } } } = f ^ { \prime } ( a ) .
$$

13) Prove Theorem 4.1.

## References

[KRD10] Allan P. Donsig Kenneth R. Davidson. Real analysis and applications. Springer, 2010.

[Rud76] Walter Rudin. Principles of mathematical analysis. McGraw-Hill, Inc., USA, third edition, 1976.