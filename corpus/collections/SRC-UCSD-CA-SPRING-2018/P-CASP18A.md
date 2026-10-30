---
schema: qual/card@1
id: P-CASP18A
kind: problem
title: 'An entire function with $\abs f\leq e^{\Re z}$ is identically zero or never zero'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Minimum Principle
relations: []
review: draft
---

::: {.problem}
Let $f$ be an analytic function on $\CC$ that satisfies the inequality $\abs{f(z)} \leq e^{\operatorname{Re} z}$ for all $z \in \CC$.
Prove that either $f(z) = 0$ for all $z \in \CC$ or $f(z) \neq 0$ for all $z \in \CC$.
:::

::: {.solution}
The function
$$
g(z)=e^{-z}f(z)
$$
is entire and satisfies
$$
\abs{g(z)}=e^{-\operatorname{Re}z}\abs{f(z)}\le1.
$$
By Liouville's theorem, $g$ is constant: $g\equiv c$. Hence
$$
f(z)=ce^z.
$$
If $c=0$, then $f\equiv0$; if $c\ne0$, then $e^z\ne0$ for every $z$, so
$f$ has no zeros.
:::
