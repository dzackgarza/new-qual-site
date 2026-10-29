---
schema: qual/card@1
id: P-TRIV-PR23
kind: problem
title: Central limit estimate of accumulated round-off error
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 23, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost epsilon and removed stray residue against Probability Problem 23 on page 30 of the source PDF.
---

::: {.problem}
Consider the sum $a$ of $10^N$ real numbers $a_k$, $a = \sum_{k=1}^{10^N} a_k$.
Let $\tilde{a}_k$ be an approximation of $a_k$ with precision $10^{-m}$.
Assume that the round-off errors $\delta_k = a_k - \tilde{a}_k$ are distributed uniformly within the interval $(-0.5 \cdot 10^{-m},\ 0.5 \cdot 10^{-m})$.
Compose the sum $\tilde{a} = \sum_{k=1}^{10^N} \tilde{a}_k$ and let $\delta = a - \tilde{a}$ be the total error of the approximation.
For the given values of $N$ and $m$ find $\epsilon$ such that
$$
P(|\delta| < \epsilon) > 0.99.
\tag{52}
$$
:::

::: {.solution}

Assume the round-off errors $\delta_k$ are independent. Put
$$
n=10^N,
\qquad
h=\frac12\,10^{-m}.
$$
Then $\delta=\sum_{k=1}^n\delta_k$.

::: pf

::: pf-step

Each round-off error has
$$
\mathbf E\delta_k=0,
\qquad
\mathbf D\delta_k=\frac{h^2}{3}=\frac{10^{-2m}}{12}.
$$


::: pf-proof

A uniform random variable on $(-h,h)$ is symmetric, hence has mean zero, and its variance is
$$
\frac1{2h}\int_{-h}^{h}x^2\,dx
=\frac{h^2}{3}.
$$
Substitute $h=10^{-m}/2$.

:::

:::

::: {.pf-step #s1-2}

Therefore the total error has
$$
\mathbf E\delta=0,
\qquad
\mathbf D\delta
=\frac{10^{N-2m}}{12},
$$
and standard deviation
$$
\sigma_\delta=\frac{10^{N/2-m}}{\sqrt{12}}.
$$


::: pf-proof

Means add by linearity. Independence makes variances add, so
$$
\mathbf D\delta
=n\frac{10^{-2m}}{12}
=\frac{10^{N-2m}}{12}.
$$
Take the positive square root.

:::

:::

::: {.pf-step #s1-3}

For large $10^N$, the central limit theorem gives the approximation
$$
\frac{\delta}{\sigma_\delta}\approx Z,
\qquad Z\sim N(0,1).
$$


::: pf-proof

The variables $\delta_k$ are independent, identically distributed, bounded, and have finite nonzero variance. Hence their standardized sum converges in distribution to a standard normal random variable as $n=10^N\to\infty$.

:::

:::

::: pf-step

If $z_{0.995}=\Phi^{-1}(0.995)$, then
$$
P(|Z|<z_{0.995})=0.99,
\qquad
z_{0.995}\approx2.57583.
$$


::: pf-proof

By symmetry of the standard normal law,
$$
P(|Z|<z)=2\Phi(z)-1.
$$
Setting this equal to $0.99$ gives $\Phi(z)=0.995$.

:::

:::

::: {.pf-step #s1-5}

Thus the central-limit estimate for the required tolerance is
$$
\boxed{
\epsilon\approx
\frac{z_{0.995}}{\sqrt{12}}\,10^{N/2-m}
\approx0.7435\,10^{N/2-m}.}
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
P(|\delta|<\epsilon)
\approx P\left(|Z|<\frac{\epsilon}{\sigma_\delta}\right).
$$
Choose $\epsilon=z_{0.995}\sigma_\delta$ and substitute step [](#s1-2){.pf-ref}. To obtain a strict numerical inequality $>0.99$ within the normal approximation, take any value slightly larger than this threshold.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested central-limit estimate as a function of $N$ and $m$.

:::

:::

:::
