## Practice Problems

1. If $p ( z )$ is a polynomial of degree greater than or equal to 2, show the sum of the residues of $\frac { 1 } { p ( z ) }$ at all the zeros of p must be equal to 0.

Proof. $p ( z )$ is a polynomial, so it has finitely many zeros $b _ { 1 } , b _ { 2 } , . . . , b _ { n }$ . Take $R > 0$ such that $R >$ $\operatorname* { m a x } _ { k = 1 } ^ { n } \left| b _ { k } \right|$ . Then all the zeros of $p ( z )$ are contained interior the contour $C _ { R } { \mathrm { : } }$ , the circle of radius R centered at 0, oriented counter-clockwise. So then

$$
\int _ { \gamma } { \frac { 1 } { p ( z ) } } d z = 2 \pi i \sum _ { k = 1 } ^ { n } \operatorname { R e s } p ( z ) = 2 \pi i \operatorname { R e s } { \frac { 1 } { z = 0 } } { \frac { 1 } { z ^ { 2 } } } { \frac { 1 } { p \left( { \frac { 1 } { z } } \right) } }
$$

$$
\begin{array} { l } { { \mathrm { N o w ~ i f ~ } p ( z ) = a _ { m } z ^ { m } + a _ { m - 1 } z ^ { m - 1 } + . . . + a _ { 0 } \mathrm { , ~ w i t h ~ } a _ { m } \mp 0 , \mathrm { ~ t h e n ~ } } } \\ { { \displaystyle \frac { 1 } { z ^ { 2 } p \Big ( \frac { 1 } { z } \Big ) } = \frac { 1 } { z ^ { 2 } \big ( a _ { m } z ^ { - m } + a _ { m - 1 } z ^ { - m + 1 } + . . . + a _ { 0 } \big ) } = \frac { z ^ { m - 2 } } { a _ { m } + a _ { m - 1 } z + . . . + a _ { 0 } z ^ { m } } } , } \end{array}
$$

where $m - 2 \geq 0$ since the degree of $p$ was assumed to be at least 2.

So finally $\frac { z ^ { m - 2 } } { a _ { m } + a _ { m - 1 } z + \ldots + a _ { 0 } z ^ { m } }$ is analytic at 0, since the denominator doesn’t vanish at 0 (as $a _ { m } \neq 0 )$ , therefore

$$
\displaystyle \mathop { \mathrm { R e s } } _ { z = 0 } \frac { 1 } { z ^ { 2 } } \frac { 1 } { p \Big ( \frac { 1 } { z } \Big ) } = 0 \Rightarrow 2 \pi i \sum _ { k = 1 } ^ { n } \operatorname { R e s } _ { z = b _ { k } } p ( z ) = 0 \Rightarrow \sum _ { k = 1 } ^ { n } \operatorname { R e s } _ { z = b _ { k } } p ( z ) = 0
$$

2. Show informally that if $\gamma$ is a simple closed curve traveled counterclockwise, then

$$
\int _ { \gamma } f ( z ) d z = - 2 \pi i \sum ( { \mathrm { ~ R e s i d u e s ~ o f ~ f ~ o u t s i d e } } \gamma , { \mathrm { ~ i n c l u d i n g ~ } } \infty )
$$

Proof. Intuitively, γ is a curve on the Riemann Sphere that on the one hand encloses all the residues of f inside γ, but on the other hand encloses all the poles of $f$ outside $\gamma$ including ∞. However if γ is positively oriented around the poles inside γ, it is negatively oriented around the poles outside γ. In symbols:

$$
\begin{array} { c } { { { \displaystyle \int _ { \gamma } f ( z ) d z - 2 \pi i \sum ( \mathrm { \small ~ R e s i d u e s ~ o f ~ f ~ i n s i d e ~ } \gamma ) = 0 } } } \\ { { { \displaystyle \Leftrightarrow \int _ { \gamma } f ( z ) d z + 2 \pi i \sum ( \mathrm { \small ~ R e s i d u e s ~ o f ~ f ~ o u t s i d e ~ } \gamma , \mathrm { \small ~ i n c l u d i n g ~ \infty ) = 0 } } } } \end{array}
$$

