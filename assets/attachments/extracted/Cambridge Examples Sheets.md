# Complex Methods: Example Sheet 1 Part IB, Lent Term 2016 Dr R. E. Hunt

## Cauchy–Riemann equations

1. (i) Where, if anywhere, in the complex plane are the following functions differentiable, and where are they analytic?

Im $z$; $| z | ^ { 2 }$; sech $z$.

(ii) Let $f ( z ) = z ^ { 5 } / | z | ^ { 4 } , z \neq 0 , f ( 0 ) = 0$ . Show that the real and imaginary parts of f satisfy the Cauchy–Riemann equations at $z = 0 ,$ but that $f$ is not differentiable at $z = 0$

2. Find, as functions of z, complex analytic functions $f ( z )$ whose real parts are the following: (i) x (ii) $x y$ (iii) sin x cosh y (iv) $\log ( x ^ { 2 } + y ^ { 2 } )$ (v) $\frac { y } { ( x + 1 ) ^ { 2 } + y ^ { 2 } }$ (vi) $\tan ^ { - 1 } \left( { \frac { 2 x y } { x ^ { 2 } - y ^ { 2 } } } \right)$

Deduce that the above functions are harmonic on appropriately-chosen domains, which you should specify.

3. By considering $w ( z ) = ( i + z ) / ( i - z )$ , show that $\phi ( x , y ) = \tan ^ { - 1 } \frac { 2 x } { x ^ { 2 } + y ^ { 2 } - 1 }$ is harmonic.

4. Verify that the function $\phi ( x , y ) = e ^ { x } ( x \cos y - y \sin y )$ is harmonic. Find its harmonic conjugate and, by considering ∇φ or otherwise, determine the family of curves orthogonal to $\phi ( x , y ) = c$ for a given constant c.

Find an analytic function f(z) such that $\operatorname { R e } f = \phi$ . Can the expression $f ( z ) = \phi ( z , 0 )$ be used to determine f(z) in general?

## Branches of multi-valued functions

5. Show how the principal branch of log z can be used to define a branch of $z ^ { i }$ which is singlevalued on the domain $\mathcal { D } = \mathbb { C } \backslash \mathbb { R } ^ { - }$. Evaluate $i ^ { i }$ for this branch.

Show, using polar coordinates, that the branch of $z ^ { i }$ defined above maps $\mathcal { D }$ onto an annulus which is covered infinitely often.

How would your answers change, if at all, for a different branch?

6. How many branch points does $f ( z ) = [ z ( z + 1 ) ] ^ { 1 / 3 }$ have? Draw some possible branch cuts in the complex plane and on the Riemann sphere.

Repeat for $f ( z ) = ( z ^ { 2 } + 1 ) ^ { 1 / 2 }$

∗ Repeat also for $f ( z ) = [ z ( z + 1 ) ( z + 2 ) ] ^ { 1 / 3 } { \mathrm { ~ a n d ~ } } f ( z ) = [ z ( z + 1 ) ( z + 2 ) ( z + 3 ) ] ^ { 1 / 2 } .$

7. Let $f ( z ) = ( z ^ { 2 } - 1 ) ^ { 1 / 2 }$ , and consider two different branches of the function f (z):

f1(z) : branch cut [−1, 1], $f _ { 1 } ( x ) = + \sqrt { x ^ { 2 } - 1 }$ for real x > 1;

f2(z) : branch cut (−∞, −1] ∪ [1, ∞), $f _ { 2 } ( x ) = + i { \sqrt { 1 - x ^ { 2 } } }$ for real $x \in ( - 1 , 1 )$

Find the limiting values of $f _ { 1 }$ and $f _ { 2 }$ above and below their respective branch cuts. Prove that $f _ { 1 }$ is an odd function, i.e., $f _ { 1 } ( z ) = - f _ { 1 } ( - z )$ , and that $f _ { 2 }$ is even.

## Conformal mappings

8. How does the disc $| z - 1 | < 1$ transform under the mapping $z \mapsto z ^ { - 1 } ?$

Use the identity

$$
{ \frac { z } { ( z - 1 ) ^ { 2 } } } = \left( { \frac { 1 } { 1 - z } } - { \frac { 1 } { 2 } } \right) ^ { 2 } - { \frac { 1 } { 4 } }
$$

