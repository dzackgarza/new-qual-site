---
schema: qual/card@1
id: P-GREPT-35
kind: problem
title: "Inclusion–exclusion count of students in three courses"
classification:
  areas: [prelim]
  topics:
  - Inclusion-Exclusion
  - Counting
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 35 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
In a survey of $100$ undergraduate math majors at a certain college, the following information is obtained about the courses they are taking during the Spring semester:

$41$ are enrolled in real analysis,

$44$ are enrolled in differential equations,

$48$ are enrolled in linear algebra,

$11$ are enrolled in both real analysis and linear algebra,

$14$ are enrolled in both real analysis and differential equations,

$19$ are enrolled in both differential equations and linear algebra, and

$10$ are not enrolled in any of these three courses.

How many of the students surveyed are enrolled in all three of these courses?

(A) $1$
(B) $2$
(C) $3$
(D) $4$
(E) $5$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Exactly $90$ of the surveyed students are enrolled in at least one of
the three courses.


::: pf-proof

There are $100$ students in the survey and $10$ are enrolled in none of the
three courses, so the union of the three enrollment sets has cardinality
$100-10=90$.

:::

:::

::: {.pf-step #s1-2}

If $n$ is the number enrolled in all three courses, then
$$
\cardinality{R\cup D\cup L}=89+n.
$$


::: pf-proof

By inclusion--exclusion,
$$
\begin{aligned}
\cardinality{R\cup D\cup L}
&=\cardinality{R}+\cardinality{D}+\cardinality{L}\\
&\quad-\cardinality{R\cap D}-\cardinality{R\cap L}-\cardinality{D\cap L}\\
&\quad+\cardinality{R\cap D\cap L}.
\end{aligned}
$$
Substituting the given values gives
$$
41+44+48-14-11-19+n=89+n.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
n=\boxed{1},
$$
so the answer is (A).


::: pf-proof

Equating the union size from step [](#s1-1){.pf-ref} with the expression in step [](#s1-2){.pf-ref} gives
$$
90=89+n,
$$
hence $n=1$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested number of students.

:::

:::

:::
