## Week 2: Calculus II (Part 1)

## Practice Problem Solutions

Problem 1. What is the length of the curve $( x ( t ) , y ( t ) ) = ( \cos ( t ) , \sin ( t ) )$ for $0 \leq t \leq \pi ?$

Solution. The length is half the circumference of a unit circle to it is π. Alternatively, using the arc length formula:

$$
L = \int _ { 0 } ^ { \pi } { \sqrt { x ^ { \prime } ( t ) ^ { 2 } + y ^ { \prime } ( t ) ^ { 2 } } } d t = \int _ { 0 } ^ { \pi } { \sqrt { \sin ^ { 2 } ( t ) + \cos ^ { 2 } ( t ) } } d t = \pi .
$$

Problem 2. Compute $\int _ { e ^ { - 3 } } ^ { e ^ { - 2 } } \frac { d x } { x \log ( x ) } .$

Solution. Using the substitution $y = \log ( x )$ gives

$$
\int _ { e ^ { - 3 } } ^ { e ^ { - 2 } } { \frac { d x } { x \log ( x ) } } = \int _ { - 3 } ^ { - 2 } { \frac { d y } { y } } = \log | - 2 | - \log | - 3 | = \log \left( { \frac { 2 } { 3 } } \right) .
$$

Problem 3. For $n \in \mathbb { N } ,$ evaluate $\int _ { 0 } ^ { \infty } x ^ { n } e ^ { - x } d x .$

Solution. Defining

$$
I _ { n } = \int _ { 0 } ^ { \infty } x ^ { n } e ^ { - x } d x ,
$$

we see $I _ { 0 } = 1$ and for $n \geq 1$

$$
I _ { n } = [ - x ^ { n } e ^ { - x } ] _ { x = 0 } ^ { x \to \infty } + n \int _ { 0 } ^ { \infty } x ^ { n - 1 } e ^ { - x } d x = n I _ { n - 1 } .
$$

Thus by induction, it is easily seen that $I _ { n } = n !$ . (One may recognize that $I _ { n } = \Gamma ( n + 1 )$ where Γ is the Gamma Function)

Problem 4. Perform the integral $\int _ { - \infty } ^ { x } { \frac { d t } { \cosh ( t ) } }$ . (Recall $\begin{array} { r } { \cosh ( t ) = \frac { e ^ { t } + e ^ { - t } } { 2 } ) } \end{array}$

Solution. We see

$$
\int _ { - \infty } ^ { x } { \frac { d t } { \cosh ( t ) } } = \int _ { - \infty } ^ { x } { \frac { 2 e ^ { t } d t } { 1 + e ^ { 2 t } } } = 2 \int _ { 0 } ^ { e ^ { x } } { \frac { d s } { 1 + s ^ { 2 } } } = 2 \arctan ( e ^ { x } )
$$

where we made the substitution $s = e ^ { t }$

Note: this function (shifted by a constant) is called the Gudermannian function and gives a connection between the ordinary trig. functions and hyperbolic trig. functions that doesn’t invoke complex numbers.

Problem 5. Compute $\int { \frac { x + 2 } { x ^ { 3 } - x ^ { 2 } + 2 x - 2 } } d x .$

Solution. The denominator factors like $x ^ { 3 } - x ^ { 2 } + 2 x - 2 = ( x - 1 ) ( x ^ { 2 } + 2 )$ . Performing partial fractions, we have

$$
{ \frac { x + 2 } { ( x - 1 ) ( x ^ { 2 } + 2 ) } } = { \frac { A } { x - 1 } } + { \frac { B x + C } { x ^ { 2 } + 2 } } \iff x + 2 = A ( x ^ { 2 } + 2 ) + ( B x + C ) ( x - 1 ) .
$$

Solving gives $A = 1 , B = - 1 , C = 0$ . Thus

$$
\int { \frac { x + 2 } { x ^ { 3 } - x ^ { 2 } + 2 x - 2 } } d x = \int \left( { \frac { 1 } { x - 1 } } - { \frac { x } { x ^ { 2 } + 2 } } \right) d x = \log ( x - 1 ) - { \frac { 1 } { 2 } } \log ( x ^ { 2 } + 2 ) + { \mathrm { c o n s t a n t } }
$$

