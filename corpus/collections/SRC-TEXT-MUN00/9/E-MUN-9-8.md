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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. The two injections are the card's own; the published solution
    cited on the card (Dan Whitman, Exercise 9.8, printed pp. 106-107) uses Dedekind cuts and
    binary expansions instead, so the card keeps its own argument and says so, and the citation is
    described as not supplying these steps. Each step re-read and the estimates redone by hand: the
    series for u(S) is bounded by 1; at the first index where S and T differ the gap is at least
    2/3^m - 1/3^m > 0; t maps R strictly increasingly into (0,1) with derivative 1/(1+|x|)^2; the
    expansion avoiding an eventual string of nines is unique; four-bit blocks recover the digits;
    and {0,1}^omega is P(Z_+) by characteristic functions, which is E-MUN-7-3. Not claimed: that
    the continuum hypothesis holds or fails, which the remark on the card states is independent.
---

::: {.problem}
Show that $\mathcal P(\ZZ_+)$ and $\RR$ have the same cardinality.

Hint: Every real number has a decimal expansion, unique when expansions
ending in an infinite string of nines are excluded.
:::

::: {.solution}
The argument is the card's own; the published solution cited on it, Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.8, printed pp. 106--107 (`tmp/sources/munkres-solutions-whitman.pdf`), uses Dedekind cuts and binary expansions instead, so the two injections below are checked here directly. The exercise is Munkres, Topology (2000), §9 Exercise 8.

::: pf

::: {.pf-step #u}
The map $u(S)=\sum_{n\in S}\frac{2}{3^{n}}$ is a well-defined injection $\mathcal P(\ZZ_{+})\to\RR$.

:::: pf-proof

::: {.pf-step #converges}
The series converges for every $S$.

::: pf-proof
$0\le\sum_{n\in S}2/3^{n}\le\sum_{n\ge1}2/3^{n}=1$, since the geometric series with ratio $1/3$ sums to $1/2$ and is multiplied by $2$; a bounded series of nonnegative terms converges, and the value lies in $[0,1]$.
:::

:::

::: {.pf-step #injective}
$S\ne T$ implies $u(S)\ne u(T)$.

::: pf-proof
Let $m$ be the least integer in the symmetric difference. Suppose $m\in S$ and $m\notin T$. The $m$-th terms differ by $2/3^{m}$ in favour of $S$, while all later terms together contribute at most $\sum_{n>m}2/3^{n}=2\cdot\frac{1}{3^{m+1}}\cdot\frac{1}{1-1/3}=\frac1{3^{m}}$ in absolute value. So $u(S)-u(T)\ge\frac{2}{3^{m}}-\frac{1}{3^{m}}=\frac{1}{3^{m}}>0$. The other case is symmetric.
:::

:::

:::

:::

::: {.pf-step #t}
The map $t(x)=\frac12\bigl(1+\frac{x}{1+\abs{x}}\bigr)$ is a strictly increasing injection $\RR\to(0,1)$.

::: pf-proof
$x\mapsto\abs{x}$ and $x\mapsto1+\abs{x}>0$ are continuous, $x\mapsto x/(1+\abs{x})$ is strictly increasing (its derivative is $1/(1+\abs{x})^{2}>0$ on each side of $0$ and it is odd), and an affine change of variable preserves strict increase. Its values lie strictly between $0$ and $1$ because $\abs{x/(1+\abs{x})}<1$.
:::

:::

::: {.pf-step #expansion}
Every $x$ determines a unique decimal expansion of $t(x)$ not ending in an infinite string of nines, and hence a binary sequence.

::: pf-proof
$t(x)\in(0,1)$ has a decimal expansion $0.d_{1}d_{2}\dots$ with digits in $\{0,\dots,9\}$; among the expansions of a real number at most two exist and exactly one avoids an eventual string of nines, which singles it out without any choice. Replacing each digit $d_{i}$ by its four-bit binary representation and concatenating gives a sequence in $\{0,1\}^{\omega}$.
:::

:::

::: {.pf-step #injective2}
$x\mapsto$ that binary sequence is injective.

::: pf-proof
The four-bit blocks recover the decimal digits, which by step [](#expansion){.pf-ref} determine $t(x)$, and $t$ is injective by step [](#t){.pf-ref}.
:::

:::

::: {.pf-step #powerset}
$\{0,1\}^{\omega}$ is in bijection with $\mathcal P(\ZZ_{+})$.

::: pf-proof
A subset $S\subseteq\ZZ_{+}$ corresponds to its characteristic function in $\{0,1\}^{\omega}$, and this correspondence is a bijection; equivalently this is [[E-MUN-7-3]].
:::

:::

::: {.pf-step}
$\cardinality{\mathcal P(\ZZ_{+})}=\cardinality{\RR}$.

::: pf-proof
Steps [](#u){.pf-ref} and [](#injective2){.pf-ref} with [](#powerset){.pf-ref} give injections in both directions, and the Schröder--Bernstein theorem gives
$$
\boxed{\cardinality{\mathcal P(\ZZ_+)}=\cardinality{\RR}=2^{\aleph_{0}}.}
$$
:::

:::

:::
:::

::: {.remark}
The continuum hypothesis asks whether a cardinal lies strictly between
$\cardinality{\ZZ_+}$ and $\cardinality{\RR}$. The generalized continuum
hypothesis asks the analogous question between the cardinalities of an
infinite set $A$ and $\mathcal P(A)$. Both statements are independent of
the usual axioms of set theory.
:::
