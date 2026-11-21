---
schema: qual/card@1
id: P-AGH414NOPROPERCOMPONENT
kind: problem
title: A one-dimensional scheme with no proper irreducible component is affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Curves
  - Riemann-Roch
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise IV.1.4 and its cited reductions III.3.1, III.3.2, III.4.2,
    together with IV.1.3. The normalization step was cross-checked against
    Stacks Project Tags 0BXR and 0C45, and descent of properness along a
    surjective map from a proper scheme against Tag 03GN.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.1.4, printed p. 84,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.1.4, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    the reduction to the integral case, the non-properness of the
    normalization, and the finiteness that carries affineness down. Not checked: Yang's Solutions outside printed pp. 84-85; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.1.4 at printed
    p. 84 beside the entry already there. No step, statement or
    hypothesis of the card changes.
---

::: {.problem}
Show that a separated, one-dimensional scheme of finite type over $k$, none of whose irreducible components is proper over $k$, is affine.

Hint: Combine (Ex.
1.3) with (III, Ex.
3.1, Ex.
3.2, Ex.
4.2).
:::

::: {.solution}

::: pf

::: pf-step

It is enough to prove that every irreducible component of
$X_{\mathrm{red}}$, with its reduced induced structure, is affine.

::: pf-proof

The scheme $X$ is noetherian because it is of finite type over a field.
By
[[P-AGH331REDAFFINE|Exercise III.3.1]],
$X$ is affine if and only if $X_{\mathrm{red}}$ is affine.

The scheme $X_{\mathrm{red}}$ is reduced and noetherian. By
[[P-AGH332COMPONENTAFFINE|Exercise III.3.2]],
it is affine if and only if each of its irreducible components is affine.
Thus it suffices to prove the assertion for one reduced irreducible
component
$$
C\subseteq X_{\mathrm{red}}.
$$

:::

:::

::: {.pf-step #s2}

The component $C$ is an integral, separated, one-dimensional
scheme of finite type over $k$, and it is not proper over $k$.

::: pf-proof

By construction $C$ is reduced and irreducible, hence integral. It is a
closed subscheme of the separated finite-type $k$-scheme $X$, so it is
separated and of finite type over $k$. The hypothesis says precisely
that this irreducible component is not proper.

It remains only to exclude dimension $0$. If $\dim C=0$, then $C$
is the spectrum of its function field, which is a finite extension of
$k$ by Zariski's lemma. Hence
$$
C\longrightarrow\Spec k
$$
is finite and therefore proper, a contradiction. Thus
$$
\dim C=1.
$$

:::

:::

::: {.pf-step #s3}

Let
$$
\nu:\widetilde C\longrightarrow C
$$
be the normalization. Then $\nu$ is finite and surjective, and
$\widetilde C$ is an integral, separated, regular, one-dimensional
scheme of finite type over $k$.

::: pf-proof

Because $C$ is an integral finite-type $k$-scheme, its normalization
is finite and birational. In particular $\nu$ is finite and dominant;
since a finite morphism is closed and its image contains the generic
point of the irreducible scheme $C$, it is surjective.

The normalization $\widetilde C$ is integral and normal. It is finite
over the finite-type $k$-scheme $C$, hence itself of finite type over
$k$; it is separated because it is finite over the separated scheme
$C$. A noetherian normal local domain of dimension $1$ is a discrete
valuation ring. Therefore every local ring of the one-dimensional
normal scheme $\widetilde C$ is regular, so $\widetilde C$ is
regular.

:::

:::

::: {.pf-step #s4}

The normalization $\widetilde C$ is not proper over $k$.

::: pf-proof

Suppose instead that $\widetilde C$ were proper over $k$. The map
$$
\nu:\widetilde C\longrightarrow C
$$
is surjective by step [](#s3){.pf-ref}. A surjective image of a universally closed
$k$-scheme is universally closed over $k$: after arbitrary base
change, the image of a closed subset of $C$ equals the image of its
closed inverse image in $\widetilde C$.

Thus $C\to\Spec k$ would be universally closed. Step [](#s2){.pf-ref} already shows
that $C$ is separated and of finite type over $k$. Hence $C$ would
be proper over $k$, contradicting the hypothesis. Therefore
$\widetilde C$ is not proper.

:::

:::

::: {.pf-step #s5}

The normalization $\widetilde C$ is affine.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $\widetilde C$ is integral, separated, regular,
one-dimensional, of finite type over $k$, and not proper. Therefore
[[P-AGH413NONPROPERISAFFINE|Exercise IV.1.3]]
applies and gives
$$
\widetilde C\ \text{affine}.
$$

:::

:::

::: {.pf-step #s6}

The component $C$ is affine.

::: pf-proof

The normalization map
$$
\nu:\widetilde C\longrightarrow C
$$
is finite and surjective by step [](#s3){.pf-ref}, and $\widetilde C$ is affine by
step [](#s5){.pf-ref}. Chevalley's theorem
[[P-AGH342CHEVALLEY|Exercise III.4.2]]
therefore implies that $C$ is affine.

:::

:::

::: {.pf-step #s7}

The original scheme $X$ is affine.

::: pf-proof

Step [](#s6){.pf-ref} proves that every irreducible component of
$X_{\mathrm{red}}$ is affine. Exercise III.3.2 then gives that
$X_{\mathrm{red}}$ is affine. Finally Exercise III.3.1 gives that
$X$ itself is affine.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required conclusion.

:::

:::

:::

::: {.remark title="Published solution"}
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.1.4, text version `tmp/sources/hartshorne-solutions-egbert.md`, reduces by (III.3.1) to reduced schemes and by (III.3.2) to irreducible components, notes the normalization is not proper since the image of a proper scheme is proper, gets $\tilde X$ affine from IV.1.3, and descends affineness by Chevalley (III.4.2) along the finite surjection $\tilde X\to X$.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.1.4, reduces to the integral case: by (III, 3.3.1) and (III, 3.3.2) one may assume $X$ integral, the normalization $\widetilde X$ is then not proper either, so (4.1.3) makes $\widetilde X$ affine, and $\widetilde X\to X$ is finite by (III, 3.4.2), hence $X$ is affine.
:::
