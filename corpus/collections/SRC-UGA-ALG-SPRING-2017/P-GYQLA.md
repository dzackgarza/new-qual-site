---
schema: qual/card@1
id: P-GYQLA
kind: problem
title: Left translation is an odd permutation iff its order is even and $|G|$ divided
  by the order is odd
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and let $\pi: G \to \operatorname{Sym}(G)$ be the Cayley (left regular) representation, where $\pi(x)(g) = x g$ for all $g \in G$.

Prove that $\pi(x)$ is an odd permutation if and only if the order $\operatorname{ord}(\pi(x))$ is even and $|G| / \operatorname{ord}(\pi(x))$ is odd.
:::

::: {.solution}
Fix $x\in G$, and put $k=\operatorname{ord}(x)$ and $m=|G|/k$.

<1>1. The order of $\pi(x)$ is $k$, and its cycle decomposition consists of exactly $m$ cycles of length $k$.

::: {.proof}
The left regular action is faithful: if $\pi(y)$ is the identity, then evaluating at the identity element of $G$ gives $y=1$. Thus $\operatorname{ord}(\pi(x))=k$. For every $g\in G$, the orbit under $\pi(x)$ is the right coset $\langle x\rangle g=\{g,xg,\ldots,x^{k-1}g\}$, consisting of exactly $k$ elements. These right cosets partition $G$ into $m$ orbits, each providing one cycle of length $k$.
:::

<1>2. The sign of the permutation is
\[
\operatorname{sgn}(\pi(x))=(-1)^{m(k-1)}.
\]

::: {.proof}
A cycle of length $k$ is a product of $k-1$ transpositions and therefore has sign $(-1)^{k-1}$. By step <1>1, $\pi(x)$ is a product of $m$ such disjoint cycles. Multiplicativity of the sign homomorphism gives the displayed formula.
:::

<1>3. The permutation $\pi(x)$ is odd if and only if $\operatorname{ord}(\pi(x))$ is even and $|G|/\operatorname{ord}(\pi(x))$ is odd.

::: {.proof}
By step <1>2, $\pi(x)$ is odd precisely when $m(k-1)$ is odd. An integer product is odd exactly when both factors are odd. Thus the condition is that $m$ be odd and $k-1$ be odd, equivalently that $m$ be odd and $k$ be even. Substitute $k=\operatorname{ord}(\pi(x))$ and $m=|G|/k$ from step <1>1.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the equivalence.
:::
:::
