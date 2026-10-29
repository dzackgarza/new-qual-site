---
schema: qual/card@1
id: P-MAXAT-6-06
kind: problem
title: Even-dimensional real projective spaces do not bound
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 6 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints RP^{2k+1}, which bounds (quotient of RP^{2k+1} x [-1,1] by the free involution induced by z -> iz). The statement now reads RP^{2k}.
---

::: {.problem}
Show that $\RP^{2k}$ cannot be a boundary.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
If a closed manifold $M$ is the boundary of a compact manifold, then $\chi(M)$ is even.

::: pf-proof
Suppose $M=\partial W$ with $\dim W=m$, and work with coefficients in $\FF_2$, so orientability is irrelevant.
Poincaré--Lefschetz duality gives
$$
H_i(W,M;\FF_2)\cong H^{m-i}(W;\FF_2),
$$
so $\chi(W,M)=(-1)^m\chi(W)$.
The long exact sequence of the pair gives $\chi(W)=\chi(M)+\chi(W,M)$. Hence
$$
\chi(M)=\bigl(1-(-1)^m\bigr)\chi(W),
$$
and the coefficient $1-(-1)^m$ is $0$ or $2$.
:::

:::

::: {.pf-step #s2}
$\chi(\RP^{2k})=1$.

::: pf-proof
The standard CW structure on $\RP^{2k}$ has one cell in each dimension $0,1,\dots,2k$, so $\chi(\RP^{2k})=\sum_{j=0}^{2k}(-1)^j=1$.
:::

:::

::: pf-qed
By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\RP^{2k}$ is not the boundary of a compact manifold.
:::

:::
:::
