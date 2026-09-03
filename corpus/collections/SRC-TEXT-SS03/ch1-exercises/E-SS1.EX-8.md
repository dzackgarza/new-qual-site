---
schema: qual/card@1
id: E-SS1.EX-8
kind: problem
title: "The chain rule for the dz and dzbz derivatives"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
---

::: exercise
8. Suppose U and $V$ are open sets in the complex plane.
   Prove that if $f : U \to V$ and $g : V \to \mathbb { C }$ are two functions that are diferentiable (in the real sense, that is, as functions of the two real variables x and $y )$ , and $h = g \circ f$ , then

$$
\frac {\partial h}{\partial z} = \frac {\partial g}{\partial z} \frac {\partial f}{\partial z} + \frac {\partial g}{\partial \overline {{z}}} \frac {\partial \overline {{f}}}{\partial z}
$$

and

$$
\frac {\partial h}{\partial \overline {{z}}} = \frac {\partial g}{\partial z} \frac {\partial f}{\partial \overline {{z}}} + \frac {\partial g}{\partial \overline {{z}}} \frac {\partial \overline {{f}}}{\partial \overline {{z}}}.
$$

This is the complex version of the chain rule.
:::
