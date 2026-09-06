---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-01
kind: problem
title: Open balls in a metric space are open
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Point-Set Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 1 of the Topology Ph.D. Qualifying Exam dated January 12, 2008 in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: For y in B(x0,epsilon), chose radius epsilon-d(y,x0)>0 and used the triangle inequality to put that entire ball inside B(x0,epsilon).
---

::: {.problem}
If $(X,d)$ is a metric space then $\{x\in X:d(x,x_0)<\epsilon\}$ is said to be the open ball of radius $\epsilon$.
Prove that an open ball is an open set.
:::

::: {.solution}
Let
\[
B(x_0,\epsilon)=\{x\in X:d(x,x_0)<\epsilon\},
\qquad \epsilon>0.
\]

<1>1. Every point $y\in B(x_0,\epsilon)$ is contained in an open ball centered at $y$ that lies inside $B(x_0,\epsilon)$.
::: {.proof}
Fix
\[
y\in B(x_0,\epsilon).
\]
Then
\[
d(y,x_0)<\epsilon,
\]
so
\[
r=\epsilon-d(y,x_0)>0.
\]
Let $z\in B(y,r)$.
By the triangle inequality,
\[
d(z,x_0)
\le d(z,y)+d(y,x_0)
<r+d(y,x_0)
=\epsilon.
\]
Hence
\[
z\in B(x_0,\epsilon).
\]
Thus
\[
B(y,r)\subseteq B(x_0,\epsilon).
\]
:::

<1>2. The ball $B(x_0,\epsilon)$ is open.
::: {.proof}
By <1>1, for every point $y\in B(x_0,\epsilon)$ there is a radius $r>0$ such that
\[
y\in B(y,r)\subseteq B(x_0,\epsilon).
\]
This is exactly the metric-topology criterion for $B(x_0,\epsilon)$ to be open.
:::
:::
