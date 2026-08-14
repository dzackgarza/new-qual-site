---
schema: qual/card@1
id: P-GK4F6
kind: problem
title: "Let $\\gamma(t)$ be a piecewise smooth curve in $\\mathbb{C}, t \\in[0,1]$. Let $F(w)$ be a continuous\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - morera
  - holomorphic-functions
  - contour-integration
relations: []
review: draft
---
:::{.problem title="?"}
Let $\gamma(t)$ be a piecewise smooth curve in $\mathbb{C}, t \in[0,1]$. Let $F(w)$ be a continuous function on $\gamma$. Show that $f(z)$ defined by
\[
f(z):=\int_{\gamma} \frac{F(w)}{w-z} d w
\]
is analytic on the complement of the curve $\gamma$.

:::

:::{.solution title="Using Morera"}
By Morera's theorem, it suffices to show $\int_\Delta f(z) \dz = 0$ for all triangles $\Delta \subseteq \gamma^c$.
Claim:
\[
\int_\Delta f(z) \dz 
&= \int_\Delta \int_\gamma {F(w) \over w-z} \dw \dz \\
&= \int_\gamma \int_\Delta {F(w) \over w-z} \dz \dw \\
&= \int_\gamma F(w) \qty{ \int_\Delta {1 \over w-z} \dz} \dw \\
&= \int_\gamma F(w) \cdot 0 \dw \\
&= 0
.\]

That the inner integral is zero follows from the fact that the function $z\mapsto {1\over w-z}$ is holomorphic on $\gamma^c$, since it has only a simple pole at $w$ where $w\in \gamma$ is fixed.

That the interchange of integrals is justified follows from Fubini's theorem: these are continuous functions on compact sets, which are uniformly bounded and thus Lebesgue measurable and integrable.

:::


:::{.solution title="Using limit definition"}
The claim is that $f$ is complex differentiable, thus smooth, thus holomorphic and equal to its Taylor series expansion.
The quick justification:
\[
\dd{}{z} f(z)
&= \dd{}{z} \int_\gamma {F(w) \over w-z}\dw \\
&= \int_\gamma \dd{}{z} {F(w) \over w-z} \dw \\
&= \int_\gamma {F(w) \over (w-z)^2} \dw
,\]
where differentiating through the integral is justified since the integrand is a continuous function of $z$ on $\gamma$ since $w\neq z$ on $\gamma$, and $\gamma$ is a compact set.

Slightly more rigorously, one can equivalently pass a limit through the integral to show that the defining limit exists:
\[
f(z+h) - f(z)
&= \int_\gamma {F(w) \over w+h-z} \dw - \int_\gamma {F(w) \over w-z}\dw \\
&= \int_\gamma {(w-z)F(w) - (w+h-z)F(w) \over (w+h-z)(w-z) } \dw \\
&= \int_\gamma F(w) {h \over (w+h-z)(w-z)} \dw \\
&\convergesto{h\to 0} \int_\gamma {F(w) \over (w-z)^2}\dw
,\]
since the term involving $h$ goes to 1.


:::

