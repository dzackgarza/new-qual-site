---
title: Stalks and exactness
order: 2
topics:
- Stalks
- Exact Sequences
- Cohomology
---

# Stalks and exactness

The sheaf category is abelian, and every diagram-chasing word in it is defined stalk by stalk.
This is the payoff of the previous page and the entry to cohomology.

[[PR-C9ZEK]]

Surjectivity of sheaves does not imply surjectivity on global sections.
The example makes the obstruction explicit.

[[FE-Y12XB]]

[[FE-DNTT6]]

[[FE-SHFISOSTALKS]]

[[PR-SHFPUSHEX]]

## The obstruction to a global lift

Lifting a global section of $\mch$ is possible over each member of some open cover, by the definition of surjectivity.
The lifts differ on overlaps by sections of $\mcf$, and those differences form a Čech $1$-cocycle.
The section lifts globally exactly when that cocycle is a coboundary, so the obstruction lives in $H^1(X, \mcf)$ and the long exact sequence
\[
0 \to \mcf(X) \to \mcg(X) \to \mch(X) \to H^1(X, \mcf) \to \cdots
\]
is the bookkeeping for it.
Everything in [[algebraic-geometry/cohomology/index|cohomology]] is downstream of this paragraph.

## Locally constant and constructible sheaves

[[D-SHFLOCSYS]]

[[D-SHFCONSTR]]

## Support

[[D-UDIVH]]

The two notions of support are written similarly but behave differently: a fixed section can vanish on an open set while the whole stalk need not vanish there.
Extension by zero is the construction that lives in the gap, and coherence on a Noetherian scheme is the hypothesis that closes it.
