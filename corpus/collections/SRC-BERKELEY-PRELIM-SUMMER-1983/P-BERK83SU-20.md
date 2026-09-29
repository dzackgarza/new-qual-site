---
schema: qual/card@1
id: P-BERK83SU-20
kind: problem
title: Uniform decay of the derivative of $f/(1+cf)$ for a nonnegative periodic function
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The derivative is f'/(1+cf)^2. Every zero of the nonnegative C^1
    function f is a minimum, so f' vanishes there. On one compact period,
    the set where |f'| is not already small is therefore separated from the
    zero set of f, giving a positive lower bound for f and uniform decay.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuously differentiable, nonnegative, and periodic of period $1$. Prove that
\[
\frac{d}{dx}\left(\frac{f(x)}{1+cf(x)}\right)\longrightarrow0
\qquad(c\to\infty)
\]
uniformly in $x$.
:::

::: {.solution}
For $c\ge0$, set
$$
g_c(x)=\frac{f(x)}{1+cf(x)}.
$$

::: pf

::: {.pf-step #s1}

One has
$$
g_c'(x)=\frac{f'(x)}{(1+cf(x))^2}.
$$

::: pf-proof

Differentiating by the quotient rule gives
$$
g_c'(x)
=
\frac{f'(x)(1+cf(x))-cf(x)f'(x)}
{(1+cf(x))^2}
=
\frac{f'(x)}{(1+cf(x))^2}.
$$

:::

:::

::: {.pf-step #s2}

If $f(x_0)=0$, then $f'(x_0)=0$.

::: pf-proof

Since $f\ge0$, any point $x_0$ with $f(x_0)=0$ is a local minimum of
the differentiable function $f$. Hence Fermat's theorem gives
$f'(x_0)=0$.

:::

:::

::: {.pf-step #s3}

Fix $\varepsilon>0$, and let
$$
K
=
\left\{
t\in[0,1]:
\abs{f'(t)}\ge\varepsilon
\right\}.
$$
If $K$ is nonempty, then
$$
m\coloneqq\min_{t\in K}f(t)>0.
$$

::: pf-proof

The set $K$ is closed in the compact interval $[0,1]$, hence compact.
By step [](#s2){.pf-ref}, no point of $K$ can be a zero of $f$. Thus $f>0$ on
$K$. If $K$ is nonempty, continuity of $f$ and compactness of $K$
imply that $f$ attains there a strictly positive minimum $m$.

:::

:::

::: {.pf-step #s4}

There exists $C>0$ such that for every $c\ge C$ and every
$x\in\RR$,
$$
\abs{g_c'(x)}<\varepsilon.
$$

::: pf-proof

Let
$$
M=\max_{t\in[0,1]}\abs{f'(t)}.
$$
If the set $K$ from step [](#s3){.pf-ref} is empty, then
$\abs{f'(x)}<\varepsilon$ for every $x$ by periodicity, and step
[](#s1){.pf-ref} gives
$$
\abs{g_c'(x)}
\le
\abs{f'(x)}
<
\varepsilon
$$
for every $c\ge0$.

Suppose instead that $K$ is nonempty, and let $m>0$ be as in step
[](#s3){.pf-ref}. Choose $C>0$ so large that
$$
\frac{M}{(1+Cm)^2}<\varepsilon.
$$
For any $x\in\RR$, periodicity lets us choose $t\in[0,1]$ with
$$
f(x)=f(t),
\qquad
f'(x)=f'(t).
$$
If $t\notin K$, then $\abs{f'(t)}<\varepsilon$, and step [](#s1){.pf-ref}
again gives $\abs{g_c'(x)}<\varepsilon$.

If $t\in K$, then $f(t)\ge m$, so for $c\ge C$,
$$
\abs{g_c'(x)}
\le
\frac{M}{(1+cm)^2}
\le
\frac{M}{(1+Cm)^2}
<
\varepsilon.
$$
Thus the same bound holds for every $x$.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
g_c'\longrightarrow0
\quad\text{uniformly on $\RR$ as $c\to\infty$}
}.
$$

::: pf-proof

Step [](#s4){.pf-ref} is exactly the $\varepsilon$-definition of uniform
convergence of $g_c'$ to $0$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
