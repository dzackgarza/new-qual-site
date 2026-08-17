---
schema: qual/card@1
id: P-5UQSK
kind: problem
title: "Let $M<\\infty$ and $\\mathcal{F} \\subseteq C[a,b]$."
classification:
  areas:
  - real-analysis
  topics:
  - equicontinuity
  - differentiation
relations: []
review: draft
solved: true
---

::: problem
Let $M<\infty$ and $\mathcal{F} \subseteq C[a,b]$.
Assume that each $f \in \mathcal{F}$ is differentiable on $(a,b)$ and satisfies $|f(a)| \leq M$ and $|f'(x)| \leq M$ for all $x \in (a,b)$.
Prove that $\mathcal{F}$ is equicontinuous on $[a,b]$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Every $f \in \mathcal F$ is Lipschitz with constant $M$: $|f(x) - f(y)| \le M|x - y|$ for all $x, y \in [a,b]$.
Proof: mean value theorem — for $x \ne y$, $f(x) - f(y) = f'(c)(x - y)$ for some $c$ between $x$ and $y$, and $|f'(c)| \le M$.

<1>2. $\mathcal F$ is equicontinuous on $[a,b]$.
<2>1. Given $\eps > 0$, set $\delta = \eps/M$.
Proof: $M < \infty$ by hypothesis.
<2>2. For $|x - y| < \delta$: $|f(x) - f(y)| \le M|x - y| < \eps$ for every $f \in \mathcal F$.
Proof: <1>1 and <2>1. <2>3. Q.E.D. Proof: <2>2 is exactly the definition of equicontinuity ($\delta$ independent of $x, y$, and $f$).

<1>3. (Remark) each $f \in \mathcal F$ is also uniformly bounded: $|f(x)| \le M + M(b - a)$.
Proof: $|f(x)| \le |f(a)| + |f(x) - f(a)| \le M + M|x - a| \le M + M(b - a)$ by <1>1.
:::
