# Week 1: Calculus I Practice Problem Solutions

Problem 1. What is the tangent line to the graph of $y = x + e ^ { x }$ at $x = 0 ?$

Solution. The tangent line is given by $\ell ( x ) = y ( 0 ) + y ^ { \prime } ( 0 ) ( x - 0 ) = 1 + 2 x$

Problem 2. Evaluate $\operatorname* { l i m } _ { x \to 0 } { \frac { ( 1 + x ) ^ { \alpha } - 1 } { x } }$ for $\alpha \in \mathbb { R }$

Solution. Using l’Hˆopital’s rule, we see

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { ( 1 + x ) ^ { \alpha } - 1 } { x } } = \operatorname* { l i m } _ { x \to 0 } { \frac { \alpha ( 1 + x ) ^ { \alpha - 1 } } { 1 } } = \alpha .
$$

This gives a first order approximation $( 1 + x ) ^ { \alpha } \sim 1 + \alpha x$ when $x \approx 0$

Problem 3. Evaluate $\operatorname* { l i m } _ { x \to 0 } { \frac { \cos ( \beta x ) - 1 } { x ^ { 2 } } }$ for $\beta \in \mathbb { R }$

Solution. Using l’Hˆopital’s rule, we see

$$
\begin{array} { r l r } {  { \operatorname* { l i m } _ { x \to 0 } \frac { \cos ( \beta x ) - 1 } { x ^ { 2 } } = \operatorname* { l i m } _ { x \to 0 } \frac { - \beta \sin ( \beta x ) } { 2 x } } } \\ & { } & { \quad = \operatorname* { l i m } _ { x \to 0 } \frac { - \beta ^ { 2 } \cos ( \beta x ) } { 2 } = - \frac { \beta ^ { 2 } } { 2 } . } \end{array}
$$

Problem 4. Let $c > 0$ . Find the minimum value of $f ( x ) = e ^ { x } - c x$ among $x \in \mathbb { R }$

Solution. Setting the derivative to zero shows that extreme points occur when

$$
e ^ { x } - c = 0 \iff x = \log ( c ) .
$$

The second derivative of f is always positive so any extreme point is a minimum. Thus the minimum value is $f ( \log ( c ) ) = c - c \log ( c )$

Problem 5. Let $f ( x ) = | x | + 3 x ^ { 2 }$ for $x \in \mathbb { R }$ . What is $f ^ { \prime } ( - 1 ) \smash { \operatorname { \updownarrow } }$

Solution. In a neighborhood of −1, we have $| x | = - x$ and so $f ( x ) = - x + 3 x ^ { 2 }$ . Then $f ^ { \prime } ( - 1 ) = - 1 + 6 ( - 1 ) = - 7$

Problem 6. Compute the limit $\operatorname* { l i m } _ { x  0 } ( x ^ { - 2 } - \sin ( x ) ^ { - 2 } )$

Solution. We see

$$
\begin{array} { l } { \displaystyle \operatorname* { l i m } _ { x \to 0 } ( x ^ { - 2 } - \sin ( x ) ^ { - 2 } ) = \operatorname* { l i m } _ { x \to 0 } \frac { \sin ^ { 2 } ( x ) - x ^ { 2 } } { x ^ { 2 } \sin ^ { 2 } ( x ) } = \operatorname* { l i m } _ { x \to 0 } \left[ \underbrace { \left( \frac { x ^ { 2 } } { \sin ^ { 2 } ( x ) } \right) } _ { \to 1 } \left( \frac { \sin ^ { 2 } ( x ) - x ^ { 2 } } { x ^ { 4 } } \right) \right] } \\ { = \displaystyle \operatorname* { l i m } _ { x \to 0 } \left[ \underbrace { \left( \frac { \sin ( x ) + x } { x } \right) } _ { \to 2 } \left( \frac { \sin ( x ) - x } { x ^ { 3 } } \right) \right] } \\ { = \displaystyle 2 \operatorname* { l i m } _ { x \to 0 } \frac { \cos ( x ) - 1 } { 3 x ^ { 2 } } = 2 \operatorname* { l i m } _ { x \to 0 } \frac { - \sin ( x ) } { 6 x } = - \frac { 1 } { 3 } . } \end{array}
$$

