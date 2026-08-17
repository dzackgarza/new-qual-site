---
schema: qual/card@1
id: P-JVAGD
kind: problem
title: "Let $f : \\mathbb{R} \\to [0,\\infty)$ be a measurable function and $\\varphi : [0,\\infty) \\to [0,\\infty)$ be a monotonic\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
  - absolute-continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f : \mathbb{R} \to [0,\infty)$ be a measurable function and $\varphi : [0,\infty) \to [0,\infty)$ be a monotonic, absolutely continuous function on $[0,T]$ for every $T < \infty$.
Assume $\varphi(0)=0$.
Prove $$\int_{\mathbb{R}} \varphi \circ f\, dx = \int_0^\infty m(\{x : f(x) > t\})\varphi'(t)\, dt.$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Rewrite $\varphi \circ f$ using the fundamental theorem of calculus.
Proof: $\varphi$ is absolutely continuous on $[0,T]$ for every $T < \infty$ and monotone with $\varphi(0) = 0$.
For every $u \ge 0$, $\varphi(u) = \int_0^u \varphi'(t)\,dt$; monotonicity gives $\varphi' \ge 0$ a.e. Hence, pointwise, \[\varphi(f(x)) = \int_0^{f(x)} \varphi'(t)\,dt = \int_0^\infty \mathbf 1_{\{f(x) > t\}}\,\varphi'(t)\,dt.\] <1>2. Integrate in $x$ and apply Tonelli.
Proof: the integrand $\mathbf 1_{\{f(x) > t\}}\varphi'(t)$ is non-negative and measurable on $\mathbb{R}\times[0,\infty)$, so Tonelli's theorem applies: \[\int_{\mathbb{R}}\varphi(f(x))\,dx = \int_0^\infty \varphi'(t)\left(\int_{\mathbb{R}}\mathbf 1_{\{f(x) > t\}}\,dx\right)dt = \int_0^\infty m(\{x : f(x) > t\})\,\varphi'(t)\,dt.\] <1>3. Q.E.D.
:::
