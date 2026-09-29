---
schema: qual/card@1
id: P-UCTOP-SU09-1
kind: problem
title: Constructing space with prescribed homology groups
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Construct a space whose integral homology groups are $\mathbb{Z}, \mathbb{Z}_5, \mathbb{Z}_5, \mathbb{Z}$ in dimensions 0, 1, 2, 3, and zero otherwise.
Does there exist a closed orientable 3-manifold with these homology groups?
:::

::: {.solution}

::: pf

::: {.pf-step #moore-spaces}
Let
$$
M_1=S^1\cup_{5}e^2,
\qquad
M_2=S^2\cup_{5}e^3,
$$
where each attaching map has degree $5$.

::: pf-proof
These are Moore spaces for $\mathbb Z/5$ in degrees $1$ and $2$. Their reduced cellular chain complexes have the single nonzero boundary map $\mathbb Z\xrightarrow{5}\mathbb Z$ in the relevant degrees, hence
$$
\widetilde H_1(M_1)\cong\mathbb Z/5,\qquad
\widetilde H_2(M_2)\cong\mathbb Z/5,
$$
with all other reduced homology zero.
:::

:::

::: pf-step
Set
$$
X=M_1\vee M_2\vee S^3.
$$
Then
$$
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,3,\\
\mathbb Z/5,&i=1,2,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof
Reduced homology of a finite wedge is the direct sum of the reduced homologies of its summands. Apply step [](#moore-spaces){.pf-ref} and $\widetilde H_3(S^3)=\mathbb Z$.
:::

:::

::: pf-step
No closed orientable $3$-manifold can have these homology groups.

::: pf-proof
Suppose $M$ were such a manifold. Poincaré duality gives
$$
H_2(M;\mathbb Z)\cong H^1(M;\mathbb Z).
$$
By the universal coefficient theorem,
$$
H^1(M;\mathbb Z)\cong\operatorname{Hom}(H_1(M),\mathbb Z)
$$
because $H_0(M)$ is free. If $H_1(M)\cong\mathbb Z/5$, this Hom group is zero. Thus $H_2(M)=0$, contradicting the required $H_2(M)\cong\mathbb Z/5$.
:::

:::

:::

:::

