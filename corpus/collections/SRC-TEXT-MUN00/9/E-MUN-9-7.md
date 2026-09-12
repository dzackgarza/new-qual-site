---
schema: qual/card@1
id: E-MUN-9-7
kind: problem
title: Strict cardinality ordering and the continuum
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $A$ and $B$ be two nonempty sets.
If there is an injection of $B$ into $A$, but no injection of $A$ into $B$, we say that $A$ has greater cardinality than $B$ .

(a) Conclude from Theorem 9.1 that every uncountable set has greater cardinality than $\mathbb{Z}_{+}$ .

(b) Show that if $A$ has greater cardinality than $B$, and $B$ has greater cardinality than $C$, then $A$ has greater cardinality than $C$ .

(c) Find a sequence $A_1, A_2, \ldots$ of infinite sets, such that for each $n \in \mathbb{Z}_+$, the set $A_{n+1}$ has greater cardinality than $A_n$ .

(d) Find a set that for every $n$ has cardinality greater than $A_{n}$ .

\*8. Show that $\mathcal{P}(\mathbb{Z}_{+})$ and $\mathbb{R}$ have the same cardinality.
[Hint: You may use the fact that every real number has a decimal expansion, which is unique if expansions that end in an infinite string of 9's are forbidden.]

A famous conjecture of set theory, called the continuum hypothesis, asserts that there exists no set having greater cardinality than $Z_{+}$ and lesser cardinality than R. The generalized continuum hypothesis asserts that, given the infinite set A, there is no set having greater cardinality than A and lesser cardinality than $\mathcal{P}(A)$ . Surprisingly enough, both of these assertions have been shown to be independent of the usual axioms for set theory.
For a readable expository account, see [Sm].
:::

::: {.solution}
(a) Let \(A\) be uncountable. Since \(A\) is infinite, Theorem 9.1 gives an injection
\[
\mathbb Z_+\hookrightarrow A.
\]
There cannot be an injection \(A\hookrightarrow\mathbb Z_+\), for then \(A\) would be countable by Theorem 7.1. Hence \(A\) has greater cardinality than \(\mathbb Z_+\).

(b) Suppose \(A\) has greater cardinality than \(B\), and \(B\) greater cardinality than \(C\). There are injections
\[
C\hookrightarrow B\hookrightarrow A,
\]
so there is an injection \(C\hookrightarrow A\). If there were an injection \(A\hookrightarrow C\), composing with \(C\hookrightarrow B\) would give an injection \(A\hookrightarrow B\), contradicting that \(A\) has greater cardinality than \(B\). Thus \(A\) has greater cardinality than \(C\).

(c) Let
\[
A_1=\mathbb Z_+,
\qquad
A_{n+1}=\mathcal P(A_n).
\]
The map \(a\mapsto\{a\}\) injects \(A_n\) into \(A_{n+1}\), while Cantor's theorem says there is no injection \(A_{n+1}\to A_n\). Hence \(A_{n+1}\) has greater cardinality than \(A_n\) for every \(n\).

(d) Set
\[
A=\bigcup_{n\ge1}A_n.
\]
Each \(A_n\) injects into \(A\) by inclusion. For a fixed \(n\), if there were an injection \(A\to A_n\), then restricting it to the subset \(A_{n+1}\subset A\) would give an injection \(A_{n+1}\to A_n\), contradicting part (c). Hence \(A\) has greater cardinality than every \(A_n\).

For the starred Exercise 8, we show
\[
|\mathcal P(\mathbb Z_+)|=|\mathbb R|.
\]
An injection \(\mathcal P(\mathbb Z_+)\to\mathbb R\) is given by the ternary expansion
\[
S\longmapsto \sum_{n\in S}\frac{2}{3^n}.
\]
Only the digits \(0\) and \(2\) occur, so distinct subsets give distinct ternary expansions and hence distinct real numbers.

Conversely, use the stated decimal-expansion fact, choosing for each real the unique decimal expansion not ending in an infinite string of \(9\)'s. Encode its sign, finite integer part, decimal point, and infinite digit sequence by a binary sequence; for example, encode each decimal digit by a fixed four-bit block and separate the finite sign/integer prefix from the fractional tail by a fixed delimiter. This gives an injection
\[
\mathbb R\hookrightarrow\{0,1\}^\omega.
\]
By the characteristic-function bijection of Exercise 7.3,
\[
\{0,1\}^\omega\cong\mathcal P(\mathbb Z_+).
\]
Thus there are injections both ways, and Schroeder--Bernstein yields
\[
\boxed{|\mathcal P(\mathbb Z_+)|=|\mathbb R|}.
\]
:::
