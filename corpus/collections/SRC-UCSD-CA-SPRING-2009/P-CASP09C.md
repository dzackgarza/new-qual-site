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
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each step re-read: the four residues are computed at simple
      poles; the decay R = O(z^{-3}) kills the residue at infinity, and the residue at infinity is
      minus the z^{-1} coefficient; and the sum of all residues on the sphere vanishes. The
      argument uses only that the four numbers are distinct, which is what makes every pole
      simple. Not claimed: the polynomial identity obtained by clearing denominators, which is a
      different (algebraic) proof.
---

::: {.problem}
Suppose that $\alpha, \beta, \gamma, \delta$ are distinct complex numbers.
Show that $$\frac{\alpha}{(\alpha - \beta)(\alpha - \gamma)(\alpha - \delta)} + \frac{\beta}{(\beta - \alpha)(\beta - \gamma)(\beta - \delta)} + \frac{\gamma}{(\gamma - \alpha)(\gamma - \beta)(\gamma - \delta)} + \frac{\delta}{(\delta - \alpha)(\delta - \beta)(\delta - \gamma)} = 0.$$

Hint: This is not an algebra qual.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source. The printed hint says this is not an algebra problem, and the residue argument is the intended route.

::: pf

::: {.pf-step #function}
Let $R(z)=\dfrac{z}{(z-\alpha)(z-\beta)(z-\gamma)(z-\delta)}$.

::: pf-proof
This is a definition; $R$ is meromorphic on the Riemann sphere with simple poles exactly at the four distinct numbers $\alpha,\beta,\gamma,\delta$ and no other singularities.
:::

:::

::: {.pf-step #residues}
The residues of $R$ at $\alpha,\beta,\gamma,\delta$ are the four summands of the displayed expression.

::: pf-proof
At a simple pole $z=p$ the residue is $\lim_{z\to p}(z-p)R(z)$. For $p=\alpha$ this gives $\alpha\big/\bigl((\alpha-\beta)(\alpha-\gamma)(\alpha-\delta)\bigr)$, and the three other cases are the same with the letters permuted.
:::

:::

::: {.pf-step #infinity}
The residue of $R$ at infinity is zero.

::: pf-proof
$R(z)=z/z^{4}\cdot(1+O(1/z))=O(z^{-3})$ as $z\to\infty$; the residue at infinity is minus the coefficient of $z^{-1}$ in the Laurent expansion there, and a function of order $O(z^{-3})$ has no $z^{-1}$ term, so the residue vanishes.
:::

:::

::: {.pf-step #sum}
The sum of all residues of $R$ on the Riemann sphere is zero.

::: pf-proof
The sum of the residues of a meromorphic function on the sphere is zero: this follows from the residue theorem applied to a large circle, whose integral tends to $0$ because $R$ decays like $z^{-3}$ while the circumference grows like $R$.
:::

:::

::: {.pf-step}
The displayed sum is zero.

::: pf-proof
By steps [](#residues){.pf-ref}, [](#infinity){.pf-ref} and [](#sum){.pf-ref}, the sum of the four finite residues, which is the displayed expression, equals minus the residue at infinity, namely $0$:
$$
\boxed{\frac{\alpha}{(\alpha-\beta)(\alpha-\gamma)(\alpha-\delta)}+\frac{\beta}{(\beta-\alpha)(\beta-\gamma)(\beta-\delta)}+\frac{\gamma}{(\gamma-\alpha)(\gamma-\beta)(\gamma-\delta)}+\frac{\delta}{(\delta-\alpha)(\delta-\beta)(\delta-\gamma)}=0.}
$$
:::

:::

:::
:::
