---
schema: qual/card@1
id: E-XQX6X
kind: problem
title: Liouville's theorem from the Schwarz lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Schwarz Lemma
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Use a version of the Schwarz lemma to prove Liouville's theorem.
:::

::: {.solution}
Let $f$ be entire with $\abs{f}\le M$, and put $g(z)\coloneqq f(z)-f(0)$, so $g(0)=0$ and $\abs{g}\le 2M$.

::: pf

::: {.pf-step #schwarz-R}
For every $R>0$ and $\abs{z}<R$, $\abs{g(z)}\le \dfrac{2M}{R}\abs{z}$.

::: pf-proof
Put $h(w)\coloneqq \frac{1}{2M}g(Rw)$, which is holomorphic on $\DD$ with $\abs h\le 1$ and $h(0)=0$.
If $h$ is constant, then $h\equiv h(0)=0$ and the bound holds.
Otherwise $\abs h<1$ on $\DD$ by the maximum modulus principle, so $h$ maps $\DD$ into $\DD$, and the Schwarz lemma gives $\abs{h(w)}\le\abs w$.
Substituting $z = Rw$ gives the claim.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
Fix $z\in\CC$.
By step [](#schwarz-R){.pf-ref}, $\abs{g(z)}\le 2M\abs{z}/R$ for every $R>\abs{z}$, and letting $R\to\infty$ gives $g(z)=0$.
So $f(z) = f(0)$ for all $z$.
:::

:::

:::

:::
