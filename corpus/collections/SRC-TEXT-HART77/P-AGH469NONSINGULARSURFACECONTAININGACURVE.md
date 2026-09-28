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

<1>1. The threefold $\widetilde{\PP^3}$ is nonsingular, and
$$
E\cong\PP_X(\mci_X/\mci_X^2).
$$
For every $P\in X$, the fibre
$$
E_P=\pi^{-1}(P)
$$
is a projective line and
$$
\OO_{\widetilde{\PP^3}}(-E)|_{E_P}\cong\OO_{\PP^1}(1).
$$

::: {.proof}
The center $X$ is nonsingular of codimension $2$ in the nonsingular threefold $\PP^3$.
The blowup theorem for a nonsingular center, used in [[P-AGH285BLOWUPCANON|Exercise II.8.5]], gives
$$
\widetilde{\PP^3}\text{ nonsingular},
\qquad
E\cong\PP_X(\mci_X/\mci_X^2),
$$
and
$$
\OO_{\widetilde{\PP^3}}(-E)|_E\cong\OO_E(1).
$$
Since the conormal bundle $\mci_X/\mci_X^2$ has rank $2$, every fibre of $E\to X$ is $\PP^1$, and restriction of the last identity gives the claimed $\OO_{\PP^1}(1)$.
:::

<1>2. For every sufficiently large integer $m$, the invertible sheaf
$$
L_m
=
\OO_{\widetilde{\PP^3}}(-E)
\tensor
\pi^*\OO_{\PP^3}(m)
$$
is very ample.

::: {.proof}
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
Apply [[P-AGH2714PROJVERYAMPLE|Exercise II.7.14(b)]] to this relative $\Proj$, with the ample sheaf $\OO_{\PP^3}(1)$ on the base.
It says that
$$
\OO_{\widetilde{\PP^3}}(1)
\tensor
\pi^*\OO_{\PP^3}(m)
$$
is very ample for every $m\gg0$.
This is exactly $L_m$.
:::

<1>3. Fix such an $m$ and let
$$
\iota_m:\widetilde{\PP^3}\hookrightarrow\PP^N
$$
be the embedding defined by $L_m$.
Each exceptional fibre $E_P$ is mapped isomorphically to a line in $\PP^N$.

::: {.proof}
On the fibre $E_P$, the pullback
$$
\pi^*\OO_{\PP^3}(m)|_{E_P}
$$
is trivial.
Step <1>1 therefore gives
$$
L_m|_{E_P}\cong\OO_{\PP^1}(1).
$$
The restriction of a projective embedding remains a closed immersion.
Its image therefore has degree
$$
\deg L_m|_{E_P}=1,
$$
so it is a line in $\PP^N$.
:::

<1>4. The hyperplanes in $\PP^N$ containing at least one exceptional fibre form a proper closed subset of $\dualof{(\PP^N)}$.

::: {.proof}
Consider the incidence variety
$$
\mathcal B
=
\{(P,H)\in X\dualof{\times(\PP^N)}:
\iota_m(E_P)\subseteq H\}.
$$
By step <1>3, $\iota_m(E_P)$ is a line.
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
\mathcal B\dualof{\longrightarrow(\PP^N)}
$$
is proper because $X$ is projective, so its image is closed.
Its dimension is at most $N-1$, strictly smaller than the dimension $N$ of the dual projective space.
Hence the image is proper.
:::

<1>5. There is a hyperplane $H\subseteq\PP^N$ such that
$$
\widetilde F
=
\iota_m^{-1}(H)
$$
is nonsingular and $H$ contains no exceptional fibre.

::: {.proof}
By step <1>1, $\widetilde{\PP^3}$ is nonsingular.
Bertini's hyperplane theorem [[T-BERTINI]] says that the hyperplanes whose inverse image under $\iota_m$ is nonsingular form a dense open subset of $\dualof{(\PP^N)}$.

Step <1>4 says that the hyperplanes containing an exceptional fibre form a proper closed subset.
The complement of that subset is therefore another nonempty open subset.
Since $\dualof{(\PP^N)}$ is irreducible, the two open sets meet.
Choose $H$ in their intersection.
:::

<1>6. The divisor $\widetilde F$ of step <1>5 is the strict transform of a degree-$m$ surface
$$
F\subseteq\PP^3
$$
containing $X$.

::: {.proof}
The line bundle of $\widetilde F$ is
$$
L_m
=
\OO_{\widetilde{\PP^3}}(-E)
\tensor
\pi^*\OO_{\PP^3}(m).
$$
For a blowup, one has
$$
\pi_*\OO_{\widetilde{\PP^3}}(-E)=\mci_X.
$$
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
Step <1>5 says that $\widetilde F$ contains no exceptional fibre, so in particular it has no component contained in $E$.
It is therefore the closure of
$$
\pi^{-1}(F\setminus X).
$$
Hence it is the strict transform of $F$.
:::

<1>7. The surface $F$ is nonsingular away from $X$.

::: {.proof}
The morphism
$$
\pi:\widetilde{\PP^3}\setminus E
\xrightarrow{\sim}
\PP^3\setminus X
$$
is an isomorphism.
By step <1>6 it identifies
$$
\widetilde F\setminus E
$$
with
$$
F\setminus X.
$$
Step <1>5 says that $\widetilde F$ is nonsingular, so the open subset $F\setminus X$ is nonsingular.
:::

<1>8. The surface $F$ is nonsingular at every point of $X$.

::: {.proof}
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
Step <1>5 excludes this.
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

<1>9. For every sufficiently large $m$, there is a nonsingular degree-$m$ surface containing $X$.

::: {.proof}
Step <1>2 gives one threshold beyond which $L_m$ is very ample for every $m$.
For each such $m$, steps <1>3--<1>6 construct a degree-$m$ surface $F$ containing $X$.
Steps <1>7--<1>8 prove that $F$ is nonsingular both away from and along $X$.
Therefore
$$
\boxed{
\text{for every }m\gg0\text{ there is a nonsingular degree-}m
\text{ surface }F\supseteq X.
}
$$
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is exactly the required assertion.
:::
:::
