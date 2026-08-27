## Week 3: Calculus II (Part 2) & Calculus III Practice Problem Solutions

Problem 1. Suppose $\textstyle f ( x ) = \sum _ { n = 1 } ^ { \infty } ( - 1 ) ^ { n } x ^ { 3 n }$ for $x \in ( - 1 , 1 )$ . Find a closed form for $f ^ { \prime } ( x )$

Solution. This is a geometric series (with the first term missing). Thus

$$
f ( x ) + 1 = \sum _ { n = 0 } ^ { \infty } ( - x ^ { 3 } ) ^ { n } = { \frac { 1 } { 1 + x ^ { 3 } } } \quad \Longrightarrow \quad f ^ { \prime } ( x ) = - { \frac { 3 x ^ { 2 } } { ( 1 + x ^ { 3 } ) ^ { 2 } } } .
$$

Problem 2. For which values of x does $\sum _ { n = 1 } ^ { \infty } { \frac { n ! x ^ { 2 n } } { n ^ { n } ( 1 + x ^ { 2 n } ) } }$ converge?

Solution. Using $\frac { x ^ { 2 n } } { 1 + x ^ { 2 n } } \leq 1$ , we see that for any x,

$$
\sum _ { n = 1 } ^ { \infty } { \frac { n ! x ^ { 2 n } } { n ^ { n } ( 1 + x ^ { 2 n } ) } } \leq \sum _ { n = 1 } ^ { \infty } { \frac { n ! } { n ^ { n } } } .
$$

