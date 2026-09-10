---
schema: qual/card@1
id: P-PS4ZH
kind: problem
title: A field extension with finitely many intermediate fields is simple
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Separability
relations: []
review: draft
---

::: problem
Let $E/F$ be a field extension with only finitely many intermediate fields. Prove that $E/F$ is simple.
:::

::: {.solution}
<1>1. The extension $E/F$ is finite algebraic.
::: {.proof}
If $\alpha\in E$ were transcendental over $F$, then
\[
F(\alpha)\supsetneq F(\alpha^2)\supsetneq F(\alpha^4)\supsetneq\cdots
\]
would give infinitely many intermediate fields, contradiction. Hence $E/F$ is algebraic.

If $E/F$ were not finitely generated, start with $F_0=F$. Whenever $F_i\ne E$, choose $\alpha_i\in E\setminus F_i$ and put
\[
F_{i+1}=F_i(\alpha_i).
\]
This produces infinitely many distinct intermediate fields, again a contradiction. Therefore $E/F$ is finitely generated and algebraic, hence finite.
:::

<1>2. The finite extension is simple.
::: {.proof}
If $F$ is finite, then $E$ is a finite field, so $E^\times$ is cyclic. A generator of $E^\times$ generates $E$ as a field over $F$.

Now suppose $F$ is infinite. The proper intermediate fields are proper $F$-vector subspaces of the finite-dimensional vector space $E$. By hypothesis there are only finitely many of them, and a finite-dimensional vector space over an infinite field cannot be the union of finitely many proper subspaces. Choose
\[
\alpha\in E
\]
outside the union of all proper intermediate fields. Then $F(\alpha)$ is an intermediate field. It cannot be proper, so
\[
E=F(\alpha).
\]
:::
:::