Problem 6. Evaluate $\int _ { 0 } ^ { a } { \frac { x ^ { 2 } + b ^ { 2 } } { x ^ { 2 } + a ^ { 2 } } }$ dx where $a , b > 0$ are constant.

Solution. Notice that

$$
\int _ { 0 } ^ { a } { \frac { x ^ { 2 } + b ^ { 2 } } { x ^ { 2 } + a ^ { 2 } } } d x = \int _ { 0 } ^ { a } \left( 1 + { \frac { b ^ { 2 } - a ^ { 2 } } { x ^ { 2 } + a ^ { 2 } } } \right) d x = a + \left( { \frac { b ^ { 2 } - a ^ { 2 } } { a } } \right) \arctan \left( { \frac { x } { a } } \right) { \overset { | x = a } { \underset { x = 0 } { \overset { | x = a } { \prod } } } } = a + { \frac { \pi } { 4 } } \left( { \frac { b ^ { 2 } - a ^ { 2 } } { a } } \right) .
$$

Problem 7. What volume is created if the area between $f ( x ) = x$ and $g ( x ) = x ^ { 2 }$ for $x \in [ 0 , 1 ]$ is revolved about the x-axis? What if the same area is revolved about the y-axis?

Solution. The area occurs on the on the interval [0, 1]. Thus the volume created when it is revolved about the x-axis is

$$
\begin{array} { r } { \pi \int _ { 0 } ^ { 1 } ( x ^ { 2 } - x ^ { 4 } ) d x = \pi \left( \frac { 1 } { 3 } - \frac { 1 } { 5 } \right) = \frac { 2 \pi } { 1 5 } } \end{array}
$$

and the volume when it is revolved about the y-axis is

$$
\begin{array} { r } { \pi \int _ { 0 } ^ { 1 } ( y - y ^ { 2 } ) d y = \pi \left( \frac { 1 } { 2 } - \frac { 1 } { 3 } \right) = \frac { \pi } { 6 } . } \end{array}
$$

Problem 8. Compute $\int _ { 0 } ^ { \pi / 2 } \frac { d x } { 1 + \tan ( x ) ^ { 2 0 2 0 } } .$

Solution. Call the integral I. Making the substitution $x = \pi / 2 - y$ , we see

$$
I = \int _ { 0 } ^ { \pi / 2 } \frac { d x } { 1 + \tan ( x ) ^ { 2 0 2 0 } } = \int _ { 0 } ^ { \pi / 2 } \frac { d y } { 1 + \tan ( \pi / 2 - y ) ^ { 2 0 2 0 } } .
$$

But $\cos ( \pi / 2 - y ) = \sin ( y )$ and sin $( \pi / 2 - y ) = \cos ( y )$ so

$$
I = \int _ { 0 } ^ { \pi / 2 } \frac { d y } { 1 + \cot ( y ) ^ { 2 0 2 0 } } = \int _ { 0 } ^ { \pi / 2 } \frac { \tan ( y ) ^ { 2 0 2 0 } d y } { 1 + \tan ( y ) ^ { 2 0 2 0 } } .
$$

Taking this representation of I and adding it to the original, we see

$$
2 I = \int _ { 0 } ^ { \pi / 2 } \left( { \frac { 1 + \tan ( x ) ^ { 2 0 2 0 } } { 1 + \tan ( x ) ^ { 2 0 2 0 } } } \right) d x = { \frac { \pi } { 2 } } \Longrightarrow I = { \frac { \pi } { 4 } } .
$$

Note that curiously enough, this manipulation did not depend on the number 2020 in any way; that is, the integral

$$
I ( \alpha ) = \int _ { 0 } ^ { \pi / 2 } { \frac { d x } { 1 + \tan ( x ) ^ { \alpha } } }
$$

is identically equal to $\pi / 4$ for $\alpha \geq 0$

Problem 9. Compute $\int _ { 0 } ^ { \infty } \frac { \log ( t ) } { 1 + t ^ { 2 } } d t .$

Solution. Using the substitution $t \mapsto 1 / t$ for $t \in ( 0 , 1 )$ , we see

