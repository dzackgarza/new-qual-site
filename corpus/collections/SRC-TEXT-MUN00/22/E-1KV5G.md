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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.4, printed pp. 265--266** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument is his.

Let $G$ be a topological group with identity $e$ and let $\alpha\in G$. Put $f_{\alpha}(x)=\alpha\cdot x$ and $g_{\alpha}(x)=x\cdot\alpha$. We treat $f_{\alpha}$; the case of $g_{\alpha}$ is the same with the factors exchanged.

*$f_{\alpha}$ is a bijection with inverse $f_{\alpha^{-1}}$.* For every $x$,
$$
f_{\alpha^{-1}}\big(f_{\alpha}(x)\big)=\alpha^{-1}\cdot(\alpha\cdot x)=(\alpha^{-1}\alpha)\cdot x=x,
\qquad
f_{\alpha}\big(f_{\alpha^{-1}}(x)\big)=\alpha\cdot(\alpha^{-1}\cdot x)=x .
$$

*$f_{\alpha}$ and its inverse are continuous.* The multiplication $m:G\times G\to G$ is continuous, hence continuous in each variable separately (Exercise 18.11). Now
$$
f_{\alpha}(x)=m(\alpha,x)=\big(m\circ j\big)(x),\qquad j(x)=\alpha\times x,
$$
where $j$ is continuous (the components are constant and identity, Theorem 18.4); so $f_{\alpha}$ is continuous. The same argument with $\alpha^{-1}$ gives $f_{\alpha}^{-1}=f_{\alpha^{-1}}$ continuous. So $f_{\alpha}$ is a homeomorphism, and likewise $g_{\alpha}$.

*$G$ is homogeneous.* Given $x,y\in G$, put $\alpha=y\cdot x^{-1}$. Then $\alpha^{-1}=x\cdot y^{-1}$ and
$$
f_{\alpha}(x)=(y\cdot x^{-1})\cdot x=y\cdot(x^{-1}x)=y,
$$
so the homeomorphism $f_{\alpha}$ carries $x$ to $y$.
:::
