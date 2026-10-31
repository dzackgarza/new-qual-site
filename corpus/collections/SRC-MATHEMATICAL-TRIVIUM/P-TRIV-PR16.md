---
schema: qual/card@1
id: P-TRIV-PR16
kind: problem
title: Sums of independent normal and of independent Poisson random variables
classification:
  areas: [prelim]
  topics:
  - Normal Distribution
  - Poisson Distribution
  - Sums of Random Variables
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 16, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed stray extraction digits against Probability Problem 16 on page 29 of the source PDF.
---

::: {.problem}
Consider two independent random variables $\xi_1$ and $\xi_2$ that are distributed according to the normal distribution with mean values $a_1$, $a_2$ and variances $\sigma_1^2$, $\sigma_2^2$ correspondingly.
Find the distribution of a random variable $\xi_1 + \xi_2$.
Repeat the exercise in case if $\xi_{1,2}$ are distributed according to the Poisson distribution with parameters $\lambda_1$ and $\lambda_2$.
:::

::: {.solution}

Let $S=\xi_1+\xi_2$.

::: pf

::: {.pf-step #s1-1}

If $\xi_i\sim N(a_i,\sigma_i^2)$, then its characteristic function is
$$
\varphi_i(t)=\exp\left(ia_it-\frac12\sigma_i^2t^2\right).
$$


::: pf-proof

This is obtained by completing the square in the Fourier transform of the normal density, or equivalently from the standard-normal characteristic function after the affine transformation $\xi_i=a_i+\sigma_iZ$.

:::

:::

::: {.pf-step #s1-2}

Independence gives
$$
\varphi_S(t)=\varphi_1(t)\varphi_2(t)
=\exp\left(i(a_1+a_2)t
-\frac12(\sigma_1^2+\sigma_2^2)t^2\right).
$$


::: pf-proof

Since $\xi_1$ and $\xi_2$ are independent,
$$
\mathbf E e^{it(\xi_1+\xi_2)}
=\mathbf E e^{it\xi_1}\,\mathbf E e^{it\xi_2}.
$$
Substitute step [](#s1-1){.pf-ref} and combine exponents.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\xi_1+\xi_2\sim
N(a_1+a_2,\sigma_1^2+\sigma_2^2)}.
$$


::: pf-proof

The characteristic function in step [](#s1-2){.pf-ref} is exactly that of the displayed normal distribution, and characteristic functions determine probability distributions uniquely.

:::

:::

::: {.pf-step #s1-4}

If instead $\xi_i\sim\operatorname{Poisson}(\lambda_i)$, then for every integer $n\geq0$,
$$
P(S=n)=\sum_{k=0}^{n}
e^{-\lambda_1}\frac{\lambda_1^k}{k!}
e^{-\lambda_2}\frac{\lambda_2^{n-k}}{(n-k)!}.
$$


::: pf-proof

The disjoint possibilities for $S=n$ are $\xi_1=k$ and $\xi_2=n-k$ for $k=0,\ldots,n$. Independence makes each joint probability the product of the two Poisson probabilities.

:::

:::

::: {.pf-step #s1-5}

The sum in step [](#s1-4){.pf-ref} simplifies to
$$
P(S=n)=e^{-(\lambda_1+\lambda_2)}
\frac{(\lambda_1+\lambda_2)^n}{n!}.
$$


::: pf-proof

Factor out $e^{-(\lambda_1+\lambda_2)}/n!$ and use
$$
\frac{n!}{k!(n-k)!}=\binom nk.
$$
The remaining sum is
$$
\sum_{k=0}^{n}\binom nk
\lambda_1^k\lambda_2^{n-k}
=(\lambda_1+\lambda_2)^n
$$
by the binomial theorem.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{\xi_1+\xi_2\sim
\operatorname{Poisson}(\lambda_1+\lambda_2)}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} is the Poisson mass function with parameter $\lambda_1+\lambda_2$.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-6){.pf-ref} give the two requested sum distributions.

:::

:::

:::