The latter sum converges; thus the former converges for all $x \in \mathbb { R }$ . To prove the latter converges, use the ratio test:

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n + 1 } } { a _ { n } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { ( n + 1 ) ! n ^ { n } } { n ! ( n + 1 ) ^ { n + 1 } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { \left( 1 + { \frac { 1 } { n } } \right) ^ { n } } } = { \frac { 1 } { e } } < 1 .
$$

Problem 3. Compute $\int _ { 0 } ^ { \infty } \lfloor x \rfloor e ^ { - x } { \cal { \Phi } }$ dx where $\lfloor x \rfloor$ denotes the largest integer smaller than x.

Solution. Split the integral into intervals $[ n , n + 1 )$ for $n \in  { \mathbb { N } } _ { 0 }$ and use $\lfloor x \rfloor = n \colon$

$$
\begin{array} { r c l } { \displaystyle \int _ { 0 } ^ { \infty } \lfloor x \rfloor e ^ { - x } d x = \displaystyle \sum _ { n = 1 } ^ { \infty } n \int _ { n } ^ { n + 1 } e ^ { - x } d x } \\ { \displaystyle } & { = \displaystyle \sum _ { n = 1 } ^ { \infty } n ( e ^ { - n } - e ^ { - ( n + 1 ) } ) } \\ { \displaystyle } & { = \displaystyle \sum _ { n = 1 } ^ { \infty } n e ^ { - n } - \sum _ { n = 1 } ^ { \infty } n e ^ { - ( n + 1 ) } } \\ { \displaystyle } & { = \displaystyle \sum _ { n = 1 } ^ { \infty } n e ^ { - n } - \sum _ { n = 2 } ^ { \infty } ( n - 1 ) e ^ { - n } = \sum _ { n = 1 } ^ { \infty } e ^ { - n } . } \end{array}
$$

Now this is a geometric series resulting in $\int _ { 0 } ^ { \infty } \lfloor x \rfloor e ^ { - x } d x = { \frac { e ^ { - 1 } } { 1 - e ^ { - 1 } } } = { \frac { 1 } { e - 1 } } .$

Problem 4. Let $\alpha \in \mathbb { R }$ . Find the Taylor Series for $( 1 + x ) ^ { \alpha }$ around $x = 0$

Solution. We see

$$
f ^ { ( k ) } ( x ) = \alpha ( \alpha - 1 ) \cdots ( \alpha - ( k - 1 ) ) ( 1 + x ) ^ { \alpha - k }
$$

and so the Taylor series is given by

$$
f ( x ) = 1 + \alpha x + { \frac { \alpha ( \alpha - 1 ) } { 2 } } x ^ { 2 } + { \frac { \alpha ( \alpha - 1 ) ( \alpha - 2 ) } { 6 } } x ^ { 3 } + \cdots = \sum _ { k = 0 } ^ { \infty } \left( \prod _ { \ell = 0 } ^ { k - 1 } ( \alpha - \ell ) \right) { \frac { x ^ { k } } { k ! } }
$$

where the empty product is 1 by convention. [Notice that if $\alpha \in \mathbb { N }$ , the coefficients are eventually zero; this fits our intuition because in this case f is a polynomial whose Taylor series should have a finite number of non-zero terms.]

Problem 5. Find the value of $\textstyle \sum _ { n = 1 } ^ { \infty } n ^ { 2 } x ^ { n }$ wherever the series converges.

Solution. The geometric series converges for $| x | < 1 ;$ we can differentiate the series term-by-term without affecting the radius of convergence. We see

$$
{ \frac { 1 } { 1 - x } } = \sum _ { n = 0 } ^ { \infty } x ^ { n } ,\tag{1}
$$

$$
\implies \frac { 1 } { ( 1 - x ) ^ { 2 } } = \sum _ { n = 1 } ^ { \infty } n x ^ { n - 1 } ,\tag{2}
$$

$$
\implies \frac { 2 } { ( 1 - x ) ^ { 3 } } = \sum _ { n = 2 } ^ { \infty } n ( n - 1 ) x ^ { n - 2 } .\tag{3}
$$

Our original series can be rewritten

$$
\sum _ { n = 1 } ^ { \infty } n ^ { 2 } x ^ { n } = \left( \sum _ { n = 2 } ^ { \infty } n ( n - 1 ) x ^ { n } \right) + \left( \sum _ { n = 1 } ^ { \infty } n x ^ { n } \right) .
$$

These two sums can be evaluated by multiplying (3) by $x ^ { 2 }$ and multiplying (2) by x. Thus

$$
\sum _ { n = 1 } ^ { \infty } n ^ { 2 } x ^ { n } = { \frac { 2 x ^ { 2 } } { ( 1 - x ) ^ { 3 } } } + { \frac { x } { ( 1 - x ) ^ { 2 } } } = { \frac { x + x ^ { 2 } } { ( 1 - x ) ^ { 3 } } } .
$$

Problem 6. For which x does $\textstyle \sum _ { n = 1 } ^ { \infty } n ! x ^ { n }$ converge? What about $\scriptstyle \sum _ { n = 1 } ^ { \infty } n ! x ^ { n ^ { 2 } } ?$

Solution. The first series does not converge for any nonzero x since the ratio test results in

$$
\operatorname* { l i m } _ { n \to \infty } \left| { \frac { ( n + 1 ) ! x ^ { n + 1 } } { n ! x ^ { n } } } \right| = ( n + 1 ) | x | = \infty
$$

when $x \neq 0$ . The second series converges for $| x | < 1$ . Indeed, performing the ratio test we see

$$
\operatorname* { l i m } _ { n \to \infty } \frac { ( n + 1 ) ! x ^ { n ^ { 2 } + 2 n + 1 } } { n ! x ^ { n ^ { 2 } } } = \operatorname* { l i m } _ { n \to \infty } ( n + 1 ) | x | ^ { 2 n + 1 } = \operatorname* { l i m } _ { n \to \infty } ( n + 1 ) e ^ { \log | x | ( 2 n + 1 ) } = \left\{ \begin{array} { l l } { 0 , } & { | x | < 1 , } \\ { + \infty , } & { | x | \geq 1 . } \end{array} \right.
$$

Problem 7. Find the Taylor Series for $\begin{array} { r } { f ( x ) = \int _ { 0 } ^ { x } \frac { \sin ( t ) } { t } d t } \end{array}$ about $x = 0$

Solution. Starting with the Taylor Series for sin(t), dividing by t and then integrating, we have

$$
\sin ( t ) = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } t ^ { 2 n + 1 } } { ( 2 n + 1 ) ! } } \quad \Longrightarrow \quad { \frac { \sin ( t ) } { t } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } t ^ { 2 n } } { ( 2 n + 1 ) ! } } \quad \Longrightarrow \quad f ( x ) = \sum _ { n = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { n } x ^ { 2 n + 1 } } { ( 2 n + 1 ) ! ( 2 n + 1 ) } } .
$$

