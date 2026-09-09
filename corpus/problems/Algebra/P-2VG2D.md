---
schema: qual/card@1
id: P-2VG2D
kind: problem
title: The integers form a PID
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Euclidean Domains
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Prove that the integers form a PID.
:::


::: {.solution}
Let $I\subseteq\ZZ$ be an ideal.

<1>1. If $I=0$, then $I=(0)$ is principal.
::: {.proof}
Immediate.
:::

<1>2. Suppose $I\ne0$. Then $I$ contains a least positive integer $d$.
::: {.proof}
Since $I$ contains a nonzero integer, it contains a positive integer after changing sign. The positive elements of $I$ form a nonempty subset of $\NN$, so by well-ordering they have a least element $d>0$.
:::

<1>3. Every element of $I$ is divisible by $d$.
::: {.proof}
Take $a\in I$. By Euclidean division,
\[
a=qd+r,\qquad0\le r<d.
\]
Because $a,d\in I$, also
\[
r=a-qd\in I.
\]
If $r>0$, this contradicts the minimality of $d$. Hence $r=0$, so $d\mid a$.
:::

<1>4. Therefore $I=(d)$.
::: {.proof}
Since $d\in I$, one has $(d)\subseteq I$. By <1>3 every element of $I$ is a multiple of $d$, so $I\subseteq(d)$. Thus equality holds.
:::

<1>5. Hence every ideal of $\ZZ$ is principal, so $\ZZ$ is a PID.
::: {.proof}
Combine <1>1 and <1>4. Since $\ZZ$ is an integral domain, this is exactly the definition of a principal ideal domain.
:::
:::