$$
\int _ { 0 } ^ { 1 } { \frac { \log ( t ) } { 1 + t ^ { 2 } } } d t = \int _ { \infty } ^ { 1 } { \frac { \log ( 1 / t ) } { 1 + { \frac { 1 } { t ^ { 2 } } } } } \left( - { \frac { 1 } { t ^ { 2 } } } \right) d t = - \int _ { 1 } ^ { \infty } { \frac { \log ( t ) } { 1 + t ^ { 2 } } } d t .
$$

Thus the integral is zero since the contributions from (0, 1) and $( 1 , \infty )$ cancel.

Problem 10. (Gabriel’s Horn) Let $f ( x ) = 1 / x$ , for $x \in [ 1 , \infty )$ . Find the volume and surface area of the shape which results from rotating the graph of f about the x-axis.

Solution. The volume is given by

$$
V = \pi \int _ { 1 } ^ { \infty } { \frac { d x } { x ^ { 2 } } } = \pi \left. \left( - { \frac { 1 } { x } } \right) \right| _ { x = 1 } ^ { x \to \infty } = \pi .
$$

The surface area formula gives

$$
S A = 2 \pi \int _ { 1 } ^ { \infty } \frac { 1 } { x } \sqrt { 1 + \frac { 1 } { x ^ { 2 } } } d x \ge 2 \pi \int _ { 1 } ^ { \infty } \frac { d x } { x } = + \infty
$$

so this shape has finite volume but infinite surface area.

Problem 11. Evalutate lim $( 3 ^ { n } + 5 ^ { n } ) ^ { 1 / n }$ . More generally, if $x _ { 1 } , \ldots , x _ { k } > 0$ , evaluate the n→∞   
limit $\operatorname* { l i m } _ { n \to \infty } ( x _ { 1 } ^ { n } + \ldots + x _ { k } ^ { n } ) ^ { 1 / n }$

Solution. We see

$$
5 \leq ( 3 ^ { n } + 5 ^ { n } ) ^ { 1 / n } \leq ( 5 ^ { n } + 5 ^ { n } ) ^ { 1 / n } = 2 ^ { 1 / n } 5 .
$$

Taking the limit as $n \to \infty$ , the squeeze theorem shows that

$$
\operatorname* { l i m } _ { n  \infty } ( 3 ^ { n } + 5 ^ { n } ) ^ { 1 / n } = 5 .
$$

More generally

$$
\operatorname* { l i m } _ { n \to \infty } ( x _ { 1 } ^ { n } + \ldots + x _ { k } ^ { n } ) ^ { 1 / n } = \operatorname* { m a x } \{ x _ { 1 } , \ldots , x _ { k } \}
$$

using similar reasoning.

Problem 12. For what values of $\alpha , \beta \in \mathbb { R }$ does the series

$$
\sum _ { n = 2 } ^ { \infty } { \frac { 1 } { n ^ { \alpha } \log ( n ) ^ { \beta } } }
$$

converge/diverge?

Solution. If $\alpha > 1$ , then we can compare this series with $\sum { \frac { 1 } { n ^ { \alpha } } }$ to see that it converges.

If $\alpha < 1$ , then we can find $\varepsilon > 0$ small enough that $\alpha + \varepsilon < 1$ . Since any power of $\log ( n )$ is asymptotically smaller than any power of $n ,$ , we see that $n ^ { \alpha }$ log $( n ) ^ { \beta } \lesssim n ^ { \alpha + \varepsilon }$ and so we can compare this series to $\sum { \frac { 1 } { n ^ { \alpha + \varepsilon } } }$ to see that it diverges.

If $\alpha = 1$ , we can use the integral test. Note that

$$
\int _ { 2 } ^ { \infty } { \frac { d x } { x \log ( x ) ^ { \beta } } } = \int _ { \log ( 2 ) } ^ { \infty } { \frac { d y } { y ^ { \beta } } }
$$

converges if and only if $\beta > 1$ . Thus the series also converges if and only if $\beta > 1$

Problem 13. Do the series $\sum _ { n = 2 } ^ { \infty } { \frac { 1 } { \log ( n ! ) } }$ and $\sum _ { n = 3 } ^ { \infty } { \frac { 1 } { \log ( n ) ^ { \log ( n ) } } }$ converge or diverge?

Solution. Using $\begin{array} { r } { \log ( n ! ) = \sum _ { k = 1 } ^ { n } \log ( k ) \leq n \log ( n ) } \end{array}$ , we have

