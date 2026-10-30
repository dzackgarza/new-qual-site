---
schema: qual/card@1
id: P-TRIV-PR27
kind: problem
title: Outlier test for wheat yield data
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 27, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Here is the data about wheat yield from 8 identical wheat fields in conventional units:

$$
2 6 . 5 \quad 2 6 . 2 \quad 3 5 . 9 \quad 3 0 . 1 \quad 3 2 . 3 \quad 2 9 . 3 \quad 2 6 . 1 \quad 2 5 . 0
$$

There is a suspicion that the data about the third field is incorrect.
Check if it should be dropped with 5% significance level.
:::

::: {.solution}

Assume the eight field yields are an independent sample from a normal population and test the single suspected high observation $35.9$ using Grubbs' statistic
$$
G=\frac{\abs{x_{\mathrm{sus}}-\bar x}}{s},
$$
where $s$ is the sample standard deviation.

::: pf

::: {.pf-step #s1-1}

The sample mean is
$$
\bar x=28.925.
$$


::: pf-proof

The eight observations sum to $231.4$, so
$$
\bar x=\frac{231.4}{8}=28.925.
$$

:::

:::

::: {.pf-step #s1-2}

The sample standard deviation is
$$
s=\sqrt{\frac1{7}\sum_{i=1}^8(x_i-\bar x)^2}
\approx3.7465.
$$


::: pf-proof

Using the mean from step [](#s1-1){.pf-ref}, the sum of squared deviations is approximately $98.2549$. Dividing by $8-1=7$ and taking the square root gives $s\approx3.7465$.

:::

:::

::: pf-step

For the suspected observation $35.9$,
$$
G_{\mathrm{obs}}
=\frac{35.9-28.925}{3.7465}
\approx1.862.
$$


::: pf-proof

The suspected value is the sample maximum, so its absolute deviation from the mean is $6.975$. Divide by the sample standard deviation from step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

At significance level $0.05$ with $n=8$, the two-sided Grubbs critical value is
$$
G_{0.05,8}\approx2.1266.
$$


::: pf-proof

For a single suspected outlier under normal sampling, the two-sided Grubbs critical value is
$$
G_{\alpha,n}
=\frac{n-1}{\sqrt n}
\sqrt{\frac{t^2}{n-2+t^2}},
$$
where $t$ is the upper $\alpha/(2n)$ quantile of Student's $t$ distribution with $n-2$ degrees of freedom. Substitution of $n=8$ and $\alpha=0.05$ gives $G_{0.05,8}\approx2.1266$.

:::

:::

::: {.pf-step #s1-5}

Since
$$
G_{\mathrm{obs}}\approx1.862<2.1266\approx G_{0.05,8},
$$
the observation $35.9$ is not rejected as an outlier at the 5% significance level.


::: pf-proof

Grubbs' test rejects the suspected observation exactly when the observed statistic exceeds the critical value. The strict inequality is in the opposite direction.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{\text{the third-field observation should not be dropped at the 5% level}.}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} shows that the data do not provide sufficient evidence, at the specified significance level, to classify $35.9$ as a single normal-sample outlier.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} answers the requested decision.

:::

:::

:::
