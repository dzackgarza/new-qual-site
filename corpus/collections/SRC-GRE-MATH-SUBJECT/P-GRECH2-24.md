---
schema: qual/card@1
id: P-GRECH2-24
kind: problem
title: Local maximum of $\int_{e^x}^{e^{2x}} t\log t\,dt$
classification:
  areas: [prelim]
  topics:
  - Fundamental Theorem of Calculus
  - Optimization
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 24 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. Both extractions garbled the limits of integration; the book's Chapter 8 solution integrates from e^x to e^(2x).
---

::: {.problem}
The function $f(x) = \int_{e^x}^{e^{2x}} t \log t \, dt$ has an absolute minimum at $x = 0$, and a local maximum at $x =$

(A) $-\log 4$
(B) $-\log 2$
(C) $\log 2$
(D) $1$
(E) $\log 4$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The derivative is
$$
f'(x)=x e^{2x}\left(4e^{2x}-1\right).
$$


::: pf-proof

By the fundamental theorem of calculus and the chain rule,
$$
\begin{aligned}
f'(x)
&=\left[e^{2x}\log(e^{2x})\right](2e^{2x})
-\left[e^x\log(e^x)\right]e^x\\
&=4xe^{4x}-xe^{2x}\\
&=xe^{2x}(4e^{2x}-1).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

The critical points are
$$
x=-\log2
\quad\text{and}\quad
x=0.
$$


::: pf-proof

Since $e^{2x}>0$, step [](#s1-1){.pf-ref} vanishes exactly when $x=0$ or
$$
4e^{2x}=1.
$$
The latter equation gives
$$
2x=\log\frac14=-2\log2,
$$
hence $x=-\log2$.

:::

:::

::: {.pf-step #s1-3}

$f$ has a local maximum at $x=-\log2$.


::: pf-proof

The factor $4e^{2x}-1$ is negative for $x<-\log2$ and positive for $x>-\log2$. Thus step [](#s1-1){.pf-ref} gives
$$
f'(x)>0\quad(x<-\log2),
$$
$$
f'(x)<0\quad(-\log2<x<0),
$$
and
$$
f'(x)>0\quad(x>0).
$$
Therefore $f'$ changes from positive to negative at $-\log2$, while it changes from negative to positive at $0$.

:::

:::

::: {.pf-step #s1-4}

The requested value is
$$
\boxed{-\log2},
$$
so the answer is (B).


::: pf-proof

Step [](#s1-3){.pf-ref} identifies the local maximum point among the two critical points.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
