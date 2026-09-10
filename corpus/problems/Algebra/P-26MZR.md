---
schema: qual/card@1
id: P-26MZR
kind: problem
title: The quaternion group has a unique element of order $2$, namely $-1$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- Show that the Quaternion group has only one element of order 2, namely $-1$.
:::

::: {.solution}
Write
\[
Q_8=\{1,-1,i,-i,j,-j,k,-k\},
\]
with
\[
i^2=j^2=k^2=ijk=-1.
\]

<1>1. The element $-1$ has order $2$.
::: {.proof}
One has $(-1)^2=1$ and $-1\ne1$.
:::

<1>2. Each of $\pm i,\pm j,\pm k$ has order $4$.
::: {.proof}
For $u\in\{i,j,k\}$,
\[
u^2=-1,
\]
so $u^4=1$ but $u^2\ne1$. Also
\[
(-u)^2=u^2=-1,
\]
so $-u$ likewise has order $4$.
:::

<1>3. Hence $-1$ is the unique element of order $2$ in $Q_8$.
::: {.proof}
The eight elements of $Q_8$ are $1,-1,\pm i,\pm j,\pm k$. The identity has order $1$,
$-1$ has order $2$ by <1>1, and all six remaining elements have order $4$ by <1>2.
:::
:::

::: {.solution}
Write
\[
Q_8=\{1,-1,i,-i,j,-j,k,-k\},
\]
with
\[
i^2=j^2=k^2=ijk=-1.
\]

<1>1. The element $-1$ has order $2$.
::: {.proof}
One has $(-1)^2=1$ and $-1\ne1$.
:::

<1>2. Each of $\pm i,\pm j,\pm k$ has order $4$.
::: {.proof}
For $u\in\{i,j,k\}$,
\[
u^2=-1,
\]
so $u^4=1$ but $u^2\ne1$. Also
\[
(-u)^2=u^2=-1,
\]
so $-u$ likewise has order $4$.
:::

<1>3. Hence $-1$ is the unique element of order $2$ in $Q_8$.
::: {.proof}
The eight elements of $Q_8$ are $1,-1,\pm i,\pm j,\pm k$. The identity has order $1$,
$-1$ has order $2$ by <1>1, and all six remaining elements have order $4$ by <1>2.
:::
:::
