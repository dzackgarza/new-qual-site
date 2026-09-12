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

For any topological space $X$, whose total homology is a finitely-generated abelian group, let $\chi(X)$ denote the usual Euler characteristic

$$\chi(X) = \sum (-1)^i \dim_{\mathbb{Q}} H_i(X; \mathbb{Q})$$

and let $\chi_2(X)$ be the "mod-2 homology Euler characteristic"

$$\chi_2(X) = \sum (-1)^i \dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2).$$

Use the universal coefficient theorem to show that $\chi(X) = \chi_2(X)$.

::: {.solution}
<1>1. Write
$$
H_i(X;\mathbb Z)\cong\mathbb Z^{b_i}\oplus T_i,
$$
where $T_i$ is finite, and set
$$
t_i=\dim_{\mathbb F_2}(T_i\otimes\mathbb F_2).
$$
::: {.proof}
The total integral homology is finitely generated, so each $H_i$ has this form and only finitely many are nonzero.
:::

<1>2. The homological universal coefficient theorem gives a split short exact sequence
$$
0\to H_i(X;\mathbb Z)\otimes\mathbb F_2
\to H_i(X;\mathbb F_2)
\to \operatorname{Tor}(H_{i-1}(X;\mathbb Z),\mathbb F_2)\to0.
$$
::: {.proof}
This is the universal coefficient theorem for homology with coefficients in $\mathbb F_2$.
:::

<1>3. Therefore
$$
\dim_{\mathbb F_2}H_i(X;\mathbb F_2)=b_i+t_i+t_{i-1}.
$$
::: {.proof}
The free summand contributes $b_i$. For a finite abelian group $T$, both $T\otimes\mathbb F_2$ and $\operatorname{Tor}(T,\mathbb F_2)$ have the same $\mathbb F_2$-dimension, namely the number of cyclic summands of even order; this is $t_i$ for $T_i$ and $t_{i-1}$ for $T_{i-1}$.
:::

<1>4. Hence
$$
\chi_2(X)=\sum_i(-1)^i b_i
+\sum_i(-1)^i t_i
+\sum_i(-1)^i t_{i-1}.
$$
::: {.proof}
Substitute <1>3 into the definition of $\chi_2$.
:::

<1>5. The two torsion sums cancel.
::: {.proof}
Reindex the last sum:
$$
\sum_i(-1)^i t_{i-1}=-\sum_j(-1)^j t_j.
$$
Only finitely many terms are nonzero, so this reindexing is legitimate.
:::

<1>6. Thus
$$
\chi_2(X)=\sum_i(-1)^i b_i=\chi(X).
$$
::: {.proof}
Over $\mathbb Q$, $\dim_{\mathbb Q}H_i(X;\mathbb Q)=b_i$. Apply <1>4--<1>5.
:::
:::
