---
schema: qual/card@1
id: P-TRIV-PR25
kind: problem
title: Monte Carlo integration and its sample size
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 25, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost minus sign in the interval from -1 to 1 and removed stray digits against Probability Problem 25 on pages 30-31 of the source PDF.
---

::: {.problem}
"Monte-Carlo method" Consider the function $f(x_1, \ldots, x_n)$ defined in $V = \{-1 \leqslant x_i \leqslant 1,\ i = 1, \ldots, n\}$ and bounded from below and above, $\abs{f(x_1, \ldots, x_n)} \leqslant C$.
Define a random variable $\eta = f(\xi_1, \ldots, \xi_n)$, where $\xi_i$ are distributed uniformly between $-1$ and $1$.

(a) Show that $\mathbf{E}\eta = I$, where $I = \int_V f(x_1, \ldots, x_n)\, d^n x$.
Hence the random variables can be used to compute the high-dimensional integrals with a given precision.

(b) Consider the series of $N$ random variables $\eta_i = f(\xi_{i1}, \ldots \xi_{in})$, $i = 1, \ldots, N$ where all $\xi_{ij}$ are distributed uniformly in $[-1, 1]$.
Then the quantity $\tilde{I} = \frac{1}{N}(\eta_1 + \ldots + \eta_N)$ for large $N$ approaches $I$ with high enough probability.
Estimate how large $N$ should be to ensure that
$$
P(\abs{\tilde{I} - I} < \Delta) \geqslant 1 - \alpha,
\tag{53}
$$
where $\Delta$ and $\alpha$ are given small numbers.
:::

::: {.solution}

The uniform distribution on the cube $V=[-1,1]^n$ has density $2^{-n}$ with respect to Lebesgue measure.

::: pf

::: {.pf-step #s1-1}

Therefore
$$
\mathbf E\eta
=\frac1{2^n}\int_V f(x)\,d^nx.
$$


::: pf-proof

The joint density of the independent coordinates $\xi_1,\ldots,\xi_n$, each uniform on $[-1,1]$, is the product $(1/2)^n$ on $V$. Thus the expectation of $f(\xi_1,\ldots,\xi_n)$ is the displayed integral against that density.

:::

:::

::: {.pf-step #s1-2}

Consequently, the source's identity $\mathbf E\eta=I$ is missing the volume factor $2^{-n}$ if
$$
I=\int_Vf(x)\,d^nx
$$
is the ordinary Lebesgue integral. The correct identity is
$$
\boxed{I=2^n\mathbf E\eta}.
$$


::: pf-proof

Multiply step [](#s1-1){.pf-ref} by $2^n$. The source's equality becomes correct only if $I$ denotes the normalized integral $2^{-n}\int_Vf$ rather than the integral explicitly printed in the problem.

:::

:::

::: {.pf-step #s1-3}

Accordingly, an unbiased Monte Carlo estimator for the printed integral is
$$
\widehat I=\frac{2^n}{N}\sum_{i=1}^N\eta_i.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} and linearity of expectation,
$$
\mathbf E\widehat I
=2^n\mathbf E\eta
=I.
$$

:::

:::

::: {.pf-step #s1-4}

Since $\abs{\eta_i}\leq C$, one has
$$
\mathbf D\eta_i\leq C^2
$$
and hence
$$
\mathbf D\widehat I
\leq\frac{4^nC^2}{N}.
$$


::: pf-proof

The variance satisfies
$$
\mathbf D\eta_i
=\mathbf E\eta_i^2-(\mathbf E\eta_i)^2
\leq\mathbf E\eta_i^2
\leq C^2.
$$
For independent samples, variances add, so
$$
\mathbf D\left(\frac{2^n}{N}\sum_{i=1}^N\eta_i\right)
=\frac{4^n}{N^2}\sum_{i=1}^N\mathbf D\eta_i
\leq\frac{4^nC^2}{N}.
$$

:::

:::

::: {.pf-step #s1-5}

Chebyshev's inequality gives
$$
P(\abs{\widehat I-I}\geq\Delta)
\leq\frac{4^nC^2}{N\Delta^2}.
$$


::: pf-proof

Apply Chebyshev's inequality to the unbiased estimator from step [](#s1-3){.pf-ref} and use the variance bound in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Thus the sufficient sample size
$$
\boxed{N\geq\frac{4^nC^2}{\alpha\Delta^2}}
$$
ensures
$$
P(\abs{\widehat I-I}<\Delta)\geq1-\alpha.
$$


::: pf-proof

Under the displayed condition, the right side of step [](#s1-5){.pf-ref} is at most $\alpha$. Taking complements gives the desired probability bound.

:::

:::

::: {.pf-step #s1-7}

If instead the intended quantity was the normalized integral
$$
I_{\mathrm{av}}=2^{-n}\int_Vf,
$$
then the source's estimator $\widetilde I=N^{-1}\sum_i\eta_i$ is unbiased and it suffices that
$$
\boxed{N\geq\frac{C^2}{\alpha\Delta^2}}.
$$


::: pf-proof

For the normalized integral, step [](#s1-1){.pf-ref} gives $\mathbf E\eta=I_{\mathrm{av}}$. Repeating steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} without the factor $2^n$ gives variance at most $C^2/N$ and the displayed sample-size bound.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} correct the normalization mismatch in part (a), and steps [](#s1-4){.pf-ref} through [](#s1-7){.pf-ref} give rigorous sample-size estimates for both the printed and normalized interpretations.

:::

:::

:::
