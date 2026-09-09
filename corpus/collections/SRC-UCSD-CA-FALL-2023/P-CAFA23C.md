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
---

::: problem
Prove that the image of a nonconstant entire function $E : \mathbb{C} \to \mathbb{C}$ is dense in $\mathbb{C}$.
:::

::: solution
Suppose the image were not dense. Then some open disk
\[
D(a,r)
\]
would be disjoint from $E(\mathbb C)$. In particular
\[
|E(z)-a|\ge r
\qquad(z\in\mathbb C).
\]
Thus
\[
F(z)=\frac1{E(z)-a}
\]
is an entire bounded function. Liouville's theorem makes $F$ constant, and
therefore $E$ constant, contrary to hypothesis. Hence the image of every
nonconstant entire function is dense in $\mathbb C$.
:::