Problem 8. Assume that $\textstyle f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }$ converges on $( - 1 , 1 )$ . Find the Maclaurin series for $g ( x ) = f ( x ) / ( 1 - x )$

Solution. Let $\textstyle g ( x ) = \sum _ { n = 0 } ^ { \infty } b _ { n } x ^ { n }$ . Then

$$
f ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n } = ( 1 - x ) \sum _ { n = 0 } ^ { \infty } b _ { n } x ^ { n } = b _ { 0 } + \sum _ { n = 1 } ^ { \infty } ( b _ { n } - b _ { n - 1 } ) x ^ { n } .
$$

Thus $b _ { 0 } = a _ { 0 }$ and $b _ { n } = a _ { n } + b _ { n - 1 }$ . From this we see $b _ { 1 } = a _ { 1 } + a _ { 0 } , b _ { 2 } = a _ { 2 } + ( a _ { 1 } + a _ { 0 } )$ and by a quick induction $b _ { k } = a _ { k } + \cdot \cdot \cdot + a _ { 1 } + a _ { 0 }$ . Hence

$$
g ( x ) = \sum _ { n = 0 } ^ { \infty } \left( \sum _ { k = 0 } ^ { n } a _ { k } \right) x ^ { n } .
$$

Note: more generally, if two power series converge in the same interval, their product will also converge on that interval and you can multiply them using the Cauchy formula for the product of infinite sums:

$$
\left( \sum _ { n = 0 } ^ { \infty } c _ { n } x ^ { n } \right) \left( \sum _ { n = 0 } ^ { \infty } d _ { n } x ^ { n } \right) = \sum _ { n = 0 } ^ { \infty } \left( \sum _ { k = 0 } ^ { n } c _ { k } d _ { n - k } \right) x ^ { n } .
$$

This formula (along with the binomial formula) is used in proving that $e ^ { x + y } = e ^ { x } e ^ { y }$ for $x , y \in \mathbb { R }$

Problem 9. Find $f ^ { ( 1 0 0 ) } ( 2 )$ for $\textstyle f ( x ) = { \frac { 3 } { x ^ { 2 } + 5 x + 4 } }$

Solution. Using partial fractions, we find

$$
f ( x ) = { \frac { 1 } { 1 + x } } - { \frac { 1 } { 4 + x } } .
$$

At this point you can just start taking derivatives and notice a pattern, or you can expand each term in a Taylor Series about $x = 2$ . I’ll do the latter:

$$
\begin{array} { c } { { f ( x ) = \displaystyle \frac { 1 } { 3 + ( x - 2 ) } - \displaystyle \frac { 1 } { 6 + ( x - 2 ) } = \displaystyle \frac { 1 } { 3 } \left( \displaystyle \frac { 1 } { 1 + \displaystyle \frac { ( x - 2 ) } { 3 } } \right) - \displaystyle \frac { 1 } { 6 } \left( \displaystyle \frac { 1 } { 1 + \displaystyle \frac { ( x - 2 ) } { 6 } } \right) } } \\ { { \displaystyle \qquad = \displaystyle \frac { 1 } { 3 } \sum _ { n = 0 } ^ { \infty } \frac { ( - 1 ) ^ { n } ( x - 2 ) ^ { n } } { 3 ^ { n } } - \displaystyle \frac { 1 } { 6 } \sum _ { n = 0 } ^ { \infty } \frac { ( - 1 ) ^ { n } ( x - 2 ) ^ { n } } { 6 ^ { n } } . } } \end{array}
$$

