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

::: problem
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
<1>1. Decompose the integral homology groups $H_i(X; \mathbb{Z})$.
<2>1. Since the total homology is finitely generated, each $H_i(X; \mathbb{Z})$ is a finitely generated abelian group, and $H_i(X; \mathbb{Z}) = 0$ for all but finitely many $i$.
Proof: hypothesis.
<2>2. By the Fundamental Theorem of Finitely Generated Abelian Groups:
\[
H_i(X; \mathbb{Z}) \cong \mathbb{Z}^{b_i} \oplus T_i,
\]
where $b_i = \operatorname{rank} H_i(X; \mathbb{Z})$ is the $i$-th Betti number and $T_i$ is the finite torsion subgroup.
Proof: classification of finitely generated abelian groups.
<2>3. Let $t_i = \dim_{\mathbb{Z}_2}(H_i(X; \mathbb{Z}) \otimes \mathbb{Z}_2) - b_i = \dim_{\mathbb{Z}_2}(T_i \otimes \mathbb{Z}_2)$.
Proof: $\mathbb{Z}^{b_i} \otimes \mathbb{Z}_2 \cong \mathbb{Z}_2^{b_i}$, which has dimension $b_i$ over $\mathbb{Z}_2$.

<1>2. Compute $\chi(X)$ via the Universal Coefficient Theorem over $\mathbb{Q}$:
<2>1. By the Universal Coefficient Theorem for homology:
\[
H_i(X; \mathbb{Q}) \cong (H_i(X; \mathbb{Z}) \otimes \mathbb{Q}) \oplus \operatorname{Tor}_1(H_{i-1}(X; \mathbb{Z}), \mathbb{Q}).
\]
Proof: Universal Coefficient Theorem with coefficients in a field.
<2>2. Since $\mathbb{Q}$ is flat (or divisible), $\operatorname{Tor}_1(A, \mathbb{Q}) = 0$ for every abelian group $A$.
Proof: Tor vanishes over fields / divisible groups.
<2>3. $H_i(X; \mathbb{Z}) \otimes \mathbb{Q} \cong (\mathbb{Z}^{b_i} \oplus T_i) \otimes \mathbb{Q} \cong \mathbb{Q}^{b_i}$, since $T_i \otimes \mathbb{Q} = 0$ for any torsion group $T_i$.
Proof: tensoring torsion modules with $\mathbb{Q}$ gives 0.
<2>4. Thus $\dim_{\mathbb{Q}} H_i(X; \mathbb{Q}) = b_i$, and:
\[
\chi(X) = \sum_i (-1)^i b_i.
\]
Proof: <2>1, <2>2, <2>3, and definition of $\chi(X)$.

<1>3. Compute $\chi_2(X)$ via the Universal Coefficient Theorem over $\mathbb{Z}_2$:
<2>1. By the Universal Coefficient Theorem with coefficients in $\mathbb{Z}_2$:
\[
0 \to H_i(X; \mathbb{Z}) \otimes \mathbb{Z}_2 \to H_i(X; \mathbb{Z}_2) \to \operatorname{Tor}_1(H_{i-1}(X; \mathbb{Z}), \mathbb{Z}_2) \to 0.
\]
Proof: Universal Coefficient Theorem for homology.
<2>2. Since $\mathbb{Z}_2$ is a field, every short exact sequence of $\mathbb{Z}_2$-vector spaces splits, so:
\[
\dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2) = \dim_{\mathbb{Z}_2}(H_i(X; \mathbb{Z}) \otimes \mathbb{Z}_2) + \dim_{\mathbb{Z}_2}\operatorname{Tor}_1(H_{i-1}(X; \mathbb{Z}), \mathbb{Z}_2).
\]
Proof: rank-nullity / dimension additivity for split exact sequences.
<2>3. $\dim_{\mathbb{Z}_2}(H_i(X; \mathbb{Z}) \otimes \mathbb{Z}_2) = b_i + t_i$.
Proof: definition of $t_i$ in <1>1.
<2>4. For any finitely generated abelian group $A \cong \mathbb{Z}^b \oplus T$, $\operatorname{Tor}_1(A, \mathbb{Z}_2) \cong \operatorname{Tor}_1(T, \mathbb{Z}_2) \cong T \otimes \mathbb{Z}_2$.
Proof: $\operatorname{Tor}_1(\mathbb{Z}, \mathbb{Z}_2) = 0$, and for cyclic groups $\operatorname{Tor}_1(\mathbb{Z}/m, \mathbb{Z}_2) \cong \mathbb{Z}/\gcd(m, 2) \cong (\mathbb{Z}/m) \otimes \mathbb{Z}_2$.
<2>5. Hence $\dim_{\mathbb{Z}_2}\operatorname{Tor}_1(H_{i-1}(X; \mathbb{Z}), \mathbb{Z}_2) = t_{i-1}$.
Proof: <2>4 applied to $A = H_{i-1}(X; \mathbb{Z})$.
<2>6. Substituting into <2>2 yields $\dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2) = b_i + t_i + t_{i-1}$.
Proof: <2>2, <2>3, and <2>5.

<1>4. Show $\chi(X) = \chi_2(X)$:
<2>1. Substitute the dimension formula into the definition of $\chi_2(X)$:
\[
\chi_2(X) = \sum_i (-1)^i \dim_{\mathbb{Z}_2} H_i(X; \mathbb{Z}_2) = \sum_i (-1)^i (b_i + t_i + t_{i-1}) = \sum_i (-1)^i b_i + \sum_i (-1)^i t_i + \sum_i (-1)^i t_{i-1}.
\]
Proof: linearity of finite summation.
<2>2. Re-indexing the third sum with $j = i - 1$:
\[
\sum_i (-1)^i t_{i-1} = \sum_j (-1)^{j+1} t_j = -\sum_j (-1)^j t_j.
\]
Proof: $(-1)^{j+1} = -(-1)^j$.
<2>3. Thus the torsion terms cancel completely:
\[
\sum_i (-1)^i t_i + \sum_i (-1)^i t_{i-1} = \sum_i (-1)^i t_i - \sum_j (-1)^j t_j = 0.
\]
Proof: <2>2.
<2>4. Therefore $\chi_2(X) = \sum_i (-1)^i b_i = \chi(X)$.
Proof: <2>1, <2>3, and <1>2.

<1>5. Q.E.D.
Proof: <1>4.
:::
