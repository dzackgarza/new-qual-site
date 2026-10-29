---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-07
kind: problem
title: Extreme value theorem in one real dimension
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Compactness
relations:
- kind: uses
  target: T-RA-WORKSHOP-D4-3-2
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(c.f. January 2007 #3a, June 2010 #2a) Let $K\subseteq\RR$ be compact and let $f:K\to\RR$ be continuous.

(a) Prove that $f(K)$ is compact.

(b) Prove that if $K$ is nonempty, then $f$ attains a maximum and a minimum on $K$.

(The proof is nearly unchanged for $f:K\subseteq\RR^n\to\RR^m$ when $n$ or $m$ is greater than 1.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) The image $f(K)$ is compact.

::: pf-proof

Let $(V_\alpha)_{\alpha\in A}$ be an open cover of $f(K)$ in $\RR$. The sets $f^{-1}(V_\alpha)$ are open in the subspace $K$ by continuity and cover $K$. Compactness supplies finitely many indices $\alpha_1,\ldots,\alpha_r$ such that
$$
K=\bigcup_{j=1}^{r}f^{-1}(V_{\alpha_j}).
$$
Applying $f$ yields $f(K)\subseteq\bigcup_{j=1}^{r}V_{\alpha_j}$. Thus every open cover of $f(K)$ has a finite subcover.

:::

:::

::: pf-step

(b) If $K$ is nonempty, then $f$ attains both its maximum and minimum on $K$.

::: pf-proof

By step [](#s1){.pf-ref}, the nonempty set $f(K)\subseteq\RR$ is compact, hence closed and bounded. Set $M=\sup f(K)$ and $m=\inf f(K)$. Boundedness makes both numbers finite. The defining properties of supremum and infimum put $M$ and $m$ in the closure of $f(K)$; closedness therefore implies $M,m\in f(K)$. Thus there exist $p,q\in K$ with $f(p)=M$ and $f(q)=m$.

:::

:::

:::

:::
