---
schema: qual/card@1
id: P-LD7LI
kind: problem
title: "Unique fixed points"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Unique fixed points"}
Show that if $f$ is holomorphic on $\DD$ and continuous on $\bar\DD$ with $f(\bar \DD) \subseteq \DD$, then $f$ has a unique fixed point in $\DD$.

> Note: this is subtle because $\DD$ is not compact!

#complex/exercise/completed

:::

:::{.solution}
Continuous images of compact sets are compact, so $f(\bar\DD)$ is a compact subset of $\DD$ and thus contained in some $\DD_r(0)$ with $0<r<1$.
On this disc,
\[
\abs{f(z)} = \abs{f(z) - z + z} < \abs{z}
.\]
By Rouché, $f(z)-z$ and $z$ have the same number of zeros, which is one.
This holds for any $r'$ with $r<r'<1$, and thus holds on $\DD$.
:::
