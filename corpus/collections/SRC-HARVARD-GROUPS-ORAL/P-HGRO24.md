---
schema: qual/card@1
id: P-HGRO24
kind: problem
title: Finite p-groups are solvable
classification:
  areas: [algebra]
  topics: [Solvable Groups]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $G$ be a group of order $p^r$, where $p$ is prime.
Prove that $G$ is solvable.
:::

::: {.solution}
<1>1. $G$ has a nontrivial center $Z(G) \neq 1$.
Proof: the class equation $|G| = |Z(G)| + \sum [G : C_G(g_i)]$; each $[G : C_G(g_i)]$ is divisible by $p$, and $|G| = p^r$ is divisible by $p$, so $p \mid |Z(G)|$, hence $Z(G) \neq 1$.

<1>2. $Z(G)$ is abelian and normal in $G$.
Proof: the center is always abelian and normal.

<1>3. $G/Z(G)$ has order $p^{r'}$ with $r' < r$.
Proof: $|Z(G)| > 1$ divides $p^r$, so $|G/Z(G)| = p^{r'}$ with $r' < r$.

<1>4. By induction on $r$, $G/Z(G)$ is solvable.
Proof: the base case $r = 0$ (trivial group) is solvable; <1>3 reduces the exponent.

<1>5. Hence $G$ is solvable.
Proof: $1 \trianglelefteq Z(G) \trianglelefteq G$ with $Z(G)$ abelian and $G/Z(G)$ solvable (<1>4); an extension of a solvable group by an abelian group is solvable.

<1>6. Q.E.D.
Proof: <1>5.
:::
