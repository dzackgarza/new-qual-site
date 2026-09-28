---
schema: qual/card@1
id: P-CAF24D
kind: problem
title: 'Entire function real on $\mathbb{R}$ and imaginary on $\operatorname{Re}z=\operatorname{Im}z$ is real on $i\mathbb{R}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire function.
Assume that

(i) $f$ takes real values on the real axis,

(ii) $f$ takes purely imaginary values on the line $\operatorname{Re} z = \operatorname{Im} z$.

Prove that $f$ takes real values on the imaginary axis.
:::

::: {.solution}
Because $f$ is entire and real-valued on $\mathbb R$, its Taylor series at
$0$ has real coefficients:
\[
f(z)=\sum_{n=0}^\infty a_n z^n,
\qquad a_n\in\mathbb R.
\]
For real $t$ the point $e^{i\pi/4}t$ lies on the line
$\operatorname{Re}z=\operatorname{Im}z$, so
\[
f(e^{i\pi/4}t)
\]
is purely imaginary. Its real part is therefore identically zero:
\[
0
=\sum_{n=0}^\infty a_n
\cos\left(\frac{n\pi}{4}\right)t^n.
\]
Hence
\[
a_n\cos\left(\frac{n\pi}{4}\right)=0
\]
for every $n$. Thus $a_n$ can be nonzero only when
\[
n\equiv2\pmod4.
\]
For such $n$, $i^n=-1$. Consequently, for real $t$,
\[
f(it)=\sum_{n\equiv2\, (4)}a_n i^n t^n
=-\sum_{n\equiv2\, (4)}a_n t^n\in\mathbb R.
\]
Therefore $f$ is real-valued on the imaginary axis.
:::
