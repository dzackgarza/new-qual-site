---
title: Meromorphic functions
order: 30
---

# Meromorphic functions

A function whose only singularities are poles: holomorphic everywhere except at a discrete set, and blowing up in the mildest possible way at each point of it.

[[D-7DFVJ]]

[[T-UBWL2]]

::: {.proof}
Consider $f(z) - P(z)$, subtracting off the principal part at each pole, to obtain a bounded entire function, and apply Liouville.
:::

::: {.remark title="Why the proof is short"}
Every step is a theorem already in hand.
The principal part at a pole is a finite sum of powers of $(z-z_0)\inv$, so subtracting it is legal and leaves a function with removable singularities.
Finiteness of the pole set makes the subtraction finite, and Liouville turns bounded-and-entire into constant.
This is the standard shape of a meromorphic-function argument: remove the poles, then quote a theorem about entire functions.
:::

[[T-DB3DO]]

::: {.remark title="Where they appear"}
A meromorphic function is what the [[Complex_Analysis/counting-zeros/the-argument-principle|argument principle]] counts, and it is the natural class for [[Complex_Analysis/residues-and-contours/the-residue-theorem|the residue theorem]] -- the residue at a pole is defined by the Laurent expansion, and meromorphic says every singularity has one with finitely many negative terms.
:::
