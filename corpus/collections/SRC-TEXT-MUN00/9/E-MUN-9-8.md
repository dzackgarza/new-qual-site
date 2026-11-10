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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §9 Exercise 8, printed p. 61, with the decimal-expansion hint printed there; the card states the exercise and the hint.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.8, printed pp. 106-107 (tmp/sources/munkres-solutions-whitman.pdf). He injects R into P(Z_+) through the Dedekind cut x -> {q in Q : q < x} and P(Z_+) into R through binary expansions, and concludes by Schroeder-Bernstein; the card instead injects P(Z_+) into R by the Cantor-set map S -> sum over S of 2/3^n, whose injectivity it checks by comparing the m-th term with the tail, and R into {0,1}^omega by four-bit blocks of decimal digits, then quotes E-MUN-7-3.
---

::: {.problem}
Show that $\mathcal P(\ZZ_+)$ and $\RR$ have the same cardinality.

Hint: Every real number has a decimal expansion, unique when expansions
ending in an infinite string of nines are excluded.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.8, printed pp. 106--107** (`tmp/sources/munkres-solutions-whitman.pdf`), which uses the Dedekind cuts $x\mapsto\{q\in\QQ:q<x\}$ and binary expansions; the card's two injections are different ones and it checks them directly.

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
