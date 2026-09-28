---
schema: qual/card@1
id: P-BKF89-2
kind: problem
title: A differential inequality forcing a nonnegative function to vanish
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f:[0,1]\to\mathbb R$ be continuously differentiable with $f(0)=0$. Suppose there is a constant $M>0$ such that
\[
0\le f'(x)\le Mf(x)
\qquad(0\le x\le1).
\]
Prove that $f(x)=0$ for all $x\in[0,1]$.
:::

::: {.solution}
<1>1. The function $f$ is nonnegative on $[0,1]$.

::: {.proof}
The inequality
$$
f'(x)\geq0
$$
shows that $f$ is nondecreasing. Since $f(0)=0$,
$$
f(x)\geq0
$$
for every $x\in[0,1]$.
:::

<1>2. Define
$$
h(x)=e^{-Mx}f(x).
$$
Then $h$ is nonincreasing on $[0,1]$.

::: {.proof}
Differentiating gives
$$
h'(x)
=
e^{-Mx}\bigl(f'(x)-Mf(x)\bigr).
$$
The hypothesis $f'(x)\leq Mf(x)$ therefore gives
$$
h'(x)\leq0.
$$
:::

<1>3. One has
$$
h(x)=0
$$
for every $x\in[0,1]$.

::: {.proof}
By step <1>1,
$$
h(x)=e^{-Mx}f(x)\geq0.
$$
By step <1>2 and
$$
h(0)=f(0)=0,
$$
one also has
$$
h(x)\leq h(0)=0
$$
for $x\geq0$. Thus $h(x)=0$ everywhere.
:::

<1>4. Consequently,
$$
\boxed{f(x)=0\quad\text{for all }x\in[0,1]}.
$$

::: {.proof}
Since $e^{-Mx}>0$, step <1>3 implies
$$
f(x)=e^{Mx}h(x)=0.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
