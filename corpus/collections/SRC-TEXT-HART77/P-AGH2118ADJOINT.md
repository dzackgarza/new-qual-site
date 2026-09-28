---
schema: qual/card@1
id: P-AGH2118ADJOINT
kind: problem
title: Inverse image is left adjoint to direct image
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Adjoint Functors
  - Direct Image
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.18 statement and source-order placement after II.1.17.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $f: X \to Y$ be a continuous map of topological spaces.
Show that for any sheaf $\mcf$ on $X$ there is a natural map $\inverseof{f} f_* \mcf \to \mcf$, and for any sheaf $\mcg$ on $Y$ there is a natural map $\mcg \to f_* \inverseof{f} \mcg$.

Use these maps to show that there is a natural bijection of sets, for any sheaves $\mcf$ on $X$ and $\mcg$ on $Y$,
\[
\Hom_X(\inverseof{f} \mcg, \mcf) = \Hom_Y(\mcg, f_* \mcf).
\]
Hence $\inverseof{f}$ is a **left adjoint** of $f_*$, and $f_*$ is a **right adjoint** of $\inverseof{f}$.
:::

::: {.solution}
Recall that for a sheaf $\mathcal G$ on $Y$, the inverse-image sheaf $f^{-1}\mathcal G$ is the sheaf associated to the presheaf
\[
\mathcal P_{\mathcal G}(U)
=
\varinjlim_{f(U)\subseteq V}\mathcal G(V),
\]
where $V$ runs over open neighborhoods of $f(U)$ in $Y$.

<1>1. For every sheaf $\mathcal F$ on $X$ there is a natural morphism
\[
\boxed{
\varepsilon_{\mathcal F}:
f^{-1}f_*\mathcal F\longrightarrow\mathcal F.
}
\]
::: {.proof} Before sheafification, for an open $U\subseteq X$ one has
\[
\mathcal P_{f_*\mathcal F}(U)
=
\varinjlim_{f(U)\subseteq V}
(f_*\mathcal F)(V)
=
\varinjlim_{f(U)\subseteq V}
\mathcal F(f^{-1}V).
\]
For every such $V$,
\[
U\subseteq f^{-1}V,
\]
so restriction gives
\[
\mathcal F(f^{-1}V)\longrightarrow\mathcal F(U).
\]
These restriction maps are compatible as $V$ shrinks, hence induce
\[
\mathcal P_{f_*\mathcal F}(U)
\longrightarrow
\mathcal F(U).
\]
They commute with restriction in $U$, so define a presheaf morphism
\[
\mathcal P_{f_*\mathcal F}\longrightarrow\mathcal F.
\]
Since $\mathcal F$ is already a sheaf, the universal property of sheafification gives a unique sheaf morphism
\[
\varepsilon_{\mathcal F}:
f^{-1}f_*\mathcal F
\longrightarrow\mathcal F.
\]
:::

<1>2. For every sheaf $\mathcal G$ on $Y$ there is a natural morphism
\[
\boxed{
\eta_{\mathcal G}:
\mathcal G\longrightarrow f_*f^{-1}\mathcal G.
}
\]
::: {.proof}
Let $V\subseteq Y$ be open and take
\[
s\in\mathcal G(V).
\]
The open $V$ contains
\[
f(f^{-1}V),
\]
so $s$ represents an element of
\[
\mathcal P_{\mathcal G}(f^{-1}V)
=
\varinjlim_{f(f^{-1}V)\subseteq W}\mathcal G(W).
\]
Passing to the associated sheaf gives a section
\[
\eta_{\mathcal G}(V)(s)
\in
(f^{-1}\mathcal G)(f^{-1}V)
=
(f_*f^{-1}\mathcal G)(V).
\]
These maps commute with restriction in $V$, hence define the desired sheaf morphism.
:::

