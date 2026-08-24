---
schema: qual/card@1
id: P-5R3FT
kind: problem
title: Unique fixed point of $ce^z$ on $\{\operatorname{Re} z<1\}$ when $|c|<1/3$
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Rouché
  - Zeros
relations: []
review: draft
---

:::{.problem title="?"}
Let $c\in \CC$ with $\abs{c} < {1\over 3}$.
Show that on the open set $\theset{z\in \CC \suchthat \Re(z) < 1}$, the function $f(z) \definedas ce^z$ has exactly one fixed point.
:::

:::{.solution}
The boundary region is $\ts{1+it\st t\in \RR}$, write $g(z) = ce^z-z$ so that fixed points of $f$ are zeros of $g$.

Big: $M(z) = z$.
Small: $m(z) = ce^z$.
Then for $z=1+it$,
\[
\abs{m(z)} = \abs{c}e^{\Re(z)} < ce < 1 \leq \sqrt{1^2+t^2} = \abs{1+it} = \abs{z}
,\]
so $M$ and $g$ have the same number of zeros, and $M$ has a unique zero. 
:::

