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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.4, printed pp. 84--85** (`tmp/sources/munkres-solutions-whitman.pdf`); the countable union over degrees and over root sets, and the removal of a countable set from $\RR$, are his.

(a) For each $n\ge1$, let $P_n$ be the set of monic degree-$n$ polynomials with rational coefficients. The coefficient map gives a bijection
$$
P_n\cong\QQ^n.
$$
Since finite products of countable sets are countable, each $P_n$ is countable. Hence
$$
P=\bigcup_{n\ge1}P_n
$$
is countable.

Each polynomial in $P$ has only finitely many real roots. The set $\mathcal A$ of algebraic real numbers is the union, over $p\in P$, of the finite root set of $p$. This is a countable union of finite sets, hence countable.

(b) Let $T$ be the set of transcendental reals. Then
$$
\RR=\mathcal A\cup T.
$$
If $T$ were countable, the right side would be a union of two countable sets and hence countable, contradicting the assumed uncountability of $\RR$. Therefore $T$ is uncountable.
:::
