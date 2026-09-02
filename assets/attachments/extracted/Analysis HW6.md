# Math 8100 Assignment 6 The Fourier Transform

Due date: Thursday the 31st of October 2019

Recall that we have defined the Fourier transform of an integrable function f on $\mathbb { R } ^ { n }$ by

$$
{ \widehat { f } } ( \xi ) = \int _ { \mathbb { R } ^ { n } } f ( x ) e ^ { - 2 \pi i x \cdot \xi } d x
$$

where $x \cdot \xi = x _ { 1 } \xi _ { 1 } + \cdot \cdot \cdot + x _ { n } \xi _ { n }$ and the convolution of two integrable functions f and g on $\mathbb { R } ^ { n }$ by

$$
f * g ( x ) = \int _ { \mathbb { R } ^ { n } } f ( x - y ) g ( y ) d y .
$$

1. Prove that if $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ , then ${ \widehat { f } } ( \xi ) \to 0 { \mathrm { ~ a s ~ } } | \xi | \to \infty$ . (This is called the Riemann-Lebesgue lemma.)

Hint: Write $\begin{array} { r } { \widehat { f } ( \xi ) = \frac { 1 } { 2 } \int [ f ( x ) - f ( x - \xi ^ { \prime } ) ] e ^ { - 2 \pi i x \cdot \xi } d x } \end{array}$ , where $\begin{array} { r } { \xi ^ { \prime } = \frac { \xi } { 2 | \xi | ^ { 2 } } } \end{array}$

2. (a) Prove that if $f , g \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ , then ${ \widehat { f * g } } ( \xi ) = { \widehat { f } } ( \xi ) { \widehat { g } } ( \xi )$ for all $\xi \in \mathbb { R } ^ { n }$

(b) Conclude from part (a) that

i. if $f , g , h \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ , then $f * g = g * f$ and $( f * g ) * h = f * ( g * h )$ almost everywhere.

ii.
there does not exist $I \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ such that $f * I = f$ almost everywhere for all $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$

3. Let $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$

(a) Show that if $y \in \mathbb { R } ^ { n }$ and

i. $g ( x ) = f ( x - y )$ for all $x \in \mathbb { R } ^ { n }$ , then ${ \widehat { g } } ( \xi ) = e ^ { - 2 \pi i y \cdot \xi } { \widehat { f } } ( \xi )$ for all $\xi \in \mathbb { R } ^ { n }$

ii.
$h ( x ) = e ^ { 2 \pi i x \cdot y } f ( x )$ for all $x \in \mathbb { R } ^ { n }$ , then ${ \widehat { h } } ( \xi ) = { \widehat { f } } ( \xi - y )$ for all $\xi \in \mathbb { R } ^ { n }$

(b) Show that if T be a non-singular linear transformation of $\mathbb { R } ^ { n }$ and $S = ( T ^ { * } ) ^ { - 1 }$ denote its inverse transpose, then

$$
{ \widehat { f \circ T } } ( \xi ) = { \frac { 1 } { | \operatorname* { d e t } T | } } { \widehat { f } } ( S \xi )
$$

for all $\xi \in \mathbb { R } ^ { n }$

4. (a) Let $f \in L ^ { 1 } ( \mathbb { R } )$

i. Let $g ( x ) = x f ( x )$ . Show that if $g \in L ^ { 1 }$ , then $\widehat { f }$ is differentiable and $\begin{array} { r } { \frac { d } { d \xi } \widehat { f } ( \xi ) = - 2 \pi i \widehat { g } ( \xi ) } \end{array}$

ii.
Let $f \in C _ { 0 } ^ { 1 } ( \mathbb { R } )$ and $\textstyle h ( x ) = { \frac { d } { d x } } f ( x )$ . Show that if $h \in L ^ { 1 }$ , then ${ \widehat { h } } ( \xi ) = 2 \pi i \xi { \widehat { f } } ( \xi )$

Recall that $C _ { 0 } ^ { 1 } ( \mathbb { R } )$ is the collection of functions in $C ^ { 1 } ( \mathbb { R } )$ which vanishes at infinity.

(b) Let $G ( x ) = e ^ { - \pi x ^ { 2 } }$ . By considering the derivative of ${ \widehat { G } } ( \xi ) / G ( \xi )$ , show that ${ \widehat { G } } ( \xi ) = G ( \xi )$

