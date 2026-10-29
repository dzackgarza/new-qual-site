---
schema: qual/card@1
id: P-UCLAB01F-01
kind: problem
title: A continuous function on a compact set attains its maximum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the retained UCLA Basic Exam, Fall 2001 PDF.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source printed "a compact set of real numbers", which fails for the empty set. The statement now says nonempty compact set.
---

::: {.problem}
Let $K$ be a nonempty compact set of real numbers and let $f:K\to\RR$ be continuous.
Prove that there exists $x_0\in K$ such that
\[
f(x)\le f(x_0)
\]
for every $x\in K$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The image $f(K)$ is a nonempty compact subset of $\RR$.


::: pf-proof

Because $K\ne\varnothing$, the image $f(K)$ is nonempty. Since $K$ is compact and $f$ is continuous, the continuous-image theorem implies that $f(K)$ is compact in $\RR$.

:::

:::

::: {.pf-step #s1-2}

The set $f(K)$ has a largest element.


::: pf-proof

By step [](#s1-1){.pf-ref}, $f(K)$ is a nonempty compact subset of $\RR$. Hence it is bounded above. Let
\[
M=\sup f(K).
\]
For each positive integer $n$, the definition of supremum gives a point $y_n\in f(K)$ such that
\[
M-\frac1n<y_n\le M.
\]
Thus $y_n\to M$. Compact subsets of $\RR$ are closed, so step [](#s1-1){.pf-ref} implies $M\in f(K)$. Therefore $M$ is the largest element of $f(K)$.

:::

:::

::: {.pf-step #s1-3}

There exists $x_0\in K$ such that
\[
f(x)\le f(x_0)
\]
for every $x\in K$.


::: pf-proof

By step [](#s1-2){.pf-ref}, the maximum value $M$ belongs to $f(K)$. Hence there is $x_0\in K$ with
\[
f(x_0)=M.
\]
For every $x\in K$, one has $f(x)\in f(K)$ and therefore
\[
f(x)\le M=f(x_0).
\]

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
