---
schema: qual/card@1
id: P-MMAQ-42RJ23SMHI
kind: problem
title: Groups of order $351=3^3\cdot 13$ are not simple; groups of order $33$ are
  cyclic
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Sylow Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked both group orders and conclusions against Groups 4 on PDF page 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked both allowed Sylow-13 counts, the exact complement count forcing a unique Sylow-3 subgroup, and the normal Sylow factors and generator of the order-33 group."
---

::: problem
- Prove that a group of order $351=3^3\cdot 13$ cannot be simple.

- Prove that a group of order $33$ must be cyclic.
:::

::: solution
<1>1. A group $G$ of order $351$ is not simple.

::: proof
Sylow's theorems give $n_{13}\mid27$ and
$n_{13}\equiv1\pmod{13}$ [@DF04]. The divisors of
$27$ are $1,3,9,27$, so $n_{13}=1$ or $27$.
If $n_{13}=1$, the unique Sylow $13$-subgroup is a
nontrivial proper normal subgroup, proving the claim.

Suppose $n_{13}=27$. Two distinct subgroups of order
$13$ have trivial intersection: a shared nonidentity
element would generate both. They therefore contain
exactly $27\cdot12=324$ distinct nonidentity elements.
Let $X$ be the complement of this set in $G$.
Then $|X|=351-324=27$, and the identity lies in $X$.

Every Sylow $3$-subgroup $P$ is contained in $X$,
since the order of a nonidentity element of $P$ is a
power of three and cannot be thirteen. But $|P|=27=|X|$,
so $P=X$. Consequently every Sylow $3$-subgroup is
the same subgroup. It is normal by Sylow conjugacy,
and is nontrivial and proper. This proves nonsimplicity
also in the second case.
:::

<1>2. A group $G$ of order $33$ is cyclic.

::: proof
Here $n_{11}\mid3$ and $n_{11}\equiv1\pmod{11}$,
so the Sylow $11$-subgroup $Q$ is unique. Also
$n_3\mid11$ and $n_3\equiv1\pmod3$; since
$11\equiv2\pmod3$, the Sylow $3$-subgroup $P$ is
unique [@DF04]. Thus both are normal, and their
intersection is trivial because its order divides
both $3$ and $11$.

For $x\in P$ and $y\in Q$, the commutator
$xyx^{-1}y^{-1}$ belongs to both normal subgroups
and hence is one. Multiplication gives a homomorphism
$P\times Q\to G$. Its kernel is trivial, because
$xy=1$ implies $x=y^{-1}\in P\cap Q$. Both groups
have order $33$, so the homomorphism is an isomorphism.
The prime-order groups $P,Q$ are cyclic. A pair of
generators has order $\operatorname{lcm}(3,11)=33$,
and its image generates $G$.
:::
:::
