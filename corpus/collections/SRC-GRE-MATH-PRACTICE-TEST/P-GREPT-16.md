---
schema: qual/card@1
id: P-GREPT-16
kind: problem
title: "$(\\partial\\theta/\\partial r)_x$ in polar coordinates"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 16 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $x = r \cos \theta$ and $y = r \sin \theta$. Which of the following expressions is equal to $\left(\frac{\partial \theta}{\partial r}\right)_x$, the partial derivative of $\theta$ with respect to $r$, keeping $x$ constant?

(A) $r^{-1} \tan \theta$
(B) $-r^{-1} \tan \theta$
(C) $r^{-1} \cot \theta$
(D) $-r^{-1} \cot \theta$
(E) $-r^{-1} \csc \theta$
:::

::: pf

::: pf-step

Keeping $x$ constant gives
$$
r\cos\theta=x=\text{constant}.
$$


::: pf-proof

This is the defining polar-coordinate relation for $x$, with the condition in
the problem that $x$ is held fixed while $r$ varies.

:::

:::

::: pf-step

Differentiating the relation in step <1>1 with respect to $r$ gives
$$
\cos\theta-r\sin\theta
\left(\frac{\partial\theta}{\partial r}\right)_x=0.
$$


::: pf-proof

Apply the product rule to $r\cos\theta$, remembering that $\theta$ depends on
$r$ when $x$ is held constant:
$$
\frac{d}{dr}(r\cos\theta)
=\cos\theta-r\sin\theta
\left(\frac{\partial\theta}{\partial r}\right)_x.
$$
The derivative of the constant $x$ is zero.

:::

:::

::: pf-step

Therefore
$$
\left(\frac{\partial\theta}{\partial r}\right)_x
=\boxed{r^{-1}\cot\theta},
$$
so the answer is (C).


::: pf-proof

Solving the equation in step <1>2 for the partial derivative gives
$$
\left(\frac{\partial\theta}{\partial r}\right)_x
=\frac{\cos\theta}{r\sin\theta}
=r^{-1}\cot\theta.
$$

:::

:::

::: pf-qed

Step <1>3 gives the required expression.

:::

:::
