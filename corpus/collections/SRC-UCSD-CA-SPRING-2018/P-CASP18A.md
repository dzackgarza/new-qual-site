---
schema: qual/card@1
id: P-CASP18A
kind: problem
title: "Entire function bounded by e^{Re z} is either identically zero or never zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Minimum Principle
relations: []
review: draft
---

::: problem
Let $f$ be an analytic function on $\mathbb{C}$ that satisfies the inequality $|f(z)| \leq e^{\operatorname{Re} z}$ for all $z \in \mathbb{C}$.
Prove that either $f(z) = 0$ for all $z \in \mathbb{C}$ or $f(z) \neq 0$ for all $z \in \mathbb{C}$.
:::

::: solution
The function
\[
g(z)=e^{-z}f(z)
\]
is entire and satisfies
\[
|g(z)|=e^{-\operatorname{Re}z}|f(z)|\le1.
\]
By Liouville's theorem, $g$ is constant: $g\equiv c$. Hence
\[
f(z)=ce^z.
\]
If $c=0$, then $f\equiv0$; if $c\ne0$, then $e^z\ne0$ for every $z$, so
$f$ has no zeros.
:::
