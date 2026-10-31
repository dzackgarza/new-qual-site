---
schema: qual/card@1
id: P-PRECALC1-11
kind: problem
title: Derivative of $x^{2+\sin x}$
classification:
  areas:
  - prelim
  topics:
  - Differentiation
relations: []
review: draft
---

::: {.problem}
Let $f(x) = x^{2 + \sin(x)}$ for $x > 0$. Find $f'(x)$.
:::

::: {.solution}

Let
$$
f(x)=x^{2+\sin x},
\qquad
x>0.
$$

::: pf

::: {.pf-step #s1-1}

Since $x>0$,
$$
\boxed{
f(x)=e^{(2+\sin x)\log x}}.
$$


::: pf-proof

Use
$$
x^a=e^{a\log x}
$$
for positive $x$.

:::

:::

::: {.pf-step #s1-2}

Differentiate the exponent:
$$
\frac{d}{dx}
\left(
(2+\sin x)\log x
\right)
=
\cos x\,\log x
+
\frac{2+\sin x}{x}.
$$


::: pf-proof

Apply the product rule:
$$
(2+\sin x)'\log x
+
(2+\sin x)(\log x)'.
$$
Now
$$
(2+\sin x)'=\cos x
$$
and
$$
(\log x)'=\frac1x.
$$

:::

:::

::: {.pf-step #s1-3}

By the chain rule,
$$
f'(x)
=
e^{(2+\sin x)\log x}
\left(
\cos x\,\log x
+
\frac{2+\sin x}{x}
\right).
$$


::: pf-proof

Differentiate the exponential expression from step [](#s1-1){.pf-ref} using step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
f'(x)
=
x^{2+\sin x}
\left(
\cos x\,\log x
+
\frac{2+\sin x}{x}
\right)}.
$$


::: pf-proof

Replace the exponential factor in step [](#s1-3){.pf-ref} by $x^{2+\sin x}$ using
step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the requested derivative.

:::

:::

:::
