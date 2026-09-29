---
schema: qual/card@1
id: P-AGH372FINITEDUAL
kind: problem
title: Dualizing sheaves under a finite morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Dualizing Sheaves
  - Finite Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both assertions with the retained Hartshorne III.7.2 transcription and the trace-compatible definition of a dualizing sheaf. The proof constructs the trace together with f! of the dualizing sheaf and verifies the defining pairing. The canonical-form trace is also described componentwise when the nonsingular schemes are not pure-dimensional.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $f: X \to Y$ be a finite morphism of projective schemes of the same dimension over a field $k$, and let $\omega_Y^\circ$ be a dualizing sheaf for $Y$.

(a) Show that $f^! \omega_Y^\circ$ is a dualizing sheaf for $X$, where $f^!$ is defined as in (Ex. 6.10).

(b) If $X$ and $Y$ are both nonsingular, and $k$ algebraically closed, conclude that there is a natural trace map $t: f_* \omega_X \to \omega_Y$.
:::

::: {.solution}
Put $n=\dim X=\dim Y$ and let $t_Y:H^n(Y,\omega_Y^\circ)\to k$ be the trace belonging to the given [[T-COHSD|dualizing sheaf]].
For a quasi-coherent sheaf $F$ on $X$, write
$$
a_F:H^n(X,F)\xrightarrow{\cong}H^n(Y,f_*F)
$$
for the natural affine-morphism cohomology comparison of [[P-AGH341AFFINEMORPH]].
Let $\varepsilon:f_*f^!\omega_Y^\circ\to\omega_Y^\circ$ be evaluation at $1$, as constructed in [[P-AGH3610FINITEFLATDUAL]].

::: pf

::: {.pf-step #s1}

The coherent sheaf $H=f^!\omega_Y^\circ$ has a trace
$$
t_H=t_Y\circ H^n(\varepsilon)\circ a_H:H^n(X,H)\longrightarrow k.
$$

::: pf-proof

The sheaves $f_*\OO_X$ and $\omega_Y^\circ$ are coherent, so their sheaf Hom is coherent by [[P-AGH363EXTCOHERENT]], in degree zero.
Under the affine equivalence defining $f^!$, it corresponds to a coherent sheaf on $X$.
Indeed, on $Y=\Spec A$, the module $\Hom_A(B,N)$ is finite over $A$ when $B,N$ are finite over the noetherian ring $A$, and its finite $A$-generators also generate it as a $B$-module.
Thus $H$ is coherent.
The displayed composition uses natural maps on cohomology and is a well-defined $k$-linear trace.

:::

:::

::: {.pf-step #s2}

The pair $(H,t_H)$ is a dualizing sheaf for $X$, proving (a).

::: pf-proof

For every coherent sheaf $F$ on $X$, finite pushforward makes $f_*F$ coherent.
The Hom adjunction of [[P-AGH3610FINITEFLATDUAL]], part (b), and duality on $Y$ give natural isomorphisms
$$
\begin{aligned}
\Hom_X(F,H)
&\cong\Hom_Y(f_*F,\omega_Y^\circ)\\
&\cong H^n(Y,f_*F)^\vee
\cong H^n(X,F)^\vee.
\end{aligned}
$$
Here $(-)^\vee$ denotes the $k$-linear dual.
The first map sends $h:F\to H$ to $\varepsilon\circ f_*h$.
Consequently, for $z\in H^n(X,F)$, its resulting functional takes the value
$$
t_Y\bigl(H^n(\varepsilon\circ f_*h)(a_F(z))\bigr)
=t_H\bigl(H^n(h)(z)\bigr),
$$
by naturality of $a_F$ and the definition in step [](#s1){.pf-ref}.
Thus the isomorphism is precisely the pairing required in the definition of a dualizing sheaf, not just an abstract vector-space isomorphism.
This proves (a) without flatness or smoothness assumptions on $f$.

:::

:::

::: {.pf-step #s3}

If $X$ and $Y$ are nonsingular and pure-dimensional of the same dimension over algebraically closed $k$, the trace in (b) is
$$
\boxed{t:f_*\omega_X\xrightarrow{f_*\theta}
f_*f^!\omega_Y\xrightarrow{\varepsilon}\omega_Y,}
$$
where $\theta:\omega_X\xrightarrow{\cong}f^!\omega_Y$ is the trace-compatible dualizing-sheaf isomorphism.

::: pf-proof

The canonical sheaves $\omega_X=\Omega_{X/k}^n$ and $\omega_Y=\Omega_{Y/k}^n$, with their Serre traces, are dualizing [@Har10a, Theorem III.7.12].
For several components of the same dimension, this follows by taking the direct sum of the dualities on those open-and-closed components.
Step [](#s2){.pf-ref}, with $\omega_Y^\circ=\omega_Y$, makes $f^!\omega_Y$ a dualizing sheaf with the trace of step [](#s1){.pf-ref}.
Uniqueness of a dualizing sheaf with its trace [@Har10a, Proposition III.7.2] supplies the unique trace-compatible isomorphism $\theta$.
Evaluation at $1$ is intrinsic to the finite algebra $f_*\OO_X$, so the displayed morphism is natural and involves no choice of local coordinates or bases.
By its construction, $t_Y\circ H^n(t)\circ a_{\omega_X}$ is the canonical trace on $X$.

:::

:::

::: {.pf-step #s4}

The same assertion holds for nonsingular schemes with components of different dimensions, with canonical sheaves understood componentwise.

::: pf-proof

A noetherian nonsingular scheme is a finite disjoint union of nonsingular integral open-and-closed components: its local rings are domains, so distinct irreducible components cannot meet.
Write these components as $X_a$ and $Y_b$, and on a component $Z$ of dimension $d$ use $\omega_Z=\Omega_{Z/k}^d$.
Every $X_a$ maps to a single $Y_b$.
Its closed image has dimension $\dim X_a$, since the morphism onto its image is finite; affinely this is equality of dimensions for an integral ring extension.
Thus $\dim X_a\le\dim Y_b$.

For equal dimensions, step [](#s3){.pf-ref} applied to $X_a\to Y_b$ gives its canonical trace.
For strictly smaller dimension, the image is a proper closed subset of the integral $Y_b$.
Every morphism from the coherent sheaf $f_*\omega_{X_a}$ to the invertible sheaf $\omega_{Y_b}$ is zero: the source has zero generic stalk and its local sections are torsion, whereas the target is torsion-free.
Use this uniquely possible zero map on that component.
Summing these finitely many component maps constructs the natural trace on all of $Y$.
This also covers the statement when nonsingular projective schemes are not assumed equidimensional.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} construct and verify the dualizing sheaf in (a), and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} construct the canonical trace in (b).

:::

:::

:::