Problem 7. Suppose that $f ( x ) = 3 x ^ { 2 } + b x + c$ has a non-simple root at $x = 2$ . What is $f ( 5 ) ?$

Solution. If a quadratic polynomial has a non-simple root at $x = 2$ then it is a multiple of $( x - 2 ) ^ { 2 }$ . Here

$$
f ( x ) = 3 ( x - 2 ) ^ { 2 } \quad \Longrightarrow \quad f ( 5 ) = 3 ( 3 ) ^ { 2 } = 2 7 .
$$

Problem 8. If $f : \mathbb { R }  \mathbb { R }$ is continuously differentiable on $( - 1 , 4 )$ with $f ( 3 ) = 5$ and $f ^ { \prime } ( x ) \geq 1$ for all $x \in ( - 1 , 4 )$ , what is the greatest possible value of $f ( 0 ) ?$

Solution. Using the fundamental theorem of calculus, we have

$$
f ( 0 ) = f ( 3 ) - \int _ { 0 } ^ { 3 } f ^ { \prime } ( x ) d x \leq f ( 3 ) - \int _ { 0 } ^ { 3 } 1 \ d x = 2 .
$$

This bound can be realized if $f ^ { \prime } ( x ) \equiv 1 \ [ \mathrm { s o } \ f ( x ) = x + 2 ]$

Problem 9. Compute $\operatorname* { l i m } _ { x \to 0 } { \frac { \sin ( 2 x ) } { ( 1 + x ) \ln ( 1 + x ) } } .$

Solution. The term $\textstyle { \frac { 1 } { 1 + x } }$ is irrelevant since it tends to 1 in the limit. Thus

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { \sin ( 2 x ) } { ( 1 + x ) \ln ( 1 + x ) } } = \operatorname* { l i m } _ { x \to 0 } { \frac { \sin ( 2 x ) } { \ln ( 1 + x ) } } = \operatorname* { l i m } _ { x \to 0 } 2 ( 1 + x ) \cos ( 2 x ) = 2 .
$$

Problem 10. Let $f ( x ) = e ^ { g ( x ) } h ( x )$ where $h ^ { \prime } ( x ) = - g ^ { \prime } ( x ) h ( x )$ for all $x \in \mathbb { R }$ . Which of the following is necessarily true? (a) f is constant $( \mathrm { b } ) \ f$ is linear and non-constant (c) g is constant (d) g is linear and non-constant (e) none of the above

Solution. Note that

$$
f ^ { \prime } ( x ) = e ^ { g ( x ) } g ^ { \prime } ( x ) h ( x ) + e ^ { g ( x ) } h ^ { \prime } ( x ) = e ^ { g ( x ) } g ^ { \prime } ( x ) h ( x ) - e ^ { g ( x ) } g ^ { \prime } ( x ) h ( x ) = 0
$$

so f is constant.

Problem 11. Let $f ( x ) = x ^ { 2 + \sin ( x ) }$ for $x > 0$ . Find $f ^ { \prime } ( x )$

Solution. The temptation here is to use the power rule or the exponential rule but in the current form, neither apply since both the base and the exponent depend on x. To fix this, we write $f ( x ) = e ^ { ( 2 + \sin ( \bar { x } ) ) \log ( x ) }$ . Thus

$$
f ^ { \prime } ( x ) = e ^ { ( 2 + \sin ( x ) ) \log ( x ) } \left( { \frac { 2 + \sin ( x ) } { x } } + \cos ( x ) \log ( x ) \right) = x ^ { 2 + \sin ( x ) } \left( { \frac { 2 + \sin ( x ) } { x } } + \cos ( x ) \log ( x ) \right)
$$

Problem 12. Let $\begin{array} { r } { J = \int _ { 0 } ^ { 1 } \sqrt { 1 - x ^ { 4 } } d x , \quad K = \int _ { 0 } ^ { 1 } \sqrt { 1 + x ^ { 4 } } d x , \quad L = \int _ { 0 } ^ { 1 } \sqrt { 1 - x ^ { 8 } } d x } \end{array}$ . Order the numbers $J , K , L , 1$ in increasing order.

Solution. For $x \in ( 0 , 1 )$ , we have

$$
1 - x ^ { 4 } < 1 - x ^ { 8 } < 1 < 1 + x ^ { 4 } .
$$