to show that the map $f ( z ) = z / ( z - 1 ) ^ { 2 }$ is a one-to-one conformal mapping of the disc $| z | < 1$ onto the domain $\mathbb { C } \setminus \left\{ x + i y : x \leqslant - { \frac { 1 } { 4 } } , \ y = 0 \right\}$ .

9. Find conformal mappings $f _ { i }$ of $\mathcal { U } _ { i }$ onto $\mathcal { V } _ { i }$ for each of the following cases. If the mapping is a composition of several functions, provide a sketch for each step. $\mathcal { D }$ denotes the unit disc $\{ z : | z | < 1 \}$

(i) $\mathcal { U } _ { 1 } = \{ z : \mathrm { R e } z < 0 , - 1 < \mathrm { I m } z < 1 \} , \mathcal { V } _ { 1 } = \mathcal { D } .$

(ii) $\mathcal { U } _ { 2 } = \mathcal { D } , \mathcal { V } _ { 2 }$ is the cut complex plane $\mathbb { C } \setminus \mathbb { R } ^ { - }$

(iii) $\mathcal { U } _ { 3 }$ is the angular sector $\{ z : 0 < \arg z < \alpha \} , \mathcal { V } _ { 3 } = \{ z : 0 < \mathrm { I m } z < 1 \}$

∗ (iv) $\mathcal { U } _ { 4 }$ is the open region bounded between two circles $\{ z : | z | < 1 , | z + i | > \sqrt { 2 } \} , \mathcal { V } _ { 4 } = \mathcal { D } .$

## Laplace’s equation

## 10. Show that

$g ( z ) = e ^ { z }$ maps the strip $\mathcal { S } = \{ z : 0 < \operatorname { I m } z < \pi \}$ onto the UHP $\{ z : \operatorname { I m } z > 0 \}$

$h ( z ) = \sin { z }$ maps the half-strip $\mathcal { H } = \left\{ z : - \frac { \pi } { 2 } < \mathrm { R e } z < \frac { \pi } { 2 } , \operatorname { I m } z > 0 \right\}$ onto the UHP.

Find a conformal map $f \colon \mathcal { H } \to \mathcal { H }$ . Hence find a function $\phi ( x , y )$ which is harmonic on the half-strip $\mathcal { H }$ with the following limiting values on its boundary $\partial \mathcal { H }$ :

$$ 
\phi ( x , y ) = \left\{ \begin{array} { l l } { 0 } & { \mathrm { o n } \partial \mathcal { H } \mathrm { i n } \mathrm { t h e } \mathrm { L H P } ( x < 0 ) , } \\ { 1 } & { \mathrm { o n } \partial \mathcal { H } \mathrm { i n } \mathrm { t h e } \mathrm { R H P } ( x > 0 ) . } \end{array} \right\}
$$

Give $\phi$ as a function of x and $y .$ Is there only one such function?

11. Using conformal mapping(s), find a solution to Laplace’s equation in the upper half-plane $\{ z : \operatorname { I m } z > 0 \}$ with boundary conditions

$$
\phi ( x , 0 ) = { \left\{ \begin{array} { l l } { 1 } & { x \in [ - 1 , 1 ] , } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right\} }
$$

[Find a map f of the upper half-plane onto itself that makes the boundary conditions easier to deal with.]

Comments on or corrections to this problem sheet are very welcome and may be sent to reh10@cam.ac.uk.

# Complex Methods: Example Sheet 2 Part IB, Lent Term 2016 Dr R. E. Hunt

## Taylor and Laurent series

1. Find the first two non-vanishing coefficients in the Taylor expansion about the origin of the following functions, assuming principal branches when there is a choice. You may make use of standard series expansions for $\log ( 1 + z )$ , etc.

$$
z / \log ( 1 + z )
$$

$$
( \cos z ) ^ { 1 / 2 } - 1
$$

$$
\log ( 1 + e ^ { z } )
$$

$$
e ^ { e ^ { z } } ,
$$

State the range of values of z for which each series converges.

How would your answers differ if you assumed branches different from the principal branch?

