---
schema: qual/card@1
id: PR-L5UH3
kind: proposition
title: Right half-plane to Disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

:::{.proposition}
\[
\HH_{R} &\mapstofrom \DD \\
\ts{ z \st \Re(z) > 0 } &\mapstofrom \ts{ w \st \abs{w} < 1 } \\
z &\mapsto {1-z \over 1+z} \\
{1-w\over 1+w} &\mapsfrom w
.\]
:::

::: {.proof}
Map the *right* half-plane $\HH_R$ to the disc $\DD$ by precomposing the standard map $\HH \to \DD$ with a rotation by $e^{i\pi/2} = i$:
\[
\HH_{R} \to \HH &\to \DD \\
z \mapsto iz &\mapsto {i- (iz) \over i + (iz)} = {i(1-z) \over i(1+z) } = {1-z \over 1+z}
.\]
The map $z \mapsto iz$ sends $\HH_R = \ts{z \st \Re z > 0}$ onto $\HH = \ts{w \st \Im w > 0}$ (multiplication by $i$ rotates the right half-plane onto the upper half-plane), and the standard Cayley map $w \mapsto \frac{i-w}{i+w}$ sends $\HH$ onto $\DD$.

To invert, solve $w = \frac{1-z}{1+z}$ for $z$:
\[
w(1+z) = 1-z \implies w + wz = 1 - z \implies z(w+1) = 1 - w \implies z = \frac{1-w}{1+w}.
\]
This is well-defined on $\DD$ since $w \neq -1$ for $|w| < 1$, and it maps $\DD$ back to $\HH_R$: for $w = u + iv$ with $u^2 + v^2 < 1$,
\[
\Re\left(\frac{1-w}{1+w}\right) = \frac{1 - |w|^2}{|1+w|^2} > 0.
\]

**Boundary behavior**: the boundary $\Re z = 0$ (the imaginary axis) maps to the unit circle $|w| = 1$, since for $z = it$ with $t \in \RR$,
\[
\left|\frac{1-it}{1+it}\right| = \frac{|1-it|}{|1+it|} = 1.
\]

> Mnemonic: every $z\in \HH_R$ is closer to $1$ than to $-1$, so $\left|\frac{1-z}{1+z}\right| < 1$.
:::
