---
schema: qual/card@1
id: P-UGAP08F-02
kind: problem
title: Differentiate an integral with a variable upper limit
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let
$$
F(x)=\int_3^{\sin x}\sqrt{1+t^4}\,dt.
$$
Compute $F'(x)$ and carefully state the theorems needed to justify the answer.
:::

::: {.solution}

Let
$$
g(t)\coloneqq\sqrt{1+t^4}
\qquad\text{and}\qquad
H(u)\coloneqq\int_3^u g(t)\,dt.
$$

::: pf

::: {.pf-step #s1-1}

The function $H$ is differentiable on $\RR$ and
$$
H'(u)=\sqrt{1+u^4}.
$$


::: pf-proof

The function $g(t)=\sqrt{1+t^4}$ is continuous on $\RR$. By the Fundamental Theorem of Calculus, if
$$
H(u)=\int_3^u g(t)\,dt,
$$
then $H$ is differentiable and $H'(u)=g(u)$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
F(x)=H(\sin x).
$$


::: pf-proof

This is immediate from the definitions of $F$ and $H$.

:::

:::

::: {.pf-step #s1-3}

The derivative is
$$
\boxed{F'(x)=\cos x\,\sqrt{1+\sin^4x}}.
$$


::: pf-proof

The sine function is differentiable with derivative $\cos x$. By step [](#s1-1){.pf-ref}, $H$ is differentiable. Therefore the chain rule applied to step [](#s1-2){.pf-ref} gives
$$
\begin{aligned}
F'(x)
&=H'(\sin x)\cos x\\
&=\sqrt{1+\sin^4x}\,\cos x.
\end{aligned}
$$
The two required results are therefore the Fundamental Theorem of Calculus for a continuous integrand and the chain rule.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the derivative and identifies the theorems that justify it.

:::

:::

:::
