---
schema: qual/card@1
id: P-RASP15B
kind: problem
title: '$L^p$ characterization via the distribution function'
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Spring 2015 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood, and the wrapping ::: {.proof} div replaced by numbered steps. Added: the
    identification of the two forms of the set, that 2^k < |f| is the same condition as
    |f| > 2^k, and measurability; the case a = 0 and the case a = infinity of the geometric
    comparison, which the prose dismissed in one sentence; the derivation of the two-sided bound
    from 2^(mp) < a^p <= 2^((m+1)p); and the monotonicity step in integrating the pointwise
    bound. Not claimed: a retained solution set; the provenance names the examination.
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space.
Prove that for any $0 < p < \infty$, $f \in L^p$ if and only if
$$
\sum_{k=-\infty}^{\infty} 2^{kp} \lambda_f(2^k) < \infty
$$
where $\lambda_f(\alpha) = \mu(\{x : \abs{f}(x) > \alpha\})$.
:::

::: {.solution}
The statement is the one printed on this card; no retained solution set covers it — the collection's `provenance` names the Spring 2015 real-analysis examination, which carries no solutions — so the argument below is the card's own, and it is the card's previous proof restructured: Tonelli, a two-sided comparison of the geometric sum, then integration.

Throughout $(X,\mathcal M,\mu)$ is a measure space, $0<p<\infty$, $f$ is measurable, $\lambda_f(\alpha)=\mu\theset{\abs f>\alpha}$, and $\norm f_p^p=\int_X\abs f^p\,d\mu\in[0,\infty]$.

::: pf

::: {.pf-step #tonelli}
$\displaystyle\sum_{k\in\ZZ}2^{kp}\lambda_f(2^k)=\int_X\Bigl(\sum_{k\in\ZZ}2^{kp}\mathbf 1_{\theset{2^k<\abs{f(x)}}}\Bigr)d\mu(x)$, both sides possibly infinite.

::: pf-proof
$\lambda_f(2^k)=\int_X\mathbf 1_{\theset{\abs f>2^k}}d\mu$, and the integrands are nonnegative, so Tonelli's theorem permits the interchange of sum and integral. Note that $\abs f>2^k$ is the same condition as $2^k<\abs f$, and that the set is measurable because $f$ is.

:::

:::

::: {.pf-step #geometric}
For $a\ge0$,
$$
\frac{2^{-p}}{1-2^{-p}}a^p\le\sum_{k\in\ZZ}2^{kp}\mathbf 1_{\theset{2^k<a}}\le\frac1{1-2^{-p}}a^p,
$$
with the convention that both sides are infinite for $a=+\infty$.

::: pf-proof
For $a=0$ the sum vanishes and so does $a^p$. For $0<a<\infty$ choose $m\in\ZZ$ with $2^m<a\le2^{m+1}$; then $2^k<a$ exactly for $k\le m$, so the sum is $\sum_{k=-\infty}^m2^{kp}=2^{mp}/(1-2^{-p})$, a convergent geometric series since $2^p>1$. From $2^{mp}<a^p\le2^{(m+1)p}=2^p\,2^{mp}$ we get $a^p2^{-p}\le2^{mp}<a^p$, which gives the two-sided bound. For $a=\infty$ every indicator is $1$ and the sum diverges, matching the right side.

:::

:::

::: {.pf-step #comparison}
$$
\frac{2^{-p}}{1-2^{-p}}\norm f_p^p\le\sum_{k\in\ZZ}2^{kp}\lambda_f(2^k)\le\frac1{1-2^{-p}}\norm f_p^p .
$$

::: pf-proof
Apply step [](#geometric){.pf-ref} pointwise with $a=\abs{f(x)}$, multiply nothing further, and integrate over $X$ using step [](#tonelli){.pf-ref} together with the monotonicity of the integral: integrating the lower bound gives $\frac{2^{-p}}{1-2^{-p}}\int_X\abs f^p$, and the integrand of the middle term is exactly the integrand on the right of step [](#tonelli){.pf-ref}. The constants are positive and finite because $p>0$.

:::

:::

::: {.pf-step #conclusion}
$f\in L^p$ iff $\displaystyle\sum_{k\in\ZZ}2^{kp}\lambda_f(2^k)<\infty$.

::: pf-proof
By step [](#comparison){.pf-ref} the series is finite iff $\norm f_p^p$ is finite, the two differing by finite positive constants. And $\norm f_p^p<\infty$ is the definition of $f\in L^p$ for a measurable $f$; when the series is infinite so is $\norm f_p^p$, and conversely.

:::

:::

:::
:::
