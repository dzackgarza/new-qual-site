---
schema: qual/card@1
id: P-BKF13-2B
kind: problem
title: Metric spaces are connected exactly when real-valued continuous images are intervals
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 2B in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked both directions: preservation of connectedness under continuous
    images and the two-valued function arising from a separation.
---

::: {.problem}
Say that a metric space $X$ has property (A) if the image of every continuous function $f:X\to\mathbb R$ is an interval, which may be open, closed or half-open.
Prove that $X$ has property (A) if and only if it is connected.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $X$ is connected, then $X$ has property (A).

::: pf-proof

Let
$$
f:X\longrightarrow\RR
$$
be continuous. A continuous image of a connected space is connected,
so $f(X)$ is a connected subset of $\RR$. The connected subsets of
$\RR$ are exactly the intervals. Hence $f(X)$ is an interval, and
$X$ has property (A).

:::

:::

::: {.pf-step #s2}

If $X$ is disconnected, then $X$ does not have property (A).

::: pf-proof

If $X$ is disconnected, there are nonempty disjoint open sets
$U,V\subseteq X$ with
$$
X=U\cup V.
$$
Since each is the complement of the other, both $U$ and $V$ are also
closed. Define
$$
f(x)
\coloneqq
\begin{cases}
0,&x\in U,\\
1,&x\in V.
\end{cases}
$$
The map $f:X\to\RR$ is continuous because it is constant on the two
clopen pieces $U$ and $V$. Its image is
$$
f(X)=\{0,1\},
$$
which is not an interval. Thus property (A) fails.

:::

:::

::: {.pf-step #s3}

Therefore
$$
\boxed{
X\text{ has property (A)}
\iff
X\text{ is connected}.
}
$$

::: pf-proof

Step [](#s1){.pf-ref} proves that connectedness implies property (A), while step
[](#s2){.pf-ref} proves the contrapositive of the converse.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required equivalence.

:::

:::

:::
