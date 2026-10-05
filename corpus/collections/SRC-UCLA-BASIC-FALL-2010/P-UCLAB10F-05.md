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
Problem 5. Prove or disprove each statement for arbitrary subsets $S,S'$ of a vector space $V$:

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
<1>1. Statement (a) is false in general.

::: {.proof}
Take
\[
V=\mathbb R^2,
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
\mathbb R(1,0),
\]
so
\[
\operatorname{span}(S)\cap\operatorname{span}(S')
=
\mathbb R(1,0)
\ne
\{0\}.
\]
Thus the claimed equality fails.
:::

<1>2. One has
\[
\operatorname{span}(S)+\operatorname{span}(S')
\subseteq
\operatorname{span}(S\cup S').
\]

::: {.proof}
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

<1>3. One has
\[
\operatorname{span}(S\cup S')
\subseteq
\operatorname{span}(S)+\operatorname{span}(S').
\]

::: {.proof}
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

<1>4. Statement (b) is true:
\[
\boxed{
\operatorname{span}(S)+\operatorname{span}(S')
=
\operatorname{span}(S\cup S')
}.
\]

::: {.proof}
Steps <1>2 and <1>3 prove the two inclusions.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 disproves part (a), and step <1>4 proves part (b).
:::
:::
