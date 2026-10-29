---
schema: qual/card@1
id: P-PRECALC1-02
kind: problem
title: Limit of $\frac{(1+x)^\alpha-1}{x}$ as $x\to0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Evaluate $\operatorname* { l i m } _ { x \to 0 } { \frac { ( 1 + x ) ^ { \alpha } - 1 } { x } }$ for $\alpha \in \RR$
:::

::: {.solution}

Define
\[
f(t)=t^\alpha
\]
for \(t>0\).

::: pf

::: {.pf-step #s1-1}

The given limit can be rewritten as
\[
\boxed{
\lim_{x\to0}
\frac{f(1+x)-f(1)}{x}}.
\]


::: pf-proof

Since
\[
f(1+x)=(1+x)^\alpha
\]
and
\[
f(1)=1^\alpha=1,
\]
the quotient is exactly the one in the problem.

:::

:::

::: {.pf-step #s1-2}

For \(t>0\),
\[
\boxed{
f(t)=e^{\alpha\log t}}.
\]


::: pf-proof

This is the standard definition of the real power \(t^\alpha\) for
\(t>0\).

:::

:::

::: {.pf-step #s1-3}

Therefore
\[
\boxed{
f'(t)=\alpha t^{\alpha-1}}.
\]


::: pf-proof

Differentiate step [](#s1-2){.pf-ref}:
\[
\begin{aligned}
f'(t)
&=
e^{\alpha\log t}\cdot\frac{\alpha}{t}\\
&=
t^\alpha\frac{\alpha}{t}\\
&=
\alpha t^{\alpha-1}.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-4}

In particular,
\[
\boxed{
f'(1)=\alpha}.
\]


::: pf-proof

Substitute \(t=1\) into step [](#s1-3){.pf-ref}:
\[
f'(1)
=
\alpha\cdot1^{\alpha-1}
=
\alpha.
\]

:::

:::

::: {.pf-step #s1-5}

By the definition of the derivative,
\[
\lim_{x\to0}
\frac{f(1+x)-f(1)}{x}
=
f'(1).
\]


::: pf-proof

This is the difference-quotient definition of the derivative at the point
\(1\).

:::

:::

::: {.pf-step #s1-6}

Hence
\[
\boxed{
\lim_{x\to0}
\frac{(1+x)^\alpha-1}{x}
=
\alpha}.
\]


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-4){.pf-ref}, and [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the requested limit.

:::

:::

:::
