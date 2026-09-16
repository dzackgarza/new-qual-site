---
schema: qual/card@1
id: P-WESRA08-II3
kind: problem
title: Rational-translation invariant measurable sets are null or conull
classification:
  areas: [real-analysis]
  topics: [Lebesgue Measure, Translation Invariance, Lebesgue Density Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose that $A\subseteq\mathbb R$ is Lebesgue measurable and
\[
A+r=A
\]
for every rational number $r$.
Prove that either
\[
m(A)=0
\qquad\text{or}\qquad
m(\mathbb R\setminus A)=0.
\]
:::

::: {.solution}
Suppose, toward a contradiction, that both $A$ and $A^c$ have positive measure.

Choose a nonnegative $\varphi\in C_c^\infty(\mathbb R)$ with
\[
\int_{\mathbb R}\varphi=1,
\]
and put
\[
\varphi_\varepsilon(x)=\varepsilon^{-1}\varphi(x/\varepsilon),
\qquad
u_\varepsilon=\mathbf1_A*\varphi_\varepsilon.
\]
Since $\mathbf1_A\in L^\infty_{\mathrm{loc}}$ and $\varphi_\varepsilon$ is compactly supported, $u_\varepsilon$ is a continuous function on $\mathbb R$.

For every $q\in\mathbb Q$ and every $x\in\mathbb R$, the identity $A+q=A$ gives
\[
\mathbf1_A(y+q)=\mathbf1_A(y).
\]
Hence, after a change of variables,
\[
u_\varepsilon(x+q)=u_\varepsilon(x).
\]
Thus every rational number is a period of $u_\varepsilon$.
Since $\mathbb Q$ is dense and $u_\varepsilon$ is continuous, $u_\varepsilon$ must be constant on $\mathbb R$.

By the Lebesgue density theorem, choose a density point $a$ of $A$ and a density point $b$ of $A^c$.
Approximate identities recover characteristic functions at density points, so
\[
u_\varepsilon(a)\longrightarrow1,
\qquad
u_\varepsilon(b)\longrightarrow0
\]
as $\varepsilon\downarrow0$.

But for every $\varepsilon>0$, the function $u_\varepsilon$ is constant, so
\[
u_\varepsilon(a)=u_\varepsilon(b),
\]
which is impossible in the limit.
Therefore $A$ and $A^c$ cannot both have positive measure.
Hence
\[
\boxed{m(A)=0\text{ or }m(A^c)=0.}
\]
:::
