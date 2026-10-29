---
schema: qual/card@1
id: P-TRIV-PR26
kind: problem
title: Confidence interval for a proportion of defective goods
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 26, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
From a collection of 500 goods 70 were investigated, and in 14 of them various defects were revealed.
Find the interval in which the fraction of the defected goods in the whole group lies with the probability 96%.
:::

::: {.solution}

Let $N=500$ be the population size, $n=70$ the sample size, and
$$
\widehat p=\frac{14}{70}=0.2
$$
the observed defective fraction. Use the normal approximation for simple random sampling without replacement.

::: pf

::: {.pf-step #s1-1}

The estimated standard error of the sample proportion, including the finite-population correction, is
$$
\widehat{\operatorname{se}}(\widehat p)
=\sqrt{\frac{\widehat p(1-\widehat p)}{n}
\frac{N-n}{N-1}}.
$$


::: pf-proof

For a finite population containing a fraction $p$ of defective items, the variance of the sample proportion under sampling without replacement is
$$
\operatorname{Var}(\widehat p)
=\frac{p(1-p)}n\frac{N-n}{N-1}.
$$
Replacing the unknown $p$ by the observed proportion $\widehat p$ gives the plug-in standard-error estimate.

:::

:::

::: {.pf-step #s1-2}

Numerically,
$$
\widehat{\operatorname{se}}(\widehat p)
=\sqrt{\frac{0.2\cdot0.8}{70}\frac{430}{499}}
\approx0.04438.
$$


::: pf-proof

Substitute $N=500$, $n=70$, and $\widehat p=0.2$ into step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

A central 96% normal interval uses
$$
z_{0.98}=\Phi^{-1}(0.98)\approx2.05375.
$$


::: pf-proof

A two-sided central interval with coverage $0.96$ leaves total tail probability $0.04$, hence $0.02$ in each tail. Its positive standard-normal endpoint therefore satisfies $\Phi(z)=0.98$.

:::

:::

::: {.pf-step #s1-4}

The approximate 96% confidence interval is
$$
\widehat p\pm z_{0.98}\widehat{\operatorname{se}}(\widehat p)
\approx0.2\pm0.09115.
$$


::: pf-proof

Multiply the standard error in step [](#s1-2){.pf-ref} by the quantile in step [](#s1-3){.pf-ref}:
$$
2.05375(0.04438)\approx0.09115.
$$

:::

:::

::: {.pf-step #s1-5}

Thus the defective fraction is estimated to lie in
$$
\boxed{0.1089\lesssim p\lesssim0.2912}
$$
with approximately 96% confidence.


::: pf-proof

Subtract and add the margin from step [](#s1-4){.pf-ref} to $\widehat p=0.2$.

:::

:::

::: {.pf-step #s1-6}

In terms of the number $K=500p$ of defective goods, this corresponds approximately to
$$
\boxed{55\lesssim K\lesssim146}.
$$


::: pf-proof

Multiply the endpoints in step [](#s1-5){.pf-ref} by $500$ and round outward to integer population counts.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} give the requested approximate 96% interval for the fraction and its equivalent population-count range.

:::

:::

:::
