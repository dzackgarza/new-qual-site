---
schema: qual/card@1
id: P-AGH244PROPIMAGE
kind: problem
title: The image of a proper closed subscheme is proper
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Morphisms
  - Graph Morphism
  - Image Subschemes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.4.4 statement, the graph-factorization hint, and the repository scheme-theoretic-image definition.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $f: X \to Y$ be a morphism of separated schemes of finite type over a noetherian scheme $S$.
Let $Z$ be a closed subscheme of $X$ which is proper over $S$.
Show that $f(Z)$ is closed in $Y$, and that $f(Z)$ with its image subscheme structure is proper over $S$.

*Hint:* factor $f$ into the graph morphism $\Gamma_f: X \to \fiberprod{X}{S}{Y}$ followed by the second projection $p_2$, and show that $\Gamma_f$ is a closed immersion.
:::

::: {.solution}
Let
\[
h=f|_Z:Z\longrightarrow Y.
\]

::: pf

::: pf-step

The graph morphism
\[
\Gamma_h:Z\longrightarrow Z\times_SY,
\qquad
z\longmapsto(z,h(z)),
\]
is a closed immersion.

::: pf-proof

The graph is the base change of the diagonal of $Y/S$.
Indeed, in the Cartesian square
\[
\begin{array}{ccc}
Z&\xrightarrow{\Gamma_h}&Z\times_SY\\
\downarrow{\scriptstyle h}&&\downarrow{\scriptstyle h\times\id_Y}\\
Y&\xrightarrow{\Delta_{Y/S}}&Y\times_SY,
\end{array}
\]
the top map is precisely the pullback of the diagonal.

Because $Y$ is separated over $S$,
\[
\Delta_{Y/S}:Y\longrightarrow Y\times_SY
\]
is a closed immersion.  Closed immersions are stable under base change, hence $\Gamma_h$ is a closed immersion.

:::

:::

