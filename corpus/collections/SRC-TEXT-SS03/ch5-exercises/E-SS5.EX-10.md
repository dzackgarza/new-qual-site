---
schema: qual/card@1
id: E-SS5.EX-10
kind: problem
title: "SS 5.10: Hadamard products of e^z - 1 and cos pi-z"
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

::: {.exercise}
10. Find the Hadamard products for:

(a) $e ^ { z } - 1$

(b) cos πz.

[Hint: The answers are $\scriptstyle e ^ { z / 2 } z \prod _ { n = 1 } ^ { \infty } ( 1 + z ^ { 2 } / 4 n ^ { 2 } \pi ^ { 2 } )$ and $\scriptstyle \prod _ { n = 0 } ^ { \infty } ( 1 - 4 z ^ { 2 } / ( 2 n + 1 ) ^ { 2 } )$ , respectively.]
:::

::: {.solution}
We use the canonical product
\[
\frac{\sin \pi w}{\pi w}
=\prod_{n=1}^{\infty}\left(1-\frac{w^2}{n^2}\right).
\tag{1}
\]

For (a), put $w=z/(2\pi i)$ in (1). Since
\[
\sin\!\left(\frac z{2i}\right)=-i\sinh\frac z2,
\]
we obtain
\[
\frac{\sinh(z/2)}{z/2}
=\prod_{n=1}^{\infty}
\left(1+\frac{z^2}{4\pi^2n^2}\right).
\]
Using
\[
e^z-1=2e^{z/2}\sinh(z/2),
\]
we get
\[
\boxed{
e^z-1
=e^{z/2}z\prod_{n=1}^{\infty}
\left(1+\frac{z^2}{4\pi^2n^2}\right)}.
\]

For (b), use
\[
\cos\pi z=\frac{\sin 2\pi z}{2\sin\pi z}.
\]
Applying (1) to numerator and denominator gives
\[
\cos\pi z
=\frac{2\pi z\prod_{n\ge1}(1-4z^2/n^2)}
{2\pi z\prod_{n\ge1}(1-z^2/n^2)}.
\]
The factors indexed by even $n$ in the numerator cancel the denominator factors, leaving exactly the odd indices:
\[
\boxed{
\cos\pi z
=\prod_{n=0}^{\infty}
\left(1-\frac{4z^2}{(2n+1)^2}\right)}.
\]
These are the required Hadamard products.
:::
