---
schema: qual/card@1
id: P-YJFBZ
kind: problem
title: Zeros of $P_n(z)=\sum_{k=0}^n z^k/k!$ and of $P_n-1$ in $\abs{z}<10$ for large
  $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
  - Uniform Convergence
relations: []
review: draft
---

::: {.problem}
For each $n\in \ZZ^{\geq 1}$, let
$$
P_n(z) = 1 + z + \frac{1}{2!} z^2 + \cdots + \frac{1}{n!}z^n.
$$
Show that for sufficiently large $n$, the polynomial $P_n$ has no zeros in $\abs{z} < 10$, while the polynomial $P_n(z) - 1$ has precisely 3 zeros there.
:::

::: {.solution}
Let $D=\theset{\abs{z}\le10}$.
The partial sums $P_n$ of the exponential series converge to $e^z$ uniformly on $D$.

::: pf

::: pf-step
For large $n$, $P_n$ has no zeros in $D$.

::: pf-proof
On $D$, $\abs{e^z}=e^{\Re z}\ge e^{-10}$. For $n$ with $\sup_D\abs{P_n-e^z}<e^{-10}$, $\abs{P_n(z)}\ge\abs{e^z}-\abs{P_n(z)-e^z}>0$ on $D$.
:::

:::

::: {.pf-step #exp-zeros}
$e^z-1$ has exactly three zeros in $\abs{z}<10$, all simple, and none on $\abs{z}=10$.

::: pf-proof
The zeros of $e^z-1$ are $2\pi ik$, $k\in\ZZ$, all simple since the derivative $e^z$ never vanishes. Since $2\pi<10<4\pi$, those with $\abs{2\pi ik}<10$ are $0$ and $\pm2\pi i$, and none has modulus $10$.
:::

:::

::: pf-step
For large $n$, $P_n-1$ has exactly three zeros in $\abs{z}<10$, counted with multiplicity.

::: pf-proof
By step [](#exp-zeros){.pf-ref}, $\delta\coloneqq\min_{\abs{z}=10}\abs{e^z-1}>0$. For $n$ with $\sup_D\abs{P_n-e^z}<\delta$,
$$
\abs{(P_n(z)-1)-(e^z-1)}<\abs{e^z-1}\qquad(\abs{z}=10),
$$
so by Rouché's theorem $P_n-1$ and $e^z-1$ have the same number of zeros in $\abs{z}<10$, which is $3$ by step [](#exp-zeros){.pf-ref}.
:::

:::

:::

:::
