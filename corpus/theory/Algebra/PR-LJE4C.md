---
schema: qual/card@1
id: PR-LJE4C
kind: proposition
title: Correspondence theorem for ideals
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Ideals
  - Rings
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a ring, $I \subseteq R$ a two-sided ideal, and $\phi\colon R \to R/I$ the quotient map.

(a) The maps $J \mapsto \bar{J} \coloneqq \phi(J) = J/I$ and $\bar{J} \mapsto \phi\inv(\bar{J})$ are mutually inverse inclusion-preserving bijections
$$
\begin{aligned}
\correspond{\text{ideals } J \subseteq R \text{ with } J \contains I}
&\mapstofrom
\correspond{\text{ideals of } R/I} \\
J &\mapsto J/I \\
\phi\inv(\bar J) &\mapsfrom \bar{J}.
\end{aligned}
$$
In particular, every ideal of $R/I$ is of the form $S/I$ for a unique ideal $S \subseteq R$ containing $I$.

(b) The same maps give a bijection between subrings $A \subseteq R$ containing $I$ and subrings of $R/I$.

(c) (Third isomorphism theorem.) For ideals $I \subseteq J \subseteq R$, there is a ring isomorphism
$$
\frac{R/I}{J/I} \cong \frac{R}{J}.
$$
:::
