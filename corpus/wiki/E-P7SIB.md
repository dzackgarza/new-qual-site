---
schema: qual/card@1
id: E-P7SIB
kind: exercise
title: "Trig identities"
classification:
  areas:
  - complex-analysis
  topics:
  - trigonometry
relations: []
review: draft
solved: true
---
:::{.exercise title="Trig identities"}
Find an identity for $\cos(4\theta)$ in terms of $\sin(\theta)$ and $\cos(\theta)$.
:::

:::{.solution}
Write $x=\cos(\theta), y= \sin(\theta)$, so $e^{i\theta} = x+iy$.
Then
\[
\cos(4\theta) + i\sin(4\theta) 
&= e^{4i\theta } \\
&= (x+iy)^4 \\
&= \sum_{0\leq k \leq 4} {4\choose k} x^k (iy)^{4-k} \\
&= x^4 + 4ix^3y - 6x^2y^2 - 4ixy^3 + y^4 \\
&= (x^4 - 6x^2y^2 + y^4) + i(4x^3y - 4xy^3)
.\]
So
\[
\cos(4\theta) 
&= \cos^4(\theta) - 6\cos^2(\theta)\sin^2(\theta) + \sin^4(\theta)\\
\sin(4\theta)
&= \cos^3(\theta)\sin(\theta) + \cos(\theta)\sin^3(\theta)
.\]


:::

