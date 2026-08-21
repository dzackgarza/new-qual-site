---
schema: qual/card@1
id: P-NL22Q
kind: problem
title: The ring of analytic functions on a domain is an integral domain
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
relations: []
review: draft
solved: true
---

::: problem
Suppose $D$ is a domain and $f, g$ are analytic on $D$.

Prove that if $fg = 0$ on $D$, then either $f \equiv 0$ or $g\equiv 0$ on $D$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that if $f, g$ are analytic on a domain $D$ and $fg \equiv 0$ on $D$, then either $f \equiv 0$ or $g \equiv 0$ on $D$.

<1>1. Assume $f \not\equiv 0$; it suffices to show $g \equiv 0$.
Proof: By symmetry between $f$ and $g$.

<1>2. The zero set $Z \definedas \theset{z \in D \suchthat f(z) = 0}$ is a closed subset of $D$ with no accumulation point in $D$.
<2>1. $Z$ is closed in $D$.
Proof: $f$ is continuous, and $Z$ is the preimage of the closed set $\theset{0}$.
<2>2. $Z$ has empty interior.
Proof: If $Z$ contained a nonempty open set $U$, then $f \equiv 0$ on $U$, and by the identity theorem $f \equiv 0$ on $D$, contradicting <1>1.

<1>3. $D \setminus Z$ is nonempty and open in $D$.
Proof: $Z \neq D$ (else $f \equiv 0$, contradicting <1>1) and $Z$ is closed by <1>2.1.

<1>4. $g \equiv 0$ on $D \setminus Z$.
Proof: For $z \in D \setminus Z$, $f(z) \neq 0$, so $fg(z) = 0$ forces $g(z) = 0$.

<1>5. $g \equiv 0$ on $D$.
Proof: <1>3 gives a nonempty open set (e.g. a disk contained in $D \setminus Z$) on which $g$ vanishes; by the identity theorem, $g$ vanishes on all of $D$.

<1>6. Q.E.D. Proof: <1>1--<1>5 show that if $f \not\equiv 0$ then $g \equiv 0$; the alternative case is symmetric.
:::
