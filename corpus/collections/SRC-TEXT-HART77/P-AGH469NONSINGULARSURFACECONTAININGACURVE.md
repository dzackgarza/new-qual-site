---
schema: qual/card@1
id: P-AGH469NONSINGULARSURFACECONTAININGACURVE
kind: problem
title: Every space curve lies on a nonsingular surface of degree $m \gg 0$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Linear Systems
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.9 together with II.7.14, II.8.24, Bertini's theorem,
    and the repository's blowup calculations. The retained Egbert and Lomont
    companion material contains no solution of this starred exercise. The
    proof below follows the printed blowup hint and adds the point that is
    needed to descend smoothness: a general hyperplane in the very ample
    blowup embedding contains no exceptional fibre, which is exactly the
    nonvanishing of the first normal derivative of the resulting hypersurface
    along X.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step pass against the book. Printed exercise and hint on p. 355.
    s1: corrected the citation of the blowup theorem from Exercise II.8.5 to
    Theorem II.8.24 printed p. 186, whose (a),(b),(c) give Xtilde
    nonsingular, E = P(I/I^2) and N = O(-1), hence O(-E) restricted to a
    fibre is O(1). s2: Exercise II.7.14 printed pp. 171-172 gives very
    ampleness of O(1) tensor pi^*O(m), with O(-E) = pi^{-1}I.O by II.7.13(a)
    printed p. 164. s3: degree 1 on each fibre, so each fibre is embedded as
    a line. s4: hyperplanes through a line form a P^{N-2}, so the bad set
    has dimension N-1. s5: Bertini for hyperplane sections, II.8.18 printed
    p. 179, stated over any algebraically closed field (the corpus card
    T-BERTINI records that), so no characteristic hypothesis is imported.
    s6: the identity pi_* O(-E) = I_X is now justified from the degree-one
    piece of the Rees algebra (II.7.13), which is what gives H^0(Xtilde,L_m)
    = H^0(P^3,I_X(m)) and hence X in F; this is the step the MSE 4430830
    attempt could not supply. s7 and s8: nonsingularity away from X and
    along X, the latter by df(P) = a(P)dx + b(P)dy from I_{X,P} = (x,y).
    Expanded one inference: a component of Ftilde inside E would contain
    fibres over an open set of X, which s5 excludes.
---

::: {.problem}
\* Let $X$ be an irreducible nonsingular curve in $\PP^3$.
Then for each $m \gg 0$, there is a nonsingular surface $F$ of degree $m$ containing $X$.

Hint: Let $\pi: \tilde{\PP} \to \PP^3$ be the blowing-up of $X$ and let $Y=\pi^{-1}(X)$.
Apply Bertini's theorem to the projective embedding of $\tilde{\PP}$ corresponding to $\mci_Y \tensor \pi^* \OO_{\PP^3}(m)$.
:::

::: {.solution}
Let
$$
\pi:\widetilde{\PP^3}=\Bl_X\PP^3\longrightarrow\PP^3
$$
be the blowup of $X$, and write
$$
E=\pi^{-1}(X)
$$
for its exceptional divisor.

::: pf