$$
\int _ { \gamma } f ( z ) d z = - 2 \pi i \sum ( { \mathrm { ~ R e s i d u e s ~ o f ~ f ~ o u t s i d e ~ } } \gamma , { \mathrm { ~ i n c l u d i n g ~ } } \infty )
$$

Alternatively, you could apply the Theorem in section $7 7$ (the one used in problem 1 above), to show $\operatorname { R e s } _ { z = \infty } f ( z ) = - \sum$ Residues of f in C, from which the result follows.

## 3. Evaluate $\textstyle \int _ { - \infty } ^ { \infty } { \frac { x ^ { 2 } } { 1 + x ^ { 4 } } } d x$

Proof. Let $\textstyle f ( z ) = { \frac { z ^ { 2 } } { 1 + z ^ { 4 } } }$ and $\gamma = [ - R , R ] \cup C _ { R }$ , the boundary of the upper semi-circle of radius R. Then $f$ is analytic away from the zeros of $z ^ { 4 } { + } 1$ , which are $z _ { 1 } = e ^ { \frac { i \pi } { 4 } } , z _ { 2 } = e ^ { \frac { 3 i \pi } { 4 } } , z _ { 1 } = e ^ { \frac { 5 i \pi } { 4 } }$ , and $z _ { 4 } = e ^ { \frac { 7 i \pi } { 4 } }$ Only $z _ { 1 } , z _ { 2 } \in \mathbb { H }$ , so for $R > 1 , z _ { 1 } , z _ { 2 }$ lie inside γ. By the Residue Theorem,

$$
2 \pi i { \bigl ( } \operatorname { R e s } _ { z = z _ { 1 } } f ( z ) + \operatorname { R e s } _ { z = z _ { 2 } } f ( z ) { \bigr ) } = \int _ { \gamma } f ( z ) d z = \int _ { C _ { R } } f ( z ) d z + \int _ { - R } ^ { R } f ( z ) d z .
$$

And now on $\begin{array} { r } { C _ { R } , \ \left| f ( z ) \right| \le \frac { R ^ { 2 } } { R ^ { 4 } - 1 } } \end{array}$ , for $R > 1$ , by the triangle inequality. So then

$$
\int _ { C _ { R } } f ( z ) d z \le \pi R \frac { R ^ { 2 } } { R ^ { 4 } - 1 } \to 0 { \mathrm { ~ a s ~ } } R \to \infty .
$$

Therefore $\begin{array} { r } { 2 \pi i ( \mathrm { R e s } _ { z = z _ { 1 } } f ( z ) + \mathrm { R e s } _ { z = z _ { 2 } } f ( z ) ) = \operatorname* { l i m } _ { R \to \infty } \int _ { - R } ^ { R } f ( z ) d z = \int _ { - \infty } ^ { \infty } \frac { x ^ { 2 } } { 1 + x ^ { 4 } } d x } \end{array}$

Finally $\begin{array} { r } { \mathrm { R e s } _ { z = z _ { k } } f ( z ) = \mathrm { R e s } _ { z = z _ { k } } \frac { z ^ { 2 } } { 1 + z ^ { 4 } } = \left. \frac { z ^ { 2 } } { 4 z ^ { 3 } } \right| _ { z _ { L } } = \frac { 1 } { 4 z _ { k } } = \frac { - z _ { k } ^ { 3 } } { 4 } } \end{array}$ , since $z _ { k } ^ { 4 } ~ = ~ - 1$ . So now $\frac { - z _ { 1 } ^ { 3 } } { 4 } + \frac { - z _ { 2 } ^ { 3 } } { 4 } =$ $\begin{array} { r } { \frac { - 1 } { 4 } \big ( e ^ { \frac { 3 \pi i } { 4 } } + e ^ { \frac { 9 \pi i } { 4 } } \big ) = \frac { - 1 } { 4 } \big ( e ^ { \frac { 3 \pi i } { 4 } } + e ^ { \frac { 9 \pi i } { 4 } } \big ) = \frac { - 1 } { 4 } i \sqrt { 2 } . } \end{array}$

