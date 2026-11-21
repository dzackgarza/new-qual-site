---
schema: qual/card@1
id: FT-FZERI
kind: theorem
title: 'Symmetric Rouché theorem on a disc: $\abs{f-g}<\abs f+\abs g$ on the circle'
slogan: 'If $\abs{f-g}<\abs{f}+\abs{g}$ on the boundary circle, then $f$ and $g$ have the same number of zeros in the disc.'
prompts:
- What does Rouché's theorem conclude about the zero counts of $f$ and $g$?
- State Rouché's theorem in its symmetric form.
- State Rouché's theorem on a closed disc $\abs{z - z_0} \leq R$.
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
---

::: {.theorem}
Let $D=\theset{z : \abs{z-z_0}<R}$, and let $f,g$ be [[D-E7A5W|holomorphic]] on an open set containing $\overline D$.
If $\abs{f(z) - g(z)} < \abs{f(z)} + \abs{g(z)}$ for all $z\in\bd D$, then $f$ and $g$ are nonvanishing on $\bd D$ and have the same number of [[D-65VIK|zeros]] in $D$, counted with multiplicity.

This is item 25 of §3 of Robert Won, *Complex Analysis Qual Sheet* (`assets/attachments/Won_-_Complex_Analysis_Qual_Sheet.pdf`): for $f,g$ meromorphic on a region and a closed curve $\gamma$ on which $\abs{f(z)+g(z)}<\abs{f(z)}+\abs{g(z)}$, one has $Z_f-P_f=Z_g-P_g$. Replacing $g$ by $-g$ gives the hypothesis above, and for holomorphic $f,g$ both pole counts are zero, so the common value is the number of zeros in $D$; the inequality itself forces $f$ and $g$ to be nonzero on $\bd D$.
:::
