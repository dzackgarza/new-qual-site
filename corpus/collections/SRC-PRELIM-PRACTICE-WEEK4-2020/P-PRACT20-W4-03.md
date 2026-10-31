---
schema: qual/card@1
id: P-PRACT20-W4-03
kind: problem
title: Salt in a tank with equal inflow and outflow rates
classification:
  areas:
  - prelim
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
Then $S(0)=3$. The volume stays at $100$ liters, so the concentration is $S/100$ grams per liter, and with $t$ in minutes

$$
\frac{dS}{dt}=\text{``salt in''}-\text{``salt out''}=\left(0.02\,\frac{\text{grams}}{\text{liter}}\right)\left(4\,\frac{\text{liters}}{\text{min}}\right)-\left(\frac{S}{100}\,\frac{\text{grams}}{\text{liter}}\right)\left(4\,\frac{\text{liters}}{\text{min}}\right)=\frac{2}{25}-\frac{S}{25}.
$$

A particular solution is $S_p(t)=2$ and the homogeneous solutions are $Ce^{-t/25}$. Thus

$$
S(t)=2+Ce^{-t/25},
$$

and $S(0)=3$ gives $C=1$, so

$$
S(t)=2+e^{-t/25}\quad\Longrightarrow\quad\boxed{S(100)=2+e^{-4}}\text{ grams}.
$$
:::
