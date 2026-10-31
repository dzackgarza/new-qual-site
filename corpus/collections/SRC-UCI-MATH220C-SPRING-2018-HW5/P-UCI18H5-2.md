---
schema: qual/card@1
id: P-UCI18H5-2
kind: problem
title: $z/2$ and $z/3$ are topologically but not conformally conjugate
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Set $f(z)=z/2$ and $g(z)=z/3$.
Prove that there is no conformal change of coordinates $\phi:\CC\to\CC$ such that $g\circ\phi(z)=\phi\circ f(z)$ for all $z\in\CC$, but there exists a homeomorphism $h:\CC\to\CC$ (that is, a continuous change of coordinates) such that $g\circ h(z)=h\circ f(z)$ for all $z\in\CC$.
:::

::: {.solution}
Both maps fix $0$ and contract the punctured plane towards it, but by different factors.

::: pf

::: {.pf-step #no-conformal-conjugacy}
There is no conformal $\phi\colon\CC\to\CC$ with $g\circ\phi=\phi\circ f$.

::: pf-proof
A conformal bijection of $\CC$ onto itself is an affine map $\phi(z)=az+b$ with $a\ne0$.
The relation $g(\phi(z))=\phi(f(z))$ then reads
$$
\frac{az+b}{3}=\frac{az}{2}+b
$$
for all $z$. Comparing the coefficients of $z$ gives $\frac a3=\frac a2$, hence $a=0$, contradicting $a\ne0$.
:::

:::

::: {.pf-step #homeomorphism}
There is a homeomorphism $h\colon\CC\to\CC$ with $g\circ h=h\circ f$.

::: pf-proof
Put $s=\log_23>0$ and define $h(0)=0$, while for $z=re^{i\theta}$ with $r>0$ and $\theta\in\RR$ set $h(z)=r^se^{i\theta}$; this is well defined, continuous, and a homeomorphism of $\CC$ with inverse $w\mapsto\abs w^{1/s}e^{i\arg w}$ extended by $0\mapsto0$.
For $z=re^{i\theta}\ne0$,
$$
h(f(z))=h\Bigl(\frac r2e^{i\theta}\Bigr)=\Bigl(\frac r2\Bigr)^se^{i\theta}=\frac{r^s}{3}e^{i\theta}=\frac{h(z)}{3}=g(h(z)),
$$
because $2^s=3$; and both sides vanish at $z=0$.
:::

:::

:::
:::
