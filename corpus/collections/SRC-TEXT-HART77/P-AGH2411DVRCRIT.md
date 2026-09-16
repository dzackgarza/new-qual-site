---
schema: qual/card@1
id: P-AGH2411DVRCRIT
kind: problem
title: Valuative criteria using discrete valuation rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Valuative Criteria
  - Discrete Valuation Rings
  - Krull-Akizuki
relations: []
review: draft
---

::: problem
If we are willing to do harder commutative algebra and stick to noetherian schemes, then the valuative criteria of separatedness and properness can be expressed using only **discrete** valuation rings.

a. If $\OO, \mfm$ is a noetherian local domain with quotient field $K$, and if $L$ is a finitely generated field extension of $K$, then there exists a discrete valuation ring $R$ of $L$ dominating $\OO$.
   Prove this in the following steps.

    - By taking a polynomial ring over $\OO$, reduce to the case where $L$ is a finite extension field of $K$.
    - Show that for a suitable choice of generators $x_1, \ldots, x_n$ of $\mfm$, the ideal $\mfa = (x_1)$ in $\OO' = \OO[x_2/x_1, \ldots, x_n/x_1]$ is not the unit ideal.
    - Let $\mfp$ be a minimal prime ideal of $\mfa$, and let $\OO'_\mfp$ be the localization of $\OO'$ at $\mfp$. This is a noetherian local domain of dimension $1$ dominating $\OO$.
    - Let $\widetilde{\OO'_\mfp}$ be the integral closure of $\OO'_\mfp$ in $L$. Use the Krull-Akizuki theorem (Nagata, p. 115) to show that $\widetilde{\OO'_\mfp}$ is noetherian of dimension $1$.
    - Finally, take $R$ to be a localization of $\widetilde{\OO'_\mfp}$ at one of its maximal ideals.

b. Let $f: X \to Y$ be a morphism of finite type of noetherian schemes.
   Show that $f$ is separated, respectively proper, if and only if the criterion of (4.3), respectively (4.7), holds for all discrete valuation rings.
:::