$$
\begin{array} { r } { \mathrm { S o } \int _ { - \infty } ^ { \infty } \frac { x ^ { 2 } } { 1 + x ^ { 4 } } d x = 2 \pi i ( \mathrm { R e s } _ { z = z _ { 1 } } f ( z ) + \mathrm { R e s } _ { z = z _ { 2 } } f ( z ) ) = 2 \pi i \frac { - 1 } { 4 } i \sqrt { 2 } = \pi \frac { \sqrt { 2 } } { 2 } = \frac { \pi } { \sqrt { 2 } } . } \end{array}
$$

## 4. Let $a \in \mathbb { R } \setminus \{ 0 \}$ . Evaluate $\textstyle { \int _ { - \infty } ^ { \infty } { \frac { c o s ( a x ) } { 1 + x ^ { 2 } } } d x }$

Proof. First we address the case $a > 0$ . We apply Jordan’s Lemma to the function $g ( z ) = e ^ { i a z } f ( z )$ , where $\begin{array} { r } { f ( z ) = \frac { 1 } { 1 + z ^ { 2 } } } \end{array}$ , and then we take real parts. Let $\gamma \ : = \ : [ - R , R ] \cup C _ { R }$ , as in problem 3. g is holomorphic away from the poles of $f ,$ which are simple poles at i and −i., where only i lies in the upper half plane. So for $R > 1$ the Residue Theorem gives:

$$
2 \pi i \operatorname { R e s } g ( z ) = \int _ { \gamma } g ( z ) d z = \int _ { C _ { R } } g ( z ) d z + \int _ { - R } ^ { R } g ( z ) d z .
$$

Since $\begin{array} { r } { | f ( z ) | \le \frac { 1 } { R ^ { 2 } - 1 } \to 0 } \end{array}$ as $R \to \infty$ , Jordan’s Lemma implies

$$
\int _ { C _ { R } } g ( z ) d z  0 \mathrm { { a s } } R  \infty .
$$

Thus, letting R → ∞ above, we have

$$
2 \pi i \operatorname { R e s } _ { z = i } g ( z ) = \int _ { - \infty } ^ { \infty } { \frac { e ^ { i a x } } { 1 + x ^ { 2 } } } d x .
$$

And finally, Res $_ { z = i } g ( z ) = \mathrm { R e s } _ { z = i } e ^ { i a z } \frac { 1 } { 1 + z ^ { 2 } } = \left. e ^ { i a z } \frac { 1 } { 2 z } \right| _ { z = i } = \frac { e ^ { - a } } { 2 i }$ . So then

$$
\int _ { - \infty } ^ { \infty } \frac { e ^ { i a x } } { 1 + x ^ { 2 } } d x = 2 \pi i \mathop { \mathrm { R e s } } _ { z = i } g ( z ) = 2 \pi i \frac { e ^ { - a } } { 2 i } = \pi e ^ { - a } .
$$

Taking real parts of both sides, gives us

$$
\int _ { - \infty } ^ { \infty } { \frac { c o s ( a x ) } { 1 + x ^ { 2 } } } d x = \pi e ^ { - a }
$$

When $a < 0 .$ , a similar argument shows

$$
\int _ { - \infty } ^ { \infty } { \frac { c o s ( a x ) } { 1 + x ^ { 2 } } } d x = \pi e ^ { a } .
$$

So finally we have $\forall a \ne 0$

