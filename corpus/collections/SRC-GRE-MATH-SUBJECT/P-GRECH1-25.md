---
schema: qual/card@1
id: P-GRECH1-25
kind: problem
title: "Exact value of $\\arctan1+\\arctan2+\\arctan3$"
classification:
  areas:
  - algebra
  topics:
  - Inverse Trigonometric Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 25 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Determine the exact value of the sum $\arctan 1 + \arctan 2 + \arctan 3$.

(A) $\frac{\pi}{2}$
(B) $\pi$
(C) $\frac{3\pi}{2}$
(D) $\frac{\pi}{4}-1$
(E) $\frac{\pi}{2}-1$
:::

::: {.solution}

Set $\alpha=\arctan 2$ and $\beta=\arctan 3$.

::: pf

::: {.pf-step #s1-1}

$\alpha+\beta=\frac{3\pi}{4}$.


::: pf-proof

Since $2,3>0$, one has
$$
0<\alpha<\frac\pi2,
\qquad
0<\beta<\frac\pi2,
$$
so $0<\alpha+\beta<\pi$. The tangent addition formula gives
$$
\tan(\alpha+\beta)
=\frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}
=\frac{2+3}{1-6}
=-1.
$$
The unique angle in $(0,\pi)$ with tangent $-1$ is $3\pi/4$.

:::

:::

::: {.pf-step #s1-2}

The requested sum is
$$
\boxed{\pi},
$$
so the answer is (B).


::: pf-proof

The principal value satisfies $\arctan1=\pi/4$. Combining this with step [](#s1-1){.pf-ref} gives
$$
\arctan1+\arctan2+\arctan3
=\frac\pi4+\frac{3\pi}{4}
=\pi.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested exact value and corresponding choice.

:::

:::

:::