$$
\sum _ { n = 2 } ^ { \infty } { \frac { 1 } { \log ( n ! ) } } \geq \sum _ { n = 2 } ^ { \infty } { \frac { 1 } { n \log ( n ) } }
$$

and so this series diverges by comparison using the result of Problem 12.

The other series converges. Indeed, we see that

$$
\log ( n ) ^ { \log ( n ) } = e ^ { \log ( \log ( n ) ) \log ( n ) } = \left( e ^ { \log ( n ) } \right) ^ { \log ( \log ( n ) ) } = n ^ { \log ( \log ( n ) ) } .
$$

Now for $n > e ^ { e ^ { 2 } }$ , we have log $( \log ( n ) ) > 2$ , thus

$$
\sum _ { n = 3 } ^ { \infty } { \frac { 1 } { \log ( n ) ^ { \log ( n ) } } } \leq C + \sum _ { n = \left\lceil e ^ { e ^ { 2 } } \right\rceil } ^ { \infty } { \frac { 1 } { n ^ { 2 } } } < \infty .
$$

Problem 14. Do the series $\sum _ { n = 1 } ^ { \infty } { \frac { n ! } { 2 ^ { n ^ { 2 } } } }$ and $\sum _ { n = 1 } ^ { \infty } { \frac { n ^ { \sqrt { n } } } { 2 ^ { n } } }$ converge or diverge?

Solution. For the first we use the ratio test. Since

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { ( n + 1 ) ! } { n ! } } { \frac { 2 ^ { n ^ { 2 } } } { 2 ^ { n ^ { 2 } + 2 n + 1 } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { n + 1 } { 2 ^ { 2 n + 1 } } } = 0
$$

the first series converges. For the second series, we use the root test. We have

$$
\operatorname* { l i m } _ { n \to \infty } \left( { \frac { n ^ { \sqrt { n } } } { 2 ^ { n } } } \right) ^ { 1 / n } = { \frac { 1 } { 2 } } \operatorname* { l i m } _ { n \to \infty } n ^ { 1 / { \sqrt { n } } } = : { \frac { 1 } { 2 } } L .
$$

Notice that

$$
\log L = \operatorname* { l i m } _ { n \to \infty } { \frac { \log ( n ) } { \sqrt { n } } } = 0 \quad \Longrightarrow \quad L = 1
$$

and thus the series converges since the root test results in a limit of $1 / 2$

Problem 15. Fix an integer $m > 0$ . Evaluate the infinite sum

$$
\sum _ { n = 1 } ^ { \infty } { \frac { m } { n ( n + m ) } } .
$$

Solution. Using partial fractions gives

$$
{ \frac { m } { n ( n + m ) } } = \left( { \frac { 1 } { n } } - { \frac { 1 } { n + m } } \right) .
$$

Now when we sum, there will be telescoping so that all terms past $\frac { 1 } { m }$ cancel, leaving behind

$$
\sum _ { n = 1 } ^ { \infty } { \frac { m } { n ( n + m ) } } = \sum _ { k = 1 } ^ { m } { \frac { 1 } { k } } .
$$

Problem 16. Decide whether the following series converge or diverge:

$$
( \mathrm { a } ) \sum _ { n = 1 } ^ { \infty } [ 1 - \operatorname { t a n h } ( n ) ] , \quad \quad ( \mathrm { b } ) \sum _ { n = 1 } ^ { \infty } \left( { \frac { \pi } { 2 } } - \arctan ( n ) \right) .
$$

Solution. We see

$$
1 - \operatorname { t a n h } ( n ) = 1 - { \frac { e ^ { n } - e ^ { - n } } { e ^ { n } + e ^ { - n } } } = { \frac { 2 e ^ { - n } } { e ^ { n } + e ^ { - n } } } \leq 2 e ^ { - 2 n }
$$

and so the first series converges by comparison to the goemetric series $\sum ( e ^ { - 2 } ) ^ { n }$

For the second series, consider

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { \pi / 2 - \arctan ( n ) } { 1 / n } } = \operatorname* { l i m } _ { n \to \infty } { \frac { - { \frac { 1 } { 1 + n ^ { 2 } } } } { - 1 / n ^ { 2 } } } = 1
$$