$$
\int _ { - \infty } ^ { \infty } { \frac { c o s ( a x ) } { 1 + x ^ { 2 } } } d x = \pi e ^ { - | a | }
$$

5. Show that for $p > 0 , q > 0$ we have

$$
\int _ { 0 } ^ { \infty } { \frac { l o g ( p x ) } { q ^ { 2 } + x ^ { 2 } } } d x = { \frac { \pi } { 2 q } } l o g ( p q )
$$

Proof. Let $\textstyle g ( z ) = { \frac { \log ( p z ) } { q ^ { 2 } + z ^ { 2 } } }$ . Note to define $\log ( p z )$ we have to define a branch cut, so let $\log ( p z ) =$ ln $| z | + i a r g ( z )$ , where $\begin{array} { r } { - \frac { \pi } { 2 } < a r g ( z ) < \frac { 3 \pi } { 2 } } \end{array}$ (i.e. with a branch along the non-positive imaginary axis). Note log(pz) is not defined at the origin, so we’ll have to take our contour to be the boundary of an upper half-disk, but with a small semicircle around the origin. I.e. let $\gamma = [ r , R ] \cup C _ { R } \cup [ - R , - r ] \cup C _ { r } ^ { * }$ , where \* denotes clockwise.

Note g is analytic in and on $\gamma ,$ , (for R sufficiently large, r sufficiently small), except at simple poles $z = i q , - i q$ , where only $i q$ lies inside $\gamma$ . Furthermore, Re $\begin{array} { r } { \mathfrak { s } _ { z = q i } g ( z ) = \frac { \log \left( p i q \right) } { 2 i q } = \frac { \ln \left( p q \right) + \frac { i \pi } { 2 } } { 2 i q } \left( \operatorname { u s i n g } p , q > 0 \right) } \end{array}$ $= \frac { \ln ( p q ) } { 2 q i } + \frac { \pi } { 4 q }$

So by the Residue Theorem,

$$
2 \pi i \Big ( \frac { \ln ( p q ) } { 2 q i } + \frac { \pi } { 4 q } \Big ) = \int _ { \mathcal { X } } g ( z ) d z = \int _ { r } ^ { R } g ( z ) d z + \int _ { C _ { R } } g ( z ) d z + \int _ { - R } ^ { - r } g ( z ) d z - \int _ { C _ { r } } g ( z ) d z
$$

Now, $\begin{array} { r } { | \int _ { C _ { R } } g ( z ) d z | \le \frac { \ln ( R ) + \pi } { R ^ { 2 } - q ^ { 2 } } \to 0 } \end{array}$ as $R \to \infty$

And $\begin{array} { r } { | \int _ { C _ { r } } g ( z ) d z | \le \frac { | \ln ( r ) | + \pi } { q ^ { 2 } - r ^ { 2 } } \to 0 } \end{array}$ as $r  0$

Further, $\begin{array} { r } { \int _ { r } ^ { R } g ( z ) d z  \int _ { 0 } ^ { \infty } \frac { l o g ( p x ) } { q ^ { 2 } + x ^ { 2 } } } \end{array}$

And $\begin{array} { r } { \int _ { - R } ^ { - r } g ( z ) d z  \int _ { 0 } ^ { \infty } \frac { l o g ( p x ) } { q ^ { 2 } + x ^ { 2 } } + \pi i \int _ { 0 } ^ { \infty } \frac { 1 } { q ^ { 2 } + x ^ { 2 } } } \end{array}$ (using the subsitution ${ \tilde { x } } = - x )$

Take real and imaginary parts above to conclude

$$
{ \frac { \pi \ln ( p q ) } { q } } = 2 \int _ { 0 } ^ { \infty } { \frac { l o g ( p x ) } { q ^ { 2 } + x ^ { 2 } } } \Rightarrow \int _ { 0 } ^ { \infty } { \frac { l o g ( p x ) } { q ^ { 2 } + x ^ { 2 } } } = { \frac { \pi \ln ( p q ) } { 2 q } }
$$

