---
schema: qual/card@1
id: P-ALGF09H
kind: problem
title: "Intersection of noetherian ring quotients is noetherian"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 8 of the official UCSD Algebra Qualifying Examination, Fall 2009; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the injective diagonal map into R/I direct-sum R/J and the module-theoretic Noetherian argument; no false appeal to inheritance by arbitrary subrings is used.
---

::: {.problem}
Let $R$ be a commutative ring with identity.
Suppose that $I$ and $J$ are ideals of $R$ such that $R/I$ and $R/J$ are Noetherian rings.
Prove that $R/(I \cap J)$ is also a Noetherian ring.
:::

::: {.solution}
We regard all quotient rings below as $R$-modules through the natural quotient maps.

<1>1. The modules $R/I$ and $R/J$ are Noetherian as $R$-modules.
::: {.proof}
An $R$-submodule of $R/I$ is exactly an ideal of the quotient ring $R/I$.
Indeed, the scalar action of $R$ on $R/I$ factors through $R/I$ itself.
Since $R/I$ is Noetherian as a ring, every ascending chain of its ideals stabilizes.
Therefore every ascending chain of $R$-submodules of $R/I$ stabilizes, so $R/I$ is a Noetherian $R$-module.
The same argument applies to $R/J$.
:::

<1>2. The direct sum
\[
R/I\oplus R/J
\]
is a Noetherian $R$-module.
::: {.proof}
A finite direct sum of Noetherian modules is Noetherian.
For completeness, consider the exact sequence
\[
0\longrightarrow R/I
\longrightarrow R/I\oplus R/J
\longrightarrow R/J
\longrightarrow0,
\]
where the first map includes the first summand and the second projects onto the second summand.
If the submodule and quotient in a short exact sequence are Noetherian, then the middle module is Noetherian: for any ascending chain in the middle module, the intersections with the submodule and the images in the quotient both stabilize, forcing the original chain to stabilize.
By <1>1, both outer modules are Noetherian, so the direct sum is Noetherian.
:::

<1>3. There is an injective $R$-linear map
\[
R/(I\cap J)\longrightarrow R/I\oplus R/J.
\]
::: {.proof}
Define
\[
\phi:R\longrightarrow R/I\oplus R/J,
\qquad
r\longmapsto(r+I,r+J).
\]
Its kernel is
\[
\ker\phi
=I\cap J.
\]
Therefore the first isomorphism theorem gives an injective $R$-linear map
\[
\bar\phi:R/(I\cap J)\hookrightarrow R/I\oplus R/J.
\]
:::

<1>4. The $R$-module $R/(I\cap J)$ is Noetherian.
::: {.proof}
By <1>2, the module
\[
R/I\oplus R/J
\]
is Noetherian.
Every submodule of a Noetherian module is Noetherian.
By <1>3, $R/(I\cap J)$ is isomorphic to an $R$-submodule of this direct sum.
Hence $R/(I\cap J)$ is a Noetherian $R$-module.
:::

<1>5. The quotient ring $R/(I\cap J)$ is Noetherian.
::: {.proof}
The ideals of
\[
R/(I\cap J)
\]
are exactly its $R$-submodules, because the $R$-action factors through the quotient ring.
By <1>4, every ascending chain of such $R$-submodules stabilizes.
Therefore every ascending chain of ideals of $R/(I\cap J)$ stabilizes.
Thus
\[
R/(I\cap J)
\]
is a Noetherian ring.
:::
:::
