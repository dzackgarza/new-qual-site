---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-09
kind: problem
title: 'Continuity of a running supremum'
classification:
  areas:
  - real-analysis
  topics:
  - continuity
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Suppose that $f:[a,b]\to\mathbb R$ is continuous and define $M:[a,b]\to\mathbb R$ by $$M(x)=\sup\{f(y):a\le y\le x\}.$$ Show that $M$ is continuous on $[a,b]$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $M$ is monotone increasing, so it suffices to check one-sided continuity.
Proof: for $x_1 \le x_2$, $\{f(y) : a \le y \le x_1\} \subseteq \{f(y) : a \le y \le x_2\}$, so $M(x_1) \le M(x_2)$.
Since $M$ is increasing on $[a,b]$, it suffices to show $M(x+) - M(x-) \to 0$ as appropriate; we show directly that $M$ is continuous via the uniform continuity of $f$.
<1>2. Bound the jump of $M$ by the oscillation of $f$.
Proof: $f$ is continuous on the compact interval $[a,b]$, hence uniformly continuous: for every $\epsilon > 0$ there is $\delta > 0$ such that $|f(u) - f(v)| < \epsilon$ whenever $|u - v| < \delta$.
Fix $x \in [a,b]$ and take $y \in [a,b]$ with $|x - y| < \delta$; assume $y > x$ (the case $y < x$ is symmetric).
For every $t \in [x,y]$, $|t - x| < \delta$ gives $f(t) \le f(x) + \epsilon$, so $\sup_{[x,y]} f \le f(x) + \epsilon$.
Since $M(y) = \max\big(M(x), \sup_{[x,y]}f\big)$ and $f(x) \le M(x)$, \[M(y) \le \max\big(M(x), f(x) + \epsilon\big) \le M(x) + \epsilon.\] Similarly, for $y < x$, $M(x) \le M(y) + \epsilon$.
Hence $|M(x) - M(y)| < \epsilon$ whenever $|x - y| < \delta$, so $M$ is (uniformly) continuous on $[a,b]$.
<1>3. Q.E.D.
:::
