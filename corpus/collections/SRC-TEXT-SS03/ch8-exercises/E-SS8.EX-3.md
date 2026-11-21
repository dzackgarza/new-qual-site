---
schema: qual/card@1
id: E-SS8.EX-3
kind: problem
title: Simple connectedness is a conformal invariant
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured both parts into numbered steps: that a conformal equivalence is a homeomorphism
    (holomorphic and inverse holomorphic, hence both continuous), the transport of a null-homotopy
    across a homeomorphism, and the second part resting on invariance of domain for a continuous
    injective map between open subsets of R^2. Supplied the small point the prose compressed: the
    composite of the homotopy with the homeomorphism is again a homotopy with the constant curve as
    endpoint, and it starts at the given curve. Not checked this session: the printed statement page.

---

::: {.exercise}
Suppose $U$ and $V$ are conformally equivalent. Prove that if $U$ is simply connected, then so is $V$. Note that this conclusion remains valid if we merely assume that there exists a continuous bijection between $U$ and $V$.
:::

::: {.solution}

The argument is the card's own; the statement is the exercise stored on the card, and no source text or solution set is retained for it.

A domain is an open connected subset of $\CC$; it is simply connected when every closed curve in it is null-homotopic, that is, homotopic through curves with fixed endpoints to a constant curve.

::: pf

::: {.pf-step #conformal}
A conformal equivalence $\Phi\colon U\to V$ is a homeomorphism.

::: pf-proof
By definition $\Phi$ is a bijection, $\Phi$ is holomorphic on $U$ and $\Phi^{-1}$ is holomorphic on $V$; a holomorphic function is continuous, so both $\Phi$ and $\Phi^{-1}$ are continuous. A continuous bijection with continuous inverse is a homeomorphism.
:::

:::

::: {.pf-step #transport}
If $\Phi\colon U\to V$ is a homeomorphism and $U$ is simply connected, then $V$ is simply connected.

::: pf-proof
Let $\gamma\colon[0,1]\to V$ be a closed curve. Then $\Phi^{-1}\circ\gamma$ is a closed curve in $U$, being a composite of continuous maps with $(\Phi^{-1}\gamma)(0)=\Phi^{-1}(\gamma(0))=\Phi^{-1}(\gamma(1))$. Since $U$ is simply connected there is a homotopy $H\colon[0,1]^{2}\to U$ with $H(s,0)=(\Phi^{-1}\gamma)(s)$ and $H(s,1)=c$ constant, and $H(0,t)=H(1,t)$ for all $t$. Then $\Phi\circ H$ is a homotopy in $V$ from $\Phi\circ\Phi^{-1}\circ\gamma=\gamma$ to the constant curve $\Phi(c)$, and it too is a homotopy of closed curves. So every closed curve in $V$ is null-homotopic.
:::

:::

::: {.pf-step #bijection}
If $\Phi\colon U\to V$ is a continuous bijection between open subsets of $\CC$, then $\Phi$ is a homeomorphism.

::: pf-proof
Invariance of domain states that a continuous injective map from an open subset of $\RR^{2}$ into $\RR^{2}$ is an open map onto its image; identifying $\CC$ with $\RR^{2}$, the injective continuous $\Phi$ maps the open set $U$ onto the open set $V=\Phi(U)$ and carries open subsets of $U$ to open subsets of $V$. Hence $\Phi$ is open, and a continuous bijection that is open has continuous inverse.
:::

:::

::: {.pf-step}
If $U$ is simply connected and $U$, $V$ are conformally equivalent, then $V$ is simply connected; the conclusion holds as well when $\Phi$ is merely a continuous bijection.

::: pf-proof
For a conformal equivalence, steps [](#conformal){.pf-ref} and [](#transport){.pf-ref} give the conclusion. Under the weaker hypothesis, step [](#bijection){.pf-ref} upgrades $\Phi$ to a homeomorphism and step [](#transport){.pf-ref} applies again.
:::

:::

:::

:::
