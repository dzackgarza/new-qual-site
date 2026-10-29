---
schema: qual/card@1
id: P-UCLARA12F-11
kind: problem
title: Entire functions with one periodic and one quasiperiodic direction
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Find all holomorphic functions $f:\CC\to\CC$ satisfying
$$
f(z+1)=f(z),\qquad f(z+i)=e^{2\pi}f(z)
$$
for every $z\in\CC$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Define
$$
h(z)\coloneqq e^{2\pi i z}f(z).
$$
Then $h$ is entire and satisfies
$$
h(z+1)=h(z),
\qquad
h(z+i)=h(z).
$$


::: pf-proof

The function $h$ is entire because both factors are entire. Using the given relations,
$$
\begin{aligned}
h(z+1)
&=e^{2\pi i(z+1)}f(z+1)\\
&=e^{2\pi iz}f(z)=h(z),
\end{aligned}
$$
and
$$
\begin{aligned}
h(z+i)
&=e^{2\pi i(z+i)}f(z+i)\\
&=e^{2\pi iz-2\pi}e^{2\pi}f(z)\\
&=h(z).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

The function $h$ is bounded on $\CC$.


::: pf-proof

By continuity, $h$ is bounded on the compact fundamental square
$$
Q=\{x+iy:0\le x\le1,\ 0\le y\le1\}.
$$
Every $z\in\CC$ can be translated by integer multiples of $1$ and $i$ into $Q$. By the two periodicity relations from step [](#s1-1){.pf-ref}, $h$ has the same value at $z$ as at the corresponding point of $Q$. Hence the bound on $Q$ is a global bound.

:::

:::

::: {.pf-step #s1-3}

The function $h$ is constant.


::: pf-proof

By step [](#s1-2){.pf-ref}, $h$ is bounded and entire. Liouville's theorem therefore gives
$$
h(z)\equiv C
$$
for some constant $C\in\CC$.

:::

:::

::: {.pf-step #s1-4}

Every solution has the form
$$
\boxed{f(z)=C e^{-2\pi i z}}
$$
for some $C\in\CC$.


::: pf-proof

From step [](#s1-3){.pf-ref} and the definition of $h$,
$$
e^{2\pi iz}f(z)=C,
$$
so
$$
f(z)=Ce^{-2\pi iz}.
$$

:::

:::

::: {.pf-step #s1-5}

Every function of the form $f(z)=Ce^{-2\pi iz}$ satisfies the two required functional equations.


::: pf-proof

Indeed,
$$
f(z+1)
=Ce^{-2\pi i(z+1)}
=f(z),
$$
and
$$
f(z+i)
=Ce^{-2\pi i(z+i)}
=e^{2\pi}f(z).
$$

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} give exactly all solutions.

:::

:::

:::
