---
schema: qual/card@1
id: P-VXWNJ
kind: problem
title: Noncyclic finite abelian groups contain $\ZZ_p^2$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Structure Theorem
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the Hungerford exercise statement reproduced in the UGA algebra problem-set archive.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a finite abelian group that is not cyclic.
Show that $G$ contains a subgroup isomorphic to $\mathbb{Z}_p \oplus \mathbb{Z}_p$ for some prime $p$.
:::

::: solution
Write $G$ as the direct sum of its Sylow subgroups,
\[
G=\bigoplus_{p\mid |G|}G_p.
\]

<1>1. At least one Sylow subgroup $G_p$ is noncyclic.
::: proof
If every $G_p$ were cyclic, then their orders would be pairwise coprime. The
direct product of finite cyclic groups of pairwise coprime orders is cyclic, so
$G$ would be cyclic, contrary to hypothesis.
:::

<1>2. A noncyclic finite abelian $p$-group contains a subgroup isomorphic to
$\ZZ_p\oplus\ZZ_p$.
::: proof
By the structure theorem for finite abelian $p$-groups,
\[
G_p\cong \ZZ_{p^{a_1}}\oplus\cdots\oplus\ZZ_{p^{a_r}}
\]
with $a_i\ge1$. Since $G_p$ is not cyclic, one has $r\ge2$.

In the first two summands, the elements
\[
x=(p^{a_1-1},0,\ldots,0),\qquad
y=(0,p^{a_2-1},0,\ldots,0)
\]
both have order $p$. They lie in distinct direct summands, so
\[
\langle x,y\rangle=\langle x\rangle\oplus\langle y\rangle
\cong\ZZ_p\oplus\ZZ_p.
\]
:::

<1>3. Hence $G$ contains a subgroup isomorphic to $\ZZ_p\oplus\ZZ_p$ for some
prime $p$.
::: proof
Choose the prime supplied by <1>1 and apply <1>2 inside the subgroup $G_p\le G$.
:::
:::
