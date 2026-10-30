---
schema: qual/card@1
id: P-EDU3Q
kind: problem
title: $(1+z/n)^n$ converges uniformly to $e^z$ on compact subsets of $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Entire Functions
  - Complex Logarithm
relations: []
review: draft
---

::: {.problem}
Prove that the sequence $\left(1+\frac{z}{n}\right)^{n}$ converges uniformly to $e^{z}$ on compact subsets of $\CC$.

> Hint: $e^{n \log w_{n}}=w_{n}^{n}$ and $e^{z}$ is uniform continuous on compact subsets of $\CC$.

:::

::: {.solution}

Let $K$ be compact, choose $R$ with $\abs{z}\le R$ on $K$, and let $\Log$ be the principal logarithm.

::: pf

::: {.pf-step #logbound}

For $\abs{w}\le\frac12$, $\abs{\Log(1+w)-w}\le\abs{w}^2$.

::: pf-proof

$\Log(1+w)-w=\sum_{k\ge2}\frac{(-1)^{k+1}w^k}{k}$, so its modulus is at most $\frac12\sum_{k\ge2}\abs{w}^k=\frac{\abs{w}^2}{2(1-\abs{w})}\le\abs{w}^2$.

:::

:::

::: {.pf-step #exponent}

For $n\ge2R$ and $z\in K$, $\bigl(1+\frac zn\bigr)^n=e^{a_n(z)}$ with $a_n(z)=n\Log\bigl(1+\frac zn\bigr)$, and $\abs{a_n(z)-z}\le R^2/n$.

::: pf-proof

Here $\abs{z/n}\le\frac12$, so $\Log(1+z/n)$ is defined and $e^{n\Log w}=w^n$ for $w=1+z/n$. Step [](#logbound){.pf-ref} gives $\abs{a_n(z)-z}=n\abs{\Log(1+z/n)-z/n}\le n\abs{z/n}^2\le R^2/n$.

:::

:::

::: pf-qed

For $n\ge2R$ and $z\in K$, Step [](#exponent){.pf-ref} and $\abs{e^\zeta-1}\le e^{\abs\zeta}-1$ give
$$
\abs{\Bigl(1+\frac zn\Bigr)^n-e^z}=\abs{e^z}\,\abs{e^{a_n(z)-z}-1}\le e^R\bigl(e^{R^2/n}-1\bigr),
$$
which tends to $0$ as $n\to\infty$ independently of $z\in K$.

:::

:::

:::
