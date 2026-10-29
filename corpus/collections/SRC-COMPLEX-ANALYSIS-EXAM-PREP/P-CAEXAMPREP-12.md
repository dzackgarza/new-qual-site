---
schema: qual/card@1
id: P-CAEXAMPREP-12
kind: problem
title: Image of a first-quadrant hyperbolic region under squaring
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Let
$$
A=\{x+iy:xy>1,\ x>0,\ y>0\}.
$$
What is the image of $A$ under the map $f(z)=z^2$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $z=x+iy\in A$, then
$$
\operatorname{Im}(z^2)>2.
$$


::: pf-proof

For $z=x+iy$,
$$
z^2=(x^2-y^2)+2ixy.
$$
Since $z\in A$ means $xy>1$, it follows that
$$
\operatorname{Im}(z^2)=2xy>2.
$$
Thus
$$
f(A)\subseteq\{w:\operatorname{Im}w>2\}.
$$

:::

:::

::: {.pf-step #s1-2}

Every $w$ with $\operatorname{Im}w>2$ is equal to $z^2$ for some $z\in A$.


::: pf-proof

Let $w$ satisfy $\operatorname{Im}w>2$. Then $w\ne0$ and its argument may be chosen as $\theta\in(0,\pi)$. Write
$$
w=re^{i\theta},
\qquad r>0,
$$
and take
$$
z=\sqrt r\,e^{i\theta/2}=x+iy.
$$
Because $0<\theta/2<\pi/2$, one has $x>0$ and $y>0$. Moreover $z^2=w$, so
$$
2xy=\operatorname{Im}(z^2)=\operatorname{Im}w>2,
$$
hence $xy>1$. Therefore $z\in A$.

:::

:::

::: {.pf-step #s1-3}

The image is
$$
\boxed{f(A)=\{w\in\CC:\operatorname{Im}w>2\}}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives one inclusion and step [](#s1-2){.pf-ref} gives the reverse inclusion.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} determines the requested image.

:::

:::

:::
