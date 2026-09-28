---
schema: qual/card@1
id: E-HAT-2.2-8
kind: problem
title: Degree of one-point compactification of polynomial equals degree as polynomial; local degree at roots equals multiplicity
classification:
  areas:
  - topology
  topics:
  - Degree
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 8; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete degree/cellular proof checked.
---

::: {.problem}
A polynomial $f(z)$ with complex coefficients, viewed as a map $\mathbb{C} \to \mathbb{C}$, can always be extended to a continuous map of one-point compactifications $\hat{f}: S^2 \to S^2$.
Show that the degree of $\hat{f}$ equals the degree of $f$ as a polynomial.
Show also that the local degree of $\hat{f}$ at a root of $f$ is the multiplicity of the root.
:::

::: {.solution}
Let
\[
f(z)=a_mz^m+a_{m-1}z^{m-1}+\cdots+a_0,
\qquad a_m\ne0.
\]

<1>1. The map $f:\mathbb C\to\mathbb C$ is proper and therefore extends continuously to one-point compactifications by setting
\[
\widehat f(\infty)=\infty.
\]
::: {.proof}
As $|z|\to\infty$,
\[
|f(z)|\ge |a_m||z|^m-\sum_{j<m}|a_j||z|^j\longrightarrow\infty.
\]
Hence inverse images of compact sets are bounded and closed, therefore compact. This is exactly the condition for extension to the one-point compactifications.
:::

<1>2. The map $\widehat f$ is homotopic to the compactification of the leading monomial $a_mz^m$.
::: {.proof}
Consider
\[
f_t(z)=a_mz^m+t(a_{m-1}z^{m-1}+\cdots+a_0),
\qquad0\le t\le1.
\]
The leading coefficient is independent of $t$, so the estimate in <1>1 is uniform in $t$ outside a sufficiently large disk. Thus the $f_t$ extend to a continuous based homotopy of one-point compactifications.
:::

<1>3. The compactified map $z\mapsto a_mz^m$ has degree $m$.
::: {.proof}
Multiplication by $a_m\ne0$ is orientation preserving as a real linear map of $\mathbb C$, so it has degree $+1$. For a nonzero regular value $w$, the equation
\[
z^m=w
\]
has exactly $m$ distinct roots. Near each root the derivative $mz^{m-1}$ is nonzero and complex multiplication by a nonzero complex number preserves the real orientation. Hence each preimage contributes local degree $+1$, so the total degree is $m$.
:::

Therefore
\[
\boxed{\deg\widehat f=m=\deg(f)\text{ as a polynomial}.}
\]

<1>4. If $z_0$ is a root of multiplicity $k$, then the local degree of $\widehat f$ at $z_0$ is $k$.
::: {.proof}
Factor
\[
f(z)=(z-z_0)^k g(z),
\qquad g(z_0)\ne0.
\]
Choose a small circle $|z-z_0|=\varepsilon$ on which $g$ has no zero. The local degree equals the winding number around $0$ of the image of this circle under $f$. The factor $(z-z_0)^k$ winds exactly $k$ times. The loop $g(z)$ is homotopic in $\mathbb C^*$ to the constant loop $g(z_0)$ when $\varepsilon$ is small, so it contributes winding number $0$. Hence the total winding number, and therefore the local degree, is $k$.
:::
:::
