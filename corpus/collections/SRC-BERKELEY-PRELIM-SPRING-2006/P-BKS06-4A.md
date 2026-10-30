---
schema: qual/card@1
id: P-BKS06-4A
kind: problem
title: Holomorphic functions on the unit disk that are real at $\frac1n+ie^{-n}$
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $D = \{ z \in \CC : \abs{z} < 1 \}$. Find all holomorphic functions $f \colon D \to \CC$ such that $f\left(\frac{1}{n} + i e^{-n}\right)$ is real for all integers $n \geq 2$.
:::

::: {.solution}

The answer is the real constant functions.

::: pf

::: {.pf-step #s1}

If $\varphi(x)=\sum_{k\ge0}b_kx^k$ is a real power series with positive radius of convergence and $\varphi(1/n)=O(e^{-n})$ as $n\to\infty$, then every $b_k$ is $0$.

::: pf-proof

Suppose not, and let $m$ be the least index with $b_m\ne0$. Then $\varphi(x)=x^m(b_m+O(x))$ as $x\to0$, so $\abs{\varphi(1/n)}\ge\abs{b_m}n^{-m}/2$ for all large $n$. Since $n^me^{-n}\to0$, this contradicts $\varphi(1/n)=O(e^{-n})$.

:::

:::

::: {.pf-step #s2}

Let $f(z)=\sum_{k\ge0}a_kz^k$ near $0$, put $z_n=\frac1n+ie^{-n}$, and let $M=\max\{\abs{f''(z)}:\abs{z}\le\frac34\}$. For $n\ge2$,
$$
\abs{f(z_n)-f(\tfrac1n)}\le M'e^{-n},
\qquad
\abs{f(z_n)-f(\tfrac1n)-ie^{-n}f'(\tfrac1n)}\le\tfrac12Me^{-2n},
$$
where $M'=\max\{\abs{f'(z)}:\abs{z}\le\frac34\}$.

::: pf-proof

For $n\ge2$ the segment from $\frac1n$ to $z_n$ lies in the closed disk $\abs{z}\le\frac34$, inside $D$. Integrating $f'$ along it gives the first bound. Taylor's formula with integral remainder, $f(a+h)-f(a)-hf'(a)=\int_0^1(1-s)h^2f''(a+sh)\,ds$, with $a=\frac1n$ and $h=ie^{-n}$, gives the second.

:::

:::

::: {.pf-step #s3}

Every $a_k$ is real.

::: pf-proof

Since $f(z_n)$ is real, the first bound of step [](#s2){.pf-ref} gives $\abs{\operatorname{Im}f(\frac1n)}\le M'e^{-n}$. Now $\operatorname{Im}f(x)=\sum_k(\operatorname{Im}a_k)x^k$ for small real $x$, so step [](#s1){.pf-ref} gives $\operatorname{Im}a_k=0$ for every $k$.

:::

:::

::: {.pf-step #s4}

$f'\equiv0$ near $0$.

::: pf-proof

By step [](#s3){.pf-ref}, $f(\frac1n)$ and $f'(\frac1n)$ are real. Taking imaginary parts in the second bound of step [](#s2){.pf-ref} gives $e^{-n}\abs{f'(\frac1n)}\le\frac12Me^{-2n}$, so $f'(\frac1n)=O(e^{-n})$. The function $f'(x)=\sum_k(k+1)a_{k+1}x^k$ is a real power series by step [](#s3){.pf-ref}, so step [](#s1){.pf-ref} gives $a_{k+1}=0$ for every $k\ge0$.

:::

:::

::: pf-qed

By step [](#s4){.pf-ref} and the identity theorem on the connected set $D$, $f$ is the constant $a_0$, which is real by step [](#s3){.pf-ref}. Conversely, every real constant function takes real values at all points $z_n$.

:::

:::

:::
