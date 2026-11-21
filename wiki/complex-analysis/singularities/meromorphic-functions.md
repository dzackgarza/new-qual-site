---
title: Meromorphic functions
order: 30
topics:
- Meromorphic Functions
- Mittag-Leffler Theorem
- Partial Fractions
---

# Meromorphic functions

A meromorphic function on an open set is holomorphic except on a discrete set, at each point of which it has a pole.

[[D-7DFVJ]]

[[T-UBWL2]]

A meromorphic function on $\CC$ that is holomorphic or has a pole at $\infty$ is a rational function, and every rational function is of this form [@SS03, ch. 3, Theorem 3.4].

[[T-DB3DO]]

::: {.example title="$\tan z$ is meromorphic on $\CC$"}
The function $\tan z = \sin z/\cos z$ is a quotient of entire functions, and $\cos z$ has simple zeros exactly at $z = \pi/2+k\pi$, so those points are simple poles and there are no others: $\tan$ is [[D-7DFVJ|meromorphic]] on $\CC$.
At each of them $\cos'(z) = -\sin z = -(-1)^{k}$, so the residue is $\sin z/\cos'(z) = -1$ by [[C-Q6BSL|the rule for a residue at a simple zero of the denominator]].
:::

::: {.remark}
The [[complex-analysis/counting-zeros/the-argument-principle|argument principle]] counts zeros minus poles of a meromorphic function, and [[complex-analysis/residues-and-contours/the-residue-theorem|the residue theorem]] applies to meromorphic functions with finitely many poles in the region, where each residue is the coefficient $c_{-1}$ of a Laurent series with finitely many negative terms.
:::
