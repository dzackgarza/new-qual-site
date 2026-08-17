---
schema: qual/card@1
id: P-NRCTX
kind: problem
title: "Assume $f : [0,1] \\to \\mathbb{R}$ is uniformly continuous, increasing…"
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - absolute-continuity
  - variation
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Assume $f : [0,1] \to \mathbb{R}$ is uniformly continuous, increasing and convex.
Prove $f$ is differentiable almost everywhere and $$f(1) - f(0) = \int_0^1 f'(x)dx.$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $f$ is absolutely continuous on $[0,1]$.
Proof: a finite convex function on a compact interval is absolutely continuous.
For completeness: $f$ is continuous on $[0,1]$ (convex on an open interval containing $[0,1]$ is continuous there; alternatively the monotone, hence one-sided limits exist and equal $f$ at the endpoints by the given continuity).
On any closed subinterval $[a,b] \subseteq (0,1)$, convexity makes $f$ Lipschitz (all secant slopes are bounded between the slopes at the endpoints), so $f'$ exists a.e. on $(0,1)$ and is increasing a.e., with $\int_a^b f' = f(b) - f(a)$.
Monotonicity of $f'$ and finiteness of $f$ give $\int_0^1 f' < \infty$ (monotone convergence as $a\searrow 0, b\nearrow 1$), and then $f(y) - f(x) = \int_x^y f'$ for all $0 \le x \le y \le 1$ by continuity.
Hence $f$ is absolutely continuous.
<1>2. $f$ is differentiable almost everywhere.
Proof: absolutely continuous functions on $[0,1]$ are differentiable a.e. (classical theorem: an AC function is of bounded variation and a monotone–difference decomposition plus the monotone-differentiation theorem gives a.e. differentiability).
<1>3. $f(1) - f(0) = \int_0^1 f'(x)\,dx$.
Proof: this is the fundamental theorem of calculus for absolutely continuous functions: $f' \in L^1$ and $f$ is the integral of its derivative.
Moreover $f$ increasing gives $f' \ge 0$ a.e., so the integral is well-defined in the extended sense and finite.
<1>4. Q.E.D.
:::
