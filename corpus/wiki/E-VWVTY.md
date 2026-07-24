---
schema: qual/card@1
id: E-VWVTY
kind: exercise
title: "Convergence of a $\\ZZ\\dash$index series"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Convergence of a $\ZZ\dash$index series"}
Find the radius of convergence for 
\[
f(z) \da \sum_{k\in \ZZ} 2^{-\abs{k}}z^k
.\]

:::

:::{.solution}
Break this up into a principal part at $z=0$ and a holomorphic part:
\[
f(z) = f_1(z) + f_2(z) \da \sum_{k\geq 1} 2^{-k}z^{-k} + \sum_{k\geq 0} 2^{-k}z^k
.\]

Using the ratio test:
\[
f_1(z) < \infty &\impliedby \limsup_k \abs{2^{-k}z^{-k}}^{1\over k} < 1 \iff \limsup_k \abs{1\over 2z} < 1 \iff {1\over 2}< \abs{z} \\
f_2(z) < \infty &\impliedby \limsup_k \abs{2^{-k}z^{k}}^{1\over k} < 1 \iff \limsup_k \abs{z\over 2}< 1 \iff \abs{z} < 2 
.\]

So $f$ converges on ${1\over 2}< \abs{z} < 2$.

:::

