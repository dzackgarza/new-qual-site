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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §7 Exercise 8, printed p. 52; the stored
    statement matches, with B the set of countable subsets of X^omega.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.8,
    printed pp. 90-92 (tmp/sources/munkres-solutions-whitman.pdf). His two injections are
    the card's: singletons into the power set, and the passage from a countable subset to
    a chosen enumeration of it, which lands in (X^omega)^omega and then in X^omega because
    omega x omega is countably infinite. He also flags the choice used, as the card does.
---

::: {.exercise}

Let $X$ denote the two-element set $\{0,1\}$ ; let $\mathcal{B}$ be the set of countable subsets of $X^{\omega}$ . Show that $X^{\omega}$ and $\mathcal{B}$ have the same cardinality.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.8, printed pp. 90--92** (`tmp/sources/munkres-solutions-whitman.pdf`); the two injections and the choice of an enumeration for each countable subset are his, and so is the remark that the choice step is genuine.

Let $\mathcal B$ be the set of countable subsets of $X^\omega$, where $X=\{0,1\}$.

There is an immediate injection
$$
X^\omega\hookrightarrow\mathcal B,
\qquad
x\mapsto\{x\}.
$$

For the opposite direction, use the axiom of choice to choose, for every nonempty $S\in\mathcal B$, a surjection
$$
e_S:\ZZ_+\to S.
$$
Fix one sequence $e_\varnothing\in(X^\omega)^\omega$. Since the range of
$e_S$ is exactly $S$, distinct nonempty subsets give distinct chosen
sequences of elements. Tag the empty subset separately. Thus
$$
S\mapsto
\begin{cases}
(0,e_\varnothing),&S=\varnothing,\\
(1,e_S),&S\ne\varnothing
\end{cases}
$$
defines an injection
$$
\mathcal B\hookrightarrow X\times(X^\omega)^\omega.
$$

Now
$$
X\times(X^\omega)^\omega
\cong X^{\{0\}\sqcup(\ZZ_+\times\ZZ_+)}
\cong X^\omega,
$$
because $\{0\}\sqcup(\ZZ_+\times\ZZ_+)$ is countably infinite. Hence there is an injection $\mathcal B\to X^\omega$. Schroeder--Bernstein gives
$$
\boxed{\cardinality{\mathcal B}=\cardinality{X^\omega}}.
$$

The simultaneous choice of an enumeration $e_S$ for every countable $S$ is a genuine choice step; without an appropriate choice principle this cardinality statement is not provable in this form in ZF alone.
:::
