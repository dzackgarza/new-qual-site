---
schema: qual/card@1
id: PR-C9ZEK
kind: proposition
title: Exactness is checked on stalks, and global sections are only left exact
slogan: 'Sheaf exactness is stalkwise; global sections preserve kernels but can lose surjectivity.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Stalks
  - Exact Sequences
  - Cohomology
relations:
- kind: uses
  target: T-3VX80
review: draft
prompts:
- How do you check that a sequence of sheaves is exact?
- Is a surjection of sheaves surjective on sections?
- Where does the failure of right exactness go?
---

::: {.proposition}
Let $X$ be a topological space. A sequence $\mcf \to \mcg \to \mch$ of sheaves of abelian groups on $X$ is exact exactly when
$$
\mcf_p \to \mcg_p \to \mch_p
$$
is exact for every $p \in X$.
For $0 \to \mcf \to \mcg \to \mch \to 0$ exact, the sequence of global sections
$$
0 \to \mcf(X) \to \mcg(X) \to \mch(X)
$$
is exact, but the last map need not be surjective.
:::

::: {.remark}
The associated long exact cohomology sequence begins
$$
0\to H^0(X,\mcf)\to H^0(X,\mcg)\to H^0(X,\mch)\xrightarrow{\delta}H^1(X,\mcf).
$$
A section $s\in H^0(X,\mch)$ lifts to a global section of $\mcg$ exactly when $\delta(s)=0$. In Čech cohomology, local lifts of $s$ differ on overlaps by a $1$-cocycle in $\mcf$ representing $\delta(s)$.
:::
