---
schema: qual/card@1
id: P-CASP13E
kind: problem
title: "Blaschke-type condition for zeros of holomorphic functions in the upper half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $x_n$ be a sequence of distinct real numbers.
Show that there exists a function holomorphic on the upper half-plane, $f \in \operatorname{Hol}(\mathbb{C}_+)$, such that $f(i + x_n) = 0$ for all $n$ if and only if $$\sum_n \frac{1}{x_n^2 + 4} < \infty.$$
:::

::: {.solution}
The statement is false as printed. In fact the identically zero function is
already a holomorphic function vanishing at all $x_n+i$, regardless of the
series. Even if one requires $f\not\equiv0$, the claim remains false for
unrestricted holomorphic functions: for example, $x_n=\sqrt n$ gives a
discrete sequence $\sqrt n+i$ in the upper half-plane, hence a Weierstrass
product gives a nonzero entire function vanishing there, while
\[
\sum_n{1\over x_n^2+4}=\sum_n{1\over n+4}=\infty.
\]

The natural corrected theorem is obtained by requiring $f$ to be bounded and
not identically zero. Let
\[
\phi(z)={z-i\over z+i},
\qquad
w_n=\phi(x_n+i)={x_n\over x_n+2i}.
\]
Then $\phi$ maps the upper half-plane biholomorphically to $\DD$, and
\[
1-|w_n|^2={4\over x_n^2+4}.
\]
Since
\[
1-|w_n|\le1-|w_n|^2\le2(1-|w_n|),
\]
the displayed series converges exactly when the Blaschke condition
$\sum_n(1-|w_n|)<\infty$ holds.

If that condition holds, the Blaschke product with zeros $w_n$ is a bounded,
nonzero holomorphic function on $\DD$; composing it with $\phi$ gives the
required bounded function on the upper half-plane. Conversely, the zeros of
every nonzero bounded holomorphic function on $\DD$ satisfy the Blaschke
condition (by Jensen's formula), and applying this to $f\circ\phi^{-1}$ gives
the necessity. Thus the stated numerical condition is exactly correct for
bounded nonzero holomorphic functions.
:::
