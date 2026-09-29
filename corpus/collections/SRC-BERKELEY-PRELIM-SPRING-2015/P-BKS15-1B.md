---
schema: qual/card@1
id: P-BKS15-1B
kind: problem
title: Integral bounds for $n!$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked both strict integral comparisons for log x, the antiderivative evaluation, and the final exponentiation.
---

::: {.problem}
For all integers $n>2$, prove
$$
\frac{n^n}{e^{n-1}}<n!<\frac{(n+1)^{n+1}}{e^n}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

One has
$$
\log(n!)
=
\sum_{k=1}^n\log k.
$$

::: pf-proof

Since $n!=\prod_{k=1}^n k$ and every factor is positive, the logarithm of the product is the sum of the logarithms.

:::

:::

::: {.pf-step #s2}

For every integer $n>1$,
$$
\int_1^n\log x\,dx
<
\sum_{k=1}^n\log k.
$$

::: pf-proof

For each $k=2,\ldots,n$, the function $\log x$ is strictly increasing on $[k-1,k]$, so
$$
\int_{k-1}^k\log x\,dx
<
\log k.
$$
Summing these inequalities gives
$$
\int_1^n\log x\,dx
<
\sum_{k=2}^n\log k
=
\sum_{k=1}^n\log k,
$$
because $\log1=0$.

:::

:::

::: {.pf-step #s3}

For every integer $n\geq1$,
$$
\sum_{k=1}^n\log k
<
\int_1^{n+1}\log x\,dx.
$$

::: pf-proof

For each $k=1,\ldots,n$, strict monotonicity gives
$$
\log k
<
\int_k^{k+1}\log x\,dx.
$$
Indeed, $\log x>\log k$ for every $x\in(k,k+1]$. Summing over $k$ yields the displayed inequality.

:::

:::

::: {.pf-step #s4}

Therefore
$$
n\log n-n+1
<
\log(n!)
<
(n+1)\log(n+1)-n.
$$

::: pf-proof

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
\int_1^n\log x\,dx
<
\log(n!)
<
\int_1^{n+1}\log x\,dx.
$$
Using
$$
\int\log x\,dx=x\log x-x+C
$$
gives
$$
\int_1^n\log x\,dx
=
n\log n-n+1
$$
and
$$
\int_1^{n+1}\log x\,dx
=
(n+1)\log(n+1)-n.
$$

:::

:::

::: {.pf-step #s5}

For every integer $n>2$,
$$
\boxed{
\frac{n^n}{e^{n-1}}
<
n!
<
\frac{(n+1)^{n+1}}{e^n}
}.
$$

::: pf-proof

The exponential function is strictly increasing. Exponentiating step [](#s4){.pf-ref} gives
$$
e^{n\log n-n+1}
<
n!
<
e^{(n+1)\log(n+1)-n}.
$$
The two endpoint expressions simplify to
$$
e^{n\log n-n+1}
=
\frac{n^n}{e^{n-1}}
$$
and
$$
e^{(n+1)\log(n+1)-n}
=
\frac{(n+1)^{n+1}}{e^n}.
$$

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required inequality.

:::

:::

:::