and so $( \pi / 2 - \arctan ( n ) ) \sim { \frac { 1 } { n } }$ which shows that the second series diverges.

Problem 17. Find a sequence $\left( a _ { n } \right)$ such that $a _ { n } > 0$ for all $n \in \mathbb { N }$ and $a _ { n } \to 0$ but

$$
\sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n } a _ { n } \mathrm { d i v e r g e s } .
$$

[Note: this shows that the assumption that $a _ { n }$ is decreasing is necessary in the Alternating Series Test.] Find a sequence $\left( b _ { n } \right)$ such that

$$
\sum _ { n = 1 } ^ { \infty } b _ { n } \mathrm { c o n v e r g e s ~ w h i l e } \sum _ { n = 1 } ^ { \infty } b _ { n } ^ { 2 } \mathrm { d i v e r g e s } .
$$

Is it possible to choose $\left( b _ { n } \right)$ so that $\sum _ { n = 1 } ^ { \infty } b _ { n }$ converges absolutely while $\textstyle \sum _ { n = 1 } ^ { \infty } b _ { n } ^ { 2 }$ diverges?

Solution. For the first part, take $\textstyle a _ { 2 m - 1 } = { \frac { 1 } { 2 ^ { m } } }$ and $\begin{array} { r } { a _ { 2 m } = { \frac { 1 } { m } } . } \end{array}$ . Then clearly $a _ { n } \ > \ 0$ and $a _ { n } \to 0$ but the even partial sums are given by

$$
\sum _ { n = 1 } ^ { 2 N } ( - 1 ) ^ { n } a _ { n } = \sum _ { n = 1 } ^ { N } { \frac { 1 } { n } } - \sum _ { n = 1 } ^ { N } { \frac { 1 } { 2 ^ { n } } } \geq - 1 + { \frac { 1 } { 2 } } \sum _ { n = 1 } ^ { N } { \frac { 1 } { n } } \to \infty \quad { \mathrm { a s } } \quad N \to \infty
$$

[where we’ve used $\scriptstyle \sum _ { n = 1 } ^ { \infty } 2 ^ { - n } = 1 ]$ . Thus the infinite sum does not converge.

For the second part, let $b _ { n } = ( - 1 ) ^ { n } / { \sqrt { n } }$ . Then $\sum b _ { n }$ converges by the alternating series test but $\sum b _ { n } ^ { 2 }$ is the harmonic series which diverges.

To answer the last question: no, this is impossible. If $b _ { n }$ converges, then $b _ { n } \to 0$ and so for sufficiently large n, we have $b _ { n } ^ { 2 } \leq | b _ { n } |$ and so $\sum b _ { n } ^ { 2 }$ converges by comparison to $\sum | b _ { n } |$ which is assumed to converge. (This proves that $\overline { { \ell ^ { 1 } } } ( \mathbb { N } ) \subseteq \ell ^ { 2 } ( \mathbb { N } )$ which is a specific case of the more general fact that $L ^ { p } ( X , \mu ) \subseteq L ^ { q } ( X , \mu )$ whenever $1 \leq p \leq q$ and $( X , \mu )$ is a measure space with no sets of arbitrarily small positive measure.)

Problem 18. Let $\left( a _ { n } \right)$ be a sequence of positive numbers. The infinite product

$$
\prod _ { n = 1 } ^ { \infty } a _ { n } = a _ { 1 } \cdot a _ { 2 } \cdot a _ { 3 } \cdot \cdot \cdot
$$

is said to converge if there is $L \in ( 0 , \infty )$ such that lim $\begin{array} { r } { { \bf \nabla } \cdot { \cal N } \longrightarrow \infty \prod _ { n = 1 } ^ { N } a _ { n } = L } \end{array}$ . Otherwise the product is said to diverge to zero or diverge to +∞ if the limit is zero or +∞ respectively. Consider the infinite products

$$
\mathrm { ( a ) } \prod _ { n = 1 } ^ { \infty } \left( 1 + { \frac { 1 } { n ^ { 2 } } } \right) , \quad \mathrm { ( b ) } \prod _ { n = 1 } ^ { \infty } \left( 1 + { \frac { 1 } { n } } \right) , \quad \mathrm { ( c ) } \prod _ { n = 1 } ^ { \infty } \left( 1 - { \frac { 1 } { \log ( n ) } } \right) .
$$

