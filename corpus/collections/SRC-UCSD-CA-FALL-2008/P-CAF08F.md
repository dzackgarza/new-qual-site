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
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: that the Riemann map exists because G is a proper simply connected domain,
    with f(G) contained in G used to make g a self-map of the disk; that alpha and beta are
    distinct and that the fixed point of h is nonzero, both by injectivity of the Riemann map
    and of psi_alpha; the inverse psi_{-alpha}; and the equality case of Schwarz's lemma
    applied at an interior point. Not claimed: a retained solution set; the provenance names
    the examination paper.
---

::: {.problem}
Let $G \subset \CC$ be open, connected, and simply connected, $G \neq \CC$.
Let $f \in H(G)$ with $f(G) \subset G$.
Suppose there exist $a, b \in \CC$, $a \neq b$ such that $f(a) = a$ and $f(b) = b$.
Prove that $f(z) = z$ for all $z \in G$.

Hint: Prove it first for the case $G = B(0; 1)$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Fall 2008 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose; the hint's reduction to $\DD$ is carried out by the two conjugations, and the equality case of Schwarz's lemma does the rest.

Throughout $G\subsetneq\CC$ is open, connected and simply connected, $f\in H(G)$ with $f(G)\subset G$, and $a\ne b$ are fixed points of $f$ in $G$.

::: pf

::: {.pf-step #conjugation}
There is a biholomorphism $\phi:G\to\DD$, and $g=\phi\circ f\circ\phi^{-1}$ is a holomorphic self-map of $\DD$ fixing the two distinct points $\alpha=\phi(a)$ and $\beta=\phi(b)$.

::: pf-proof
$G$ is a proper simply connected domain, so the Riemann mapping theorem provides a biholomorphism $\phi$ onto $\DD$. Then $g$ is a composite of holomorphic maps with $g(\DD)=\phi(f(G))\subseteq\phi(G)=\DD$; it fixes $\alpha$ because $g(\alpha)=\phi(f(a))=\phi(a)$ and similarly for $\beta$. Finally $\alpha\ne\beta$ since $\phi$ is injective and $a\ne b$.

:::

:::

::: {.pf-step #normalize}
With $\psi_\alpha(z)=\frac{z-\alpha}{1-\overline\alpha z}$ and $h=\psi_\alpha\circ g\circ\psi_\alpha^{-1}$, the map $h$ is a holomorphic self-map of $\DD$ with $h(0)=0$ that fixes the nonzero point $z_0=\psi_\alpha(\beta)$.

::: pf-proof
$\psi_\alpha$ is a holomorphic automorphism of $\DD$ with inverse $\psi_{-\alpha}$, since $\abs\alpha<1$, so $h$ maps $\DD$ into $\DD$ holomorphically. $h(0)=\psi_\alpha(g(\alpha))=\psi_\alpha(\alpha)=0$, and $h(z_0)=\psi_\alpha(g(\beta))=\psi_\alpha(\beta)=z_0$. Finally $z_0\ne0$ because $\psi_\alpha$ is injective and $\beta\ne\alpha$.

:::

:::

::: {.pf-step #schwarz}
$h(z)=e^{i\theta}z$ for some real $\theta$.

::: pf-proof
$h$ is holomorphic on $\DD$ with $h(0)=0$, so Schwarz's lemma gives $\abs{h(z)}\le\abs z$ for all $z\in\DD$. At the fixed point $z_0\ne0$ we have $\abs{h(z_0)}=\abs{z_0}$, so equality holds at an interior point of $\DD$; the equality case of Schwarz's lemma then makes $h$ a rotation, $h(z)=e^{i\theta}z$ for a constant $\theta\in\RR$.

:::

:::

::: {.pf-step #rotation-trivial}
$e^{i\theta}=1$, so $h$ is the identity.

::: pf-proof
$z_0=h(z_0)=e^{i\theta}z_0$ with $z_0\ne0$, so $e^{i\theta}=1$ and $h(z)=z$ for all $z$.

:::

:::

::: {.pf-step #conclusion}
$f(z)=z$ for all $z\in G$.

::: pf-proof
$h=\mathrm{id}$ gives $\psi_\alpha\circ g\circ\psi_\alpha^{-1}=\mathrm{id}$, hence $g=\mathrm{id}$ on $\DD$, hence $f=\phi^{-1}\circ g\circ\phi=\mathrm{id}$ on $G$.

:::

:::

:::
:::
