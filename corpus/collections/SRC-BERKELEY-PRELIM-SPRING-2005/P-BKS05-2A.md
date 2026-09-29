---
schema: qual/card@1
id: P-BKS05-2A
kind: problem
title: Discontinuous additive functions $\RR\to\RR$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained Hamel-basis construction: make
    a Q-linear additive map with f(1)=1 and f(pi)=0; continuity would
    force f(x)=x by density of Q.
---

::: {.problem}
Prove or disprove the statement: Every function $f \colon  { \mathbb { R } } \to  { \mathbb { R } }$ such that $f ( x + y ) =$ $f ( x ) + f ( y )$ for all x and y is continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There exists an additive function $f:\RR\to\RR$ such that
$$
f(1)=1
\qquad\text{and}\qquad
f(\pi)=0.
$$

::: pf-proof

Since $\pi$ is irrational, the set $\{1,\pi\}$ is linearly
independent over $\QQ$. Extend it to a basis $B$ of $\RR$ as a
$\QQ$-vector space. Define a function on the basis by
$$
f(1)=1,
\qquad
f(\pi)=0,
$$
and, for definiteness, $f(b)=0$ for every
$b\in B\setminus\{1,\pi\}$. Extend this assignment $\QQ$-linearly
to all of $\RR$.

The resulting map is $\QQ$-linear, hence additive:
$$
f(x+y)=f(x)+f(y)
$$
for all $x,y\in\RR$.

:::

:::

::: {.pf-step #s2}

The function $f$ from step [](#s1){.pf-ref} is not continuous.

::: pf-proof

For every $q\in\QQ$,
$$
f(q)=qf(1)=q.
$$
Suppose $f$ were continuous. Given any $x\in\RR$, choose a sequence
$(q_n)$ in $\QQ$ with $q_n\to x$. Then
$$
f(x)
=
\lim_{n\to\infty}f(q_n)
=
\lim_{n\to\infty}q_n
=
x.
$$
Thus continuity would force $f(x)=x$ for every $x\in\RR$. In
particular it would give $f(\pi)=\pi$, contradicting
$f(\pi)=0$ from step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

The statement in the problem is false.

::: pf-proof

Step [](#s1){.pf-ref} constructs an additive function $\RR\to\RR$, and step
[](#s2){.pf-ref} shows that it is discontinuous.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the required counterexample.

:::

:::

:::
