---
schema: qual/card@1
id: P-GREPT-47
kind: problem
title: "Area between $(\\sin x+\\cos x)^4$ and $(\\sin x-\\cos x)^4$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 47 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
The curves $y = (\sin x + \cos x)^4$ and $y = (\sin x - \cos x)^4$ intersect at $x = 0$. If $a$ is the smallest positive value of $x$ at which these curves next intersect, determine the area between these curves from $x = 0$ to $x = a$.

(A) $2$
(B) $\pi$
(C) $4$
(D) $\frac{3\pi}{2}$
(E) $2\pi$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The two curves intersect exactly when
$$
\sin 2x=0.
$$


::: pf-proof

Let
$$
u=\sin x+\cos x,
\qquad
v=\sin x-\cos x.
$$
Since $u^4=v^4$ if and only if $u^2=v^2$, intersection is equivalent to
$$
0=u^2-v^2=(u-v)(u+v)=4\sin x\cos x=2\sin2x.
$$

:::

:::

::: {.pf-step #s1-2}

The smallest positive intersection after $x=0$ is
$$
a=\frac\pi2.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the intersections occur when $2x=k\pi$, hence when
$x=k\pi/2$. The smallest positive such value is $\pi/2$.

:::

:::

::: {.pf-step #s1-3}

On $0<x<\pi/2$, the difference between the first curve and the second
is
$$
4\sin2x>0.
$$


::: pf-proof

Using the notation from step [](#s1-1){.pf-ref},
$$
u^4-v^4=(u^2-v^2)(u^2+v^2).
$$
Now
$$
u^2-v^2=2\sin2x
$$
and
$$
u^2+v^2=2(\sin^2x+\cos^2x)=2.
$$
Thus the difference is $4\sin2x$, which is positive on
$(0,\pi/2)$.

:::

:::

::: {.pf-step #s1-4}

Therefore the area between the curves is
$$
\boxed{4},
$$
so the answer is (C).


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
\begin{aligned}
A
&=\int_0^{\pi/2}4\sin2x\,dx\\
&=\left[-2\cos2x\right]_0^{\pi/2}\\
&=4.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required area.

:::

:::

:::
