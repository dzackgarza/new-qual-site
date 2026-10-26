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
\[
g(x)=\sup\{f(x):f\in\mathcal F\}
\]
is continuous.
:::

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

::: pf-step

Fix $x\in X$ and $\varepsilon>0$. There exists $\delta>0$ such that whenever $\rho(x,y)<\delta$,
$$
\abs{f(x)-f(y)}<\varepsilon
$$
for every $f\in\mathcal F$.


::: pf-proof

This is exactly equicontinuity of the family $\mathcal F$ at the point $x$.

:::

:::

::: pf-step

If $\rho(x,y)<\delta$, with $\delta$ as in step <1>2, then
$$
g(x)\le g(y)+\varepsilon.
$$


::: pf-proof

For every $f\in\mathcal F$, step <1>2 gives
$$
f(x)<f(y)+\varepsilon\le g(y)+\varepsilon.
$$
Taking the supremum over all $f\in\mathcal F$ on the left yields
$$
g(x)\le g(y)+\varepsilon.
$$

:::

:::

::: pf-step

If $\rho(x,y)<\delta$, then
$$
g(y)\le g(x)+\varepsilon.
$$


::: pf-proof

For every $f\in\mathcal F$, step <1>2 also gives
$$
f(y)<f(x)+\varepsilon\le g(x)+\varepsilon.
$$
Taking the supremum over $f\in\mathcal F$ gives the asserted inequality.

:::

:::

::: pf-step

If $\rho(x,y)<\delta$, then
$$
\abs{g(x)-g(y)}\le\varepsilon.
$$


::: pf-proof

Steps <1>3 and <1>4 give
$$
-\varepsilon\le g(x)-g(y)\le\varepsilon,
$$
which is equivalent to the stated bound.

:::

:::

::: pf-qed

The point $x\in X$ and the number $\varepsilon>0$ were arbitrary. Step <1>5 therefore proves that $g$ is continuous at every point of $X$.

:::

:::
