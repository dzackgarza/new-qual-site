---
title: Undergraduate review
order: 43
---

# Undergraduate review

## Limits superior

[[D-HOKQD]]

::: {.example title="The supremum and the limit superior differ"}
For $x_n \coloneqq \frac{n+1}{n}$, $\sup_n x_n = x_1 = 2$, while $x_n\to1$, so $\limsup_n x_n = 1$.

:::

## Convergence theorems

[[T-TRW6N]]

[[T-LDJNS]]

[[T-5K3IO]]

## Differentiation

::: {.fact}
Let $f\colon[a,b]\to\RR$.

- If $f$ is monotone, or more generally of bounded variation, then $f'(x)$ exists for almost every $x$ and $\int_a^b\abs{f'} < \infty$.

- The Cantor function has bounded variation and $f'=0$ almost everywhere, but it is not constant, so $f(x) - f(a) = \int_a^x f'$ can fail for $f$ of bounded variation.

- If $f$ is absolutely continuous, then $f(x) = f(a) + \int_a^x f'$ for all $x\in[a,b]$.

- If $f\in L^1([a,b])$, then $F(x) \coloneqq\int_a^x f$ is absolutely continuous and $F' = f$ almost everywhere.

:::

::: {.corollary title="Lebesgue density theorem"}
If $E\subseteq\RR$ is a Lebesgue measurable set of finite measure and $m$ is Lebesgue measure, then for almost every $x\in E$,
$$
\lim_{r\to 0}\frac{m(E\cap B(x,r))}{m(B(x,r))} = 1.
$$

:::

A continuous function $\RR\to\RR$ need not be differentiable at any point: see [[real-analysis/counterexamples-undergraduate#The Weierstrass function|the Weierstrass function]].

## Baire category

[[D-2MJRE]]

[[D-5NODS]]

[[D-GG91S]]

::: {.example}
Every countable subset of $\RR$, such as $\QQ$, is meager, since each point is closed with empty interior.

:::

::: {.fact}
In a topological space $X$:

- a subset of a meager set is meager;

- a countable union of meager sets is meager;

- a countable intersection of residual sets is residual;

- a countable intersection of dense open sets is residual.

If $X$ is a complete metric space, the Baire category theorem states that every residual subset of $X$ is dense, and in particular nonempty.

:::

[[E-QSNCL]]