Hint: You may also want to use the fact that $\begin{array} { r } { \int _ { \mathbb { R } } G ( x ) d x = 1 } \end{array}$ (see “challenge” problem).

5. The functions D, F , and P defined below are all bounded $L ^ { + } ( \mathbb { R } )$ functions with integrals equal to 1.

(a) Show that if

$$
D ( x ) = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { ~ i f ~ } } | x | \leq 1 / 2 } \\ { 0 } & { { \mathrm { ~ o t h e r w i s e } } } \end{array} \right. }
$$

then

$$
\widehat { D } ( \xi ) = \frac { \sin \pi \xi } { \pi \xi } .
$$

This gives, in light of Assignment 5 Challenge Problem $1 ( a )$ , an explicit example of a function which is not in $L ^ { 1 } ( \mathbb { R } )$ , but yet is the Fourier transform of an $L ^ { 1 }$ function.
See Question 6 for additional higher dimensional examples.

(b) Let

$$
F ( x ) = { \left\{ \begin{array} { l l } { 1 - | x | } & { { \mathrm { ~ i f ~ } } | x | \leq 1 } \\ { 0 } & { { \mathrm { ~ o t h e r w i s e } } } \end{array} \right. } .
$$

i. Show that

$$
\widehat { F } ( \xi ) = \left( \frac { \sin \pi \xi } { \pi \xi } \right) ^ { 2 } .
$$

Hint: It may help to write ${ \widehat { F } } ( \xi ) = h ( \xi ) + h ( - \xi )$ where $\begin{array} { r } { h ( \xi ) = e ^ { 2 \pi i \xi } \int _ { 0 } ^ { 1 } y e ^ { - 2 \pi i y \xi } d y } \end{array}$

ii.
Find the Fourier transform of the function

$$
f ( x ) = \left( \frac { \sin \pi x } { \pi x } \right) ^ { 2 } .
$$

Be careful to fully justify your answer.

(c) Show that if

$$
P ( x ) = { \frac { 1 } { \pi } } { \frac { 1 } { 1 + x ^ { 2 } } } .
$$

then

$$
\int _ { - \infty } ^ { \infty } e ^ { - 2 \pi | \xi | } e ^ { 2 \pi i x \xi } d \xi = P ( x )
$$

and hence that

$$
{ \widehat { P } } ( \xi ) = e ^ { - 2 \pi | \xi | } .
$$

Be careful to fully justify your answer.

Remark: In Questions $\mathit { 4 0 }$ and 5 above D is for Dirichlet, F is for Fej´er, P is for Poisson, and G is for Gauss-Weierstrass.
The respective “approximate identities”, namely $\{ ( \widehat { D } ) _ { t } \} _ { t > 0 } , \ \{ ( \widehat { F } ) _ { t } \} _ { t > 0 } , \ \{ P _ { t } \} _ { t > 0 } ,$ and $\{ G _ { \sqrt { t } } \} _ { t > 0 } .$ , are generally referred to as Dirichlet, Fej´er, Poisson, and Gauss-Weierstrass kernels.

6. Show that for any $\varepsilon > 0$ the function $F ( \xi ) = ( 1 + | \xi | ^ { 2 } ) ^ { - \varepsilon }$ is the Fourier transform of an $L ^ { 1 } ( \mathbb { R } ^ { n } )$ function.
   Hint: Consider the function

$$
f ( x ) = \int _ { 0 } ^ { \infty } G _ { t } ( x ) e ^ { - \pi t ^ { 2 } } t ^ { 2 \varepsilon - 1 } d t ,
$$

where $G _ { t } ( x ) = t ^ { - n } e ^ { - \pi | x | ^ { 2 } / t ^ { 2 } }$ . Now use Fubini/Tonelli to prove that $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ with ${ \widehat { f } } ( \xi ) = F ( \xi ) \| f \| _ { 1 }$

## Extra Challenge Problems

Not to be handed in with the assignment

1. By considering the iterated integral

$$
\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { \infty } x e ^ { - x ^ { 2 } ( 1 + y ^ { 2 } ) } d x \right) d y
$$

show (with justification) that

$$
\int _ { 0 } ^ { \infty } e ^ { - x ^ { 2 } } d x = { \frac { \sqrt { \pi } } { 2 } }
$$

and hence that

$$
\int _ { - \infty } ^ { \infty } e ^ { - \pi x ^ { 2 } } d x = 1 .
$$
