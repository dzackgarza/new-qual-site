---
schema: qual/card@1
id: E-MUN-7-8
kind: problem
title: Cardinality of countable subsets of $X^{\omega}$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 8; the stored statement matches. The proof requires a choice principle to choose enumerations simultaneously for all countable subsets, which is stated explicitly in the solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ denote the two-element set $\{0,1\}$ ; let $\mathcal{B}$ be the set of countable subsets of $X^{\omega}$ . Show that $X^{\omega}$ and $\mathcal{B}$ have the same cardinality.
:::

::: {.solution}
Let \(\mathcal B\) be the set of countable subsets of \(X^\omega\), where \(X=\{0,1\}\).

There is an immediate injection
\[
X^\omega\hookrightarrow\mathcal B,
\qquad
x\mapsto\{x\}.
\]

For the opposite direction, use the axiom of choice to choose, for every nonempty \(S\in\mathcal B\), a surjection
\[
e_S:\mathbb Z_+\to S.
\]
(For \(S=\varnothing\), choose a fixed dummy sequence.) Since the range of \(e_S\) is exactly \(S\), distinct subsets give distinct chosen sequences of elements. Thus
\[
S\mapsto e_S
\]
defines an injection
\[
\mathcal B\hookrightarrow (X^\omega)^\omega.
\]

Now
\[
(X^\omega)^\omega
\cong X^{\mathbb Z_+\times\mathbb Z_+}
\cong X^\omega,
\]
because \(\mathbb Z_+\times\mathbb Z_+\) is countably infinite. Hence there is an injection \(\mathcal B\to X^\omega\). Schroeder--Bernstein gives
\[
\boxed{|\mathcal B|=|X^\omega|}.
\]

The simultaneous choice of an enumeration \(e_S\) for every countable \(S\) is a genuine choice step; without an appropriate choice principle this cardinality statement is not provable in this form in ZF alone.
:::
