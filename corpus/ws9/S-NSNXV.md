---
schema: qual/card@1
id: S-NSNXV
kind: solution
title: Solution to P-LCEHH
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - normal-subgroups
  - field-extensions
relations:
- kind: solves
  target: P-LCEHH
review: draft
---

:::{.solution}
By the Galois correspondence, we have
$$L \leftrightarrow \{e\}, \quad K \leftrightarrow H_2, \quad E \leftrightarrow H_1, \quad F \leftrightarrow D_4$$
and
- $E/F$ normal iff $H_1 \trianglelefteq D_4$
- $K/E$ normal iff $H_2 \trianglelefteq H_2$
- $K/F$ not normal iff $H_2 \not\trianglelefteq D_4$

So writing $D_4 = \langle \sigma,\tau \mid \sigma^4=\tau^2=e,\ \tau\sigma\tau^{-1}=\sigma^{-1}\rangle$, we can take $H_1 = \langle \sigma^2,\tau\rangle = \{e,\tau,\sigma^2,\tau\sigma^2\}$, then $[D_4:H_1]=2$ so $H_1 \trianglelefteq D_4$. We can then take $H_2 = \langle \tau\rangle = \{e,\tau\} \le H_1$. We have $H_2 \not\trianglelefteq D_4$, since e.g. if we write $\sigma=(1234), \tau=(24) \in S_n$, $\sigma\tau\sigma^{-1} = (13) \notin \langle \tau\rangle$.

But $H_2 \trianglelefteq H_1$, since $H_1 \cong \{e,\tau,\sigma^2,\tau\sigma^2\} = \{(),(24),(13)(24),(13)\}$, while
- $\tau\tau\tau^{-1} = \tau \in H_1$
- $\sigma^2\tau\sigma^{-2} = (\sigma\tau\sigma^{-1})^2 = (13)(13) = e \in H_1$
- $\tau\sigma^2\tau(\tau\sigma^2)^{-1} = (13)(24)(13) = (24) = \tau \in H_1$

So $hH_2h^{-1} = H_2\ \forall h \in H_1$ and thus $H_2 \trianglelefteq H_1$. So taking
$$H_1 = \langle \sigma^2,\tau\rangle, \qquad H_2 = \langle \tau\rangle$$
suffices. $\blacksquare$
:::
