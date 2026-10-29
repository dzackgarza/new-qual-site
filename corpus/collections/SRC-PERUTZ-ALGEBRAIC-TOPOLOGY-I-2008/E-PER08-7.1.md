---
schema: qual/card@1
id: E-PER08-7.1
kind: problem
title: Homology splits over path components
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retyped the mathematics against Exercise 7.1 of the Perutz 2008 notes.
---

::: {.problem}
Show that, in general, $H_n(X)=\bigoplus_{Y\in\pi_0(X)}H_n(Y)$, where $\pi_0(X)$ is the set of path-components of $X$.
Thus $H_0(X)\cong\ZZ^{\pi_0(X)}$.
:::

::: {.solution}
Write $S_*(X)$ for the singular chain complex.
When $\pi_0(X)$ is infinite, $\ZZ^{\pi_0(X)}$ must be read as the direct sum $\bigoplus_{\pi_0(X)} \ZZ$, the free abelian group on $\pi_0(X)$, not the product.

::: pf

::: {.pf-step #split}
$S_*(X) = \bigoplus_{Y \in \pi_0(X)} S_*(Y)$ as chain complexes.

::: pf-proof
A singular simplex $\Delta^n \to X$ has path-connected image, so its image lies in a unique path component $Y$.
So each $S_n(X)$ is the direct sum of the $S_n(Y)$.
Each face of a simplex in $Y$ is again in $Y$, so the boundary map preserves each summand.
:::

:::

::: {.pf-step #sum}
$H_n(X) \cong \bigoplus_{Y \in \pi_0(X)} H_n(Y)$.

::: pf-proof
By step [](#split){.pf-ref}, the boundary maps are direct sums.
The kernel and the image of a direct sum of maps are the direct sums of the kernels and images, so homology commutes with direct sums of chain complexes.
:::

:::

::: {.pf-step #h0-connected}
If $Y$ is path-connected and nonempty, $H_0(Y) \cong \ZZ$.

::: pf-proof
The augmentation $\varepsilon\colon S_0(Y) \to \ZZ$, $\sum n_i y_i \mapsto \sum n_i$, is surjective and vanishes on boundaries, since $\partial\sigma = \sigma(1) - \sigma(0)$ for a path $\sigma$.
If $\varepsilon(c) = 0$ and $y_0 \in Y$, then $c = \sum n_i (y_i - y_0)$, and each $y_i - y_0$ is the boundary of a path from $y_0$ to $y_i$.
So $\ker \varepsilon$ is the group of boundaries, and $H_0(Y) \cong \ZZ$.
:::

:::

::: pf-step
$H_0(X) \cong \bigoplus_{Y \in \pi_0(X)} \ZZ$.

::: pf-proof
This is step [](#sum){.pf-ref} in degree $0$ together with step [](#h0-connected){.pf-ref}.
:::

:::

:::
:::
