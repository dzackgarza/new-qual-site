---
schema: qual/card@1
id: P-M2NVE
kind: problem
title: No continuous map $S^2\to S^2$ with $f(x)\perp x$
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 6 of the official UGA Fall 2006 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the explicit homotopy from the identity to the antipodal map and the resulting degree contradiction.
---

::: problem
Prove that there does not exist a continuous map $f:S^2\to S^2$ from the unit sphere in $\RR^3$ to itself such that $f(x)\perp x$ (as vectors in $\RR^3$) for all $x\in S^2$.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that a continuous map
\[
f:S^2\longrightarrow S^2
\]
satisfies
\[
f(x)\perp x
\qquad
(x\in S^2).
\]
:::

<1>2. Define
\[
H:S^2\times[0,1]\longrightarrow\RR^3,
\qquad
H(x,t)=\cos(\pi t)x+\sin(\pi t)f(x).
\]
Then $H(x,t)\in S^2$ for every $(x,t)$.
::: {.proof}
Since both $x$ and $f(x)$ lie on the unit sphere and are orthogonal by <1>1,
\[
\begin{aligned}
\|H(x,t)\|^2
&=\cos^2(\pi t)\|x\|^2
  +\sin^2(\pi t)\|f(x)\|^2
  +2\cos(\pi t)\sin(\pi t)\langle x,f(x)\rangle\\
&=\cos^2(\pi t)+\sin^2(\pi t)\\
&=1.
\end{aligned}
\]
Thus $H$ takes values in $S^2$.
:::

<1>3. The map $H$ is a homotopy from the identity map of $S^2$ to the antipodal map.
::: {.proof}
Continuity follows from continuity of $f$ and of the trigonometric functions.
At the endpoints,
\[
H(x,0)=x
\]
and
\[
H(x,1)=-x.
\]
Hence
\[
\operatorname{id}_{S^2}\simeq a_2,
\qquad
a_2(x)=-x.
\]
:::

<1>4. This homotopy is impossible because the two endpoint maps have different degrees.
::: {.proof}
Degree is invariant under homotopy, so <1>3 would imply
\[
\deg(\operatorname{id}_{S^2})=\deg(a_2).
\]
But
\[
\deg(\operatorname{id}_{S^2})=1,
\]
whereas the antipodal map on $S^n$ has degree
\[
(-1)^{n+1},
\]
and therefore
\[
\deg(a_2)=(-1)^3=-1.
\]
Thus <1>3 would force $1=-1$, a contradiction.
:::

<1>5. Therefore no such continuous map $f:S^2\to S^2$ exists.
::: {.proof}
The assumption in <1>1 led to the contradiction in <1>4.
:::
:::
