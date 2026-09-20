---
schema: qual/card@1
id: P-AGXVARFINCLOSED
kind: problem
title: Equidimensional finite morphisms are closed and surjective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Finite Morphisms
  - Dimension
  - Properness
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Definitions 4.3 and Exercises 4.4 in the recorded Zaidenberg source.
    The source prints "embedding" in its definition of finite morphism, but the
    same exercise immediately asks for a non-surjective finite morphism; those
    two clauses are incompatible. The proof below therefore uses the
    repository's standard definition D-MORFIN: the comorphism is module-finite,
    without injectivity assumed.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked closedness by integrality and lying over after quotienting a closed
    subset, then checked that equal dimensions force the comorphism kernel to
    vanish by the affine height-dimension formula. Injectivity then makes the
    closed image dense, hence all of the irreducible target.
---

::: {.problem}
Show that if $f:X\to Y$ is finite and $\dim X = \dim Y$, then $f$ is closed and surjective.
:::

::: {.solution}
Write
$$
A=\mco(Y),
\qquad
B=\mco(X),
$$
and let
$$
\varphi=f^*:A\longrightarrow B
$$
be the comorphism. We use the standard definition
[[D-MORFIN|of a finite morphism]], so $B$ is a finite $A$-module and
$\varphi$ is not assumed injective.

<1>1. Every finite morphism of affine varieties is closed.

::: {.proof}
Let
$$
Z=V(J)\subseteq X
$$
be closed. Since $B$ is finite over $A$, it is integral over $\varphi(A)$.
Passing to quotients, $B/J$ is integral over the image of
$$
A/\varphi^{-1}(J)\longrightarrow B/J.
$$
After replacing the source ring by its image, this is an injective integral
extension. By lying over, every maximal ideal of $A$ containing
$\varphi^{-1}(J)$ is the contraction of a maximal ideal of $B$ containing
$J$. Hence
$$
f(Z)=V\bigl(\varphi^{-1}(J)\bigr),
$$
which is closed in $Y$.

Thus $f$ is a closed map. This is the affine argument recorded in
[[P-AGH235QUASIFINITE|the standard finite-morphism closedness proof]].
:::

<1>2. If
$$
I=\ker\varphi,
$$
then
$$
\dim B=\dim(A/I).
$$

::: {.proof}
The ring $B$ is finite over $A$, hence integral over the image
$$
A/I\hookrightarrow B.
$$
Integral extensions preserve Krull dimension: lying over and going up lift
prime chains from $A/I$ to $B$, while incomparability prevents a strict prime
chain in $B$ from contracting with repetitions. Therefore
$$
\dim B=\dim(A/I).
$$
:::

<1>3. Under the hypothesis
$$
\dim X=\dim Y,
$$
the comorphism $\varphi:A\to B$ is injective.

::: {.proof}
The varieties $X$ and $Y$ are irreducible, so $A$ and $B$ are finitely
generated integral algebras over the ground field. In particular,
$$
I=\ker\varphi
$$
is a prime ideal of the domain $A$.

Suppose $I\ne0$. Then
$$
\height I\geq1.
$$
The affine dimension formula
[[P-AGH2320DIMENSION|gives]]
$$
\dim(A/I)+\height I=\dim A,
$$
so
$$
\dim(A/I)<\dim A.
$$
By step <1>2,
$$
\dim B=\dim(A/I)<\dim A.
$$
Equivalently,
$$
\dim X<\dim Y,
$$
contrary to the hypothesis. Hence
$$
I=0,
$$
and $\varphi$ is injective.
:::

<1>4. The morphism $f$ is surjective.

::: {.proof}
By step <1>3, the comorphism is injective, so $f$ is dominant. Thus
$$
\overline{f(X)}=Y.
$$
By step <1>1, the image $f(X)$ is closed. Hence
$$
f(X)=\overline{f(X)}=Y,
$$
so $f$ is surjective.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves closedness for every finite morphism, and steps <1>2--<1>4
show that the equal-dimension hypothesis forces surjectivity.
:::
:::
