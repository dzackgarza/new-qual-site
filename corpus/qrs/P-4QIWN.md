---
schema: qual/card@1
id: P-4QIWN
kind: problem
title: "Let $f(z)$ be a non-constant analytic function in $|z|>0$ such that"
classification:
  areas:
  - complex-analysis
  topics:
  - essential-singularities
  - singularities
  - identity-theorem
  - zeros
relations: []
review: draft
solved: true
---

::: problem
Let $f(z)$ be a non-constant analytic function in $|z|>0$ such that $f(z_n) = 0$ for infinite many points $z_n$ with $\lim_{n \rightarrow \infty} z_n =0$.
Show that $z=0$ is an essential singularity for $f(z)$.
(An example of such a function is $f(z) = \sin (1/z)$.)
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $f$ is nonconstant and analytic in $\theset{\abs z > 0}$ with zeros $z_n \to 0$, show $z = 0$ is an essential singularity of $f$.

<1>1. $z = 0$ is either removable, a pole, or an essential singularity.
Proof: $f$ is analytic in a punctured neighborhood of $0$, so its Laurent expansion about $0$ determines the type of the isolated singularity: no negative terms (removable), finitely many (pole), or infinitely many (essential).

<1>2. $z = 0$ is not a removable singularity.
Proof: If $0$ were removable, $f$ would extend to a function $\tilde f$ holomorphic in a disk $D_\varepsilon(0)$, with $\tilde f(z_n) = f(z_n) = 0$ for infinitely many $z_n \in D_\varepsilon(0)$ accumulating at $0 \in D_\varepsilon(0)$; by the identity theorem, $\tilde f \equiv 0$, contradicting that $f$ is nonconstant.

<1>3. $z = 0$ is not a pole.
Proof: If $0$ were a pole of order $m \geq 1$, then $f(z) = z^{-m} g(z)$ with $g$ holomorphic near $0$ and $g(0) \neq 0$; by continuity, $g(z) \neq 0$ in a punctured neighborhood of $0$, so $f$ has no zeros there — contradicting the existence of zeros $z_n \to 0$, $z_n \neq 0$.

<1>4. Q.E.D. Proof: By <1>1, <1>2 and <1>3, the only remaining possibility is that $z = 0$ is an essential singularity.
(Example: $f(z) = \sin(1/z)$ has zeros at $z_n = 1/(n\pi) \to 0$ and an essential singularity at $0$.)
:::
