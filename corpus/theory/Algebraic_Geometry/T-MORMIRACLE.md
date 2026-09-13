---
schema: qual/card@1
id: T-MORMIRACLE
kind: theorem
title: Miracle flatness
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
Let $f : X \to Y$ be a local homomorphism of Noetherian local rings, or a morphism of schemes locally of finite type, with $X$ Cohen--Macaulay and $Y$ regular.
If
\[
\dim_x X_{f(x)} = \dim_x X - \dim_{f(x)} Y
\]
at every point, that is, the fibres have the expected dimension, then $f$ is flat.
:::

::: {.remark}
This is the theorem that makes flatness checkable, since the hypotheses are about dimension and the conclusion is about modules.
In the form one uses it: a morphism between smooth varieties with equidimensional fibres of the expected dimension is flat.

It also explains the blowup counterexample rather than merely contradicting it: $\Bl_0 \AA^2 \to \AA^2$ has a fibre of dimension $1$ where the expected dimension is $0$, so the hypothesis fails at exactly the point where flatness does.

The displayed dimension formula is itself a consequence of flatness in general, so the theorem says that for a Cohen--Macaulay source over a regular base the necessary condition is sufficient.
Cohen--Macaulay is the hypothesis people forget, and it is what rules out a source with an embedded component in one fibre.
:::
