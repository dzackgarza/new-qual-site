---
schema: qual/card@1
id: P-ZCE6E
kind: problem
title: The subgraph of a nonnegative function is measurable if and only if the function
  is, and $m(\mathcal{A})=\int_{\RR^n}f=\int_0^\infty m(\{f\ge t\})\,dt$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2019 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2019.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: problem
Let $f:\mathbb R^n\to[0,\infty]$ and define
\[
\mathcal A:=\{(x,t)\in\mathbb R^n\times\mathbb R:0\le t\le f(x)\}.
\]

1. Prove that $f$ is Lebesgue measurable if and only if $\mathcal A$ is Lebesgue measurable in $\mathbb R^{n+1}$.

2. If $f$ is measurable, prove
\[
m_{n+1}(\mathcal A)
=\int_{\mathbb R^n}f(x)\,dx
=\int_0^\infty m_n(\{x:f(x)\ge t\})\,dt.
\]
:::

::: solution
<1>1. If $f$ is measurable, then $\mathcal A$ is measurable.
::: proof
Define
\[
H(x,t):=f(x)-t.
\]
The map $(x,t)\mapsto f(x)$ is measurable, as is $(x,t)\mapsto t$, so $H$ is measurable. Therefore
\[
\mathcal A
=(\mathbb R^n\times[0,\infty))\cap H^{-1}([0,\infty])
\]
is Lebesgue measurable.
:::

<1>2. If $\mathcal A$ is measurable, then $f$ is measurable.
::: proof
For every fixed $x\in\mathbb R^n$, the vertical section is
\[
\mathcal A_x
:=\{t:(x,t)\in\mathcal A\}
=[0,f(x)].
\]
Hence
\[
f(x)=m_1(\mathcal A_x)
=\int_{\mathbb R}\mathbf1_{\mathcal A}(x,t)\,dt.
\]
Since $\mathbf1_{\mathcal A}$ is a nonnegative measurable function on $\mathbb R^{n+1}$, Tonelli's theorem implies that the function
\[
x\longmapsto \int_{\mathbb R}\mathbf1_{\mathcal A}(x,t)\,dt
\]
is measurable. Thus $f$ is measurable.
:::

<1>3. Compute the measure of the subgraph.
::: proof
Assume $f$ is measurable. By Step 1, $\mathcal A$ is measurable, so Tonelli gives
\[
\begin{aligned}
m_{n+1}(\mathcal A)
&=\int_{\mathbb R^{n+1}}\mathbf1_{\mathcal A}(x,t)\,d(x,t)\\
&=\int_{\mathbb R^n}\left(\int_{\mathbb R}\mathbf1_{\mathcal A}(x,t)\,dt\right)dx\\
&=\int_{\mathbb R^n}f(x)\,dx.
\end{aligned}
\]
:::

<1>4. Derive the layer-cake formula.
::: proof
For $t\ge0$, the horizontal section is
\[
\mathcal A^t
:=\{x:(x,t)\in\mathcal A\}
=\{x:f(x)\ge t\}.
\]
A second application of Tonelli gives
\[
\begin{aligned}
m_{n+1}(\mathcal A)
&=\int_0^\infty\left(\int_{\mathbb R^n}\mathbf1_{\mathcal A}(x,t)\,dx\right)dt\\
&=\int_0^\infty m_n(\{x:f(x)\ge t\})\,dt.
\end{aligned}
\]
Combining with Step 3 yields
\[
\boxed{
m_{n+1}(\mathcal A)
=\int_{\mathbb R^n}f(x)\,dx
=\int_0^\infty m_n(\{f\ge t\})\,dt.}
\]
:::
:::
