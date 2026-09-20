---
schema: qual/card@1
id: P-AGXVARQUASIFINDIM
kind: problem
title: Quasi-finite morphisms do not raise dimension
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasi-finite Morphisms
  - Dimension
  - Fibers
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the finite-morphism clause of Zaidenberg Exercises 4.4 in the recorded
    source. The source proves finite morphisms are quasi-finite and then asks
    to deduce dim X <= dim Y; the dimension argument uses only
    quasi-finiteness.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Restored the surrounding source context that X and Y are affine varieties.
    The card retains the valid stronger formulation with quasi-finite as the
    hypothesis.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Factored through the closure Z of the image, used the completed
    fibre-dimension theorem on the dominant quasi-finite map X -> Z, and then
    used dim Z <= dim Y for a closed subvariety.
---

::: {.problem}
Let
$$
f:X\longrightarrow Y
$$
be a quasi-finite morphism of affine varieties over the algebraically closed
ground field $k$. Show that
$$
\dim X\leq\dim Y.
$$
:::

::: {.solution}
Let
$$
Z=\overline{f(X)}\subseteq Y
$$
with its reduced induced structure.

<1>1. The closed subset $Z$ is an affine variety, and the induced morphism
$$
g:X\longrightarrow Z
$$
is dominant and quasi-finite.

::: {.proof}
The variety $X$ is irreducible, so its continuous image $f(X)$ is
irreducible. The closure of an irreducible subset is irreducible, hence $Z$
is irreducible. Since $Z$ is closed in the affine variety $Y$, it is affine.
Thus $Z$ is an affine variety.

By definition of $Z$, the factor map
$$
g:X\longrightarrow Z
$$
has dense image and is therefore dominant.

For every point $z\in Z$, its fibre under $g$ is the same set as its fibre
under $f$. Since $f$ is quasi-finite, that fibre is finite. Hence $g$ is
quasi-finite.
:::

<1>2. One has
$$
\dim X\leq\dim Z.
$$

::: {.proof}
Choose any point
$$
z\in g(X).
$$
The fibre
$$
g^{-1}(z)
$$
is nonempty and finite. Hence every irreducible component of this fibre is a
point and has dimension $0$.

Apply
[[P-AGXVARFIBERDIM|the fibre-dimension theorem]]
to the dominant morphism
$$
g:X\longrightarrow Z.
$$
Every irreducible component of every nonempty fibre has dimension at least
$$
\dim X-\dim Z.
$$
For the chosen fibre this gives
$$
0
\geq
\dim X-\dim Z.
$$
Therefore
$$
\dim X\leq\dim Z.
$$
:::

<1>3. Since $Z\subseteq Y$ is closed,
$$
\dim Z\leq\dim Y.
$$

::: {.proof}
Every chain of irreducible closed subsets of $Z$ is also a chain of
irreducible closed subsets of $Y$. Therefore the supremum of chain lengths
defining $\dim Z$ cannot exceed the corresponding supremum defining
$\dim Y$.
:::

<1>4. Therefore
$$
\boxed{\dim X\leq\dim Y.}
$$

::: {.proof}
Combine step <1>2 and step <1>3:
$$
\dim X
\leq
\dim Z
\leq
\dim Y.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove that a quasi-finite morphism of affine varieties
cannot raise dimension.
:::
:::
