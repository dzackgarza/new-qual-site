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
<1>1. Conjugation in $S_3$ preserves cycle type.

::: {.proof}
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

<1>2. The identity forms the conjugacy class
$$
\{1\}.
$$

::: {.proof}
For every $\sigma\in S_3$,
$$
\sigma1\sigma^{-1}=1.
$$
:::

<1>3. The three transpositions form one conjugacy class:
$$
\{(12),(13),(23)\}.
$$

::: {.proof}
By step <1>1, every conjugate of a transposition is again a
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

<1>4. The two $3$-cycles form one conjugacy class:
$$
\{(123),(132)\}.
$$

::: {.proof}
By step <1>1, conjugates of a $3$-cycle are $3$-cycles. Moreover,
$$
(23)(123)(23)^{-1}
=
(132),
$$
so the two $3$-cycles are conjugate.
:::

<1>5. These are all conjugacy classes of $S_3$.

::: {.proof}
The elements of $S_3$ are exactly
$$
1,\ (12),\ (13),\ (23),\ (123),\ (132).
$$
Steps <1>2--<1>4 partition these six elements into three conjugacy
classes. Hence no further classes exist.
:::

<1>6. Therefore the conjugacy classes are
$$
\boxed{
\{1\},
\qquad
\{(12),(13),(23)\},
\qquad
\{(123),(132)\}.
}
$$

::: {.proof}
This is the class decomposition established in steps <1>2--<1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested list.
:::
:::
