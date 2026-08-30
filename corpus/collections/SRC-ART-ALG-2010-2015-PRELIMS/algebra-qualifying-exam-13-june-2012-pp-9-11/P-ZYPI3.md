---
schema: qual/card@1
id: P-ZYPI3
kind: problem
title: Finitely generated modules over a PID, groups of order $72$, and rational canonical
  form
classification:
  areas:
  - prelim
  topics:
  - Structure Theorem
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
a. State the structure theorem for finitely generated modules over a PID. You may state either the invariant factors or elementary divisors version.

b. Determine all abelian groups of size 72 up to isomorphism.
Explain how this relates to part (a).

c. Determine all conjugacy classes of 3x3 matrices over $\mathbb{Q}$ with characteristic polynomial $x^3 - 2x^2 + x$.
Explain how this relates to part (a).
:::

::: {.solution}
<1>1. Part (a): State the Structure Theorem for finitely generated modules over a PID:
<2>1. **Theorem (Invariant Factor Form):** Let $R$ be a principal ideal domain (PID) and let $M$ be a finitely generated $R$-module. Then there is an isomorphism:
\[
M \cong R^r \oplus R/(a_1) \oplus R/(a_2) \oplus \cdots \oplus R/(a_k),
\]
where $r \ge 0$ is an integer (the free rank of $M$), and $a_1, a_2, \dots, a_k \in R \setminus \{0\}$ are non-units satisfying the divisibility chain:
\[
a_1 \mid a_2 \mid \cdots \mid a_k.
\]
The rank $r$ and the ideals $(a_1), \dots, (a_k)$ are uniquely determined by $M$.
Proof: standard theorem of module theory over PIDs (Dummit & Foote Theorem 12.1.5).

<1>2. Part (b): Determine all abelian groups of order $72$:
<2>1. Any abelian group $G$ is a $\mathbb{Z}$-module. Since $\mathbb{Z}$ is a PID, a finite abelian group of order $72$ is a torsion $\mathbb{Z}$-module ($r = 0$).
Proof: definition of abelian groups as $\mathbb{Z}$-modules.
<2>2. Factor $72 = 2^3 \cdot 3^2$. By the primary decomposition (elementary divisor form), $G \cong G_2 \oplus G_3$, where $|G_2| = 2^3 = 8$ and $|G_3| = 3^2 = 9$.
Proof: Chinese Remainder Theorem / primary decomposition.
<2>3. The isomorphism classes of $G_2$ of order $8$ correspond to partitions of $3$:
- Partition $3$: $\mathbb{Z}_8$
- Partition $2+1$: $\mathbb{Z}_4 \oplus \mathbb{Z}_2$
- Partition $1+1+1$: $\mathbb{Z}_2 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_2$
Proof: abelian $p$-groups classified by integer partitions.
<2>4. The isomorphism classes of $G_3$ of order $9$ correspond to partitions of $2$:
- Partition $2$: $\mathbb{Z}_9$
- Partition $1+1$: $\mathbb{Z}_3 \oplus \mathbb{Z}_3$
Proof: abelian $p$-groups classified by integer partitions.
<2>5. Taking all $3 \times 2 = 6$ combinations yields the 6 isomorphism classes:
1. $\mathbb{Z}_8 \oplus \mathbb{Z}_9 \cong \mathbb{Z}_{72}$ (invariant factor: $72$)
2. $\mathbb{Z}_8 \oplus \mathbb{Z}_3 \oplus \mathbb{Z}_3 \cong \mathbb{Z}_3 \oplus \mathbb{Z}_{24}$ (invariant factors: $3 \mid 24$)
3. $\mathbb{Z}_4 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_9 \cong \mathbb{Z}_2 \oplus \mathbb{Z}_{36}$ (invariant factors: $2 \mid 36$)
4. $\mathbb{Z}_4 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_3 \oplus \mathbb{Z}_3 \cong \mathbb{Z}_6 \oplus \mathbb{Z}_{12}$ (invariant factors: $6 \mid 12$)
5. $\mathbb{Z}_2 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_9 \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_{18}$ (invariant factors: $2 \mid 2 \mid 18$)
6. $\mathbb{Z}_2 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_3 \oplus \mathbb{Z}_3 \cong \mathbb{Z}_2 \oplus \mathbb{Z}_6 \oplus \mathbb{Z}_6$ (invariant factors: $2 \mid 6 \mid 6$)
Proof: product of cyclic groups and invariant factor conversion.

<1>3. Part (c): Determine all conjugacy classes of $3 \times 3$ matrices over $\mathbb{Q}$ with characteristic polynomial $x^3 - 2x^2 + x$:
<2>1. A matrix $A \in M_3(\mathbb{Q})$ makes $V = \mathbb{Q}^3$ into a finitely generated torsion module over the PID $R = \mathbb{Q}[x]$ via $x \cdot v = Av$.
Conjugacy classes of matrices correspond bijectively to isomorphism classes of $\mathbb{Q}[x]$-modules of $\mathbb{Q}$-dimension 3.
Proof: theory of rational canonical forms over PIDs.
<2>2. By the Structure Theorem, $V \cong \mathbb{Q}[x]/(f_1) \oplus \cdots \oplus \mathbb{Q}[x]/(f_k)$ where $f_1 \mid \cdots \mid f_k$ are monic polynomials with $\prod_{i=1}^k f_i(x) = p_A(x) = x(x-1)^2$.
Proof: invariant factor theorem for $\mathbb{Q}[x]$-modules.
<2>3. The possible invariant factor chains dividing $x(x-1)^2$ with product degree $3$ are:
- **Case 1 ($k=1$):** Invariant factor $f_1(x) = x(x-1)^2 = x^3 - 2x^2 + x$.
  Minimal polynomial $m_A(x) = x(x-1)^2$.
  Rational canonical form: Companion matrix $C(x^3 - 2x^2 + x) = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 2 \end{pmatrix}$ (or Jordan form $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$).
- **Case 2 ($k=2$):** Invariant factors $f_1(x) = x-1$ and $f_2(x) = x(x-1) = x^2 - x$.
  Minimal polynomial $m_A(x) = x(x-1)$.
  Rational canonical form: $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ (or Jordan form $\begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$).
Proof: divisibility $f_1 \mid f_2$ and degree sum $1 + 2 = 3$.
<2>4. Thus there are exactly **2** conjugacy classes of such matrices over $\mathbb{Q}$.
Proof: <2>3.

<1>4. Conclusion:
(a) Theorem stated above.
(b) Exactly 6 isomorphism classes of abelian groups of size 72.
(c) Exactly 2 conjugacy classes of $3 \times 3$ matrices over $\mathbb{Q}$. Q.E.D.
Proof: <1>1, <1>2, and <1>3.
:::
