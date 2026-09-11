---
schema: qual/card@1
id: P-AGXMISCGENUSONERAM
kind: problem
title: Maps of finite degree between genus one curves are unramified
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann--Hurwitz
  - Ramification
  - Elliptic Curves
relations: []
review: draft
---

::: problem
What is the maximum number of ramification points that a mapping of finite degree from one smooth projective curve over $\CC$ of genus 1 to another smooth projective curve of genus 1 can have?
Give an explanation for your answer.
:::

::: solution
By the Riemann--Hurwitz formula, if we have a mapping $f$ of finite degree $d$ from one smooth projective (irreducible, say) curve onto another, the Euler characteristic of the source curve is $d$ times the Euler characteristic of the target minus a certain nonnegative number $e$, and moreover $e$ is zero if and only if the mapping is unramified.
Now compute: the Euler characteristic of our source and target curves is, by hypothesis, $0$, so this $e$ is zero, and therefore the mapping is unramified.
:::