::: {.pf-step #s2}

The second projection
\[
p_2:Z\times_SY\longrightarrow Y
\]
is proper.

::: pf-proof

The projection $p_2$ is the base change of the proper structure morphism
\[
Z\longrightarrow S
\]
along the morphism $Y\to S$.
Proper morphisms are stable under base change, so $p_2$ is proper.

:::

:::

::: {.pf-step #s3}

The closed immersion $\Gamma_h$ is proper.

::: pf-proof

A closed immersion is finite: affine-locally it is induced by a quotient ring map.  Hartshorne II.4.1 proves that every finite morphism is proper.  Therefore $\Gamma_h$ is proper.

:::

:::

::: pf-step

The morphism
\[
\boxed{h:Z\longrightarrow Y}
\]
is proper.

::: pf-proof

By construction,
\[
h=p_2\circ\Gamma_h.
\]
Both morphisms on the right are proper by steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.  Proper morphisms are stable under composition, so $h$ is proper.

:::

:::

::: {.pf-step #s5}

The set-theoretic image
\[
\boxed{h(Z)=f(Z)}
\]
is closed in $Y$.

::: pf-proof

A proper morphism is universally closed, hence in particular closed.  Since $Z$ is closed in itself, its image under the closed map $h$ is a closed subset of $Y$.

:::

:::

::: {.pf-step #s6}

Let
\[
i:Y'\hookrightarrow Y
\]
be the scheme-theoretic image of $h$.  Then
\[
|Y'|=h(Z)=f(Z).
\]

::: pf-proof

The morphism $h$ is proper, hence quasi-compact and quasi-separated.  Therefore its scheme-theoretic image is defined by
\[
\mathcal I
=
\ker\bigl(\mathcal O_Y\longrightarrow h_*\mathcal O_Z\bigr).
\]

We show directly that the underlying closed set is the closure of $h(Z)$.  Work on an affine open
\[
V=\Spec A\subseteq Y
\]
and put
\[
W=h^{-1}(V).
\]
Because $h$ is quasi-compact, $W$ is quasi-compact.  On $V$, the ideal of the scheme-theoretic image is
\[
I=\ker\bigl(A\longrightarrow\Gamma(W,\mathcal O_W)\bigr).
\]
Every element of $I$ vanishes at every point of $h(W)$, so
\[
\overline{h(W)}\subseteq V(I).
\]

Conversely, let $\mathfrak p\in V$ lie outside $\overline{h(W)}$.  Choose
\[
a\in A\setminus\mathfrak p
\]
such that
\[
D(a)\cap h(W)=\varnothing.
\]
Then
\[
h^{-1}(D(a))=\varnothing.
\]
Thus the pullback of $a$ to $W$ belongs to every prime ideal at every point of $W$, hence is locally nilpotent.  A finite affine cover of the quasi-compact scheme $W$ supplies one exponent $N$ such that the pullback of $a^N$ is zero globally.  Therefore
\[
a^N\in I.
\]
Since $a\notin\mathfrak p$, also $a^N\notin\mathfrak p$, so
\[
\mathfrak p\notin V(I).
\]
Hence
\[
V(I)=\overline{h(W)}.
\]
These affine equalities glue, proving
\[
|Y'|=\overline{h(Z)}.
\]

Here step [](#s5){.pf-ref} shows that the image is already closed, so
\[
|Y'|=\overline{h(Z)}=h(Z).
\]

:::

:::

::: pf-step

The induced morphism
\[
q:Z\longrightarrow Y'
\]
is surjective on underlying topological spaces.

::: pf-proof

By definition $h=i\circ q$.  Hence
\[
i(q(Z))=h(Z).
\]
The closed immersion $i$ is a homeomorphism of $|Y'|$ onto its image in $Y$.  By step [](#s6){.pf-ref} that image is exactly $h(Z)$.  Therefore
\[
q(Z)=|Y'|.
\]

:::

:::

::: {.pf-step #s8}

The structure morphism
\[
Y'\longrightarrow S
\]
is separated and of finite type.

::: pf-proof

The closed immersion
\[
Y'\hookrightarrow Y
\]
is finite, hence of finite type, and $Y\to S$ is of finite type.  Thus their composite $Y'\to S$ is of finite type.

Likewise a closed subscheme of a separated $S$-scheme is separated over $S$: its diagonal is obtained by composing a closed immersion with the pullback of the closed diagonal of $Y/S$.

:::

:::

::: {.pf-step #s9}

For every base change
\[
S'\longrightarrow S,
\]
the induced map
\[
q_{S'}:Z_{S'}\longrightarrow Y'_{S'}
\]
is surjective.

::: pf-proof

Surjectivity of morphisms of schemes is stable under base change.
Concretely, let $y'\in Y'_{S'}$ map to $y\in Y'$.  Since $q$ is surjective, choose $z\in Z$ over $y$.  The fibre of
\[
Z_{S'}\longrightarrow Y'_{S'}
\]
over $y'$ is the spectrum of a tensor product of nonzero residue fields over $\kappa(y)$, hence is nonempty.  Thus some point of $Z_{S'}$ maps to $y'$.

:::

:::

::: {.pf-step #s10}

The morphism
\[
Y'\longrightarrow S
\]
is universally closed.

::: pf-proof

Let $S'\to S$ be arbitrary and let
\[
C\subseteq Y'_{S'}
\]
be closed.  Its inverse image
\[
q_{S'}^{-1}(C)\subseteq Z_{S'}
\]
is closed.

Since $Z\to S$ is proper, its base change
\[
Z_{S'}\longrightarrow S'
\]
is closed.  Hence the image
\[
\operatorname{im}\bigl(q_{S'}^{-1}(C)\to S'\bigr)
\]
is closed in $S'$.

By surjectivity of $q_{S'}$ from step [](#s9){.pf-ref}, every point of $C$ has a preimage in $q_{S'}^{-1}(C)$.  Therefore
\[
\operatorname{im}(C\to S')
=
\operatorname{im}\bigl(q_{S'}^{-1}(C)\to S'\bigr),
\]
which is closed.  Thus every base change of $Y'\to S$ is a closed map.

:::

:::

::: {.pf-step #s11}

The image subscheme $Y'$ is proper over $S$.

::: pf-proof

By step [](#s8){.pf-ref}, $Y'\to S$ is separated and of finite type.  By step [](#s10){.pf-ref}, it is universally closed.  These are exactly the three defining conditions for properness.

:::

:::

::: {.pf-step #s12}

Therefore
\[
\boxed{
f(Z)\text{ is closed in }Y,
\qquad
f(Z)\text{ with its scheme-theoretic image structure is proper over }S.
}
\]

::: pf-proof

The first assertion is step [](#s5){.pf-ref}.  The second is steps [](#s6){.pf-ref} and [](#s11){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s12){.pf-ref} is the required conclusion.

:::

:::

:::
