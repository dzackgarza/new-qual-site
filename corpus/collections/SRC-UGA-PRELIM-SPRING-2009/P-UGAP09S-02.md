---
schema: qual/card@1
id: P-UGAP09S-02
kind: problem
title: Prove $x+1/x$ is continuous at $3$ from the $\varepsilon$-$\delta$ definition
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Prove directly from the $\varepsilon$-$\delta$ definition that
$$
f(x)=x+\frac1x
$$
is continuous at $x=3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If
$$
|x-3|<1,
$$
then
$$
\left|f(x)-f(3)\right|
\le
\frac76|x-3|.
$$


::: pf-proof

The inequality $|x-3|<1$ implies
$$
2<x<4,
$$
so in particular $|x|>2$. Since
$$
f(3)=3+\frac13=\frac{10}{3},
$$
one has
$$
\begin{aligned}
\left|f(x)-f(3)\right|
&=
\left|x-3+\frac1x-\frac13\right|\\
&\le
|x-3|
+\left|\frac{3-x}{3x}\right|\\
&=
|x-3|
\left(1+\frac1{3|x|}\right)\\
&\le
|x-3|
\left(1+\frac16\right)
=
\frac76|x-3|.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

Given $\varepsilon>0$, choose
$$
\boxed{\delta=\min\left\{1,\frac{6\varepsilon}{7}\right\}}.
$$


::: pf-proof

If $|x-3|<\delta$, then $|x-3|<1$, so step [](#s1-1){.pf-ref} applies, and
$$
\left|f(x)-f(3)\right|
\le
\frac76|x-3|
<
\frac76\delta
\le
\varepsilon.
$$
Thus the $\varepsilon$-$\delta$ condition for continuity at $3$ is satisfied.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves directly from the definition that $f$ is continuous at
$x=3$.

:::

:::

:::
