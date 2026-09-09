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
Recall
\[
Q_8=\{1,-1,i,-i,j,-j,k,-k\},
\]
with
\[
i^2=j^2=k^2=ijk=-1.
\]

<1>1. The element $-1$ has order $2$.
::: {.proof}
One has
\[
(-1)^2=1
\]
and $-1\ne1$. Hence $|-1|=2$.
:::

<1>2. Each of $\pm i,\pm j,\pm k$ has order $4$.
::: {.proof}
For example,
\[
i^2=-1\ne1,
\qquad
i^4=(-1)^2=1,
\]
so $i$ has order $4$. Also
\[
(-i)^2=i^2=-1,
\]
so $-i$ has order $4$ as well. The same calculation applies to $\pm j$ and $\pm k$.
:::

<1>3. Therefore $-1$ is the unique element of order $2$ in $Q_8$.
::: {.proof}
The identity has order $1$, <1>1 gives order $2$ for $-1$, and <1>2 shows that the remaining six elements all have order $4$.
:::
:::