6. How many zeroes does $z ^ { 4 } - 5 z + 1$ have in $\{ 1 < | z | < 2 \} ?$ (Note: this is not the set $\{ 1 \leq | z | < 2 \} )$

Proof. We apply Rouche’s Theorem to the function $f ( z ) = z ^ { 4 } - 5 z + 1$

i) First we count the zeros in the set $\{ | z | < 2 \}$

Let $g _ { 1 } ( z ) = z ^ { 4 }$ . Then on $C _ { 2 } = \big \{ | z | = 2 \big \} , | f ( z ) - g _ { 1 } ( z ) | = \big | - 5 z + 1 \big | \leq 5 \big | z \big | + 1 = 1 1 < 1 6 = \big | g _ { 1 } ( z ) \big |$ . So the number of zeros of $f$ in $\{ | z | < 2 \}$ equals the number of zeros of $g _ { 1 }$ in $\{ | z | < 2 \}$ which is 4 $( g _ { 1 }$ has a zero of order 4 at 0).

ii) We now count the zeros in the set $\{ | z | < 1 \}$

Let $g _ { 2 } = - 5 z$ . Then on $C _ { 1 } = \left\{ | z | = 1 \right\} , | f ( z ) - g _ { 2 } ( z ) | = | z ^ { 4 } + 1 | \leq | z | ^ { 4 } + 1 = 2 < 5 = | g _ { 2 } ( z ) |$ . So the number of zeros of f in $\{ | z | < 1 \}$ equals the number of zeros of $g _ { 2 }$ in $\{ | z | < 1 \}$ which is 1 (g2 has a zero of order 1 at 0).

Therefore f has 4 − 1 = 3 zeros on $\left\{ \left| z \right| < 2 \right\} \setminus \left\{ \left| z \right| < 1 \right\} = \left\{ 1 \leq \left| z \right| < 2 \right\}$

Finally, when $| z | = 1 , | f ( z ) | \geq | - 5 z | - | z | ^ { 4 } - 1 = 5 - 2 = 3 > 0 \Rightarrow f ( z ) \neq 0$ when $| z | = 1$ . So f has 3 zeros on $\{ 1 < | z | < 2 \}$

7. Show there is exactly one point z in the right half plane $\{ z : R e ( z ) > 0 \}$ at which $z + e ^ { - z } = 2$ Hint: Consider the countour in the right half plane enclosing the (nearly) half disk bounded by $\{ | z | = R \}$ and the vertical line $R e ( z ) = \epsilon \ :$ , for $R > 3$ and $\epsilon > 0$ small (so in particular, the ball of radius 1 centered at 2 is contained inside the contour).

Proof. Let γ be the contour in the hint. Then using the fact $\vert e ^ { z } \vert = e ^ { R e z }$ , on γ we have $\left| e ^ { - z } \right| = e ^ { - R e z } <$ $e ^ { 0 } = 1$ , since γ lies in $\{ z : R e ( z ) > 0 \}$ and $e ^ { x }$ is a monotonically increasing (real) function.

Now let $f ( z ) = z + e ^ { - z } - 2$ and $g ( z ) = z - 2$ . On $\gamma , \ \left| f - g \right| = \left| e ^ { - z } \right| < 1 < \left| z - 2 \right| = g { \left( z \right) }$ , since the ball of radius 1 centered at 2 is contained inside γ, so all points on γ are distance greater than 1 from 2.

So now applying Rouche’s Theorem, we have the number of zeros of f in γ equals the number of zeros of $g$ in $\gamma _ { : }$ , which equals 1, since $z - 2$ has a zero at 2, which is inside γ.

Finally, this is the only solution in the right half plane, because we can let $R \to \infty , \epsilon \to 0$ , and the previous argument remains valid (i.e. f still only has one zero inside $\gamma )$ □

