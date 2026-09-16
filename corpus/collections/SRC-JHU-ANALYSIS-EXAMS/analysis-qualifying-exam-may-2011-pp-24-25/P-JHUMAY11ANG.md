---
schema: qual/card@1
id: P-JHUMAY11ANG
kind: problem
title: '$L^p$ norms converge to the $L^\infty$ norm on a probability space'
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
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^\infty([0,1])$.

(a) Prove that for $1<p<\infty$,
\[
\|f\|_p\le\|f\|_\infty.
\]

(b) Prove that
\[
\lim_{p\to\infty}\|f\|_p=\|f\|_\infty.
\]
:::

::: {.solution}
<1>1. For every $1<p<\infty$,
$$
\norm{f}_p\le\norm{f}_\infty.
$$
::: {.proof}
Let $M=\norm{f}_\infty$. Since $[0,1]$ has measure $1$,
$$
\norm{f}_p^p=\int_0^1\abs{f}^p\le M^p,
$$
and taking $p$th roots gives the claim. In particular,
$$
\limsup_{p\to\infty}\norm{f}_p\le M.
$$
:::

<1>2. If $M>0$, then
$$
\liminf_{p\to\infty}\norm{f}_p\ge M.
$$
::: {.proof}
Fix $0<\varepsilon<M$. By the definition of essential supremum,
$$
A_\varepsilon=\{x:\abs{f(x)}>M-\varepsilon\}
$$
has positive measure. Therefore
$$
\norm{f}_p^p\ge (M-\varepsilon)^p m(A_\varepsilon),
$$
so
$$
\norm{f}_p\ge (M-\varepsilon)m(A_\varepsilon)^{1/p}.
$$
Letting $p\to\infty$ gives
$$
\liminf_{p\to\infty}\norm{f}_p\ge M-\varepsilon.
$$
Since $\varepsilon>0$ is arbitrary,
$$
\liminf_{p\to\infty}\norm{f}_p\ge M.
$$
:::

<1>3. Therefore
$$
\boxed{
\lim_{p\to\infty}\norm{f}_p=\norm{f}_\infty.
}
$$
::: {.proof}
If $M=0$, then $f=0$ almost everywhere and the result is immediate. If $M>0$, combine the limsup bound from step <1>1 with the liminf bound from step <1>2.
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>1 proves part (a), and step <1>3 proves part (b).
:::
:::
