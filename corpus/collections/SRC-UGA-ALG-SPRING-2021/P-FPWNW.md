---
schema: qual/card@1
id: P-FPWNW
kind: problem
title: Groups of order $p^2$ are abelian; the Sylow theorems; groups of order $4225=5^2
  13^2$ are abelian, with their isomorphism classes
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
a. Show that every group of order $p^2$ with $p$ prime is abelian.

b. State the 3 Sylow theorems.

c. Show that any group of order $4225 = 5^2 13^2$ is abelian.

d. Write down one representative from each isomorphism class of abelian groups of order 4225.
:::

::: {.solution}
**(a).**

<1>1. Let $G$ have order $p^2$. Then $Z(G) \neq 1$ (a $p$-group has nontrivial center).
Proof: class equation.

<1>2. $G/Z(G)$ has order $1$ or $p$ (since $|Z(G)|$ is $p$ or $p^2$).
Proof: <1>1 and Lagrange.

<1>3. If $|G/Z(G)| = p$, then $G/Z(G)$ is cyclic, which forces $G$ abelian (a group with cyclic center quotient is abelian).
Proof: standard fact.

<1>4. If $|G/Z(G)| = 1$, then $G = Z(G)$ is abelian.
Proof: <1>2.

<1>5. Hence $G$ is abelian.
Proof: <1>3 and <1>4.

**(b).**

<1>1. **Sylow 1:** For each prime $p$ dividing $|G|$, there is a Sylow $p$-subgroup.
**Sylow 2:** All Sylow $p$-subgroups are conjugate, and the number $n_p$ satisfies $n_p \equiv 1 \pmod p$ and $n_p \mid |G|$.
**Sylow 3:** $n_p \equiv 1 \pmod p$ and $n_p$ divides $|G|/p^a$ (where $p^a$ is the largest power of $p$ dividing $|G|$).
Proof: statement of the Sylow theorems.

**(c).**

<1>1. Let $G$ have order $4225 = 5^2 \cdot 13^2$. By Sylow, $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 13^2 = 169$, so $n_5 \in \{1, 169\}$.
Proof: Sylow's theorem.

<1>2. $n_{13} \equiv 1 \pmod{13}$ and $n_{13} \mid 25$, so $n_{13} = 1$.
Proof: Sylow's theorem (the divisors of $25$ are $1, 5, 25$, and only $1 \equiv 1 \pmod{13}$).

<1>3. Hence $G$ has a unique normal Sylow $13$-subgroup $P \cong \ZZ/13^2$ or $\ZZ/13 \times \ZZ/13$.
Proof: <1>2.

<1>4. The normal subgroup $P$ acts by conjugation on the Sylow $5$-subgroups, so $n_5$ divides $|P| = 169$ and $n_5 \equiv 1 \pmod 5$; the only such divisor is $n_5 = 1$.
Proof: <1>3 and Sylow (the orbit sizes divide $169$, and $n_5 \equiv 1 \pmod 5$ forces $n_5 = 1$).

<1>5. Hence $G$ has a unique normal Sylow $5$-subgroup $Q$ and a unique normal Sylow $13$-subgroup $P$, so $G = P \times Q$.
Proof: <1>3 and <1>4.

<1>6. $P$ and $Q$ are abelian (groups of order $p^2$ are abelian by (a)), so $G = P \times Q$ is abelian.
Proof: <1>5 and (a).

**(d).**

<1>1. The abelian groups of order $4225 = 5^2 \cdot 13^2$ are the products of abelian groups of order $5^2$ and $13^2$.
Proof: fundamental theorem of finite abelian groups.

<1>2. The abelian groups of order $5^2$ are $\ZZ/25$ and $\ZZ/5 \times \ZZ/5$; the abelian groups of order $13^2$ are $\ZZ/169$ and $\ZZ/13 \times \ZZ/13$.
Proof: fundamental theorem.

<1>3. Hence the four isomorphism classes are:
$$\ZZ/25 \times \ZZ/169,\ \ZZ/25 \times \ZZ/13 \times \ZZ/13,\ \ZZ/5 \times \ZZ/5 \times \ZZ/169,\ \ZZ/5 \times \ZZ/5 \times \ZZ/13 \times \ZZ/13.$$
Proof: <1>1 and <1>2.

<1>4. Q.E.D.
Proof: <1>5 (a), <1>1 (b), <1>6 (c), <1>3 (d).
:::
