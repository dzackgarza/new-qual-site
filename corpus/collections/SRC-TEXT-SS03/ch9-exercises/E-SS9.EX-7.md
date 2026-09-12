---
schema: qual/card@1
id: E-SS9.EX-7
kind: problem
title: "SS 9.7: Evaluations of zeta at 2 and 4 from the cotangent series"
classification:
  areas:
  - complex-analysis
  topics: ['Elliptic Functions', 'Weierstrass P', 'Lattices']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
7. Setting $\tau = 1 / 2$ in the expression

$$
\sum_ {m = - \infty} ^ {\infty} \frac {1}{(m + \tau) ^ {2}} = \frac {\pi^ {2}}{\sin^ {2} (\pi \tau)},
$$

deduce that

$$
\sum_ {m \geq 1, m \text {odd}} \frac {1}{m ^ {2}} = \frac {\pi^ {2}}{8} \quad \text {and} \quad \sum_ {m \geq 1} \frac {1}{m ^ {2}} = \frac {\pi^ {2}}{6} = \zeta (2).
$$

Similarly, using $\textstyle \sum { 1 / ( m + \tau ) ^ { 4 } }$ deduce that

$$
\sum_ {m \geq 1, m \text {odd}} \frac {1}{m ^ {4}} = \frac {\pi^ {4}}{9 6} \quad \text {and} \quad \sum_ {m \geq 1} \frac {1}{m ^ {4}} = \frac {\pi^ {4}}{9 0} = \zeta (4).
$$

These results were already obtained using Fourier series in the exercises at the end of Chapters 2 and 3 in Book I.
:::

::: solution
At \(\tau=1/2\),
\[
\sum_{m\in\mathbb Z}\frac1{(m+1/2)^2}=\pi^2.
\]
Since \((m+1/2)^{-2}=4(2m+1)^{-2}\) and the positive and negative odd integers contribute equally,
\[
\pi^2=8\sum_{\substack{r\ge1\\r\text{ odd}}}\frac1{r^2},
\]
so
\[
\sum_{r\ge1,\ r\text{ odd}}r^{-2}=\frac{\pi^2}{8}.
\]
Now
\[
\zeta(2)=\sum_{r\text{ odd}}r^{-2}+\sum_{r\ge1}(2r)^{-2}
=\frac{\pi^2}{8}+\frac14\zeta(2),
\]
whence \(\zeta(2)=\pi^2/6\).

Differentiate the identity
\[
\sum_{m\in\mathbb Z}(m+\tau)^{-2}=\pi^2\csc^2(\pi\tau)
\]
twice. Since
\[
\frac{d^2}{d\tau^2}(m+\tau)^{-2}=6(m+\tau)^{-4},
\]
and, writing \(u=\pi\tau\),
\[
\frac{d^2}{d\tau^2}\bigl(\pi^2\csc^2u\bigr)
=\pi^4\bigl(4\csc^2u\cot^2u+2\csc^4u\bigr),
\]
at \(\tau=1/2\) we get
\[
6\sum_{m\in\mathbb Z}(m+1/2)^{-4}=2\pi^4.
\]
Therefore
\[
\sum_{m\in\mathbb Z}(m+1/2)^{-4}=\frac{\pi^4}{3}.
\]
Since this equals \(32\sum_{r\ge1,\ r\text{ odd}}r^{-4}\),
\[
\sum_{r\ge1,\ r\text{ odd}}r^{-4}=\frac{\pi^4}{96}.
\]
Finally
\[
\zeta(4)=\frac{\pi^4}{96}+\frac1{16}\zeta(4),
\]
so \(\zeta(4)=\pi^4/90\).
:::
