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
Let $M\geq0$ satisfy $|f'(t)|\leq M$ for all $t\in(a,b]$.

::: pf

::: {.pf-step #s1}

For all $a<x<y\leq b$, one has $|f(y)-f(x)|\leq M(y-x)$.

::: pf-proof

Differentiability implies continuity on $[x,y]$ and differentiability on $(x,y)$. The mean value theorem gives $\xi\in(x,y)$ such that $f(y)-f(x)=f'(\xi)(y-x)$. The bound on $f'$ yields the claimed inequality.

:::

:::

::: {.pf-step #s2}

The sequence $f(a+(b-a)/n)$, for positive integers $n$, converges to some $L\in\mathbb R$.

::: pf-proof

Put $x_n=a+(b-a)/n$. By step [](#s1){.pf-ref}, for all positive integers $m,n$,
\[
|f(x_n)-f(x_m)|\leq M|x_n-x_m|.
\]
Since $(x_n)$ converges to $a$, it is Cauchy, so $(f(x_n))$ is Cauchy. Completeness of $\mathbb R$ gives its limit $L$.

:::

:::

::: {.pf-step #s3}

The right-hand limit is $\boxed{\lim_{x\to a^+}f(x)=L}$.

::: pf-proof

For $x\in(a,b]$, step [](#s1){.pf-ref} and the triangle inequality give
\[
|f(x)-L|\leq M|x-x_n|+|f(x_n)-L|.
\]
Letting $n\to\infty$ and using step [](#s2){.pf-ref} yields $|f(x)-L|\leq M(x-a)$. Given $\varepsilon>0$, choose $\delta=\min\{b-a,\varepsilon/(M+1)\}>0$. If $a<x<a+\delta$, then $|f(x)-L|\leq M(x-a)<\varepsilon$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} establishes the required finite right-hand limit.

:::

:::

:::
