---
schema: qual/card@1
id: PR-XCDL5
kind: proposition
title: "Log: Upper half-plane to horizontal strip"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.proposition title="Log: Upper half-plane to horizontal strip"}
\[
\HH &\mapstofrom \RR \cross (0, \pi) \\
\ts{ z \st \Im(z) > 0 } &\mapstofrom \ts{ w \st \Im(z) \in (0, \pi ) } \\
z &\mapsto \log(z) \\
e^w &\mapsfrom w
.\]

- Why this lands in a strip: use that $\arg(z) \in (0, \pi)$ and $\log(z) = \abs{z} + i\arg(z)$.

**Boundary behavior**:

- As $x$ travels from $-\infty \to 0$, $F(x)$ travels horizontally from $\infty + i\pi$ to $-\infty + i\pi$.
- As $x$ travels from $o\to \infty$, $F(x)$ travels from $-\infty\to\infty$ in $\RR$.

:::
