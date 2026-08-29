---
schema: qual/card@1
id: P-G52LZ
kind: problem
title: Every $p$-group is nilpotent
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Nilpotent Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Show that every $p\dash$group is nilpotent.
:::

::: {.solution}
<1>1. Let $G$ be a finite $p$-group, $|G| = p^n$.
Proof: setup.

<1>2. $G$ has a nontrivial center $Z(G) \neq 1$.
Proof: the class equation: $|G| = |Z(G)| + \sum [G : C_G(g_i)]$, and each $[G : C_G(g_i)]$ is divisible by $p$, so $p \mid |Z(G)|$.

<1>3. Define the upper central series $1 = Z_0 \le Z_1 \le Z_2 \le \cdots$ by $Z_{i+1}/Z_i = Z(G/Z_i)$.
Proof: definition of the upper central series.

<1>4. Each $Z_{i+1}/Z_i$ is nontrivial as long as $Z_i \neq G$.
Proof: $G/Z_i$ is a $p$-group (or trivial), so it has a nontrivial center unless it is trivial.

<1>5. Hence the upper central series reaches $G$ in finitely many steps: $Z_n = G$.
Proof: each step strictly increases the order (by a factor of at least $p$), and $|G| = p^n$ is finite, so after at most $n$ steps we reach $G$.

<1>6. A group whose upper central series reaches the whole group is nilpotent.
Proof: definition of nilpotency.

<1>7. Hence $G$ is nilpotent.
Proof: <1>5 and <1>6.

<1>8. Q.E.D.
Proof: <1>7.
:::
