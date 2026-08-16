---
schema: qual/card@1
id: E-FODKS
kind: exercise
title: "Let $I \\normal R$, then since $R$ is a PID we have $I = (b)$ for some\u2026"
classification:
  areas:
  - algebra
  topics:
  - principal-ideal-domains
  - ideals
  - factorization
relations: []
review: draft
---

::: exercise
Let $I \normal R$, then since $R$ is a PID we have $I = (b)$ for some $b\in R$.
We can write $(b) = Rb$; if $a\in I$ is an irreducible element, we'd like to show that $Rb = Ra$.

Note that since $a \in (b)$, we have $(a) \subseteq (b)$ and thus $Ra \subseteq Rb$.

Since $a\in Rb$, we have $a = rb$ for some $r\in R$.
Since $a$ is irreducible, either $r$ is a unit or $b$ is a unit.

If $r$ is a unit, then $a = rb \implies r\inv a = b$.
But then $x\in Rb \implies x = r'b = r'r\inv a \in Ra$, so $Rb \subseteq Ra$ and thus $Ra = Rb = I$.

Otherwise, if $b$ is a unit, $a = rb \implies Ra = R$.
But any ideal containing a unit is the entire ring, so $Rb = (b) = R$ as well, so again $Ra = I$.
:::
