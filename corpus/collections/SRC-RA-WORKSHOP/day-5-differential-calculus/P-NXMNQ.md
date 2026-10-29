---
schema: qual/card@1
id: P-NXMNQ
kind: problem
title: $f:\RR	o\RR$ with $f(0)=0$ is differentiable at $0$ if and only
  if $f(x)=xg(x)$ for a function $g$ continuous at $0$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Suppose that $f:\RR\to\RR$ satisfies $f(0)=0$.
Prove that $f$ is differentiable at $x=0$ if and only if there is a function $g:\RR\to\RR$ which is continuous at $x=0$ and satisfies $f(x)=xg(x)$ for all $x\in\RR$.
:::

::: {.solution}

::: pf

::: pf-step

If $f(x)=xg(x)$ for all $x\in\RR$ and $g$ is continuous at $0$, then $f$ is differentiable at $0$ and $f'(0)=g(0)$.

::: pf-proof

For $x\ne0$, the hypothesis $f(0)=0$ gives
$$
\frac{f(x)-f(0)}{x}=\frac{xg(x)}{x}=g(x).
$$
Continuity of $g$ at $0$ implies that this difference quotient converges to $g(0)$ as $x\to0$, which is the definition of $f'(0)$.

:::

:::

::: pf-step

If $f$ is differentiable at $0$, then the function
$$
g(x)\coloneqq\begin{cases}f(x)/x,&x\ne0,\\f'(0),&x=0\end{cases}
$$
is continuous at $0$ and satisfies $f(x)=xg(x)$ for every $x\in\RR$.

::: pf-proof

For $x\ne0$, multiplication of $g(x)=f(x)/x$ by $x$ gives the identity. At $x=0$, both sides vanish by the hypothesis $f(0)=0$.

For $x\ne0$, the equality $f(0)=0$ gives $g(x)=(f(x)-f(0))/x$. Differentiability of $f$ at $0$ therefore implies
$$
\lim_{x\to0}g(x)=f'(0)=g(0),
$$
which proves continuity at $0$.

:::

:::

:::

:::
