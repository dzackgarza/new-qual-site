---
schema: qual/card@1
id: P-BERK97S-04
kind: problem
title: An upper bound on real parts forces two entire functions to be affine-related
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f,g$ be entire functions and suppose there is a real constant $k$ such that
\[
\operatorname{Re}f(z)\le k\operatorname{Re}g(z)
\]
for every $z\in\mathbb C$. Show that there are constants $a,b$ such that
\[
f(z)=ag(z)+b.
\]
:::

::: {.solution}
Define
$$
h\coloneqq f-kg.
$$

<1>1. The function $h$ is entire and satisfies
$$
\Re h(z)\leq0
$$
for every $z\in\CC$.

::: {.proof}
Since $f$ and $g$ are entire and $k$ is constant, $h$ is entire. Because
$k$ is real,
$$
\Re h(z)
=
\Re f(z)-k\Re g(z)
\leq0
$$
by the hypothesis.
:::

<1>2. The entire function $e^h$ is bounded by $1$ in modulus.

::: {.proof}
For every $z\in\CC$,
$$
\abs{e^{h(z)}}
=
e^{\Re h(z)}
\leq1
$$
by step <1>1.
:::

<1>3. The function $h$ is constant.

::: {.proof}
By step <1>2 and Liouville's theorem, $e^h$ is constant. Differentiating
gives
$$
e^{h(z)}h'(z)=0
$$
for every $z\in\CC$. Since the exponential function never vanishes,
$$
h'(z)=0
$$
for every $z$. Hence $h$ is constant on $\CC$.
:::

<1>4. There are constants $a,b\in\CC$ such that
$$
f(z)=ag(z)+b
$$
for every $z\in\CC$.

::: {.proof}
By step <1>3, there is $b\in\CC$ with
$$
h=f-kg=b.
$$
Thus
$$
f=kg+b.
$$
Taking
$$
a=k
$$
gives the required form.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the desired conclusion.
:::
:::
