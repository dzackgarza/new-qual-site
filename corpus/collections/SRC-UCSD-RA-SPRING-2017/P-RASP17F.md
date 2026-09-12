---
schema: qual/card@1
id: P-RASP17F
kind: problem
title: "Approximate identities, mollified indicators, and weak derivatives imply absolute continuity"
classification:
  areas:
  - real-analysis
  topics:
  - Approximate Identity
  - Weak Derivatives
  - Absolute Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Spring 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\varphi \in C_c^\infty(\mathbb{R}, [0, \infty))$ satisfy $\int_\mathbb{R} \varphi \, dm = 1$ and for $\varepsilon > 0$ let $\delta_\varepsilon(x) = \frac{1}{\varepsilon}\varphi\left(\frac{x}{\varepsilon}\right)$.

1. If $-\infty < a < b < \infty$ and $h_\varepsilon(x) := \mathbf{1}_{[a,b]} * \delta_\varepsilon$, show $h_\varepsilon'(x) = \delta_\varepsilon(x - a) - \delta_\varepsilon(x - b)$.

2. If $f \in C_c(\mathbb{R}, \mathbb{R})$ and $g \in L^1(\mathbb{R}, m)$ satisfy
$$
\int_\mathbb{R} f h' \, dm = -\int_\mathbb{R} g h \, dm \quad \text{for all } h \in C_c^\infty(\mathbb{R}),
$$
show $f$ is absolutely continuous and $f' = g$ $m$-a.e.
:::


::: solution
<1>1. Differentiate the mollified indicator.
::: proof
For every \(x\in\mathbb R\),
\[
h_\varepsilon(x)
=\int_a^b\delta_\varepsilon(x-y)\,dy.
\]
With \(t=x-y\),
\[
h_\varepsilon(x)
=\int_{x-b}^{x-a}\delta_\varepsilon(t)\,dt.
\]
Since \(\delta_\varepsilon\) is smooth, the Fundamental Theorem of Calculus gives
\[
\boxed{
h_\varepsilon'(x)
=\delta_\varepsilon(x-a)-\delta_\varepsilon(x-b).}
\]
:::

<1>2. Construct an absolutely continuous primitive of \(g\).
::: proof
Define
\[
G(x):=\int_0^x g(t)\,dt.
\]
Because \(g\in L^1(\mathbb R)\), \(G\) is absolutely continuous on every bounded interval and
\[
G'=g
\]
almost everywhere. Therefore for every \(h\in C_c^\infty(\mathbb R)\), integration by parts for absolutely continuous functions gives
\[
\int_\mathbb R G h'\,dm
=-\int_\mathbb R g h\,dm.
\]
Subtracting this from the assumed identity for \(f\), the continuous function
\[
u:=f-G
\]
satisfies
\[
\int_\mathbb R u h'\,dm=0
\qquad\text{for every }h\in C_c^\infty(\mathbb R).
\]
Thus the distributional derivative of \(u\) is zero.
:::

<1>3. A continuous function with zero distributional derivative is constant.
::: proof
Let \(\delta_\varepsilon\) be the mollifier above. Since \(u'\) is the zero distribution,
\[
(u*\delta_\varepsilon)'=u'*\delta_\varepsilon=0.
\]
Hence \(u*\delta_\varepsilon\) is constant on \(\mathbb R\) for every \(\varepsilon>0\).

Because \(u\) is continuous, mollification converges locally uniformly:
\[
u*\delta_\varepsilon\longrightarrow u.
\]
A locally uniform limit of constant functions is constant, so there is \(C\in\mathbb R\) such that
\[
u(x)=C
\qquad\text{for all }x.
\]
Therefore
\[
f(x)=C+G(x)=C+\int_0^x g(t)\,dt.
\]
Thus \(f\) is absolutely continuous and, by the Lebesgue Fundamental Theorem of Calculus,
\[
\boxed{f'(x)=g(x)\text{ for a.e. }x.}
\]
:::
:::
