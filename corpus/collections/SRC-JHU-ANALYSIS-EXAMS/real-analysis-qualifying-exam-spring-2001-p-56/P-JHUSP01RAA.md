---
schema: qual/card@1
id: P-JHUSP01RAA
kind: problem
title: 'Mollifier convolutions converge in $L^p$ but not in $L^\infty$'
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Real Analysis Qualifying Exam, Spring 2001, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $\phi\in C_c^\infty(\mathbb R^n)$ satisfy $\int\phi=1$, and define
\[
\phi_\varepsilon(x)=\varepsilon^{-n}\phi(x/\varepsilon).
\]
Prove that if $1\le p<\infty$ and $f\in L^p(\mathbb R^n)$, then
\[
f*\phi_\varepsilon\to f
\qquad\text{in }L^p.
\]
Show that the analogous statement fails for $p=\infty$.
:::

::: {.solution}
For $1\le p<\infty$, changing variables $y=\varepsilon z$ gives
\[
(f*\phi_\varepsilon)(x)-f(x)
=\int_{\mathbb R^n}\phi(z)\bigl(f(x-\varepsilon z)-f(x)\bigr)\,dz.
\]
By Minkowski's integral inequality,
\[
\|f*\phi_\varepsilon-f\|_p
\le\int |\phi(z)|\,\|f(\cdot-\varepsilon z)-f\|_p\,dz.
\]
For each fixed $z$, translation continuity in $L^p$ gives
\[
\|f(\cdot-\varepsilon z)-f\|_p\to0.
\]
The integrand is bounded by $2\|f\|_p|\phi(z)|$, which is integrable in $z$. Dominated convergence therefore yields
\[
\|f*\phi_\varepsilon-f\|_p\longrightarrow0.
\]

For $p=\infty$, take $f=\mathbf1_{[0,\infty)}$ in one dimension. Every $f*\phi_\varepsilon$ is continuous. But no continuous function $g$ can satisfy
\[
\|g-f\|_\infty<\frac12.
\]
Indeed, such an essential-supremum bound and continuity would force $g(x)<1/2$ for every $x<0$ and $g(x)>1/2$ for every $x>0$, contradicting continuity at $0$. Hence
\[
\|f*\phi_\varepsilon-f\|_\infty\ge\frac12
\]
for every $\varepsilon$, so convergence in $L^\infty$ fails.
:::
