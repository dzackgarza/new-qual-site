---
schema: qual/card@1
id: P-7Y4VS
kind: problem
title: Let $U$ be an open subset of $\mathbb{C}$. We use the notion
classification:
  areas:
  - real-analysis
  topics:
  - holomorphic-functions
  - normal-families
  - l2
relations: []
review: draft
---

::: {.problem title="?"}
Let $U$ be an open subset of $\mathbb{C}$.
We use the notion $$\|f\|_{L^2(U)} = \left(\int_U |f|^2 dxdy\right)^{1/2}.$$

- Let $f : U \to \mathbb{C}$ be a holomorphic function.
  Show that for any compact set $K \subset U$, there is a constant $C_K$, such that $$\sup_{z\in K}|f(z)| \le C_K \|f\|_{L^2(U)}.$$

- Prove that $\{f \text{ holomorphic on } U : \|f\|_{L^2(U)} \le 1\}$ is a normal family.

- Suppose $U$ is the punctured disc $D(0,1) - \{0\}$.
  If $f$ is holomorphic on $U$ and $\|f\|_{L^2(U)} < \infty$, prove that $z = 0$ is a removable singularity of $f$.
:::
