---
schema: qual/card@1
id: P-GRECH7-19
kind: problem
title: Which product of intervals is closed in $\RR^2$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 19 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Which of the following sets in $\RR^2$ is closed?

(A) $(2, 5) \times (1, 3)$
(B) $(2, 5] \times [1, 3)$
(C) $[2, 5] \times (1, 3)$
(D) $(2, 5) \times [1, 3]$
(E) $[2, 5] \times [1, 3]$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The set
$$
[2,5]\times[1,3]
$$
is closed in $\RR^2$.


::: pf-proof

The coordinate projections
$$
\pi_1,\pi_2\colon\RR^2\to\RR
$$
are continuous. Therefore
$$
[2,5]\times[1,3]
=\pi_1^{-1}([2,5])\cap\pi_2^{-1}([1,3])
$$
is an intersection of two closed sets, since the intervals $[2,5]$ and $[1,3]$ are closed in $\RR$.

:::

:::

::: {.pf-step #s1-2}

Each of choices (A)--(D) is not closed.


::: pf-proof

For (A), the points $(2+1/n,2)$ lie in the set for all sufficiently large $n$ and converge to $(2,2)$, which is omitted. The same sequence shows that (B) and (D) are not closed. For (C), the points $(3,1+1/n)$ lie in the set and converge to $(3,1)$, which is omitted. Thus each of (A)--(D) fails to contain one of its limit points.

:::

:::

::: {.pf-step #s1-3}

Hence the closed set is
$$
\boxed{[2,5]\times[1,3]},
$$
so the answer is (E).


::: pf-proof

Step [](#s1-1){.pf-ref} proves that choice (E) is closed, while step [](#s1-2){.pf-ref} rules out all other choices.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required choice.

:::

:::

:::
