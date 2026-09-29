---
schema: qual/card@1
id: P-AGXGATHIDEALQUOT
kind: problem
title: Ideal quotients compute closures of differences of subvarieties
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ideal Quotients
  - Zariski Closure
  - Radical Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Gathmann 2.23 card and collection context together with
    the retained Problem Set 2 native source and migration record. The source
    contains only a question mark in its solution slot, so there is no source
    argument to integrate. Cross-checked the radical-ideal step against the
    strong Nullstellensatz in T-JRTS2.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read both inclusions in part (a), including the separating function at
    a point outside Y_2, and checked that vanishing on a subset is equivalent
    to vanishing on its closure. For part (b), checked the quotient-ring form
    of the strong Nullstellensatz and the passage from equality of vanishing
    ideals back to equality of closed subsets.
---

::: {.problem}
For two ideals $J_1, J_2\normal R$, the *ideal quotient* is
\[
J_1 : J_2 \da \ts{f\in R \st fJ_2 \subset J_1}
.\]

Let $X$ be an affine variety.

a. Show that if $Y_1, Y_2 \subset X$ are subvarieties then
\[
I(\bar{Y_1\sm Y_2}) = I(Y_1): I(Y_2)
.\]

b. If $J_1, J_2 \normal A(X)$ are radical, then
\[
\bar{V(J_1) \sm V(J_2)} = V(J_1: J_2)
.\]
:::

::: {.solution}
Put
$$
R=A(X).
$$

::: pf

::: {.pf-step #closure-invariant-vanishing-ideal}
For every subset $S\subseteq X$,
$$
\boxed{I(\overline S)=I(S).}
$$

::: pf-proof
The inclusion
$$
I(\overline S)\subseteq I(S)
$$
is immediate from
$$
S\subseteq\overline S.
$$

Conversely, let $f\in I(S)$. Then
$$
S\subseteq V(f).
$$
The set $V(f)$ is Zariski closed, so it contains the closure of $S$:
$$
\overline S\subseteq V(f).
$$
Thus $f$ vanishes on $\overline S$, hence
$$
f\in I(\overline S).
$$

For part (a), write
$$
I_i=I(Y_i)\subseteq R
\qquad(i=1,2).
$$
:::

:::

::: {.pf-step #forward-inclusion-quotient}
One has
$$
I(Y_1\sm Y_2)\subseteq I_1:I_2.
$$

::: pf-proof
Let
$$
f\in I(Y_1\sm Y_2)
$$
and
$$
g\in I_2.
$$
For a point $p\in Y_1$, there are two cases.

If $p\in Y_2$, then
$$
g(p)=0.
$$
If $p\notin Y_2$, then
$$
f(p)=0.
$$
Hence in either case
$$
(fg)(p)=0.
$$
Thus $fg$ vanishes on all of $Y_1$, so
$$
fg\in I_1.
$$
Since this holds for every $g\in I_2$,
$$
fI_2\subseteq I_1,
$$
which is exactly
$$
f\in I_1:I_2.
$$
:::

:::

::: {.pf-step #reverse-inclusion-quotient}
One has
$$
I_1:I_2\subseteq I(Y_1\sm Y_2).
$$

::: pf-proof
Let
$$
f\in I_1:I_2
$$
and choose
$$
p\in Y_1\sm Y_2.
$$
Because $Y_2$ is a closed subvariety of the affine variety $X$, it is the
common zero locus of functions in $R$. Since
$$
p\notin Y_2,
$$
there exists
$$
g\in I(Y_2)=I_2
$$
such that
$$
g(p)\ne0.
$$

The assumption
$$
f\in I_1:I_2
$$
gives
$$
fg\in I_1.
$$
Since $p\in Y_1$,
$$
0=(fg)(p)=f(p)g(p).
$$
Because $g(p)\ne0$, it follows that
$$
f(p)=0.
$$
This holds for every $p\in Y_1\sm Y_2$, so
$$
f\in I(Y_1\sm Y_2).
$$
:::

:::

::: {.pf-step #ideal-quotient-formula-part-a}
Part (a):
$$
\boxed{
I(\overline{Y_1\sm Y_2})
=
I(Y_1):I(Y_2).
}
$$

::: pf-proof
By step [](#closure-invariant-vanishing-ideal){.pf-ref},
$$
I(\overline{Y_1\sm Y_2})
=
I(Y_1\sm Y_2).
$$
Steps [](#forward-inclusion-quotient){.pf-ref} and [](#reverse-inclusion-quotient){.pf-ref} give
$$
I(Y_1\sm Y_2)
=
I_1:I_2.
$$
Substituting
$$
I_i=I(Y_i)
$$
gives the displayed identity.
:::

:::

::: {.pf-step #radical-ideal-equals-vanishing-ideal}
If $J\subseteq R$ is radical, then
$$
\boxed{I(V(J))=J.}
$$

::: pf-proof
Choose an affine embedding
$$
X\subseteq\AA^n
$$
and write
$$
R=k[x_1,\ldots,x_n]/K.
$$
Let
$$
\pi:k[x_1,\ldots,x_n]\twoheadrightarrow R
$$
be the quotient map and put
$$
\widetilde J=\pi^{-1}(J).
$$
Since $J$ is radical, $\widetilde J$ is radical.

The zero set $V_X(J)$ is the same subset as
$$
V_{\AA^n}(\widetilde J).
$$
By the strong Nullstellensatz [[T-JRTS2]],
$$
I_{\AA^n}(V_{\AA^n}(\widetilde J))
=
\sqrt{\widetilde J}
=
\widetilde J.
$$
Passing to the quotient by $K$ gives
$$
I_X(V_X(J))=J.
$$
:::

:::

::: {.pf-step #closure-formula-part-b}
Part (b):
$$
\boxed{
\overline{V(J_1)\sm V(J_2)}
=
V(J_1:J_2).
}
$$

::: pf-proof
Set
$$
Y_i=V(J_i).
$$
The proof of part (a) uses only that $Y_1$ and $Y_2$ are closed subsets of
$X$, so step [](#ideal-quotient-formula-part-a){.pf-ref} applies to these zero loci even if they are reducible.
By step [](#radical-ideal-equals-vanishing-ideal){.pf-ref} and the radicality of $J_1,J_2$,
$$
I(Y_i)=I(V(J_i))=J_i.
$$
Therefore step [](#ideal-quotient-formula-part-a){.pf-ref} gives
$$
I\!\left(\overline{V(J_1)\sm V(J_2)}\right)
=
J_1:J_2.
$$

The set
$$
Z=\overline{V(J_1)\sm V(J_2)}
$$
is closed in the affine variety $X$. For every closed subset of an affine
variety, the Nullstellensatz gives
$$
V(I(Z))=Z.
$$
Hence
$$
\overline{V(J_1)\sm V(J_2)}
=
V\!\left(
I\!\left(\overline{V(J_1)\sm V(J_2)}\right)
\right)
=
V(J_1:J_2).
$$
:::

:::

::: pf-qed
Steps [](#closure-invariant-vanishing-ideal){.pf-ref}, [](#forward-inclusion-quotient){.pf-ref}, [](#reverse-inclusion-quotient){.pf-ref} and [](#ideal-quotient-formula-part-a){.pf-ref} prove part (a). Steps [](#radical-ideal-equals-vanishing-ideal){.pf-ref} and [](#closure-formula-part-b){.pf-ref} apply the strong
Nullstellensatz to radical ideals in $A(X)$ and prove part (b).
:::

:::
:::
