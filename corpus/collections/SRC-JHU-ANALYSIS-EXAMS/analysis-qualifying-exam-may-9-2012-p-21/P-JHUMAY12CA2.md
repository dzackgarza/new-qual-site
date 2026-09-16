---
schema: qual/card@1
id: P-JHUMAY12CA2
kind: problem
title: Unique fixed point of a disk map whose boundary values lie in the open disk
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Suppose $f$ is holomorphic on the open unit disc $D(0,1)$ and continuous on $\overline{D(0,1)}$.
Assume $|f(\xi)| < 1$ for $\xi \in \partial D(0,1)$.
Show that there exists a unique point $a \in D(0,1)$ such that $f(a) = a$.
:::

::: {.solution}
<1>1. The function $g(z)=f(z)-z$ has exactly one zero in the unit disk, counted with multiplicity.
::: {.proof}
On $|z|=1$ the hypothesis gives
$$
|f(z)|<1=|-z|.
$$
Both $f$ and $-z$ are holomorphic on the unit disk and continuous on its closure. Therefore the [[T-CJCKL|Rouché theorem]], applied to
$$
g(z)=(-z)+f(z),
$$
shows that $g$ and $-z$ have the same number of zeros in the disk, counted with multiplicity. The function $-z$ has exactly one zero there, namely the simple zero at $0$. Hence $g$ also has exactly one zero in the disk.
:::

<1>2. The unique zero of $g$ is the unique fixed point of $f$ in the unit disk.
::: {.proof}
For $a\in D(0,1)$,
$$
g(a)=0
\quad\Longleftrightarrow\quad
f(a)=a.
$$
By step <1>1 there is exactly one such zero, so there is exactly one fixed point.
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>2 proves the required existence and uniqueness.
:::
:::
