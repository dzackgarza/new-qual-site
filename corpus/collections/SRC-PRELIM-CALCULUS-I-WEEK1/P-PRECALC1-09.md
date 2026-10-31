---
schema: qual/card@1
id: P-PRECALC1-09
kind: problem
title: Limit of $\frac{\sin 2x}{(1+x)\ln(1+x)}$ as $x\to0$
classification:
  areas:
  - prelim
  topics:
  - Limits
  - L'Hôpital's Rule
relations: []
review: draft
---

::: {.problem}
Compute $\displaystyle \lim_{x \to 0} \frac{\sin(2x)}{(1 + x) \ln(1 + x)}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Rewrite the quotient as
$$
\boxed{
\frac{\sin(2x)}{(1+x)\ln(1+x)}
=
\frac{\sin(2x)}{2x}
\cdot
\frac{2x}{\ln(1+x)}
\cdot
\frac1{1+x}}.
$$


::: pf-proof

Multiply the three factors on the right and cancel $2x$.

:::

:::

::: {.pf-step #s1-2}

The first factor satisfies
$$
\boxed{
\lim_{x\to0}
\frac{\sin(2x)}{2x}
=
1}.
$$


::: pf-proof

Set $u=2x$. Then $u\to0$, and use the standard limit
$$
\frac{\sin u}{u}\to1.
$$

:::

:::

::: {.pf-step #s1-3}

The logarithmic factor satisfies
$$
\boxed{
\lim_{x\to0}
\frac{x}{\ln(1+x)}
=
1}.
$$


::: pf-proof

The standard limit
$$
\frac{\ln(1+x)}{x}\to1
$$
holds as $x\to0$. Taking reciprocals gives the displayed limit.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\lim_{x\to0}
\frac{2x}{\ln(1+x)}
=
2}.
$$


::: pf-proof

Multiply the limit in step [](#s1-3){.pf-ref} by $2$.

:::

:::

::: {.pf-step #s1-5}

The final factor satisfies
$$
\boxed{
\lim_{x\to0}
\frac1{1+x}
=
1}.
$$


::: pf-proof

The function $1/(1+x)$ is continuous at $x=0$.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
\lim_{x\to0}
\frac{\sin(2x)}{(1+x)\ln(1+x)}
=
1\cdot2\cdot1
=
2}.
$$


::: pf-proof

Apply the product law for limits to steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the requested limit.

:::

:::

:::