8. Show if $p ( z ) = z ^ { n } + a _ { n - 1 } z ^ { n - 1 } + \ldots + a _ { 1 } z + a _ { 0 }$ , then there must be at least one point $z _ { \mathrm { 0 } }$ with $| z _ { 0 } | = 1$ such that $| p ( z _ { 0 } ) | \geq 1$ . Hint: If $| p ( z ) | < 1$ everywhere on $\{ | z | = 1 \}$ , how many zeros must $q ( z ) = a _ { n - 1 } z ^ { n - 1 } + \ldots + a _ { 1 } z + a _ { 0 }$ have?

Proof. Suppose for contradiction that $| p ( z ) | < 1$ everywhere on $\{ | z | = 1 \}$ . Let $g ( z ) = - z ^ { n } , f ( z ) =$ $p ( z ) + g ( z ) = a _ { n - 1 } z ^ { n - 1 } + \ldots + a _ { 1 } z + a _ { 0 } = q ( z )$ . Then on $\{ | z | = 1 \}$ ,

$$
| f ( z ) - g ( z ) | = | p ( z ) | < 1 = 1 ^ { n } = | g ( z ) | .
$$

So by Rouche’s Theorem f and g have the same number of zeros in the unit disk. But this is a contradiction, because g has n zeros in the unit disk, but $f$ can have at most $n - 1$ zeros there, being a polynomial of degree $n - 1$

9. Let $\textstyle f ( z ) = { \frac { z - 1 } { z + 1 } }$ . What is the image under f of:

a. The real axis (Hint: this is a line)

b. $\{ | z | = 2 \}$ (Hint: this is a circle)

c. $\{ | z | = 1 \}$

d. The imaginary axis

Proof. a. Since f is an LFT, f sends lines to circles or lines. So it suffices to check where three distinct points of R are sent to find its image under f . Note $f ( 1 ) = 0 , f ( \infty ) = 1$ , and $f ( - 1 ) = \infty$ So f sends the real axis to the line through 0 and 1, i.e. the real axis.

b. Again, f is an LFT, so it sends circles to circles or lines. And $\begin{array} { r } { f ( 2 ) = \frac { 1 } { 3 } , f ( - 2 ) = 3 . } \end{array}$ and $f ( 2 i ) =$ $\begin{array} { r } { \frac { - 1 + 2 i } { 1 + 2 i } = \frac { 1 } { 5 } \big ( - 1 + 2 i \big ) \big ( 1 - 2 i \big ) = \frac { 1 } { 5 } \big ( 3 + 4 i \big ) } \end{array}$ . Since these points don’t lie on a line, f maps $\{ | z | = 2 \}$ to the circle through these points.

c. Since $f ( - 1 ) = \infty$ , the image of $\{ | z | = 1 \}$ is a line. To find which, we map two other points: $\begin{array} { r } { f ( 1 ) = 0 , f ( i ) = \frac { i - 1 } { i + 1 } = \frac { ( i - 1 ) ^ { 2 } } { 2 } = - i } \end{array}$ . Thus f maps $\{ | z | = 1 \}$ to the line through 0 and −i, i.e. the imaginary axis.

d. You may recall $\textstyle f ( z ) = { \frac { z - 1 } { z + 1 } }$ maps the right half plane to the unit disk, sending the boundary to the boundary. To veryify this, i ${ \textrm { f } } z = i y , | f ( z ) | = | { \frac { i y - 1 } { i y + 1 } } = | ( - 1 ) { \frac { i y - 1 } { - i y - 1 } } | = 1$ , since $- i y - 1$ is the conjugate of $i y - 1$ . Thus the image of the imaginary axis under f is a subset of the unit circle. But since $f$ is invertible, and the imaginary axis is sent to a line or a circle, it follows that the f sends the imaginary axis to the entire unit circle.

10. Suppose $a , b , c , d \in \mathbb { R } , a d > b c$ . Show $\begin{array} { r } { T ( z ) = \frac { a z + b } { c z + d } } \end{array}$ leaves the upper half plane H invariant (i.e. T sends the upper half plane to itself).

