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
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source did not say where x lies; the statement now takes x in G.'
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (already
    repaired on 2026-10-29 to place x in G; nothing further needed), and the existing
    prose against a fresh re-derivation: both $C_G(x)$ and the set of h in H
    commuting with x are subgroups, by the standard closedness computations; and for
    h in G membership in the latter is equivalent to h in H and h in C_G(x), which is
    membership in the intersection. Correct. The prose gave the equivalence in one
    line; the proof states the two conditions separately and records that the
    conclusion is an equality of subgroups, not only of sets. No source solution is
    retained for this card, so no source comparison was made. What was not checked:
    any printed source.
---

::: {.problem}
Show that for $H\leq G$ and $x\in G$, $C_H(x) = H \intersect C_G(x)$.
:::

::: {.solution}
Let $G$ be a group, $H\leq G$ a subgroup and $x\in G$; write $C_G(x)=\theset{g\in G:gx=xg}$ for the centralizer of $x$ in $G$, and $C_H(x)=C_G(x)\cap H$ for its analogue in $H$, where the second description is the statement to be proved.

::: pf

::: {.pf-step #definitions}
$C_G(x)=\theset{g\in G:gx=xg}$ is a subgroup of $G$ and $C_H(x)=\theset{h\in H:hx=xh}$ is a subgroup of $H$.

::: pf-proof
$C_G(x)$ contains $e$ because $ex=x=xe$; if $gx=xg$ then multiplying on the left and right by $g^{-1}$ gives $xg^{-1}=g^{-1}x$, so $g^{-1}\in C_G(x)$; and if $gx=xg$ and $hx=xh$ then $(gh)x=g(hx)=g(xh)=(gx)h=(xg)h=x(gh)$, so $C_G(x)$ is closed under multiplication. The same computations with $h,k\in H$ show that $\theset{h\in H:hx=xh}$ is a subgroup of $H$, since $H$ contains $e$ and is closed under inverses and products.
:::

:::

::: {.pf-step #elementwise}
For every $h\in G$: $h\in\theset{h\in H:hx=xh}$ if and only if $h\in H\cap C_G(x)$.

::: pf-proof
Both sides say exactly two things about $h$: that $h\in H$, and that $h$ commutes with $x$. Formally, $h$ lies in the first set iff $h\in H$ and $hx=xh$; and $h$ lies in $H\cap C_G(x)$ iff $h\in H$ and $h\in C_G(x)$, which by step [](#definitions){.pf-ref} means $h\in H$ and $hx=xh$. The two conditions are identical.
:::

:::

::: {.pf-step}
$C_H(x)=H\cap C_G(x)$.

::: pf-proof
Two sets with the same elements are equal, and step [](#elementwise){.pf-ref} says that membership in $C_H(x)$ and in $H\cap C_G(x)$ agree for every $h\in G$. Since $H\cap C_G(x)$ is a subset of $H$ and is closed under the group operations as an intersection of subgroups of $G$ contained in $H$, the two sets are equal subgroups of $H$, not merely equal sets.
:::

:::

:::
:::
