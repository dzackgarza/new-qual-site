---
schema: qual/card@1
id: P-UGAP11F-01
kind: problem
title: Contrapositive, converse, and deductions from a conditional statement
classification:
  areas: [prelim]
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Assume the following statement is true:

> If Michael got at least $80$ on his final exam, then he passed his history class.

(a) Write the contrapositive.

(b) Write the converse.

(c) What, if anything, can be concluded if Michael's final-exam score was $75$?

(d) What, if anything, can be concluded if Michael passed the course?

(e) What, if anything, can be concluded if Michael failed the course?
:::

::: {.solution}

Let
$$
P=\text{“Michael scored at least $80$ on the final”}
$$
and
$$
Q=\text{“Michael passed the history class.”}
$$
The given statement is
$$
P\Longrightarrow Q.
$$

::: pf

::: {.pf-step #s1-1}

The contrapositive is:

$$
\boxed{
\text{If Michael did not pass the history class, then he scored below $80$ on the final.}}
$$


::: pf-proof

The contrapositive of
$$
P\Longrightarrow Q
$$
is
$$
\neg Q\Longrightarrow\neg P.
$$
Here
$$
\neg Q
$$
means that Michael failed the class, and
$$
\neg P
$$
means that his score was below $80$.

:::

:::

::: {.pf-step #s1-2}

The converse is:

$$
\boxed{
\text{If Michael passed the history class, then he scored at least $80$ on the final.}}
$$


::: pf-proof

The converse of
$$
P\Longrightarrow Q
$$
is
$$
Q\Longrightarrow P.
$$
The converse need not follow from the original implication.

:::

:::

::: {.pf-step #s1-3}

If Michael's final-exam score was $75$, nothing can be concluded about whether he passed the class.


::: pf-proof

A score of $75$ means
$$
\neg P.
$$
The implication
$$
P\Longrightarrow Q
$$
does not imply either
$$
\neg P\Longrightarrow Q
$$
or
$$
\neg P\Longrightarrow\neg Q.
$$
Thus both passing and failing are logically compatible with the given information.

:::

:::

::: {.pf-step #s1-4}

If Michael passed the course, nothing can be concluded about whether his final-exam score was at least $80$.


::: pf-proof

Passing the course means
$$
Q.
$$
Inferring
$$
P
$$
from
$$
Q
$$
would use the converse from step [](#s1-2){.pf-ref}, which is not assumed true.

:::

:::

::: {.pf-step #s1-5}

If Michael failed the course, then his final-exam score was below $80$.


::: pf-proof

Failing the course means
$$
\neg Q.
$$
By the contrapositive in step [](#s1-1){.pf-ref},
$$
\neg Q\Longrightarrow\neg P.
$$
Therefore his score was below $80$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} answer parts (a)--(e), respectively.

:::

:::

:::
