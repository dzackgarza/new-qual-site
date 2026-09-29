---
schema: qual/card@1
id: P-BKS84-3
kind: problem
title: A differential inequality with zero boundary data forces nonpositivity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the integrating-factor reduction to a convex function and the mean-value-theorem argument forcing it below its zero endpoint chord.
---

::: {.problem}
Let $f:[0,1]\to\mathbb R$ be continuous with
\[
f(0)=f(1)=0.
\]
Suppose $f''$ exists on $(0,1)$ and
\[
f''+2f'+f\ge0.
\]
Prove that
\[
f(x)\le0
\]
for every $0\le x\le1$.
:::

::: {.solution}
::: pf

::: {.pf-step #g-convex-setup}
Define
$$
g(x)\coloneqq e^x f(x).
$$
Then $g$ is continuous on $[0,1]$, twice differentiable on $(0,1)$,
$g(0)=g(1)=0$, and
$$
g''(x)\geq0
$$
for $0<x<1$.

::: pf-proof
The endpoint conditions give
$$
g(0)=f(0)=0,
\qquad
g(1)=e f(1)=0.
$$
On $(0,1)$,
$$
\begin{aligned}
g''(x)
&=
e^x\bigl(f''(x)+2f'(x)+f(x)\bigr)\\
&\geq0,
\end{aligned}
$$
because $e^x>0$ and the assumed differential inequality holds.
:::

:::

::: {.pf-step #g-prime-nondecreasing}
The derivative $g'$ is nondecreasing on $(0,1)$.

::: pf-proof
Let $0<a<b<1$. Since $g''$ exists on $(0,1)$, the function $g'$ is
continuous on $[a,b]$ and differentiable on $(a,b)$. By the mean value
theorem, for some $c\in(a,b)$,
$$
g'(b)-g'(a)
=
g''(c)(b-a)
\geq0
$$
by step [](#g-convex-setup){.pf-ref}. Hence $g'(a)\leq g'(b)$.
:::

:::

::: {.pf-step #g-nonpositive}
For every $x\in(0,1)$,
$$
g(x)\leq0.
$$

::: pf-proof
Fix $x\in(0,1)$. The mean value theorem on $[0,x]$ gives
$c\in(0,x)$ such that
$$
\frac{g(x)-g(0)}{x}
=
g'(c),
$$
and the mean value theorem on $[x,1]$ gives $d\in(x,1)$ such that
$$
\frac{g(1)-g(x)}{1-x}
=
g'(d).
$$
Since $c<d$, step [](#g-prime-nondecreasing){.pf-ref} gives $g'(c)\leq g'(d)$. Using
$g(0)=g(1)=0$ from step [](#g-convex-setup){.pf-ref},
$$
\frac{g(x)}{x}
\leq
-\frac{g(x)}{1-x}.
$$
Multiplication by the positive number $x(1-x)$ yields
$$
(1-x)g(x)\leq-xg(x),
$$
and therefore $g(x)\leq0$.
:::

:::

::: {.pf-step #f-nonpositive-boxed}
For every $x\in[0,1]$,
$$
\boxed{f(x)\leq0}.
$$

::: pf-proof
For $0<x<1$, step [](#g-nonpositive){.pf-ref} and
$$
f(x)=e^{-x}g(x)
$$
give $f(x)\leq0$ because $e^{-x}>0$. At the endpoints,
$f(0)=f(1)=0$ by hypothesis.
:::

:::

::: pf-qed
Step [](#f-nonpositive-boxed){.pf-ref} is the required conclusion.
:::

:::
:::
