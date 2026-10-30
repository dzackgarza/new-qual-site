---
schema: qual/card@1
id: P-GREPT-11
kind: problem
title: "A vector $\\mathbf a$ with $\\mathbf a\\cdot[(\\mathbf a+\\mathbf c)\\times\\mathbf b]=12$"
classification:
  areas: [prelim]
  topics:
  - Cross Product
  - Triple Product
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 11 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $\hat{\mathbf{i}} = (1, 0, 0)$, $\hat{\mathbf{j}} = (0, 1, 0)$, and $\hat{\mathbf{k}} = (0, 0, 1)$. If $\mathbf{b}$ and $\mathbf{c}$ are vectors such that $\norm{\mathbf{b}} = 3$, $\mathbf{b} \cdot \mathbf{c} = 5$, $\norm{\mathbf{c}} = 7$, and $\mathbf{b} \times \mathbf{c} = 8\hat{\mathbf{j}} + 4\hat{\mathbf{k}}$, which of the following vectors satisfies the equation $\mathbf{a} \cdot [(\mathbf{a} + \mathbf{c}) \times \mathbf{b}] = 12$?

(A) $\mathbf{a} = 2\hat{\mathbf{i}} + \hat{\mathbf{j}} - 2\hat{\mathbf{k}}$
(B) $\mathbf{a} = \hat{\mathbf{i}} - \hat{\mathbf{j}} + 2\hat{\mathbf{k}}$
(C) $\mathbf{a} = \hat{\mathbf{i}} - 2\hat{\mathbf{j}} + \hat{\mathbf{k}}$
(D) $\mathbf{a} = 2\hat{\mathbf{i}} - \hat{\mathbf{j}} + \hat{\mathbf{k}}$
(E) $\mathbf{a} = \hat{\mathbf{i}} + 2\hat{\mathbf{j}} - 2\hat{\mathbf{k}}$
:::

::: {.remark}
No vectors satisfy all four printed conditions. Lagrange's identity gives
$$
\norm{\mathbf b\times\mathbf c}^2
=\norm{\mathbf b}^2\norm{\mathbf c}^2-(\mathbf b\cdot\mathbf c)^2
=9\cdot49-25
=416,
$$
while $\norm{8\hat{\mathbf j}+4\hat{\mathbf k}}^2=80$. The solution below uses only the value of $\mathbf b\times\mathbf c$, so its answer (C) is the answer for any $\mathbf b,\mathbf c$ with $\mathbf b\times\mathbf c=8\hat{\mathbf j}+4\hat{\mathbf k}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The equation
$$
\mathbf a\cdot[(\mathbf a+\mathbf c)\times\mathbf b]=12
$$
is equivalent to
$$
\mathbf a\cdot(\mathbf c\times\mathbf b)=12.
$$


::: pf-proof

By bilinearity of the cross product and linearity of the dot product,
$$
\mathbf a\cdot[(\mathbf a+\mathbf c)\times\mathbf b]
=\mathbf a\cdot(\mathbf a\times\mathbf b)
+\mathbf a\cdot(\mathbf c\times\mathbf b).
$$
The vector $\mathbf a\times\mathbf b$ is perpendicular to $\mathbf a$, so
the first dot product is $0$.

:::

:::

::: {.pf-step #s1-2}

Writing
$$
\mathbf a=a_1\hat{\mathbf i}+a_2\hat{\mathbf j}+a_3\hat{\mathbf k},
$$
the equation from step [](#s1-1){.pf-ref} becomes
$$
-8a_2-4a_3=12.
$$


::: pf-proof

Since
$$
\mathbf b\times\mathbf c=8\hat{\mathbf j}+4\hat{\mathbf k},
$$
antisymmetry of the cross product gives
$$
\mathbf c\times\mathbf b=-8\hat{\mathbf j}-4\hat{\mathbf k}.
$$
Taking the dot product with $\mathbf a$ yields
$\mathbf a\cdot(\mathbf c\times\mathbf b)=-8a_2-4a_3$.

:::

:::

::: {.pf-step #s1-3}

Among the five choices, only
$$
\boxed{\mathbf a=\hat{\mathbf i}-2\hat{\mathbf j}+\hat{\mathbf k}}
$$
satisfies the equation, so the answer is (C).


::: pf-proof

For choices (A)--(E), the pairs $(a_2,a_3)$ are respectively
$$
(1,-2),\ (-1,2),\ (-2,1),\ (-1,1),\ (2,-2).
$$
The corresponding values of $-8a_2-4a_3$ are
$$
0,\ 0,\ 12,\ 4,\ -8.
$$
Thus only choice (C) satisfies step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required vector.

:::

:::

:::
