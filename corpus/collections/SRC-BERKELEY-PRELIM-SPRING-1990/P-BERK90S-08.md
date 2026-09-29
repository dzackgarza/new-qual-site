---
schema: qual/card@1
id: P-BERK90S-08
kind: problem
title: The multiplicative group $\CC^*$ has no proper finite-index subgroup
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared Problem 8 with the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Used the finite quotient exponent and roots of nonzero complex numbers.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked normality, the application of Lagrange's theorem, and the root construction for every positive index.
---

::: {.problem}
Let $H$ be a finite-index subgroup of the multiplicative group $\CC^*$. Prove that
$$
H=\CC^*.
$$
:::

::: {.solution}
Put $G\coloneqq\CC^*$ and $n\coloneqq[G:H]$.

::: pf

::: {.pf-step #s1}

Every $w\in G$ satisfies $w^n\in H$.

::: pf-proof

Since $G$ is abelian, $H$ is normal. The quotient group $G/H$ has order
$n$, so [[T-SZRXI|Lagrange's theorem]] gives $(wH)^n=H$.
Thus $w^n\in H$.

:::

:::

::: {.pf-step #s2}

Every $z\in G$ belongs to $H$.

::: pf-proof

Write $z=re^{i\theta}$ with $r>0$ and $\theta\in\RR$. Since $n\geq1$,
the number $w\coloneqq r^{1/n}e^{i\theta/n}$ is nonzero and satisfies
$w^n=z$. Step [](#s1){.pf-ref} gives $z\in H$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives $G\subseteq H$, and the subgroup hypothesis gives
$H\subseteq G$. Therefore $H=G=\CC^*$.

:::

:::

:::