Proof. First we note that since T is an LFT, it sends lines to circles or lines. T clearly then sends the real line to itself, since if $x \in \mathbb { R }$ , both the numerator and denominator of $\textstyle T ( x ) = { \frac { a x + b } { c x + d } }$ are real numbers $\textstyle { \left( { \mathrm { i f ~ } } x = { \frac { - d } { c } } \right. }$ , then $T ( x ) = \infty$ , which still lines on the real line).

Therefore by the continuity of T, it suffices to check that $T ( z _ { 0 } )$ lands in the upper half plane, for any $z _ { 0 } \in \mathbb { H } .$ . So let $z _ { 0 } = i .$ . Then $\begin{array} { r } { T ( i ) = \frac { a i + b } { c i + d } = \frac { ( b + a i ) ( d - c i ) } { c ^ { 2 } + d ^ { 2 } } = \frac { ( b d + a c ) + i ( a d - b c ) } { c ^ { 2 } + d ^ { 2 } } } \end{array}$ . So then $\begin{array} { r } { I m ( T ( i ) ) = \frac { ( a d - b c ) } { c ^ { 2 } + d ^ { 2 } } > 0 } \end{array}$ since $a d - b c > 0$ , by assumption. Thus $T ( i ) \in \mathbb { H }$ , so we’re done. □

11. Find a bijective conformal map that takes a bounded region of C to an unbounded region.

Proof. Take $\begin{array} { r } { f ( z ) = \frac { 1 } { z } } \end{array}$ . Then f sends the bounded set $\{ 0 < | z | < 1 \}$ to the unbounded set $\{ | z | > 1 \}$ Moreover $f$ is conformal on $\{ 0 < | z | < 1 \}$ , since $f$ is analytic there, and $\begin{array} { r }  f ^ { \prime } ( z ) ~ = ~ \frac { - 1 } { z ^ { 2 } } ~ \ne ~ 0 , ~ \forall z ~ \in \ \end{array}$ $\mathbb { C } \setminus \{ 0 \}$ ,

12. What is the image of the region $A = \left\{ x + i y : x y > 1 , x > 0 , y > 0 \right\}$ under the transformation $f ( z ) = z ^ { 2 } ?$

Proof. Note, in the right half plane $\{ R e ( z ) > 0 \} , f ( z ) = z ^ { 2 }$ is conformal, since $f ^ { \prime } ( z ) = 2 z = 0 { \mathrm { ~ i f f ~ } } z = 0$ So it suffices to map the boundary of A and see where a point in the interior is sent. The boundary of A is the part of the curve $x y = 1$ in the first quadrant $\{ x > 0 , y > 0 \}$ . Now $f ( x + i y ) = x ^ { 2 } - y ^ { 2 } + i 2 x y$ , so the image of $x y = 1$ is the set $v = 2$ in the $u , v$ plane. So now the interior point $2 + 2 i = 2 \sqrt { 2 } e ^ { \frac { i \pi } { 4 } }$ is sent to 8i under f. So the image of A under f is the set $\{ v > 2 \}$ . □

13. Let A be the upper half of the unit disk $\{ | z | < 1 \}$ . Find the temperature T inside A if the circular portion of the boundary is insulated, and $T = 0$ for $0 < x < 1$ on the real axis, and $T = 1 0$ for $- 1 < x < 0$ on the real axis.

Proof. Use the map $\log ( z )$ to make A to the half strip $B = \left. u < 0 , 0 < v < \pi \right.$ in the $u , v$ plane, where the temperature is 10 when $v = \pi$ and 0 when $v = 0$ . Then the in the half-strip, we have $\begin{array} { r } { T _ { 0 } = \frac { 1 0 v } { \pi } } \end{array}$ Therefore the tempterature in the $x , y$ plane is given by $\begin{array} { r } { T ( x , y ) = T _ { 0 } ( \log ( x + i y ) ) = \frac { 1 0 } { \pi } t a n ^ { - 1 } ( \frac { y } { x } ) } \end{array}$ .