2. Let $a , b$ be complex constants with $0 < | a | < | b |$ . Use partial fractions to find the Laurent expansions of $1 { \big / } \{ ( z - a ) ( z - b ) \}$ about $z = 0$ in each of the regions $| z | < | a | , | a | < | z | < | b |$ and $| z | > | b |$

3. Find the first three terms of the Laurent expansion of $f ( z ) = \csc ^ { 2 } z$ valid for $0 < | z | < \pi$

∗ Show that the function $h ( z ) = f ( z ) - z ^ { - 2 } - ( z + \pi ) ^ { - 2 } - ( z - \pi ) ^ { - 2 }$ has only removable singularities in $| z | < 2 \pi$ . Explain how to remove them to obtain a function $H ( z )$ analytic in that region. Find a Taylor series for $H ( z )$ about the origin and explain why it must be convergent in $| z | < 2 \pi$ Hence, or otherwise, find the three non-zero central terms of the Laurent expansion of $f ( z )$ valid for $\pi < | z | < 2 \pi$

4. Write down the location and type of each of the singularities of the following functions: (i) $\frac { 1 } { z ^ { 3 } ( z - 1 ) ^ { 2 } }$ (ii) $\tan z$ (iii) $z \operatorname { c o t h } z$ (iv) $\frac { e ^ { z } - e } { ( 1 - z ) ^ { 3 } }$ (v) $\exp ( \tan z )$ (vi) $\sinh { \frac { z } { z ^ { 2 } - 1 } }$ (vii) $\log ( 1 + e ^ { z } )$ (viii) $\tan ( z ^ { - 1 } )$

## Integration and residues

5. Evaluate $\oint _ { \gamma } \bar { z } \mathrm { d } z$ when γ is the circle $| z | = 1 ,$ and when $\gamma$ is the circle $| z - 1 | = 1$

6. (i) Show that if $f ( z )$ is analytic, then the residue of $f ( z ) / ( z - z _ { 0 } )$ at $z = z _ { 0 }$ is $f ( z _ { 0 } )$

(ii) Show that if $1 / f ( z )$ has a simple pole at $z = z _ { 0 } ,$ then its residue at $z = z _ { 0 }$ is $1 / f ^ { \prime } ( z _ { 0 } )$

(iii) Show that if $h ( z )$ has a simple zero at $z = z _ { 0 }$ and $g ( z )$ is analytic and non-zero, the residue of $g ( z ) / h ( z )$ at $z = z _ { 0 }$ is $g ( z _ { 0 } ) / h ^ { \prime } ( z _ { 0 } )$

(iv) Prove the formula for the residue of a function $f ( z )$ that has a pole of order N at $z = z _ { 0 } \mathrm { : }$

$$
\operatorname* { l i m } _ { z \to z _ { 0 } } \left\{ \frac { 1 } { ( N - 1 ) ! } \frac { \mathrm { d } ^ { N - 1 } } { \mathrm { d } z ^ { N - 1 } } \big ( ( z - z _ { 0 } ) ^ { N } f ( z ) \big ) \right\} .
$$

7. Evaluate, using Cauchy’s theorem or the residue theorem,

(i) $\oint _ { \gamma _ { 1 } } \frac { \mathrm { d } z } { 1 + z ^ { 2 } }$ (ii) $\oint _ { \gamma _ { 2 } } { \frac { \mathrm { d } z } { 1 + z ^ { 2 } } }$ (iii) $\oint _ { \gamma _ { 3 } } { \frac { e ^ { z } \cos z \mathrm { d } z } { ( 1 + z ^ { 2 } ) \sin z } }$ ∗ (iv) $\oint _ { \gamma _ { 4 } } \frac { z ^ { 3 } e ^ { 1 / z } \mathrm { d } z } { 1 + z }$

where $\gamma _ { 1 }$ is the ellipse $x ^ { 2 } + 4 y ^ { 2 } = 1 , \gamma _ { 2 }$ is the circle $x ^ { 2 } + y ^ { 2 } = 2 , \gamma _ { 3 }$ is the circle $| z - ( 2 + i ) | = { \sqrt { 2 } }$ and $\gamma _ { 4 }$ is the circle $| z | = 2$

