---
schema: qual/card@1
id: PR-MIRACLEFLAT
kind: proposition
title: Miracle flatness for finite morphisms
slogan: 'Finite plus Cohen--Macaulay source, smooth target, and equal dimension forces flatness.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Finite Morphisms
  - Cohen-Macaulay Rings
relations:
- kind: uses
  target: D-SCHCMGOR
- kind: uses
  target: D-MORFIN
review: draft
prompts:
- Show that a finite morphism between smooth varieties is flat, and state the hypotheses this needs.
---

::: {.proposition title="Miracle flatness"}
Let $f\colon X\to Y$ be a finite morphism of locally Noetherian schemes. Assume that for every $x\in X$, with $y=f(x)$,

- $\OO_{X,x}$ is Cohen--Macaulay;
- $\OO_{Y,y}$ is regular; and
- $\dim\OO_{X,x}=\dim\OO_{Y,y}$.

Then $f$ is flat.
In particular, a finite surjective morphism between smooth varieties of the same dimension over a field is flat.
[@Har77, Exercise III.10.9]
:::

::: {.proof}
Fix $x\in X$ and put
$$
A=\OO_{Y,y},\qquad B=\OO_{X,x},\qquad d=\dim A=\dim B.
$$
The ring $B$ is a finite $A$-module. Since $A\to B$ is local and finite, $\sqrt{\mfm_A B}=\mfm_B$, so depth computed with respect to $\mfm_A$ agrees with depth computed with respect to $\mfm_B$. Hence
$$
\depth_A B
=\depth_B B
=d,
$$
because $B$ is Cohen--Macaulay.

The regular local ring $A$ has finite global dimension $d$, so the finite $A$-module $B$ has finite projective dimension. Auslander--Buchsbaum gives
$$
\operatorname{pd}_A B+\depth_A B
=\depth A=d.
$$
Thus $\operatorname{pd}_A B=0$, so $B$ is finite projective over the local ring $A$, hence free. Therefore $B$ is flat over $A$. This holds at every $x$, so $f$ is flat.
:::

::: {.example}
The hypotheses cannot be dropped.
The inclusion of the origin $\Spec k \to \AA^1_k$ is finite and both schemes are smooth, but it is not flat, since $k = k[t]/(t)$ is a torsion $k[t]$-module; here the dimensions differ.
The normalization
$$
\AA^1_k\longrightarrow V(y^2-x^3),\qquad t\longmapsto(t^2,t^3),
$$
is finite between one-dimensional varieties with smooth source, but the target is not regular at the cusp. It is not flat: its generic rank is $1$, while over the cusp the fibre ring is
$$
k[t]\tensor_{k[t^2,t^3]}k\cong k[t]/(t^2),
$$
which has $k$-dimension $2$. A finite flat module over the connected cusp has locally constant rank, so these fibre dimensions cannot occur for a flat morphism.
:::
