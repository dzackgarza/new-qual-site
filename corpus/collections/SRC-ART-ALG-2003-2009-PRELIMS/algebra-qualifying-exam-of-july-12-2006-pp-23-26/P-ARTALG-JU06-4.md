---
schema: qual/card@1
id: P-ARTALG-JU06-4
kind: problem
title: Normal subgroups of p-groups of every order up to p^k
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the full range of exponents and the normality requirement with July 2006 Groups 4 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the central order-p subgroup, the induction boundary, and normality and order of each inverse image."
---

::: problem
If $p$ is a prime, $k$ is a positive integer and $G$ is a group of order $p^k$, show that for each positive integer $i \leq k$, $G$ has a normal subgroup of order $p^i$.
:::

::: solution
<1>1. Every nontrivial finite $p$-group has a central subgroup of order $p$.

::: proof
In the class equation, each noncentral conjugacy class has size
$[G:C_G(x)]$, a power of $p$ greater than $1$ [@DF04]. It follows
that $p\mid |Z(G)|$. Since the center contains the identity, it
contains some $z\ne1$.
By Lagrange's theorem, the order of $z$ is $p^a$ with $a\geq1$.
Then $c=z^{p^{a-1}}$ is nonidentity and satisfies $c^p=1$, so it
has order $p$. The subgroup $C=\langle c\rangle$ lies in the center
and is therefore normal in $G$.
:::

<1>2. Induction on $k$ gives the asserted normal subgroups.

::: proof
When $k=1$, the only requested order is $p$, and $G$ itself is a
normal subgroup of that order.

Let $k\geq2$ and assume the assertion for groups of order $p^{k-1}$.
Choose $C$ as in step <1>1. It supplies the subgroup of order $p$.
Let $\rho:G\to G/C$ be the quotient map; its codomain has order
$p^{k-1}$.

For any $i$ with $2\leq i\leq k$, induction supplies a normal
subgroup $M\lhd G/C$ of order $p^{i-1}$. Set $N=\rho^{-1}(M)$.
For $g\in G$ and $n\in N$, we have
$$
\rho(gng^{-1})=\rho(g)\rho(n)\rho(g)^{-1}\in M,
$$
so $N$ is normal in $G$. The map $N\to M$ is surjective with
kernel $C$. Its fibers are cosets of $C$, each of size $p$;
hence $|N|=p|M|=p^i$. This constructs the required subgroup for
every $i$ and completes the induction.
:::
:::
