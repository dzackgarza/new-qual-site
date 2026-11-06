---
schema: qual/card@1
id: P-KAQ4G
kind: problem
title: $\int\frac{\sin x}{\cos^2 x}\,dx$ and $\int\csc(ax)\cot(ax)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
  - u-Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
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
    its answer: the two identities in step 1 were differentiated and the two displayed primitives checked against the printed integrands, on the intervals where each integrand is defined
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The two primitives are verified by differentiating the printed forms, using the derivatives of sec and csc.
---

::: {.problem}
Evaluate
$$
\int\frac{\sin x}{\cos^2x}\,dx
\qquad\text{and}\qquad
\int\csc(ax)\cot(ax)\,dx,
$$
where $a\ne0$.
:::

::: {.solution}

Write $\sec x=1/\cos x$, $\csc y=1/\sin y$, and $a\ne0$ throughout.

::: pf

::: {.pf-step #identities}

$\dfrac{\sin x}{\cos^2x}=\sec x\tan x$, $(\sec x)'=\sec x\tan x$, and
$(\csc(ax))'=-a\csc(ax)\cot(ax)$ wherever the functions are defined.

::: pf-proof

$\frac{\sin x}{\cos^2x}=\frac{1}{\cos x}\cdot\frac{\sin x}{\cos x}=\sec x\tan
x$. Differentiating $\sec x=(\cos x)^{-1}$ gives $-(\cos x)^{-2}(-\sin
x)=\frac{\sin x}{\cos^2x}=\sec x\tan x$. Differentiating
$\csc(ax)=(\sin(ax))^{-1}$ gives $-(\sin(ax))^{-2}\cdot
a\cos(ax)=-a\frac{\cos(ax)}{\sin^2(ax)}=-a\csc(ax)\cot(ax)$.

:::

:::

::: {.pf-step #first}

$\boxed{\displaystyle\int\frac{\sin x}{\cos^2x}\,dx=\sec x+C}$ on each
interval on which $\cos x\ne0$.

::: pf-proof

The integrand is $\sec x\tan x$ by step [](#identities){.pf-ref}, and that
step exhibits $\sec x$ as a primitive. The integrand is continuous on each
interval of $\{x:\cos x\ne0\}$ and those intervals are the connected
components of the domain, so the antiderivatives there are $\sec x$ plus a
constant.

:::

:::

::: {.pf-step #second}

$\boxed{\displaystyle\int\csc(ax)\cot(ax)\,dx=-\frac{1}{a}\csc(ax)+C}$ on each
interval on which $\sin(ax)\ne0$.

::: pf-proof

By step [](#identities){.pf-ref},
$\frac{d}{dx}\left(-\frac{1}{a}\csc(ax)\right)=-\frac{1}{a}\cdot(-a\csc(ax)\cot(ax))=\csc(ax)\cot(ax)$,
so the displayed function is a primitive; adding the constant covers all
primitives on each component of the domain.

:::

:::

:::


:::
