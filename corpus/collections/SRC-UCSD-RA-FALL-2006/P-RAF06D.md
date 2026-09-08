---
schema: qual/card@1
id: P-RAF06D
kind: problem
title: "Characterizations of convex functions: secant slopes and monotone derivative"
classification:
  areas:
  - real-analysis
  topics:
  - Convex Functions
  - Absolute Continuity
  - Monotone Derivatives
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2006 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Recall that a function $f : (a, b) \to \mathbb{R}$ (with $-\infty \leq a < b \leq \infty$) is called convex if
$$
f((1-\lambda)x + \lambda y) \leq (1-\lambda)f(x) + \lambda f(y), \quad \forall \lambda \in (0, 1), x, y \in (a, b).
$$

(a) Show that $f$ is convex if and only if for all $x, y, x', y' \in (a, b)$ with $x \leq x' < y'$ and $x < y \leq y'$,
$$
\frac{f(y) - f(x)}{y - x} \leq \frac{f(y') - f(x')}{y' - x'}.
$$

(b) Show that $f$ is convex if and only if $f$ is absolutely continuous on every compact subinterval $[c, d]$ of $(a, b)$ and $f'$ is increasing a.e.
:::

::: solution
<1>1. Record the three-point secant-slope inequality for a convex function.
::: proof
For $u<v<w$, convexity at
\[
v=(1-\lambda)u+\lambda w,
\qquad
\lambda=\frac{v-u}{w-u},
\]
gives
\[
f(v)\le \frac{w-v}{w-u}f(u)+\frac{v-u}{w-u}f(w).
\]
Rearranging yields
\[
\frac{f(v)-f(u)}{v-u}
\le
\frac{f(w)-f(u)}{w-u}.
\]
The same inequality, rearranged in the other direction, also gives
\[
\frac{f(w)-f(u)}{w-u}
\le
\frac{f(w)-f(v)}{w-v}.
\]
Thus for every $u<v<w$,
\[
\frac{f(v)-f(u)}{v-u}
\le
\frac{f(w)-f(u)}{w-u}
\le
\frac{f(w)-f(v)}{w-v}.
\]
:::

<1>2. Prove the forward implication in part (a).
::: proof
Write
\[
s(u,v):=\frac{f(v)-f(u)}{v-u}.
\]
Suppose $x\le x'<y'$ and $x<y\le y'$.

If $x'<y$, Step 1 gives
\[
s(x,y)\le s(x',y)\le s(x',y').
\]
If $y\le x'$, then repeated use of Step 1 across the ordered points gives
\[
s(x,y)\le s(y,x')\le s(x',y')
\]
when $y<x'$, while for $y=x'$ the first inequality is replaced directly by
\[
s(x,y)\le s(y,y').
\]
Hence in every case
\[
\boxed{s(x,y)\le s(x',y').}
\]
:::

<1>3. Prove the converse implication in part (a).
::: proof
Assume the stated secant-slope inequality. Let $x<z<y$. Apply it with
\[
x'=x,
\qquad
y'=y,
\qquad
y=z.
\]
Then
\[
\frac{f(z)-f(x)}{z-x}
\le
\frac{f(y)-f(x)}{y-x}.
\]
Writing
\[
\lambda=\frac{z-x}{y-x}\in(0,1)
\]
and rearranging gives
\[
f(z)\le (1-\lambda)f(x)+\lambda f(y).
\]
This is exactly convexity.
:::

<1>4. A convex function is locally absolutely continuous and has an a.e.-increasing derivative.
::: proof
Let $[c,d]\subset(a,b)$ be compact. Choose
\[
a<c_0<c<d<d_0<b.
\]
For $c\le x<y\le d$, Step 2 gives
\[
s(c_0,c)\le s(x,y)\le s(d,d_0).
\]
Hence all secant slopes on $[c,d]$ are uniformly bounded in absolute value. Thus $f$ is Lipschitz on $[c,d]$, so it is absolutely continuous there.

A Lipschitz function is differentiable almost everywhere. Let $x<y$ be two differentiability points. For sufficiently small $h>0$ with $x+h<y-h$, Step 2 yields
\[
s(x,x+h)\le s(y-h,y).
\]
Letting $h\downarrow0$ gives
\[
f'(x)\le f'(y).
\]
Therefore $f'$ is increasing on the full-measure set where it exists, i.e. increasing a.e.
:::

<1>5. Local absolute continuity plus an a.e.-increasing derivative implies convexity.
::: proof
Assume $f$ is absolutely continuous on compact subintervals and that $f'$ is increasing a.e. Let $x<z<y$ in $(a,b)$. Absolute continuity gives
\[
f(z)-f(x)=\int_x^z f'(s)\,ds,
\qquad
f(y)-f(z)=\int_z^y f'(t)\,dt.
\]
For almost every pair $(s,t)\in(x,z)\times(z,y)$ we have $s<t$, hence
\[
f'(s)\le f'(t).
\]
Integrating this nonnegative difference over the rectangle gives
\[
(z-x)\int_z^y f'(t)\,dt
\ge
(y-z)\int_x^z f'(s)\,ds.
\]
Therefore
\[
\frac{f(z)-f(x)}{z-x}
\le
\frac{f(y)-f(z)}{y-z}.
\]
This adjacent-secant inequality is equivalent to
\[
\frac{f(z)-f(x)}{z-x}
\le
\frac{f(y)-f(x)}{y-x},
\]
and Step 3 shows that this is equivalent to convexity. Hence $f$ is convex.
:::
:::