Show that (a) converges, (b) diverges to $+ \infty$ and (c) diverges to 0.

Solution. Let $\textstyle P = \prod _ { n = 1 } ^ { \infty } a _ { n }$ . Since log is continuous, we can pass it through limits so we see

$$
\log ( P ) = \log \left( \operatorname* { l i m } _ { N \to \infty } \prod _ { n = 1 } ^ { N } a _ { n } \right) = \operatorname* { l i m } _ { N \to \infty } \log \left( \prod _ { n = 1 } ^ { N } a _ { n } \right) = \operatorname* { l i m } _ { N \to \infty } \sum _ { n = 1 } ^ { N } \log ( a _ { n } ) = \sum _ { n = 1 } ^ { \infty } \log ( a _ { n } ) .
$$

Thus we need only check the sums

$$
\left( \mathrm { a } \right) \sum _ { n = 1 } ^ { \infty } \log \left( 1 + \frac { 1 } { n ^ { 2 } } \right) , \quad \left( \mathrm { b } \right) \sum _ { n = 1 } ^ { \infty } \log \left( 1 + \frac { 1 } { n } \right) , \quad \left( \mathrm { c } \right) \sum _ { n = 1 } ^ { \infty } \log \left( 1 - \frac { 1 } { \log ( n ) } \right) .
$$

Note that as $x  0 .$ , we have $\log ( 1 + x ) \sim x$ . Thus by the limit comparison test, the first some converges while the second divergest to +∞ and the third diverges to −∞. Undoing the logarithm, this shows that the first product converges, the second diverges to +∞ and the third diverges to 0. [Of course, this is a bit formal; special considerations should be taken if $P = \infty$ or $P = 0$ since $\log ( P )$ is not defined in those cases, but it’s the same general idea.]

Problem 19. Suppose that $( x ( t ) , y ( t ) )$ for $t \in [ a , b ]$ is the parameterization a curve and that $x ^ { \prime } ( t ) \neq 0$ for all $t \in [ a , b ]$ . Find $\textstyle { \frac { d y } { d x } }$ and $\textstyle { \frac { d ^ { 2 } y } { d x ^ { 2 } } }$ as functions of t.

Solution. From the chain rule, we have $\begin{array} { r } { { \frac { d y } { d t } } = { \frac { d y } { d x } } { \frac { d x } { d t } } } \end{array}$ . Since $x ^ { \prime } ( t ) \neq 0$ , this shows that

$$
{ \frac { d y } { d x } } = { \frac { y ^ { \prime } ( t ) } { x ^ { \prime } ( t ) } } .
$$

Now

$$
{ \frac { d ^ { 2 } y } { d x ^ { 2 } } } = { \frac { d } { d x } } \left( { \frac { d y } { d x } } \right) = { \frac { 1 } { x ^ { \prime } ( t ) } } { \frac { d } { d t } } \left( { \frac { y ^ { \prime } ( t ) } { x ^ { \prime } ( t ) } } \right) = { \frac { y ^ { \prime \prime } ( t ) x ^ { \prime } ( t ) - y ^ { \prime } ( t ) x ^ { \prime \prime } ( t ) } { x ^ { \prime } ( t ) ^ { 3 } } } .
$$

Problem 20. Does the series

$$
{ \frac { 1 } { 3 } } + { \frac { 1 } { 3 { \sqrt { 3 } } } } + { \frac { 1 } { 3 { \sqrt { 3 } } { \sqrt { 3 } } } } + \cdots + { \frac { 1 } { 3 { \sqrt { 3 } } { \sqrt { 3 } } + \cdots + { \sqrt { 3 } } + \cdots } } .
$$

converge or diverge?

Solution. Put $\begin{array} { r } { H _ { n } = \sum _ { k = 1 } ^ { n } \frac { 1 } { k } } \end{array}$ . Then the series can be written

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 3 ^ { H _ { n } } } } .
$$

Now

