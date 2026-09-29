---
schema: qual/card@1
id: P-AGXVARPROJCLOSURE
kind: problem
title: The projective closure as the variety together with its boundary at infinity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Closure
  - Hyperplane at Infinity
  - Homogenization
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the corresponding clause of Zaidenberg Exercises 9.2 in the recorded
    source. For an affine variety X in A^n and its projective closure Xbar in
    P^n, it asks to prove Xbar = X union partial X, where partial X is the
    intersection with the hyperplane at infinity x_0=0.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the standard embedding A^n -> P^n, the affine chart U_0, and the
    hyperplane at infinity explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked that the projective closure intersects the standard affine chart
    in exactly X because X is already closed in that chart, then decomposed
    P^n as the disjoint union of the affine chart and the hyperplane at
    infinity.
---

::: {.problem}
Let
$$
X\subseteq\AA^n_k
$$
be an affine variety, embedded in projective space by
$$
\AA^n_k\hookrightarrow\PP^n_k,
\qquad
(a_1,\ldots,a_n)
\longmapsto
[1:a_1:\ldots:a_n].
$$
Let $\overline X\subseteq\PP^n_k$ be its projective Zariski closure, and let
$$
H_0=\{x_0=0\}
$$
be the hyperplane at infinity. Show that
$$
\overline X=X\union\bd X,
\qquad
\bd X=H_0\intersect\overline X.
$$
:::

::: {.solution}
Put
$$
U_0=\{x_0\ne0\}\subseteq\PP^n_k.
$$
Under the standard embedding, $U_0\cong\AA^n_k$ and $X$ is identified with
a closed subset of $U_0$.

::: pf

::: {.pf-step #closure-intersect-u0}
The projective closure satisfies
$$
\boxed{\overline X\intersect U_0=X.}
$$

::: pf-proof
Let
$$
j:U_0\hookrightarrow\PP^n_k
$$
be the open immersion. For any subset $S$ of a topological space and any
open subset $U$, closure restricts by
$$
\overline S^{\,T}\intersect U
=
\overline{S\intersect U}^{\,U}.
$$
Applying this with
$$
T=\PP^n_k,
\qquad
S=X,
\qquad
U=U_0
$$
gives
$$
\overline X\intersect U_0
=
\overline X^{\,U_0}.
$$

But $X$ is an affine variety in
$$
U_0\cong\AA^n_k,
$$
so $X$ is Zariski closed in $U_0$. Therefore its closure inside $U_0$ is
itself:
$$
\overline X^{\,U_0}=X.
$$
Hence
$$
\overline X\intersect U_0=X.
$$
:::

:::

::: {.pf-step #complement-u0-is-h0}
The complement of $U_0$ in $\PP^n_k$ is exactly the hyperplane at
infinity:
$$
\PP^n_k\sm U_0=H_0.
$$

::: pf-proof
By definition,
$$
U_0=\{[x_0:\ldots:x_n]:x_0\ne0\}.
$$
Its complement is therefore
$$
\{[x_0:\ldots:x_n]:x_0=0\}
=
H_0.
$$
:::

:::

::: {.pf-step #closure-decomposition}
The projective closure decomposes as
$$
\boxed{
\overline X
=
X\union(H_0\intersect\overline X).
}
$$

::: pf-proof
By step [](#complement-u0-is-h0){.pf-ref},
$$
\PP^n_k
=
U_0\union H_0.
$$
Intersecting with $\overline X$ gives
$$
\overline X
=
(\overline X\intersect U_0)
\union
(\overline X\intersect H_0).
$$
Step [](#closure-intersect-u0){.pf-ref} identifies the first term with $X$. Therefore
$$
\overline X
=
X\union(H_0\intersect\overline X).
$$
:::

:::

::: {.pf-step #boundary-formula}
With
$$
\bd X
\coloneqq
H_0\intersect\overline X,
$$
one has
$$
\boxed{\overline X=X\union\bd X.}
$$

::: pf-proof
This is the identity in step [](#closure-decomposition){.pf-ref} with $\bd X$ written for the boundary at
infinity.
:::

:::

::: pf-qed
Step [](#closure-intersect-u0){.pf-ref} identifies the affine part of the projective closure with $X$, and
steps [](#complement-u0-is-h0){.pf-ref}, [](#closure-decomposition){.pf-ref} and [](#boundary-formula){.pf-ref} identify the remaining part with the boundary at infinity.
:::

:::

:::
