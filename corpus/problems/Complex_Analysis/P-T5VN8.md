---
schema: qual/card@1
id: P-T5VN8
kind: problem
title: $f(x)/x$ is increasing when $f'$ is increasing and $f(0)=0$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
relations: []
review: draft
---

::: {.problem}
Let $f:[0,\infty)\to\RR$ be continuous, differentiable on
$(0,\infty)$, satisfy $f(0)=0$, and suppose $f'$ is increasing. For
$x>0$ define $g(x)=f(x)/x$. Prove that $g$ is increasing.
:::

::: {.solution}
Fix $0<x<y$.

::: pf

::: {.pf-step #slopes}

$\dfrac{f(y)-f(x)}{y-x} \ge \dfrac{f(x)}{x}$.

::: pf-proof

By the mean value theorem there are $\xi\in(0,x)$ and $\eta\in(x,y)$ such that
$$
\frac{f(x)-f(0)}{x}=f'(\xi),
\qquad
\frac{f(y)-f(x)}{y-x}=f'(\eta).
$$
Since $\xi<\eta$ and $f'$ is increasing, $f'(\eta)\ge f'(\xi)$, and $f(0)=0$.

:::

:::

::: pf-step

$g(y)\ge g(x)$.

::: pf-proof

By step [](#slopes){.pf-ref},
$$
f(y)\ge f(x)+(y-x)\frac{f(x)}{x}=y\,\frac{f(x)}{x},
$$
and dividing by $y>0$ gives $f(y)/y\ge f(x)/x$.

:::

:::

:::

:::