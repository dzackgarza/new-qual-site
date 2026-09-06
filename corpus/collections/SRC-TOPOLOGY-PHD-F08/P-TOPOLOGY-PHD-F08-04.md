---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-04
kind: problem
title: Continuity of the distance to a subset
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part One, question 4 of the Topology Ph.D. Qualifying Exam
    dated January 17, 2009 in assets/attachments/F08phdtop.pdf. As literally
    written, A must be nonempty for the displayed infimum to define a
    real-valued function.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Rewrote the existing proof under the necessary nonempty hypothesis. The
    triangle inequality gives d(x,A) <= d(x,y)+d(y,A); symmetry yields the
    1-Lipschitz estimate and therefore continuity.
---

::: {.problem}
Let $(X,d)$ be a metric space and let $A\subset X$.
If $x\in X$ define the distance of $x$ to $A$ to be $\inf\{d(x,a):a\in A\}$.
Prove that the real-valued function on $X$ defined by $x\mapsto d(x,A)$ is continuous.
:::

::: {.solution}
The statement is meaningful as a real-valued function when $A\ne\varnothing$, which we assume below.

<1>1. For all $x,y\in X$,
\[
d(x,A)\le d(x,y)+d(y,A).
\]
::: {.proof}
Fix $x,y\in X$.
For every $a\in A$, the triangle inequality gives
\[
d(x,a)\le d(x,y)+d(y,a).
\]
Since
\[
d(x,A)=\inf_{b\in A}d(x,b)\le d(x,a),
\]
we have
\[
d(x,A)\le d(x,y)+d(y,a)
\]
for every $a\in A$.
Thus $d(x,A)$ is a lower bound for the nonempty set
\[
\{d(x,y)+d(y,a):a\in A\}.
\]
It is therefore at most its infimum, namely
\[
d(x,y)+\inf_{a\in A}d(y,a)
=d(x,y)+d(y,A).
\]
:::

<1>2. The distance-to-$A$ function is $1$-Lipschitz:
\[
|d(x,A)-d(y,A)|\le d(x,y)
\]
for all $x,y\in X$.
::: {.proof}
From <1>1,
\[
d(x,A)-d(y,A)\le d(x,y).
\]
Interchanging $x$ and $y$ and using symmetry of the metric gives
\[
d(y,A)-d(x,A)\le d(y,x)=d(x,y).
\]
Together these inequalities are equivalent to
\[
|d(x,A)-d(y,A)|\le d(x,y).
\]
:::

<1>3. The function
\[
f:X\to\mathbb R,
\qquad
f(x)=d(x,A),
\]
is continuous.
::: {.proof}
Let $x\in X$ and let $\varepsilon>0$.
Take
\[
\delta=\varepsilon.
\]
If $d(x,y)<\delta$, then by <1>2,
\[
|f(x)-f(y)|
=|d(x,A)-d(y,A)|
\le d(x,y)
<\delta
=\varepsilon.
\]
Thus $f$ is continuous at every $x\in X$; indeed, the same estimate shows that it is uniformly continuous.
:::
:::
