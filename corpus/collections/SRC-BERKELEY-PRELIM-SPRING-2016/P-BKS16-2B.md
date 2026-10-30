---
schema: qual/card@1
id: P-BKS16-2B
kind: problem
title: Pointwise limits of convex functions are convex
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Checked the statement against Problem 2B in the vendored Berkeley Spring 2016 exam and independently reviewed the supplied solution.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the midpoint-convexity passage to the pointwise limit and the symmetric second-difference limit for a twice-differentiable function.
---

::: {.problem}
Let $(f_i)_{i=1}^\infty$ and $g$ be twice-differentiable real-valued functions on $\RR$, with $f_i''\ge 0$.
Suppose that
$$
\lim_{i\to\infty} f_i(x)=g(x)
$$
for all $x\in\RR$.
Show that $g''\ge 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $i\geq1$ and every $z,h\in\RR$,
$$
2f_i(z)\leq f_i(z+h)+f_i(z-h).
$$


::: pf-proof

It is enough to take $h>0$. Since $f_i''\geq0$, the derivative $f_i'$ is nondecreasing. Hence for $0\leq s\leq h$,
$$
f_i'(z+s)\geq f_i'(z-s).
$$
Integrating over $s\in[0,h]$ gives
$$
f_i(z+h)-f_i(z)
\geq
f_i(z)-f_i(z-h),
$$
which rearranges to the displayed inequality. The case $h<0$ is the same after replacing $h$ by $-h$, and $h=0$ is equality.

:::

:::

::: {.pf-step #s1-2}

For every $z,h\in\RR$,
$$
2g(z)\leq g(z+h)+g(z-h).
$$


::: pf-proof

Fix $z$ and $h$. By step [](#s1-1){.pf-ref},
$$
2f_i(z)\leq f_i(z+h)+f_i(z-h)
$$
for every $i$. Taking $i\to\infty$ and using the assumed pointwise convergence at the three points $z$, $z+h$, and $z-h$ gives the claimed inequality.

:::

:::

::: {.pf-step #s1-3}

For every $z\in\RR$,
$$
g''(z)\geq0.
$$


::: pf-proof

For $h\neq0$, step [](#s1-2){.pf-ref} gives
$$
\frac{g(z+h)-2g(z)+g(z-h)}{h^2}\geq0.
$$
Because $g$ is twice differentiable at $z$,
$$
g(z\pm h)
=
g(z)\pm g'(z)h+\frac12g''(z)h^2+o(h^2).
$$
Therefore
$$
g''(z)
=
\lim_{h\to0}
\frac{g(z+h)-2g(z)+g(z-h)}{h^2},
$$
and the limit of the nonnegative quantities on the right is nonnegative.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the required inequality at every real $z$.

:::

:::

:::
