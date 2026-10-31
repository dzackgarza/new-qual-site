---
schema: qual/card@1
id: E-MUN-9-8
kind: problem
title: The power set of the positive integers has the cardinality of the reals
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: codex
  date: 2026-10-31
  note: Checked the statement and hint against Munkres, Topology, second edition, Section 9, Exercise 8.
---

::: {.problem}
Show that $\mathcal P(\ZZ_+)$ and $\RR$ have the same cardinality.

Hint: Every real number has a decimal expansion, unique when expansions
ending in an infinite string of nines are excluded.
:::

::: {.solution}
For $S\subseteq\ZZ_+$, put
$$
u(S)=\sum_{n\in S}\frac{2}{3^n}\in\RR.
$$
This map is injective. If $S\ne T$ and $m$ is the first integer on which
their membership differs, the difference between their $m$-th terms is
$2/3^m$, while all later terms together have absolute value at most
$$
\sum_{n>m}\frac{2}{3^n}=\frac1{3^m}<\frac2{3^m}.
$$
Thus $u(S)\ne u(T)$.

For an injection in the other direction, map $x\in\RR$ to
$$
t(x)=\frac12\left(1+\frac{x}{1+\abs{x}}\right)\in(0,1).
$$
This map is strictly increasing. Choose the unique decimal expansion of
$t(x)$ that does not end in an infinite string of nines. Encode each
decimal digit by its four-bit binary representation. Concatenating these
blocks gives a binary sequence, and the blocks recover every decimal
digit. Hence this construction injects $\RR$ into $\{0,1\}^\omega$.
By [[E-MUN-7-3]], the latter set is in bijection with
$\mathcal P(\ZZ_+)$. Schroeder--Bernstein now gives
$$
\boxed{\cardinality{\mathcal P(\ZZ_+)}=\cardinality{\RR}}.
$$
:::

::: {.remark}
The continuum hypothesis asks whether a cardinal lies strictly between
$\cardinality{\ZZ_+}$ and $\cardinality{\RR}$. The generalized continuum
hypothesis asks the analogous question between the cardinalities of an
infinite set $A$ and $\mathcal P(A)$. Both statements are independent of
the usual axioms of set theory.
:::
