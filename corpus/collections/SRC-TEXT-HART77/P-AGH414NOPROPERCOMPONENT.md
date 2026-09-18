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
<1>1. It is enough to prove that every irreducible component of
\(X_{\mathrm{red}}\), with its reduced induced structure, is affine.

::: {.proof}
The scheme \(X\) is noetherian because it is of finite type over a field.
By
[[P-AGH331REDAFFINE|Exercise III.3.1]],
\(X\) is affine if and only if \(X_{\mathrm{red}}\) is affine.

The scheme \(X_{\mathrm{red}}\) is reduced and noetherian. By
[[P-AGH332COMPONENTAFFINE|Exercise III.3.2]],
it is affine if and only if each of its irreducible components is affine.
Thus it suffices to prove the assertion for one reduced irreducible
component
$$
C\subseteq X_{\mathrm{red}}.
$$
:::

<1>2. The component \(C\) is an integral, separated, one-dimensional
scheme of finite type over \(k\), and it is not proper over \(k\).

::: {.proof}
By construction \(C\) is reduced and irreducible, hence integral. It is a
closed subscheme of the separated finite-type \(k\)-scheme \(X\), so it is
separated and of finite type over \(k\). The hypothesis says precisely
that this irreducible component is not proper.

It remains only to exclude dimension \(0\). If \(\dim C=0\), then \(C\)
is the spectrum of its function field, which is a finite extension of
\(k\) by Zariski's lemma. Hence
$$
C\longrightarrow\Spec k
$$
is finite and therefore proper, a contradiction. Thus
$$
\dim C=1.
$$
:::

<1>3. Let
$$
\nu:\widetilde C\longrightarrow C
$$
be the normalization. Then \(\nu\) is finite and surjective, and
\(\widetilde C\) is an integral, separated, regular, one-dimensional
scheme of finite type over \(k\).

::: {.proof}
Because \(C\) is an integral finite-type \(k\)-scheme, its normalization
is finite and birational. In particular \(\nu\) is finite and dominant;
since a finite morphism is closed and its image contains the generic
point of the irreducible scheme \(C\), it is surjective.

The normalization \(\widetilde C\) is integral and normal. It is finite
over the finite-type \(k\)-scheme \(C\), hence itself of finite type over
\(k\); it is separated because it is finite over the separated scheme
\(C\). A noetherian normal local domain of dimension \(1\) is a discrete
valuation ring. Therefore every local ring of the one-dimensional
normal scheme \(\widetilde C\) is regular, so \(\widetilde C\) is
regular.
:::

<1>4. The normalization \(\widetilde C\) is not proper over \(k\).

::: {.proof}
Suppose instead that \(\widetilde C\) were proper over \(k\). The map
$$
\nu:\widetilde C\longrightarrow C
$$
is surjective by step <1>3. A surjective image of a universally closed
\(k\)-scheme is universally closed over \(k\): after arbitrary base
change, the image of a closed subset of \(C\) equals the image of its
closed inverse image in \(\widetilde C\).

Thus \(C\to\Spec k\) would be universally closed. Step <1>2 already shows
that \(C\) is separated and of finite type over \(k\). Hence \(C\) would
be proper over \(k\), contradicting the hypothesis. Therefore
\(\widetilde C\) is not proper.
:::

<1>5. The normalization \(\widetilde C\) is affine.

::: {.proof}
By steps <1>3 and <1>4, \(\widetilde C\) is integral, separated, regular,
one-dimensional, of finite type over \(k\), and not proper. Therefore
[[P-AGH413NONPROPERISAFFINE|Exercise IV.1.3]]
applies and gives
$$
\widetilde C\ \text{affine}.
$$
:::

<1>6. The component \(C\) is affine.

::: {.proof}
The normalization map
$$
\nu:\widetilde C\longrightarrow C
$$
is finite and surjective by step <1>3, and \(\widetilde C\) is affine by
step <1>5. Chevalley's theorem
[[P-AGH342CHEVALLEY|Exercise III.4.2]]
therefore implies that \(C\) is affine.
:::

<1>7. The original scheme \(X\) is affine.

::: {.proof}
Step <1>6 proves that every irreducible component of
\(X_{\mathrm{red}}\) is affine. Exercise III.3.2 then gives that
\(X_{\mathrm{red}}\) is affine. Finally Exercise III.3.1 gives that
\(X\) itself is affine.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
