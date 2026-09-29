---
schema: qual/card@1
id: P-BERK97S-04
kind: problem
title: Entire $f,g$ with $\operatorname{Re}f\le k\operatorname{Re}g$ satisfy $f=ag+b$
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

::: pf

::: {.pf-step #s1}

The function $h$ is entire and satisfies
$$
\Re h(z)\leq0
$$
for every $z\in\CC$.

::: pf-proof

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

:::

::: {.pf-step #s2}

The entire function $e^h$ is bounded by $1$ in modulus.

::: pf-proof

For every $z\in\CC$,
$$
\abs{e^{h(z)}}
=
e^{\Re h(z)}
\leq1
$$
by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

The function $h$ is constant.

::: pf-proof

By step [](#s2){.pf-ref} and Liouville's theorem, $e^h$ is constant. Differentiating
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

:::

::: {.pf-step #s4}

There are constants $a,b\in\CC$ such that
$$
f(z)=ag(z)+b
$$
for every $z\in\CC$.

::: pf-proof

By step [](#s3){.pf-ref}, there is $b\in\CC$ with
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

:::

::: pf-qed

Step [](#s4){.pf-ref} is the desired conclusion.

:::

:::

:::
