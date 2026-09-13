---
schema: qual/card@1
id: P-AGH248PROPSTAB
kind: problem
title: Stability properties of a class of morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphism Properties
  - Base Change
  - Separated Morphisms
relations: []
review: draft
---

::: problem
Let $\mathscr{P}$ be a property of morphisms of schemes such that

a. a closed immersion has $\mathscr{P}$;

b. a composition of two morphisms having $\mathscr{P}$ has $\mathscr{P}$;

c. $\mathscr{P}$ is stable under base extension.

Then show that

d. a product of morphisms having $\mathscr{P}$ has $\mathscr{P}$;

e. if $f: X \to Y$ and $g: Y \to Z$ are two morphisms, and if $g \circ f$ has $\mathscr{P}$ and $g$ is separated, then $f$ has $\mathscr{P}$;

f. if $f: X \to Y$ has $\mathscr{P}$, then $f_{\text{red}}: X_{\text{red}} \to Y_{\text{red}}$ has $\mathscr{P}$.

*Hint:* for (e), consider the graph morphism $\Gamma_f: X \to \fiberprod{X}{Z}{Y}$ and note that it is obtained by base extension from the diagonal morphism $\Delta: Y \to \fiberprod{Y}{Z}{Y}$.
:::