The $1 0 0 ^ { \mathrm { t h } }$ coefficient is $f ^ { ( 1 0 0 ) } ( 2 ) / 1 0 0 !$ and so $\begin{array} { r } { f ^ { ( 1 0 0 ) } ( 2 ) = 1 0 0 ! \left( \frac { 1 } { 3 ^ { 1 0 1 } } - \frac { 1 } { 6 ^ { 1 0 1 } } \right) \approx 6 . 0 3 6 1 \times 1 0 ^ { 1 0 9 } } \end{array}$

Problem 10. The polynomial $\begin{array} { r } { p ( x ) = 1 + \frac { 1 } { 2 } ( x - 1 ) - \frac { 1 } { 8 } ( x - 1 ) ^ { 2 } } \end{array}$ is used to approximate $\sqrt { 1 . 0 1 }$ Which of the following best approximates the error ${ \sqrt { 1 . 0 1 } } - p ( 1 . 0 1 ) !$

(A) $\textstyle { \frac { 1 } { 1 6 } } \times 1 0 ^ { - 6 }$ (B) $\scriptstyle { \frac { 1 } { 4 8 } } \times 1 0 ^ { - 8 }$ (C) $\frac { 3 } { 8 } \times 1 0 ^ { - 1 0 }$ (D) $- \frac { 3 } { 8 } \times 1 0 ^ { - 1 0 }$ (E) $\begin{array} { r } { - \frac { 1 } { 1 6 } \times 1 0 ^ { - 6 } . } \end{array}$

Solution. By Problem 4, we have

$$
\sqrt { 1 + \varepsilon } \approx 1 + \left( \frac { 1 } { 2 } \right) \frac { \varepsilon } { 1 ! } + \left( \frac { 1 } { 2 } \right) \left( - \frac { 1 } { 2 } \right) \frac { \varepsilon ^ { 2 } } { 2 ! } + \left( \frac { 1 } { 2 } \right) \left( - \frac { 1 } { 2 } \right) \left( - \frac { 3 } { 2 } \right) \frac { \varepsilon ^ { 3 } } { 3 ! } = 1 + \frac { \varepsilon } { 2 } - \frac { \varepsilon ^ { 2 } } { 8 } + \frac { \varepsilon ^ { 3 } } { 1 6 }
$$

when $\left| \varepsilon \right| \ll 1$ . Thus

$$
\sqrt { 1 + \varepsilon } - p ( 1 + \varepsilon ) \approx \frac { \varepsilon ^ { 3 } } { 1 6 } .
$$

Plugging in $\varepsilon = 0 . 0 1$ shows that (A) is the correct answer. [Quicker answer: you should note that $p$ is a second order approximation, so the error should be on the order of $\varepsilon ^ { 3 }$ where $\varepsilon = 1 0 ^ { - 2 }$ ; thus answers (B), (C), (D) can be eliminated very easily and all that remains to find the sign of the third derivative of $f ( x ) = { \sqrt { x } }$ at $x = 1 . ]$

Problem 11. Find $a _ { 0 } , a _ { 1 } , a _ { 2 } , a _ { 3 }$ such that $x ^ { 3 } - x + 1 = a _ { 0 } + a _ { 1 } ( x - 2 ) + a _ { 2 } ( x - 2 ) ^ { 2 } + a _ { 3 } ( x - 2 ) ^ { 3 }$

Solution. We can view this as the Taylor series for the polynomial centered at $x = 2$ . Plugging in $x = 2$ gives $a _ { 0 } = 7$ . Taking a derivative and then plugging in $x = 2$ gives $a _ { 1 } = 1 1$ . Taking two derivatives and plugging in $x = 2$ gives $a _ { 2 } = 6$ . Finally taking three derivatives shows $a _ { 3 } = 1$ (or you can simply notice that $a _ { 3 }$ it is the coefficient of $x ^ { 3 } )$ .

Problem 12. Suppose $\mathcal { C } _ { 0 }$ is an equilateral triangle of area 1 and that $\mathcal { C } _ { n + 1 }$ is formed by adding an equilateral triangle on the middle third of each line segment forming the boundary of ${ \mathcal { C } } _ { n }$ . The first few steps are pictured as follows:

<!-- image-->  
The Koch Snowflake is $\mathcal { C } _ { \infty }$ ; the limiting shape of this process. Find the area of the Koch Snowflake.

