---
schema: qual/card@1
id: P-Y34JB
kind: problem
title: The graph of a measurable function on $\RR$ has measure zero in $\RR^2$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Fall 2021 real-analysis qualifying exam recorded by SRC-UGA-RA-FALL-2021.
- event: solution-written
  by: prior-author
  date: 2026-08-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f$ be a measurable function on $\mathbb{R}$. Show that the graph of $f$ has measure zero in $\mathbb{R}^{2}$.
:::

::: {.solution}
Let
\[
\Gamma:=\{(x,f(x)):x\in\mathbb R\}\subset\mathbb R^2.
\]

<1>1. The graph $\Gamma$ is Lebesgue measurable.
::: {.proof}
The map
\[
F:\mathbb R^2\to\mathbb R,
\qquad
F(x,y)=y-f(x),
\]
is Lebesgue measurable because $(x,y)\mapsto y$ is continuous and $(x,y)\mapsto f(x)$ is measurable. Hence
\[
\Gamma=F^{-1}(\{0\})
\]
is Lebesgue measurable.
:::

<1>2. Every vertical section of $\Gamma$ has one-dimensional measure zero.
::: {.proof}
For fixed $x\in\mathbb R$,
\[
\Gamma_x:=\{y\in\mathbb R:(x,y)\in\Gamma\}=\{f(x)\}.
\]
Therefore
\[
m_1(\Gamma_x)=0.
\]
:::

<1>3. Apply Tonelli's theorem.
::: {.proof}
Since $\mathbf1_\Gamma\ge0$ is measurable, Tonelli's theorem gives
\[
\begin{aligned}
m_2(\Gamma)
&=\int_{\mathbb R^2}\mathbf1_\Gamma(x,y)\,d(x,y)\\
&=\int_{\mathbb R}\left(\int_{\mathbb R}\mathbf1_\Gamma(x,y)\,dy\right)dx\\
&=\int_{\mathbb R}m_1(\Gamma_x)\,dx\\
&=0.
\end{aligned}
\]
Thus
\[
\boxed{m_2(\Gamma)=0.}
\]
:::
:::
