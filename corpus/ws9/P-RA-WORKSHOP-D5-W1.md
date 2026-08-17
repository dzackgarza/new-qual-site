---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-W1
kind: problem
title: 'A function with zero derivative is constant'
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - mean-value-theorem
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(June 1999 #10) Show that if $f$ is differentiable on $(a,b)$ with $f'(x)=0$ on $(a,b)$, then $f$ is constant on $(a,b)$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Fix $x < y$ in $(a,b)$ and apply the mean value theorem.
Proof: $f$ is differentiable on $(a,b)$, hence continuous on $[x,y]$ and differentiable on $(x,y)$.
By MVT there is $\xi \in (x,y)$ with \[f(y) - f(x) = f'(\xi)(y - x) = 0\cdot(y-x) = 0,\] since $f' \equiv 0$ on $(a,b)$.
<1>2. Conclude.
Proof: $f(x) = f(y)$ for all $a < x < y < b$; hence $f$ is constant on $(a,b)$.
<1>3. Q.E.D.
:::
