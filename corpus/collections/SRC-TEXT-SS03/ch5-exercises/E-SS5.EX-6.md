---
schema: qual/card@1
id: E-SS5.EX-6
kind: problem
title: "SS 5.6: Wallis's product formula"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
6. Prove Wallis’s product formula

$$
{\frac {\pi}{2}} = {\frac {2 \cdot 2}{1 \cdot 3}} \cdot {\frac {4 \cdot 4}{3 \cdot 5}} \dots {\frac {2 m \cdot 2 m}{(2 m - 1) \cdot (2 m + 1)}} \dots .
$$

[Hint: Use the product formula for sin z at $z = \pi / 2 . ]$
:::

::: solution
The product formula for the sine function is
\[
\frac{\sin z}{z}=\prod_{n=1}^{\infty}\left(1-\frac{z^2}{\pi^2n^2}\right).
\]
Set $z=\pi/2$. Since $\sin(\pi/2)=1$,
\[
\frac{2}{\pi}
=\prod_{n=1}^{\infty}\left(1-\frac1{4n^2}\right)
=\prod_{n=1}^{\infty}
\frac{(2n-1)(2n+1)}{(2n)^2}.
\]
Taking reciprocals gives
\[
\boxed{
\frac{\pi}{2}
=\prod_{n=1}^{\infty}
\frac{(2n)^2}{(2n-1)(2n+1)}}.
\]
This is Wallis's product formula.
:::
