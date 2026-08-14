---
schema: qual/card@1
id: P-AKPY4
kind: problem
title: "Suppose $D$ is a domain and $f, g$ are analytic on $D$. Prove that if $fg = 0$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - identity-theorem
  - zeros
relations: []
review: draft
---

::: {.problem title="?"}
Suppose $D$ is a domain and $f, g$ are analytic on $D$.

Prove that if $fg = 0$ on $D$, then either $f \equiv 0$ or $g\equiv 0$ on $D$.
:::

::: {.solution}
Suppose $fg=0$ on $D$ but $f\not\equiv 0$, we'll show $g\equiv 0$ on $D$.
Since $f\not \equiv 0$, $f(z_0)\neq 0$ at some point $z_0$.
Since $f$ is holomorphic, in particular $f$ is continuous, so there is a neighborhood $U\ni z_0$ where $f(z)\neq 0$ for any $z\in U$.
But $f(z)g(z) = 0$ for all $z\in U$, and since $\CC$ is an integral domain, this forces $g(z) = 0$ for every $z\in U$.
So $g\equiv 0$ on $U$.
Now $U$ is a set with a limit point, so by the identity principle, $g\equiv 0$ on $D$.
:::
