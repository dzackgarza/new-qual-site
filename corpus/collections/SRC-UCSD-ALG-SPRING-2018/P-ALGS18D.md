---
schema: qual/card@1
id: P-ALGS18D
kind: problem
title: "A finitely generated projective module over a PID is free"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $A$ is a PID, and $M$ is a finitely generated $A$-module.
Prove that $M$ is projective if and only if $M$ is free.
:::

::: {.solution}
<1>1. Every free $A$-module is projective.
::: {.proof}
Let $F$ be free with basis $(e_i)_{i\in I}$, let $q:N\twoheadrightarrow P$ be a surjective $A$-linear map, and let $f:F\to P$ be $A$-linear.
For each $i$, choose $n_i\in N$ with $q(n_i)=f(e_i)$.
There is a unique $A$-linear map $\widetilde f:F\to N$ with $\widetilde f(e_i)=n_i$, and then $q\widetilde f=f$.
Thus $F$ has the lifting property for surjections.
:::

<1>2. Suppose conversely that $M$ is finitely generated and projective.
Then there is a surjection
\[
\pi:A^n\twoheadrightarrow M
\]
for some $n$.
::: {.proof}
Choose finitely many generators $m_1,\dots,m_n$ of $M$ and define $\pi(e_i)=m_i$ on the standard basis of $A^n$.
:::

<1>3. Since $M$ is projective, $\pi$ splits: there is an $A$-linear map $s:M\to A^n$ with $\pi s=\operatorname{id}_M$.
::: {.proof}
Apply projectivity of $M$ to the surjection $\pi:A^n\twoheadrightarrow M$ and the identity map $M\to M$.
:::

<1>4. The map $s$ is injective, so $M\cong s(M)$ is a submodule of the finite free module $A^n$.
::: {.proof}
If $s(m)=0$, then $m=(\pi s)(m)=0$.
:::

<1>5. Every submodule of a free module over a PID is free; hence $s(M)$, and therefore $M$, is free.
::: {.proof}
This is the standard submodule theorem for modules over a PID. For finite free ambient modules it follows by induction on the rank: project a submodule of $A^n$ to the last coordinate, use that both the kernel and image are free, and split the resulting short exact sequence because the image is free.
:::

<1>6. Therefore a finitely generated $A$-module is projective if and only if it is free.
::: {.proof}
Combine <1>1 and <1>5.
:::
:::