::: {.pf-step #s1}

The threefold $\widetilde{\PP^3}$ is nonsingular, and
$$
E\cong\PP_X(\mci_X/\mci_X^2).
$$
For every $P\in X$, the fibre
$$
E_P=\pi^{-1}(P)
$$
is a projective line and
$$
\OO_{\widetilde{\PP^3}}(-E)\restrict_{E_P}\cong\OO_{\PP^1}(1).
$$

::: pf-proof

The center $X$ is nonsingular of codimension $2$ in the nonsingular threefold $\PP^3$.
The blowup theorem for a nonsingular center, Theorem II.8.24 (printed p. 186), gives
$$
\widetilde{\PP^3}\text{ nonsingular},
\qquad
E\cong\PP_X(\mci_X/\mci_X^2),
$$
which is (a) and (b) of that theorem, and in (c) it identifies the normal sheaf $\mathcal N_{E/\widetilde{\PP^3}}=\OO_{\widetilde{\PP^3}}(E)\restrict_E$ with $\OO_{\PP(\mci_X/\mci_X^2)}(-1)$. Hence
$$
\OO_{\widetilde{\PP^3}}(-E)\restrict_E\cong\OO_E(1).
$$
Here $E$ is the subscheme $Y'$ of the theorem: by II.7.13(a) (printed p. 164) the inverse image ideal $\pi^{-1}\mci_X\cdot\OO$ is invertible, and it is $\OO_{\widetilde{\PP^3}}(-E)$, so $E$ is the subscheme that ideal defines.
Since the conormal bundle $\mci_X/\mci_X^2$ has rank $2$, every fibre of $E\to X$ is $\PP^1$, and restriction of the last identity gives the claimed $\OO_{\PP^1}(1)$.

:::

:::

::: {.pf-step #s2}

For every sufficiently large integer $m$, the invertible sheaf
$$
L_m
=
\OO_{\widetilde{\PP^3}}(-E)
\tensor
\pi^*\OO_{\PP^3}(m)
$$
is very ample.

::: pf-proof

By the Rees-algebra construction,
$$
\widetilde{\PP^3}
=
\Proj_{\PP^3}\bigoplus_{q\ge0}\mci_X^q,
$$
and its relative twisting sheaf is
$$
\OO_{\widetilde{\PP^3}}(1)
\cong
\mci_X\OO_{\widetilde{\PP^3}}
\cong
\OO_{\widetilde{\PP^3}}(-E).
$$
The identification $\OO_{\widetilde{\PP^3}}(1)=\OO_{\widetilde{\PP^3}}(-E)$ is Proposition II.7.13(a) with its proof (printed p. 164), where the twisting sheaf of the blowup is computed to be the inverse image ideal $\pi^{-1}\mci_X\cdot\OO$.
Apply Exercise II.7.14 (printed pp. 171--172) to this relative $\Proj$, with the ample sheaf $\OO_{\PP^3}(1)$ on the base and $\mathcal L=\OO_{\PP^3}(1)$.
Its last part says that
$$
\OO_{\widetilde{\PP^3}}(1)
\tensor
\pi^*\OO_{\PP^3}(m)
$$
is very ample on $\widetilde{\PP^3}$ relative to $\Spec k$ for every $m\gg0$, the base being a point, that is, very ample.
This is exactly $L_m$.

:::

:::

::: {.pf-step #s3}

Fix such an $m$ and let
$$
\iota_m:\widetilde{\PP^3}\hookrightarrow\PP^N
$$
be the embedding defined by $L_m$.
Each exceptional fibre $E_P$ is mapped isomorphically to a line in $\PP^N$.

::: pf-proof

On the fibre $E_P$, the pullback
$$
\pi^*\OO_{\PP^3}(m)\restrict_{E_P}
$$
is trivial.
Step [](#s1){.pf-ref} therefore gives
$$
L_m\restrict_{E_P}\cong\OO_{\PP^1}(1).
$$
The restriction of a projective embedding remains a closed immersion.
Its image therefore has degree
$$
\deg L_m\restrict_{E_P}=1,
$$
so it is a line in $\PP^N$.

:::

:::

::: {.pf-step #s4}

The hyperplanes in $\PP^N$ containing at least one exceptional fibre form a proper closed subset of $\dualof{(\PP^N)}$.

::: pf-proof

Consider the incidence variety
$$
\mathcal B
=
\{(P,H)\in X\times\dualof{(\PP^N)}:
\iota_m(E_P)\subseteq H\}.
$$
By step [](#s3){.pf-ref}, $\iota_m(E_P)$ is a line.
Hyperplanes containing a fixed line form a projective subspace of codimension $2$ in $\dualof{(\PP^N)}$.
Consequently
$$
\dim\mathcal B
=
1+(N-2)
=
N-1.
$$
The projection
$$
\mathcal B\longrightarrow\dualof{(\PP^N)}
$$
is proper because $X$ is projective, so its image is closed.
Its dimension is at most $N-1$, strictly smaller than the dimension $N$ of the dual projective space.
Hence the image is proper.

:::

:::

::: {.pf-step #s5}

There is a hyperplane $H\subseteq\PP^N$ such that
$$
\widetilde F
=
\iota_m^{-1}(H)
$$
is nonsingular and $H$ contains no exceptional fibre.

::: pf-proof

By step [](#s1){.pf-ref}, $\widetilde{\PP^3}$ is nonsingular.
Bertini's hyperplane theorem [[T-BERTINI]] says that the hyperplanes whose inverse image under $\iota_m$ is nonsingular form a dense open subset of $\dualof{(\PP^N)}$.

Step [](#s4){.pf-ref} says that the hyperplanes containing an exceptional fibre form a proper closed subset.
The complement of that subset is therefore another nonempty open subset.
Since $\dualof{(\PP^N)}$ is irreducible, the two open sets meet.
Choose $H$ in their intersection.

:::

:::

::: {.pf-step #s6}

The divisor $\widetilde F$ of step [](#s5){.pf-ref} is the strict transform of a degree-$m$ surface
$$
F\subseteq\PP^3
$$
containing $X$.

::: pf-proof

The line bundle of $\widetilde F$ is
$$
L_m
=
\OO_{\widetilde{\PP^3}}(-E)
\tensor
\pi^*\OO_{\PP^3}(m).
$$
For a blowup the degree-one piece of the Rees algebra gives
$$
\pi_*\OO_{\widetilde{\PP^3}}(-E)=\mci_X,
$$
because $\widetilde{\PP^3}=\Proj\bigoplus_{q\ge0}\mci_X^q$ and $\OO(-E)=\OO(1)$ is the sheaf whose pushforward is the degree-one piece $\mci_X$ of that graded algebra (the computation is the one in the proof of II.7.13(a), printed p. 164).
The projection formula therefore identifies
$$
H^0(\widetilde{\PP^3},L_m)
\cong
H^0(\PP^3,\mci_X(m)).
$$
Thus the section cutting out $\widetilde F$ corresponds to a degree-$m$ homogeneous form vanishing on $X$.
Let $F$ be its zero surface in $\PP^3$.
Then
$$
X\subseteq F,
$$
and away from $E$ the blowup is an isomorphism.
Step [](#s5){.pf-ref} says that $\widetilde F$ contains no exceptional fibre. A component of $\widetilde F$ contained in $E$ would be a divisor in $E=\PP(\mci_X/\mci_X^2)$, and such a divisor meets the fibre $E_P$ over every $P$ in a nonempty open subset of $X$, so $\widetilde F$ would contain those fibres. Hence $\widetilde F$ has no component contained in $E$ either.
It is therefore the closure of
$$
\pi^{-1}(F\setminus X).
$$
Hence it is the strict transform of $F$.

:::

:::

::: {.pf-step #s7}

The surface $F$ is nonsingular away from $X$.

::: pf-proof

The morphism
$$
\pi:\widetilde{\PP^3}\setminus E
\xrightarrow{\sim}
\PP^3\setminus X
$$
is an isomorphism.
By step [](#s6){.pf-ref} it identifies
$$
\widetilde F\setminus E
$$
with
$$
F\setminus X.
$$
Step [](#s5){.pf-ref} says that $\widetilde F$ is nonsingular, so the open subset $F\setminus X$ is nonsingular.

:::

:::

::: {.pf-step #s8}

The surface $F$ is nonsingular at every point of $X$.

::: pf-proof

Fix a point $P\in X$.
Because $X$ is a nonsingular codimension-two subvariety of the nonsingular threefold $\PP^3$, choose regular local parameters
$$
x,y,z
$$
at $P$ such that
$$
\mci_{X,P}=(x,y).
$$
Let $f$ be a local equation for $F$.
Since $X\subseteq F$, write
$$
f=ax+by
$$
for some
$$
a,b\in\OO_{\PP^3,P}.
$$

On the blowup of the ideal $(x,y)$, the exceptional fibre over $P$ is the projective line of normal directions $[u:v]$.
The strict transform of $F$ meets this fibre in the zero locus of the linear form
$$
a(P)u+b(P)v.
$$
If
$$
a(P)=b(P)=0,
$$
that linear form vanishes identically, so the whole exceptional fibre $E_P$ is contained in $\widetilde F$.
Step [](#s5){.pf-ref} excludes this.
Therefore
$$
(a(P),b(P))\ne(0,0).
$$

Modulo the maximal ideal at $P$, differentiation of
$$
f=ax+by
$$
gives
$$
df(P)=a(P)\,dx+b(P)\,dy\ne0.
$$
By the Jacobian criterion, the hypersurface $F$ is nonsingular at $P$.
Since $P$ was arbitrary, $F$ is nonsingular along all of $X$.

:::

:::

::: {.pf-step #s9}

For every sufficiently large $m$, there is a nonsingular degree-$m$ surface containing $X$.

::: pf-proof

Step [](#s2){.pf-ref} gives one threshold beyond which $L_m$ is very ample for every $m$.
For each such $m$, steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} construct a degree-$m$ surface $F$ containing $X$.
Steps [](#s7){.pf-ref} and [](#s8){.pf-ref} prove that $F$ is nonsingular both away from and along $X$.
Therefore
$$
\boxed{
\text{for every }m\gg0\text{ there is a nonsingular degree-}m
\text{ surface }F\supseteq X.
}
$$

:::

:::

::: pf-qed

Step [](#s9){.pf-ref} is exactly the required assertion.

:::

:::

:::
