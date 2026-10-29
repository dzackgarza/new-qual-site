---
schema: qual/card@1
id: P-EN5JE
kind: problem
title: "$\\abs{HK} = \\abs{H}\\abs{K}/\\abs{H \\cap K}$"
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Let $H, K \leq G$ a finite group, and without using the normalizers of $H$ or $K$, show that $\abs{HK} = \abs{H} \abs{K}/\abs{H\intersect K}$.
:::

::: {.solution}
Let $\phi:H\times K\to HK$ be the surjection $\phi(h,k)=hk$.

::: pf

::: {.pf-step #fiber}
Every fiber of $\phi$ has exactly $\abs{H\cap K}$ elements.

::: pf-proof
Fix $hk\in HK$.
If $x\in H\cap K$, then $\phi(hx,x^{-1}k)=hk$, and distinct $x$ give distinct pairs $(hx,x^{-1}k)$.
Conversely, if $h_1k_1=hk$, then $x\coloneqq h^{-1}h_1=kk_1^{-1}$ lies in $H\cap K$, and $(h_1,k_1)=(hx,x^{-1}k)$.
Thus $x\mapsto(hx,x^{-1}k)$ is a bijection from $H\cap K$ onto the fiber over $hk$.
:::

:::

::: pf-qed
Counting $H\times K$ by the fibers of $\phi$, step [](#fiber){.pf-ref} gives $\abs{H}\abs{K}=\abs{HK}\,\abs{H\cap K}$, so $\abs{HK}=\abs{H}\abs{K}/\abs{H\cap K}$.
:::

:::

:::
