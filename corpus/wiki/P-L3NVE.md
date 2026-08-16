---
schema: qual/card@1
id: P-L3NVE
kind: problem
title: "Let $X = S^1 \\cross S^1$ and $A\\subset X$ be a subspace with $A \\cong S^1 \\vee S^1$. Show that there is no\u2026"
classification:
  areas:
  - topology
  topics:
  - retracts
  - fundamental-group
  - surfaces
relations: []
review: draft
---

::: problem
Let $X = S^1 \cross S^1$ and $A\subset X$ be a subspace with $A \cong S^1 \vee S^1$.
Show that there is no retraction from $X$ to $A$.

**Solution**:

We have $\pi_1(S^1 \cross S^1) = \pi_1(S^1) \cross \pi_1(S^1)$ since $S^1$ is path-connected (by a lemma from the problem sets), and this equals $\ZZ \cross \ZZ$.

We also have $\pi_1(S^1 \vee S^1) = \pi_1(S^1) \ast_{\theset{pt}} \pi_1(S^1)$, which by Van-Kampen is $\ZZ\ast \ZZ$.

Suppose $X$ retracts onto $A$, we can then look at the inclusion $\iota: A \injects X$.
The induced homomorphism $\iota_*: \pi_1(A) \injects \pi_1(X)$ is then also injective, so we've produced an injection from $f: \ZZ \ast \ZZ \injects \ZZ \cross \ZZ$.

This is a contradiction, because no such injection can exists.
In particular, the commutator $[a,b]$ is nontrivial in the source.
But $f(aba^{-1}b^{-1}) = f(a)f(b)f(a)^{-1}f(b)^{-1}$ since $f$ is a homomorphism, but since the target is a commutative group, this has to equal $f(a)f(a)^{-1} f(b)f(b)^{-1} = e$.
So there is a non-trivial element in the kernel of $f$, and $f$ can not be injective - a contradiction.
:::
