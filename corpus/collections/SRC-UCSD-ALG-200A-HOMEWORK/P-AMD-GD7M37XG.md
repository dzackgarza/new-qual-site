---
schema: qual/card@1
id: P-AMD-GD7M37XG
kind: problem
title: Normality of Sylow subgroups in an intermediate subgroup chain
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 2(a).
    Restored the source hypotheses P normal H and H normal K; the prior
    shorthand could be read as already assuming P normal K.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Since P is Sylow in G and P≤H, it is Sylow in H. Normality in H makes it
    the unique Sylow p-subgroup of H, hence characteristic in H. Characteristic
    in H together with H normal K gives P normal K.
---

::: {.problem}
Let $G$ be finite and suppose
\[
P\le H\le K\le G,
\qquad
P\in\operatorname{Syl}_p(G).
\]

Assume
\[
P\normal H
\qquad\text{and}\qquad
H\normal K.
\]
Prove that $P\normal K$.
:::

::: {.solution}
<1>1. The subgroup $P$ is a Sylow $p$-subgroup of $H$.
::: {.proof}
The subgroup $P$ is a $p$-subgroup of $H$ because $P\le H$.

Let $Q\le H$ be any $p$-subgroup.
Then $Q$ is also a $p$-subgroup of $G$.
Since $P$ is Sylow in $G$,
\[
|Q|\le|P|.
\]
Thus no $p$-subgroup of $H$ has order larger than $P$, so
\[
P\in\operatorname{Syl}_p(H).
\]
:::

<1>2. The subgroup $P$ is the unique Sylow $p$-subgroup of $H$.
::: {.proof}
By <1>1, $P$ is Sylow in $H$.
By hypothesis,
\[
P\normal H.
\]
All Sylow $p$-subgroups of $H$ are conjugate in $H$, while normality makes every $H$-conjugate of $P$ equal to $P$.
Hence every Sylow $p$-subgroup of $H$ is $P$.
:::

<1>3. The subgroup $P$ is characteristic in $H$.
::: {.proof}
Every automorphism of $H$ preserves subgroup order and therefore sends a Sylow $p$-subgroup to a Sylow $p$-subgroup.
By uniqueness from <1>2, any $\varphi\in\operatorname{Aut}(H)$ satisfies
\[
\varphi(P)=P.
\]
Thus $P\operatorname{char}H$.
:::

<1>4. Therefore $P\normal K$.
::: {.proof}
By <1>3,
\[
P\operatorname{char}H,
\]
and by hypothesis
\[
H\normal K.
\]
A characteristic subgroup of a normal subgroup is normal in the ambient group.
Therefore
\[
P\normal K.
\]
:::
:::
