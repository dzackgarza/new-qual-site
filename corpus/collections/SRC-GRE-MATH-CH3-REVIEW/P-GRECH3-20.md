---
schema: qual/card@1
id: P-GRECH3-20
kind: problem
title: Maximum directional derivative from two directional derivatives
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
  note: "Checked against Chapter 3 review Question 20 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. Choice (C) reads as the digits 4 and 3 before the square root in both extractions."
---

::: {.problem}
Let $f(x,y)$ be a function that is differentiable everywhere. At a certain point $P$ in the $xy$-plane, the directional derivative of $f$ in the direction of $\hat{\mathbf{i}}-\hat{\mathbf{j}}$ is $\sqrt{2}$ and the directional derivative of $f$ in the direction of $\hat{\mathbf{i}}+\hat{\mathbf{j}}$ is $3\sqrt{2}$. What is the maximum directional derivative of $f$ at $P$?

(A) $3\sqrt{2}$
(B) $2\sqrt{5}$
(C) $4\,3\sqrt{2}$
(D) $6$
(E) $8$
:::

::: {.remark}
The source prints choice (C) as the digits $4$ and $3$ followed by $\sqrt{2}$, with no fraction bar.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The given directional derivatives imply
$$
f_x(P)-f_y(P)=2
\qquad\text{and}\qquad
f_x(P)+f_y(P)=6.
$$


::: pf-proof

The unit vectors in the stated directions are
$$
\mathbf{u}=\frac{(1,-1)}{\sqrt2},
\qquad
\mathbf{v}=\frac{(1,1)}{\sqrt2}.
$$
For a differentiable function,
$$
D_{\mathbf{u}}f(P)=\nabla f(P)\cdot\mathbf{u}
=\frac{f_x(P)-f_y(P)}{\sqrt2}.
$$
Since this equals $\sqrt2$, multiplication by $\sqrt2$ gives
$$
f_x(P)-f_y(P)=2.
$$
Similarly,
$$
D_{\mathbf{v}}f(P)
=\frac{f_x(P)+f_y(P)}{\sqrt2}
=3\sqrt2
$$
gives
$$
f_x(P)+f_y(P)=6.
$$

:::

:::

::: {.pf-step #s1-2}

The gradient at $P$ is
$$
\nabla f(P)=(4,2).
$$


::: pf-proof

Adding the two equations in step [](#s1-1){.pf-ref} gives $2f_x(P)=8$, hence $f_x(P)=4$. Subtracting them gives $2f_y(P)=4$, hence $f_y(P)=2$.

:::

:::

::: {.pf-step #s1-3}

The maximum directional derivative of $f$ at $P$ is
$$
\boxed{2\sqrt5},
$$
so the answer is (B).


::: pf-proof

For any unit vector $\mathbf{w}$,
$$
D_{\mathbf{w}}f(P)=\nabla f(P)\cdot\mathbf{w}
\le \|\nabla f(P)\|
$$
by the Cauchy--Schwarz inequality, with equality when $\mathbf{w}$ points in the direction of the gradient. By step [](#s1-2){.pf-ref},
$$
\|\nabla f(P)\|
=\sqrt{4^2+2^2}
=\sqrt{20}
=2\sqrt5.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested maximum directional derivative and corresponding choice.

:::

:::

:::
