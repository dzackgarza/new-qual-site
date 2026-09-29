---
schema: qual/card@1
id: P-BERK77S-05
kind: problem
title: The values of the multivalued power $i^i$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used all logarithms log i=i(pi/2+2 pi k). Exponentiating i times these
    logarithms gives precisely the positive real values
    exp(-pi/2-2 pi k), k in Z.
---

::: {.problem}
Write all values of $i^i$ in the form $a+bi$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The complete set of logarithms of $i$ is
$$
\log i
=
i\left(\frac\pi2+2\pi k\right),
\qquad
k\in\ZZ.
$$

::: pf-proof

The number $i$ has modulus $1$ and arguments
$$
\frac\pi2+2\pi k,
\qquad
k\in\ZZ.
$$
Hence every logarithm of $i$ is
$$
\ln1+i\left(\frac\pi2+2\pi k\right)
=
i\left(\frac\pi2+2\pi k\right),
$$
and every integer $k$ gives one.

:::

:::

::: {.pf-step #s2}

Corresponding to the logarithm indexed by $k$,
$$
i\log i
=
-\left(\frac\pi2+2\pi k\right).
$$

::: pf-proof

Multiply the expression in step [](#s1){.pf-ref} by $i$ and use $i^2=-1$.

:::

:::

::: {.pf-step #s3}

The complete set of values of $i^i$ is
$$
\boxed{
i^i
=
e^{-\pi/2-2\pi k}+0i,
\qquad
k\in\ZZ.
}
$$

::: pf-proof

For a complex exponent, the multivalued power is obtained from
$$
i^i=\exp(i\log i)
$$
as $\log i$ ranges over all logarithms. Step [](#s2){.pf-ref} therefore gives
$$
\exp\left(
-\frac\pi2-2\pi k
\right).
$$
These numbers are positive real, so in the requested form their imaginary
part is $0$. Step [](#s1){.pf-ref} exhausts all logarithms, so no other values occur.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the requested list of all values.

:::

:::

:::
