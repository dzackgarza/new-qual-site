---
schema: qual/card@1
id: P-BKF00-2
kind: problem
title: A subset on which every continuous real function attains a maximum is compact
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    If A were not closed, a point of its closure outside A would make the
    continuous function given by minus the distance to that point have
    supremum zero on A without attaining it. Thus A is closed in the compact
    space X and hence compact.
---

::: {.problem}
Let $A$ be a subset of a compact metric space $(X,d)$. Assume that for every continuous function
\[
f:X\to\mathbb R,
\]
the restriction $f|_A$ attains a maximum on $A$. Prove that $A$ is compact.
:::

::: {.solution}
<1>1. The subset $A$ is closed in $X$.

<2>1. Suppose for contradiction that $A$ is not closed, and choose
$$
x\in\overline A\setminus A.
$$

::: {.proof}
If $A$ is not closed, then $\overline A\neq A$, so such a point exists.
:::

<2>2. The function
$$
g:X\to\RR,
\qquad
g(y)=-d(y,x),
$$
is continuous.

::: {.proof}
The reverse triangle inequality gives
$$
\abs{d(y,x)-d(z,x)}\leq d(y,z)
$$
for all $y,z\in X$. Thus $y\mapsto d(y,x)$ is $1$-Lipschitz and hence
continuous, so $g$ is continuous.
:::

<2>3. The restriction $g|_A$ has supremum $0$ on $A$ but does not attain
that value.

::: {.proof}
Since $x\notin A$, every $a\in A$ satisfies $d(a,x)>0$, and therefore
$$
g(a)=-d(a,x)<0.
$$
Thus $0$ is an upper bound for $g(A)$ and is not attained.

Because $x\in\overline A$, for every $\varepsilon>0$ there is
$a_\varepsilon\in A$ such that
$$
d(a_\varepsilon,x)<\varepsilon.
$$
Hence
$$
g(a_\varepsilon)>-\varepsilon.
$$
No negative number can therefore be an upper bound for $g(A)$, so
$$
\sup g(A)=0.
$$
Consequently $g|_A$ has no maximum.
:::

<2>4. Q.E.D.

::: {.proof}
Step <2>2 gives a continuous real-valued function on $X$, while step <2>3
shows that its restriction to $A$ does not attain a maximum. This
contradicts the hypothesis, so the assumption in step <2>1 is false.
Therefore $A$ is closed.
:::

<1>2. The subset $A$ is compact.

::: {.proof}
By step <1>1, $A$ is closed in the compact space $X$. Every closed subset
of a compact space is compact.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the required conclusion.
:::
:::
