---
schema: qual/card@1
id: P-BKS06-9B
kind: problem
title: Bounded divergent sequence with $\abs{2a_n-a_{n-1}-a_{n+1}}\le n^{-2}$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Find a bounded non-convergent sequence of real numbers $(a_{n})_{n \geq 1}$ such that
$$
\abs{2 a_{n} - a_{n-1} - a_{n+1}} \leq n^{-2}
$$
for all $n \geq 2$.
:::

::: {.solution}

One example is $a_n=f(n)$ with $f(x)=\frac12\sin(\ln(x+1))$.

::: pf

::: {.pf-step #s1}

The sequence $(a_n)$ is bounded and does not converge.

::: pf-proof

$\abs{a_n}\le\frac12$. The numbers $\ln(n+1)$ tend to $\infty$, with increments $\ln\frac{n+2}{n+1}\le\frac1{n+1}<1$. Each interval $[2\pi k+\frac\pi3,2\pi k+\frac{2\pi}3]$ and $[2\pi k+\frac{4\pi}3,2\pi k+\frac{5\pi}3]$ has length $\frac\pi3>1$, so for every large $k$ it contains some $\ln(n+1)$. Hence $a_n\ge\frac{\sqrt3}4$ for infinitely many $n$ and $a_n\le-\frac{\sqrt3}4$ for infinitely many $n$.

:::

:::

::: {.pf-step #s2}

For $n\ge2$, $2a_n-a_{n-1}-a_{n+1}=-f''(\xi)$ for some $\xi\in(n-1,n+1)$.

::: pf-proof

Taylor's theorem gives $f(n\pm1)=f(n)\pm f'(n)+\frac12f''(\xi_\pm)$ with $\xi_+\in(n,n+1)$ and $\xi_-\in(n-1,n)$. Adding, $2a_n-a_{n-1}-a_{n+1}=-\frac12(f''(\xi_+)+f''(\xi_-))$. The average of $f''(\xi_+)$ and $f''(\xi_-)$ is a value $f''(\xi)$ with $\xi$ between them, by the intermediate value theorem.

:::

:::

::: {.pf-step #s3}

For $x>-1$, $\abs{f''(x)}\le(x+1)^{-2}$.

::: pf-proof

$f'(x)=\frac{\cos(\ln(x+1))}{2(x+1)}$ and $f''(x)=-\frac{\cos(\ln(x+1))+\sin(\ln(x+1))}{2(x+1)^2}$, and $\abs{\cos\theta+\sin\theta}\le\sqrt2<2$.

:::

:::

::: pf-qed

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, $\abs{2a_n-a_{n-1}-a_{n+1}}\le(\xi+1)^{-2}<n^{-2}$, because $\xi>n-1$. With step [](#s1){.pf-ref}, this sequence has the required properties.

:::

:::

:::
