---
schema: qual/card@1
id: E-1KV5G
kind: problem
title: Translations are homeomorphisms; topological groups are homogeneous
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 4, printed p. 146; the
    stored statement is the printed one, including the definition of homogeneous.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.4, printed pp.
    265-266. Translations are bijections with the translation by the inverse as inverse, and
    they are continuous because multiplication is continuous in each variable separately
    (Exercise 18.11); homogeneity by the translation carrying x to y, namely alpha = y
    x^{-1}. (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the two inverses of f_alpha, continuity of
    f_alpha as m composed with x -> alpha x x (Theorem 18.4), the same for g_alpha, and
    homogeneity with alpha = y x^{-1}. Whitman, Exercise TG.4, printed pp. 265-266. The
    printed statement needed no repair.
---

::: {.exercise}

Let $\alpha$ be an element of the topological group $G$.
Show that the maps $f_\alpha, g_\alpha: G \to G$ defined by

$$
f_\alpha(x) = \alpha \cdot x \quad \text{and} \quad g_\alpha(x) = x \cdot \alpha
$$

are homeomorphisms of $G$.
Conclude that $G$ is a homogeneous space.
(This means that for every pair $x, y$ of points of $G$, there exists a homeomorphism of $G$ onto itself that carries $x$ to $y$.)
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.4, printed pp. 265--266** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument is his.

Let $G$ be a topological group with multiplication $m:G\times G\to G$, $m(x,y)=x\cdot y$, and let $\alpha\in G$. Put $f_{\alpha}(x)=\alpha\cdot x$ and $g_{\alpha}(x)=x\cdot\alpha$.

::: pf

::: {.pf-step #bijection}
$f_{\alpha}$ is a bijection with inverse $f_{\alpha^{-1}}$.

::: pf-proof
For every $x\in G$,
$$
f_{\alpha^{-1}}\big(f_{\alpha}(x)\big)=\alpha^{-1}\cdot(\alpha\cdot x)=(\alpha^{-1}\alpha)\cdot x=e\cdot x=x,
\qquad
f_{\alpha}\big(f_{\alpha^{-1}}(x)\big)=\alpha\cdot(\alpha^{-1}\cdot x)=(\alpha\alpha^{-1})\cdot x=x,
$$
using associativity and the defining properties of $\alpha^{-1}$ and $e$.
:::

:::

::: {.pf-step #continuous}
$f_{\alpha}$ and $f_{\alpha}^{-1}=f_{\alpha^{-1}}$ are continuous.

::: pf-proof
The map $j:G\to G\times G$, $j(x)=\alpha\times x$, is continuous because its components are the constant map $\alpha$ and the identity of $G$ (Theorem 18.4), and $f_{\alpha}=m\circ j$ is then continuous as a composite of continuous maps. The same argument with $\alpha^{-1}$ in place of $\alpha$ shows that $f_{\alpha^{-1}}$ is continuous.
:::

:::

::: {.pf-step #homeomorphism}
$f_{\alpha}$ and $g_{\alpha}$ are homeomorphisms of $G$.

::: pf-proof
$f_{\alpha}$ is a bijection with continuous inverse by steps [](#bijection){.pf-ref} and [](#continuous){.pf-ref}, hence a homeomorphism. For $g_{\alpha}$ the same three facts hold with the multiplication read in the other order: $g_{\alpha^{-1}}\circ g_{\alpha}$ and $g_{\alpha}\circ g_{\alpha^{-1}}$ are the identity, and $g_{\alpha}=m\circ j'$ with $j'(x)=x\times\alpha$ continuous, so $g_{\alpha}$ is a homeomorphism with inverse $g_{\alpha^{-1}}$.
:::

:::

::: {.pf-step #homogeneous}
$G$ is homogeneous.

::: pf-proof
Let $x,y\in G$ and put $\alpha=y\cdot x^{-1}$. Then
$$
f_{\alpha}(x)=(y\cdot x^{-1})\cdot x=y\cdot(x^{-1}x)=y\cdot e=y,
$$
and $f_{\alpha}$ is a homeomorphism of $G$ onto itself by step [](#homeomorphism){.pf-ref}. So some homeomorphism of $G$ carries $x$ to $y$.
:::

:::

:::
:::