<1>3. The maps $\varepsilon$ are natural in $\mathcal F$, and the maps $\eta$ are natural in $\mathcal G$.
::: {.proof} Let
\[
\alpha:\mathcal F\to\mathcal F'
\]
be a sheaf morphism on $X$.
In the construction of <1>1, applying $\alpha$ before or after restricting
\[
\mathcal F(f^{-1}V)\to\mathcal F(U)
\]
gives the same result because $\alpha$ commutes with restrictions.
Hence
\[
\varepsilon_{\mathcal F'}\circ f^{-1}f_*\alpha
=
\alpha\circ\varepsilon_{\mathcal F}.
\]

Similarly, for
\[
\beta:\mathcal G\to\mathcal G'
\]
on $Y$, applying $\beta$ to a representative section before or after the construction in <1>2 gives
\[
f_*f^{-1}\beta\circ\eta_{\mathcal G}
=
\eta_{\mathcal G'}\circ\beta.
\]
:::

<1>4. The first triangle identity holds:
\[
\boxed{
\varepsilon_{f^{-1}\mathcal G}
\circ
f^{-1}\eta_{\mathcal G}
=
\operatorname{id}_{f^{-1}\mathcal G}.
}
\]
::: {.proof} A section of $f^{-1}\mathcal G$ is locally represented by a section
\[
s\in\mathcal G(V)
\]
on an open $V\subseteq Y$.
Under
\[
f^{-1}\eta_{\mathcal G},
\]
that local representative is sent to the section of
\[
f^{-1}f_*f^{-1}\mathcal G
\]
represented by the image of $s$ in
\[
(f^{-1}\mathcal G)(f^{-1}V).
\]
The counit $\varepsilon_{f^{-1}\mathcal G}$ then restricts that section back to the open on which the original germ section was represented.
By construction this returns exactly the original local section.

Since the equality holds locally on a cover, the two sheaf morphisms are equal globally.
:::

<1>5. The second triangle identity holds:
\[
\boxed{
f_*\varepsilon_{\mathcal F}
\circ
\eta_{f_*\mathcal F}
=
\operatorname{id}_{f_*\mathcal F}.
}
\]
::: {.proof} Let $V\subseteq Y$ and
\[
s\in(f_*\mathcal F)(V)
=\mathcal F(f^{-1}V).
\]
The unit
\[
\eta_{f_*\mathcal F}
\]
sends $s$ to the section of
\[
f^{-1}f_*\mathcal F
\]
over $f^{-1}V$ represented by $s$ itself on the neighborhood $V$.

The counit $\varepsilon_{\mathcal F}$ is defined by restricting such a representative from
\[
f^{-1}V
\]
to the open under consideration.  Here that open is already $f^{-1}V$, so it returns $s$.  Thus the composite is the identity on every open $V$.
:::

<1>6. Given
\[
\alpha:f^{-1}\mathcal G\longrightarrow\mathcal F,
\]
define
\[
\Phi(\alpha)
:=
\mathcal G
\xrightarrow{\eta_{\mathcal G}}
f_*f^{-1}\mathcal G
\xrightarrow{f_*\alpha}
f_*\mathcal F.
\]
Thus
\[
\Phi:
\operatorname{Hom}_X(f^{-1}\mathcal G,\mathcal F)
\longrightarrow
\operatorname{Hom}_Y(\mathcal G,f_*\mathcal F).
\]
::: {.proof}
Both arrows in the displayed composite are sheaf morphisms on $Y$, so their composite is one.  This defines $\Phi$.
:::

<1>7. Given
\[
\beta:\mathcal G\longrightarrow f_*\mathcal F,
\]
define
\[
\Psi(\beta)
:=
f^{-1}\mathcal G
\xrightarrow{f^{-1}\beta}
f^{-1}f_*\mathcal F
\xrightarrow{\varepsilon_{\mathcal F}}
\mathcal F.
\]
Thus
\[
\Psi:
\operatorname{Hom}_Y(\mathcal G,f_*\mathcal F)
\longrightarrow
\operatorname{Hom}_X(f^{-1}\mathcal G,\mathcal F).
\]
::: {.proof}
Again this is a composite of sheaf morphisms, now on $X$.
:::

<1>8. For every $\alpha:f^{-1}\mathcal G\to\mathcal F$,
\[
\Psi(\Phi(\alpha))=\alpha.
\]
::: {.proof}
Expand the definitions:
\[
\Psi(\Phi(\alpha))
=
\varepsilon_{\mathcal F}
\circ
f^{-1}(f_*\alpha)
\circ
f^{-1}\eta_{\mathcal G}.
\]
By naturality of the counit from <1>3,
\[
\varepsilon_{\mathcal F}
\circ
f^{-1}f_*\alpha
=
\alpha
\circ
\varepsilon_{f^{-1}\mathcal G}.
\]
Hence
\[
\Psi(\Phi(\alpha))
=
\alpha
\circ
\varepsilon_{f^{-1}\mathcal G}
\circ
f^{-1}\eta_{\mathcal G}.
\]
The last two factors compose to the identity by <1>4, so the result is $\alpha$.
:::

<1>9. For every $\beta:\mathcal G\to f_*\mathcal F$,
\[
\Phi(\Psi(\beta))=\beta.
\]
::: {.proof}
Expanding gives
\[
\Phi(\Psi(\beta))
=
f_*\varepsilon_{\mathcal F}
\circ
f_*f^{-1}\beta
\circ
\eta_{\mathcal G}.
\]
By naturality of the unit from <1>3,
\[
f_*f^{-1}\beta
\circ
\eta_{\mathcal G}
=
\eta_{f_*\mathcal F}
\circ
\beta.
\]
Therefore
\[
\Phi(\Psi(\beta))
=
f_*\varepsilon_{\mathcal F}
\circ
\eta_{f_*\mathcal F}
\circ
\beta.
\]
The first two factors compose to the identity by <1>5, leaving $\beta$.
:::

<1>10. Thus there is a natural bijection
\[
\boxed{
\operatorname{Hom}_X(f^{-1}\mathcal G,\mathcal F)
\cong
\operatorname{Hom}_Y(\mathcal G,f_*\mathcal F).
}
\]
Hence
\[
\boxed{f^{-1}\dashv f_*.}
\]
::: {.proof}
Steps <1>8 and <1>9 show that $\Phi$ and $\Psi$ are inverse bijections.  Their formulas are built functorially from $f^{-1}$, $f_*$, the unit, and the counit, so the bijection is natural in both $\mathcal F$ and $\mathcal G$.  This is exactly the definition that $f^{-1}$ is left adjoint to $f_*$.
:::

<1>11. Q.E.D.
::: {.proof}
Steps <1>1--<1>5 construct the natural maps requested, and <1>6--<1>10 prove the adjunction.
:::
:::
