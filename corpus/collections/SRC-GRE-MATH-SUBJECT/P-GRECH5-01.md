---
schema: qual/card@1
id: P-GRECH5-01
kind: problem
title: Nonuniqueness in a linear system
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 1 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
Two distinct solutions, $\mathbf{x}_1$ and $\mathbf{x}_2$, can be found to the linear system $A\mathbf{x} = \mathbf{b}$. Which of the following is necessarily true?

(A) $\mathbf{b} = \mathbf{0}$.
(B) $A$ is invertible.
(C) $A$ has more columns than rows.
(D) $\mathbf{x}_1 = -\mathbf{x}_2$.
(E) There exists a solution $\mathbf{x}$ such that $\mathbf{x} \neq \mathbf{x}_1$ and $\mathbf{x} \neq \mathbf{x}_2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The nonzero vector
$$
\mathbf{v}=\mathbf{x}_2-\mathbf{x}_1
$$
lies in the nullspace of $A$.


::: pf-proof

Since both vectors solve the system,
$$
A\mathbf{x}_1=\mathbf{b}
\qquad\text{and}\qquad
A\mathbf{x}_2=\mathbf{b}.
$$
Subtracting gives
$$
A(\mathbf{x}_2-\mathbf{x}_1)=\mathbf{0}.
$$
The solutions are distinct, so $\mathbf v\ne\mathbf0$.

:::

:::

::: {.pf-step #s1-2}

For every real number $t$,
$$
\mathbf{x}_1+t\mathbf{v}
$$
is also a solution.


::: pf-proof

By step [](#s1-1){.pf-ref} and linearity,
$$
A(\mathbf{x}_1+t\mathbf v)
=A\mathbf{x}_1+tA\mathbf v
=\mathbf b.
$$

:::

:::

::: {.pf-step #s1-3}

There is a solution distinct from both $\mathbf{x}_1$ and $\mathbf{x}_2$, so the answer is
$$
\boxed{\text{(E)}}.
$$


::: pf-proof

Take $t=2$ in step [](#s1-2){.pf-ref} and set
$$
\mathbf{x}=\mathbf{x}_1+2\mathbf v.
$$
Since $\mathbf v\ne0$, this vector differs from $\mathbf{x}_1$. Also
$$
\mathbf{x}_2=\mathbf{x}_1+\mathbf v,
$$
so $\mathbf x-\mathbf x_2=\mathbf v\ne0$. Thus $\mathbf x$ is a third distinct solution.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the necessarily true statement among the choices.

:::

:::

:::
