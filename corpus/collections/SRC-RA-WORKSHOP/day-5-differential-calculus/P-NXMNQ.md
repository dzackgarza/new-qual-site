---
schema: qual/card@1
id: P-NXMNQ
kind: problem
title: $f:\mathbb{R}\to\mathbb{R}$ with $f(0)=0$ is differentiable at $0$ if and only
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
Suppose that $f:\mathbb{R}\to\mathbb{R}$ satisfies $f(0)=0$.
Prove that $f$ is differentiable at $x=0$ if and only if there is a function $g:\mathbb{R}\to\mathbb{R}$ which is continuous at $x=0$ and satisfies $f(x)=xg(x)$ for all $x\in\mathbb{R}$.
:::
::: {.solution}
<1>1. If $f(x)=xg(x)$ for all $x\in\mathbb R$ and $g$ is continuous at $0$, then $f$ is differentiable at $0$ and $f'(0)=g(0)$.

::: {.proof}
For $x\ne0$, the hypothesis $f(0)=0$ gives
\[
\frac{f(x)-f(0)}{x}=\frac{xg(x)}{x}=g(x).
\]
Continuity of $g$ at $0$ implies that this difference quotient converges to $g(0)$ as $x\to0$, which is the definition of $f'(0)$.
:::

<1>2. If $f$ is differentiable at $0$, the function
\[
g(x):=\begin{cases}f(x)/x,&x\ne0,\\f'(0),&x=0\end{cases}
\]
satisfies $f(x)=xg(x)$ for every $x\in\mathbb R$.

::: {.proof}
For $x\ne0$, multiplication of $g(x)=f(x)/x$ by $x$ gives the identity. At $x=0$, both sides vanish by the hypothesis $f(0)=0$.
:::

<1>3. The function $g$ defined in step <1>2 is continuous at $0$.

::: {.proof}
For $x\ne0$, the equality $f(0)=0$ gives $g(x)=(f(x)-f(0))/x$. Differentiability of $f$ at $0$ therefore implies
\[
\lim_{x\to0}g(x)=f'(0)=g(0),
\]
which proves continuity at $0$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 proves one implication, and steps <1>2–<1>3 construct the required function for the converse.
:::
:::
