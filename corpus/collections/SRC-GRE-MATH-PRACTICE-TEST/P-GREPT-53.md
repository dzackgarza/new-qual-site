---
schema: qual/card@1
id: P-GREPT-53
kind: problem
title: "Image of a point under a linear map of the plane given on two points"
classification:
  areas: [applied-algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 53 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $T\colon \RR^2 \to \RR^2$ be the linear transformation that maps the point $(1, 2)$ to $(2, 3)$ and the point $(-1, 2)$ to $(2, -3)$. Then $T$ maps the point $(2, 1)$ to

(A) $(1, 6)$
(B) $(-1, 4)$
(C) $(3, 2)$
(D) $(-4, 3)$
(E) $(-3, 1)$
:::

::: {.solution}

::: pf

::: pf-step

The vectors
$$
\mathbf a=(1,2),
\qquad
\mathbf b=(-1,2)
$$
form a basis of $\RR^2$.


::: pf-proof

The determinant of the matrix with columns $\mathbf a,\mathbf b$ is
$$
\det\begin{pmatrix}1&-1\\2&2\end{pmatrix}=4\ne0,
$$
so the vectors are linearly independent and hence form a basis.

:::

:::

::: pf-step

The vector $(2,1)$ has the basis expansion
$$
(2,1)=\frac54\mathbf a-\frac34\mathbf b.
$$


::: pf-proof

Indeed,
$$
\frac54(1,2)-\frac34(-1,2)
=\left(\frac54+\frac34,\frac{10}4-\frac64\right)
=(2,1).
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
T(2,1)=\boxed{(1,6)},
$$
so the answer is (A).


::: pf-proof

By linearity and the given values of $T$,
$$
\begin{aligned}
T(2,1)
&=\frac54T(1,2)-\frac34T(-1,2)\\
&=\frac54(2,3)-\frac34(2,-3)\\
&=(1,6).
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required image.

:::

:::

:::
