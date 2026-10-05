---
schema: qual/card@1
id: P-UCLAB04F-02
kind: problem
title: State and prove Rolle's theorem
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the official UCLA Basic Exam Fall 2004 PDF.
---

::: {.problem}
State and prove Rolle's Theorem.

You may use without proof theorems about maxima and minima of continuous or differentiable functions.
:::

::: {.solution}
<1>1. Rolle's Theorem states: if $f:[a,b]\to\mathbb R$ is continuous on $[a,b]$, differentiable on $(a,b)$, and
\[
f(a)=f(b),
\]
then there exists $c\in(a,b)$ such that
\[
\boxed{f'(c)=0}.
\]

::: {.proof}
This is the statement to be proved.
:::

<1>2. If $f$ is constant on $[a,b]$, then the conclusion holds.

::: {.proof}
If
\[
f(x)=f(a)
\]
for every $x\in[a,b]$, then
\[
f'(c)=0
\]
for every $c\in(a,b)$. Since $a<b$, such points exist.
:::

<1>3. Suppose $f$ is not constant. Then either its maximum or its minimum on $[a,b]$ is attained at an interior point $c\in(a,b)$.

::: {.proof}
By continuity on the compact interval $[a,b]$, the function attains both a maximum and a minimum.

Because $f(a)=f(b)$ and $f$ is not constant, there is some $x\in(a,b)$ with
\[
f(x)\ne f(a).
\]
If $f(x)>f(a)$, then the maximum value is strictly larger than the endpoint value and therefore cannot be attained only at $a$ or $b$; some maximizing point lies in $(a,b)$. If $f(x)<f(a)$, the same argument applied to the minimum gives an interior minimizing point.
:::

<1>4. At the interior extremum $c$ from step <1>3,
\[
f'(c)=0.
\]

::: {.proof}
Suppose first that $c$ is a local maximum. For all sufficiently small $h>0$,
\[
\frac{f(c+h)-f(c)}{h}\le0,
\]
while for all sufficiently small $h<0$,
\[
\frac{f(c+h)-f(c)}{h}\ge0.
\]
Since $f'(c)$ exists, the right and left difference quotients have the same limit. That common limit must be both nonpositive and nonnegative, hence zero.

The proof for a local minimum is identical with the inequalities reversed.
:::

<1>5. Rolle's Theorem holds.

::: {.proof}
Step <1>2 handles the constant case. If $f$ is nonconstant, steps <1>3--<1>4 produce $c\in(a,b)$ with $f'(c)=0$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the theorem stated in step <1>1.
:::
:::
