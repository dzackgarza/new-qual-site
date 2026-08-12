---
schema: qual/card@1
id: D-BVOUL
kind: definition
title: "Group Action"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.definition title="Group Action"}
An action of $G$ on $X$ is a group morphism
\[
\phi:G \times X &\rightarrow X \\ 
(g,x) &\mapsto g x
\]
or equivalently
\[
\phi: G &\to \Aut(X) \\
g &\mapsto (x \mapsto \phi_g (x) \definedas g\cdot x)
\]
satisfying

1. $e\cdot x = x$
2. $g\cdot (h\cdot x) = (gh)\cdot x$
:::