14. Consider the region the entire unit disk $\{ | z | < 1 \}$ . The electric potential is maintained at $\phi = 0$ on the lower semicicle and at $\phi = 1$ on the upper semicircle. Find the value of $\phi$ inside.

Proof. We apply our general procedure for the Dirichlet problem by mapping the unit disk to the upper half plane. We can do this with the LFT

$$
u + i v = f ( x + i y ) = f { \big ( } z { \big ) } = { \frac { 1 } { i } } { \frac { z + 1 } { z - 1 } } = { \frac { 1 } { i } } { \frac { ( x + 1 ) + i y } { ( x - 1 ) + i y } }
$$

So then $\begin{array} { r } { u = \frac { - 2 y } { ( x - 1 ) ^ { 2 } + y ^ { 2 } } } \end{array}$ and $\begin{array} { r } { v = \frac { 1 - x ^ { 2 } - y ^ { 2 } } { ( x - 1 ) ^ { 2 } + y ^ { 2 } } } \end{array}$ . We can use the standard solution on the upper half plane:

$$
\phi _ { 0 } ( u , v ) = 0 + \frac { 1 } { \pi } \bigl ( 1 - 0 \bigr ) \tan ^ { - 1 } \frac { v } { u } = \frac { 1 } { \pi } \tan ^ { - 1 } \frac { v } { u }
$$

The solution on the unit disk is then

$$
\phi ( x , y ) = \phi _ { 0 } ( f ( x , y ) ) = \phi _ { 0 } ( u , v ) = \frac { 1 } { \pi } \tan ^ { - 1 } \Big ( \frac { x ^ { 2 } + y ^ { 2 } - 1 } { 2 } \Big ) ,
$$

where the values of arctangent must be taken between 0 and $\pi .$

15. Find the flow around the upper half of the unit circle if the velocity is parallel to the x axis and is α at ∞. (Here A is the region of the upper-half plane exterior to the unit circle, i.e. $A = \{ \mathrm { z } : I m ( z ) > 0 , | z | > 1 \}$ .

Proof. Use the mapping $z \mapsto z + { \frac { 1 } { z } }$ . This maps A to the upper half plane, and $F _ { 0 } ( z ) = \alpha z$ is the complex potential in the upper half plane, so the potential in A is given by $\begin{array} { r } { F ( z ) = \alpha ( z + \frac { 1 } { z } ) } \end{array}$ . And then $\begin{array} { r } { \phi ( r , \theta ) = \alpha \Big ( r + \frac { 1 } { r } \Big ) \cos \theta , \psi ( r , \theta ) = \alpha \Big ( r - \frac { 1 } { r } \Big ) \sin \theta } \end{array}$ □

16. Let f be analytic in a domain (open and connected) A, and let $z _ { 1 } , z _ { 2 } \in A$ . Let $f ^ { \prime } ( z _ { 1 } ) \neq 0$ . Show f is not constant on a neighborhood of $z _ { 2 }$ .

Proof. Suppose for contraction $f \ = \ c$ constant, on a neighborhood $\boldsymbol { B } ( z _ { 2 } , r )$ of $z _ { 2 }$ . Then since $B ( z _ { 2 } , r ) \subset A$ (connected) has accumulation points (every point is one in fact), the Identity Principle implies that $f = c$ constant on A, since $\{ z \in A : f ( z ) - c = 0 \}$ . has an accumulation point in A. But if that were the case, then $f ^ { \prime } ( z ) = 0 ~ \forall z \in A$ , so in particular, $f ^ { \prime } { \big ( } z _ { 1 } ) = 0$ , a contraction. Therefore f is non-constant on all neighborhoods of $z _ { 2 }$