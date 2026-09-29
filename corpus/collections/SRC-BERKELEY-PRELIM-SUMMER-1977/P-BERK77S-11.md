---
schema: qual/card@1
id: P-BERK77S-11
kind: problem
title: Positivity propagation for the transport equation $f_x=f_t$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Followed the characteristic segment s↦(x+t-s,s). Its derivative along f
    is -f_x+f_t=0, so f(x,t)=f(x+t,0); positivity on the initial line
    therefore propagates to every point.
---

::: {.problem}
Let $f(x,t)$ be a $C^1$ function satisfying
\[
\frac{\partial f}{\partial x}=\frac{\partial f}{\partial t}.
\]
Suppose $f(x,0)>0$ for every $x$. Prove that
\[
f(x,t)>0
\]
for every $x,t$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Fix arbitrary $x,t\in\RR$ and define
$$
\phi(s)=f(x+t-s,s).
$$

::: pf-proof

Since $f$ is $C^1$, the function $\phi$ is differentiable for all
$s\in\RR$.

:::

:::

::: {.pf-step #s2}

The function $\phi$ is constant.

::: pf-proof

By the chain rule,
$$
\begin{aligned}
\phi'(s)
&=
-f_x(x+t-s,s)
+
f_t(x+t-s,s)\\
&=
0,
\end{aligned}
$$
because $f_x=f_t$ everywhere. Hence $\phi$ is constant.

:::

:::

::: {.pf-step #s3}

For every $x,t\in\RR$,
$$
f(x,t)=f(x+t,0).
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\phi(t)=\phi(0).
$$
The definition in step [](#s1){.pf-ref} gives
$$
\phi(t)=f(x,t)
$$
and
$$
\phi(0)=f(x+t,0).
$$

:::

:::

::: {.pf-step #s4}

For every $x,t\in\RR$,
$$
\boxed{
f(x,t)>0.
}
$$

::: pf-proof

Step [](#s3){.pf-ref} gives
$$
f(x,t)=f(x+t,0).
$$
The hypothesis says that $f(y,0)>0$ for every real $y$. Applying it to
$y=x+t$ proves the claim.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required positivity conclusion.

:::

:::

:::
