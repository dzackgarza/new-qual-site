---
schema: qual/card@1
id: P-BKS88-1
kind: problem
title: Differentiability at a point from the limit of the derivative
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
  note: Checked against the vendored UC Berkeley Spring 1988 preliminary examination.
---

::: {.problem}
Suppose that $f(x)$, $-\infty<x<\infty$, is a continuous real valued function, that $f'(x)$ exists for $x\neq0$, and that $\lim_{x\to0}f'(x)$ exists.
Prove that $f'(0)$ exists.
:::

::: {.solution}
Let
\[
L:=\lim_{x\to 0} f'(x).
\]

<1>1. For every $h\neq 0$, there is a point $c_h$ strictly between $0$ and $h$ such that
\[
\frac{f(h)-f(0)}{h}=f'(c_h).
\]

::: {.proof}
If $h>0$, the function $f$ is continuous on $[0,h]$ and differentiable on $(0,h)$, so the mean value theorem gives such a point $c_h\in(0,h)$. If $h<0$, apply the mean value theorem on $[h,0]$ to obtain $c_h\in(h,0)$. In either case,
\[
f(h)-f(0)=f'(c_h)h,
\]
which gives the displayed identity.
:::

<1>2. The difference quotient of $f$ at $0$ tends to $L$ as $h\to 0$.

::: {.proof}
By step <1>1, for each $h\neq 0$ choose $c_h$ strictly between $0$ and $h$. Then
\[
0<|c_h|<|h|,
\]
so $c_h\to 0$ as $h\to 0$. Since $c_h\neq 0$ and $f'(x)\to L$ as $x\to 0$, it follows that
\[
\lim_{h\to 0}\frac{f(h)-f(0)}{h}
=\lim_{h\to 0}f'(c_h)
=L.
\]
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2, the defining limit for $f'(0)$ exists and equals $L$.
:::
:::
