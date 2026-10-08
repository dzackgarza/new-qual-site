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

<1>1. For all $a<x<y\leq b$, one has $|f(y)-f(x)|\leq M(y-x)$.

::: {.proof}
Differentiability implies continuity on $[x,y]$ and differentiability on $(x,y)$. The mean value theorem gives $\xi\in(x,y)$ such that $f(y)-f(x)=f'(\xi)(y-x)$. The bound on $f'$ yields the claimed inequality.
:::

<1>2. The sequence $f(a+(b-a)/n)$, for positive integers $n$, converges to some $L\in\mathbb R$.

::: {.proof}
Put $x_n=a+(b-a)/n$. By step <1>1, for all positive integers $m,n$,
\[
|f(x_n)-f(x_m)|\leq M|x_n-x_m|.
\]
Since $(x_n)$ converges to $a$, it is Cauchy, so $(f(x_n))$ is Cauchy. Completeness of $\mathbb R$ gives its limit $L$.
:::

<1>3. The right-hand limit is $\boxed{\lim_{x\to a^+}f(x)=L}$.

::: {.proof}
For $x\in(a,b]$, step <1>1 and the triangle inequality give
\[
|f(x)-L|\leq M|x-x_n|+|f(x_n)-L|.
\]
Letting $n\to\infty$ and using step <1>2 yields $|f(x)-L|\leq M(x-a)$. Given $\varepsilon>0$, choose $\delta=\min\{b-a,\varepsilon/(M+1)\}>0$. If $a<x<a+\delta$, then $|f(x)-L|\leq M(x-a)<\varepsilon$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 establishes the required finite right-hand limit.
:::
:::
