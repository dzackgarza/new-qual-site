---
schema: qual/card@1
id: P-PRACT20-W3-25
kind: problem
title: The integrals $\int_0^{\pi/2}(a\cos^2x+b\sin^2x)^{-n}\,dx$ by differentiating in parameters
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
For $a , b > 0$ and $n \in \mathbb { N }$ , define

$$
I _ { n } ( a , b ) = \int _ { 0 } ^ { \pi / 2 } \frac { d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n } } .
$$

Show that

$$
\frac { \partial I _ { n } } { \partial a } + \frac { \partial I _ { n } } { \partial b } + n I _ { n + 1 } = 0 .
$$

Evaluate $I _ { 1 } ( a , b )$ explicitly and use this to evaluate $I _ { 2 } ( a , b )$
:::

::: {.solution}
Differentiating under the integral (legal by Leibniz rule), we find

$$
\frac { \partial I _ { n } } { \partial a } ( a , b ) = - \int _ { 0 } ^ { \pi / 2 } \frac { n \cos ^ { 2 } ( x ) d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } } , \quad \frac { \partial I _ { n } } { \partial b } ( a , b ) = - \int _ { 0 } ^ { \pi / 2 } \frac { n \sin ^ { 2 } ( x ) d x } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } }
$$

and so

$$
\frac { \partial I _ { n } } { \partial a } + \frac { \partial I _ { n } } { \partial b } = - n \int _ { 0 } ^ { \pi / 2 } \frac { \cos ^ { 2 } ( x ) + \sin ^ { 2 } ( x ) } { ( a \cos ^ { 2 } ( x ) + b \sin ^ { 2 } ( x ) ) ^ { n + 1 } } d x = - n I _ { n + 1 } .
$$

To evaluate $I_1(a,b)$, divide numerator and denominator by $\cos^2(x)$ and substitute $u = \tan(x)$:

$$
\begin{aligned}
I_1(a,b) &= \int_0^{\pi/2} \frac{dx}{a\cos^2(x) + b\sin^2(x)}
= \int_0^{\pi/2} \frac{\sec^2(x)\,dx}{a + b\tan^2(x)}
= \int_0^\infty \frac{du}{a + bu^2} \\
&= \frac{1}{a}\int_0^\infty \frac{du}{1 + \frac{b}{a}u^2}
= \frac{1}{a}\sqrt{\frac{a}{b}}\,\arctan\left(u\sqrt{\frac{b}{a}}\right)\Big|_{u=0}^{u\to\infty}
= \frac{\pi}{2\sqrt{ab}}.
\end{aligned}
$$

Then

$$
I _ { 2 } ( a , b ) = - \frac { \partial I _ { 1 } } { \partial a } ( a , b ) - \frac { \partial I _ { 1 } } { \partial b } ( a , b ) = \frac { \pi } { 4 a \sqrt { a b } } + \frac { \pi } { 4 b \sqrt { a b } } = \frac { \pi } { 4 \sqrt { a b } } \left( \frac { 1 } { a } + \frac { 1 } { b } \right) .
$$
:::
