---
schema: qual/card@1
id: E-SS6.EX-6
kind: problem
title: $1+\frac13+\cdots+\frac1{2n-1}-\frac12\log n\to\frac\gamma2+\log2$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Show that

$$
1 + \frac {1}{3} + \frac {1}{5} + \dots + \frac {1}{2 n - 1} - \frac {1}{2} \log n \rightarrow \frac {\gamma}{2} + \log 2,
$$

where $\gamma$ is Euler’s constant.
:::

::: {.solution}

The argument is the card's own: the odd harmonic sum is expressed through $H_{2n}$ and $H_{n}$, and the Euler asymptotic expansion of $H_{m}$ is inserted.

::: pf

::: {.pf-step #odd}

$\displaystyle 1+\frac13+\cdots+\frac{1}{2n-1}=H_{2n}-\frac12H_{n}$, where $H_{m}=1+\frac12+\cdots+\frac1m$.

::: pf-proof

The even terms of $H_{2n}$ are $\frac12+\frac14+\cdots+\frac{1}{2n}=\frac12\bigl(1+\frac12+\cdots+\frac1n\bigr)=\frac12H_{n}$. Subtracting them from $H_{2n}$ leaves exactly the odd ones $1+\frac13+\cdots+\frac{1}{2n-1}$.

:::

:::

::: {.pf-step #euler}

$H_{m}=\log m+\gamma+o(1)$ as $m\to\infty$, with $\gamma$ Euler's constant.

::: pf-proof

This is the defining asymptotic of Euler's constant: $\gamma=\lim_{m\to\infty}(H_{m}-\log m)$, and $H_{m}-\log m$ converges to $\gamma$ precisely when the difference is $\gamma+o(1)$. Convergence of $H_{m}-\log m$ follows from the comparison of $\sum_{k=1}^{m}\frac1k$ with $\int_{1}^{m}\frac{dt}{t}$, the error $\frac1k-\int_{k}^{k+1}\frac{dt}{t}$ being $O\bigl(1/k^{2}\bigr)$ and summable.

:::

:::

::: {.pf-step #compute}

$H_{2n}-\frac12H_{n}-\frac12\log n=\log2+\frac{\gamma}{2}+o(1)$.

::: pf-proof

By step [](#euler){.pf-ref}, $H_{2n}=\log(2n)+\gamma+o(1)$ and $H_{n}=\log n+\gamma+o(1)$. Substituting,
$$
H_{2n}-\tfrac12H_{n}-\tfrac12\log n=\log(2n)+\gamma-\tfrac12\log n-\tfrac{\gamma}{2}-\tfrac12\log n+o(1),
$$
and $\log(2n)-\frac12\log n-\frac12\log n=\log 2+\log n-\log n=\log2$, while $\gamma-\frac{\gamma}{2}=\frac{\gamma}{2}$.

:::

:::

::: {.pf-step #conclusion}

$\displaystyle 1+\frac13+\cdots+\frac{1}{2n-1}-\frac12\log n\longrightarrow\frac{\gamma}{2}+\log2$.

::: pf-proof

Steps [](#odd){.pf-ref} and [](#compute){.pf-ref} give, for every $n$,
$$
1+\frac13+\cdots+\frac{1}{2n-1}-\tfrac12\log n=H_{2n}-\tfrac12H_{n}-\tfrac12\log n=\log2+\frac{\gamma}{2}+o(1),
$$
so the left side converges:
$$
\boxed{1+\frac13+\cdots+\frac{1}{2n-1}-\frac12\log n\to\frac{\gamma}{2}+\log 2.}
$$

:::

:::

:::

:::
