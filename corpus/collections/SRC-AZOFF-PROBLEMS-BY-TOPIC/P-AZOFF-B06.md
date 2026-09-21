---
schema: qual/card@1
id: P-AZOFF-B06
kind: problem
title: A $C^1$ function with $\|\nabla F(0,0)\|<1$ maps small disks into small intervals
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Several variables, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Chose c strictly between the norm of the gradient at the origin and 1.
    Continuity of the gradient gives a ball on which its norm is below c.
    Integrating F along each radial segment gives |F(z)| <= c||z||, hence
    |F(z)|<r on the radius-r ball. The source compilation contains no worked
    solution.
---

::: {.problem}
Let $F:\mathbb R^2\to\mathbb R$ be continuously differentiable, with $F(0,0)=0$ and
\[
\|\nabla F(0,0)\|<1.
\]
Prove that there is $r>0$ such that $|F(x,y)|<r$ whenever $\|(x,y)\|<r$.
:::

::: {.solution}
Put
$$
\alpha=\norm{\nabla F(0,0)}<1
$$
and choose
$$
c=\frac{1+\alpha}{2}.
$$
Then
$$
\alpha<c<1.
$$

<1>1. There exists $r>0$ such that
$$
\norm{\nabla F(z)}<c
$$
whenever
$$
\norm z<r.
$$

::: {.proof}
Since $F$ is continuously differentiable, its gradient is continuous at the
origin. Because
$$
c-\alpha>0,
$$
there is $r>0$ such that
$$
\norm{\nabla F(z)-\nabla F(0,0)}
<
c-\alpha
$$
whenever $\norm z<r$. The triangle inequality then gives
$$
\norm{\nabla F(z)}
\leq
\norm{\nabla F(z)-\nabla F(0,0)}
+
\norm{\nabla F(0,0)}
<
c.
$$
:::

<1>2. For every $z=(x,y)\in\RR^2$ with $\norm z<r$,
$$
\abs{F(z)}\leq c\norm z.
$$

::: {.proof}
Fix such a $z$ and define
$$
g(t)=F(tz),
\qquad
0\leq t\leq1.
$$
Then
$$
g'(t)=\nabla F(tz)\cdot z.
$$
Since
$$
\norm{tz}\leq\norm z<r,
$$
step <1>1 and Cauchy--Schwarz give
$$
\abs{g'(t)}
\leq
\norm{\nabla F(tz)}\,\norm z
<
c\norm z.
$$
Using $F(0,0)=0$ and the fundamental theorem of calculus,
$$
\begin{aligned}
\abs{F(z)}
&=
\abs{g(1)-g(0)}\\
&=
\abs{\int_0^1 g'(t)\,dt}\\
&\leq
\int_0^1\abs{g'(t)}\,dt\\
&\leq
c\norm z.
\end{aligned}
$$
:::

<1>3. Whenever $\norm{(x,y)}<r$,
$$
\boxed{\abs{F(x,y)}<r}.
$$

::: {.proof}
By step <1>2,
$$
\abs{F(x,y)}
\leq
c\norm{(x,y)}
<
cr.
$$
Since $c<1$,
$$
cr<r.
$$
Combining these inequalities gives the claim.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the required radius and estimate.
:::
:::
