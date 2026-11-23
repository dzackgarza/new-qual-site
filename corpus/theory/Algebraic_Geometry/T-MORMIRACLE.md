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
Let $(A,\mfm)\to(B,\mfn)$ be a local homomorphism of Noetherian local rings. Assume that $A$ is regular, $B$ is Cohen--Macaulay, and the fibre ring $B/\mfm B$ has pure dimension $\dim B-\dim A$, that is, $\dim B=\dim A+\dim(B/\mfm B)$ with every minimal prime of $B/\mfm B$ of that dimension.
Then $B$ is flat over $A$ [@Vak25, Theorem 26.2.10, whose hypothesis is purity of the fibre ring].
The numerical equality alone is what a flat local map satisfies; it is the purity that the theorem assumes.
The printed statement writes the local map as $(B,\mathfrak n)\to(A,\mathfrak m)$ with $B$ regular, $A$ Cohen--Macaulay and the fibre $A\otimes_B(B/\mathfrak n)$ of pure dimension $\dim A-\dim B$, so the letters on the two rings are the other way round from the ones displayed here.
:::

::: {.corollary title="Geometric form"}
Let $f\colon X\to Y$ be a morphism locally of finite type between locally Noetherian schemes. Assume that $X$ is Cohen--Macaulay and $Y$ is regular. If for every $x\in X$, with $y=f(x)$, the local ring of the fibre at $x$,
$$
\OO_{X_y,x}=\OO_{X,x}/\mfm_y\OO_{X,x},
$$
has pure dimension $\dim\OO_{X,x}-\dim\OO_{Y,y}$, in particular if $\dim\OO_{X,x}=\dim\OO_{Y,y}+\dim\OO_{X_y,x}$ at every $x$ and $\OO_{X_y,x}$ is equidimensional, then $f$ is flat: this is the theorem applied to the local homomorphism $\OO_{Y,y}\to\OO_{X,x}$ at each $x$ [@Vak25, Theorem 26.2.10].

In particular, if $X$ and $Y$ are smooth irreducible varieties and every nonempty fibre is pure of dimension $\dim X-\dim Y$, then $f$ is flat [@Vak25, Theorem 26.2.11].
:::

::: {.remark}
Let $d=\dim A$ and choose a regular system of parameters $t_1,\ldots,t_d$ for $A$. The dimension equality says that their images in $B$ cut the dimension down by exactly $d$. Since $B$ is Cohen--Macaulay, $t_1,\ldots,t_d$ form a $B$-regular sequence. The local criterion for flatness then lifts flatness from the residue-field quotient $B/\mfm B$ successively across the parameters, giving flatness over $A$.

For the blowup $\Bl_0\AA^2\to\AA^2$, the generic fibres are zero-dimensional while the exceptional fibre has dimension $1$. The local dimension equality therefore fails over the origin, consistently with nonflatness.

For flat local maps of Noetherian local rings the displayed dimension formula is necessary. With a regular base and a
Cohen--Macaulay source it is also sufficient, with no further hypothesis on the fibre ring: that is the Stacks Project,
Lemma 10.128.1, tag 00R4, and the theorem above is its pure-fibre form [@Vak25, Theorem 26.2.10].
:::
