---
schema: qual/card@1
id: E-KD56B
kind: problem
title: First countability of the lower limit topology and the ordered square
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that $\mathbb{R}_\ell$ and the ordered square satisfy the first countability axiom.
(This result does not, of course, imply that they are metrizable.)
:::

::: {.solution}
For the lower-limit line, the family
\[
\mathcal B_x=\{[x,x+1/n):n\in\mathbb Z_+\}
\]
is a countable neighborhood basis at $x$. Indeed every basic neighborhood $[x,b)$ contains one of these for sufficiently large $n$.

Now let $I_o^2=I\times I$ with dictionary order. We give countable local bases.

If $0<y<1$, then
\[
\left\{\{x\}\times(y-1/n,y+1/n)\cap I^2:n\ge1\right\}
\]
forms a local basis at $(x,y)$ after discarding the finitely many terms that leave $I$.

At a lower endpoint $(x,0)$ with $x>0$, use intervals
\[
\big((x-1/n,1),(x,1/n)\big)
\]
for large $n$ with $x-1/n\ge0$. At an upper endpoint $(x,1)$ with $x<1$, use
\[
\big((x,1-1/n),(x+1/n,0)\big).
\]
Every order interval about the relevant point contains one of these once $n$ is large enough. At the minimum $(0,0)$ use the countable initial rays ending at $(0,1/n)$, and at the maximum $(1,1)$ use the corresponding final rays beginning at $(1,1-1/n)$.

Thus every point of the ordered square has a countable local basis, so it is first countable.
:::
