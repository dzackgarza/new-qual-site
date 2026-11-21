---
schema: qual/card@1
id: E-MUN-7-4
kind: problem
title: Countability of algebraic numbers and uncountability of transcendentals
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 4; the stored statement matches.
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
    Read against Munkres, Topology (2000), §7 Exercise 4, printed p. 51; both parts are
    stored as printed, including the hypothesis that each polynomial equation has
    finitely many roots and that the reals are uncountable.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.4,
    printed pp. 84-85 (tmp/sources/munkres-solutions-whitman.pdf). The count is his:
    the degree-n polynomials with rational coefficients form a countable set, their
    union over n is countable, each has finitely many real roots, and the algebraic
    numbers are the countable union of those finite root sets; (b) then removes a
    countable set from an uncountable one. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two parts, which is what Queue D asks for on this card. Part (a) is proved by three substeps: the countability of the monic rational polynomials, the identification of the algebraic numbers with the union of their finite root sets, and the conclusion; part (b) is the uncountability argument from the assumed uncountability of the reals. The theorems of the section that the argument uses (7.5 for countable unions, 7.6 for finite products) are named, which the prose left implicit. Statement re-read against Munkres, Topology (2000), §7 Exercise 4, printed p. 51, and the argument against Dan Whitman's set, Exercise 7.4, printed pp. 84-85. No statement repair.
---

::: {.exercise}

(a) A real number $x$ is said to be algebraic (over the rationals) if it satisfies some polynomial equation of positive degree

$$
x^n + a_{n-1}x^{n-1} + \dots + a_1 x + a_0 = 0
$$

with rational coefficients $a_{i}$. Assuming that each polynomial equation has only finitely many roots, show that the set of algebraic numbers is countable.

(b) A real number is said to be transcendental if it is not algebraic.
Assuming the reals are uncountable, show that the transcendental numbers are uncountable.
(It is a somewhat surprising fact that only two transcendental numbers are familiar to us: $e$ and $\pi$. Even proving these two numbers transcendental is highly nontrivial.)
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.4, printed pp. 84--85** (`tmp/sources/munkres-solutions-whitman.pdf`); the countable union over degrees and over root sets, and the removal of a countable set from $\RR$, are his. The statement is Munkres, *Topology*, 2nd ed. (2000), §7 Exercise 4, printed p. 51.

::: pf

::: {.pf-step #part-a}
(a) The set $\mathcal A$ of algebraic real numbers is countable.

::: pf-proof

::: {.pf-step #polynomials}
The set $P$ of monic polynomials of positive degree with rational coefficients is countable.

::: pf-proof
For $n\ge1$ let $P_n$ be the set of monic polynomials $x^n+a_{n-1}x^{n-1}+\dots+a_0$ with $a_i\in\QQ$; the coefficient map $x^n+a_{n-1}x^{n-1}+\dots+a_0\mapsto(a_0,\dots,a_{n-1})$ is a bijection $P_n\to\QQ^n$. A finite product of countable sets is countable (Theorem 7.6), so each $P_n$ is countable, and $P=\bigcup_{n\ge1}P_n$ is a countable union of countable sets, hence countable (Theorem 7.5).
:::

:::

::: {.pf-step #algebraic}
$\mathcal A$ is a countable union of finite sets.

::: pf-proof
By the hypothesis of the exercise, each $p\in P$ has only finitely many real roots; write $R(p)$ for that finite set. A real number $x$ is algebraic exactly when $x\in R(p)$ for some $p\in P$, since a polynomial equation of positive degree with rational coefficients may be taken monic by dividing by its leading coefficient, which is rational and nonzero. So $\mathcal A=\bigcup_{p\in P}R(p)$, a countable union indexed by the countable set $P$ of step [](#polynomials){.pf-ref} whose members are finite.
:::

:::

A countable union of finite sets is countable, so $\mathcal A$ is countable by step [](#algebraic){.pf-ref}; this is part (a).
:::

:::

::: {.pf-step #part-b}
(b) The set $T$ of transcendental real numbers is uncountable.

::: pf-proof
$T=\RR-\mathcal A$ by the definition of transcendental, and $\RR=\mathcal A\cup T$. If $T$ were countable, then $\RR$ would be the union of the two countable sets $\mathcal A$ (step [](#part-a){.pf-ref}) and $T$, hence countable, contradicting the uncountability of $\RR$ that the exercise assumes. So $T$ is uncountable; this is part (b).
:::

:::

:::
:::
