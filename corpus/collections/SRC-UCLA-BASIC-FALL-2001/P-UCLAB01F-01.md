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
---

::: {.problem}
Let $K$ be a compact set of real numbers and let $f:K\to\mathbb R$ be continuous.
Prove that there exists $x_0\in K$ such that
\[
f(x)\le f(x_0)
\]
for every $x\in K$.
:::

::: {.solution}
As stated, the assertion requires the implicit hypothesis $K\ne\varnothing$: if $K=\varnothing$, there is no point $x_0\in K$. Assume therefore that $K$ is nonempty.

<1>1. The image $f(K)$ is a nonempty compact subset of $\mathbb R$.

::: {.proof}
Because $K\ne\varnothing$, the image $f(K)$ is nonempty. Since $K$ is compact and $f$ is continuous, the continuous-image theorem implies that $f(K)$ is compact in $\mathbb R$.
:::

<1>2. The set $f(K)$ has a largest element.

::: {.proof}
By step <1>1, $f(K)$ is a nonempty compact subset of $\mathbb R$. Hence it is bounded above. Let
\[
M=\sup f(K).
\]
For each positive integer $n$, the definition of supremum gives a point $y_n\in f(K)$ such that
\[
M-\frac1n<y_n\le M.
\]
Thus $y_n\to M$. Compact subsets of $\mathbb R$ are closed, so step <1>1 implies $M\in f(K)$. Therefore $M$ is the largest element of $f(K)$.
:::

<1>3. There exists $x_0\in K$ such that
\[
f(x)\le f(x_0)
\]
for every $x\in K$.

::: {.proof}
By step <1>2, the maximum value $M$ belongs to $f(K)$. Hence there is $x_0\in K$ with
\[
f(x_0)=M.
\]
For every $x\in K$, one has $f(x)\in f(K)$ and therefore
\[
f(x)\le M=f(x_0).
\]
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the required conclusion for every nonempty compact $K$, while the opening observation identifies the empty-set exception in the statement as printed.
:::
:::
