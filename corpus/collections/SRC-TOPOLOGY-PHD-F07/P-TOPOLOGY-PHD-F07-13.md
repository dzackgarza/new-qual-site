---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-13
kind: problem
title: A pair of maps from S^1 to S^2 are homotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part Two, question 1 of the Topology Ph.D. Qualifying Exam in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used the explicit homotopy H((x,y),t)=(x,y cos(pi t),y sin(pi t)). Its
    squared norm is x^2+y^2=1, and the endpoint maps are exactly f and g.
---

::: {.problem}
Recall that $S^n$ is defined to be $\{(x_1,x_2,\ldots,x_n,x_{n+1})\in\mathbb R^{n+1}\mid x_1^2+x_2^2+\cdots+x_n^2+x_{n+1}^2=1\}$.
We shall be interested in the values $n=1,2$.
Then define $f,g:S^1\to S^2$ by $f(\cos(s),\sin(s))=(\cos(s),\sin(s),0)$ and $g(\cos(s),\sin(s))=(\cos(s),-\sin(s),0)$.
Show that $f$ is homotopic to $g$.
:::

::: {.solution}
Define
\[
H:S^1\times I\longrightarrow S^2
\]
by
\[
H((x,y),t)
=\bigl(x,\,y\cos(\pi t),\,y\sin(\pi t)\bigr).
\]

<1>1. The formula for $H$ takes values in $S^2$.
::: {.proof}
If $(x,y)\in S^1$, then
\[
x^2+y^2=1.
\]
Therefore
\[
\begin{aligned}
\|H((x,y),t)\|^2
&=x^2+y^2\cos^2(\pi t)+y^2\sin^2(\pi t)\\
&=x^2+y^2\bigl(\cos^2(\pi t)+\sin^2(\pi t)\bigr)\\
&=x^2+y^2\\
&=1.
\end{aligned}
\]
Hence $H((x,y),t)\in S^2$ for every $((x,y),t)\in S^1\times I$.
:::

<1>2. The map $H:S^1\times I\to S^2$ is continuous.
::: {.proof}
The coordinate functions
\[
(x,y,t)\longmapsto x,
\qquad
(x,y,t)\longmapsto y\cos(\pi t),
\qquad
(x,y,t)\longmapsto y\sin(\pi t)
\]
are continuous on $S^1\times I$ as restrictions and products of continuous real-valued functions.
Thus the corresponding map into $\mathbb R^3$ is continuous.
By <1>1 its image lies in the subspace $S^2$, so $H$ is continuous as a map to $S^2$.
:::

<1>3. At $t=0$, the map $H$ equals $f$.
::: {.proof}
For $(x,y)\in S^1$,
\[
H((x,y),0)
=\bigl(x,y\cos0,y\sin0\bigr)
=(x,y,0).
\]
Writing $(x,y)=(\cos s,\sin s)$ gives
\[
H((\cos s,\sin s),0)
=(\cos s,\sin s,0)
=f(\cos s,\sin s).
\]
:::

<1>4. At $t=1$, the map $H$ equals $g$.
::: {.proof}
For $(x,y)\in S^1$,
\[
H((x,y),1)
=\bigl(x,y\cos\pi,y\sin\pi\bigr)
=(x,-y,0).
\]
Thus
\[
H((\cos s,\sin s),1)
=(\cos s,-\sin s,0)
=g(\cos s,\sin s).
\]
:::

<1>5. Therefore $f\simeq g$.
::: {.proof}
By <1>2, $H$ is continuous, and <1>3--<1>4 give
\[
H(-,0)=f,
\qquad
H(-,1)=g.
\]
Hence $H$ is a homotopy from $f$ to $g$.
:::
:::
