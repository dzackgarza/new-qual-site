---
schema: qual/card@1
id: P-WPVFN
kind: problem
title: "Let $g\\in L^\\infty([0, 1])$ Prove that $\\int _{[0,1]} f(x) g(x)\\, dx = 0 \\quad\\text{for all continuous } f:[0, 1] \\to \\RR \\implies g(x) = 0 \\text{ almost everywhere. }$"
classification:
  areas:
  - real-analysis
  topics:
  - l-infty
  - density
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Let $g\in L^\infty([0, 1])$ Prove that
\[
\int _{[0,1]} f(x) g(x)\, dx = 0 
\quad\text{for all continuous } f:[0, 1] \to \RR 
\implies g(x) = 0 \text{ almost everywhere. }
\]
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The linear functional $\Lambda(h) = \int_{[0,1]} g(x)h(x)\,dx$ is bounded on $L^1([0,1])$: $|\Lambda(h)| \le \|g\|_\infty\|h\|_1$.
Proof: $|\int g h| \le \int |g||h| \le \|g\|_\infty \int |h| = \|g\|_\infty\|h\|_1$.

<1>2. $\Lambda$ vanishes on all of $L^1([0,1])$.
<2>1. $\Lambda = 0$ on the dense subspace $C([0,1])$.
Proof: hypothesis.
<2>2. For every $h \in L^1$, choose continuous $f_k \to h$ in $L^1$; then $|\Lambda(h)| \le |\Lambda(h - f_k)| + |\Lambda(f_k)| \le \|g\|_\infty\|h - f_k\|_1 + 0 \to 0$.
Proof: continuity of the functional (<1>1), density of $C([0,1])$ in $L^1([0,1])$, and the hypothesis for the $f_k$.
<2>3. Q.E.D. Proof: <2>2.

<1>3. $g = 0$ a.e. <2>1. Apply <1>2 to $h = \mathrm{sgn}(g) \in L^1$: $\int g\,\mathrm{sgn}(g)\,dx = 0$.
Proof: $\Lambda(\mathrm{sgn}(g)) = 0$ by <1>2. <2>2. $\int |g|\,dx = 0$, so $g = 0$ a.e. Proof: $g\,\mathrm{sgn}(g) = |g|$ everywhere (with $\mathrm{sgn}(0) = 0$). <2>3. Q.E.D. Proof: <2>1 and <2>2.
:::
