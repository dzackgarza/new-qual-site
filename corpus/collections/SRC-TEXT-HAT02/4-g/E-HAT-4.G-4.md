---
schema: qual/card@1
id: E-HAT-4.G-4
kind: problem
title: Nerve lemma for subcomplex covers of CW complexes
classification:
  areas:
  - topology
  topics:
  - CW Complexes
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: source-checked
  by: claude
  date: 2026-11-08
  note: >-
    Read Hatcher pp.458-460: Proposition 4G.1 (homotopy equivalences on vertex spaces give h.e. of realizations), Proposition 4G.2 for open covers via partition of unity, Corollary 4G.3 (nerve), and the definition of ΔX_U as in the proof. The subcomplex cover's diagram has X_σ=∩_{i∈σ}X_i again a subcomplex, and CW complexes are paracompact [VBKT] as in the printed hint.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    The previous 'homotopy gluing lemma therefore proves by cellular induction' asserted without carrying out induction or stating the lemma. Replaced by explicit skeleta induction: over int e, p^{-1}(int e)=int e×Δ^{\cardinality{J(e)}-1} with J(e)={i|e⊂X_i}, contractible fiber; (X^n,X^{n-1}) and (Y^n,Y^{n-1}) are CW pairs with HEP, and p is a homotopy equivalence on Y^{n-1} by induction and on the attached n-cells by the product structure, so the gluing lemma (Prop. 0.6.2) gives p:Y^n→X^n a homotopy equivalence, hence p:ΔX_U→X. The nerve corollary then follows from Proposition 4G.1 applied to X_σ→*.
---

::: {.problem}
Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by families of subcomplexes.
[CW complexes are paracompact; see [VBKT].]
:::

::: {.solution}
Let $X=\bigcup_{i\in I}X_i$ be a CW complex covered by subcomplexes. For each
nonempty finite $\sigma\subset I$, put $X_\sigma=\bigcap_{i\in\sigma}X_i$.
Every $X_\sigma$ is a subcomplex, and $\{X_\sigma\}$ is the diagram of
finite intersections of the cover. Let $\Delta X_{\mathcal U}$ be its
realization (p.458) and

$$
p:\Delta X_{\mathcal U}\longrightarrow X,\qquad p(x_\sigma,s)=x_\sigma
\;(x_\sigma\in X_\sigma,\;s\in\Delta^{\cardinality{\sigma}-1}),
$$

the map forgetting the simplex coordinate; on the $0$-simplex $\{i\}$ it is the
inclusion $X_i\hookrightarrow X$.

::: pf

::: pf-step

$X$ is paracompact, so Proposition 4G.2 applies to open covers, and the hint
is respected; we now prove the subcomplex case directly.

::: pf-proof

CW complexes are paracompact [VBKT] as noted in the printed hint, but the open-cover
proof of Proposition 4G.2 uses a partition of unity, which is not available for
subcomplexes. We argue instead via CW skeleta and cofibrations.

:::

:::

::: pf-step

Over an open $n$-cell $e\subset X$, $p$ is a product with a contractible simplex.

::: pf-proof

Let $J(e)=\{i\in I\mid e\subset X_i\}$, the finite set of indices of subcomplexes
containing $e$ ($e$ is compact, so $J(e)$ is finite, and $e\subset X_i$ iff
$\operatorname{int}e\subset X_i$ because $X_i$ is a subcomplex). For any
$\sigma$ with $e\subset X_\sigma$ we have $\sigma\subset J(e)$, and conversely
$\sigma\subset J(e)$ implies $e\subset X_\sigma$. Hence the part of
$\Delta X_{\mathcal U}$ lying over $\operatorname{int}e$ is

$$
\bigcup_{\emptyset\neq\sigma\subset J(e)} X_\sigma\cap\operatorname{int}e
\times\operatorname{int}\Delta^{\cardinality{\sigma}-1}
= \operatorname{int}e\times
\bigcup_{\emptyset\neq\sigma\subset J(e)}\operatorname{int}\Delta^{\cardinality{\sigma}-1}
= \operatorname{int}e\times\operatorname{int}\Delta^{\cardinality{J(e)}-1}.
$$

