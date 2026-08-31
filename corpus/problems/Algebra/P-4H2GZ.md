---
schema: qual/card@1
id: P-4H2GZ
kind: problem
title: $C_H(x)=H\cap C_G(x)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
- Show that for $H\leq G$, $C_H(x) = H \intersect C_G(x)$.
:::

::: {.solution}
<1>1. $C_H(x) = \{h \in H : hx = xh\}$.
::: {.proof}
definition of the centralizer of $x$ in $H$.
:::

<1>2. $C_G(x) = \{g \in G : gx = xg\}$.
::: {.proof}
definition of the centralizer of $x$ in $G$.
:::

<1>3. $h \in C_H(x)$ iff $h \in H$ and $hx = xh$ iff $h \in H$ and $h \in C_G(x)$ iff $h \in H \cap C_G(x)$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Hence $C_H(x) = H \cap C_G(x)$.
::: {.proof}
<1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
