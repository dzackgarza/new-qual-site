---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS5-P3
kind: problem
title: Quotient of $\mathbb R^2$ by concentric circles is homeomorphic to a closed ray
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(May 2013) Define an equivalence relation $\sim$ on $\mathbb R^2$ by $(x_1,y_1)\sim(x_2,y_2)$ if and only if $x_1^2+y_1^2=x_2^2+y_2^2$.

(a) Identify the quotient space $X=\mathbb R^2/{\sim}$ as a familiar space and prove that it is homeomorphic to this familiar space.

(b) Determine whether the natural map $p\colon\mathbb R^2\to X$ is a covering map.
Justify your answer.
:::

::: {.solution}
(a) Define
\[
r:\mathbb R^2\to[0,\infty),
\qquad
r(x,y)=\sqrt{x^2+y^2}.
\]
The fibers of \(r\) are exactly the equivalence classes. Therefore \(r\) factors uniquely through a bijection
\[
\bar r:X=\mathbb R^2/{\sim}\ \longrightarrow[0,\infty)
\]
with \(r=\bar r\circ p\). Since \(p\) is a quotient map and \(r\) is continuous, \(\bar r\) is continuous. Its inverse is
\[
[0,\infty)\to X,
\qquad
t\mapsto p(t,0),
\]
which is continuous as the composite of the continuous inclusion \(t\mapsto(t,0)\) with \(p\). Thus
\[
X\cong[0,\infty).
\]

(b) The quotient map \(p\) is not a covering map. For every \(r>0\), the fiber over the class of radius \(r\) is the circle
\[
p^{-1}([r])=\{(x,y):x^2+y^2=r^2\}.
\]
Fibers of a covering map are discrete subspaces of the total space, but this circle is not discrete. Hence \(p\) cannot be a covering map.
:::
