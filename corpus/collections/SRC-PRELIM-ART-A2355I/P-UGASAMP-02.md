---
schema: qual/card@1
id: P-UGASAMP-02
kind: problem
title: Continuity at a point and continuity of $x^2$ at $2$
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
Let $a\in\RR$ and let $I$ be an open interval containing $a$. For a function $f:I\to\RR$, give the definition of continuity at $a$. Prove that
$$
f(x)=x^2
$$
is continuous at $a=2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A function $f:I\to\RR$ is continuous at $a\in I$ if for every $\varepsilon>0$ there exists $\delta>0$ such that, for every $x\in I$,
$$
\abs{x-a}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(a)}<\varepsilon.
$$


::: pf-proof

This is the $\varepsilon$--$\delta$ definition of continuity at a point.

:::

:::

::: {.pf-step #s1-2}

If $\abs{x-2}<1$, then
$$
\abs{x+2}<5.
$$


::: pf-proof

The inequality $\abs{x-2}<1$ implies
$$
1<x<3.
$$
Hence
$$
3<x+2<5,
$$
so $\abs{x+2}<5$.

:::

:::

::: {.pf-step #s1-3}

Given $\varepsilon>0$, set
$$
\delta=\min\left\{1,\frac{\varepsilon}{5}\right\}.
$$
If $\abs{x-2}<\delta$, then
$$
\abs{x^2-4}<\varepsilon.
$$


::: pf-proof

Since $\delta\le1$, the hypothesis $\abs{x-2}<\delta$ implies $\abs{x-2}<1$. By step [](#s1-2){.pf-ref},
$$
\abs{x+2}<5.
$$
Therefore
$$
\abs{x^2-4}
=
\abs{x-2}\,\abs{x+2}
<
5\abs{x-2}
<
5\delta
\le
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-4}

The function $f(x)=x^2$ is continuous at $2$.


::: pf-proof

Step [](#s1-3){.pf-ref} verifies the definition in step [](#s1-1){.pf-ref} with $a=2$ and $f(2)=4$. Thus
$$
\boxed{f(x)=x^2\text{ is continuous at }2.}
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition, and step [](#s1-4){.pf-ref} proves the required continuity.

:::

:::

:::
