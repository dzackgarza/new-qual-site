---
schema: qual/card@1
id: P-AMD-2AFAX7LD
kind: problem
title: $S^3 - \{p_0, p_1\} \simeq S^2$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that $S^3 - \{p_0, p_1\} \simeq S^2$
:::

::: {.solution}
**Goal:** Prove that the complement of two distinct points in the 3-sphere, $S^3 \setminus \{p_0, p_1\}$, is homotopy equivalent to $S^2$.

<1>1. $S^3 \setminus \{p_0\}$ is homeomorphic to $\mathbb{R}^3$.
<2>1. Standard stereographic projection from the pole $p_0$ gives a homeomorphism $\phi \colon S^3 \setminus \{p_0\} \to \mathbb{R}^3$.
<2>2. Proof: Stereographic projection is well-defined, continuous, bijective, and has a continuous inverse given by the explicit inverse stereographic projection formula.
Q.E.D.

<1>2. Under the homeomorphism $\phi$, $S^3 \setminus \{p_0, p_1\}$ is homeomorphic to $\mathbb{R}^3 \setminus \{\phi(p_1)\}$.
<2>1. Proof: A homeomorphism $\phi \colon X \to Y$ restricts to a homeomorphism $X \setminus \{x\} \to Y \setminus \{\phi(x)\}$ for any point $x \in X$.
Here $X = S^3 \setminus \{p_0\}$ and $x = p_1 \in X$ since $p_1 \neq p_0$.
Q.E.D.

<1>3. $\mathbb{R}^3 \setminus \{\phi(p_1)\}$ is homeomorphic to $\mathbb{R}^3 \setminus \{0\}$.
<2>1. Proof: Translation by $-\phi(p_1)$, given by $v \mapsto v - \phi(p_1)$, is a homeomorphism of $\mathbb{R}^3$ that maps $\phi(p_1)$ to the origin $0$.
Q.E.D.

<1>4. $\mathbb{R}^3 \setminus \{0\}$ deformation retracts to the unit sphere $S^2$.
<2>1. Let $r \colon \mathbb{R}^3 \setminus \{0\} \to S^2$ be defined by $r(x) = \frac{x}{\|x\|}$ and let $\iota \colon S^2 \hookrightarrow \mathbb{R}^3 \setminus \{0\}$ be the inclusion.
<2>2. The map $r$ is continuous and restricts to the identity on $S^2$ because for any $x \in S^2$, $\|x\| = 1 \implies r(x) = x$.
<2>3. Define $H \colon (\mathbb{R}^3 \setminus \{0\}) \times [0, 1] \to \mathbb{R}^3 \setminus \{0\}$ by $H(x, t) = (1-t)x + t \frac{x}{\|x\|}$.
<2>4. For all $x \in \mathbb{R}^3 \setminus \{0\}$ and $t \in [0, 1]$, $(1-t) + \frac{t}{\|x\|} > 0$, so $H(x, t) \neq 0$.
Thus $H$ is a well-defined continuous map into $\mathbb{R}^3 \setminus \{0\}$.
<2>5. $H(x, 0) = x = \operatorname{id}_{\mathbb{R}^3 \setminus \{0\}}(x)$, $H(x, 1) = \iota(r(x))$, and for every $s \in S^2$ and $t \in [0, 1]$, $H(s, t) = s$.
<2>6. Proof: By <2>1–<2>5, $H$ is a strong deformation retraction of $\mathbb{R}^3 \setminus \{0\}$ onto $S^2$.
Q.E.D.

<1>5. Homotopy equivalence is an equivalence relation preserved under homeomorphisms.
<2>1. Proof: Every homeomorphism is a homotopy equivalence, and a deformation retraction is a homotopy equivalence.
Composing homotopy equivalences yields a homotopy equivalence: $$S^3 \setminus \{p_0, p_1\} \cong \mathbb{R}^3 \setminus \{\phi(p_1)\} \cong \mathbb{R}^3 \setminus \{0\} \simeq S^2.$$ Q.E.D.

<1>6. Q.E.D. <2>1. Proof: Combining <1>1 through <1>5 establishes $S^3 \setminus \{p_0, p_1\} \simeq S^2$.
:::
