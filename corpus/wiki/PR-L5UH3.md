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

:::{.proposition title="Right half-plane to Disc"}
\[
\HH_{R} &\mapstofrom \DD \\
\ts{ z \st \Re(z) > 0 } &\mapstofrom \ts{ w \st \abs{w} < 1 } \\
z &\mapsto {1-z \over 1+z} \\
{1-w\over 1+w} &\mapsfrom w
.\]

Just map the *right* half-plane $\HH_R$ to the disc $\DD$ by precomposing with a rotation $e^{i\pi/2} = i$:
\[
\HH_{R} \to \HH &\to \DD \\
z \mapsto iz &\mapsto {i- (iz) \over i + (iz)} = {i(1-z) \over i(1+z) } = {1-z \over 1+z}
.\]

This can easily be inverted:
\[
&\quad w = {1+z \over 1+z} \\
&\implies -(1-w) + z(w+1) = 0 \\
&\implies z = {1-w \over 1+w}
.\]

**Boundary behavior**:
Just a rotated version of $\HH\to \DD$!

> Mnemonic: every $z\in \HH_R$ is closed to 1 than $-1$.

:::
