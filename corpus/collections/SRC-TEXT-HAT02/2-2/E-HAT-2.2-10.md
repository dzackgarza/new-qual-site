---
schema: qual/card@1
id: E-HAT-2.2-10
kind: problem
title: Homology of $S^2$ with equatorial antipodal identification, and $S^3$ with equatorial $S^2$ antipodal identification
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 10; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete degree/cellular proof checked.
---

::: {.problem}
Let $X$ be the quotient space of $S^2$ under the identifications $x \sim -x$ for $x$ in the equator $S^1$.
Compute the homology groups $H_i(X)$.
Do the same for $S^3$ with antipodal points of the equatorial $S^2 \subset S^3$ identified.
:::

::: {.solution}
Let $X_2$ be the quotient of $S^2$ obtained by identifying antipodal points on the equator.

<1>1. The space $X_2$ has a CW structure with one $0$-cell, one $1$-cell, and two $2$-cells, with both $2$-cells attached to the $1$-skeleton $\mathbb{RP}^1\cong S^1$ by maps of degree $2$ up to sign.
::: {.proof}
The quotient equator is $S^1/(x\sim-x)=\mathbb{RP}^1\cong S^1$. The northern and southern open hemispheres descend to two open $2$-cells. On the boundary of either hemisphere the quotient map $S^1\to\mathbb{RP}^1$ is the standard double covering, hence has degree $\pm2$ according to orientation choices.
:::

Thus the cellular chain complex is
\[
0\longrightarrow\mathbb Z^2
\xrightarrow{d_2}\mathbb Z
\xrightarrow{0}\mathbb Z\longrightarrow0,
\qquad
 d_2(a,b)=2a\pm2b.
\]
Therefore
\[
\boxed{
H_i(X_2)\cong
\begin{cases}
\mathbb Z,&i=0,2,\\
\mathbb Z_2,&i=1,\\
0,&\text{otherwise}.
\end{cases}}
\]
Indeed, $\operatorname{im}d_2=2\mathbb Z$ and $\ker d_2\cong\mathbb Z$.

Now let $X_3$ be the quotient of $S^3$ obtained by identifying antipodal points on the equatorial $S^2$.

<1>2. The $2$-skeleton of $X_3$ is $\mathbb{RP}^2$, and the two hemispheres give two $3$-cells attached by the standard covering map
\[
S^2\longrightarrow\mathbb{RP}^2.
\]
::: {.proof}
The equator quotient is exactly $\mathbb{RP}^2$. Each open hemisphere of $S^3$ is a $3$-ball, and its boundary is identified with $\mathbb{RP}^2$ by the antipodal quotient map.
:::

<1>3. The cellular boundary $d_3:\mathbb Z^2\to\mathbb Z$ is zero.
::: {.proof}
For the standard CW structure on $\mathbb{RP}^3$, the attaching map of the $3$-cell is the same quotient map $S^2\to\mathbb{RP}^2$, and its cellular boundary coefficient is
\[
1+(-1)^3=0.
\]
Equivalently, after collapsing $\mathbb{RP}^1$, the attaching map $S^2\to S^2$ has degree zero. Each of the two $3$-cells in $X_3$ has this attaching map, so both columns of $d_3$ vanish.
:::

The cellular chain complex is therefore
\[
0\longrightarrow\mathbb Z^2
\xrightarrow{0}\mathbb Z
\xrightarrow{2}\mathbb Z
\xrightarrow{0}\mathbb Z\longrightarrow0.
\]
Hence
\[
\boxed{
H_i(X_3)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z_2,&i=1,\\
\mathbb Z^2,&i=3,\\
0,&\text{otherwise}.
\end{cases}}
\]
:::
