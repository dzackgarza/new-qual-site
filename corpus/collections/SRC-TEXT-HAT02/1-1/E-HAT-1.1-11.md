---
schema: qual/card@1
id: E-HAT-1.1-11
kind: exercise
title: Inclusion of path-component induces isomorphism on $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Path Components
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

If $X_0$ is the path-component of a space $X$ containing the basepoint $x_0$, show that the inclusion $X_0 \hookrightarrow X$ induces an isomorphism $\pi_1(X_0, x_0) \approx \pi_1(X, x_0)$.

::: solution
**Goal:** Prove that
$$
i_*:\pi_1(X_0,x_0)\to\pi_1(X,x_0)
$$
from the inclusion $i:X_0\hookrightarrow X$ is bijective.

<1> Prove the key image lemma.
    *Proof:*
    <2>1. Let $A$ be connected and $h:A\to X$ satisfy $h(a_0)=x_0$.
    <2>2. For any $a\in A$, choose a path $\alpha$ in $A$ from $a_0$ to $a$.
    <2>3. Then $h\circ\alpha$ is a path in $X$ from $x_0$ to $h(a)$.
    <2>4. Hence $h(a)\in X_0$. So $h(A)\subseteq X_0$.

<1> Surjectivity.
    *Proof:*
    <2>1. A loop in $\pi_1(X,x_0)$ is a map $\gamma:(S^1,x_0)\to(X,x_0)$.
    <2>2. Since $S^1$ is connected and $\gamma(x_0)=x_0$, the lemma gives $\gamma(S^1)\subseteq X_0$.
    <2>3. Therefore every class in $\pi_1(X,x_0)$ is represented by a loop in $X_0$, so $i_*$ is surjective.

<1> Injectivity.
    *Proof:*
    <2>1. If two loops in $X_0$ become homotopic in $X$, there is
        $H:D^2\times I\to X$ with boundary loops in $X_0$.
    <2>2. Since $D^2\times I$ is connected and $H(x_0,0)=x_0$, the lemma gives $H(D^2\times I)\subseteq X_0$.
    <2>3. So the same homotopy lies in $X_0$, giving homotopy in $\pi_1(X_0,x_0)$.
    <2>4. Hence $i_*$ is injective.

<1> Therefore $i_*$ is an isomorphism.

Authored by **Codex 5.3 Spark Extra High**.
:::
