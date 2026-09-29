---
schema: qual/card@1
id: P-BERK89S-12
kind: problem
title: The contour integral $\int_{|z|=2}(2z-1)e^{z/(z-1)}\,dz$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Expanded the integrand at its unique singularity $z=1$, extracted the
    residue directly, and applied the residue theorem.
---

::: {.problem}
Evaluate
\[
\int_C(2z-1)e^{z/(z-1)}\,dz,
\]
where $C$ is the positively oriented circle $|z|=2$.
:::

::: {.solution}
::: pf

::: {.pf-step #singularity-inside-contour}
The integrand is holomorphic on and inside $C$ except at $z=1$.

::: pf-proof
The only possible singularity of
$$
(2z-1)e^{z/(z-1)}
$$
occurs where $z-1=0$, namely at $z=1$. Since $\abs{1}<2$, this point lies
inside $C$, and the integrand is holomorphic everywhere else on and inside
the contour.
:::

:::

::: {.pf-step #residue-value}
The residue of the integrand at $z=1$ is $2e$.

::: pf-proof
Set $w=z-1$. Then
$$
2z-1=2w+1,
\qquad
\frac{z}{z-1}=1+\frac1w.
$$
Hence
$$
(2z-1)e^{z/(z-1)}
=e(2w+1)e^{1/w}
=e(2w+1)\sum_{n=0}^\infty\frac{w^{-n}}{n!}.
$$
The coefficient of $w^{-1}$ receives one contribution from the factor $1$
with $n=1$, and one from the factor $2w$ with $n=2$. Therefore
$$
\operatorname{Res}_{z=1}(2z-1)e^{z/(z-1)}
=e\left(1+\frac{2}{2!}\right)
=2e.
$$
:::

:::

::: {.pf-step #integral-value-boxed}
The integral equals
$$
\boxed{4\pi i e}.
$$

::: pf-proof
By steps [](#singularity-inside-contour){.pf-ref} and [](#residue-value){.pf-ref}, the residue theorem gives
$$
\int_C(2z-1)e^{z/(z-1)}\,dz
=2\pi i\operatorname{Res}_{z=1}(2z-1)e^{z/(z-1)}
=2\pi i(2e)
=4\pi i e.
$$
:::

:::

::: pf-qed
Step [](#integral-value-boxed){.pf-ref} gives the requested value.
:::

:::
:::
