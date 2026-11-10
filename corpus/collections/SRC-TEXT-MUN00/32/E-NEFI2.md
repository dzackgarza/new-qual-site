---
schema: qual/card@1
id: E-NEFI2
kind: problem
title: Regular Lindelof spaces are normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
  - Countability
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 32 Exercise 4, printed p. 205,
    and against the proof of Theorem 32.1 (printed p. 200), whose indexing the card copies with a
    countable subcover in place of a countable basis, and Exercise 30.9 (a closed subspace of a
    Lindelof space is Lindelof, printed p. 194). No complete published proof was located, and the
    two sets that reach the exercise state the method without proving it: Ana Emilia de Orellana,
    printed p. 33, writes "it is very similar to the theorem, regular and second countable imply
    normal, so we just need to know that it has a countable basis, for this consider a cover a in
    B_n inside U_n and use the Lindelof condition"; "Doug's World", printed p. 6, writes "follow the
    same line of argument as with Theorem 32.1 but rely on a countable subcovering of the space in
    lieu of a countable basis". The card's proof is the argument both describe, with the
    checklists A <= U and B <= V carried out: this is the collision check: a point of U_m cap V_n
    lies in closure U_m, which the definition of U_m excludes, when m <= n, and in closure V_n,
    which the definition of V_n excludes, when n <= m. The search is recorded in the
    COMPLAINTS.md entry for this batch.
---

::: {.exercise}

Show that every regular Lindelöf space is normal.
:::

::: {.solution}
Let $A,B\subset X$ be disjoint closed sets. If either is empty, $X$ and $\varnothing$ separate them. Assume both are nonempty. Since $X$ is regular, for each $a\in A$ choose an open $U_a\ni a$ with
$$
\overline{U_a}\cap B=\varnothing.
$$
Because closed subspaces of Lindelöf spaces are Lindelöf, $A$ is Lindelöf. Hence choose a countable family $U_1,U_2,\dots$ covering $A$. Similarly choose open sets $V_1,V_2,\dots$ covering $B$ with
$$
\overline{V_n}\cap A=\varnothing.
$$

Define
$$
U=\bigcup_{n\ge1}\left(U_n\setminus\bigcup_{i=1}^n\overline{V_i}\right),
$$
$$
V=\bigcup_{n\ge1}\left(V_n\setminus\bigcup_{i=1}^n\overline{U_i}\right).
$$
Each is open. Every $a\in A$ belongs to some $U_n$, and $a\notin\overline{V_i}$ for all $i$, so $A\subset U$. Similarly $B\subset V$.

They are disjoint. If $x$ belonged to both, choose $m,n$ such that
$$
x\in U_m\setminus\bigcup_{i\le m}\overline{V_i}
$$
and
$$
x\in V_n\setminus\bigcup_{i\le n}\overline{U_i}.
$$
If $m\le n$, then $x\in U_m\subset\overline{U_m}$, contradicting the second membership; if $n\le m$, then $x\in V_n\subset\overline{V_n}$, contradicting the first. Thus $X$ is normal.
:::
