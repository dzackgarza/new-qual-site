---
schema: qual/card@1
id: P-GRECH3-26
kind: problem
title: Line integral along an astroid arc
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
  note: "Checked against Chapter 3 review Question 26 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Let $C$ be the portion of the astroid $x^{2/3}+y^{2/3}=1$ from $(1,0)$ to $(0,1)$, which can be parameterized by the equations
$$
x=\cos^3 t,\quad y=\sin^3 t
$$
as $t$ increases from $0$ to $\frac{\pi}{2}$. Evaluate the integral:
$$
\int_C(y\cos xy-1)\,dx+(1+x\cos xy)\,dy
$$

(A) $-2$
(B) $-1$
(C) $1$
(D) $\frac{1}{2}\pi-1$
(E) $2$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The integrand is the exact differential of
$$
\Phi(x,y)=\sin(xy)-x+y.
$$


::: pf-proof

The partial derivatives of $\Phi$ are
$$
\Phi_x=y\cos(xy)-1,
\qquad
\Phi_y=x\cos(xy)+1.
$$
Therefore
$$
d\Phi
=(y\cos xy-1)\,dx+(1+x\cos xy)\,dy,
$$
which is exactly the integrand.

:::

:::

::: {.pf-step #s1-2}

The line integral depends only on the endpoints and equals
$$
\boxed{2},
$$
so the answer is (E).


::: pf-proof

By step [](#s1-1){.pf-ref} and the fundamental theorem for line integrals,
$$
\int_C d\Phi
=\Phi(0,1)-\Phi(1,0).
$$
The endpoint values are
$$
\Phi(0,1)=\sin0-0+1=1
$$
and
$$
\Phi(1,0)=\sin0-1+0=-1.
$$
Hence
$$
\int_C d\Phi=1-(-1)=2.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested integral value and corresponding choice.

:::

:::

:::