$$
H _ { n } = \sum _ { k = 1 } ^ { n } { \frac { 1 } { k } } = \sum _ { k = 1 } ^ { n } \int _ { k } ^ { k + 1 } { \frac { 1 } { k } } d x = \sum _ { k = 1 } ^ { n } \int _ { k } ^ { k + 1 } { \frac { 1 } { \left\lfloor x \right\rfloor } } d x = \int _ { 1 } ^ { n + 1 } { \frac { d x } { \left\lfloor x \right\rfloor } } \geq \int _ { 1 } ^ { n + 1 } { \frac { d x } { x } } = \log ( n + 1 ) .
$$

Thus

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 3 ^ { H _ { n } } } } \leq \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 3 ^ { \log ( n + 1 ) } } } = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { e ^ { \log ( 3 ) \log ( n + 1 ) } } } = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { ( n + 1 ) ^ { \log ( 3 ) } } } < \infty
$$

since $\log ( 3 ) > 1$

Problem 21. Evaluate the following limits or prove that they diverge:

$$
\operatorname* { l i m } _ { n \to \infty } \left( { \frac { 1 } { \sqrt { n ^ { 2 } + 1 ^ { 2 } } } } + { \frac { 1 } { \sqrt { n ^ { 2 } + 2 ^ { 2 } } } } + \cdots + { \frac { 1 } { \sqrt { n ^ { 2 } + n ^ { 2 } } } } \right) ;\tag{1}
$$

$$
\operatorname* { l i m } _ { n \to \infty } \left( { \frac { 1 } { \sqrt { n ^ { 2 } + 1 } } } + { \frac { 1 } { \sqrt { n ^ { 2 } + 2 } } } + \cdots + { \frac { 1 } { \sqrt { n ^ { 2 } + n } } } \right) ;\tag{2}
$$

$$
\operatorname* { l i m } _ { n \to \infty } \left( { \frac { 1 } { \sqrt { n ^ { 2 } + 1 } } } + { \frac { 1 } { \sqrt { n ^ { 2 } + 2 } } } + \cdots + { \frac { 1 } { \sqrt { n ^ { 2 } + n ^ { 2 } } } } \right) .\tag{3}
$$

Solution. For (1), we see

$$
\operatorname* { l i m } _ { n \to \infty } \sum _ { k = 1 } ^ { n } { \frac { 1 } { \sqrt { n ^ { 2 } + k ^ { 2 } } } } = \operatorname* { l i m } _ { n \to \infty } \sum _ { k = 1 } ^ { n } { \frac { 1 } { n } } { \frac { 1 } { \sqrt { 1 + \left( { \frac { k } { n } } \right) ^ { 2 } } } } = \int _ { 0 } ^ { 1 } { \frac { d x } { \sqrt { 1 + x ^ { 2 } } } } = \sinh ^ { - 1 } ( 1 ) .
$$

[You can evaluate the integral using the substitution $x = \sinh ( t )$ and the identity $\cosh ^ { 2 } ( t ) -$ $\mathrm { \bar { s i n h } } ^ { 2 } ( t ) = 1 . ]$

For (2), call the limit $L _ { 2 }$ . We have

$$
L _ { 2 } = \operatorname* { l i m } _ { n \to \infty } \sum _ { k = 1 } ^ { n } { \frac { 1 } { \sqrt { n ^ { 2 } + k } } } \leq \operatorname* { l i m } _ { n \to \infty } \sum _ { k = 1 } ^ { n } { \frac { 1 } { n } } = 1 .
$$

Also

