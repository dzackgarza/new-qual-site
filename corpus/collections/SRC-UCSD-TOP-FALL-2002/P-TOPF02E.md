---
schema: qual/card@1
id: P-TOPF02E
kind: problem
title: "Every continuous self-map of RP^{2n} has a fixed point"
classification:
  areas:
  - topology
  topics:
  - Fixed Point Theory
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Prove that any continuous map $f : \mathbb{RP}^{2n} \to \mathbb{RP}^{2n}$ has a fixed point, if $n \geq 1$.
:::

::: {.solution}

::: pf

::: {.pf-step #rational-homology}
With rational coefficients,
$$
H_k(\mathbb{RP}^{2n};\mathbb Q)=
\begin{cases}
\mathbb Q,&k=0,\\
0,&k>0.
\end{cases}
$$

::: pf-proof
The positive-dimensional integral homology of even-dimensional real projective space is torsion, so it vanishes after tensoring with $\mathbb Q$; the space is connected, giving $H_0\cong\mathbb Q$.
:::

:::

::: pf-step
For any continuous self-map $f:\mathbb{RP}^{2n}\to\mathbb{RP}^{2n}$, the Lefschetz number is
$$
L(f)=1.
$$

::: pf-proof
By step [](#rational-homology){.pf-ref}, the only nonzero rational homology group is $H_0$, and any self-map of a connected space induces the identity on $H_0$. Therefore
$$
L(f)=\sum_k(-1)^k\operatorname{tr}(f_*|H_k(-;\mathbb Q))=1.
$$
:::

:::

::: pf-step
Hence $f$ has a fixed point.

::: pf-proof
The Lefschetz fixed-point theorem states that a self-map of a finite CW complex with nonzero Lefschetz number has a fixed point. Since $\mathbb{RP}^{2n}$ is a finite CW complex and $L(f)=1\ne0$, the conclusion follows.
:::

:::

:::

:::

