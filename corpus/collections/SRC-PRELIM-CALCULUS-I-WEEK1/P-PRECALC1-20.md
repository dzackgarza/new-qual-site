---
schema: qual/card@1
id: P-PRECALC1-20
kind: problem
title: Derivative of $\int_0^{x^2}e^{-t^2}\,dt$
classification:
  areas:
  - prelim
  topics:
  - Fundamental Theorem of Calculus
  - Chain Rule
relations: []
review: draft
---

::: {.problem}
Compute the derivative $\displaystyle \frac{d}{dx} \int_{0}^{x^{2}} e^{-t^{2}}\, dt$.
:::

::: {.solution}

Define
$$
F(u)
=
\int_0^u e^{-t^2}\,dt.
$$

::: pf

::: {.pf-step #s1-1}

By the fundamental theorem of calculus,
$$
\boxed{
F'(u)=e^{-u^2}}.
$$


::: pf-proof

The integrand $e^{-t^2}$ is continuous on $\RR$.

:::

:::

::: pf-step

The given function is
$$
\boxed{
F(x^2)}.
$$


::: pf-proof

Substitute $u=x^2$ into the definition of $F$.

:::

:::

::: {.pf-step #s1-3}

By the chain rule,
$$
\frac{d}{dx}F(x^2)
=
F'(x^2)\cdot2x.
$$


::: pf-proof

Differentiate the composition $F\circ(x\mapsto x^2)$.

:::

:::

::: {.pf-step #s1-4}

Using step [](#s1-1){.pf-ref},
$$
F'(x^2)
=
e^{-(x^2)^2}
=
e^{-x^4}.
$$


::: pf-proof

Substitute $u=x^2$ into
$$
F'(u)=e^{-u^2}.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\frac{d}{dx}
\int_0^{x^2}e^{-t^2}\,dt
=
2x\,e^{-x^4}}.
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the requested derivative.

:::

:::

:::
