---
schema: qual/card@1
id: P-TOPS10E
kind: problem
title: "Euler characteristic equals mod-2 Euler characteristic via UCT"
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Universal Coefficient Theorem
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
For any topological space $X$, whose total homology is a finitely-generated abelian group, let $\chi(X)$ denote the usual Euler characteristic
$$
\chi(X) = \sum_i (-1)^i \dim_{\mathbb{Q}} H_i(X; \mathbb{Q})
$$
and let $\chi_2(X)$ be the "mod-$2$ homology Euler characteristic"
$$
\chi_2(X) = \sum_i (-1)^i \dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2).
$$
Use the universal coefficient theorem to show that $\chi(X) = \chi_2(X)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
Decompose the integral homology groups $H_i(X; \mathbb{Z})$.

::: pf-proof

::: pf-step
Since the total homology is finitely generated, each $H_i(X; \mathbb{Z})$ is a finitely generated abelian group, and $H_i(X; \mathbb{Z}) = 0$ for all but finitely many $i$.

::: pf-proof
hypothesis.
:::

:::

::: pf-step
By the Fundamental Theorem of Finitely Generated Abelian Groups:
\[
H_i(X; \mathbb{Z}) \cong \mathbb{Z}^{b_i} \oplus T_i,
\]
where $b_i = \operatorname{rank} H_i(X; \mathbb{Z})$ is the $i$-th Betti number and $T_i$ is the finite torsion subgroup.

::: pf-proof
classification of finitely generated abelian groups.
:::

:::

::: pf-step
Let $t_i = \dim_{\mathbb{Z}_2}(H_i(X; \mathbb{Z}) \otimes \mathbb{Z}_2) - b_i = \dim_{\mathbb{Z}_2}(T_i \otimes \mathbb{Z}_2)$.

::: pf-proof
$\mathbb{Z}^{b_i} \otimes \mathbb{Z}_2 \cong \mathbb{Z}_2^{b_i}$, which has dimension $b_i$ over $\mathbb{Z}_2$.
:::

:::

:::

:::

