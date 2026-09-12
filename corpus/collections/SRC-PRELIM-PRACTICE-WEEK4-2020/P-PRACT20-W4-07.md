---
schema: qual/card@1
id: P-PRACT20-W4-07
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 7"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Find all the solutions of the equation $y y ^ { \prime \prime } - 2 ( y ^ { \prime } ) ^ { 2 } = 0$ which pass through $x = 1 , y = 1$
:::

::: {.solution}
Divide the equation by $y y ^ { \prime }$ to arrive at

$$
{ \frac { y ^ { \prime \prime } } { y ^ { \prime } } } - 2 { \frac { y ^ { \prime } } { y } } = 0 \quad \Longrightarrow \quad \log ( y ^ { \prime } ) - 2 \log ( y ) = C \quad \Longrightarrow \quad { \frac { y ^ { \prime } } { y ^ { 2 } } } = C
$$

where now $C > 0$ . Integrating again gives

$$
- { \frac { 1 } { y } } = C x + D \Longrightarrow y ( x ) = { \frac { 1 } { D - C x } }
$$

where again $C > 0$ . Plugging in $y ( 1 ) = 1$ shows that $D - C = 1 { \mathrm { ~ s o ~ } } D = 1 + C$ . So the set of all such solutions is

$$
{ \Bigg | } y ( x ) = { \frac { 1 } { 1 + C ( 1 - x ) } } , { \Bigg | } \quad \mathrm { f o r } \ C > 0 .
$$
:::
