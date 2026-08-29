---
schema: qual/card@1
id: P-DKDKR
kind: problem
title: Lifting the group law to a covering of a topological group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
relations: []
review: draft
---

::: problem
4. Let $p: \tilde G \surjects G$ be such a covering, $a,b\in \tilde G$, we then want to show that $p(a)p(b) = p(a\star b)$ for some group operation $\star$ which we need to construct.

Pick a basepoint $x\in G$ and any point $\tilde x \in p^{-1}(x)$.
Since $\tilde G$ is path connected, pick two paths $\alpha, \beta$ from $\tilde x$ to $a,b$ respectively.

Now define a path $f: I \into G$ by $f(t) = (p\circ \alpha)(t) \cdot (p\circ \beta)(t)$, that is, evaluating $f, g$ at a given time in $\tilde G$, projecting the results down into $G$, and multiplying them there.
By uniqueness of path lifting, this yields a lift $\tilde f: I \into \tilde G$

Then define $a\star b = \tilde f(1)$, the endpoint of $\tilde f$ in $\tilde G$.
Then by construction,

$p(a\star b) = p(\tilde f(1)) = f(1) = (p\circ\alpha)(1)\cdot (p\circ\beta)(1) = p(a)p(b)$.
(Need to show this is continuous, and doesn't depend on $\alpha,\beta$?)
:::
