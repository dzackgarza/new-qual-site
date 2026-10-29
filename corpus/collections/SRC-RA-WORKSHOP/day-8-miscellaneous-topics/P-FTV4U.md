---
schema: qual/card@1
id: P-FTV4U
kind: problem
title: "Bounded variation of x sin(1/x) on the unit interval"
classification:
  areas:
  - real-analysis
  topics:
  - Variation
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Define $f \colon [0,1] \to [-1,1]$ by $$f(x)\coloneqq \begin{cases} x\sin\big({\frac{1}{x}}\big) & 0 < x \leq 1 \\ 0 & x = 0 \end{cases}$$ Determine, with justification, whether $f$ is if bounded variation on the interval $[0,1]$.
:::

::: {.solution}

For each $k\geq0$, let $t_k\coloneqq2/((2k+1)\pi)$.

::: pf

::: {.pf-step #s1}

$0<t_{k+1}<t_k<1$, $t_k\to0$, and $f(t_k)=(-1)^kt_k$.

::: pf-proof

The numbers $t_k$ decrease to zero because their denominators increase without bound, and $t_0=2/\pi<1$. Moreover $1/t_k=(2k+1)\pi/2$, so $\sin(1/t_k)=(-1)^k$ and the asserted values follow.

:::

:::

::: {.pf-step #s2}

For every integer $K\geq1$, the partition $0<t_K<t_{K-1}<\cdots<t_0<1$ of $[0,1]$ has variation sum at least $\sum_{k=0}^{K-1}(t_k+t_{k+1})$.

::: pf-proof

By step [](#s1){.pf-ref}, consecutive values $f(t_{k+1})$ and $f(t_k)$ have opposite signs, so
$$
\abs{f(t_k)-f(t_{k+1})}=t_k+t_{k+1}.
$$
The two remaining increments, from $0$ to $t_K$ and from $t_0$ to $1$, are nonnegative.

:::

:::

::: {.pf-step #s3}

The variation sums of these partitions are unbounded as $K\to\infty$.

::: pf-proof

By step [](#s2){.pf-ref}, the sum is at least
$$
\sum_{k=0}^{K-1}(t_k+t_{k+1})
=t_0+2\sum_{k=1}^{K-1}t_k+t_K
\geq\frac4\pi\sum_{k=1}^{K-1}\frac1{2k+1}.
$$
For $k\geq1$, $2k+1\leq3k$, so the right-hand side is at least $\frac4{3\pi}\sum_{k=1}^{K-1}1/k$, which diverges.

:::

:::

::: pf-step

$\boxed{\text{No}}$: $f$ is not of bounded variation on $[0,1]$.

::: pf-proof

Total variation is the supremum of all finite partition variation sums. By step [](#s3){.pf-ref}, those sums are unbounded, so $V_{[0,1]}(f)=\infty$.

:::

:::

:::

:::
