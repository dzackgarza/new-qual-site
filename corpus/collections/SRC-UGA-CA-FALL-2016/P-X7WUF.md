---
schema: qual/card@1
id: P-X7WUF
kind: problem
title: Residue at a pole of order $m$ as $\lim_{\tau\to a}\frac{d^{m-1}}{d\tau^{m-1}}\bigl((\tau-a)^m
  F(\tau)\bigr)$, and $\oint_{|z|=4}\frac{e^\tau}{(\tau^2+\pi^2)^2}\,d\tau$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
  - Contour Integration
relations: []
review: draft
---

::: problem
(a) Let $F$ be an analytic function inside and on a simple closed
curve $C$, except for a pole of order $m\geq 1$ at $z=a$ inside $C$.
Prove that

$$\frac{1}{2 \pi i}\oint_{C} F(\tau) d\tau =
\lim_{\tau\rightarrow a} \frac{d^{m-1}}{d\tau^{m-1}}\big((\tau-a)^m F(\tau))\big).$$


(b) Evaluate $$\oint_{C}\frac{e^{\tau}}{(\tau^2+\pi^2)^2}d\tau$$
where $C$ is the circle $|z|=4$.
:::

::: solution
Part (a) is missing the factor $1/(m-1)!$. The correct residue formula is
\[
\frac{1}{2\pi i}\oint_C F(\tau)\,d\tau
=\operatorname{Res}_{\tau=a}F
=\frac1{(m-1)!}\lim_{\tau\to a}
\frac{d^{m-1}}{d\tau^{m-1}}
\bigl((\tau-a)^mF(\tau)\bigr).
\]
This follows immediately from the Laurent expansion: the derivative on the
right equals $(m-1)!$ times the coefficient of $(\tau-a)^{-1}$.

For part (b), the poles inside $|z|=4$ are the double poles $\pm i\pi$. Their
residues are
\[
\frac1{4\pi^2}+\frac{i}{4\pi^3},
\qquad
\frac1{4\pi^2}-\frac{i}{4\pi^3},
\]
respectively, so their sum is $1/(2\pi^2)$. Therefore
\[
\boxed{\oint_C{e^\tau\over(\tau^2+\pi^2)^2}\,d\tau={i\over\pi}.}
\]

The mathematical exercise is thereby resolved; its separate provenance issue
remains, since this card does not occur in the official Fall 2016 UGA DOCX to
which its collection currently points.
:::
