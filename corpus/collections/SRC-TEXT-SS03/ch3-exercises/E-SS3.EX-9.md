---
schema: qual/card@1
id: E-SS3.EX-9
kind: problem
title: "SS 3.9: The integral of log(sin pi-x) on [0,1]"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
9. Show that

$$
\int_ {0} ^ {1} \log (\sin \pi x) d x = - \log 2.
$$

[Hint: Use the contour shown in Figure 9.]

Figure 9. Contour in Exercise 9
:::

::: {.solution}
The endpoint singularities are integrable because
\[
\log(\sin t)\sim\log t\quad(t\downarrow0),
\qquad
\log(\sin t)\sim\log(\pi-t)\quad(t\uparrow\pi).
\]
Let
\[
I=\int_0^{\pi/2}\log(\sin t)\,dt.
\]
By $t\mapsto\pi/2-t$,
\[
I=\int_0^{\pi/2}\log(\cos t)\,dt.
\]
Therefore
\[
2I=\int_0^{\pi/2}\log(\sin t\cos t)\,dt
=\int_0^{\pi/2}\log\left(\frac12\sin 2t\right)dt.
\]
Thus
\[
2I=-\frac\pi2\log2+\frac12\int_0^\pi\log(\sin u)\,du.
\]
By symmetry about $\pi/2$, the last integral equals $2I$. Hence
\[
2I=-\frac\pi2\log2+I,
\qquad
I=-\frac\pi2\log2.
\]
Finally, with $t=\pi x$,
\[
\int_0^1\log(\sin\pi x)\,dx
=\frac1\pi\int_0^\pi\log(\sin t)\,dt
=\frac{2I}{\pi}
=-\log2.
\]
:::
