---
schema: qual/card@1
id: P-CASP25C
kind: problem
title: "Square root of an injective holomorphic function with f(0)=0"
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Injective Functions
  - Square Roots
relations: []
review: draft
---

::: {.problem}
Let $f : \mathbb{D} \to \mathbb{C}$ be a holomorphic function in the unit disc.
Assume $f$ is injective and $f(0) = 0$.
Prove that there exists a holomorphic function $g$ in $\mathbb{D}$ such that $(g(z))^2 = f(z^2)$ for all $z \in \mathbb{D}$.
:::

::: {.solution}
Since $f$ is injective and $f(0)=0$, the zero at $0$ is simple. Thus
\[
f(w)=w h(w),
\]
where $h$ is holomorphic and nowhere zero on $\mathbb D$. Consequently
\[
f(z^2)=z^2 h(z^2).
\]

The function $h(z^2)$ is holomorphic and nowhere zero on the simply connected
disk. Hence it has a holomorphic square root: there is $q\in H(\mathbb D)$
with
\[
q(z)^2=h(z^2).
\]
Define
\[
g(z)=zq(z).
\]
Then $g$ is holomorphic on $\mathbb D$ and
\[
g(z)^2=z^2q(z)^2=z^2h(z^2)=f(z^2).
\]
:::
