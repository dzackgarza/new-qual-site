---
schema: qual/card@1
id: P-WESCA05-I8
kind: problem
title: "Evaluate a Cauchy-integral-formula contour integral"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 8 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Evaluate
$$
\int_{\abs{z}=2}\frac{e^{\pi z}}{(z-1)^2}\,dz.
$$
:::

::: {.solution}

Assume the circle $\abs{z}=2$ has its standard positive orientation.

::: pf

::: {.pf-step #s1-1}

The function
$$
F(z)=e^{\pi z}
$$
is analytic on and inside the circle $\abs{z}=2$, and $1$ lies inside that circle.


::: pf-proof

The exponential function is entire, so $F$ is analytic on all of $\CC$. Moreover
$$
\abs{1}=1<2.
$$
Thus the hypotheses of the differentiated Cauchy integral formula apply at $a=1$.

:::

:::

::: {.pf-step #s1-2}

The differentiated Cauchy integral formula gives
$$
\int_{\abs{z}=2}\frac{e^{\pi z}}{(z-1)^2}\,dz
=
2\pi i\,F'(1).
$$


::: pf-proof

For a function $F$ analytic on and inside a positively oriented simple closed contour $C$, the Cauchy integral formula for the first derivative states
$$
F'(a)
=
\frac{1}{2\pi i}
\int_C\frac{F(z)}{(z-a)^2}\,dz.
$$
Apply this with $C=\{\abs{z}=2\}$, $a=1$, and $F(z)=e^{\pi z}$, using step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

One has
$$
F'(1)=\pi e^\pi.
$$


::: pf-proof

Differentiating gives
$$
F'(z)=\pi e^{\pi z}.
$$
Evaluating at $z=1$ gives the claim.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\displaystyle
\int_{\abs{z}=2}\frac{e^{\pi z}}{(z-1)^2}\,dz
=2\pi^2 i e^\pi.}
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into the identity in step [](#s1-2){.pf-ref}:
$$
2\pi i\,F'(1)
=
2\pi i\cdot\pi e^\pi
=
2\pi^2 i e^\pi.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested contour integral.

:::

:::

:::
