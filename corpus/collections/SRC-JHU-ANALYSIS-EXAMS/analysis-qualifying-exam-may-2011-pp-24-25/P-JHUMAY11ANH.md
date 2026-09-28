---
schema: qual/card@1
id: P-JHUMAY11ANH
kind: problem
title: 'Weak $L^2$ convergence: lower semicontinuity and strong convergence from norm convergence'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $f_j\rightharpoonup f$ weakly in $L^2(\RR^n)$.

(a) Prove
$$
\norm{f}_2\le\liminf_j\norm{f_j}_2,
$$
and give an example of strict inequality.

(b) If $\norm{f_j}_2\to\norm{f}_2$, prove $\norm{f_j-f}_2\to0$.
:::

::: {.solution}
<1>1. Weak convergence implies
$$
\norm{f}_2\le\liminf_j\norm{f_j}_2.
$$
::: {.proof}
If $f=0$, the inequality is immediate. If $f\ne0$, set $g=f/\norm{f}_2$. Then $\norm{g}_2=1$, and weak convergence gives
$$
\norm{f}_2
=\abs{\inner{f}{g}}
=\lim_j\abs{\inner{f_j}{g}}
\le\liminf_j\norm{f_j}_2.
$$
:::

<1>2. Strict inequality can occur.
::: {.proof}
Let $(e_j)$ be an orthonormal sequence in $L^2(\RR^n)$. Bessel's inequality gives $e_j\rightharpoonup0$, whereas $\norm{e_j}_2=1$ for every $j$. Thus
$$
\norm{0}_2=0<1=\liminf_j\norm{e_j}_2.
$$
:::

<1>3. If $\norm{f_j}_2\to\norm{f}_2$, then
$$
\boxed{\norm{f_j-f}_2\to0}.
$$
::: {.proof}
Weak convergence gives
$$
\inner{f_j}{f}\to\inner{f}{f}=\norm{f}_2^2.
$$
Therefore
$$
\begin{aligned}
\norm{f_j-f}_2^2
&=\norm{f_j}_2^2+\norm{f}_2^2-2\operatorname{Re}\inner{f_j}{f}\\
&\longrightarrow 0.
\end{aligned}
$$
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>1 proves the lower-semicontinuity assertion in part (a), step <1>2 gives the requested strict example, and step <1>3 proves part (b).
:::
:::