::: {.pf-step #s2}
Compute $\chi(X)$ via the Universal Coefficient Theorem over $\mathbb{Q}$:

::: pf-proof

::: {.pf-step #s2-1}
By the Universal Coefficient Theorem for homology:
\[
H_i(X; \mathbb{Q}) \cong (H_i(X; \mathbb{Z}) \otimes \mathbb{Q}) \oplus \operatorname{Tor}_1(H_{i-1}(X; \mathbb{Z}), \mathbb{Q}).
\]

::: pf-proof
Universal Coefficient Theorem with coefficients in a field.
:::

:::

::: {.pf-step #s2-2}
Since $\mathbb{Q}$ is flat (or divisible), $\operatorname{Tor}_1(A, \mathbb{Q}) = 0$ for every abelian group $A$.

::: pf-proof
Tor vanishes over fields / divisible groups.
:::

:::

::: {.pf-step #s2-3}
$H_i(X; \mathbb{Z}) \otimes \mathbb{Q} \cong (\mathbb{Z}^{b_i} \oplus T_i) \otimes \mathbb{Q} \cong \mathbb{Q}^{b_i}$, since $T_i \otimes \mathbb{Q} = 0$ for any torsion group $T_i$.

::: pf-proof
tensoring torsion modules with $\mathbb{Q}$ gives 0.
:::

:::

::: pf-step
Thus $\dim_{\mathbb{Q}} H_i(X; \mathbb{Q}) = b_i$, and:
\[
\chi(X) = \sum_i (-1)^i b_i.
\]

::: pf-proof
Steps [](#s2-1){.pf-ref}, [](#s2-2){.pf-ref}, [](#s2-3){.pf-ref}, and definition of $\chi(X)$.
:::

:::

:::

:::

::: {.pf-step #s3}
Compute $\chi_2(X)$ via the Universal Coefficient Theorem over $\mathbb{Z}_2$:

::: pf-proof

::: pf-step
By the Universal Coefficient Theorem with coefficients in $\mathbb{Z}_2$:
\[
0 \to H_i(X; \mathbb{Z}) \otimes \mathbb{Z}_2 \to H_i(X; \mathbb{Z}_2) \to \operatorname{Tor}_1(H_{i-1}(X; \mathbb{Z}), \mathbb{Z}_2) \to 0.
\]

::: pf-proof
Universal Coefficient Theorem for homology.
:::

:::

::: {.pf-step #s3-2}
Since $\mathbb{Z}_2$ is a field, every short exact sequence of $\mathbb{Z}_2$-vector spaces splits, so:
\[
\dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2) = \dim_{\mathbb{Z}_2}(H_i(X; \mathbb{Z}) \otimes \mathbb{Z}_2) + \dim_{\mathbb{Z}_2}\operatorname{Tor}_1(H_{i-1}(X; \mathbb{Z}), \mathbb{Z}_2).
\]

::: pf-proof
rank-nullity / dimension additivity for split exact sequences.
:::

:::

::: {.pf-step #s3-3}
$\dim_{\mathbb{Z}_2}(H_i(X; \mathbb{Z}) \otimes \mathbb{Z}_2) = b_i + t_i$.

::: pf-proof
definition of $t_i$ in step [](#s1){.pf-ref}.
:::

:::

::: {.pf-step #s3-4}
For any finitely generated abelian group $A \cong \mathbb{Z}^b \oplus T$, $\operatorname{Tor}_1(A, \mathbb{Z}_2) \cong \operatorname{Tor}_1(T, \mathbb{Z}_2) \cong T \otimes \mathbb{Z}_2$.

::: pf-proof
$\operatorname{Tor}_1(\mathbb{Z}, \mathbb{Z}_2) = 0$, and for cyclic groups $\operatorname{Tor}_1(\mathbb{Z}/m, \mathbb{Z}_2) \cong \mathbb{Z}/\gcd(m, 2) \cong (\mathbb{Z}/m) \otimes \mathbb{Z}_2$.
:::

:::

::: {.pf-step #s3-5}
Hence $\dim_{\mathbb{Z}_2}\operatorname{Tor}_1(H_{i-1}(X; \mathbb{Z}), \mathbb{Z}_2) = t_{i-1}$.

::: pf-proof
Step [](#s3-4){.pf-ref} applied to $A = H_{i-1}(X; \mathbb{Z})$.
:::

:::

::: pf-step
Substituting into step [](#s3-2){.pf-ref} yields $\dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2) = b_i + t_i + t_{i-1}$.

::: pf-proof
Steps [](#s3-2){.pf-ref}, [](#s3-3){.pf-ref}, and [](#s3-5){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s4}
Show $\chi(X) = \chi_2(X)$:

::: pf-proof

::: {.pf-step #s4-1}
Substitute the dimension formula into the definition of $\chi_2(X)$:
\[
\chi_2(X) = \sum_i (-1)^i \dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2) = \sum_i (-1)^i (b_i + t_i + t_{i-1}) = \sum_i (-1)^i b_i + \sum_i (-1)^i t_i + \sum_i (-1)^i t_{i-1}.
\]

::: pf-proof
linearity of finite summation.
:::

:::

::: {.pf-step #s4-2}
Re-indexing the third sum with $j = i - 1$:
\[
\sum_i (-1)^i t_{i-1} = \sum_j (-1)^{j+1} t_j = -\sum_j (-1)^j t_j.
\]

::: pf-proof
$(-1)^{j+1} = -(-1)^j$.
:::

:::

::: {.pf-step #s4-3}
Thus the torsion terms cancel completely:
\[
\sum_i (-1)^i t_i + \sum_i (-1)^i t_{i-1} = \sum_i (-1)^i t_i - \sum_j (-1)^j t_j = 0.
\]

::: pf-proof
Step [](#s4-2){.pf-ref}.
:::

:::

::: pf-step
Therefore $\chi_2(X) = \sum_i (-1)^i b_i = \chi(X)$.

::: pf-proof
Steps [](#s4-1){.pf-ref}, [](#s4-3){.pf-ref}, and [](#s2){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Step [](#s4){.pf-ref}.
:::

:::
:::
