---
schema: qual/card@1
id: P-UCLAB18S-12
kind: problem
title: Supremum of an equicontinuous family
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Let $\mathcal F$ be an equicontinuous family of real-valued functions on a compact metric space $X$, with every $f\in\mathcal F$ taking values in $[-1,1]$.
Prove that
$$
g(x)=\sup\{f(x):f\in\mathcal F\}
$$
is continuous.
:::

::: {.solution}

::: pf

::: pf-step

For every $x\in X$, the value $g(x)$ is a finite real number.


::: pf-proof

Every $f\in\mathcal F$ takes values in $[-1,1]$. Hence
$$
-1\le f(x)\le1
$$
for every $f\in\mathcal F$. Therefore the set $\{f(x):f\in\mathcal F\}$ is bounded above, and its supremum satisfies $g(x)\in[-1,1]$.

:::

:::

::: {.pf-step #s1-2}

Fix $x\in X$ and $\varepsilon>0$. There exists $\delta>0$ such that whenever $\rho(x,y)<\delta$,
$$
\abs{f(x)-f(y)}<\varepsilon
$$
for every $f\in\mathcal F$.


::: pf-proof

This is exactly equicontinuity of the family $\mathcal F$ at the point $x$.

:::

:::

::: {.pf-step #s1-3}

If $\rho(x,y)<\delta$, with $\delta$ as in step [](#s1-2){.pf-ref}, then
$$
g(x)\le g(y)+\varepsilon.
$$


::: pf-proof

For every $f\in\mathcal F$, step [](#s1-2){.pf-ref} gives
$$
f(x)<f(y)+\varepsilon\le g(y)+\varepsilon.
$$
Taking the supremum over all $f\in\mathcal F$ on the left yields
$$
g(x)\le g(y)+\varepsilon.
$$

:::

:::

::: {.pf-step #s1-4}

If $\rho(x,y)<\delta$, then
$$
g(y)\le g(x)+\varepsilon.
$$


::: pf-proof

For every $f\in\mathcal F$, step [](#s1-2){.pf-ref} also gives
$$
f(y)<f(x)+\varepsilon\le g(x)+\varepsilon.
$$
Taking the supremum over $f\in\mathcal F$ gives the asserted inequality.

:::

:::

::: {.pf-step #s1-5}

If $\rho(x,y)<\delta$, then
$$
\abs{g(x)-g(y)}\le\varepsilon.
$$


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} give
$$
-\varepsilon\le g(x)-g(y)\le\varepsilon,
$$
which is equivalent to the stated bound.

:::

:::

::: pf-qed

The point $x\in X$ and the number $\varepsilon>0$ were arbitrary. Step [](#s1-5){.pf-ref} therefore proves that $g$ is continuous at every point of $X$.

:::

:::

:::