The second factor is the interior of the simplex spanned by $J(e)$, contractible.
Thus $p^{-1}(\operatorname{int}e)=\operatorname{int}e\times\Delta^{\cardinality{J(e)}-1}$
with $p$ the projection, a homotopy equivalence. On the boundary
$\partial e\subset X^{n-1}$, $J(e')\supset J(e)$ for faces $e'$, and the
inclusion of simplex-factors is the face inclusion
$\Delta^{\cardinality{J(e)}-1}\hookrightarrow\Delta^{\cardinality{J(e')}-1}$.

:::

:::

::: pf-step

$p$ is a homotopy equivalence by cellular induction.

::: pf-proof

Write $X^n$ for the $n$-skeleton. Put $Y^n=p^{-1}(X^n)$. Then
$Y^{-1}=\emptyset$, $Y^0=X^0$ (each $0$-cell lies in some $X_i$, $J(e)=$ its indices,
$\Delta^{\cardinality{J(e)}-1}$ is a simplex, but over a $0$-cell $e=\{pt\}$ the fiber is that
simplex, and $p$ collapses it; $X^0$ is discrete, so $p:Y^0\to X^0$ is a homotopy
equivalence). Assume inductively $p:Y^{n-1}\to X^{n-1}$ is a homotopy equivalence.
$X^n$ is obtained from $X^{n-1}$ by attaching $n$-cells $e$ via $\varphi_e:S^{n-1}\to X^{n-1}$.
$Y^n$ is obtained from $Y^{n-1}$ by attaching $\Delta^{\cardinality{J(e)}-1}\times D^n$ along
$\Delta^{\cardinality{J(e)}-1}\times S^{n-1}$ via $p$ on the second factor and the face
inclusions on the first; the attaching maps are the compositions

$$
\Delta^{\cardinality{J(e)}-1}\times S^{n-1}
\xrightarrow{\operatorname{id}\times\varphi_e}
\Delta^{\cardinality{J(e)}-1}\times X^{n-1}
\subset Y^{n-1}
$$

up to the identification of $\Delta^{\cardinality{J(e)}-1}$ with the fiber simplex. Both
pairs $(X^n,X^{n-1})$ and $(Y^n,Y^{n-1})$ are CW pairs, hence have the homotopy
extension property (Proposition 0.16, Appendix). The map of pairs
$p:(Y^n,Y^{n-1})\to (X^n,X^{n-1})$ restricts to a homotopy equivalence on
$Y^{n-1}$ by induction and to $\operatorname{int}e\times\Delta^{\cardinality{J(e)}-1}\to
\operatorname{int}e$, a homotopy equivalence, on the attached cells. The
homotopy gluing lemma for CW pairs (or Proposition 0.6.2, that a map of
adjunction spaces which is a homotopy equivalence on the subspace and on the
attached cells is a homotopy equivalence) therefore gives that
$p:Y^n\to X^n$ is a homotopy equivalence. Taking direct limits over $n$,
$X=\operatorname{colim}X^n$, $\Delta X_{\mathcal U}=\operatorname{colim}Y^n$ with
the weak topology, and a direct limit of homotopy equivalences of CW inclusions
is a homotopy equivalence, so $p:\Delta X_{\mathcal U}\to X$ is a homotopy
equivalence. This is the subcomplex-cover version of Proposition 4G.2 (p.459).

:::

:::

::: pf-step

Nerve corollary.

::: pf-proof

If every nonempty $X_\sigma$ is contractible, choose a point $x_\sigma\in X_\sigma$
and let $c_\sigma:X_\sigma\to\{x_\sigma\}$ be the constant map, a homotopy
equivalence. The family $c_\sigma$ is a map of complexes of spaces from
$\{X_\sigma\}$ to the constant diagram $\{\ast\}_\sigma$ over the same base
$\Gamma=N(\mathcal U)$ (the nerve, whose $n$-simplices are the $\sigma$ with
$\cardinality{\sigma}=n+1$ and $X_\sigma\neq\emptyset$). By Proposition 4G.1 (p.458), a map of
complexes of spaces which is a homotopy equivalence on each vertex space induces a
homotopy equivalence of realizations, so

$$
\Delta X_{\mathcal U}\simeq\Delta\{\ast\}=\realization{N(\mathcal U)}.
$$

Combined with $p:\Delta X_{\mathcal U}\simeq X$, this gives $X\simeq N(\mathcal U)$,
i.e. $X\simeq\realization{N(\mathcal U)}$, which is Corollary 4G.3 for subcomplex covers.

:::

:::

:::

:::