8. By integrating the function $z ^ { n } ( z - a ) ^ { - 1 } ( z - a ^ { - 1 } ) ^ { - 1 }$ around the unit circle in the z-plane (where a is real, $a > 1$, and n is a non-negative integer), evaluate

$$
\int _ { 0 } ^ { 2 \pi } { \frac { \cos n \theta } { 1 - 2 a \cos \theta + a ^ { 2 } } } \mathrm { d } \theta .
$$

## The calculus of residues

9. Evaluate $\lim _ { R \to \infty } \int _ { - R } ^ { R } { \frac { x \mathrm { d } x } { 1 + x + x ^ { 2 } } }$ . Why is the limit here rather than just the integral $\int _ { - \infty } ^ { \infty } \mathrm { d } z$

10. By integrating around a keyhole contour, show that

$$
\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } \mathrm { d } x } { 1 + x } } = { \frac { \pi } { \sin ( \pi a ) } } \qquad ( 0 < a < 1 ) .
$$

Explain why the given restrictions on the value of a are necessary.

∗ 11. By integrating around a contour involving the real axis and the line $z = r e ^ { 2 \pi i / n }$ , evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { \mathrm { d } x } { 1 + x ^ { n } } } \qquad ( n \geqslant 2 ) .
$$

Check (by change of variable) that your answer agrees with that of the previous question.

12. Establish the following:

$$
\int _ { 0 } ^ { \infty } { \frac { \cos { x } } { ( 1 + x ^ { 2 } ) ^ { 3 } } } \mathrm { d } x = { \frac { 7 \pi } { 1 6 e } }\tag{i}
$$

$$
\int _ { 0 } ^ { \infty } { \frac { \sin ^ { 2 } { x } } { x ^ { 2 } } } \mathrm { { d } } x = { \frac { \pi } { 2 } }\tag{iii}
$$

$$
\int _ { 0 } ^ { \infty } { \frac { \log x } { 1 + x ^ { 2 } } } \mathrm { d } x = 0 .
$$

[For part (iii), integrate $( \log z ) ^ { 2 } / ( 1 + z ^ { 2 } )$ around a keyhole, or log $z / ( 1 + z ^ { 2 } )$ along the real axis (or both). What goes wrong if you integrate log $z / ( 1 + z ^ { 2 } )$ around a keyhole?]

∗ 13. Let $P ( z )$ be a non-constant polynomial. Consider the contour integral

$$
I = \oint _ { \gamma } { \frac { P ^ { \prime } ( z ) } { P ( z ) } } \mathrm { d } z .
$$

Show that, if $\gamma$ is a contour that encloses no zeros of $P ,$ then $I = 0$

Evaluate the limit of I as $R \to \infty ,$ where $\gamma$ is the circle $| z | = R ,$ and deduce that $P$ has at least one zero in the complex plane.

14. By considering the integral of $f ( z ) = \cot z / ( z ^ { 2 } + \pi ^ { 2 } a ^ { 2 } )$ around a suitable large contour, prove that, provided ia is not an integer,

$$
\sum _ { n = - \infty } ^ { \infty } { \frac { 1 } { n ^ { 2 } + a ^ { 2 } } } = { \frac { \pi } { a } } \coth ( \pi a ) .
$$

By considering a similar integral prove also that, if a is not an integer,

$$
\sum _ { n = - \infty } ^ { \infty } \frac { 1 } { ( n + a ) ^ { 2 } } = \frac { \pi ^ { 2 } } { \sin ^ { 2 } ( \pi a ) } .
$$

Find an expression for $\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } + a ^ { 2 } } }$ and take the limit as $a \to 0$ to deduce the value of $\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { n ^ { 2 } } }$

Comments on or corrections to this problem sheet are very welcome and may be sent to reh10@cam.ac.uk.

# Complex Methods: Example Sheet 3 Part IB, Lent Term 2016 Dr R. E. Hunt

Fourier Transforms

1. Let

$$
f ( x ) = { \left\{ \begin{array} { l l } { 1 } & { | x | < { \frac { 1 } { 2 } } a , } \\ { 0 } & { { \mathrm { o t h e r w i s e } } ; } \end{array} \right\} } \qquad g ( x ) = { \left\{ \begin{array} { l l } { a - | x | } & { | x | < a , } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right\} }
$$

