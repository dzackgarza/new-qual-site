---
schema: qual/card@1
id: P-UCLAB18F-04
kind: problem
title: 'Monotonicity of $f(x)/x$ for $f$ with decreasing derivative'
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $f:[0,1]\to\RR$ be continuous on $[0,1]$, differentiable on $(0,1)$, with $f(0)=0$.
Suppose $f'$ is decreasing on $(0,1)$.
Show that
$$
g(x)=\frac{f(x)}x
$$
is decreasing on $(0,1)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Fix
$$
0<x<y<1.
$$
There exists
$$
\xi\in(0,x)
$$
such that
$$
\frac{f(x)}x=f'(\xi).
$$


::: pf-proof

Apply the mean value theorem to $f$ on $[0,x]$.
Since
$$
f(0)=0,
$$
there is $\xi\in(0,x)$ with
$$
\frac{f(x)-f(0)}{x-0}
=
f'(\xi).
$$

:::

:::

::: {.pf-step #s1-2}

There exists
$$
\eta\in(x,y)
$$
such that
$$
\frac{f(y)-f(x)}{y-x}
=
f'(\eta).
$$


::: pf-proof

Apply the mean value theorem to $f$ on $[x,y]$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
f'(\eta)\le f'(\xi).
$$


::: pf-proof

The points satisfy
$$
\xi<x<\eta.
$$
Since $f'$ is decreasing on $(0,1)$,
$$
f'(\eta)\le f'(\xi).
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\frac{f(y)-f(x)}{y-x}
\le
\frac{f(x)}x.
$$


::: pf-proof

Substitute the identities from steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} into the inequality of step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The inequality in step [](#s1-4){.pf-ref} implies
$$
\frac{f(y)}y
\le
\frac{f(x)}x.
$$


::: pf-proof

Multiply step [](#s1-4){.pf-ref} by $y-x>0$:
$$
f(y)-f(x)
\le
\frac{y-x}{x}f(x).
$$
Hence
$$
f(y)
\le
f(x)
+
\frac{y-x}{x}f(x)
=
\frac yx f(x).
$$
Divide by $y>0$:
$$
\frac{f(y)}y
\le
\frac{f(x)}x.
$$

:::

:::

::: {.pf-step #s1-6}

Thus
$$
\boxed{g(x)=\frac{f(x)}x\text{ is decreasing on }(0,1)}.
$$


::: pf-proof

The points
$$
0<x<y<1
$$
were arbitrary, and step [](#s1-5){.pf-ref} gives
$$
g(y)\le g(x).
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
