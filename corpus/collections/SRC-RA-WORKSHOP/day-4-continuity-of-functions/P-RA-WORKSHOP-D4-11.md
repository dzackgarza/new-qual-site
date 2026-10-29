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
Let $(X,d)$ be a complete metric space, $A\subset X$ be a bounded set, and $F:X\to X$.
Assume there exists some $k>0$ such that $$d(F(a),F(b))\le kd(a,b)\qquad\text{for all }a,b\in X$$ and that $A\subset F(A)$.
Provide a description of $A$ if $k<1$.
Can anything be said about $A$ if $k\ge1$?
:::

::: {.solution}

::: pf

::: pf-step

If $0<k<1$, then $\boxed{A=\varnothing\text{ or }A=\{x^*\}}$, where $x^*$ is the unique fixed point of $F$.

::: pf-proof

Since $A\subseteq F(A)$ and $F$ is $k$-Lipschitz,
$$
\operatorname{diam}(A)\leq\operatorname{diam}(F(A))
\leq k\,\operatorname{diam}(A).
$$
Boundedness gives $\operatorname{diam}(A)<\infty$, so $k<1$ forces $\operatorname{diam}(A)=0$. Thus $A$ contains at most one point. If $A=\{a\}$, the inclusion $\{a\}\subseteq F(\{a\})=\{F(a)\}$ implies $F(a)=a$. Such a fixed point is unique: if $F(a)=a$ and $F(b)=b$, then $d(a,b)\leq k\,d(a,b)$, hence $a=b$. Completeness guarantees existence of this unique fixed point by the Banach contraction theorem, but the empty set still satisfies the given inclusion.

:::

:::

::: pf-step

If $k\geq1$, nothing beyond boundedness can be said in general: for $X=\RR$ every bounded subset of $\RR$ can occur.

::: pf-proof

Take $X=\RR$ with its usual complete metric and $F=\operatorname{id}_{\RR}$. For any $k\geq1$ the inequality $d(F(a),F(b))=d(a,b)\leq k\,d(a,b)$ holds, and $A=F(A)$ for every bounded subset $A\subseteq\RR$, including the empty set.

:::

:::

:::

:::