Taking the square root and integrating shows that $J < L < 1 < K$

Problem 13. Find $c \in \mathbb { R }$ such that $g : \mathbb { R }  \mathbb { R }$ satisfies $\textstyle 3 x ^ { 5 } + 9 6 = \int _ { c } ^ { x } g ( t ) d t$

Solution. Differentiating shows that $g ( x ) = 1 5 x ^ { 4 }$ . Thus

$$
3 x ^ { 5 } + 9 6 = 3 x ^ { 5 } - 3 c ^ { 5 } \implies c = - 2 .
$$

Problem 14. Define $f ( 0 ) = 0$ and $\begin{array} { r } { f ( x ) = \frac { | x | } { x } } \end{array}$ for $x \neq 0$ . Compute $\int _ { - 1 } ^ { 1 } f ( x ) d x .$

Solution. The function is odd so the integral on a symmetric range is zero.

Problem 15. Let $\textstyle f ( x ) = \int _ { 1 } ^ { x } { \frac { d t } { 1 + t ^ { 2 } } }$ . Find an equation for the tangent line at $( 2 , f ( 2 ) )$ .

Solution. The tangent line is given by $\ell ( x ) = f ( 2 ) + f ^ { \prime } ( 2 ) ( x - 2 )$ . Here

$$
f ( 2 ) = \arctan ( 2 ) - { \frac { \pi } { 4 } }
$$

and $\begin{array} { r } { f ^ { \prime } ( 2 ) = \frac { 1 } { 1 + 2 ^ { 2 } } = \frac { 1 } { 5 } \sec \ell ( x ) = \arctan ( 2 ) - \frac { \pi } { 4 } + \frac { 1 } { 5 } ( x - 2 ) } \end{array}$

Problem 16. Let $\begin{array} { r } { f ( x ) = \int _ { 0 } ^ { x } \cos ^ { 2 } ( t ^ { 2 } ) d t } \end{array}$ . Find $( f ^ { - 1 } ) ^ { \prime } ( y )$ for $y = f ( 3 )$

Solution. Recall that $\begin{array} { r } { ( f ^ { - 1 } ) ^ { \prime } ( y ) = \frac { 1 } { f ^ { \prime } ( f ^ { - 1 } ( y ) ) } } \end{array}$ . Thus

$$
( f ^ { - 1 } ) ^ { \prime } ( f ( 3 ) ) = { \frac { 1 } { f ^ { \prime } ( 3 ) } } = \sec ^ { 2 } ( 9 ) .
$$

Problem 17. For continuous functions $f , g : \mathbb { R }  \mathbb { R }$ , define the relation ∼ by $f \sim g$ iff

$$
\operatorname* { l i m } _ { x \to \infty } { \frac { f ( x ) } { g ( x ) } } = 1 .
$$

Suppose that $f \sim g$ . Which of these does NOT necessarily follow:

(a) $f ^ { 2 } \sim g ^ { 2 }$ (b) ${ \sqrt { f } } \sim { \sqrt { g } }$ (c) ef ∼ eg (d) $f + g \sim 2 g$ (e) $g \sim f$

Solution. The one which does NOT follow is $\mathbf { \Psi } ( \mathbf { c } ) \mathbf { \Psi } e ^ { f } \sim e ^ { g }$ . Indeed, put $f ( x ) = x$ and $g ( x ) = x - 1$ . Then $f \sim g .$ , but

$$
\operatorname* { l i m } _ { x \to \infty } { \frac { e ^ { f ( x ) } } { e ^ { g ( x ) } } } = \operatorname* { l i m } _ { x \to \infty } e = e \neq 1
$$

so $e ^ { f } \not \sim e ^ { g }$

Problem 18. Let $g ( x ) = e ^ { 2 x + 1 }$ . Compute $\operatorname* { l i m } _ { x \to 0 } { \frac { g ( g ( x ) ) - g ( e ) } { x } }$

Solution. The key is to recognize the limit as $( g \circ g ) ^ { \prime } ( 0 )$ . Now

$$
( g \circ g ) ^ { \prime } ( x ) = { \frac { d } { d x } } \left( e ^ { 2 e ^ { 2 x + 1 } + 1 } \right) = e ^ { 2 e ^ { 2 x + 1 } + 1 } ( 4 e ^ { 2 x + 1 } )
$$

