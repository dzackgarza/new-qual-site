---
schema: qual/card@1
id: P-PRECALC1-10
kind: problem
title: The product $e^{g}h$ when $h'=-g'h$
classification:
  areas:
  - prelim
  topics:
  - Differentiation
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
Let $f(x) = e^{g(x)} h(x)$ where $h'(x) = -g'(x) h(x)$ for all $x \in \RR$. Which of the following is necessarily true?

(a) $f$ is constant.

(b) $f$ is linear and non-constant.

(c) $g$ is constant.

(d) $g$ is linear and non-constant.

(e) None of the above.
:::

::: {.solution}

::: pf

::: pf-step

Differentiate
$$
f(x)=e^{g(x)}h(x).
$$


::: pf-proof

Use the product rule and the chain rule.

:::

:::

::: {.pf-step #s1-2}

One obtains
$$
\boxed{
f'(x)
=
e^{g(x)}g'(x)h(x)
+
e^{g(x)}h'(x)}.
$$


::: pf-proof

The derivative of
$$
e^{g(x)}
$$
is
$$
e^{g(x)}g'(x).
$$

:::

:::

::: {.pf-step #s1-3}

Factor out $e^{g(x)}$:
$$
\boxed{
f'(x)
=
e^{g(x)}
\left(
g'(x)h(x)+h'(x)
\right)}.
$$


::: pf-proof

This is an algebraic factorization of step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The given relation
$$
h'(x)=-g'(x)h(x)
$$
implies
$$
g'(x)h(x)+h'(x)=0.
$$


::: pf-proof

Substitute the stated formula for $h'(x)$.

:::

:::

::: pf-step

Hence
$$
\boxed{
f'(x)=0}
$$
for every $x\in\RR$.


::: pf-proof

Combine steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore $f$ is constant on $\RR$.


::: pf-proof

A differentiable function whose derivative is identically zero on an interval
is constant there. The real line is an interval.

:::

:::

::: {.pf-step #s1-7}

Thus the necessarily true statement is
$$
\boxed{\text{(a) }f\text{ is constant}.}
$$


::: pf-proof

This is step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the required choice.

:::

:::

:::
