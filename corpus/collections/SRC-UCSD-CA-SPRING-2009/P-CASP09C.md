---
schema: qual/card@1
id: P-CASP09C
kind: problem
title: "Partial fraction identity for four distinct complex numbers via residues"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Suppose that $\alpha, \beta, \gamma, \delta$ are distinct complex numbers.
Show that $$\frac{\alpha}{(\alpha - \beta)(\alpha - \gamma)(\alpha - \delta)} + \frac{\beta}{(\beta - \alpha)(\beta - \gamma)(\beta - \delta)} + \frac{\gamma}{(\gamma - \alpha)(\gamma - \beta)(\gamma - \delta)} + \frac{\delta}{(\delta - \alpha)(\delta - \beta)(\delta - \gamma)} = 0.$$

Hint: This is not an algebra qual.
:::

::: {.solution}
Consider
\[
R(z)=\frac{z}{(z-\alpha)(z-\beta)(z-\gamma)(z-\delta)}.
\]
Its residues at the four finite poles are exactly the four summands in the
displayed expression. Since
\[
R(z)=O(z^{-3})\qquad(z\to\infty),
\]
the residue at infinity is zero. The sum of all residues of a meromorphic
function on the Riemann sphere is zero, so the sum of the four finite residues
is zero. This is precisely the desired identity.
:::
