---
title: Commuting limiting operations
order: 50
topics:
- Uniform Convergence
- Convergence of Functions
---

# Commuting limiting operations

## Double limits

::: {.example title="Iterated limits of a double sequence need not agree"}
For $a_{mn}\coloneqq\frac{n}{n+m}$,
$$
\lim_{m\to \infty}\lim_{n\to\infty} \frac{n}{n + m} = 1 \neq 0 =
\lim_{n\to \infty}\lim_{m\to\infty} \frac{n}{n + m}.
$$

:::

## Suprema and limits

[[PR-LCV2V]]

## Continuity

[[PR-SCTER]]

## Differentiability

[[PR-DWOXP]]

::: {.example title="A differentiable function need not have a continuous derivative"}
$f(x)\coloneqq x^2\sin(1/x)$ for $x\neq0$ and $f(0)\coloneqq0$ is differentiable on $\RR$, and $f'(x) = 2x\sin(1/x)-\cos(1/x)$ has no limit at $0$.
A continuous function need not be differentiable: $\abs x$ is continuous and not differentiable at $0$, and the Weierstrass function is continuous and differentiable nowhere.

:::

## Integrals

[[PR-UZVC3]]

::: {.example title="A pointwise limit of Riemann integrable functions need not be Riemann integrable"}
Let $(q_n)$ enumerate $\QQ\cap[0,1]$ and $f_N\coloneqq\sum_{n\leq N}\chi_{\theset{q_n}}$.
Each $f_N$ has finitely many discontinuities and $\int_0^1 f_N = 0$, but $f_N\to\chi_{\QQ\cap[0,1]}$ pointwise, which is not Riemann integrable.

:::
