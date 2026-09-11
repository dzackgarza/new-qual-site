---
schema: qual/card@1
id: P-AGH291FORMALREG
kind: problem
title: Formal-regular functions along a subvariety of projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Completion
  - Conormal Sheaves
relations: []
review: draft
---

::: problem
Let $X$ be a noetherian scheme, $Y$ a closed subscheme, and $\hat X$ the completion of $X$ along $Y$.
We call the ring $\Gamma(\hat X, \OO_{\hat X})$ the ring of **formal-regular** functions on $X$ along $Y$.
In this exercise we show that if $Y$ is a connected, nonsingular, positive dimensional subvariety of $X = \PP^n_k$ over an algebraically closed field $k$, then $\Gamma(\hat X, \OO_{\hat X}) = k$.

a. Let $\mci$ be the ideal sheaf of $Y$.
Show that there is an inclusion of sheaves on $Y$, $\mci/\mci^2 \injects \OO_Y(-1)^{n+1}$.

b. Show that for any $r \geq 1$, $\Gamma(Y, \mci^r/\mci^{r+1}) = 0$.

c. Use the exact sequences
\[
0 \to \mci^r/\mci^{r+1} \to \OO_X/\mci^{r+1} \to \OO_X/\mci^r \to 0
\]
and induction on $r$ to show that $\Gamma(Y, \OO_X/\mci^r) = k$ for all $r \geq 1$.

d. Conclude that $\Gamma(\hat X, \OO_{\hat X}) = k$.
Actually the same result holds without the hypothesis that $Y$ is nonsingular, but the proof is more difficult.
:::