Solution. Every time we add a triangle, we replace one edge with four edges, meaning that at the next step, we add 4 times as many triangles as we did at the previous step. Originally, we add 3 extra triangles, meaning at step n, we add $3 \cdot 4 ^ { n - 1 }$ triangles. Since each of these triangles has $1 / 3$ the side length of the previous triangles (and since area scales with the square of the side length), each of the the triangles added at step n has area $1 / 9 ^ { n }$ . Thus the area of the Koch snowflake is

$$
1 + \sum _ { n = 1 } ^ { \infty } { \frac { 3 \cdot 4 ^ { n - 1 } } { 9 ^ { n } } } = 1 + { \frac { 3 } { 4 } } \sum _ { n = 1 } ^ { \infty } \left( { \frac { 4 } { 9 } } \right) ^ { n } = 1 + { \frac { 3 } { 4 } } \cdot { \frac { 4 / 9 } { 1 - 4 / 9 } } = { \frac { 8 } { 5 } } .
$$

Problem 13. In how many of the standard octants of xyz-space does the graph of $f ( x , y ) = e ^ { x + y }$ appear?

Solution. Four, since the value is always positive.

Problem 14. Find the equation of the plane containing the origin and the points (2, 0, 0) and (0, 0, 1).

Solution. All three of those points have $y = 0$ , so they are contained in the xz-plane.

