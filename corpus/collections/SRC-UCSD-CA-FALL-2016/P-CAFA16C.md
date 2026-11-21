---
schema: qual/card@1
id: P-CAFA16C
kind: problem
title: '$\int_0^\infty \log x/(x^2+1)\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The keyhole identity is now computed term by term ((log x + 2 pi i)^2 = (log x)^2 + 4 pi i log x - 4 pi^2, and the value of the auxiliary integral pi/2), the vanishing of both arcs is estimated, the two residues are computed with the branch values Log i = pi i/2 and Log(-i) = 3 pi i/2 and 1/i = -i, and the answer I = 0 is checked independently by the substitution x -> 1/x. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Using the calculus of residues, compute $\int_0^{\infty} \frac{\log x}{x^2 + 1}\,dx$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Write $I=\int_0^\infty\frac{\log x}{x^2+1}dx$ and let $\Log$ be the branch of the logarithm on $\CC\setminus[0,\infty)$ with $0<\arg z<2\pi$.

::: pf

::: {.pf-step #banks}
With $F(z)=\dfrac{(\Log z)^2}{z^2+1}$, the two radial sides of the keyhole contour contribute $\displaystyle\int_0^\infty\frac{(\log x)^2-(\log x+2\pi i)^2}{x^2+1}dx=-4\pi iI+2\pi^3$ in the limit.

::: pf-proof
On the upper bank $z=x$ and $\Log x=\log x$; on the lower bank $z=xe^{2\pi i}$ and $\Log z=\log x+2\pi i$, and the contour traverses it from $\infty$ to $0$. So the limit of the two radial pieces is
$$
\int_0^\infty\frac{(\log x)^2}{x^2+1}dx-\int_0^\infty\frac{(\log x+2\pi i)^2}{x^2+1}dx .
$$
Since $(\log x+2\pi i)^2=(\log x)^2+4\pi i\log x-4\pi^2$, this equals $-4\pi i\int_0^\infty\frac{\log x}{x^2+1}dx+4\pi^2\int_0^\infty\frac{dx}{x^2+1}$, and $\int_0^\infty\frac{dx}{x^2+1}=\frac\pi2$, giving $-4\pi iI+2\pi^3$.
:::

:::

::: {.pf-step #arcs}
The integrals over the large and small circles tend to $0$.

::: pf-proof
On $\abs z=R>2$, $\abs{\Log z}\le\log R+2\pi$ and $\abs{z^2+1}\ge R^2-1$, so the integral over the circle is at most $2\pi R\frac{(\log R+2\pi)^2}{R^2-1}\to0$. On $\abs z=r<\frac12$, $\abs{\Log z}\le\abs{\log r}+2\pi$ and $\abs{z^2+1}\ge1-r^2$, so the integral is at most $2\pi r\frac{(\abs{\log r}+2\pi)^2}{1-r^2}\to0$ since $r(\log r)^2\to0$.
:::

:::

::: {.pf-step #residues}
$\operatorname{Res}(F,i)=\dfrac{\pi^2i}{8}$, $\operatorname{Res}(F,-i)=-\dfrac{9\pi^2i}{8}$, and their sum is $-\pi^2i$.

::: pf-proof
Both poles are simple, so $\operatorname{Res}(F,i)=\frac{(\Log i)^2}{2i}$ and $\operatorname{Res}(F,-i)=\frac{(\Log(-i))^2}{-2i}$. On the branch, $\Log i=\frac{\pi i}{2}$ and $\Log(-i)=\frac{3\pi i}{2}$; so $(\Log i)^2=-\frac{\pi^2}{4}$ and $(\Log(-i))^2=-\frac{9\pi^2}{4}$. Hence
$$
\operatorname{Res}(F,i)=\frac{-\pi^2/4}{2i}=\frac{\pi^2i}{8},\qquad
\operatorname{Res}(F,-i)=\frac{-9\pi^2/4}{-2i}=-\frac{9\pi^2i}{8},
$$
using $1/i=-i$, and the sum is $-\frac{8\pi^2i}{8}=-\pi^2i$.
:::

:::

::: {.pf-step}
$I=0$.

::: pf-proof
The contour encloses both poles, so by the residue theorem the contour integral equals $2\pi i(-\pi^2i)=2\pi^3$. By steps [](#banks){.pf-ref} and [](#arcs){.pf-ref} it also equals $-4\pi iI+2\pi^3$. Hence $-4\pi iI=0$, so $I=0$. As a check, the substitution $x\mapsto1/x$ gives $I=-I$.
:::

:::

:::
:::
