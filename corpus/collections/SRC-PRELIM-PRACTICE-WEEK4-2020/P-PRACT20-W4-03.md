---
schema: qual/card@1
id: P-PRACT20-W4-03
kind: problem
title: Salt in a tank with equal inflow and outflow rates
classification:
  areas:
  - applied-algebra
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
A tank initially contains a salt solution of 3 grams of salt dissolved in 100 liters of water.
A salt solution containing 0.02 grams of salt per liter is pumped into the tank at 4 liters per minute.
The tank is also draining at 4 liters per minute.
Assuming the mixing is instantaneous, how many grams of salt are in the tank after 100 minutes?
:::

::: {.solution}
Let $S$ denote the amount of salt in the tank in grams.
Then $S ( 0 ) = 3$ , and the change in S is given by

$$
{ \frac { d S } { d t } } = \mathrm {  ~ \tilde { \ s a l t } ~ i n " ~ } - \mathrm {  ~ \tilde { \ s a l t } ~ o u t " ~ } = \left( 0 . 0 2 { \frac { g \mathrm { r a m s } } { \mathrm { l i t e r s } } } \right) \left( 4 \mathrm { \frac { l i t e r s } { s e c } } \right) - \left( { \frac { S } { 1 0 0 } } { \frac { g \mathrm { r a m s } } { \mathrm { l i t e r s } } } \right) \left( 4 { \frac { \mathrm { l i t e r s } } { s e c } } \right) = { \frac { 2 } { 2 5 } } - { \frac { S } { 2 5 } } .
$$

The particular solution is $S _ { p } ( t ) = 2$ and the homogeneous solution is $S _ { h } ( t ) = e ^ { - t / 2 5 }$ . Thus the solution is

$$
S ( t ) = 2 - C e ^ { - t / 2 5 } .
$$

and S(0) = 3 gives $C = - 1$ so

$$
S ( t ) = 2 + e ^ { - t / 2 5 } \quad \Longrightarrow \quad \Bigl \lceil S ( 1 0 0 ) = 2 + e ^ { - 4 } . \Bigr \rceil
$$
:::
