---
schema: qual/card@1
id: P-AGH2311CLOSEDSUB
kind: problem
title: Closed subschemes under base change and the scheme-theoretic image
classification:
  areas:
  - algebraic-geometry
  topics:
  - Closed Subschemes
  - Base Change
  - Reduced Induced Structure
relations: []
review: draft
---

::: problem
a. Closed immersions are stable under base extension: if $f: Y \to X$ is a closed immersion and $X' \to X$ is any morphism, then $f': \fiberprod{Y}{X}{X'} \to X'$ is also a closed immersion.

b. If $Y$ is a closed subscheme of an affine scheme $X = \Spec A$, then $Y$ is also affine, and in fact $Y$ is the closed subscheme determined by a suitable ideal $\mfa \subseteq A$ as the image of the closed immersion $\Spec A/\mfa \to \Spec A$.

c. Let $Y$ be a closed subset of a scheme $X$ and give $Y$ the reduced induced subscheme structure.
If $Y'$ is any other closed subscheme of $X$ with the same underlying topological space, show that the closed immersion $Y \to X$ factors through $Y'$.
We express this by saying that **the reduced induced structure is the smallest subscheme structure on a closed subset**.

d. Let $f: Z \to X$ be a morphism.
Then there is a unique closed subscheme $Y$ of $X$ with the following property: the morphism $f$ factors through $Y$, and if $Y'$ is any other closed subscheme of $X$ through which $f$ factors, then $Y \to X$ factors through $Y'$ also.
We call $Y$ the **scheme-theoretic image** of $f$.
If $Z$ is a reduced scheme, then $Y$ is just the reduced induced structure on the closure of the image $f(Z)$.
:::

::: remark
For part (b): first show that $Y$ can be covered by a finite number of open affine subsets of the form $D(f_i) \intersect Y$ with $f_i \in A$.
By adding some more $f_i$ with $D(f_i) \intersect Y = \varnothing$ if necessary, arrange that the $D(f_i)$ cover $X$.
Next show that $f_1, \ldots, f_r$ generate the unit ideal of $A$.
Then use the affineness criterion of II.2.17(b) to show that $Y$ is affine, and II.2.18(d) to show that $Y$ comes from an ideal $\mfa \subseteq A$.
A second proof using sheaves of ideals appears later in Hartshorne V.10.
:::
