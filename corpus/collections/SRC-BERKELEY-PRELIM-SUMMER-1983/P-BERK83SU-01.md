---
schema: qual/card@1
id: P-BERK83SU-01
kind: problem
title: The thirteenth root of $21982145917308330487013369$
classification: {areas: [prelim], topics: [Abstract Algebra]}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Direct repeated-squaring arithmetic gives
    89^13=21982145917308330487013369. Since x -> x^13 is strictly
    increasing on positive integers, the given positive integer whose
    thirteenth power is the displayed number is uniquely 89.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained sheet `assets/attachments/Summer83.pdf`: the statement is its Problem 1, and the printed words
    are the card's. The exam, the problem number and the file are now named in the solution's
    opening sentence. Not checked in this pass: the solution, which the edit does not touch.
---

::: {.problem}
The number
$$
21982145917308330487013369
$$
is the thirteenth power of a positive integer. Determine that integer.
:::

::: {.solution}
This is Problem 1 of the Preliminary Exam, Summer 1983, retained in this repository as `assets/attachments/Summer83.pdf`; the statement below is its wording.

::: pf

::: {.pf-step #s1}

One has
$$
89^{13}=21982145917308330487013369.
$$

::: pf-proof

Repeated squaring gives
$$
89^2=7921,
$$
$$
89^4=62742241,
$$
and
$$
89^8=3936588805702081.
$$
Hence
$$
\begin{aligned}
89^{13}
&=
89^8\cdot89^4\cdot89\\
&=
21982145917308330487013369.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The positive integer in the problem is
$$
\boxed{89}.
$$

::: pf-proof

By hypothesis, the displayed number is $m^{13}$ for some positive
integer $m$. Step [](#s1){.pf-ref} shows that it is also $89^{13}$. The function
$$
x\longmapsto x^{13}
$$
is strictly increasing on the positive real numbers, so
$$
m^{13}=89^{13}
$$
implies $m=89$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} gives the requested integer.

:::

:::

:::
