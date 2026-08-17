---
schema: qual/card@1
id: E-EYILL
kind: exercise
title: "No fixed points implies homotopic to antipodal"
classification:
  areas:
  - topology
  topics:
  - degree
  - fixed-points
  - homotopy
relations: []
review: draft
solved: true
---
:::{.exercise title="No fixed points implies homotopic to antipodal"}
Show that if $f: S^n\to S^n$ has no fixed points $\iff \deg f = (-1)^{n+1}$ and $f$ is homotopic to the antipodal map.
:::

:::{.concept}
\envlist

- If $f(x)\neq x$, the line segment $L(-x, f(x))$ does not contain $0$. 

- If $f(x) \neq -x$, the line segment $L(x, f(x))$ does not contain $0$.
:::

:::{.solution}
The straight line homotopy $H(t, x) = (1-t)f(x) + t(-x)$ is a homotopy between $f$ and the antipodal map in $\RR^{n+1}$.
Use that $H(t, x) = 0 \iff t=1/2 \iff f(x) = x$, so $H(t, \wait)$ is always a line from $x$ to $f(x)$ not passing through $0$, so $H(t, \wait) \neq 0$. 
So this descends to a homotopy of $\RR^{n+1}\smz \homotopic S^n$, or explicitly one can project
\[
H: I\cross S^n &\to S^n \\
(t, x) &\mapsto {H(t, x) \over \norm{H(t, x)}}
.\]

Less explicitly: if $f(x) \neq x$ for all $x\in S^n$, there is a unique geodesic through these two points, so let each point flow along its corresponding geodesic.
:::
