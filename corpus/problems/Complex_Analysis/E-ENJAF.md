---
schema: qual/card@1
id: E-ENJAF
kind: exercise
title: Expansion at an essential singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Essential Singularities
  - Power Series
relations: []
review: draft
---

:::{.exercise}
Find a Laurent expansion at $z=0$ for
\[
f(z) \da e^{1\over z}\cos\qty{1\over z}
.\]

:::

:::{.solution}
Note that a direct expansion won't work, since there are infinitely many contributions to the constant term.
Instead, a trick: consider $g(z) \da e^z\cos(z)$, so $g(1/z ) = f(z)$.
Expanding $g$ is easier:
\[
g(z) 
&= e^{z}\cos(z)\\
&= {1\over 2}e^z\qty{e^{iz} + e^{-iz}} \\
&= {1\over 2}\qty{e^{(1+i)z} + e^{(1-i)z}} \\
&= {1\over 2} \sum_{k\geq 0}\qty{(1+i)^k + (1-i)^k} {z^k\over k!} \\
\implies f(z) 
&= {1\over 2} \sum_{k\geq 0}\qty{(1+i)^k + (1-i)^k} {1 \over k!z^k } \\
.\]

:::

