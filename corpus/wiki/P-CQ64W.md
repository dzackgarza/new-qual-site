---
schema: qual/card@1
id: P-CQ64W
kind: problem
title: Universal cover of $(S^1\times S^1)\vee S^2$ and $\pi_2$
classification:
  areas:
  - topology
  topics:
  - covering-spaces
  - homotopy
  - homology
relations: []
review: draft
solved: true
---
Describe the universal cover of $X = (S^1 \cross S^1) \vee S^2$ and compute $\pi_2(X)$.

:::{.solution}

\envlist
:::{.concept}
\envlist

- $\pi_{\geq 2}(\univcover{X} ) \cong \pi_{\geq 2}(X)$ for $\univcover{X}$ the universal cover of $X$
- Structure of the universal cover of a wedges
- $\univcover{T^2} = \RR^2$ and $\univcover{S^2} = S^2$
- By Mayer-Vietoris, $H_n(\wedgeprod X_i) = \bigoplus H_n(X_i)$.
:::

The universal cover can be identified as
\[
\univcover{X} = \RR^2 \wedgeprod_{i, j \in \ZZ^2} S^2
,\]
i.e. the plane with a sphere wedged onto every integer lattice point.
We can then check
\[
\pi_1(X) 
&\cong \pi_1(\univcover{X} ) \\
&= \pi_1( \RR^2 \wedgeprod_{i, j \in \ZZ^2} S^2 ) \\
&= \pi_1( \RR^2 \wedgeprod_{i, j \in \ZZ^2} S^2 ) \\
&= \prod_{i,j \in \ZZ^2} \pi_1(\RR^2) \cross \pi_1(S^2) \\
&= 0
,\]
using that $\pi_1(S^2) = 0$.
Then by Hurewicz, $\pi_2(X) \cong H_2(X)$, so we can compute
\[
H_2(X) 
&= H_2( \RR^2 \wedgeprod_{i, j \in \ZZ^2} S^2 ) \\
&= \bigoplus_{i,j \in \ZZ^2} H_2(\RR^2) \oplus H_2(S^2) \\
&= \bigoplus_{i,j \in \ZZ^2} \ZZ
.\]

:::
