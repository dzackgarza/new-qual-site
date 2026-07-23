---
schema: qual/card@1
id: E-B3GAV
kind: exercise
title: "Show that there is no continuous square root function defined on all o\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that there is no continuous square root function defined on all of $\CC$.
:::

:::{.solution}
Suppose $f(z)^2 = z$. 
Then $f$ is a section to the covering map
\[
p: \CC\units &\to \CC\units \\
z & \mapsto z^2
,\]
so $p\circ f = \id$.
Using $\pi_1(\CC\units) = \ZZ$, the induced maps are $p_*(1) = 2$ and $f_*(1) = n$ for some $n\in \ZZ$.
But then $p_* \circ f_*$ is multiplication by $2n$, contradicting $p_* \circ f_* = \id$ by functoriality.
:::
