---
schema: qual/card@1
id: P-QXYTV
kind: problem
title: "Suppose that $f:[a,b]\\to\\mathbb{R}$ is"
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - l-infty
  - limits
relations: []
review: draft
solved: true
---

::: problem
Suppose that $f:[a,b]\to\mathbb{R}$ is continuous, $f\geq 0$ on $[a,b]$, and put $M=\sup\{f(x):x\in[a,b]\}$.
Prove that $$\lim_{p\to\infty}\left(\int_a^b f(x)^p\,dx\right)^{1/p}=M.$$
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Upper bound: $(\int_a^b f^p)^{1/p} \le M\,(b-a)^{1/p}$.
Proof: $0 \le f \le M$ on $[a,b]$, so $\int_a^b f^p \le M^p (b-a)$, and $(b-a)^{1/p} \to 1$.
<1>2. Hence $\limsup_{p\to\infty}(\int_a^b f^p)^{1/p} \le M$.
Proof: <1>1 and $(b-a)^{1/p} \to 1$.
<1>3. Lower bound: for each $0 < \eps < M$, $\liminf_{p\to\infty}(\int_a^b f^p)^{1/p} \ge M - \eps$.
Proof: since $f$ is continuous, it attains $M$ at some $x_0 \in [a,b]$.
The set $\{f > M - \eps\}$ is open (continuity) and contains $x_0$, so it contains an interval of length $\delta > 0$.
Hence \[ \int_a^b f^p \ge (M-\eps)^p \delta, \qquad \text{so} \qquad \Big(\int_a^b f^p\Big)^{1/p} \ge (M-\eps)\,\delta^{1/p} \to M - \eps . \] <1>4. $\lim_{p\to\infty}(\int_a^b f^p)^{1/p} = M$.
Proof: <1>2 and <1>3 (letting $\eps \to 0$). <1>5. Q.E.D.
:::
