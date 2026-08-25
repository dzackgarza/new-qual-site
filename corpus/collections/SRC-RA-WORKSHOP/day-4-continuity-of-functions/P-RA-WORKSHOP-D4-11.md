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
---

::: {.problem title="?"}
(June 2013 #5b) Let $(X,d)$ be a complete metric space, $A\subset X$ be a bounded set, and $F:X\to X$.
Assume there exists some $k>0$ such that $$d(F(a),F(b))\le kd(a,b)\qquad\text{for all }a,b\in X$$ and that $A\subset F(A)$.
Provide a description of $A$ if $k<1$.
Can anything be said about $A$ if $k\ge1$?
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Case $k < 1$: $A$ is a singleton.
Proof: $A \subseteq F(A)$ gives $\mathrm{diam}(A) \le \mathrm{diam}(F(A))$ (a subset has no larger diameter).
Since $F$ is $k$-Lipschitz with $k < 1$, $\mathrm{diam}(F(A)) \le k\,\mathrm{diam}(A)$.
Hence $\mathrm{diam}(A) \le k\,\mathrm{diam}(A)$, forcing $\mathrm{diam}(A) = 0$ (as $k < 1$ and $\mathrm{diam}(A) < \infty$ by boundedness).
So $A$ contains at most one point; since $A \subseteq F(A)$ and $A \ne \varnothing$ (say $A$ is nonempty — if empty, trivially a singleton set is described), $A = \{a\}$, and $a \in F(A) = \{F(a)\}$ forces $F(a) = a$: $A$ is the singleton containing the unique fixed point of the contraction $F$.
(Uniqueness: two fixed points $a \ne a'$ would satisfy $d(a,a') = d(F(a),F(a')) \le k\,d(a,a') < d(a,a')$, impossible.)
Existence of the fixed point is the Banach contraction theorem (complete space, $k < 1$), and $A$ must be exactly that point.
<1>2. Case $k \ge 1$: nothing can be said in general.
Proof: take $X = \mathbb{R}$ with the usual metric (complete) and $F = \mathrm{id}$, $k = 1$.
Then $A \subseteq F(A) = A$ holds for every bounded nonempty $A$, and $A$ can be any bounded set (a point, an interval, infinitely many points).
So no structural description of $A$ is possible from the hypotheses alone when $k \ge 1$.
<1>3. Q.E.D.
:::
