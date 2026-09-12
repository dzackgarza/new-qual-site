---
schema: qual/card@1
id: P-HGRO19
kind: problem
title: A normal subgroup of order 3 or 9 in a group of order 36
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Prove that every group of order $36$ has a nontrivial normal subgroup of order $3$ or $9$.
:::

::: solution
Let $n_3$ be the number of Sylow $3$-subgroups of $G$.
Since $|G|=36=2^2\cdot3^2$, Sylow's theorem gives
\[
n_3\equiv1\pmod3,
\qquad
n_3\mid4.
\]
Thus $n_3=1$ or $4$.

<1>1. If $n_3=1$, then $G$ has a normal subgroup of order $9$.
::: proof
The unique Sylow $3$-subgroup has order $9$ and is normal.
:::

<1>2. If $n_3=4$, then $G$ has a normal subgroup of order $3$ or $9$.
::: proof
Let $G$ act by conjugation on its four Sylow $3$-subgroups. This gives a
homomorphism
\[
\varphi:G\to S_4.
\]
The action is transitive by Sylow conjugacy, so $|\operatorname{im}\varphi|$ is
divisible by $4$. Also
\[
|\operatorname{im}\varphi|\mid |G|=36
\quad\text{and}\quad
|\operatorname{im}\varphi|\mid |S_4|=24.
\]
Hence $|\operatorname{im}\varphi|$ divides $12$ and is divisible by $4$, so it
is $4$ or $12$. Therefore
\[
|\ker\varphi|=\frac{36}{|\operatorname{im}\varphi|}
\]
is respectively $9$ or $3$. The kernel is normal in $G$.
:::

<1>3. Hence every group of order $36$ has a nontrivial normal subgroup of order
$3$ or $9$.
::: proof
Combine <1>1 and <1>2.
:::
:::
