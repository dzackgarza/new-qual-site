---
schema: qual/card@1
id: P-AGH382AFFINEMORPH
kind: problem
title: Cohomology is preserved by an affine morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Higher Direct Images
  - Affine Morphisms
  - Quasicoherent Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise III.8.2, Proposition III.8.1, and the affine vanishing theorem III.3.5 in Hartshorne. The proof checks the higher-direct-image vanishing on affine opens of Y, whose inverse images are noetherian affine schemes because f is affine and X is noetherian, then invokes III.8.1.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $f: X \to Y$ be an affine morphism of schemes (II, Ex.
5.17) with $X$ noetherian, and let $\mcf$ be a quasi-coherent sheaf on $X$.
Show that the hypotheses of (Ex.
8.1) are satisfied, and hence that
\[
H^i(X, \mcf) \cong H^i(Y, f_* \mcf)
\]
for each $i \geq 0$.
:::

::: {.solution}
<1>1. If $V\subseteq Y$ is affine open, then $f^{-1}(V)$ is a noetherian affine scheme and $\mcf|_{f^{-1}(V)}$ is quasi-coherent.

::: {.proof}
Because $f$ is an affine morphism, the inverse image of every affine open subset of $Y$ is affine.
Thus
$$
f^{-1}(V)=\Spec B
$$
for some ring $B$.
It is an open subscheme of the noetherian scheme $X$, hence is noetherian.
Quasi-coherence is local and is preserved by restriction to an open subscheme, so
$$
\mcf|_{f^{-1}(V)}
$$
is quasi-coherent.
:::

<1>2. For every affine open $V\subseteq Y$ and every $i>0$,
$$
H^i\bigl(f^{-1}(V),\mcf|_{f^{-1}(V)}\bigr)=0.
$$

::: {.proof}
By step <1>1, $f^{-1}(V)$ is a noetherian affine scheme and the restricted sheaf is quasi-coherent.
The affine vanishing theorem, Hartshorne III.3.5, therefore gives
$$
H^i\bigl(f^{-1}(V),\mcf|_{f^{-1}(V)}\bigr)=0
$$
for every $i>0$.
:::

<1>3. The higher direct images of $\mcf$ vanish:
$$
\boxed{R^if_*\mcf=0\qquad(i>0)}.
$$

::: {.proof}
Proposition III.8.1 identifies $R^if_*\mcf$ with the sheaf associated to the presheaf
$$
V\longmapsto
H^i\bigl(f^{-1}(V),\mcf|_{f^{-1}(V)}\bigr).
$$
Affine open subsets form a basis for the topology of the scheme $Y$.
By step <1>2 this presheaf is zero on every member of that basis when $i>0$.
Consequently all its stalks vanish, and its associated sheaf is zero.
Thus $R^if_*\mcf=0$ for $i>0$.
:::

<1>4. For every $i\ge0$ there is a natural isomorphism
$$
\boxed{H^i(X,\mcf)\cong H^i(Y,f_*\mcf)}.
$$

::: {.proof}
Step <1>3 verifies exactly the vanishing hypothesis of [[P-AGH381DEGENLERAY|Exercise III.8.1]].
Applying that exercise gives the natural isomorphisms
$$
H^i(X,\mcf)\cong H^i(Y,f_*\mcf)
$$
in every degree $i\ge0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 verifies the required higher-direct-image hypothesis, and step <1>4 gives the requested cohomology isomorphisms.
:::
:::
