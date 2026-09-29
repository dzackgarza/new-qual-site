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

::: pf

::: {.pf-step #A-is-closed}
The subset $A$ is closed in $X$.

::: pf-proof

::: {.pf-step #not-closed-assumption}
Suppose for contradiction that $A$ is not closed, and choose
$$
x\in\overline A\setminus A.
$$

::: pf-proof
If $A$ is not closed, then $\overline A\neq A$, so such a point exists.
:::

:::

::: {.pf-step #g-continuous}
The function
$$
g:X\to\RR,
\qquad
g(y)=-d(y,x),
$$
is continuous.

::: pf-proof
The reverse triangle inequality gives
$$
\abs{d(y,x)-d(z,x)}\leq d(y,z)
$$
for all $y,z\in X$. Thus $y\mapsto d(y,x)$ is $1$-Lipschitz and hence
continuous, so $g$ is continuous.
:::

:::

::: {.pf-step #g-sup-not-attained}
The restriction $g|_A$ has supremum $0$ on $A$ but does not attain
that value.

::: pf-proof
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

:::

::: pf-qed
Step [](#g-continuous){.pf-ref} gives a continuous real-valued function on $X$, while step [](#g-sup-not-attained){.pf-ref}
shows that its restriction to $A$ does not attain a maximum. This
contradicts the hypothesis, so the assumption in step [](#not-closed-assumption){.pf-ref} is false.
Therefore $A$ is closed.
:::

:::

:::

::: {.pf-step #A-is-compact}
The subset $A$ is compact.

::: pf-proof
By step [](#A-is-closed){.pf-ref}, $A$ is closed in the compact space $X$. Every closed subset
of a compact space is compact.
:::

:::

::: pf-qed
Step [](#A-is-compact){.pf-ref} is the required conclusion.
:::

:::

:::
