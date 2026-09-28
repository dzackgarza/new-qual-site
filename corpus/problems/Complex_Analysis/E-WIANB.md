---
schema: qual/card@1
id: E-WIANB
kind: problem
title: Bounded holomorphic functions form a Banach space
classification:
  areas:
  - complex-analysis
  topics:
  - Function Spaces
  - Uniform Convergence
  - Morera
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
For $\Omega\subseteq\CC$, show that $A(\CC)\definedas \theset{f: \Omega \to \CC \st f\text{ is holomorphic, bounded}}$ is a Banach space.

> Hint: Apply Morera's Theorem and Cauchy's Theorem
:::

::: {.solution}
Interpreting the displayed space as
\[
A(\Omega)=\{f:\Omega\to\mathbb C:f\text{ is holomorphic and bounded}\}
\]
with the supremum norm $\|f\|_\infty=\sup_{z\in\Omega}|f(z)|$, let
$(f_n)$ be Cauchy in $\|\cdot\|_\infty$. Then for every $z\in\Omega$ the
sequence $(f_n(z))$ is Cauchy in $\mathbb C$, so define
\[
f(z)=\lim_{n\to\infty}f_n(z).
\]
The Cauchy property in supremum norm shows that $f_n\to f$ uniformly on all of
$\Omega$: given $\varepsilon>0$, choose $N$ such that
$\|f_n-f_m\|_\infty<\varepsilon$ for $m,n\ge N$ and let $m\to\infty$.

The limit $f$ is bounded, since for fixed $N$,
\[
\|f\|_\infty\le \|f-f_N\|_\infty+\|f_N\|_\infty<\infty.
\]
It is holomorphic because uniform convergence on $\Omega$ implies uniform
convergence on every compact subset, and locally uniform limits of holomorphic
functions are holomorphic (equivalently, apply Morera's theorem on triangles
compactly contained in $\Omega$). Hence $f\in A(\Omega)$ and
$\|f_n-f\|_\infty\to0$. Therefore $A(\Omega)$ is complete.
:::
