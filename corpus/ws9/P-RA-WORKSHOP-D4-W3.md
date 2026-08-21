---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-W3
kind: problem
title: An epsilon-delta proof for the cube-root function
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Give an $\epsilon$-$\delta$ proof that $f(x)=x^{1/3}$ is continuous on $[0,1]$.
(You may also wish to try this for $f(x)=\sqrt{x}$ and/or on the interval $[0,\infty)$ as in June 2011 and others.)
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Use the factorization $u^3 - v^3 = (u-v)(u^2 + uv + v^2)$.
Proof: for $x, a \in [0,1]$ with $u = x^{1/3}$, $v = a^{1/3}$: \[|x^{1/3} - a^{1/3}| = \frac{|x - a|}{x^{2/3} + x^{1/3}a^{1/3} + a^{2/3}}.\] <1>2. Case $a = 0$: continuous at $0$.
Proof: the denominator collapses: $|x^{1/3} - 0| = x^{1/3}$.
Given $\epsilon > 0$, choose $\delta = \epsilon^3$; then $|x - 0| < \delta$ gives $x^{1/3} < \epsilon$.
<1>3. Case $a > 0$: continuous at $a$.
Proof: the denominator satisfies $x^{2/3} + x^{1/3}a^{1/3} + a^{2/3} \ge a^{2/3} > 0$, so \[|x^{1/3} - a^{1/3}| \le \frac{|x - a|}{a^{2/3}}.\] Given $\epsilon > 0$, choose $\delta = \epsilon\,a^{2/3}$; then $|x - a| < \delta$ gives $|x^{1/3} - a^{1/3}| < \epsilon$.
<1>4. Q.E.D. Proof: $f$ is continuous at every $a \in [0,1]$, so continuous on $[0,1]$.
(The same factorization shows $x \mapsto \sqrt{x}$ is continuous on $[0,\infty)$: for $a > 0$ the denominator $\sqrt{x} + \sqrt{a} \ge \sqrt{a}$; at $0$ take $\delta = \epsilon^2$.)
:::
