---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-07
kind: problem
title: 'The $L^p$ norms of a nonnegative continuous function converge to its maximum'
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - l-infty
  - limits
relations: []
review: draft
---

::: {.problem title="?"}
(January 2010 #5) Suppose that $f:[a,b]\to\mathbb R$ is continuous, $f\ge0$ on $[a,b]$, and put $$M=\sup\{f(x):x\in[a,b]\}.$$ Prove that $$\lim_{p\to\infty}\left(\int_a^b f(x)^p\,dx\right)^{1/p}=M.$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Upper bound.
    Proof: $0 \le f \le M$ on $[a,b]$, so $f^p \le M^p$ and
    \[\left(\int_a^b f(x)^p\,dx\right)^{1/p} \le \left(\int_a^b M^p\,dx\right)^{1/p} = M(b-a)^{1/p}.\]
    As $p \to \infty$, $(b-a)^{1/p} \to 1$, so $\limsup_p(\int f^p)^{1/p} \le M$.
<1>2. Lower bound.
    Proof: fix $\epsilon \in (0, M)$. Since $f$ is continuous and attains the value $M$ (extreme value theorem on $[a,b]$), the set $\{x : f(x) > M - \epsilon\}$ is open and nonempty; it contains an interval $[u, v]$ of positive length $\ell = v - u > 0$. Then
    \[\int_a^b f(x)^p\,dx \ge \int_u^v (M - \epsilon)^p\,dx = \ell\,(M-\epsilon)^p,\]
    so $\left(\int_a^b f^p\right)^{1/p} \ge (M - \epsilon)\,\ell^{1/p}$. As $p \to \infty$, $\ell^{1/p} \to 1$, so $\liminf_p(\int f^p)^{1/p} \ge M - \epsilon$ for every $\epsilon > 0$.
<1>3. Conclude.
    Proof: $\limsup \le M$ and $\liminf \ge M$, so the limit exists and equals $M$.
<1>4. Q.E.D.
:::
