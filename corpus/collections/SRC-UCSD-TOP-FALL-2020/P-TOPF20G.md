---
schema: qual/card@1
id: P-TOPF20G
kind: problem
title: "The swap map on M x M has a fixed point when chi(M) is nonzero"
classification:
  areas:
  - topology
  topics:
  - Fixed Point Theory
  - Euler Characteristic
  - Manifolds
  - Lefschetz Fixed Point Theorem
relations: []
review: draft
---

::: problem
Let $M$ be a closed, orientable $n$-dimensional manifold with nonzero Euler characteristic.
Consider the map $f : M \times M \to M \times M$ defined by $f(x, y) = (y, x)$ for any $x, y \in M$.
Show that any map $g : M \times M \to M \times M$ that is homotopic to $f$ has a fixed point.
:::

::: {.solution}
<1>1. The Lefschetz number of the swap $f(x,y)=(y,x)$ is $\chi(M)$.
::: {.proof}
Over $\mathbb Q$, Künneth identifies
$$H_k(M\times M)=\bigoplus_{p+q=k}H_p(M)\otimes H_q(M).$$
The swap sends $x\otimes y$ to $(-1)^{pq}y\otimes x$. Summands with $p\ne q$ occur in exchanged pairs and contribute zero trace. On $H_p(M)\otimes H_p(M)$, the graded swap has trace $(-1)^p\dim H_p(M)$: for a vector space $V$, the ordinary flip on $V\otimes V$ has trace $\dim V$. Multiplying by the Lefschetz sign $(-1)^{2p}=1$ and summing gives
$$L(f)=\sum_p(-1)^p b_p(M)=\chi(M).$$
:::

<1>2. Since $\chi(M)\ne0$, $L(f)\ne0$.
::: {.proof}
This is the hypothesis and <1>1.
:::

<1>3. If $g\simeq f$, then $L(g)=L(f)\ne0$.
::: {.proof}
The Lefschetz number depends only on the induced maps on homology, hence is homotopy invariant.
:::

<1>4. Therefore every such $g$ has a fixed point.
::: {.proof}
By the Lefschetz fixed-point theorem, a self-map of the compact triangulable space $M\times M$ with nonzero Lefschetz number has a fixed point.
:::
:::
