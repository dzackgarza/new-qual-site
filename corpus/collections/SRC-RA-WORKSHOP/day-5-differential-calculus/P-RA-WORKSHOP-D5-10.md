---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-10
kind: problem
title: A differential inequality with zero initial value
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(January 2005 #6) Suppose that $f:[0,1]\to\mathbb R$ is a differentiable function with $f(0)=0$ and that there exists some $K>0$ so that $|f'(x)|\le K|f(x)|$ for all $x\in[0,1]$.
Prove that $f(x)=0$ on $[0,1]$.

Note: See [Rud76, Chap 5, #26] for a significant hint.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function $f$ is bounded: there is $M\geq0$ with $|f(x)|\leq M$ for every $x\in[0,1]$.

::: pf-proof

Differentiability implies continuity, and a continuous real-valued function on the compact interval $[0,1]$ is bounded. Choose $M=\max_{x\in[0,1]}|f(x)|$.

:::

:::

::: {.pf-step #s2}

For every integer $n\geq0$ and every $x\in[0,1]$,
\[
|f(x)|\leq\frac{MK^n x^n}{n!}.
\]

::: pf-proof

Proceed by induction on $n$. The case $n=0$ follows from step [](#s1){.pf-ref}. Suppose the bound holds for $n$. Define $h_n(t)=MK^n t^n/n!$ and
\[
H_n(x)=\frac{MK^{n+1}x^{n+1}}{(n+1)!}.
\]
The induction hypothesis and the differential inequality give $|f'(t)|\leq K h_n(t)=H_n'(t)$ on $(0,1)$. Thus both $H_n+f$ and $H_n-f$ have nonnegative derivative on $(0,1)$ and are nondecreasing on $[0,1]$ by the mean value theorem. Since $H_n(0)=f(0)=0$, one has $-H_n(x)\leq f(x)\leq H_n(x)$ for every $x\in[0,1]$. This is the bound for $n+1$.

:::

:::

::: {.pf-step #s3}

The function satisfies $\boxed{f(x)=0\text{ for all }x\in[0,1]}$.

::: pf-proof

Fix $x\in[0,1]$. By step [](#s2){.pf-ref}, for every $n\geq0$,
\[
0\leq|f(x)|\leq M\frac{(Kx)^n}{n!}.
\]
The right-hand side converges to zero: if $A=Kx$, the ratio of consecutive terms $A^n/n!$ is $A/(n+1)$, eventually at most $1/2$. Therefore $f(x)=0$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the assertion on the entire interval.

:::

:::

:::
