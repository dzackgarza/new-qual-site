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
**Part (a).**

<1>1. $f_\alpha(x) = \alpha x$ is a homeomorphism of $G$.
::: {.proof}
left multiplication by $\alpha$ is continuous with continuous inverse $f_{\alpha^{-1}}$.
:::

<1>2. $f_\alpha$ sends the coset $xH$ to $(\alpha x)H$.
::: {.proof}
$f_\alpha(xH) = \{\alpha x h : h \in H\} = (\alpha x)H$.
:::

<1>3. Hence $f_\alpha$ induces a well-defined bijection $\bar f_\alpha: G/H \to G/H$, $xH \mapsto (\alpha x)H$.
::: {.proof}
<1>2.
:::

<1>4. $\bar f_\alpha$ is a homeomorphism.
::: {.proof}
it is induced by the homeomorphism $f_\alpha$ and is compatible with the quotient topology (its inverse is $\bar f_{\alpha^{-1}}$).
:::

<1>5. Hence $G/H$ is homogeneous: for any two cosets $xH$ and $yH$, the map $\bar f_{yx^{-1}}$ sends $xH$ to $yH$.
::: {.proof}
<1>4.
:::

**Part (b).**

<1>1. A one-point set in $G/H$ is $\{xH\} = p(xH)$.
::: {.proof}
definition.
:::

<1>2. $p^{-1}(\{xH\}) = xH$, which is closed in $G$ (since $H$ is closed and left multiplication is a homeomorphism).
::: {.proof}
$xH = f_x(H)$ is closed.
:::

<1>3. Hence $\{xH\}$ is closed in $G/H$.
::: {.proof}
by the definition of the quotient topology, a subset is closed iff its preimage under $p$ is closed.
:::

**Part (c).**

<1>1. Let $U \subseteq G$ be open; we show $p(U)$ is open in $G/H$.
::: {.proof}
setup.
:::

<1>2. $p^{-1}(p(U)) = UH = \bigcup_{h \in H} Uh$, which is open (a union of open sets, since right multiplication is a homeomorphism).
::: {.proof}
$p^{-1}(p(U)) = \{uh : u \in U, h \in H\} = UH = \bigcup_{h \in H} Uh$.
:::

<1>3. Hence $p(U)$ is open in $G/H$.
::: {.proof}
by the definition of the quotient topology, $p(U)$ is open iff $p^{-1}(p(U))$ is open.
:::

**Part (d).**

<1>1. $G/H$ is a group (since $H$ is normal), and the group operations are continuous.
<2>1. Multiplication in $G/H$ is continuous.
::: {.proof}
the multiplication $G/H \times G/H \to G/H$ is induced by the continuous multiplication $G \times G \to G$, and the quotient map is open (part (c)), so the induced map is continuous.
:::
<2>2. Inversion in $G/H$ is continuous.
::: {.proof}
inversion $G/H \to G/H$ is induced by the continuous inversion $G \to G$.
:::
<2>3. One-point sets are closed in $G/H$ (part (b)).
::: {.proof}
part (b).
:::

<1>2. Hence $G/H$ is a topological group.
::: {.proof}
<1>1.
:::

<1>3. Q.E.D.
::: {.proof}
<1>5 (a), <1>3 (b), <1>3 (c), and <1>2 (d).
:::
:::
