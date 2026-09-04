---
schema: qual/card@1
id: P-ONG5Z
kind: problem
title: A space with a path-connected deformation retract is path-connected
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Connectedness
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 3 of the official UGA Spring 2014 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified that the deformation homotopy supplies paths from arbitrary points of the ambient space into the retract, which concatenate through a path in the retract.
---

::: problem
Suppose that $X \subset Y$ and $X$ is a deformation retract of $Y$.

Show that if $X$ is a path connected space, then $Y$ is path connected.
:::

::: {.solution}
<1>1. Fix a deformation retraction of $Y$ onto $X$.
::: {.proof}
Since $X$ is a deformation retract of $Y$, there are a retraction
\[
r:Y\to X
\]
and a continuous homotopy
\[
H:Y\times[0,1]\to Y
\]
such that
\[
H(y,0)=y,
\qquad
H(y,1)=r(y)
\]
for every $y\in Y$, and
\[
H(x,t)=x
\]
for every $x\in X$ and $t\in[0,1]$.
:::

<1>2. Every point of $Y$ can be joined by a path in $Y$ to a point of $X$.
::: {.proof}
Let $y\in Y$.
Define
\[
\alpha_y:[0,1]\to Y,
\qquad
\alpha_y(t)=H(y,t).
\]
Continuity of $H$ implies that $\alpha_y$ is continuous, and <1>1 gives
\[
\alpha_y(0)=y,
\qquad
\alpha_y(1)=r(y)\in X.
\]
Thus $\alpha_y$ is a path from $y$ to a point of $X$.
:::

<1>3. Any two points of $Y$ can be joined by a path in $Y$.
::: {.proof}
Let $y_0,y_1\in Y$.
By <1>2 there are paths
\[
\alpha_0:y_0\leadsto r(y_0),
\qquad
\alpha_1:y_1\leadsto r(y_1).
\]
Since $X$ is path connected, there is a path
\[
\beta:[0,1]\to X
\]
from $r(y_0)$ to $r(y_1)$.
Composing with the inclusion $X\hookrightarrow Y$, we may regard $\beta$ as a path in $Y$.

Let $\overline{\alpha_1}(t)=\alpha_1(1-t)$ be the reverse of $\alpha_1$.
Then the concatenation
\[
\alpha_0*\beta*\overline{\alpha_1}
\]
is a path in $Y$ from $y_0$ to $y_1$.
:::

<1>4. Therefore $Y$ is path connected.
::: {.proof}
By <1>3, every pair of points of $Y$ is joined by a path in $Y$, which is the definition of path connectedness.
:::
:::
