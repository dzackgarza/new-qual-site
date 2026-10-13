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
(c.f. January 2007 #3a, June 2010 #2a) Prove Theorem 3.2 for a function $f:K\subset\mathbb R\to\mathbb R$.
(The proof is nearly unchanged when $n$ or $m$ is greater than 1.)
:::

::: {.solution}
Let $K\subseteq\mathbb R$ be compact and $f:K\to\mathbb R$ continuous.

::: pf

::: {.pf-step #s1}

The image $f(K)$ is compact.

::: pf-proof

Let $(V_\alpha)_{\alpha\in A}$ be an open cover of $f(K)$ in $\mathbb R$. The sets $f^{-1}(V_\alpha)$ are open in the subspace $K$ by continuity and cover $K$. Compactness supplies finitely many indices $\alpha_1,\ldots,\alpha_r$ such that
\[
K=\bigcup_{j=1}^{r}f^{-1}(V_{\alpha_j}).
\]
Applying $f$ yields $f(K)\subseteq\bigcup_{j=1}^{r}V_{\alpha_j}$. Thus every open cover of $f(K)$ has a finite subcover.

:::

:::

::: {.pf-step #s2}

If $K$ is nonempty, then $f$ attains both its maximum and minimum on $K$.

::: pf-proof

By step [](#s1){.pf-ref}, the nonempty set $f(K)\subseteq\mathbb R$ is compact, hence closed and bounded. Set $M=\sup f(K)$ and $m=\inf f(K)$. Boundedness makes both numbers finite. The defining properties of supremum and infimum put $M$ and $m$ in the closure of $f(K)$; closedness therefore implies $M,m\in f(K)$. Thus there exist $p,q\in K$ with $f(p)=M$ and $f(q)=m$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the compact-image assertion of Theorem 3.2 for functions on subsets of $\mathbb R$. Step [](#s2){.pf-ref} proves the extreme-value assertion, including its stated specialization to nondegenerate closed intervals.

:::

:::

:::
