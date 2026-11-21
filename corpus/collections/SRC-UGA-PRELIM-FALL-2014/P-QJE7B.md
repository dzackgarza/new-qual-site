---
schema: qual/card@1
id: P-QJE7B
kind: problem
title: $\{v_1+v_2,\, v_2-v_3,\, v_2+2v_3\}$ is a basis whenever $\{v_1,v_2,v_3\}$
  is
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's proof into numbered steps; the coordinate matrix, its determinant and
    the change-of-basis conclusion are unchanged. Checked: the three coordinate columns against
    the definitions of w_1, w_2, w_3, the determinant by expansion along the first row, and the
    invertibility argument. Not checked against a printed source: the UGA preliminary examinations
    are not retained in tmp/sources and the card records no page.
---

::: {.problem}
Let $v_1$, $v_2$, $v_3$ form a basis for a vector space $V$.
Prove that $v_1+v_2$, $v_2-v_3$, $v_2+2v_3$ form a basis for $V$.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $(v_1,v_2,v_3)$ is an ordered basis of $V$ and $w_1=v_1+v_2$, $w_2=v_2-v_3$, $w_3=v_2+2v_3$.

::: pf

::: {.pf-step #matrix}

The coordinate columns of $w_1,w_2,w_3$ in $(v_1,v_2,v_3)$ are $(1,1,0)^{t}$, $(0,1,-1)^{t}$ and $(0,1,2)^{t}$, so the coordinate matrix is $A=\begin{pmatrix}1&0&0\\1&1&1\\0&-1&2\end{pmatrix}$.

::: pf-proof

Read off the coefficients: $w_1=1\cdot v_1+1\cdot v_2+0\cdot v_3$, $w_2=0\cdot v_1+1\cdot v_2-1\cdot v_3$, $w_3=0\cdot v_1+1\cdot v_2+2\cdot v_3$.

:::

:::

::: {.pf-step #det}

$\det A=3\neq0$.

::: pf-proof

Expanding along the first row, $\det A=1\cdot(1\cdot2-1\cdot(-1))=3$.

:::

:::

::: {.pf-step #done}

$(w_1,w_2,w_3)$ is a basis of $V$.

::: pf-proof

A family whose coordinate matrix in a basis is invertible is a basis: if $\sum c_iw_i=0$, then $A(c_1,c_2,c_3)^{t}=0$, so $(c_1,c_2,c_3)=0$; and three independent vectors in a space of dimension three span it.

:::

:::

:::

:::
