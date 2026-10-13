---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-11
kind: problem
title: A contraction image containing a bounded set
classification:
  areas:
  - real-analysis
  topics:
  - Fixed Points
  - Metric Spaces
  - Completeness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(June 2013 #5b) Let $(X,d)$ be a complete metric space, $A\subset X$ be a bounded set, and $F:X\to X$.
Assume there exists some $k>0$ such that $$d(F(a),F(b))\le kd(a,b)\qquad\text{for all }a,b\in X$$ and that $A\subset F(A)$.
Provide a description of $A$ if $k<1$.
Can anything be said about $A$ if $k\ge1$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $0<k<1$, then $A$ is empty or a singleton consisting of a fixed point of $F$.

::: pf-proof

Since $A\subseteq F(A)$ and $F$ is $k$-Lipschitz,
\[
\operatorname{diam}(A)\leq\operatorname{diam}(F(A))
\leq k\,\operatorname{diam}(A).
\]
Boundedness gives $\operatorname{diam}(A)<\infty$, so $k<1$ forces $\operatorname{diam}(A)=0$. Thus $A$ contains at most one point. If $A=\{a\}$, the inclusion $\{a\}\subseteq F(\{a\})=\{F(a)\}$ implies $F(a)=a$. Such a fixed point is unique: if $F(a)=a$ and $F(b)=b$, then $d(a,b)\leq k\,d(a,b)$, hence $a=b$. Completeness guarantees existence of this unique fixed point by the Banach contraction theorem, but the empty set still satisfies the given inclusion.

:::

:::

::: {.pf-step #s2}

If $k\geq1$, every bounded subset of $\mathbb R$ can occur.

::: pf-proof

Take $X=\mathbb R$ with its usual complete metric and $F=\operatorname{id}_{\mathbb R}$. For any $k\geq1$ the inequality $d(F(a),F(b))=d(a,b)\leq k\,d(a,b)$ holds, and $A=F(A)$ for every bounded subset $A\subseteq\mathbb R$, including the empty set. Thus the hypotheses impose no further restriction on $A$ beyond boundedness in this example.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives the exact classification for contractions; step [](#s2){.pf-ref} exhibits unrestricted bounded sets for $k\geq1$.

:::

:::

:::
