---
schema: qual/card@1
id: P-CAFA23C
kind: problem
title: "Image of a nonconstant entire function is dense"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each step re-read: the complement of the closure of the
      image is nonempty and open, so it contains a disc; that disc gives a positive lower bound on
      |E - a|; the reciprocal is therefore entire with |F| <= 1/r; and Liouville makes it, and
      hence E, constant. The card also records that the conclusion cannot be improved, with e^z as
      the example. Not claimed: Picard's theorems, which say more about the omitted values.
---

::: {.problem}
Prove that the image of a nonconstant entire function $E : \CC \to \CC$ is dense in $\CC$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #nondense}
If $E(\CC)$ is not dense in $\CC$ then there are $a\in\CC$ and $r>0$ with $E(\CC)\cap D(a,r)=\varnothing$.

::: pf-proof
The complement of the closure of $E(\CC)$ is a nonempty open set, and a nonempty open subset of $\CC$ contains a disc $D(a,r)$; the closed complement is exactly the set of points at positive distance from $E(\CC)$, so a disc in it misses $E(\CC)$.
:::

:::

::: {.pf-step #distance}
$\abs{E(z)-a}\ge r$ for every $z$.

::: pf-proof
If $\abs{E(z)-a}<r$ then $E(z)\in D(a,r)$, contradicting step [](#nondense){.pf-ref}.
:::

:::

::: {.pf-step #bounded}
$F(z)=\dfrac{1}{E(z)-a}$ is entire and $\abs{F(z)}\le\dfrac1r$.

::: pf-proof
The denominator never vanishes by step [](#distance){.pf-ref}, so $F$ is holomorphic on $\CC$; and $\abs{F(z)}=1/\abs{E(z)-a}\le1/r$.
:::

:::

::: {.pf-step #liouville}
$F$ is constant, hence $E$ is constant.

::: pf-proof
Liouville's theorem makes a bounded entire function constant. If $F=c\ne0$ then $E=a+1/c$ is constant, contradicting the hypothesis that $E$ is nonconstant.
:::

:::

::: {.pf-step}
The image of a nonconstant entire function is dense.

::: pf-proof
The assumption that the image is not dense leads to the contradiction of step [](#liouville){.pf-ref}, so $\overline{E(\CC)}=\CC$:
$$
\boxed{E\text{ entire, nonconstant}\implies\overline{E(\CC)}=\CC.}
$$
The conclusion is sharp: $E(z)=e^{z}$ has image $\CC\setminus\{0\}$, which is dense but not all of $\CC$, so density is the most that can be asserted.
:::

:::

:::
:::
