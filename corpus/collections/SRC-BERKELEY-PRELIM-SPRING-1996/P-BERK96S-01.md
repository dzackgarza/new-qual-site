---
schema: qual/card@1
id: P-BERK96S-01
kind: problem
title: Limit of $(n^n/n!)^{1/n}$
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
  date: 2026-09-23
---

::: {.problem}
Compute
\[
\lim_{n\to\infty}\left(\frac{n^n}{n!}\right)^{1/n}.
\]
:::

::: {.solution}
For $n\ge1$, set
$$
a_n\coloneqq\left(\frac{n^n}{n!}\right)^{1/n}.
$$

::: pf

::: {.pf-step #s1}

For every $n\ge2$,
$$
\int_1^n\log x\,dx
\le \log(n!)
\le \int_1^n\log x\,dx+\log n.
$$

::: pf-proof

Since $\log x$ is increasing, for $2\le k\le n$,
$$
\int_{k-1}^k\log x\,dx\le\log k.
$$
Summing gives
$$
\int_1^n\log x\,dx\le\sum_{k=2}^n\log k=\log(n!).
$$

Similarly, for $1\le k\le n-1$,
$$
\log k\le\int_k^{k+1}\log x\,dx.
$$
Hence
$$
\log((n-1)!)\le\int_1^n\log x\,dx,
$$
and adding $\log n$ gives the upper bound.

:::

:::

::: {.pf-step #s2}

One has
$$
1-\frac{1+\log n}{n}
\le \log a_n
\le 1-\frac1n.
$$

::: pf-proof

The integral in step [](#s1){.pf-ref} is
$$
\int_1^n\log x\,dx
=n\log n-n+1.
$$
Also,
$$
\log a_n
=\frac{n\log n-\log(n!)}{n}.
$$
Substituting the upper and lower bounds for $\log(n!)$ from step
[](#s1){.pf-ref} yields exactly the stated inequalities.

:::

:::

::: {.pf-step #s3}

The requested limit is
$$
\boxed{e}.
$$

::: pf-proof

Both bounds in step [](#s2){.pf-ref} tend to $1$, so the squeeze theorem gives
$$
\lim_{n\to\infty}\log a_n=1.
$$
Continuity of the exponential function therefore gives
$$
\lim_{n\to\infty}a_n=e.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} computes the required limit.

:::

:::

:::
