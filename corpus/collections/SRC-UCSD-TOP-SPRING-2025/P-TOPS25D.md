---
schema: qual/card@1
id: P-TOPS25D
kind: problem
title: Euler characteristic equals mod-2 homology Euler characteristic
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: problem
For any topological space $X$ whose total homology is a finitely-generated abelian group, let $\chi(X)$ denote the usual Euler characteristic
\[
\chi(X) = \sum_i (-1)^i \dim_{\mathbb{Q}} H_i(X; \mathbb{Q})
\]
and let $\chi_2(X)$ be the "mod-2 homology Euler characteristic"
\[
\chi_2(X) = \sum_i (-1)^i \dim_{\mathbb{F}_2} H_i(X; \mathbb{F}_2).
\]
Use the universal coefficient theorem to show that $\chi(X) = \chi_2(X)$.
:::

::: {.solution}
<1>1. Write each finitely generated integral homology group as
$$H_i(X;\mathbb Z)\cong\mathbb Z^{b_i}\oplus T_i,$$
with $T_i$ finite.
::: {.proof}
This is the structure theorem for finitely generated abelian groups. The rational Betti number is $b_i$.
:::

<1>2. Let $t_i=\dim_{\mathbb F_2}(T_i\otimes\mathbb F_2)$. The homology UCT gives
$$\dim_{\mathbb F_2}H_i(X;\mathbb F_2)=b_i+t_i+t_{i-1}.$$
::: {.proof}
The exact sequence is
$$0\to H_i(X;\mathbb Z)\otimes\mathbb F_2\to H_i(X;\mathbb F_2)\to\operatorname{Tor}(H_{i-1}(X;\mathbb Z),\mathbb F_2)\to0.$$
For a finite abelian group, the dimensions of $T\otimes\mathbb F_2$ and $\operatorname{Tor}(T,\mathbb F_2)$ agree: both count the cyclic summands of even order.
:::

<1>3. Consequently the torsion contributions cancel in the alternating sum:
$$\chi_2(X)=\sum_i(-1)^ib_i+\sum_i(-1)^it_i+\sum_i(-1)^it_{i-1}=\sum_i(-1)^ib_i.$$
::: {.proof}
Reindex the last sum; it is the negative of the preceding torsion sum.
:::

<1>4. Thus
$$\boxed{\chi_2(X)=\chi(X).}$$
::: {.proof}
By definition $\chi(X)=\sum_i(-1)^ib_i$.
:::
:::
