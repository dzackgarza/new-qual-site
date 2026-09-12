---
schema: qual/card@1
id: P-BKS03-5B
kind: problem
title: Distance between a compact set and a closed set is attained
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $C,D\subseteq\mathbb R^n$ be nonempty closed sets and assume $C$ is bounded.
Prove there exist $x_0\in C$ and $y_0\in D$ such that
\[
d(x_0,y_0)\le d(x,y)
\]
for all $x\in C$ and $y\in D$.
:::

::: {.solution}
It follows from the triangle inequality that $d ( x , y )$ is uniformly continuous as a real-valued function on $C \times D$ . If C and D were both bounded, then $C \times D$ would be compact and $d ( x , y )$ would attain its minimum.
In the general case, let $d _ { 0 }$ be the infimum of $d ( x , y )$ on $C \times D$ . Let $\boldsymbol { B } _ { R _ { 0 } }$ be a closed ball of radius $R _ { 0 }$ around the origin containing $C _ { i }$ and set $R _ { 1 } = R _ { 0 } + d _ { 0 } + \epsilon .$ for some arbitrary $\epsilon > 0$ . Then for $y \notin B _ { R _ { 1 } }$ , we clearly have $d ( x , y ) > d _ { 0 } + \epsilon$ for all $x \in C$ It follows that $D \cap B _ { R _ { 1 } }$ is non-empty, and the infimum of $d ( x , y )$ on $C \times ( D \cap B _ { R _ { 1 } } )$ is equal to $d _ { 0 }$ . Since $C \times ( D \cap B _ { R _ { 1 } } )$ is compact, the minimum is attained for some $( x _ { 0 } , y _ { 0 } ) \in C \times ( D \cap B _ { R _ { 1 } } )$
:::
