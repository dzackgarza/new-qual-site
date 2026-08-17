---
schema: qual/card@1
id: P-3A7RU
kind: problem
title: "Show that the punctured unit disk $\\{z : 0 < |z| < 1\\}$ and the annulu…"
classification:
  areas:
  - real-analysis
  topics:
  - conformal-maps
  - biholomorphisms
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Show that the punctured unit disk $\{z : 0 < |z| < 1\}$ and the annulus $\{z : 1 < |z| < 2\}$ cannot be conformally equivalent.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that the punctured disk $D^* = \{z : 0 < |z| < 1\}$ and the annulus $A = \{z : 1 < |z| < 2\}$ are not conformally equivalent.

<1>1. Suppose $\varphi: D^* \to A$ is a biholomorphism; derive a contradiction.
<2>1. $\varphi$ extends holomorphically to a map $D \to \bar A$.
Proof: $\varphi$ is bounded (its image lies in the bounded annulus $A$), so by the Riemann removable singularity theorem $0$ is a removable singularity; write the extension as $\varphi: D \to \bar A$ with $\varphi(0) = \alpha \in \bar A$.
<2>2. $\alpha \in \bd A$, i.e. $|\alpha| \in \{1, 2\}$.
Proof: $\alpha = \lim_{z \to 0}\varphi(z) \in \bar A$ (since $\varphi$ is bounded and $\varphi(D^*) = A$). If $\alpha \in A$, then $\alpha = \varphi(z_0)$ for a unique $z_0 \in D^*$; but $\varphi$ is a homeomorphism onto $A$, so picking $z_n \to 0$, $\varphi(z_n) \to \alpha$ forces $z_n = \varphi^{-1}(\varphi(z_n)) \to \varphi^{-1}(\alpha) = z_0 \ne 0$, a contradiction.
Hence $\alpha \notin A$, so $\alpha \in \bd A$.
<2>3. $\varphi$ is injective on all of $D$ and $\varphi(D) = A \cup \{\alpha\}$.
Proof: $\varphi$ is injective on $D^*$; by <2>2, $\alpha \notin A = \varphi(D^*)$, so no point of $D^*$ maps to $\alpha$; and $\varphi(D) = \varphi(D^*) \cup \{\varphi(0)\} = A \cup \{\alpha\}$.
<2>4. $\varphi(D)$ is open.
Proof: an injective holomorphic map on a domain is conformal onto its image, so by the open mapping theorem $\varphi(D)$ is open in $\CC$.
<2>5. $A \cup \{\alpha\}$ is not open.
Proof: $\alpha$ lies on $\bd A$, i.e. on the circle $|w| = 1$ or $|w| = 2$; every neighborhood of $\alpha$ contains points of $\CC \setminus \bar A$ (outside the annulus), which do not lie in $A \cup \{\alpha\}$.
<2>6. Contradiction.
Proof: <2>3–<2>4 give $\varphi(D) = A \cup \{\alpha\}$ open, contradicting <2>5.

<1>2. Q.E.D. Proof: <1>1 shows no biholomorphism exists.
:::
