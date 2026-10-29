---
schema: qual/card@1
id: P-GRECH4-15
kind: problem
title: A solution of a first-order PDE
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 15 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
If $w = f(x, y)$ is a solution of the partial differential equation

$$
2\frac{\partial w}{\partial x} - 3\frac{\partial w}{\partial y} = 0
$$

then $w$ could equal

(A) $(2x - 3y)^6$
(B) $\sin[\log(3x - 2y)]$
(C) $e^{\arctan(3x + 2y)}$
(D) $[\arccos(2y - 3x)]^2$
(E) $\sqrt{2x + 3y}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If
$$
s=3x+2y,
$$
then
$$
2s_x-3s_y=0.
$$


::: pf-proof

The partial derivatives are $s_x=3$ and $s_y=2$, so
$$
2s_x-3s_y=2(3)-3(2)=0.
$$

:::

:::

::: {.pf-step #s1-2}

Every differentiable function of $s=3x+2y$ satisfies the PDE.


::: pf-proof

Let $w=H(s)$ for a differentiable one-variable function $H$. By the chain rule,
$$
w_x=H'(s)s_x,
\qquad
w_y=H'(s)s_y.
$$
Therefore, by step [](#s1-1){.pf-ref},
$$
2w_x-3w_y
=H'(s)(2s_x-3s_y)
=0.
$$

:::

:::

::: {.pf-step #s1-3}

The function
$$
\boxed{w=e^{\arctan(3x+2y)}}
$$
satisfies the PDE, so the answer is (C).


::: pf-proof

This function has the form $H(3x+2y)$ with
$$
H(s)=e^{\arctan s}.
$$
Hence step [](#s1-2){.pf-ref} applies.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies a listed solution of the given PDE.

:::

:::

:::
