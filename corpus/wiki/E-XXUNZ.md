---
schema: qual/card@1
id: E-XXUNZ
kind: exercise
title: "Show that if $f_n\\to f$ uniformly then $\\int_\\gamma f_n\\to \\int_\\gamma f$."
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - contour-integration
  - sequences-of-functions
relations: []
review: draft
solved: true
---
:::{.exercise title="?"}
Show that if $f_n\to f$ uniformly then $\int_\gamma f_n\to \int_\gamma f$.

:::

:::{.solution}
\[
\abs{
\int_\gamma f_n(z) \dz - \int_\gamma f(z) \dz
}
&=
\abs{\int_\gamma f_n(z) - f(z) \dz}  \\
&\leq \int_\gamma \abs{f_n - f} \abs{\dz} \\
&\leq \int_\gamma \norm{f_n - f}_{\infty, \gamma} \cdot \abs{\dz} \\
&= \eps \cdot \length(\gamma) \\
&\convergesto{n\to\infty} 0
.\]

:::