Problem 15. Let \` be the line of intersection for the planes $x + y + z = 3$ and $x - y + z = 5$ . Find the equation for the plane containing (0, 0, 0) and perpendicular to \`.

Solution. The planes have normal vectors (1, 1, 1) and (1, −1, 1); the line of intersection is normal to both of these so it is parallel to

$$
( 1 , 1 , 1 ) \times ( 1 , - 1 , 1 ) = { \left| \begin{array} { l l l } { { \hat { \mathbf { 1 } } } } & { { \hat { \mathbf { 3 } } } } & { { \hat { \mathbf { k } } } } \\ { { 1 } } & { { 1 } } & { { 1 } } \\ { { 1 } } & { { - 1 } } & { { 1 } } \end{array} \right| } = ( 2 , 0 , - 2 ) .
$$

The new plane must be normal to this and contain zero so it is given by $2 x - 2 z = 0 \implies x = z$

Problem 16. Find all functions f (x, y) satisfying ${ \frac { \partial f } { \partial x } } ( x , y ) = 2 x + y , \quad { \frac { \partial f } { \partial y } } ( x , y ) = x + 2 y .$

Solution. Integrating the first equality in x, we find $f ( x , y ) = x ^ { 2 } + x y + g ( y )$ for some function g. Differentiating in y shows that $g ^ { \prime } ( y ) = 2 y$ and so $g ( y ) = y ^ { 2 } + C$ and thus $f ( x , y ) = x ^ { 2 } + x y + y ^ { 2 } + C$ where C is a constant.

Problem 17. Find the point on the plane $2 x + y + 3 z = 3$ which is closest to the origin.

Solution. We need to minimize $f ( x , y , z ) = x ^ { 2 } + y ^ { 2 } + z ^ { 2 }$ subject to $g ( x , y , z ) : = 2 x + y + 3 z - 3 = 0$ A Lagrange multiplier suggests the relationships

$$
2 x = 2 \lambda , 2 y = \lambda , 2 z = 3 \lambda .
$$

Plugging these into the constraint, we find $\lambda = 3 / 7$ and so the point is given by $( 6 / 1 4 , 3 / 1 4 , 9 / 1 4 )$ [Note: as a shortcut, you could reason that the closest point to the origin is found by travelling from the origin in the direction normal to the plane until you hit the plane. The normal direction here is (2, 1, 3) so you simply need to scale this vector to lie in the plane.]

Problem 18. Let $f ( x _ { 1 } , \ldots , x _ { n } ) = \sum _ { 1 \leq i < j \leq n } x _ { i } x _ { j }$ . Find $\frac { \partial f } { \partial x _ { n } }$

Solution. The only time that the index n appears is when $j = n$ . Thus taking the derivative, we find $\begin{array} { r } { \frac { \partial f } { \partial x _ { n } } ( x _ { 1 } , \dots , x _ { n } ) = \sum _ { i = 1 } ^ { n - 1 } x _ { i } } \end{array}$

Problem 19. Set up an area integral (i.e. an integral in xy-space) which represents the volume of the solid bounded above by the graph of $z = 6 - x ^ { 2 } - 2 y ^ { 2 }$ and below by the graph of $z = - 2 + x ^ { 2 } + 2 y ^ { 2 }$

Solution. These two graphs meet at the elipse $x ^ { 2 } + 2 y ^ { 2 } = 4$ . Thus the integral is given by

$$
\int _ { - 2 } ^ { 2 } \int _ { - \sqrt { ( 4 - x ^ { 2 } ) / 2 } } ^ { \sqrt { ( 4 - x ^ { 2 } ) / 2 } } ( 8 - 2 x ^ { 2 } - 4 y ^ { 2 } ) d x d y
$$

Problem 20. Minimize the function $f ( x , y , z ) = x + 4 z$ on the curve $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 2$

Solution. The minimum must satisfy

$$
1 = 2 \lambda x , ~ 0 = 2 \lambda y , ~ 4 = 2 \lambda z .
$$

Plugging these into the constrant gives $\scriptstyle { \frac { 1 } { 4 \lambda ^ { 2 } } } + { \frac { 4 } { \lambda ^ { 2 } } } = 2 \sec \lambda ^ { 2 } = 1 7 / 8$ . Since f is increasing in both x and z, we take the negative roots and find that f is minimized along the curve at $( - \sqrt { 2 / 1 7 } , 0 , - \sqrt { 3 2 / 1 7 } )$

Problem 21. Let F be a constant unit force in the direction of $( - 1 , 0 , 1 )$ . Find the work done by F on a particle which moves along the path $r ( t ) = ( t , t ^ { 2 } , t ^ { 3 } )$ for $t \in [ 0 , 1 ]$

Solution. The work is given by

$$
\int _ { \mathcal { C } } \mathbf { F } \cdot d \mathbf { r } = \int _ { 0 } ^ { 1 } \mathbf { F } ( \mathbf { r } ( t ) ) \cdot \mathbf { r } ^ { \prime } ( t ) d t = \int _ { 0 } ^ { 1 } ( - 1 + 3 t ^ { 2 } ) d t = 0 .
$$

Problem 22. Find the integral of $f ( x , y ) = e ^ { y ^ { 2 } }$ over the triangular region bounded by the graph of $y = | x |$ for $x \in [ - 2 , 2 ]$ and the line $y = 2$

Solution. We should integrate in x first since $e ^ { y ^ { 2 } }$ doesn’t have an elementary antiderivative. The integral is given by

$$
\int _ { 0 } ^ { 2 } \int _ { - y } ^ { y } e ^ { y ^ { 2 } } d x d y = \int _ { 0 } ^ { 2 } 2 y e ^ { y ^ { 2 } } d y = e ^ { y ^ { 2 } } { \biggl | } _ { y = 0 } ^ { y = 2 } = e ^ { 4 } - 1 .
$$

Problem 23. Let $D = \{ ( x , y ) \in \mathbb { R } ^ { 2 } : x \geq 0 , y \geq 0 \}$ . Calculate

$$
\int \int _ { D } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y
$$

Use this to evaluate the Gaussian integral $\int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x .$

Solution. We can calculate the double integral uing polar coordinates:

$$
\iint _ { D } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y = \int _ { 0 } ^ { \pi / 2 } \int _ { 0 } ^ { \infty } e ^ { - r ^ { 2 } } r d r d \theta = { \frac { \pi } { 2 } } ( - { \frac { 1 } { 2 } } e ^ { - r ^ { 2 } } { \bigg | } _ { r = 0 } ^ { r  \infty } ) = { \frac { \pi } { 4 } } .
$$

Now notice that by Fubini’s theorem,

$$
\iint _ { D } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) } d x d y = \left( \int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x \right) \left( \int _ { 0 } ^ { \infty } e ^ { - y ^ { 2 } } d y \right) = \left( \int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x \right) ^ { 2 }
$$

so

$$
\int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \frac { \sqrt { \pi } } { 2 } } \quad { \mathrm { a n d ~ b y ~ e v e n n e s s } } \quad \int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \sqrt { \pi } } .
$$

Problem 24. Evaluate $\int _ { 0 } ^ { \infty } \frac { \sin ( t ) } { t } d t$ by differentiating $I ( s ) = \int _ { 0 } ^ { \infty } e ^ { - s t } \frac { \sin ( t ) } { t } d t$ with respect to s.

Solution. We see

$$
I ^ { \prime } ( s ) = \int _ { 0 } ^ { \infty } { \frac { d } { d s } } e ^ { - s t } { \frac { \sin ( t ) } { t } } d t = - \int _ { 0 } ^ { \infty } e ^ { - s t } \sin ( t ) d t .
$$

Now integrating by parts twice, we see

$$
\begin{array} { r l } { I ^ { \prime } ( s ) = - \displaystyle ( [ - e ^ { - s t } \cos ( t ) ] _ { t = 0 } ^ { t  \infty } - s \int _ { 0 } ^ { \infty } e ^ { - s t } \cos ( t ) d t ) } & { { } } \\ { = - ( 1 - [ s e ^ { - s t } \sin ( t ) ] _ { t = 0 } ^ { t  \infty } - s ^ { 2 } \int _ { 0 } ^ { \infty } e ^ { - s t } \sin ( t ) d t ) } & { { } } \\ { = - 1 - s ^ { 2 } I ^ { \prime } ( s ) } & { { } \Longrightarrow { } \quad I ^ { \prime } ( s ) = - \displaystyle \frac 1 { 1 + s ^ { 2 } } . } \end{array}
$$

Now integrating we see

$$
I ( s ) - I ( 0 ) = \int _ { 0 } ^ { s } I ^ { \prime } ( r ) d r = - \int _ { 0 } ^ { s } { \frac { d r } { 1 + r ^ { 2 } } } = - \arctan ( s ) .
$$

Now lim $_ { 1 _ { s \to \infty } I ( s ) } = 0$ so

$$
\int _ { 0 } ^ { \infty } { \frac { \sin ( t ) } { t } } d t = I ( 0 ) = \operatorname* { l i m } _ { s \to \infty } ( I ( s ) + \arctan ( s ) ) = { \frac { \pi } { 2 } } .
$$

[Note: incidentally this also shows that $\begin{array} { r } { I ( s ) = \frac { \pi } { 2 } - \arctan ( s ) } \end{array}$ is the Laplace transform of $\frac { \sin ( t ) } { t } .$

Problem 25. For $a , b > 0$ and $n \in \mathbb { N }$ , define

$$
I _ { n } ( a , b ) = \int _ { 0 } ^ { \pi / 2 } \frac { d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n } } .
$$

Show that

$$
\frac { \partial I _ { n } } { \partial a } + \frac { \partial I _ { n } } { \partial b } + n I _ { n + 1 } = 0 .
$$

Evaluate $I _ { 1 } ( a , b )$ explicitly and use this to evaluate $I _ { 2 } ( a , b )$

Solution. Differentiating under the integral (legal by Leibniz rule), we find

$$
\frac { \partial I _ { n } } { \partial a } ( a , b ) = - \int _ { 0 } ^ { \pi / 2 } \frac { n \cos ^ { 2 } ( \theta ) d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } } , \quad \frac { \partial I _ { n } } { \partial b } ( a , b ) = - \int _ { 0 } ^ { \pi / 2 } \frac { n \sin ^ { 2 } ( \theta ) d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } }
$$

and so

$$
\frac { \partial I _ { n } } { \partial a } + \frac { \partial I _ { n } } { \partial b } = - n \int _ { 0 } ^ { \pi / 2 } \frac { \cos ^ { 2 } ( x ) + \sin ^ { 2 } ( x ) } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } } d x = - n I _ { n + 1 } .
$$

We can evaluate $I _ { 1 } ( a , b )$ using a u-substitution and trig. substitution:

$$
\begin{array} { r l } & { I _ { 1 } ( a , b ) = \displaystyle \int _ { 0 } ^ { \pi / 2 } \frac { d u } { \alpha \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) } } \\ & { \quad \quad \quad - \displaystyle \int _ { 0 } ^ { \pi / 2 } \frac { \sec ^ { 2 } ( x ) d x } { \alpha + b \tan ^ { 2 } ( x ) } } \\ & { \quad \quad \quad - \displaystyle \int _ { 0 } ^ { \infty } \frac { d u } { \alpha + b u ^ { 2 } } \qquad [ u - \tan ( x ) ] } \\ & { \quad \quad \quad \quad = \displaystyle \frac { 1 } { \alpha } \int _ { 0 } ^ { \infty } \frac { d u } { 1 + \frac { b } { \alpha } n ^ { 2 } } } \\ & { \quad \quad \quad = \displaystyle \frac { 1 } { \alpha } \cdot \left( \sqrt { \frac { d } { \alpha } } \right) \arctan \left( u \sqrt { \frac { b } { \alpha } } \right) \Big | _ { u = 0 } ^ { n > \infty } } \\ & { \quad \quad \quad = \displaystyle \frac { \pi } { 2 \sqrt { \alpha \delta } } . } \end{array}
$$

Then

$$
I _ { 2 } ( a , b ) = - \frac { \partial I _ { 1 } } { \partial a } ( a , b ) - \frac { \partial I _ { 1 } } { \partial b } ( a , b ) = \frac { \pi } { 4 a \sqrt { a b } } + \frac { \pi } { 4 b \sqrt { a b } } = \frac { \pi } { 4 \sqrt { a b } } \left( \frac { 1 } { a } + \frac { 1 } { b } \right) .
$$

Problem 26. Let C be the ellipse given by $( x / a ) ^ { 2 } + ( y / b ) ^ { 2 } = 1$ (where $a , b > 0 )$ . Calculate

$$
\oint _ { \mathcal { C } } ( - y ) d x + x d y .
$$

Solution. This is a classic Green’s theorem problem. Rather than try to perform the line integral, we should translate this into an area integral over the shape bounded by the curve and then integrate with the polar transform $x = a r \cos ( \theta ) , y = b r \sin ( \theta )$

$$
\oint _ { \mathcal { C } } ( - y ) d x + x d y = \int _ { D } 2 d x d y = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 1 } 2 a b r d r d \theta = 2 \pi a b .
$$

Problem 27. Let C be the triangle with vertices (0, 0), (1, 0), (1, 2). Find the path integral of $\mathbf { F } ( x , y ) = ( x y , x ^ { 2 } y ^ { 3 } )$ around this curve.

Solution. This is another classic Green’s theorem problem. We see

$$
\int _ { \mathcal { C } } \mathbf { F } \cdot d \mathbf { r } = \int _ { D } ( 2 x y ^ { 3 } - x ) d x d y = \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 2 x } ( 2 x y ^ { 3 } - x ) d y d x = \int _ { 0 } ^ { 1 } ( 8 x ^ { 5 } - 2 x ^ { 2 } ) d x = { \frac { 4 } { 3 } } - { \frac { 2 } { 3 } } = { \frac { 2 } { 3 } } .
$$

Problem 28. What is the flux of $\mathbf { F } ( x , y , z ) = ( x , y , z )$ through the surface $z = { \sqrt { 1 - x ^ { 2 } - y ^ { 2 } } }$ with normal pointing upward?

Solution. The flux through the surface is given by the surface integral of F · n where n is the normal to the surface. We can evaluate this easily using Gauss’ divergence theorem:

$$
\iint _ { S } \mathbf { F } \cdot \mathbf { n } d S = \iiint _ { V } \nabla \cdot \mathbf { F } d V = 3 \mathrm { V o l } ( V ) = 2 \pi .
$$

[Note: ordinarily we would also need to account for the flux through the bottom of the surface, but the flux of F through the bottom is zero here since $\mathbf { F } \cdot \mathbf { n } = - z = 0$ on the xy-plane.]