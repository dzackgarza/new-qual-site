---
schema: qual/card@1
id: P-PJH3T
kind: problem
title: Here we examine
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
relations: []
review: draft
---

::: problem
Here we examine

$$
H_1\RP^2 \mapsvia{\delta_1} H_0 \del M \mapsvia{(i^0, j^0)} H_0 M \oplus H_0 D^2 \mapsvia{l^0 - r^0} H_0\RP^2 \mapsvia{\delta_0} 0\\
\ZZ_2 \mapsvia{\delta_1} \ZZ \mapsvia{(i^0, j^0)} \ZZ \oplus \ZZ \mapsvia{l^0 + r^0} H_0\RP^2 \mapsvia{\delta_0} 0
$$

Since there is no nontrivial homomorphism from $\ZZ_2 \to \ZZ$, we have $\delta_1 = 0$.

We also have $\delta_0 = 0$ and $\ker \delta_0 = H_0 \RP^2 = \im l^0 + r^0$ making $l^0 + r^0$ surjective, so by the first isomorphism theorem we have $H_0 \RP^2 \cong \frac{\ZZ \oplus \ZZ}{\ker l^0 + r^0} = \frac{\ZZ \oplus \ZZ}{\im (i^0, j^0)}$

By a similar argument used earlier, the double covering of the boundary circle $\del M$ over $S^1$ yields the map $(i^0, j^0): \ZZ \into \ZZ \oplus \ZZ$ given by $x \mapsto (2x, 2x)$ with

**Summary:**

With all of this information, we finally have

```{=latex}
\begin{tikzcd}
&  &  &  & 0 \arrow[lllldd, out=0, in=-180, "0"'] \\
&  &  &  &  \\
0 \arrow[rr] \arrow[rr, "{0 \mapsto (0,0)}"] &  & 0 \oplus 0 \arrow[rr, "{(0,0)  \mapsto 0}"] &  & 0 \arrow[lllldd, "0"', out=0, in=-180] \\
&  &  &  &  \\
\mathbb{Z} \arrow[rr, "{x\mapsto (2x, 0)}"] &  & 2\mathbb{Z} \oplus 0 \arrow[rr, "{(x,0) \mapsto x \mod 2}"] &  & \mathbb{Z}_2 \arrow[lllldd, "0"', out=0, in=-180] \\
&  &  &  &  \\
\mathbb{Z} \arrow[rr, "{x \mapsto (2x, x)}"] &  & 2\mathbb{Z} \oplus \mathbb{Z} \arrow[rr, "{(x,y) \mapsto x-y}"] &  & \mathbb{Z} \arrow[lllldd, "0"', out=0, in=-180] \\
&  &  &  &  \\
0 &  &  &  &
\end{tikzcd}
```

And so we find $H_*(\RP^2) = \ZZ \delta_0 + \ZZ_2\delta_1$
:::
