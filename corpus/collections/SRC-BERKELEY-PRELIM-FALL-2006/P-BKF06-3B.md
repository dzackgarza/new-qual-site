---
schema: qual/card@1
id: P-BKF06-3B
kind: problem
title: Continuity of $x\mapsto\max_{y\in[0,1]}f(x,y)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained compact-neighborhood uniform
    continuity argument and the symmetric maximum estimate.
---

::: {.problem}
Let $f:\mathbb R\times[0,1]\to\mathbb R$ be continuous.
For $x\in\mathbb R$, define
\[
g(x)=\max\{f(x,y):y\in[0,1]\}.
\]
Show that $g$ is continuous.
:::

::: {.solution}
<1>1. For every $x\in\RR$, the maximum defining $g(x)$ exists.

::: {.proof}
For fixed $x$, the function
$$
y\longmapsto f(x,y)
$$
is continuous on the compact interval $[0,1]$. Hence it attains a
maximum there.
:::

<1>2. Fix $a\in\RR$ and $\epsilon>0$. There exists
$\delta\in(0,1]$ such that
$$
\abs{x-z}<\delta
$$
and $x,z\in[a-1,a+1]$ imply
$$
\abs{f(x,y)-f(z,y)}<\epsilon
$$
for every $y\in[0,1]$.

::: {.proof}
The rectangle
$$
K=[a-1,a+1]\times[0,1]
$$
is compact. The restriction of $f$ to $K$ is therefore uniformly
continuous. Choose a uniform-continuity radius $\delta_0>0$ for
$\epsilon$, and set
$$
\delta=\min\{1,\delta_0\}.
$$
For points $(x,y),(z,y)\in K$, their Euclidean distance is
$\abs{x-z}$. Thus the displayed implication follows.
:::

<1>3. Under the hypotheses of step <1>2,
$$
\abs{g(x)-g(z)}<\epsilon.
$$

::: {.proof}
By step <1>1, choose $y_x\in[0,1]$ with
$$
g(x)=f(x,y_x).
$$
Then step <1>2 gives
$$
g(x)
=
f(x,y_x)
<
f(z,y_x)+\epsilon
\le
g(z)+\epsilon.
$$
Interchanging $x$ and $z$ gives
$$
g(z)<g(x)+\epsilon.
$$
Together these inequalities yield
$$
\abs{g(x)-g(z)}<\epsilon.
$$
:::

<1>4. The function $g$ is continuous at $a$.

::: {.proof}
If $\abs{x-a}<\delta$, where $\delta$ is from step <1>2, then
$x,a\in[a-1,a+1]$. Applying step <1>3 with $z=a$ gives
$$
\abs{g(x)-g(a)}<\epsilon.
$$
This is continuity at $a$.
:::

<1>5. Therefore
$$
\boxed{g\text{ is continuous on }\RR}.
$$

::: {.proof}
The point $a\in\RR$ in step <1>4 was arbitrary.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
