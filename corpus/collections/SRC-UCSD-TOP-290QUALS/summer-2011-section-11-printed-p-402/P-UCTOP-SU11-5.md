---
schema: qual/card@1
id: P-UCTOP-SU11-5
kind: problem
title: Euler characteristic equals mod-2 Euler characteristic
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
For any topological space $X$, whose total homology is a finitely-generated abelian group, let $\chi(X)$ denote the usual Euler characteristic

$$\chi(X) = \sum (-1)^i \dim_{\mathbb{Q}} H_i(X; \mathbb{Q})$$

and let $\chi_2(X)$ be the "mod-2 homology Euler characteristic"

$$\chi_2(X) = \sum (-1)^i \dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2).$$

Use the universal coefficient theorem to show that $\chi(X) = \chi_2(X)$.
:::

::: {.solution}

::: pf

::: pf-step
Write
$$
H_i(X;\mathbb Z)\cong\mathbb Z^{b_i}\oplus T_i,
$$
where $T_i$ is finite, and set
$$
t_i=\dim_{\mathbb F_2}(T_i\otimes\mathbb F_2).
$$

::: pf-proof
The total integral homology is finitely generated, so each $H_i$ has this form and only finitely many are nonzero.
:::

:::

::: pf-step
The homological universal coefficient theorem gives a split short exact sequence
$$
0\to H_i(X;\mathbb Z)\otimes\mathbb F_2
\to H_i(X;\mathbb F_2)
\to \operatorname{Tor}(H_{i-1}(X;\mathbb Z),\mathbb F_2)\to0.
$$

::: pf-proof
This is the universal coefficient theorem for homology with coefficients in $\mathbb F_2$.
:::

:::

::: {.pf-step #dimension-formula}
Therefore
$$
\dim_{\mathbb F_2}H_i(X;\mathbb F_2)=b_i+t_i+t_{i-1}.
$$

::: pf-proof
The free summand contributes $b_i$. For a finite abelian group $T$, both $T\otimes\mathbb F_2$ and $\operatorname{Tor}(T,\mathbb F_2)$ have the same $\mathbb F_2$-dimension, namely the number of cyclic summands of even order; this is $t_i$ for $T_i$ and $t_{i-1}$ for $T_{i-1}$.
:::

:::

::: {.pf-step #chi2-split-sum}
Hence
$$
\chi_2(X)=\sum_i(-1)^i b_i
+\sum_i(-1)^i t_i
+\sum_i(-1)^i t_{i-1}.
$$

::: pf-proof
Substitute step [](#dimension-formula){.pf-ref} into the definition of $\chi_2$.
:::

:::

::: {.pf-step #torsion-sums-cancel}
The two torsion sums cancel.

::: pf-proof
Reindex the last sum:
$$
\sum_i(-1)^i t_{i-1}=-\sum_j(-1)^j t_j.
$$
Only finitely many terms are nonzero, so this reindexing is legitimate.
:::

:::

::: pf-step
Thus
$$
\chi_2(X)=\sum_i(-1)^i b_i=\chi(X).
$$

::: pf-proof
Over $\mathbb Q$, $\dim_{\mathbb Q}H_i(X;\mathbb Q)=b_i$. Apply steps [](#chi2-split-sum){.pf-ref} and [](#torsion-sums-cancel){.pf-ref}.
:::

:::

:::

:::
