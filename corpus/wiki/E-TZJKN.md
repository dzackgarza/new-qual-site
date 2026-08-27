---
schema: qual/card@1
id: E-TZJKN
kind: exercise
title: Holomorphic functions have harmonic components
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

:::{.exercise}
Show that if $f = u+iv$ is holomorphic then $u, v$ are harmonic.
:::

:::{.solution}
Idea: use Cauchy-Riemann, take further derivatives, and use equality of partials.

- By CR, 
\[
u_x = v_y && u_y = -v_x
.\]

- Differentiate with respect to $x$: 
\[
u_{xx} = v_{yx} && u_{yx} = -v_{xx}
.\]
- Differentiate with respect to $y$:
\[
u_{xy} = v_{yy} && u_{yy} = -v_{xy}
.\]
- Clairaut's theorem: partials are equal, so
\[
u_{xx} - v_{yx} = 0 \implies u_{xx} + u_{yy} = 0 \\ \\
v_{xx} + u_{yx} = 0 \implies v_{xx} + v_{yy} = 0 \\ \\
.\]



:::
