---
schema: qual/card@1
id: P-UMC34
kind: problem
title: "Find all entire functions that satisfy $\\abs{f(z)} \\geq \\abs{z} \\quad \\forall z\\in \\CC$ Prove this list is\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - removable-singularities
  - zeros
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Find all entire functions that satisfy
\[
\abs{f(z)} \geq \abs{z} \quad \forall z\in \CC
.\]
Prove this list is complete.

:::


:::{.concept}
\envlist
- If $f$ is bounded in a neighborhood of a singularity $z_0$, then $z_0$ is removable.

:::


:::{.solution}
\envlist

- Suppose $f$ is entire and define $g(z) \definedas {z \over f(z)}$.
- By the inequality, $\abs{g(z)} \leq 1$, so $g$ is bounded.
- $g$ potentially has singularities at the zeros $Z_f \definedas f\inv(0)$, but since $f$ is entire, $g$ is holomorphic on $\CC\setminus Z_f$.
- Claim: $Z_f = \theset{0}$.
  - If $f(z) = 0$, then $\abs{z} \leq \abs{f(z)} = 0$ which forces $z=0$.
- We can now apply Riemann's removable singularity theorem:
  - Check $g$ is bounded on some open subset $D\smz$, clear since it's bounded everywhere
  - Check $g$ is holomorphic on $D\smz$, clear since the only singularity of $g$ is $z=0$.
- By Riemann's removable singularity theorem, the singularity $z = 0$ is removable and $g$ has an extension to an entire function $\tilde g$.
- By continuity, we have $\abs{\tilde g(z)} \leq 1$ on all of $\CC$
  - If not, then $\abs{\tilde g(0)} = 1+\eps > 1$, but then there would be a domain $\Omega \subseteq \CC\smz$ such that $1 < \abs{\tilde g(z)} \leq 1 +\eps$ on $\Omega$, a contradiction.
- By Liouville, $\tilde g$ is constant, so $\tilde g(z) = c_0$ with $\abs {c_0} \leq 1$
- Thus $f(z) = c_0\inv z \definedas cz$ where $\abs{c}\geq 1$

Thus all such functions are of the form $f(z) = cz$ for some $c\in \CC$ with $\abs{c}\geq 1$.
:::
