---
schema: qual/card@1
id: P-O3LYK
kind: problem
title: "Let $U \\subset \\mathbb{C}$ be an open set containing $\\overline{D}(P,r)$."
classification:
  areas:
  - real-analysis
  topics:
  - rouche
  - holomorphic-functions
relations: []
review: draft
---

::: {.problem title="?"}
Let $U \subset \mathbb{C}$ be an open set containing $\overline{D}(P,r)$.
Prove that if $f : U \to \mathbb{C}$ is a holomorphic function such that $f$ is nowhere zero on $\partial D(P,r)$ and $g : U \to \mathbb{C}$ is a holomorphic function sufficiently uniformly close to $f$ on $\partial D(P,r)$, then the number of zeros of $f$ in $D(P,r)$ equals the number of zeros of $g$ in $D(P,r)$ (counting multiplicity).
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $U \supset \overline{D(P,r)}$ be open, $f: U \to \CC$ holomorphic and nowhere zero on $\bd D(P,r)$. Show that if $g: U \to \CC$ is holomorphic and sufficiently uniformly close to $f$ on $\bd D(P,r)$, then $f$ and $g$ have the same number of zeros in $D(P,r)$ (counting multiplicity).

<1>1. $m := \min_{z \in \bd D(P,r)} |f(z)| > 0$.
    Proof: $f$ is nowhere zero on the compact set $\bd D(P,r)$ by hypothesis and $|f|$ is continuous.

<1>2. Choose $g$ with $|g(z) - f(z)| < m$ on $\bd D(P,r)$.
    Proof: this is what "sufficiently uniformly close" means: uniform closeness means $\sup_{\bd D(P,r)}|g - f| < m$.

<1>3. $|g(z) - f(z)| < |f(z)|$ on $\bd D(P,r)$.
    Proof: <1>1 and <1>2: $|g - f| < m \le |f|$ on the boundary.

<1>4. $f$ and $g$ have the same number of zeros in $D(P,r)$ counting multiplicity.
    Proof: Rouch\'e's theorem on the circle $\bd D(P,r)$ using <1>3.

<1>5. Q.E.D.
    Proof: <1>1–<1>4 establish the claim.
:::
