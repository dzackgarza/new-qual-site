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

::: {.problem}
Prove that there does not exist a continuous map $f:S^2\to S^2$ from the unit sphere in $\RR^3$ to itself such that $f(x)\perp x$ (as vectors in $\RR^3$) for all $x\in S^2$.
:::

::: {.solution}

::: pf

::: {.pf-step #assume-orthogonal-map}
Suppose, for contradiction, that a continuous map
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

::: {.pf-step #homotopy-well-defined}
Define
\[
H:S^2\times[0,1]\longrightarrow\RR^3,
\qquad
H(x,t)=\cos(\pi t)x+\sin(\pi t)f(x).
\]
Then $H(x,t)\in S^2$ for every $(x,t)$.

::: pf-proof
Since both $x$ and $f(x)$ lie on the unit sphere and are orthogonal by step [](#assume-orthogonal-map){.pf-ref},
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

:::

::: {.pf-step #identity-homotopic-to-antipodal}
The map $H$ is a homotopy from the identity map of $S^2$ to the antipodal map.

::: pf-proof
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

:::

::: {.pf-step #homotopy-impossible}
This homotopy is impossible because the two endpoint maps have different degrees.

::: pf-proof
Degree is invariant under homotopy, so step [](#identity-homotopic-to-antipodal){.pf-ref} would imply
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
Thus step [](#identity-homotopic-to-antipodal){.pf-ref} would force $1=-1$, a contradiction.
:::

:::

::: pf-step
Therefore no such continuous map $f:S^2\to S^2$ exists.

::: pf-proof
The assumption in step [](#assume-orthogonal-map){.pf-ref} led to the contradiction in step [](#homotopy-impossible){.pf-ref}.
:::

:::

:::

:::
