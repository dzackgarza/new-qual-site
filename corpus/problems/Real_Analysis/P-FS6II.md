---
schema: qual/card@1
id: P-FS6II
kind: problem
title: Tonelli's theorem and the layer-cake representation of a nonnegative measurable
  function
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Measure Theory
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
a.
Carefully state Tonelli's theorem for a nonnegative function $F(x, t)$ on $\RR^n\cross \RR$.

b.
  Let $f:\RR^n\to [0, \infty]$ and define
\[
\mca \definedas \theset{(x, t) \in \RR^n\cross \RR \suchthat 0\leq t \leq f(x)}
.\]

  Prove the validity of the following two statements:

  1. $f$ is Lebesgue measurable on $\RR^{n} \iff \mca$ is a Lebesgue measurable subset of $\RR^{n+1}$.
  2. If $f$ is Lebesgue measurable on $\RR^n$ then
  \[
  m(\mathcal{A})=\int_{\mathbb{R}^{n}} f(x) d x=\int_{0}^{\infty} m\left(\left\{x \in \mathbb{R}^{n}\suchthat f(x) \geq t\right\}\right) d t
  .\]
:::
::: {.solution}
(a) Let $F\colon \RR^n \times \RR \to [0,\infty]$ be Lebesgue measurable on $\RR^{n+1}$. Then for a.e. $x \in \RR^n$ the slice $t \mapsto F(x,t)$ is measurable on $\RR$, the function $x \mapsto \int_\RR F(x, t)\,dt$, defined a.e., is measurable on $\RR^n$, and
$$
\int_{\RR^{n+1}} F = \int_{\RR^n}\left(\int_\RR F(x, t)\,dt\right)dx,
$$
all integrals possibly infinite. The same holds with the roles of $x$ and $t$ exchanged.

(b)

::: pf

::: {.pf-step #s1}

If $f$ is measurable, then $\mca$ is measurable.

::: pf-proof

$\mca = \theset{(x,t) : t \ge 0} \cap \theset{(x,t) : f(x) - t \ge 0}$, where $f(x) - t$ is taken in $[-\infty, \infty]$. The function $(x,t) \mapsto f(x)$ is measurable on $\RR^{n+1}$ because $f$ is measurable (cylinder functions of measurable functions are measurable; see [[E-JJ746]]), and $(x,t) \mapsto t$ is continuous, so their difference is measurable.

:::

:::

::: {.pf-step #s2}

If $\mca$ is measurable, then $f$ is measurable.

::: pf-proof

For every $x$, the slice $\theset{t : (x,t) \in \mca}$ is $[0, f(x)]$, which has length $f(x)$. By part (a) applied to $F = \chi_\mca$, the function $x \mapsto m_1([0, f(x)]) = f(x)$ is measurable.

:::

:::

::: {.pf-step #s3}

If $f$ is measurable, then $m(\mca) = \int_{\RR^n} f(x)\,dx = \int_0^\infty m\theset{x : f(x) \ge t}\,dt$.

::: pf-proof

By step [](#s1){.pf-ref}, $\chi_\mca$ is measurable. Part (a) with the $t$-integral inside gives $m(\mca) = \int_{\RR^n}\int_\RR \chi_\mca(x,t)\,dt\,dx = \int_{\RR^n} f(x)\,dx$, since the slice at $x$ has length $f(x)$. Part (a) with the $x$-integral inside gives $m(\mca) = \int_\RR\int_{\RR^n}\chi_\mca(x,t)\,dx\,dt$. For $t < 0$ the slice $\theset{x : (x,t) \in \mca}$ is empty, and for $t \ge 0$ it is $\theset{x : f(x) \ge t}$, so this equals $\int_0^\infty m\theset{f \ge t}\,dt$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are (b)1, and step [](#s3){.pf-ref} is (b)2.

:::

:::

:::
