---
schema: qual/card@1
id: P-BKS07-8B
kind: problem
title: UC Berkeley Spring 2007 prelim 8B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let A be the set of $z \in \mathbb { C }$ such that $| z | \le 1$ , Im $( z ) \geq 0$ , and $z \not \in \{ 1 , - 1 \}$ . Find an explicit continuous function $u \colon A \to \mathbb { R }$ such that

• u is harmonic on the interior of A,

$u ( z ) = 3$ for z ∈ A ∩ R

• u(z) = 7 for z in the intersection of A with the unit circle.
:::

::: {.solution}
We use a conformal transformation to reduce to a problem on a different region.
The transformation $w = f ( z )$ where $f ( z ) : = ( 1 + z ) / ( 1 - z )$ maps the interval $( - 1 , 1 )$ to $( 0 , \infty )$ and maps the upper half of the unit circle to the ray from $f ( - 1 ) = 0 { \mathrm { ~ t o ~ } } f ( 1 ) = \infty$ passing through $f ( i ) = i$ It therefore maps A to the first quadrant or its complement (ignoring boundaries); that it is the former can be determined by calculating $f ( i / 2 )$ , or by observing the orientation of the image of the path from −1 to 1.

Let $Q = f ( A )$ , so Q is the closed first quadrant minus the origin.
The function Im log w (where we use the standard branch of log) is a continuous function on $Q _ { i }$ , harmonic on the interior, whose values along the positive real and imaginary axes are 0 and $\pi / 2$ , respectively, so $\textstyle 3 + { \frac { 8 } { \pi } }$ Im log w is harmonic on the interior of Q and has the values 3 and 7 along those axes.
Substituting $w = f ( z )$ , we find that

$$
u = 3 + { \frac { 8 } { \pi } } \operatorname { I m } \log \left( { \frac { 1 + z } { 1 - z } } \right)
$$

is a solution.
:::
