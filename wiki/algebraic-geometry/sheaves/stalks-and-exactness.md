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

The gap between "surjective" and "surjective on sections" is the single most examined point in this topic, because it is where a student who has only memorised definitions gives the wrong answer.
The example makes the gap a number.

[[FE-Y12XB]]

[[FE-DNTT6]]

## What to say when asked where it fails

Lifting a global section of $\mch$ is possible over each member of some open cover, by the definition of surjectivity.
The lifts differ on overlaps by sections of $\mcf$, and those differences form a Čech $1$-cocycle.
The section lifts globally exactly when that cocycle is a coboundary, so the obstruction lives in $H^1(X, \mcf)$ and the long exact sequence
\[
0 \to \mcf(X) \to \mcg(X) \to \mch(X) \to H^1(X, \mcf) \to \cdots
\]
is the bookkeeping for it.
Everything in [[algebraic-geometry/cohomology/index|cohomology]] is downstream of this paragraph.
