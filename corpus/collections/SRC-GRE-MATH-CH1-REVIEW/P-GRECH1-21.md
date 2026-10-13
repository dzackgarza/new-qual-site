---
schema: qual/card@1
id: P-GRECH1-21
kind: problem
title: Evaluate $\cos(-\sin x)$ given $\sin(\sin x)=1/2$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 21 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Let $x$ be the real number such that $\sin(\sin x) = \frac{1}{2}$ and $2 < x < 3$. What's the value of $\cos(-\sin x)$?

(A) $-\sqrt{1 - \left(\frac{\pi}{6}\right)^2}$
(B) $\sqrt{1 - \left(\frac{\pi}{3}\right)^2}$
(C) $\sqrt{1 - \left(\frac{\pi}{6}\right)^2}$
(D) $-\frac{\sqrt{3}}{2}$
(E) $\frac{\sqrt{3}}{2}$
:::

::: {.solution}
Set $\theta=\sin x$.

<1>1. $0<\theta<1$, and hence $\cos\theta>0$.

::: {.proof}
Since $2<x<3<\pi$, the angle $x$ lies in $(0,\pi)$, so $\sin x>0$. Also $x>2>\pi/2$, so $x\ne\pi/2$ and therefore $\sin x<1$. Thus $0<\theta<1<\pi/2$, which implies $\cos\theta>0$.
:::

<1>2. $\cos\theta=\frac{\sqrt3}{2}$.

::: {.proof}
The hypothesis gives $\sin\theta=1/2$. Hence
$$
\cos^2\theta=1-\sin^2\theta
=1-\frac14
=\frac34.
$$
By the positivity from step <1>1,
$$
\cos\theta=\frac{\sqrt3}{2}.
$$
:::

<1>3. The requested value is
$$
\boxed{\cos(-\sin x)=\frac{\sqrt3}{2}},
$$
so the answer is (E).

::: {.proof}
Cosine is even, so
$$
\cos(-\sin x)=\cos(\sin x)=\cos\theta.
$$
Apply step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested value and corresponding choice.
:::
:::
