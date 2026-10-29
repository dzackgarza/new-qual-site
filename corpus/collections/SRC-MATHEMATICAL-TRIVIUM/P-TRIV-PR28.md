---
schema: qual/card@1
id: P-TRIV-PR28
kind: problem
title: Chi-squared test of a Poisson fit to a cosmic-ray spectrum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 28, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the garbled spectrum table, including the 80-90 MeV bin, against Probability Problem 28 on page 31 of the source PDF.
---

::: {.problem}
In an experiment on the detection of cosmic rays a detector counts particles with different energies coming from different directions.
The observed spectrum of the particles is shown in table below.

| Energy, MeV | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 | 80-90 |
|---|---|---|---|---|---|---|---|---|---|
| # of p. | 15 | 71 | 75 | 68 | 39 | 17 | 10 | 4 | 1 |

At the significance level 0.05, test the hypothesis that the particle spectrum is distributed according to the Poisson distribution with parameter $\lambda$.
Find the effective estimate for $\lambda$.
:::

::: {.solution}

Interpret the nine successive 10-MeV bins as the Poisson count values $0,1,\ldots,8$. The observed frequencies are
$$
(15,71,75,68,39,17,10,4,1),
$$
with total sample size $300$.

::: pf

::: {.pf-step #s1-1}

The maximum-likelihood estimate of the Poisson parameter is the sample mean,
$$
\widehat\lambda
=\frac{\sum_{k=0}^{8}kO_k}{300}
=\boxed{2.54}.
$$


::: pf-proof

For independent Poisson observations $X_1,\ldots,X_N$, the log-likelihood is
$$
\ell(\lambda)
=-N\lambda+\left(\sum_iX_i\right)\log\lambda
-\sum_i\log(X_i!).
$$
Its derivative vanishes at $\widehat\lambda=N^{-1}\sum_iX_i$. From the frequency table,
$$
\sum_{k=0}^8kO_k=762,
$$
so $\widehat\lambda=762/300=2.54$.

:::

:::

::: {.pf-step #s1-2}

Under the fitted Poisson law, the expected frequencies for $k=0,\ldots,5$ are approximately
$$
(23.660,60.096,76.322,64.619,41.033,20.845).
$$


::: pf-proof

For each $k$,
$$
E_k=300e^{-2.54}\frac{2.54^k}{k!}.
$$
Evaluating this expression for $k=0,\ldots,5$ gives the displayed values.

:::

:::

::: {.pf-step #s1-3}

Pool the tail $k\geq6$. Its observed and expected frequencies are
$$
O_{\geq6}=15,
\qquad
E_{\geq6}
=300\left(1-\sum_{k=0}^{5}e^{-2.54}\frac{2.54^k}{k!}\right)
\approx13.424.
$$


::: pf-proof

The observed tail is $10+4+1=15$. Pooling is required because the separate fitted expectations for the higher cells fall below the usual chi-squared approximation threshold. The expected tail is the complement of the fitted probabilities through $k=5$.

:::

:::

::: {.pf-step #s1-4}

Pearson's chi-squared statistic for the seven resulting cells is
$$
\chi^2
=\sum\frac{(O-E)^2}{E}
\approx\boxed{6.343}.
$$


::: pf-proof

Using the six cells in step [](#s1-2){.pf-ref} and the pooled tail in step [](#s1-3){.pf-ref} gives
$$
\chi^2
=\sum_{k=0}^{5}\frac{(O_k-E_k)^2}{E_k}
+\frac{(15-13.424)^2}{13.424}
\approx6.343.
$$

:::

:::

::: pf-step

The reference distribution has
$$
7-1-1=5
$$
degrees of freedom.


::: pf-proof

There are seven pooled categories. Their probabilities sum to one, costing one degree of freedom, and the parameter $\lambda$ was estimated from the same data, costing one further degree of freedom.

:::

:::

::: {.pf-step #s1-6}

At significance level $0.05$, the critical value is
$$
\chi^2_{0.95,5}\approx11.07.
$$
Since
$$
6.343<11.07,
$$
the Poisson hypothesis is not rejected.


::: pf-proof

The chi-squared goodness-of-fit test rejects when the statistic exceeds the upper 5% critical value for the reference degrees of freedom. Step [](#s1-4){.pf-ref} gives a statistic well below that threshold.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{\widehat\lambda=2.54}
$$
and the observed spectrum is compatible with the fitted Poisson distribution at the 5% significance level.


::: pf-proof

The estimate is step [](#s1-1){.pf-ref}, and the goodness-of-fit decision is step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives both requested conclusions.

:::

:::

:::
