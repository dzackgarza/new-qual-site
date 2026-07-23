---
schema: qual/card@1
id: P-CZ3R7
kind: problem
title: "a. Prove that if $c>0$,"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
\envlist

a. Prove that if $c>0$,
\[
\abs{w_1} = c\abs{w_2} \implies \abs{w_1 - c^2 w_2} = c\abs{w_1 - w_2}
.\]

b. Prove that if $c>0$ and $c\neq 1$, with $z_1\neq z_2$, then the following equation represents a circle:
\[
\abs{z-z_1 \over z-z_2} = c
.\]
Find its center and radius.

> Hint: use part (a)

:::

:::{.solution title="part 1"}
\[
\abs{w_1 - c^2 w_2}^2 
&= (w_1 - c^2 w_2) ( \bar{w_1} - c^2 \bar{w_2} ) \\
&= \abs{w_1}^2 + c^4 \abs{w_2}^2 - 2c^2 \Re(w_1 \bar{w_2}) \\
&= {\color{green} c^2 \abs{w_2}^2 } + c^4 \abs{w_2}^2 - 2c^2 \Re(w_1 \bar{w_2}) \\
&= c^2 \abs{w_2}^2 + {\color{green} c^2 \abs{w_1}^2 } - 2c^2 \Re(w_1 \bar{w_2}) \\
&= c^2 \abs{w_1 - w_2}
,\]
where we've applied the assumption $\abs{w_1} = c\abs{w_2}$ twice.
:::

:::{.solution title="part 2"}
Using part 1:
\[
w_1\da z-z_1, w_2 \da z-z_2 \implies \abs{w_1} &= c\abs{w_2} \\
\implies \abs{w_1 - c^2 w_2} &= c \abs{w_1 - w_2} \\
\implies \abs{ z-z_1 - c^2 (z-z_2) } &= \abs{(z-z_1) - (z-z_2)} \\
\implies \abs{(1-c^2) z - z_3} &= \abs{ z_2 - z_1 } \\
\implies \abs{z-z_4} &= r
,\]
where the $z_i$ and $r$ are all constant, so this is the equation of a circle.
:::


