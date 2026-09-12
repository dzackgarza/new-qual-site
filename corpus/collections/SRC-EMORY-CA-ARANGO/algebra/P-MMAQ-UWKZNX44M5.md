---
schema: qual/card@1
id: P-MMAQ-UWKZNX44M5
kind: problem
title: If $G/Z(G)$ is cyclic then $G$ is abelian; $p$-groups have nontrivial center;
  groups of order $p^2$ are abelian
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared all three assertions and the nontrivial p-group hypothesis with Groups 5 on PDF page 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the central-coset representatives, divisibility in the class equation, and both possible center orders for a group of order p squared."
---

::: problem
1. Let $G$ be a group, and $Z(G)$ the center of $G$.
   Prove that if $G/Z(G)$ is cyclic, then $G$ is abelian.

2. Prove that a group of order $p^n$, where $p$ is a prime and $n \geq 1$, has non-trivial center.

3. Prove that a group of order $p^2$ must be abelian.
:::

::: solution
<1>1. A group with cyclic quotient by its center is abelian.

::: proof
Choose $a\in G$ whose coset generates $G/Z(G)$.
Every element of $G$ has the form $a^i z$ for some
integer $i$ and $z\in Z(G)$. For any two such elements,
centrality gives
$$
(a^i z)(a^j w)=a^{i+j}zw
=a^{j+i}wz=(a^j w)(a^i z).
$$
Thus every pair of elements commutes. The argument
also covers the trivial cyclic quotient by taking $a=1$.
:::

<1>2. A group of order $p^n$, with $n\geq1$, has
nontrivial center.

::: proof
Let $G$ act on itself by conjugation. The orbit of
$x$ has size $[G:C_G(x)]$ by orbit-stabilizer, where
$C_G(x)$ is its centralizer [@DF04]. The orbit has
one element exactly when $x\in Z(G)$. Every other
orbit has size a power of $p$ greater than one,
and hence divisible by $p$.

Partitioning $G$ into its conjugacy classes therefore
gives $|G|\equiv|Z(G)|\pmod p$. Since $p\mid|G|$,
one has $p\mid|Z(G)|$. The center contains the identity,
so its positive order is at least $p$.
:::

<1>3. Every group of order $p^2$ is abelian.

::: proof
By step <1>2 and Lagrange's theorem, the center has
order $p$ or $p^2$. In the second case $Z(G)=G$,
so the group is abelian. In the first case $G/Z(G)$
has prime order $p$. A group of prime order is cyclic:
any nonidentity element generates a subgroup whose
order divides $p$ and exceeds one. Step <1>1 then
again gives that $G$ is abelian. In fact this rules
out center order $p$, leaving $Z(G)=G$.
:::
:::
