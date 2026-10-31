---
schema: qual/card@1
id: P-PRECALC1-18
kind: problem
title: Derivative of $g\circ g$ at $0$ for $g(x)=e^{2x+1}$
classification:
  areas:
  - prelim
  topics:
  - Differentiation
  - Chain Rule
relations: []
review: draft
---

::: {.problem}
Let $g(x) = e^{2x + 1}$. Compute $\displaystyle \lim_{x \to 0} \frac{g(g(x)) - g(e)}{x}$.
:::

::: {.solution}

Let
$$
h(x)=g(g(x)).
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\boxed{
g(0)=e}.
$$


::: pf-proof

$$
g(0)
=
e^{2\cdot0+1}
=
e.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{
h(0)=g(e)}.
$$


::: pf-proof

By definition,
$$
h(0)=g(g(0)).
$$
Apply step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The given limit is
$$
\boxed{
\lim_{x\to0}
\frac{h(x)-h(0)}{x}
=
h'(0)}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} identifies the numerator as the standard difference quotient for
$h$ at $0$.

:::

:::

::: {.pf-step #s1-4}

The derivative of $g$ is
$$
\boxed{
g'(x)=2e^{2x+1}}.
$$


::: pf-proof

Apply the chain rule to
$$
g(x)=e^{2x+1}.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
g'(0)=2e}.
$$


::: pf-proof

Substitute $x=0$ into step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Also,
$$
\boxed{
g'(e)=2e^{2e+1}}.
$$


::: pf-proof

Substitute $x=e$ into step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

By the chain rule,
$$
h'(0)
=
g'(g(0))\,g'(0).
$$


::: pf-proof

Since
$$
h=g\circ g,
$$
the chain rule gives
$$
h'(x)=g'(g(x))g'(x).
$$
Set $x=0$.

:::

:::

::: pf-step

Therefore
$$
h'(0)
=
\left(
2e^{2e+1}
\right)
(2e).
$$


::: pf-proof

Use steps [](#s1-1){.pf-ref}, [](#s1-5){.pf-ref}, and [](#s1-6){.pf-ref}, and [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Simplifying,
$$
\boxed{
h'(0)
=
4e^{2e+2}}.
$$


::: pf-proof

$$
2e^{2e+1}\cdot2e
=
4e^{2e+1+1}
=
4e^{2e+2}.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\lim_{x\to0}
\frac{g(g(x))-g(e)}{x}
=
4e^{2e+2}}.
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the requested limit.

:::

:::

:::
