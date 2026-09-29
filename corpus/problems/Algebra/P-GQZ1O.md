---
schema: qual/card@1
id: P-GQZ1O
kind: problem
title: The torsion subset of a module over an integral domain is a submodule
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $R$ be an integral domain and $M$ an $R$-module. Define
\[
T(M)=\{m\in M:rm=0\text{ for some }0\ne r\in R\}.
\]
Prove that $T(M)$ is an $R$-submodule of $M$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

One has $0\in T(M)$.

::: pf-proof

For any nonzero $r\in R$, $r0=0$.

:::

:::

::: {.pf-step #s2}

If $m,n\in T(M)$ and $c\in R$, then $cm+n\in T(M)$.

::: pf-proof

Choose nonzero annihilators $a,b\in R$ with
\[
am=0,
\qquad
bn=0.
\]
Since $R$ is a domain,
\[
ab\ne0.
\]
Then
\[
ab(cm+n)
=bc(am)+a(bn)
=0.
\]
Thus $cm+n$ is torsion.

:::

:::

::: pf-step

Therefore $T(M)\le M$.

::: pf-proof

Apply the submodule criterion using steps [](#s1){.pf-ref} and [](#s2){.pf-ref}. The domain hypothesis is used exactly to ensure that the product of two nonzero annihilators is still nonzero.

:::

:::

:::

:::
