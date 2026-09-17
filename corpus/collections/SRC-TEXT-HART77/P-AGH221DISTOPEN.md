---
schema: qual/card@1
id: P-AGH221DISTOPEN
kind: problem
title: Distinguished open subsets of an affine scheme are affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Localization
  - Locally Ringed Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.1 statement and source-order placement after II.1.22.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a ring, let $X = \Spec A$, let $f \in A$, and let $D(f) \subseteq X$ be the open complement of $V(f)$.
Show that the locally ringed space $\qty{D(f), \ro{\OO_X}{D(f)}}$ is isomorphic to $\Spec A_f$.
:::

::: {.solution}
Let
\[
\lambda:A\longrightarrow A_f
\]
be the localization map.  It induces a morphism of affine schemes
\[
\lambda^*:\operatorname{Spec}A_f
\longrightarrow
\operatorname{Spec}A,
\qquad
\mathfrak q\longmapsto\lambda^{-1}(\mathfrak q).
\]

<1>1. The image of $\lambda^*$ is exactly
\[
D(f)=\{\mathfrak p\in\operatorname{Spec}A:f\notin\mathfrak p\}.
\]
::: {.proof}
If
\[
\mathfrak q\in\operatorname{Spec}A_f,
\]
then $f/1$ is a unit in $A_f$, so it cannot lie in the prime ideal $\mathfrak q$.  Hence
\[
f\notin\lambda^{-1}(\mathfrak q),
\]
so the image lies in $D(f)$.

Conversely, if
\[
\mathfrak p\in D(f),
\]
then the multiplicative system
\[
\{1,f,f^2,\ldots\}
\]
is disjoint from $\mathfrak p$.  Therefore
\[
\mathfrak pA_f
\]
is a prime ideal of $A_f$, and
\[
\lambda^{-1}(\mathfrak pA_f)=\mathfrak p.
\]
Thus every point of $D(f)$ occurs in the image.
:::

<1>2. Extension and contraction give inverse bijections
\[
\boxed{
\operatorname{Spec}A_f
\xleftrightarrow[\mathfrak p\mapsto\mathfrak pA_f]
{\mathfrak q\mapsto\lambda^{-1}(\mathfrak q)}
D(f).
}
\]
::: {.proof}
The standard prime-correspondence theorem for localization says that prime ideals of $A_f$ are in bijection with prime ideals of $A$ disjoint from the powers of $f$, precisely the primes not containing $f$.  The inverse maps are contraction and extension.
:::

<1>3. The bijection in <1>2 is a homeomorphism.
::: {.proof}
A basis for the topology on $\operatorname{Spec}A_f$ is given by distinguished opens
\[
D_{A_f}(a/1),
\qquad
a\in A.
\]
Every distinguished open defined by a general fraction $a/f^n$ is the same one, because $f/1$ is a unit.

Under contraction, one has
\[
D_{A_f}(a/1)
\longmapsto
D_A(a)\cap D_A(f).
\]
Indeed,
\[
a/1\notin\mathfrak pA_f
\iff
a\notin\mathfrak p
\]
for $\mathfrak p\in D(f)$.

The sets
\[
D_A(a)\cap D_A(f)
\]
form a basis for the subspace topology on $D(f)$.  Hence the bijection sends a basis to a basis and is a homeomorphism.
:::

<1>4. Let
\[
\mathfrak p\in D(f),
\qquad
\mathfrak q=\mathfrak pA_f.
\]
Then the induced map on local rings is an isomorphism
\[
\boxed{
(A_f)_{\mathfrak q}
\xrightarrow{\sim}
A_{\mathfrak p}.
}
\]
::: {.proof}
Because $f\notin\mathfrak p$, the element $f$ is already a unit in the local ring $A_{\mathfrak p}$.  Hence the localization map
\[
A\longrightarrow A_{\mathfrak p}
\]
factors uniquely through
\[
A_f.
\]

The elements of $A_f$ outside $\mathfrak q=\mathfrak pA_f$ are precisely the fractions whose numerators lie outside $\mathfrak p$.  Localizing $A_f$ at those elements therefore inverts exactly the same elements of $A$ as localizing $A$ at $\mathfrak p$.  Thus
\[
(A_f)_{\mathfrak pA_f}
\cong
A_{\mathfrak p}.
\]
:::

<1>5. Under the homeomorphism of <1>3, the structure sheaf on $\operatorname{Spec}A_f$ is naturally isomorphic to the restriction $\mathcal O_X|_{D(f)}$.
::: {.proof}
It is enough to compare the sheaves on the basis
\[
D_A(a)\cap D_A(f)
=D_A(af)
\]
of $D(f)$.

The corresponding basic open in $\operatorname{Spec}A_f$ is
\[
D_{A_f}(a/1).
\]
Its sections are
\[
\mathcal O_{\operatorname{Spec}A_f}
\bigl(D_{A_f}(a/1)\bigr)
=(A_f)_{a/1}.
\]
On the other hand,
\[
\mathcal O_X(D_A(af))
=A_{af}.
\]
There is a canonical localization isomorphism
\[
(A_f)_{a/1}
\cong
A_{af}.
\]
These isomorphisms commute with restriction to smaller distinguished opens because all restriction maps are localization maps.  Hence they glue to an isomorphism of sheaves on the homeomorphic spaces.

Equivalently, the same conclusion follows stalkwise from <1>4, since the stalk of $\mathcal O_X|_{D(f)}$ at $\mathfrak p$ is $A_{\mathfrak p}$.
:::

<1>6. Therefore
\[
\boxed{
\left(D(f),\mathcal O_X|_{D(f)}\right)
\cong
\operatorname{Spec}A_f
}
\]
as locally ringed spaces.
::: {.proof}
Step <1>3 gives the homeomorphism of underlying spaces and <1>5 gives the compatible isomorphism of structure sheaves.  The stalk maps are the local-ring isomorphisms in <1>4, so the resulting ringed-space isomorphism is an isomorphism of locally ringed spaces.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>6 is the assertion of the exercise.
:::
:::
