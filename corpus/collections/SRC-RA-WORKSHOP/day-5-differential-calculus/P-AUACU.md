---
schema: qual/card@1
id: P-AUACU
kind: problem
title: A bounded derivative on $(a,b]$ implies $\lim_{x\to a^+}f(x)$ exists
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Prove that if $f'$ exists and is bounded on $(a,b]$, then $\lim_{x\to a^+}f(x)$ exists.
:::

::: {.solution}
Let $M\geq0$ satisfy $\abs{f'(t)}\leq M$ for all $t\in(a,b]$.

::: pf

::: {.pf-step #s1}

For all $a<x<y\leq b$, one has $\abs{f(y)-f(x)}\leq M(y-x)$.

::: pf-proof

Differentiability implies continuity on $[x,y]$ and differentiability on $(x,y)$. The mean value theorem gives $\xi\in(x,y)$ such that $f(y)-f(x)=f'(\xi)(y-x)$. The bound on $f'$ yields the claimed inequality.

:::

:::

::: {.pf-step #s2}

The sequence $f(a+(b-a)/n)$, for positive integers $n$, converges to some $L\in\RR$.

::: pf-proof

Put $x_n=a+(b-a)/n$. By step [](#s1){.pf-ref}, for all positive integers $m,n$,
$$
\abs{f(x_n)-f(x_m)}\leq M\abs{x_n-x_m}.
$$
Since $(x_n)$ converges to $a$, it is Cauchy, so $(f(x_n))$ is Cauchy. Completeness of $\RR$ gives its limit $L$.

:::

:::

::: pf-step

$\lim_{x\to a^+}f(x)=L$.

::: pf-proof

For $x\in(a,b]$, step [](#s1){.pf-ref} and the triangle inequality give
$$
\abs{f(x)-L}\leq M\abs{x-x_n}+\abs{f(x_n)-L}.
$$
Letting $n\to\infty$ and using step [](#s2){.pf-ref} yields $\abs{f(x)-L}\leq M(x-a)$. Given $\varepsilon>0$, choose $\delta=\min\{b-a,\varepsilon/(M+1)\}>0$. If $a<x<a+\delta$, then $\abs{f(x)-L}\leq M(x-a)<\varepsilon$.

:::

:::

:::

:::
