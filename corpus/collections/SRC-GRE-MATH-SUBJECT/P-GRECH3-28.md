---
schema: qual/card@1
id: P-GRECH3-28
kind: problem
title: Set up a double integral between two elliptic surfaces
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
  note: "Checked against Chapter 3 review Question 28 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Set up, but do not evaluate, a double integral that gives the volume of the solid bounded above by the elliptic paraboloid $z=1-\left(x^2+\frac{1}{9}y^2\right)$ and bounded below by the elliptic cone $z=\sqrt{x^2+\frac{1}{9}y^2}-1$.

(A) $4\int_0^1\int_0^3\left(2-\sqrt{x^2+\frac{1}{9}y^2}\right)dy\,dx$
(B) $\int_{-1}^1\int_{-3\sqrt{1-x^2}}^{3\sqrt{1-x^2}}\left(2-\frac{3}{2}\sqrt{x^2+\frac{1}{9}y^2}\right)dy\,dx$
(C) $2\int_0^1\int_{-3}^3\left(x^2-\frac{1}{9}y^2-\sqrt{x^2+\frac{1}{9}y^2}\right)dy\,dx$
(D) $2\int_0^1\int_{-3}^3\left(2-x^2-\frac{1}{9}y^2-\sqrt{x^2+\frac{1}{9}y^2}\right)dy\,dx$
(E) $\int_{-1}^1\int_{-3\sqrt{1-x^2}}^{3\sqrt{1-x^2}}\left(2-x^2-\frac{1}{9}y^2-\sqrt{x^2+\frac{1}{9}y^2}\right)dy\,dx$
:::

::: {.solution}

Write
$$
q(x,y)=x^2+\frac19y^2.
$$

::: pf

::: {.pf-step #s1-1}

The two surfaces intersect above the ellipse
$$
q(x,y)=1.
$$


::: pf-proof

At an intersection,
$$
1-q=\sqrt q-1,
$$
so
$$
2-q-\sqrt q=0.
$$
Setting $r=\sqrt q\ge0$ gives
$$
2-r^2-r=(1-r)(r+2)=0.
$$
Thus $r=1$, hence $q=1$.

:::

:::

::: {.pf-step #s1-2}

The projection of the solid to the $xy$-plane is
$$
R=\left\{(x,y):-1\le x\le1,
-3\sqrt{1-x^2}\le y\le3\sqrt{1-x^2}\right\}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the boundary of the projection is the ellipse
$$
x^2+\frac19y^2=1.
$$
Inside this ellipse, $0\le r=\sqrt q\le1$, and the vertical separation of the surfaces is
$$
\bigl(1-q\bigr)-\bigl(\sqrt q-1\bigr)
=2-r^2-r
=(1-r)(r+2)\ge0.
$$
Thus the bounded solid projects to the ellipse interior $q\le1$. Solving the ellipse inequality for $y$ gives the displayed iterated-integral bounds.

:::

:::

::: {.pf-step #s1-3}

The required volume integral is
$$
\boxed{
\int_{-1}^1
\int_{-3\sqrt{1-x^2}}^{3\sqrt{1-x^2}}
\left(
2-x^2-\frac19y^2-\sqrt{x^2+\frac19y^2}
\right)
dy\,dx
},
$$
so the answer is (E).


::: pf-proof

Over the region $R$ from step [](#s1-2){.pf-ref}, the upper surface is
$$
z_{\mathrm{top}}=1-q
$$
and the lower surface is
$$
z_{\mathrm{bottom}}=\sqrt q-1.
$$
Hence
$$
z_{\mathrm{top}}-z_{\mathrm{bottom}}
=2-q-\sqrt q
=2-x^2-\frac19y^2-\sqrt{x^2+\frac19y^2}.
$$
Integrating this vertical thickness over the bounds from step [](#s1-2){.pf-ref} yields the displayed integral.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested double-integral setup and corresponding choice.

:::

:::

:::
