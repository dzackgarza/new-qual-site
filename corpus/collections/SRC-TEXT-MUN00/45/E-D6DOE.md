---
schema: qual/card@1
id: E-D6DOE
kind: problem
title: Ascoli's theorem over proper metric targets
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Show that our proof of Ascoli's theorem goes through if $\mathbb{R}^n$ is replaced by any metric space in which all closed bounded subspaces are compact.
:::

::: {.solution}
Inspect the proof of Ascoli's theorem. The only property of the target $\mathbb R^n$ used beyond metrizability is that for each $x\in X$, pointwise boundedness places the set
\[
\{f(x):f\in\mathcal F\}
\]
in a compact set, and likewise finitely many bounded target sets arising in the finite-net argument have compact closure. If every closed bounded subset of the metric target $Y$ is compact, these steps remain valid verbatim.

More explicitly, equicontinuity reduces uniform control on a compact domain to finitely many evaluation points. Pointwise boundedness makes the possible values at each of these finitely many points lie in bounded subsets of $Y$; their closures are compact by hypothesis, hence totally bounded. Finite $\varepsilon$-nets in these compact closures then give a finite $\varepsilon$-net for $\mathcal F$ in the uniform metric. Thus $\mathcal F$ is totally bounded. The closure of an equicontinuous family is equicontinuous, and pointwise limits remain in the compact value closures; the standard diagonal/Cauchy argument therefore gives compactness of the closure exactly as in the Euclidean proof. Hence Ascoli's theorem holds for every proper metric target (every closed bounded subset compact).
:::
