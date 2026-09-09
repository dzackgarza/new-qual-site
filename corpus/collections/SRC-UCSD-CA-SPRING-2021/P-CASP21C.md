---
schema: qual/card@1
id: P-CASP21C
kind: problem
title: "Maximum |f'(0)| for holomorphic functions omitting negative reals with f(0)=1"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Extremal Problems
relations: []
review: draft
---

::: problem
Let $\mathcal{F}$ denote the family of holomorphic functions $f : \Delta \to \mathbb{C}$ such that (i) $f$ omits all strictly negative real numbers, and (ii) $f(0) = 1$.
Find the maximum value of $|f'(0)|$ as $f \in \mathcal{F}$.
:::

::: solution
Let
\[
\Omega=\mathbb C\setminus(-\infty,0].
\]
Every $f\in\mathcal F$ takes values in $\Omega$. Let $s$ be the principal
square root on $\Omega$, so $s(1)=1$ and $s(\Omega)$ is the right half-plane.
Then
\[
g(z)=\frac{s(f(z))-1}{s(f(z))+1}
\]
maps $\mathbb D$ holomorphically into itself and satisfies $g(0)=0$.
Schwarz's lemma gives $|g'(0)|\le1$. Since
\[
g'(0)=\frac{f'(0)}4,
\]
we obtain
\[
|f'(0)|\le4.
\]

The bound is attained: for any $\theta\in\mathbb R$,
\[
f_\theta(z)=
\left(\frac{1+e^{i\theta}z}{1-e^{i\theta}z}\right)^2
\]
belongs to $\mathcal F$, satisfies $f_\theta(0)=1$, and has
$|f_\theta'(0)|=4$. Hence
\[
\boxed{\max_{f\in\mathcal F}|f'(0)|=4.}
\]
:::
