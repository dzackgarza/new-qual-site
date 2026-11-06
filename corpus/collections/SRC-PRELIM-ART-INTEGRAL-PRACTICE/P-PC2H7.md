---
schema: qual/card@1
id: P-PC2H7
kind: problem
title: Sum-to-product and product-to-sum identities for sine, cosine, and tangent
classification:
  areas:
  - prelim
  topics:
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-ART-INTEGRAL-PRACTICE has an empty provenance list, its own
    remark records that the drill sheet's original paper was not found, and
    searching assets/attachments/ and the migration records finds no copy of the
    sheet, so there is no page to read and the printed statement could not be
    compared with a source document. What was checked here is the statement and
    its answer: all seven identities re-derived from the addition formulas, with the domain restriction in (c) accounted for by the nonzero denominator
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. All seven identities derived from the four addition formulas by adding and subtracting them.
---

::: {.problem}
Prove the following identities for real $x,y$:

(a) $\cos x+\cos y=2\cos\frac{x+y}{2}\cos\frac{x-y}{2}$;

(b) $\cos x-\cos y=-2\sin\frac{x+y}{2}\sin\frac{x-y}{2}$;

(c) $\tan x-\tan y=\dfrac{\sin(x-y)}{\cos x\cos y}$ whenever $\cos x\cos y\ne0$;

(d) $\sin x\cos y=\frac12\bigl(\sin(x+y)+\sin(x-y)\bigr)$;

(e) $\cos x\sin y=\frac12\bigl(\sin(x+y)-\sin(x-y)\bigr)$;

(f) $\cos x\cos y=\frac12\bigl(\cos(x+y)+\cos(x-y)\bigr)$;

(g) $\sin x\sin y=-\frac12\bigl(\cos(x+y)-\cos(x-y)\bigr)$.
:::


::: {.solution}

Use the addition formulas $\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$ and
$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$, valid for all real angles.

::: pf

::: {.pf-step #cosine}

(a) and (b) hold for all real $x,y$.

::: pf-proof

Adding the two addition formulas for the cosine gives
$\cos(A+B)+\cos(A-B)=2\cos A\cos B$, and subtracting them gives
$\cos(A+B)-\cos(A-B)=-2\sin A\sin B$. Take $A=\frac{x+y}{2}$ and
$B=\frac{x-y}{2}$, so that $A+B=x$ and $A-B=y$; substituting in the two
identities gives exactly (a) and (b).

:::

:::

::: {.pf-step #tangent}

(c) holds whenever $\cos x\cos y\ne0$.

::: pf-proof

$\tan x-\tan y=\frac{\sin x}{\cos x}-\frac{\sin y}{\cos y}=\frac{\sin x\cos
y-\cos x\sin y}{\cos x\cos y}$ over the common denominator $\cos x\cos y$,
which is legitimate because it is nonzero; and the numerator is $\sin(x-y)$ by
the subtraction formula for the sine. So the identity holds wherever both
tangents are defined.

:::

:::

::: {.pf-step #sine-products}

(d), (e), (f) and (g) hold for all real $x,y$.

::: pf-proof

Adding and subtracting the sine addition formulas gives
$\sin(A+B)+\sin(A-B)=2\sin A\cos B$ and $\sin(A+B)-\sin(A-B)=2\cos A\sin B$;
with $A=x$, $B=y$ these are (d) and (e) after dividing by $2$. Adding and
subtracting the cosine formulas gives $\cos(A+B)+\cos(A-B)=2\cos A\cos B$,
which is (f), and $\cos(A-B)-\cos(A+B)=2\sin A\sin B$, which rearranges to (g)
as stated.

:::

:::

:::


:::
