---
schema: qual/card@1
id: P-BKF20-8B
kind: problem
title: Conjugacy classes in $S_3$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 class list. Conjugation
    preserves cycle type, and the standard conjugation formula shows all
    transpositions are conjugate and the two 3-cycles are conjugate.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked that the three displayed classes are disjoint, each is closed
    under conjugacy, and together they contain all six elements of S_3.
---

::: {.problem}
Find all conjugacy classes in $S_3$, listing the elements of each class.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Conjugation in $S_3$ preserves cycle type.

::: pf-proof

For $\sigma\in S_3$ and a cycle
$$
\tau=(i_1\,i_2\,\ldots\,i_r),
$$
one has
$$
\sigma\tau\sigma^{-1}
=
(\sigma(i_1)\,\sigma(i_2)\,\ldots\,\sigma(i_r)).
$$
Thus conjugating merely relabels the entries of a cycle and hence
preserves its cycle type.

:::

:::

::: {.pf-step #s2}

The identity forms the conjugacy class
$$
\{1\}.
$$

::: pf-proof

For every $\sigma\in S_3$,
$$
\sigma1\sigma^{-1}=1.
$$

:::

:::

::: {.pf-step #s3}

The three transpositions form one conjugacy class:
$$
\{(12),(13),(23)\}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, every conjugate of a transposition is again a
transposition. Conversely, for any two transpositions
$$
(ij)
\qquad\text{and}\qquad
(rs),
$$
choose $\sigma\in S_3$ with
$$
\sigma(i)=r,
\qquad
\sigma(j)=s.
$$
Then
$$
\sigma(ij)\sigma^{-1}=(rs).
$$
Thus all three transpositions are conjugate.

:::

:::

::: {.pf-step #s4}

The two $3$-cycles form one conjugacy class:
$$
\{(123),(132)\}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, conjugates of a $3$-cycle are $3$-cycles. Moreover,
$$
(23)(123)(23)^{-1}
=
(132),
$$
so the two $3$-cycles are conjugate.

:::

:::

::: {.pf-step #s5}

These are all conjugacy classes of $S_3$.

::: pf-proof

The elements of $S_3$ are exactly
$$
1,\ (12),\ (13),\ (23),\ (123),\ (132).
$$
Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} partition these six elements into three conjugacy
classes. Hence no further classes exist.

:::

:::

::: {.pf-step #s6}

Therefore the conjugacy classes are
$$
\boxed{
\{1\},
\qquad
\{(12),(13),(23)\},
\qquad
\{(123),(132)\}.
}
$$

::: pf-proof

This is the class decomposition established in steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the requested list.

:::

:::

:::
