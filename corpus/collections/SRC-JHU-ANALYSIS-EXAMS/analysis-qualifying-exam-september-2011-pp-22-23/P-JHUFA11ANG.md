---
schema: qual/card@1
id: P-JHUFA11ANG
kind: problem
title: Small-level decay of the distribution function of an $L^p$ function
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Distribution Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 7 of the September 2011 JHU analysis qualifying exam in the preserved compiled source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let
\[
\omega(\alpha)=m\{x\in\mathbb R^n:|f(x)|>\alpha\},\qquad \alpha>0,
\]
be the distribution function of $f\in L^p(\mathbb R^n)$, where $p>0$.
Does $\alpha^p\omega(\alpha)$ tend to a limit as $\alpha\to0^+$? Give a proof or counterexample.
:::

::: solution
Yes. The limit exists and equals $0$.

<1>1. Use the layer-cake identity.
::: proof
For the nonnegative function $|f|^p$,
\[
\|f\|_p^p
=p\int_0^\infty \alpha^{p-1}\omega(\alpha)\,d\alpha<\infty.
\]
Thus
\[
\int_0^a \alpha^{p-1}\omega(\alpha)\,d\alpha\longrightarrow0
\qquad(a\downarrow0).
\]
:::

<1>2. Bound $\alpha^p\omega(\alpha)$ by a shrinking tail of that integral.
::: proof
The distribution function $\omega$ is decreasing. Hence for $t\in[\alpha/2,\alpha]$,
\[
\omega(t)\ge\omega(\alpha).
\]
Therefore
\[
\begin{aligned}
\int_{\alpha/2}^{\alpha}t^{p-1}\omega(t)\,dt
&\ge \omega(\alpha)\int_{\alpha/2}^{\alpha}t^{p-1}\,dt\\
&=\frac{1-2^{-p}}p\,\alpha^p\omega(\alpha).
\end{aligned}
\]
Consequently
\[
0\le \alpha^p\omega(\alpha)
\le \frac{p}{1-2^{-p}}
\int_0^\alpha t^{p-1}\omega(t)\,dt
\longrightarrow0.
\]
Thus
\[
\boxed{\lim_{\alpha\to0^+}\alpha^p\omega(\alpha)=0.}
\]
:::
:::