$$
L _ { 2 } = \operatorname* { l i m } _ { n \to \infty } \sum _ { k = 1 } ^ { n } { \frac { 1 } { \sqrt { n ^ { 2 } + k } } } \geq \operatorname* { l i m } _ { n \to \infty } \sum _ { k = 1 } ^ { n } { \frac { 1 } { \sqrt { n ^ { 2 } + n } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { n } { \sqrt { n ^ { 2 } + n } } } = 1 .
$$

Thus $L _ { 2 } = 1$

Limit (3) diverges. To prove this, we use the same lower bound as in (2), but there are more terms:

$$
\sum _ { k = 1 } ^ { n ^ { 2 } } { \frac { 1 } { \sqrt { n ^ { 2 } + k } } } \geq \sum _ { k = 1 } ^ { n ^ { 2 } } { \frac { 1 } { \sqrt { 2 n ^ { 2 } } } } = { \frac { n } { \sqrt { 2 } } } \to \infty .
$$

Problem 22. Compute the integral $\int _ { 0 } ^ { 1 } \frac { \log ( 1 + t ) } { 1 + t ^ { 2 } } d t .$

Solution. Call the integral I. Using the substitution $t = \tan ( \theta )$ , we have

$$
\begin{array} { l } { I = \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( 1 + \tan ( \theta ) ) d \theta } \\ { = \displaystyle \int ^ { \pi / 4 } \log ( \sec ( \theta ) ( \cos ( \theta ) + \sin ( \theta ) ) d \theta } \\ { = \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( \cos ( \theta ) + \sin ( \theta ) ) d \theta - \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( \cos ( \theta ) ) d \theta . } \end{array}
$$

But cos $( \theta ) + \sin ( \theta ) = \sqrt { 2 } \cos ( \pi / 4 - \theta )$ . Thus

$$
\begin{array} { r l } & { I = \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( \sqrt { 2 } \cos ( \pi / 4 - \theta ) ) d \theta - \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( \cos ( \theta ) ) d \theta } \\ & { \quad = \displaystyle \int _ { 0 } ^ { \pi / 4 } \frac { \log 2 } { 2 } + \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( \cos ( \pi / 4 - \theta ) ) d \theta - \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( \cos ( \theta ) ) d \theta } \\ & { \quad = \displaystyle \frac { \pi \log 2 } { 8 } + \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( \cos ( \theta ) ) d \theta - \displaystyle \int _ { 0 } ^ { \pi / 4 } \log ( \cos ( \theta ) ) d \theta = \displaystyle \frac { \pi \log 2 } { 8 } , } \end{array}
$$

using the substitution $\phi = \pi / 4 - \theta$

Problem 23. Decide whether the following integral converges: $\int _ { 0 } ^ { \infty } { \frac { d x } { 1 + x ^ { 4 } \sin ^ { 2 } ( x ) } }$

Solution. The integral converges. Call the integral I and break it up into intervals of length $\pi$ (since $\sin ^ { 2 } ( x )$ is π-periodic):

$$
I = \sum _ { n = 0 } ^ { \infty } \int _ { n \pi } ^ { ( n + 1 ) \pi } \frac { d x } { 1 + x ^ { 4 } \sin ^ { 2 } ( x ) } = \sum _ { n = 0 } ^ { \infty } \int _ { 0 } ^ { \pi } \frac { d y } { 1 + ( y + n \pi ) ^ { 4 } \sin ^ { 2 } ( y ) } \le \sum _ { n = 0 } ^ { \infty } \int _ { 0 } ^ { \pi } \frac { d y } { 1 + ( n \pi ) ^ { 4 } \sin ^ { 2 } ( y ) } .
$$

But since $\sin ^ { 2 } ( y )$ is symmetric about $\pi / 2$ , we have

$$
I \leq 2 \sum _ { n = 0 } ^ { \infty } \int _ { 0 } ^ { \pi / 2 } \frac { d y } { 1 + ( n \pi ) ^ { 4 } \sin ^ { 2 } ( y ) } .
$$

And finally, using sin $( y ) \ge y / 2$ for $y \in [ 0 , \pi / 2 ]$ , we see

$$
I \leq \sum _ { n = 0 } ^ { \infty } \int _ { 0 } ^ { \pi / 2 } { \frac { d y } { 1 + { \frac { 1 } { 4 } } ( n \pi ) ^ { 4 } y ^ { 2 } } } = { \frac { \pi } { 2 } } + \sum _ { n = 1 } ^ { \infty } { \frac { 2 } { ( n \pi ) ^ { 2 } } } \int _ { 0 } ^ { n ^ { 2 } \pi ^ { 3 } / 4 } { \frac { d t } { 1 + t ^ { 2 } } } \leq { \frac { \pi } { 2 } } + C \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } }
$$

where $\begin{array} { r } { C = \frac { 2 } { \pi ^ { 2 } } \int _ { 0 } ^ { \infty } \frac { d t } { 1 + t ^ { 2 } } = \frac { 1 } { \pi } } \end{array}$ . Thus the integral converges since $\textstyle \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } }$ converges.