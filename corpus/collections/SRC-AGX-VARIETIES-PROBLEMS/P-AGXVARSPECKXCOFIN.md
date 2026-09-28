---
schema: qual/card@1
id: P-AGXVARSPECKXCOFIN
kind: problem
title: $\operatorname{Specm} k[x]$ carries the cofinite topology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Zariski Topology
  - Cofinite Topology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg 2.9 in the recorded source. The source uses Specm A, the
    maximal spectrum of an affine domain, for the classical affine variety
    associated to A. For A=k[x] this is the affine line.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced Spec k[x] by Specm k[x]. The original scheme-spectrum statement
    is false: Spec k[x] contains the generic point (0), whose singleton is not
    closed, whereas every singleton is closed in a cofinite topology.
    Also made the source's algebraically closed base field explicit.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Identified maximal ideals with (x-a), described V(I) for nonzero ideals by
    the finitely many roots of a generator, and checked conversely that every
    finite subset is cut out by a product of linear factors.
---

::: {.problem}
Let $k$ be an algebraically closed field and let
$$
\operatorname{Specm}k[x]
$$
be the maximal spectrum with its Zariski topology. Show that this topology is
the cofinite topology.
:::

::: {.solution}
<1>1. The points of $\operatorname{Specm}k[x]$ are exactly
$$
\mathfrak m_a=(x-a),
\qquad
a\in k.
$$

::: {.proof}
By the weak Nullstellensatz, every maximal ideal of the finitely generated
$k$-algebra $k[x]$ is the kernel of evaluation at a point $a\in k$. Hence it
has the form
$$
(x-a).
$$
Conversely,
$$
k[x]/(x-a)\cong k
$$
is a field, so every $(x-a)$ is maximal.
:::

<1>2. Every proper Zariski-closed subset of
$\operatorname{Specm}k[x]$ is finite.

::: {.proof}
Let
$$
Z=V_{\max}(I)
$$
be a proper closed subset. Since $k[x]$ is a principal ideal domain, write
$$
I=(f).
$$
Properness of $Z$ excludes $I=(0)$, because
$$
V_{\max}(0)=\operatorname{Specm}k[x].
$$
Thus
$$
f\ne0.
$$

By step <1>1,
$$
\mathfrak m_a\in V_{\max}(f)
\quad\Longleftrightarrow\quad
f\in(x-a)
\quad\Longleftrightarrow\quad
f(a)=0.
$$
A nonzero polynomial has only finitely many roots. Therefore $Z$ is finite.
:::

<1>3. Every finite subset of $\operatorname{Specm}k[x]$ is Zariski closed.

::: {.proof}
Let
$$
F
=
\{\mathfrak m_{a_1},\ldots,\mathfrak m_{a_r}\}.
$$
Put
$$
g(x)
=
\prod_{i=1}^r(x-a_i).
$$
For $a\in k$,
$$
g\in\mathfrak m_a
\quad\Longleftrightarrow\quad
g(a)=0
\quad\Longleftrightarrow\quad
a\in\{a_1,\ldots,a_r\}.
$$
Hence
$$
V_{\max}(g)=F.
$$
The empty set is also closed, being $V_{\max}(1)$.
:::

<1>4. The Zariski closed subsets are exactly the whole space and the finite
subsets.

::: {.proof}
Step <1>2 shows every proper closed subset is finite. Step <1>3 shows every
finite subset is closed. Together with the whole space, these are exactly the
closed subsets.
:::

<1>5. Therefore the Zariski topology on $\operatorname{Specm}k[x]$ is the
cofinite topology.

::: {.proof}
The cofinite topology is defined by declaring the whole space and the finite
subsets to be the closed sets. Step <1>4 gives exactly this family.

Equivalently, the correspondence between affine varieties and their
coordinate rings identifies
$$
\operatorname{Specm}k[x]\cong\AA^1_k,
$$
and this is the special case of
[[P-AGXVARCURVECOFIN|the cofinite topology on an irreducible curve]].
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