Show that

$$
\widetilde f ( k ) = \frac { 2 } { k } \sin \frac { a k } { 2 } \quad \mathrm { a n d } \quad \widetilde g ( k ) = \frac { 4 } { k ^ { 2 } } \sin ^ { 2 } \frac { a k } { 2 } .
$$

Verify by contour integration the inversion formula for $f ( x )$ , including the value at $x = { \textstyle { \frac { 1 } { 2 } } } a$ What is the convolution of $f$ with itself?

2. Using the results of the previous question and Parseval’s identity, evaluate the integrals

$$
\int _ { - \infty } ^ { \infty } \frac { \sin ^ { 2 } x } { x ^ { 2 } } \mathrm { d } x \quad \mathrm { a n d } \quad \int _ { - \infty } ^ { \infty } \frac { \sin ^ { 4 } x } { x ^ { 4 } } \mathrm { d } x .
$$

3. By using the relationship between the Fourier transform and its inverse, show that for real a and b with $a > 0$ ,

$$
e ^ { - a | t | } = { \frac { a } { \pi } } \int _ { - \infty } ^ { \infty } { \frac { 1 } { \omega ^ { 2 } + a ^ { 2 } } } e ^ { i \omega t } \mathrm { d } \omega \quad { \mathrm { a n d } } \quad e ^ { - a t } \sin b t H ( t ) = { \frac { 1 } { 2 \pi } } \int _ { - \infty } ^ { \infty } { \frac { b } { ( i \omega + a ) ^ { 2 } + b ^ { 2 } } } e ^ { i \omega t } \mathrm { d } \omega
$$

where $H ( t )$ is the Heaviside step function. What are the values of the integrals when $a < 0 ?$ What happens when $a = 0 ?$

4. Show that the convolution of the function $e ^ { - | x | }$ with itself is given by $f ( x ) = ( 1 + | x | ) e ^ { - | x | }$ . Use the convolution theorem to show that

$$
f ( x ) = { \frac { 2 } { \pi } } \int _ { - \infty } ^ { \infty } { \frac { e ^ { i k x } } { ( 1 + k ^ { 2 } ) ^ { 2 } } } \mathrm { d } k
$$

and verify this result by contour integration.

∗ 5. Suppose that $f ( x )$ has period $2 \pi$ and let $g ( x ) = f ( x ) e ^ { - a | x | }$ where $a > 0$ . Show that the Fourier Transform of $g$ is given by

$$
\widetilde { g } ( k ) = \frac { F ( k - i a ) } { 1 - e ^ { - 2 \pi i ( k - i a ) } } - \frac { F ( k + i a ) } { 1 - e ^ { - 2 \pi i ( k + i a ) } }
$$

where $\begin{array} { r } { F ( k ) = \int _ { 0 } ^ { 2 \pi } f ( x ) e ^ { - i k x } \mathrm { d } x . } \end{array}$

Assuming that $F$ is analytic, sketch the locations of the singularities of $\widetilde g$ in the complex k-plane. Further assuming that $F$ decays sufficiently quickly at infinity, use the Fourier inversion theorem and a suitable contour to show that

$$
g ( x ) = { \frac { 1 } { 2 \pi } } \sum _ { n = - \infty } ^ { \infty } F ( n ) e ^ { ( i n - a ) x }
$$

for $x > 0$ and derive a similar result when $x < 0$

Deduce that

$$
f ( x ) = { \frac { 1 } { 2 \pi } } \sum _ { n = - \infty } ^ { \infty } F ( n ) e ^ { i n x } .
$$

[This shows how the Fourier transform representation of a function reduces to a Fourier series if the function is periodic.]

## Laplace Transforms

6. Starting from the Laplace transform of 1 (namely $p ^ { - 1 } )$ , and using only standard properties of the Laplace transform (shifting, etc.), find the Laplace transforms of the following functions: $\mathrm { ( i ) } e ^ { - 2 t } \mathrm { ( i i ) } t ^ { 3 } e ^ { - 3 t } \mathrm { ( i i i ) } e ^ { 3 t } \sin 4 t \mathrm { ( i v ) } e ^ { - 4 t }$ cosh 2t.

