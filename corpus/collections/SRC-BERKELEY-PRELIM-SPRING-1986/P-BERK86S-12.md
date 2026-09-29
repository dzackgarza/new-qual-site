---
schema: qual/card@1
id: P-BERK86S-12
kind: problem
title: A mean-value subfunction inequality forces convexity
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
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Proved the maximum principle by showing that an interior maximizer forces
    a neighborhood of maximizers, making the interior maximum set clopen.
    Subtracting an affine chord preserves the submean inequality, so the
    maximum principle yields the chord characterization of convexity.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and suppose
\[
f(x)\le\frac1{2h}\int_{x-h}^{x+h}f(y)\,dy
\]
for every $x\in\mathbb R$ and $h>0$.

1. Prove that the maximum of $f$ on any closed interval is attained at one of the endpoints.
2. Prove that $f$ is convex.
:::

::: {.solution}
::: pf

::: {.pf-step #local-constancy-at-max}
Fix a closed interval $[a,b]$ with $a<b$, and let
$$
M\coloneqq\max_{x\in[a,b]}f(x).
$$
If $x_0\in(a,b)$ satisfies $f(x_0)=M$, then there is an open interval
around $x_0$ on which $f$ is identically $M$.

::: pf-proof
Choose
$$
0<h<\min\{x_0-a,b-x_0\}.
$$
Since $f(y)\leq M$ throughout $[a,b]$,
$$
M
=
f(x_0)
\leq
\frac1{2h}\int_{x_0-h}^{x_0+h}f(y)\,dy
\leq
M.
$$
Thus
$$
\frac1{2h}\int_{x_0-h}^{x_0+h}f(y)\,dy=M.
$$
If $f(y_0)<M$ at some point of this interval, continuity would give a
nontrivial subinterval on which $f\leq M-\varepsilon$ for some
$\varepsilon>0$, forcing the average to be strictly less than $M$.
Therefore
$$
f(y)=M
$$
for every $y\in[x_0-h,x_0+h]$.
:::

:::

::: {.pf-step #max-at-endpoint-boxed}
The maximum of $f$ on $[a,b]$ is attained at an endpoint.

::: pf-proof
Let
$$
S\coloneqq\{x\in(a,b):f(x)=M\}.
$$
The set $S$ is closed in $(a,b)$ because $f$ is continuous. By step
[](#local-constancy-at-max){.pf-ref}, it is also open in $(a,b)$.

If $S=\varnothing$, then no interior point attains the maximum, so an
endpoint does. If $S\neq\varnothing$, connectedness of $(a,b)$ gives
$$
S=(a,b).
$$
Continuity at the endpoints then gives
$$
f(a)=f(b)=M.
$$
Thus in every case
$$
\boxed{
\max_{x\in[a,b]}f(x)=\max\{f(a),f(b)\}
}.
$$
:::

:::

::: {.pf-step #subtract-affine-preserves}
If $\ell:\RR\to\RR$ is affine and
$$
g\coloneqq f-\ell,
$$
then $g$ satisfies the same submean inequality:
$$
g(x)
\leq
\frac1{2h}\int_{x-h}^{x+h}g(y)\,dy.
$$

::: pf-proof
Write
$$
\ell(y)=cy+d.
$$
Then
$$
\frac1{2h}\int_{x-h}^{x+h}\ell(y)\,dy
=
cx+d
=
\ell(x).
$$
Subtract this equality from the assumed inequality for $f$.
:::

:::

::: {.pf-step #chord-inequality}
For every $a<b$ and every $x\in[a,b]$,
$$
f(x)
\leq
\frac{b-x}{b-a}f(a)
+
\frac{x-a}{b-a}f(b).
$$

::: pf-proof
Let $\ell$ be the affine function whose graph is the chord joining
$(a,f(a))$ and $(b,f(b))$:
$$
\ell(x)
\coloneqq
\frac{b-x}{b-a}f(a)
+
\frac{x-a}{b-a}f(b).
$$
Set $g=f-\ell$. By step [](#subtract-affine-preserves){.pf-ref}, $g$ satisfies the same submean inequality.
Moreover,
$$
g(a)=g(b)=0.
$$
Apply step [](#max-at-endpoint-boxed){.pf-ref} to $g$ on $[a,b]$. Its maximum is attained at an
endpoint and therefore equals $0$. Hence
$$
g(x)\leq0
$$
throughout $[a,b]$, which is exactly the displayed inequality.
:::

:::

::: {.pf-step #convex-boxed}
The function $f$ is convex.

::: pf-proof
Let $x,y\in\RR$ and $0\leq t\leq1$. If $x=y$, the convexity inequality is
an equality. Otherwise, after interchanging $x$ and $y$ if necessary,
assume $x<y$ and apply step [](#chord-inequality){.pf-ref} at
$$
z=(1-t)x+ty.
$$
Since
$$
\frac{y-z}{y-x}=1-t,
\qquad
\frac{z-x}{y-x}=t,
$$
step [](#chord-inequality){.pf-ref} gives
$$
f((1-t)x+ty)
\leq
(1-t)f(x)+tf(y).
$$
Thus
$$
\boxed{f\text{ is convex on }\RR}.
$$
:::

:::

::: pf-qed
Step [](#max-at-endpoint-boxed){.pf-ref} proves part 1 and step [](#convex-boxed){.pf-ref} proves part 2.
:::

:::
:::
