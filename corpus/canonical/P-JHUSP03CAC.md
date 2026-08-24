---
schema: qual/card@1
id: P-JHUSP03CAC
kind: problem
title: Argument principle to determine zeros in a region
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
solved: false
relations: []
review: draft
---

Let $C$ be the closed curve defined by two pieces: the first piece is given by the set of all $z$ satisfying $|z - 1| = 3$ and $\operatorname{Re}(z - 1) \geq 0$.
The second piece is the straight line segment from $1 + 3i$ to $1 - 3i$.
Orient $C$ in the counterclockwise direction, and let $\Omega$ be the region enclosed by $C$.
Suppose $f$ is holomorphic in a neighborhood of $\overline{\Omega}$ with no zeros on $C$.
Suppose also that:

$$\frac{1}{2\pi i} \int_C \frac{zf'(z)}{f(z)} \, dz = 3 \qquad \text{and} \qquad \frac{1}{2\pi i} \int_C \frac{z^2 f'(z)}{f(z)} \, dz = \frac{5}{2}.$$

Determine all the zeros of $f$ in $\Omega$ explicitly.
