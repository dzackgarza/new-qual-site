---
schema: qual/card@1
id: P-UCLAB10F-05
kind: problem
title: Span of intersections and unions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Prove or disprove each statement for arbitrary subsets $S,S'$ of a vector space $V$:

(a)
\[
\operatorname{span}(S)\cap\operatorname{span}(S')
=
\operatorname{span}(S\cap S').
\]

(b)
\[
\operatorname{span}(S)+\operatorname{span}(S')
=
\operatorname{span}(S\cup S').
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement (a) is false in general.


::: pf-proof

Take
\[
V=\RR^2,
\qquad
S=\{(1,0)\},
\qquad
S'=\{(2,0)\}.
\]
Then
\[
S\cap S'=\varnothing,
\]
so
\[
\operatorname{span}(S\cap S')
=
\operatorname{span}(\varnothing)
=
\{0\}.
\]
On the other hand,
\[
\operatorname{span}(S)
=
\operatorname{span}(S')
=
\RR(1,0),
\]
so
\[
\operatorname{span}(S)\cap\operatorname{span}(S')
=
\RR(1,0)
\ne
\{0\}.
\]
Thus the claimed equality fails.

:::

:::

::: {.pf-step #s1-2}

One has
\[
\operatorname{span}(S)+\operatorname{span}(S')
\subseteq
\operatorname{span}(S\cup S').
\]


::: pf-proof

Every vector in $\operatorname{span}(S)$ is a finite linear combination of elements of $S$, hence of elements of $S\cup S'$. Thus
\[
\operatorname{span}(S)\subseteq\operatorname{span}(S\cup S').
\]
Similarly,
\[
\operatorname{span}(S')\subseteq\operatorname{span}(S\cup S').
\]
Since the right-hand side is a subspace, it contains every sum of one vector from each of these two subspaces.

:::

:::

::: {.pf-step #s1-3}

One has
\[
\operatorname{span}(S\cup S')
\subseteq
\operatorname{span}(S)+\operatorname{span}(S').
\]


::: pf-proof

The sum
\[
\operatorname{span}(S)+\operatorname{span}(S')
\]
is a subspace of $V$. It contains $S$, because
\[
S\subseteq\operatorname{span}(S),
\]
and it contains $S'$. Hence it contains
\[
S\cup S'.
\]
By minimality of the span, every subspace containing $S\cup S'$ must contain
\[
\operatorname{span}(S\cup S').
\]

:::

:::

::: {.pf-step #s1-4}

Statement (b) is true:
\[
\boxed{
\operatorname{span}(S)+\operatorname{span}(S')
=
\operatorname{span}(S\cup S')
}.
\]


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} prove the two inclusions.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} disproves part (a), and step [](#s1-4){.pf-ref} proves part (b).

:::

:::

:::
