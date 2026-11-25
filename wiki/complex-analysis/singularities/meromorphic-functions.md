---
title: Meromorphic functions
order: 30
topics:
- Meromorphic Functions
---

# Meromorphic functions

Recall that a [[D-7DFVJ|meromorphic function]] on an open set is holomorphic there except at poles, which form a set with no limit point in the open set.

[[D-7DFVJ]]

[[T-UBWL2]]

On the sphere the meromorphic functions are the rational functions: [[T-UBWL2]].

::: {.example title="$\tan z$ is meromorphic on $\CC$"}
The function $\tan z = \sin z/\cos z$ is a quotient of entire functions, and $\cos z$ has simple zeros exactly at $z = \pi/2+k\pi$, so those points are simple poles and there are no others: $\tan$ is [[D-7DFVJ|meromorphic]] on $\CC$.
At each of them $\cos'(z) = -\sin z = -(-1)^{k}$, so the residue is $\sin z/\cos'(z) = -1$ by [[C-Q6BSL|the rule for a residue at a simple zero of the denominator]].
:::

::: {.remark}
[[T-JXDQT|The argument principle]] counts zeros minus poles of a meromorphic function, and [[T-HRPNO|the residue theorem]] applies to meromorphic functions with finitely many poles in the region.
:::
