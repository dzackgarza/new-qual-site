---
schema: qual/card@1
id: P-GRECH3-13
kind: problem
title: Cyclic product of thermodynamic partial derivatives
classification:
  areas:
  - real-analysis
  topics:
  - Partial Derivatives
  - Implicit Differentiation
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 13 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. The chapter-3.pdf extraction wrote a lowercase p in two partial derivatives; the book extraction and its solution write P."
---

::: {.problem}
If the variables $P$, $V$, and $T$ are related by the equation $PV=nRT$, where $n$ and $R$ are constants, simplify the expression
$$
\frac{\partial V}{\partial T}\cdot\frac{\partial T}{\partial P}\cdot\frac{\partial P}{\partial V}.
$$

(A) $-1$
(B) $1$
(C) $-nR$
(D) $nR$
(E) $\frac{1}{nR}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Holding $P$ fixed,
$$
\left(\frac{\partial V}{\partial T}\right)_P=\frac{nR}{P}.
$$


::: pf-proof

From $PV=nRT$,
$$
V=\frac{nRT}{P}.
$$
Differentiating with respect to $T$ while $P$ is fixed gives the displayed derivative.

:::

:::

::: {.pf-step #s1-2}

Holding $V$ fixed,
$$
\left(\frac{\partial T}{\partial P}\right)_V=\frac{V}{nR}.
$$


::: pf-proof

Solving the relation for $T$ gives
$$
T=\frac{PV}{nR}.
$$
Differentiating with respect to $P$ while $V$ is fixed gives the displayed derivative.

:::

:::

::: {.pf-step #s1-3}

Holding $T$ fixed,
$$
\left(\frac{\partial P}{\partial V}\right)_T=-\frac{nRT}{V^2}.
$$


::: pf-proof

Solving the relation for $P$ gives
$$
P=\frac{nRT}{V}.
$$
Differentiating with respect to $V$ while $T$ is fixed yields
$$
\left(\frac{\partial P}{\partial V}\right)_T
=-\frac{nRT}{V^2}.
$$

:::

:::

::: {.pf-step #s1-4}

The cyclic product is
$$
\boxed{-1},
$$
so the answer is (A).


::: pf-proof

Multiplying the derivatives from steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} gives
$$
\frac{nR}{P}\cdot\frac{V}{nR}\cdot
\left(-\frac{nRT}{V^2}\right)
=-\frac{nRT}{PV}.
$$
The defining relation $PV=nRT$ therefore reduces this expression to $-1$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the simplified value and corresponding choice.

:::

:::

:::
