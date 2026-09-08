---
schema: qual/card@1
id: P-JHUSP08ANB
kind: problem
title: '$\|f\|_p\to\|f\|_\infty$ on $[0,1]$, with a counterexample on $\RR$'
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
  note: Checked against Problem 2 of the JHU Analysis Qualifying Exam, Spring 2008, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
(a) Let $f\in L^\infty([0,1])$. Prove that
\[
\lim_{p\to\infty}\left(\int_0^1|f|^p\,dx\right)^{1/p}=\|f\|_\infty.
\]

(b) Give an example showing that the corresponding statement fails if $[0,1]$ is replaced by $\mathbb R$.
:::

::: {.solution}
<1>1. The limit on $[0,1]$ equals the essential supremum.
::: {.proof}
Let
\[
M=\|f\|_\infty.
\]
Since $[0,1]$ has measure $1$,
\[
\|f\|_p\le M
\qquad(1\le p<\infty).
\]
Thus
\[
\limsup_{p\to\infty}\|f\|_p\le M.
\]

Fix $\varepsilon>0$. By the definition of essential supremum, the set
\[
E_\varepsilon=\{x\in[0,1]:|f(x)|>M-\varepsilon\}
\]
has positive measure. Therefore
\[
\|f\|_p^p
\ge \int_{E_\varepsilon}|f|^p
\ge (M-\varepsilon)^p m(E_\varepsilon),
\]
so
\[
\|f\|_p\ge (M-\varepsilon)m(E_\varepsilon)^{1/p}.
\]
Letting $p\to\infty$ gives
\[
\liminf_{p\to\infty}\|f\|_p\ge M-\varepsilon.
\]
Since $\varepsilon>0$ is arbitrary,
\[
\liminf_{p\to\infty}\|f\|_p\ge M.
\]
Combining the two bounds yields
\[
\lim_{p\to\infty}\|f\|_p=M=\|f\|_\infty.
\]
:::

<1>2. The statement fails on $\mathbb R$ for arbitrary $L^\infty$ functions.
::: {.proof}
Take
\[
f(x)\equiv1.
\]
Then $f\in L^\infty(\mathbb R)$ and
\[
\|f\|_\infty=1,
\]
but for every finite $p$,
\[
\int_{\mathbb R}|f(x)|^p\,dx=\infty.
\]
Thus the finite-$p$ norms are infinite, so they do not converge to $\|f\|_\infty=1$.
:::
:::
