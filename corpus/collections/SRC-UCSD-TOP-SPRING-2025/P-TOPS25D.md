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

::: {.problem}
For any topological space $X$ whose total homology is a finitely-generated abelian group, let $\chi(X)$ denote the usual Euler characteristic
$$
\chi(X) = \sum_i (-1)^i \dim_{\QQ} H_i(X; \QQ)
$$
and let $\chi_2(X)$ be the "mod-2 homology Euler characteristic"
$$
\chi_2(X) = \sum_i (-1)^i \dim_{\FF_2} H_i(X; \FF_2).
$$
Use the universal coefficient theorem to show that $\chi(X) = \chi_2(X)$.
:::

::: {.solution}

::: pf

::: pf-step
Write each finitely generated integral homology group as
$$H_i(X;\ZZ)\cong\ZZ^{b_i}\oplus T_i,$$
with $T_i$ finite.

::: pf-proof
This is the structure theorem for finitely generated abelian groups. The rational Betti number is $b_i$.
:::

:::

::: pf-step
Let $t_i=\dim_{\FF_2}(T_i\otimes\FF_2)$. The homology UCT gives
$$\dim_{\FF_2}H_i(X;\FF_2)=b_i+t_i+t_{i-1}.$$

::: pf-proof
The exact sequence is
$$0\to H_i(X;\ZZ)\otimes\FF_2\to H_i(X;\FF_2)\to\operatorname{Tor}(H_{i-1}(X;\ZZ),\FF_2)\to0.$$
For a finite abelian group, the dimensions of $T\otimes\FF_2$ and $\operatorname{Tor}(T,\FF_2)$ agree: both count the cyclic summands of even order.
:::

:::

::: pf-step
Consequently the torsion contributions cancel in the alternating sum:
$$\chi_2(X)=\sum_i(-1)^ib_i+\sum_i(-1)^it_i+\sum_i(-1)^it_{i-1}=\sum_i(-1)^ib_i.$$

::: pf-proof
Reindex the last sum; it is the negative of the preceding torsion sum.
:::

:::

::: pf-step
Thus
$$\boxed{\chi_2(X)=\chi(X).}$$

::: pf-proof
By definition $\chi(X)=\sum_i(-1)^ib_i$.
:::

:::

:::

:::