7. Using partial fractions and expressions for the Laplace transforms of elementary functions, find the inverse Laplace transform of $\widehat { f } ( p ) = ( p + 3 ) / \{ ( p - 2 ) ( p ^ { 2 } + 1 ) \}$ . Verify this result using the Bromwich inversion formula.

8. Use Laplace transforms to solve the differential equation

$$
y ^ { \prime \prime \prime } - 3 y ^ { \prime \prime } + 3 y ^ { \prime } - y = t ^ { 2 } e ^ { t }
$$

with initial conditions $y ( 0 ) = 1 , y ^ { \prime } ( 0 ) = 0 , y ^ { \prime \prime } ( 0 ) = - 2 .$

9. Solve the integral equation $f ( t ) + 4 \int _ { 0 } ^ { t } ( t - \tau ) f ( \tau ) \mathrm { d } \tau = t$ for the unknown function $f .$ Verify your solution.

10. Solve the system of differential equations ${ \frac { \mathrm { d } } { \mathrm { d } t } } \left( { \begin{array} { l } { x } \\ { y } \end{array} } \right) = \left( { \begin{array} { l l } { - 5 } & { 1 0 } \\ { - 1 } & { 1 } \end{array} } \right) \left( { \begin{array} { l } { x } \\ { y } \end{array} } \right) \mathrm { w i t h } \left( { \begin{array} { l } { x } \\ { y } \end{array} } \right) = \left( { \begin{array} { l } { 3 } \\ { 1 } \end{array} } \right) \mathrm { a t } t = 0 .$

∗ 11. The zeroth order Bessel function $J _ { 0 } ( t )$ satisfies the differential equation

$$
t J _ { 0 } ^ { \prime \prime } + J _ { 0 } ^ { \prime } + t J _ { 0 } = 0
$$

with $J _ { 0 } ( 0 ) = 1$ (and $J _ { 0 } ^ { \prime } ( 0 ) = 0$ from the equation). Find the Laplace transform of $J _ { 0 }$ and deduce that $\begin{array} { r } { \int _ { 0 } ^ { \infty } J _ { 0 } ( t ) \mathrm { d } t = 1 } \end{array}$ . Find the convolution of $J _ { 0 }$ with itself.

12. Use Laplace transforms to solve the heat equation $\partial T / \partial t = \partial ^ { 2 } T / \partial x ^ { 2 }$ with boundary conditions $T ( x , 0 ) = 3 \sin { 2 \pi x } ( 0 < x < 1 ) , T ( 0 , t ) = T ( 1 , t ) = 0 ( t > 0 )$

13. Using the equality $\begin{array} { r } { \int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } \mathrm { d } x = \frac { 1 } { 2 } \sqrt { \pi } , } \end{array}$ find the Laplace transform of $f ( t ) = t ^ { - 1 / 2 }$ . By integrating around a Bromwich keyhole contour, verify the inversion formula for $f ( t )$ . What is the Laplace transform of $t ^ { 1 / 2 } ?$

∗ 14. The gamma and beta functions are defined for $z , w \in \mathbb { C }$ by

$$
\Gamma ( z ) = \int _ { 0 } ^ { \infty } t ^ { z - 1 } e ^ { - t } \mathrm { d } t \quad \mathrm { a n d } \quad B ( z , w ) = \int _ { 0 } ^ { 1 } t ^ { z - 1 } ( 1 - t ) ^ { w - 1 } \mathrm { d } t
$$

when Re z, Re w > 0 (and by analytic continuation elsewhere). Show that $\Gamma ( z + 1 ) = z \Gamma ( z )$ and hence that $\Gamma ( n + 1 ) = n !$ if n is a positive integer. Using the previous question, write down the value of $\Gamma ( \frac 1 2 )$

For a fixed value of $z ,$ find the Laplace transform of $f ( t ) = t ^ { z - 1 }$ in terms of $\Gamma ( z )$ . Find the Laplace transform of the convolution $t ^ { z - 1 } * t ^ { w - 1 }$ . Hence establish that

$$
B ( z , w ) = { \frac { \Gamma ( z ) \Gamma ( w ) } { \Gamma ( z + w ) } } .
$$