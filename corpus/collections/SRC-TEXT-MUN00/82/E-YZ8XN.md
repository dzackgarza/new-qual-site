---
schema: qual/card@1
id: E-YZ8XN
kind: problem
title: Simple connectedness implies semilocal simple connectedness
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

::: {.exercise}

Show that a simply connected space is semilocally simply connected.
:::

::: {.solution}
If \(X\) is simply connected, then \(X\) is path connected and
\[
\pi_1(X,x)=0
\]
for every basepoint \(x\in X\). Let \(x\in X\). Taking \(U=X\) itself (or any path-connected neighborhood of \(x\)), the inclusion-induced homomorphism
\[
\pi_1(U,x)\longrightarrow\pi_1(X,x)
\]
has trivial target and hence is trivial. This is precisely the semilocal simple-connectedness condition. Therefore every simply connected space is semilocally simply connected.
:::
