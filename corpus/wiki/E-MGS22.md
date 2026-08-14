---
schema: qual/card@1
id: E-MGS22
kind: exercise
title: "Let $f : X \\to Y$ be a continuous function, with $X$ compact."
classification:
  areas:
  - topology
  topics:
  - compactness
  - continuity
relations: []
review: draft
---

Let $f : X \to Y$ be a continuous function, with $X$ compact.
Show that $f(X)$ is compact.

::: {.solution}
::: {.concept}
:::
Let $f:X\to Y$ be continuous with $X$ compact, and $\theset{U_\alpha} \covers f(X)$ be an open cover.
Then $\theset{f\inv(U_\alpha)} \covers X$ is an open cover of $X$, since $x\in X \implies f(x) \in f(X) \implies f(x) \in U_\alpha$ for some $\alpha$, so $x\in f\inv(U_\alpha)$ by definition.
By compactness of $X$ there is a finite subcover $\theset{f\inv(U_j) \suchthat j\leq N} \covers X$.
Then the finite subcover $\theset{U_j\suchthat j\leq N} \covers f(X)$, since if $y\in f(X)$, $y\in U_\alpha$ for some $\alpha$ and thus $f\inv(y) \in f\inv(U_j)$ for some $j$ since $\theset{U_j}$ is a cover of $X$.
:::
