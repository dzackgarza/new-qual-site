---
schema: qual/card@1
id: E-U8UBU
kind: problem
title: Coset spaces of topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $H$ be a subgroup of the topological group $G$.
If $x \in G$, define $xH = \ts{x \cdot h \mid h \in H}$; this set is called a left coset of $H$ in $G$.
Let $G/H$ denote the collection of left cosets of $H$ in $G$; it is a partition of $G$.
Give $G/H$ the quotient topology.

(a) Show that if $\alpha \in G$, the map $f_\alpha(x) = \alpha \cdot x$ induces a homeomorphism of $G/H$ carrying $xH$ to $(\alpha \cdot x)H$.
Conclude that $G/H$ is a homogeneous space.

(b) Show that if $H$ is a closed set in the topology of $G$, then one-point sets are closed in $G/H$.

(c) Show that the quotient map $p: G \to G/H$ is open.

(d) Show that if $H$ is closed in the topology of $G$ and is a normal subgroup of $G$, then $G/H$ is a topological group.
:::

::: {.solution}
Let $p\colon G\to G/H$ be the quotient map. A map $g\colon G/H\to Z$ is continuous if and only if $g\circ p$ is continuous, by the definition of the quotient topology. Left and right translations of $G$ are homeomorphisms ([[E-1KV5G]]).

<1>1. (a) The map $\bar f_\alpha(xH)=(\alpha x)H$ is a well-defined homeomorphism of $G/H$, and $G/H$ is homogeneous.

::: {.proof}
$f_\alpha(xH)=(\alpha x)H$, so $\bar f_\alpha$ is well defined and $\bar f_\alpha\circ p=p\circ f_\alpha$ is continuous; hence $\bar f_\alpha$ is continuous.
Its inverse is $\bar f_{\alpha^{-1}}$, continuous for the same reason.
Given cosets $xH$ and $yH$, the homeomorphism $\bar f_{yx^{-1}}$ carries $xH$ to $yH$.
:::

<1>2. (b) If $H$ is closed, one-point sets are closed in $G/H$.

::: {.proof}
$p^{-1}(\{xH\})=xH=f_x(H)$ is closed, as the image of the closed set $H$ under a homeomorphism.
:::

<1>3. (c) $p$ is open.

::: {.proof}
For open $U\subseteq G$, $p^{-1}(p(U))=UH=\bigcup_{h\in H}Uh$ is a union of right translates of $U$, hence open, so $p(U)$ is open.
:::

<1>4. (d) If $H$ is closed and normal, $G/H$ is a topological group.

::: {.proof}
Since $H$ is normal, $G/H$ is a group with multiplication $\bar m(xH,yH)=xyH$ and inversion $\bar\iota(xH)=x^{-1}H$, and $\bar m\circ(p\times p)=p\circ m$, $\bar\iota\circ p=p\circ\iota$.
By step <1>3, $p\times p$ is a continuous open surjection, hence a quotient map, so $\bar m$ is continuous; $\bar\iota$ is continuous because $\bar\iota\circ p$ is.
By step <1>2, $G/H$ is $T_1$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 through <1>4 prove (a) through (d).
:::
:::
