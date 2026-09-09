---
schema: qual/card@1
id: P-52FST
kind: problem
title: $H\operatorname{char} K\trianglelefteq G$ implies $H\trianglelefteq G$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Automorphisms
  - Subgroups
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

::: problem
- Show that if $H \leq G$, $K\normal G$ is a normal subgroup, and $H~\text{char}~K$ then $H$ is normal in  $G$.

  > So normality is not transitive, but strengthening one to "characteristic" gives a weak form of transitivity.
:::


::: {.solution}
Assume $H\operatorname{char}K$ and $K\trianglelefteq G$.

<1>1. For every $g\in G$, conjugation by $g$ restricts to an automorphism of $K$.
::: {.proof}
Because $K\trianglelefteq G$,
\[
gKg^{-1}=K.
\]
Thus the inner automorphism
\[
c_g:G\to G,\qquad x\mapsto gxg^{-1}
\]
restricts to an automorphism $c_g|_K\in\operatorname{Aut}(K)$.
:::

<1>2. Every such conjugation preserves $H$.
::: {.proof}
Since $H$ is characteristic in $K$, every automorphism of $K$ maps $H$ to itself. Applying this to $c_g|_K$ from <1>1 gives
\[
gHg^{-1}=H
\]
for every $g\in G$.
:::

<1>3. Therefore $H\trianglelefteq G$.
::: {.proof}
The equality $gHg^{-1}=H$ for all $g\in G$ is exactly the definition of normality.
:::
:::
