---
schema: qual/card@1
id: P-GREPT-12
kind: problem
title: "Volume of revolution of one arch of $y=\\sin x$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 12 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If one arch of the curve $y = \sin x$ is revolved around the $x$-axis, what's the volume of the generated solid?

(A) $\frac{\pi^2}{4}$
(B) $\frac{\pi^2}{2}$
(C) $2\pi$
(D) $\pi^2$
(E) $2\pi^2$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Taking the arch on $[0,\pi]$, the volume of revolution is
$$
V=\pi\int_0^\pi \sin^2x\,dx.
$$


::: pf-proof

On one arch of $y=\sin x$, namely $0\le x\le\pi$, revolving the graph about
the $x$-axis produces disks of radius $\sin x$. The disk method therefore
gives
$$
V=\int_0^\pi \pi(\sin x)^2\,dx.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\int_0^\pi\sin^2x\,dx=\frac\pi2.
$$


::: pf-proof

Using
$$
\sin^2x=\frac{1-\cos2x}{2},
$$
we obtain
$$
\int_0^\pi\sin^2x\,dx
=\frac12\left[x-\frac12\sin2x\right]_0^\pi
=\frac\pi2.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the volume is
$$
V=\boxed{\frac{\pi^2}{2}},
$$
so the answer is (B).


::: pf-proof

Substituting step [](#s1-2){.pf-ref} into the formula of step [](#s1-1){.pf-ref} gives
$$
V=\pi\cdot\frac\pi2=\frac{\pi^2}{2}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required volume.

:::

:::

:::
