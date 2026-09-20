---
schema: qual/card@1
id: P-AGXVAREXREDUCIBLE
kind: problem
title: The affine cubic $V(x(xy-1))$ has two irreducible components
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducible Components
  - Plane Curves
  - Reducibility
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Example 3.2 in the recorded source. Under the notes'
    standing convention k is algebraically closed of characteristic zero, and
    the example states that V(x(xy-1)) is reducible with two irreducible
    components.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's ambient affine plane and standing base-field convention
    explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the decomposition V(fg)=V(f) union V(g), irreducibility of the
    line and hyperbola from their coordinate domains, and maximality of the
    two incomparable irreducible closed subsets.
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic zero, and let
$$
X=V(x(xy-1))\subseteq\AA^2_k.
$$
Show that $X$ is reducible and has exactly two irreducible components.
:::

::: {.solution}
Put
$$
L=V(x),
\qquad
H=V(xy-1).
$$

<1>1. The cubic decomposes as
$$
\boxed{X=L\cup H.}
$$

::: {.proof}
For any point $(a,b)\in\AA^2_k$,
$$
a(ab-1)=0
$$
if and only if
$$
a=0
\qquad\text{or}\qquad
ab-1=0.
$$
Therefore
$$
V(x(xy-1))
=
V(x)\cup V(xy-1)
=
L\cup H.
$$
:::

<1>2. The closed subset $L$ is irreducible.

::: {.proof}
Its coordinate ring is
$$
k[L]
=
k[x,y]/(x)
\cong
k[y],
$$
which is an integral domain. Hence $L$ is irreducible.
:::

<1>3. The closed subset $H$ is irreducible.

::: {.proof}
Its coordinate ring is
$$
k[H]
=
k[x,y]/(xy-1)
\cong
k[x,x^{-1}],
$$
which is an integral domain. Hence $H$ is irreducible.
:::

<1>4. Neither $L$ nor $H$ contains the other.

::: {.proof}
The point
$$
(0,0)
$$
lies in $L$ but not in $H$, while
$$
(1,1)
$$
lies in $H$ but not in $L$.
Therefore
$$
L\nsubseteq H
\qquad\text{and}\qquad
H\nsubseteq L.
$$
:::

<1>5. The irreducible components of $X$ are exactly
$$
\boxed{
L=V(x)
\quad\text{and}\quad
H=V(xy-1).
}
$$

::: {.proof}
By steps <1>2--<1>3, both $L$ and $H$ are irreducible closed subsets of $X$.
Step <1>4 shows that neither is contained in the other.

Let $Z\subseteq X$ be irreducible. By step <1>1,
$$
Z
=
(Z\cap L)\cup(Z\cap H),
$$
where both intersections are closed in $Z$. Since $Z$ is irreducible, one of
these intersections must equal $Z$. Thus
$$
Z\subseteq L
\qquad\text{or}\qquad
Z\subseteq H.
$$
Hence every irreducible closed subset of $X$ lies in one of $L$ or $H$, so
the maximal irreducible closed subsets are exactly $L$ and $H$.
:::

<1>6. The variety $X$ is reducible.

::: {.proof}
Step <1>1 writes $X$ as the union of the two proper closed subsets $L$ and
$H$. Therefore $X$ is reducible.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 identifies the two irreducible components, and step <1>6 proves
reducibility.
:::
:::
