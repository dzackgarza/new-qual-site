---
schema: qual/card@1
id: P-UCLAB13F-04
kind: problem
title: Vanishing integrals over rational squares force a function to vanish
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Let $f:\mathbb R^2\to\mathbb R$ be continuous. Assume that for every square
\[
S=\left\{a<x<a+\frac1n,\ b<y<b+\frac1n\right\},
\]
where $a,b\in\mathbb Q$ and $n\ge1$,
\[
\iint_S f(x,y)\,dx\,dy=0.
\]
Prove that $f(x,y)=0$ for all $(x,y)\in\mathbb R^2$.
:::

::: {.solution}
<1>1. Suppose there exists a point
\[
p=(x_0,y_0)
\]
such that
\[
f(p)>0.
\]
Then there is a nonempty open rectangle $U$ on which
\[
f>0.
\]

::: {.proof}
By continuity of $f$ at $p$, choose $\delta>0$ such that
\[
|f(x,y)-f(p)|
<
\frac12f(p)
\]
whenever
\[
\|(x,y)-p\|<\delta.
\]
Then on the open ball $B(p,\delta)$,
\[
f(x,y)>\frac12f(p)>0.
\]
Choose a nonempty open axis-parallel rectangle
\[
U\subseteq B(p,\delta).
\]
:::

<1>2. Every nonempty open rectangle in $\mathbb R^2$ contains a square of the form
\[
S=
\left\{
a<x<a+\frac1n,
b<y<b+\frac1n
\right\}
\]
with
\[
a,b\in\mathbb Q,
\qquad
n\in\mathbb N.
\]

::: {.proof}
Write
\[
U=(\alpha,\beta)\times(\gamma,\eta).
\]
Choose rational numbers
\[
a\in(\alpha,\beta),
\qquad
b\in(\gamma,\eta).
\]
Since
\[
\beta-a>0
\qquad\text{and}\qquad
\eta-b>0,
\]
choose $n$ sufficiently large that
\[
\frac1n
<
\min\{\beta-a,\eta-b\}.
\]
Then the square with lower-left corner $(a,b)$ and side length $1/n$ lies in $U$.
:::

<1>3. The assumption
\[
f(p)>0
\]
is impossible.

::: {.proof}
Take the square $S\subseteq U$ supplied by step <1>2.
By step <1>1,
\[
f(x,y)>0
\]
for every $(x,y)\in S$.
Since $f$ is continuous and $S$ has positive area,
\[
\iint_S f(x,y)\,dx\,dy>0.
\]
But $S$ is one of the squares covered by the hypothesis, so its integral must be $0$.
This contradiction rules out $f(p)>0$.
:::

<1>4. There is no point $p$ with
\[
f(p)<0.
\]

::: {.proof}
If
\[
f(p)<0,
\]
the same continuity argument gives a nonempty open rectangle on which $f<0$.
Step <1>2 then gives an allowed rational square $S$ contained in that rectangle, and
\[
\iint_S f(x,y)\,dx\,dy<0,
\]
again contradicting the hypothesis.
:::

<1>5. Therefore
\[
\boxed{f(x,y)=0}
\]
for every $(x,y)\in\mathbb R^2$.

::: {.proof}
At each point, steps <1>3--<1>4 rule out both positive and negative values.
The only remaining value is $0$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
