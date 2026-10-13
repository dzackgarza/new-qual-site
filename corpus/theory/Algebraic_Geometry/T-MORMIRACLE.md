---
schema: qual/card@1
id: T-MORMIRACLE
kind: theorem
title: Miracle flatness
slogan: 'For a Cohen--Macaulay source over a regular base, fibres of the expected dimension force flatness.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flatness
  - Regularity
  - Fibre Dimension
relations:
- kind: uses
  target: D-MORFLAT
review: draft
prompts:
- Give a criterion for a morphism to be flat.
- When is a morphism between smooth varieties flat?
---

::: {.theorem title="Miracle flatness"}
Let $(A,\mfm)\to(B,\mfn)$ be a local homomorphism of Noetherian local rings. Assume that $A$ is regular, $B$ is Cohen--Macaulay, and
$$
\dim B=\dim A+\dim(B/\mfm B).
$$
Then $B$ is flat over $A$.
:::

::: {.corollary title="Geometric form"}
Let $f\colon X\to Y$ be a morphism locally of finite type between locally Noetherian schemes. Assume that $X$ is Cohen--Macaulay and $Y$ is regular. If for every $x\in X$, with $y=f(x)$,
$$
\dim\OO_{X,x}
=\dim\OO_{Y,y}+\dim\OO_{X_y,x},
$$
then $f$ is flat.

In particular, if $X$ and $Y$ are smooth irreducible varieties and every nonempty fibre is pure of dimension $\dim X-\dim Y$, then $f$ is flat.
:::

::: {.remark}
Let $d=\dim A$ and choose a regular system of parameters $t_1,\ldots,t_d$ for $A$. The dimension equality says that their images in $B$ cut the dimension down by exactly $d$. Since $B$ is Cohen--Macaulay, $t_1,\ldots,t_d$ form a $B$-regular sequence. The local criterion for flatness then lifts flatness from the residue-field quotient $B/\mfm B$ successively across the parameters, giving flatness over $A$.

For the blowup $\Bl_0\AA^2\to\AA^2$, the generic fibres are zero-dimensional while the exceptional fibre has dimension $1$. The local dimension equality therefore fails over the origin, consistently with nonflatness.

For flat local maps of Noetherian local rings the displayed dimension formula is necessary. Miracle flatness says that, with regular base and Cohen--Macaulay source, this necessary dimension condition is also sufficient.
:::
