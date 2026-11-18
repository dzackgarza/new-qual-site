---
schema: qual/card@1
id: P-W5XWA
kind: problem
title: The Banach–Saks theorem in Hilbert space
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Hilbert Spaces
  - Norms
relations: []
review: draft
---

::: {.problem}
Assume that $(x_n)$ is a weakly converging sequence in a Hilbert space $H$.
Show that there is a subsequence $(y_n)$ of $(x_n)$ so that $\frac1n\sum_{j=1}^n y_j$ converges in norm.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Banach–Saks argument follows, with the removal of the weak limit, the inductive choice and the norm computation as separate steps.

Let $(x_{n})$ converge weakly in the Hilbert space $H$.

::: pf

::: {.pf-step #remove}
It suffices to treat the case $x_{n}\rightharpoonup0$; a weakly convergent sequence is bounded.

::: pf-proof
If $x_{n}\rightharpoonup x$, put $x'_{n}=x_{n}-x$; then $x'_{n}\rightharpoonup0$, and a subsequence of $(x'_{n})$ with norm-convergent Cesàro means gives one for $(x_{n})$ with means shifted by $x$. Boundedness is the uniform boundedness principle applied to the functionals $\langle\cdot,x_{n}\rangle$: write $\norm{x_{n}}\le K$.
:::

:::

::: {.pf-step #choose}
There are indices $n_{1}<n_{2}<\cdots$ such that, with $y_{j}=x_{n_{j}}$ and $s_{j-1}=y_{1}+\cdots+y_{j-1}$, one has $\abs{\langle y_{j},s_{j-1}\rangle}<2^{-j}$.

::: pf-proof
Induction: $s_{j-1}$ is determined once $y_{1},\dots,y_{j-1}$ are chosen, and $x_{n}\rightharpoonup0$ means $\langle x_{n},s_{j-1}\rangle\to0$; so all sufficiently large $n$ satisfy the inequality, and we take $n_{j}$ larger than $n_{j-1}$.
:::

:::

::: {.pf-step #norm}
With $S_{n}=\frac{1}{n}\sum_{j\le n}y_{j}$ one has $\norm{S_{n}}^{2}\le\dfrac{K^{2}}{n}+\dfrac{2}{n^{2}}$, so $S_{n}\to0$ in norm.

::: pf-proof
$\norm{S_{n}}^{2}=\frac{1}{n^{2}}\sum_{j,k\le n}\langle y_{j},y_{k}\rangle=\frac{1}{n^{2}}\Big(\sum_{j\le n}\norm{y_{j}}^{2}+2\operatorname{Re}\sum_{j\le n}\langle y_{j},s_{j-1}\rangle\Big)$, the second sum because $\langle y_{j},y_{k}\rangle$ with $k<j$ appears twice. By step [](#remove){.pf-ref} the first sum is at most $nK^{2}$, and by step [](#choose){.pf-ref} the second is at most $2\sum_{j}2^{-j}=2$. Hence $\norm{S_{n}}^{2}\le K^{2}/n+2/n^{2}\to0$.
:::

:::

::: {.pf-qed}
The subsequence $(y_{n})$ of $(x_{n})$ has $\frac1n\sum_{j\le n}y_{j}=S_{n}\to0$ in norm by step [](#norm){.pf-ref}, and in the general case the same means converge in norm to the weak limit $x$.
:::

:::

:::
