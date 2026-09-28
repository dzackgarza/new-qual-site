---
schema: qual/card@1
id: E-SS3.EX-1
kind: problem
title: "SS 3.1: Zeros of sin pi-z and residues of its reciprocal"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
1. Using Euler’s formula

$$
\sin \pi z = \frac {e ^ {i \pi z} - e ^ {- i \pi z}}{2 i},
$$

show that the complex zeros of sin πz are exactly at the integers, and that they are each of order 1.

Calculate the residue of 1/ sin πz at $z = n \in \mathbb { Z }$
:::

::: {.solution}
By Euler's formula,
\[
\sin \pi z=0
\iff e^{i\pi z}=e^{-i\pi z}
\iff e^{2\pi i z}=1.
\]
Write $z=x+iy$. Then
\[
e^{2\pi i z}=e^{2\pi i x}e^{-2\pi y}.
\]
If this equals $1$, its modulus is $1$, so $e^{-2\pi y}=1$ and hence $y=0$. Then $e^{2\pi i x}=1$, so $x\in\mathbb Z$. Thus the zeros are exactly the integers.

At $z=n\in\mathbb Z$,
\[
\frac{d}{dz}\sin\pi z=\pi\cos\pi z=\pi(-1)^n\ne0,
\]
so each zero is simple.

For a holomorphic function $g$ with a simple zero at $n$, the residue of $1/g$ at $n$ is $1/g'(n)$. Therefore
\[
\operatorname{Res}_{z=n}\frac1{\sin\pi z}
=\frac1{\pi\cos\pi n}
=\frac{(-1)^n}{\pi}.
\]
:::
