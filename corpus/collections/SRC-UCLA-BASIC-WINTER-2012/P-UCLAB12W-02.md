---
schema: qual/card@1
id: P-UCLAB12W-02
kind: problem
title: Pointwise convergence of convex functions to a continuous limit is uniform
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Let $f_n:[a,b]\to\RR$ be convex functions and suppose
\[
f(x)=\lim_{n\to\infty}f_n(x)
\]
exists for every $x\in[a,b]$ and is continuous on $[a,b]$.
Prove that $f_n\to f$ uniformly.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that $f_n\not\to f$ uniformly. Then there exist $\varepsilon>0$, a strictly increasing sequence $(n_k)$, and points $x_k\in[a,b]$ such that
$$
\abs{f_{n_k}(x_k)-f(x_k)}\ge\varepsilon
$$
for every $k$.


::: pf-proof

This is the negation of uniform convergence, with the indices chosen successively so that $n_k\to\infty$.

:::

:::

::: {.pf-step #s1-2}

After passing to a subsequence, there is $x\in[a,b]$ such that
$$
x_k\longrightarrow x.
$$


::: pf-proof

The interval $[a,b]$ is compact and hence sequentially compact.

:::

:::

::: {.pf-step #s1-3}

If $x\in(a,b)$, then
$$
f_{n_k}(x_k)\longrightarrow f(x).
$$


::: pf-proof

Write $g_k=f_{n_k}$. Choose fixed points
$$
p<x<q
$$
in $(a,b)$. For all sufficiently large $k$, one has $p<x_k<q$. Convexity gives
$$
g_k(x_k)
\le
\frac{q-x_k}{q-p}g_k(p)
+
\frac{x_k-p}{q-p}g_k(q).
$$
Taking the limit superior and using pointwise convergence at $p$ and $q$ gives
$$
\limsup_{k\to\infty}g_k(x_k)
\le
\frac{q-x}{q-p}f(p)
+
\frac{x-p}{q-p}f(q).
$$
Given $\eta>0$, choose $p$ and $q$ sufficiently close to $x$ that
$$
\abs{f(p)-f(x)}<\eta,
\qquad
\abs{f(q)-f(x)}<\eta.
$$
The right-hand side is then at most $f(x)+\eta$. Hence
$$
\limsup_{k\to\infty}g_k(x_k)\le f(x).
$$

For the lower bound, if $x_k\le x$, convexity implies monotonicity of secant slopes:
$$
\frac{g_k(x)-g_k(x_k)}{x-x_k}
\le
\frac{g_k(q)-g_k(x)}{q-x}.
$$
The right-hand side is bounded as $k\to\infty$, because $g_k(q)\to f(q)$ and $g_k(x)\to f(x)$. Since $x-x_k\to0$,
$$
g_k(x_k)\ge g_k(x)-o(1).
$$
If $x_k\ge x$, the slope inequality
$$
\frac{g_k(x)-g_k(p)}{x-p}
\le
\frac{g_k(x_k)-g_k(x)}{x_k-x}
$$
gives the same conclusion
$$
g_k(x_k)\ge g_k(x)-o(1).
$$
Thus in either case
$$
\liminf_{k\to\infty}g_k(x_k)\ge f(x).
$$
Combining the upper and lower bounds proves the claim.

:::

:::

::: {.pf-step #s1-4}

If $x=a$, then
$$
f_{n_k}(x_k)\longrightarrow f(a).
$$


::: pf-proof

Again write $g_k=f_{n_k}$. Fix $y\in(a,b]$. For all sufficiently large $k$, $a\le x_k<y$. By convexity,
$$
g_k(x_k)
\le
\frac{y-x_k}{y-a}g_k(a)
+
\frac{x_k-a}{y-a}g_k(y).
$$
Since $x_k\to a$, pointwise convergence at $a$ and $y$ gives
$$
\limsup_{k\to\infty}g_k(x_k)\le f(a).
$$

For the lower bound, choose $\delta>0$ with $a+2\delta\le b$ and set
$$
y=a+\delta,
\qquad
z=a+2\delta.
$$
For large $k$, $x_k<y<z$. Monotonicity of secant slopes gives
$$
\frac{g_k(y)-g_k(x_k)}{y-x_k}
\le
\frac{g_k(z)-g_k(y)}{z-y}.
$$
Hence
$$
g_k(x_k)
\ge
 g_k(y)
-(y-x_k)\frac{g_k(z)-g_k(y)}{z-y}.
$$
Taking the limit inferior yields
$$
\liminf_{k\to\infty}g_k(x_k)
\ge
2f(a+\delta)-f(a+2\delta).
$$
By continuity of $f$ at $a$, the right-hand side tends to $f(a)$ as $\delta\downarrow0$. Therefore
$$
\liminf_{k\to\infty}g_k(x_k)\ge f(a).
$$
Together with the upper bound, this proves the claim.

:::

:::

::: {.pf-step #s1-5}

If $x=b$, then
$$
f_{n_k}(x_k)\longrightarrow f(b).
$$


::: pf-proof

This is symmetric to step [](#s1-4){.pf-ref}. For the upper bound, fix $y\in[a,b)$ and use convexity on $[y,b]$; as $x_k\to b$, the convex coefficient of $g_k(b)$ tends to $1$, giving
$$
\limsup_{k\to\infty}g_k(x_k)\le f(b).
$$

For the lower bound, choose $\delta>0$ with $b-2\delta\ge a$ and set
$$
p=b-2\delta,
\qquad
y=b-\delta.
$$
For large $k$, $p<y<x_k$. Secant-slope monotonicity gives
$$
\frac{g_k(y)-g_k(p)}{y-p}
\le
\frac{g_k(x_k)-g_k(y)}{x_k-y},
$$
so
$$
g_k(x_k)
\ge
 g_k(y)
+(x_k-y)\frac{g_k(y)-g_k(p)}{y-p}.
$$
Taking the limit inferior gives
$$
\liminf_{k\to\infty}g_k(x_k)
\ge
2f(b-\delta)-f(b-2\delta).
$$
Continuity at $b$ and $\delta\downarrow0$ give the required lower bound $f(b)$.

:::

:::

::: {.pf-step #s1-6}

In every case,
$$
f_{n_k}(x_k)-f(x_k)\longrightarrow0.
$$


::: pf-proof

Steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} show that $f_{n_k}(x_k)\to f(x)$, according as $x$ is interior, $a$, or $b$. By step [](#s1-2){.pf-ref} and continuity of $f$,
$$
f(x_k)\to f(x).
$$
Subtracting gives the claim.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} contradicts the fixed lower bound
$$
\abs{f_{n_k}(x_k)-f(x_k)}\ge\varepsilon
$$
from step [](#s1-1){.pf-ref}. Therefore $f_n\to f$ uniformly on $[a,b]$.

:::

:::

:::
