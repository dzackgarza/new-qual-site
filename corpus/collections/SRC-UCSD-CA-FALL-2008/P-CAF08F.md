---
schema: qual/card@1
id: P-CAF08F
kind: problem
title: "A holomorphic self-map of a simply connected proper domain with two fixed points is the identity"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G \subset \mathbb{C}$ be open, connected, and simply connected, $G \neq \mathbb{C}$.
Let $f \in H(G)$ with $f(G) \subset G$.
Suppose there exist $a, b \in \mathbb{C}$, $a \neq b$ such that $f(a) = a$ and $f(b) = b$.
Prove that $f(z) = z$ for all $z \in G$.
:::

::: solution
By the Riemann mapping theorem, choose a conformal bijection
\[
\phi:G\to\mathbb D.
\]
Set
\[
g=\phi\circ f\circ\phi^{-1}:\mathbb D\to\mathbb D.
\]
Then $g$ fixes the two distinct points
\[
\alpha=\phi(a),\qquad \beta=\phi(b).
\]

Conjugate once more by the disk automorphism
\[
\psi_\alpha(z)=\frac{z-\alpha}{1-\overline\alpha z}
\]
and define
\[
h=\psi_\alpha\circ g\circ\psi_\alpha^{-1}.
\]
Then $h:\mathbb D\to\mathbb D$ is holomorphic, $h(0)=0$, and it fixes the
nonzero point $\psi_\alpha(\beta)$.

Schwarz's lemma gives $|h(z)|\le|z|$. Since equality holds at the nonzero fixed
point, the equality case of Schwarz's lemma implies
\[
h(z)=e^{i\theta}z
\]
for some real $\theta$. The nonzero fixed point forces $e^{i\theta}=1$, hence
$h$ is the identity. Therefore $g$ and then $f$ are identities:
\[
f(z)=z\qquad(z\in G).
\]
:::