so $( g \circ g ) ^ { \prime } ( 0 ) = e ^ { 2 e + 1 } \cdot ( 4 e ) = 4 e ^ { 2 e + 2 } .$

Problem 19. Suppose that f is differentiable at $x = x _ { 0 }$ . What is $\operatorname* { l i m } _ { h \to 0 } { \frac { f ( x _ { 0 } + h ) - f ( x _ { 0 } - h ) } { h } } \ ?$

Solution. By adding and subtracting $f ( x _ { 0 } )$ in the middle of the numerator, we see that this limit is $2 f ^ { \prime } ( x _ { 0 } )$

Problem 20. Compute the derivative $\frac { d } { d x } \int _ { 0 } ^ { x ^ { 2 } } e ^ { - t ^ { 2 } } d t$

Solution. By the fundamental theorem of calculus and the chain rule

$$
\frac { d } { d x } \int _ { 0 } ^ { x ^ { 2 } } e ^ { - t ^ { 2 } } d t = 2 x e ^ { - x ^ { 4 } } .
$$

Problem 21. Find the first derivative of $\begin{array} { r } { f ( x ) = \frac { x ^ { 3 } } { ( 6 x ^ { 2 } + 1 ) \sqrt [ 3 ] { ( x + 3 ) ^ { 4 } } } } \end{array}$ when $x > 0$

Solution. We can vastly simplify the problem using logarithmic differentiation. Indeed,

$$
\log ( f ( x ) ) = 3 \log ( x ) - \log ( 6 x ^ { 2 } + 1 ) - { \frac { 4 } { 3 } } \log ( x + 3 ) .
$$

Thus

$$
{ \frac { f ^ { \prime } ( x ) } { f ( x ) } } = { \frac { 3 } { x } } - { \frac { 1 2 x } { 6 x ^ { 2 } + 1 } } - { \frac { 4 } { 3 ( x + 3 ) } }
$$

and

$$
f ^ { \prime } ( x ) = { \frac { x ^ { 3 } } { ( 6 x ^ { 2 } + 1 ) { \sqrt [ 3 ] { ( x + 3 ) ^ { 4 } } } } } \left( { \frac { 3 } { x } } - { \frac { 1 2 x } { 6 x ^ { 2 } + 1 } } - { \frac { 4 } { 3 ( x + 3 ) } } \right) .
$$

Problem 22. Calculate $\operatorname* { l i m } _ { n  \infty } \sum _ { k = n + 1 } ^ { 2 n } { \frac { 1 } { k } } .$

Solution. Note

$$
\operatorname* { l i m } _ { n \to \infty } \sum _ { k = n + 1 } ^ { 2 n } { \frac { 1 } { k } } = \operatorname* { l i m } _ { n \to \infty } \sum _ { k = 1 } ^ { n } { \frac { 1 } { n + k } } = \operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { n } } \sum _ { k = 1 } ^ { n } { \frac { 1 } { 1 + { \frac { k } { n } } } } .
$$

This is a limit of Riemann sums for $\frac { 1 } { 1 + x }$ on [0, 1]. Thus

$$
\operatorname* { l i m } _ { n  \infty } \sum _ { k = n + 1 } ^ { 2 n } { \frac { 1 } { k } } = \int _ { 0 } ^ { 1 } { \frac { d x } { 1 + x } } = \ln ( 2 ) .
$$

Note: this actually proves that the harmonic series $\scriptstyle \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { k } }$ diverges. Indeed, looking at the partial sums $\textstyle H _ { n } = \sum _ { k = 1 } ^ { n } { \frac { 1 } { k } }$ , we have proven that $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } ( \dot { H } _ { 2 n } - H _ { n } ) = \ln ( 2 ) } \end{array}$ . But then for all m sufficiently large, we have $H _ { 2 m } - H _ { m } > 1 / 2$ which shows that the sequence $\{ H _ { n } \}$ is not a Cauchy sequence.

Problem 23. How many real roots does $2 x ^ { 5 } + 8 x - 7$ have?

Solution. Since the polynomial has odd order it has at least one real root (by the intermediate value theorem). The derivative of the polynomial is $1 0 x ^ { 4 } + 8$ which is always positive so the polynomial is always strictly increasing and thus has at most one root.

