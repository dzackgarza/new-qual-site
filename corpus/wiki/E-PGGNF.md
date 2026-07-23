---
schema: qual/card@1
id: E-PGGNF
kind: exercise
title: "Half disc to full disc"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Half disc to full disc"}
Find a conformal map from $\ts{z\in \CC \st \abs{z} < 1, \Im(z) > 0} = \DD \intersect \HH$ to $\DD$.
:::

:::{.solution}
Note that $z\mapsto z^2$ doesn't actually work, because the image is $\DD\sm \RR_{\geq 0}$ and has a slit deleted.
Instead compose:

- $z\mapsto i{z-1\over z+1}$, which maps $\DD\to \HH$ and restricts to map $\DD \intersect \HH \to Q_1$.
- $z\mapsto z^2$, which maps $Q_1\to \HH$
- $z\mapsto {z-i\over z+i}$ which maps $\HH\to \DD$.
:::

:::{.solution title="Using Joukowski maps"}
In parts:

- Use $z\mapsto z\inv$ to send $\HH \intersect \DD$ to $Q_{34} \intersect \DD^c$.
- Use $z\mapsto -z$ to map this to $\HH \intersect \DD^c$
- Use $z\mapsto {1\over 2}(z+z\inv)$ to map $\HH \intersect \DD^c$ to $\HH$
- Then use the Cayley map $z\mapsto {z-i\over z+i}$ to map $\HH\to \DD$.

:::


