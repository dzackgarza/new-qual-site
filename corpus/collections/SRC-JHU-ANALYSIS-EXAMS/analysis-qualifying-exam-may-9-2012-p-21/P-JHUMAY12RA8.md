---
schema: qual/card@1
id: P-JHUMAY12RA8
kind: problem
title: Fourier transform is continuous and vanishes at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, May 9, 2012, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^1(\mathbb R)$ and define
\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx.
\]
Prove that $\widehat f\in C_0(\mathbb R)$; that is, $\widehat f$ is continuous and tends to $0$ at infinity. Do not quote the Riemann--Lebesgue lemma without a proof sketch.
:::

::: {.solution}
<1>1. Continuity.
::: {.proof}
Let $\xi_n\to\xi$. For every $x$,
\[
f(x)e^{-2\pi i x\xi_n}\longrightarrow f(x)e^{-2\pi i x\xi},
\]
and
\[
|f(x)e^{-2\pi i x\xi_n}|=|f(x)|\in L^1(\mathbb R).
\]
Dominated convergence gives
\[
\widehat f(\xi_n)\longrightarrow\widehat f(\xi).
\]
Thus $\widehat f$ is continuous.
:::

<1>2. Vanishing at infinity for smooth compactly supported functions.
::: {.proof}
Let $g\in C_c^1(\mathbb R)$. Integration by parts gives, for $\xi\ne0$,
\[
\widehat g(\xi)
=\frac1{2\pi i\xi}\int_{\mathbb R}g'(x)e^{-2\pi i x\xi}\,dx,
\]
because the boundary term vanishes. Hence
\[
|\widehat g(\xi)|\le\frac{\|g'\|_1}{2\pi|\xi|}\longrightarrow0
\qquad(|\xi|\to\infty).
\]
:::

<1>3. Approximate an arbitrary $L^1$ function.
::: {.proof}
Fix $\varepsilon>0$. Choose $g\in C_c^1(\mathbb R)$ such that
\[
\|f-g\|_1<\frac{\varepsilon}{2},
\]
using density of $C_c^1(\mathbb R)$ in $L^1(\mathbb R)$. For every $\xi$,
\[
|\widehat f(\xi)-\widehat g(\xi)|
\le\|f-g\|_1<\frac{\varepsilon}{2}.
\]
By <1>2, there exists $R$ such that $|\widehat g(\xi)|<\varepsilon/2$ whenever $|\xi|>R$. Therefore, for $|\xi|>R$,
\[
|\widehat f(\xi)|
\le|\widehat f(\xi)-\widehat g(\xi)|+|\widehat g(\xi)|
<\varepsilon.
\]
Thus $\widehat f(\xi)\to0$ as $|\xi|\to\infty$. Together with continuity, this proves
\[
\widehat f\in C_0(\mathbb R).
\]
:::
:::