Problem 24. Calculate lim $\left. \frac { 1 } { x } \int _ { 0 } ^ { x } ( 1 + \sin ( 2 t ) ) ^ { 1 / t } d t \right.$ x→0

Solution. Setting $\begin{array} { r } { F ( x ) = \int _ { 0 } ^ { x } ( 1 + \sin ( 2 t ) ) ^ { 1 / t } d t } \end{array}$ , we see that the problem is asking for $F ^ { \prime } ( 0 )$ By FToC, we have $F ^ { \prime } ( x ) = ( 1 + \sin ( 2 x ) ) ^ { 1 / x }$ . Thus

$$
{ \begin{array} { r l } & { F ^ { \prime } ( 0 ) = \operatorname* { l i m } _ { x \to 0 } ( 1 + \sin ( 2 x ) ) ^ { 1 / x } = \exp \left( \operatorname* { l i m } _ { x \to 0 } { \frac { \log ( 1 + \sin ( 2 x ) ) } { x } } \right) } \\ & { \qquad = \exp \left( \operatorname* { l i m } _ { x \to 0 } { \frac { 2 \cos ( 2 x ) / ( 1 + \sin ( 2 x ) ) } { 1 } } \right) = e ^ { 2 } . } \end{array} }
$$

Note: to be more rigorous, you would actually need to show that $F ^ { \prime } ( 0 )$ exists and is equal to this limit; on the GRE you can dispose of theoretical concerns like this for the sake of time, and because you will be given options for the answer.

Problem 25. Let $f : [ 0 , 1 ] \to \mathbb { R }$ be continuous and suppose that f is differentiable on (0, 1) with $f ( 0 ) = 1 , f ( 1 ) = 0$ . Which of the following are necessarily true?

(a) There is $x \in ( 0 , 1 )$ such that $f ( x ) = x$

(b) There is $x \in ( 0 , 1 )$ such that $f ^ { \prime } ( x ) = - 1$

(c) $f ( x ) > 0$ for all $x \in [ 0 , 1 )$

Solution. (a) is true by applying the intermediate value theorem to $f \left( x \right) - x . \ \left( \mathrm { b } \right)$ is true by the mean value theorem. (c) is not necessarily true (as can be easily seen by drawing a picture).

Problem 26. Calculate $\int _ { - 3 } ^ { 3 } | x + 1 | d x .$

Solution. There are several ways to do this. One way is to explicitly calculate the integral by splitting up the region; another is to notice that we are simply adding the areas of two isosceles right trangles. The answer is 10.

Problem 27. Calculate lim $\int _ { 1 } ^ { n } { \frac { d x } { x ^ { n } } }$ n→∞

Solution. Explicitly calculating the integral gives

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { 1 } ^ { n } { \frac { d x } { x ^ { n } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { n ^ { 1 - n } - 1 } { 1 - n } } = 0 .
$$

Alternatively, you could use the dominated convergence theorem to see that this is zero without the annoying algebra.

Problem 28. Calculate $\operatorname* { l i m } _ { n  \infty } { \frac { 3 } { n } } \sum _ { i = 1 } ^ { n } [ ( { \frac { 3 i } { n } } ) ^ { 2 } - ( { \frac { 3 i } { n } } ) ]$

Solution. We can recognize this as a limit of Riemann sums for $x ^ { 2 } - x$ with step size $3 / n$ on [0, 3] or as thrice the limit of Riemann sums of $( 3 x ) ^ { 2 } - 3 x$ with step size $1 / n$ on [0, 1]. Thus

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { 3 } { n } } \sum _ { i = 1 } ^ { n } \left[ \left( { \frac { 3 i } { n } } \right) ^ { 2 } - \left( { \frac { 3 i } { n } } \right) \right] = \int _ { 0 } ^ { 3 } ( x ^ { 2 } - x ) d x = 9 - 9 / 2 = 9 / 2
$$

or

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { 3 } { n } } \sum _ { i = 1 } ^ { n } \left[ \left( { \frac { 3 i } { n } } \right) ^ { 2 } - \left( { \frac { 3 i } { n } } \right) \right] = 3 \int _ { 0 } ^ { 1 } ( 9 x ^ { 2 } - 3 x ) d x = 3 ( 3 - 3 / 2 ) = 9 / 2 .
$$