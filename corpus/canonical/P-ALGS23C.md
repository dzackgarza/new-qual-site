---
schema: qual/card@1
id: P-ALGS23C
kind: problem
title: "Injectivity by localization, flat equals free over PID, and projective implies flat"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
---

::: problem
Suppose $A$ is a unital commutative ring, $M$ and $N$ are $A$-modules, and $f: M \to N$ is an $A$-module homomorphism.
For every maximal ideal $\mathfrak{m}$ of $A$, let $M_\mathfrak{m}$ and $N_\mathfrak{m}$ be the localizations of $M$ and $N$ at $\mathfrak{m}$, respectively.
Recall that $$f_\mathfrak{m}: M_\mathfrak{m} \to N_\mathfrak{m}, \quad f_\mathfrak{m}\!\left(\frac{x}{s}\right) := \frac{f(x)}{s}$$ is an $A_\mathfrak{m}$-module homomorphism.
Prove that if $f_\mathfrak{m}$ is injective for all maximal ideals $\mathfrak{m}$, then $f$ is injective.

(a) Suppose $D$ is a PID. Prove that a finitely generated $D$-module is flat if and only if it is free.

(b) Prove that every projective $A$-module is flat.
:::
