---
schema: qual/card@1
id: P-TOPS20F
kind: problem
title: "Every self-map of RP^{2n} has a fixed point"
classification:
  areas:
  - topology
  topics:
  - Fixed Point Theory
  - Projective Spaces
  - Cohomology
relations: []
review: draft
---

::: problem
Consider a continuous map $f : \mathbb{RP}^n \to \mathbb{RP}^n$, where $n$ is a positive even number.
Show that $f$ has a fixed point.
:::

::: {.solution}
<1>1. For even $n>0$, the rational homology of $\mathbb{RP}^n$ is
$$H_0(\mathbb{RP}^n;\mathbb Q)\cong\mathbb Q,$$
with all positive-degree rational homology groups zero.
::: {.proof}
Integral homology in positive degrees is $2$-torsion in the odd degrees below $n$, and the top integral homology vanishes because even-dimensional real projective space is nonorientable. Tensoring with $\mathbb Q$ kills the torsion.
:::

<1>2. Hence every self-map $f:\mathbb{RP}^n\to\mathbb{RP}^n$ has Lefschetz number
$$L(f)=1.$$
::: {.proof}
Only $H_0(-;\mathbb Q)$ contributes to the Lefschetz trace, and any self-map of a connected space induces the identity there.
:::

<1>3. Therefore $f$ has a fixed point.
::: {.proof}
Real projective space is a compact triangulable space, so the Lefschetz fixed-point theorem applies. Since $L(f)=1\ne0$, a fixed point must exist.
:::
:::
