---
schema: qual/card@1
id: P-IYE3I
kind: problem
title: The Joukowski map $f(z)=\frac{1}{2}(z+\frac{1}{z})$ on the punctured disc and
  its exterior
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
  - Geometry
relations: []
review: draft
---

::: {.problem}
Consider the function $f(z)=\frac{1}{2}\left(z+\frac{1}{z}\right)$ for $z \in \CC \backslash\{0\}$.
Let $\DD$ denote the open unit disc.

a.
Show that $f$ is one-to-one on the punctured disc $\DD \backslash\{0\}$.
What is the image of the circle $\abs{z}=r$ under this map when $0<r<1$ ?

b.
Show that $f$ is one-to-one on the domain $\CC \setminus \overline{\DD}$.
What is the image of this domain under this map?

c.
Show that there exists a map $g: \CC \backslash[-1,1] \rightarrow \DD \backslash\{0\}$ such that $(g \circ f)(z)=z$ for all $z \in \DD \backslash\{0\}$.
Describe the map $g$ by an explicit formula.

:::

::: {.solution}

::: pf

::: {.pf-step #eq}

For $z,w\neq0$, $f(z)=f(w)$ if and only if $z=w$ or $zw=1$.

::: pf-proof

$2(f(z)-f(w))=(z-w)+\frac{w-z}{zw}=(z-w)\bigl(1-\frac1{zw}\bigr)$.

:::

:::

::: {.pf-step #inj}

$f$ is one-to-one on $\DD\setminus\{0\}$ and on $\CC\setminus\overline{\DD}$.

::: pf-proof

If $z,w$ both lie in $\DD\setminus\{0\}$, then $\abs{zw}<1$; if both lie in $\CC\setminus\overline{\DD}$, then $\abs{zw}>1$. In both cases $zw\neq1$, so Step [](#eq){.pf-ref} gives $z=w$ whenever $f(z)=f(w)$.

:::

:::

::: {.pf-step #ellipse}

For $0<r<1$, $f$ maps the circle $\abs{z}=r$ onto the ellipse
$$
\frac{u^2}{A_r^2}+\frac{v^2}{B_r^2}=1,\qquad A_r=\tfrac12\bigl(\tfrac1r+r\bigr),\quad B_r=\tfrac12\bigl(\tfrac1r-r\bigr),
$$
with foci $\pm1$, traversed clockwise as $z$ runs counterclockwise.

::: pf-proof

For $z=re^{it}$, $f(z)=\frac12(re^{it}+r^{-1}e^{-it})=A_r\cos t-iB_r\sin t$. The foci are at $\pm\sqrt{A_r^2-B_r^2}=\pm1$.

:::

:::

::: {.pf-step #image}

$f(\DD\setminus\{0\})=f(\CC\setminus\overline{\DD})=\CC\setminus[-1,1]$.

::: pf-proof

For $w\in\CC$, the solutions of $f(z)=w$ are the roots of $z^2-2wz+1=0$, whose product is $1$. If $w=\cos t\in[-1,1]$, the roots are $e^{\pm it}$, both on the unit circle. If $w\notin[-1,1]$, neither root lies on the unit circle, because $f(e^{it})=\cos t\in[-1,1]$; since their product is $1$, exactly one root lies in $\DD\setminus\{0\}$ and the other in $\CC\setminus\overline{\DD}$.

:::

:::

::: {.pf-step #inverse}

Let $\sqrt{w^2-1}\coloneqq w\sqrt{1-w^{-2}}$ with the principal square root. Then
$$
\boxed{g(w)=w-\sqrt{w^2-1}}
$$
is holomorphic on $\CC\setminus[-1,1]$, maps it into $\DD\setminus\{0\}$, and satisfies $g(f(z))=z$ for $z\in\DD\setminus\{0\}$.

::: pf-proof

$1-w^{-2}\in(-\infty,0]$ exactly when $w^2\in(0,1]$, that is, when $w\in[-1,1]\setminus\{0\}$; so $g$ is holomorphic on $\CC\setminus[-1,1]$. Since $(w-\sqrt{w^2-1})(w+\sqrt{w^2-1})=1$ and both factors are roots of $z^2-2wz+1$, Step [](#image){.pf-ref} shows that $\abs{g(w)}\neq1$ on the connected set $\CC\setminus[-1,1]$. As $w\to\infty$, $g(w)=w\bigl(1-\sqrt{1-w^{-2}}\bigr)\to0$, so $\abs{g}<1$ throughout, and $g\neq0$ because $g(w)(w+\sqrt{w^2-1})=1$. Finally, for $z\in\DD\setminus\{0\}$ the roots of $\zeta^2-2f(z)\zeta+1$ are $z$ and $1/z$, and $g(f(z))$ is the one in $\DD$, namely $z$.

:::

:::

::: pf-qed

Steps [](#inj){.pf-ref} and [](#ellipse){.pf-ref} answer (a); Steps [](#inj){.pf-ref} and [](#image){.pf-ref} answer (b), with image $\CC\setminus[-1,1]$; Step [](#inverse){.pf-ref} answers (c).

:::

:::

:::
