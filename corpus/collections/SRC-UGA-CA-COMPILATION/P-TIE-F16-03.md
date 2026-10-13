---
schema: qual/card@1
id: P-TIE-F16-03
kind: problem
title: Complex line integrals and the ML estimate for $\int_{|z|=R}\frac{\log z}{z^2}\,dz$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2016, question 3.
---

::: {.problem}
(a) $f : D \to \mathbb { C }$ be a continuous function, where $D \subset \mathbb { C }$ is a domain.Let $\alpha : [ a , b ] \to D$ be a smooth curve.
Give a precise definition of the complex line integral

$$
\int _ { \alpha } f .
$$

(b) Assume that there exists a constant M such that $| f ( \tau ) | \le M$ for all $\tau \in { \mathrm { I m a g e } } ( \alpha )$ . Prove that

$$
\big | \int _ { \alpha } f \big | \leq M \times \mathrm { l e n g t h } ( \alpha ) .
$$

(c) Let $C _ { R }$ be the circle $| z | = R ,$ , described in the counterclockwise direction, where $R > 1$ Provide an upper bound for $| \int _ { C _ { R } } \frac { \log { ( z ) } } { z ^ { 2 } } |$ , which depends only on R and other constants.
:::

::: {.remark}
Erratum: part (c) does not specify a branch or determination of $\log z$. No single-valued holomorphic logarithm exists on a neighborhood of the full circle $C_R$.
The estimate below uses the standard continuous determination along the parametrization
$$
z(t)=Re^{it},
\qquad
0\le t\le2\pi,
$$
namely
$$
\Log_{C_R}(Re^{it})=\log R+it.
$$
:::

::: {.solution}
<1>1. The complex line integral of $f$ along a smooth curve
$$
\alpha:[a,b]\to D
$$
is defined by
$$
\boxed{
\int_\alpha f(z)\,dz
\coloneqq
\int_a^b
f(\alpha(t))\alpha'(t)\,dt.
}
$$

::: {.proof}
The composition
$$
t\longmapsto f(\alpha(t))\alpha'(t)
$$
is continuous on $[a,b]$ because $f$ is continuous and $\alpha$ is smooth. Hence the ordinary complex-valued Riemann integral on the right exists, and this is the definition of the line integral along the parametrized curve.
:::

<1>2. If
$$
\abs{f(\tau)}\le M
$$
for every $\tau$ in the image of $\alpha$, then
$$
\boxed{
\abs{\int_\alpha f(z)\,dz}
\le
M\,\operatorname{length}(\alpha).
}
$$

::: {.proof}
By step <1>1 and the triangle inequality,
$$
\begin{aligned}
\abs{\int_\alpha f(z)\,dz}
&=
\abs{
\int_a^b
f(\alpha(t))\alpha'(t)\,dt
}\\
&\le
\int_a^b
\abs{f(\alpha(t))}
\abs{\alpha'(t)}\,dt\\
&\le
M
\int_a^b
\abs{\alpha'(t)}\,dt.
\end{aligned}
$$
By definition,
$$
\operatorname{length}(\alpha)
=
\int_a^b
\abs{\alpha'(t)}\,dt.
$$
Substitution gives the estimate.
:::

<1>3. Along
$$
C_R:
z(t)=Re^{it},
\qquad
0\le t\le2\pi,
$$
the chosen determination satisfies
$$
\abs{\Log_{C_R}(z(t))}
\le
\sqrt{(\log R)^2+4\pi^2}.
$$

::: {.proof}
By definition,
$$
\Log_{C_R}(Re^{it})
=
\log R+it.
$$
Hence
$$
\abs{\Log_{C_R}(Re^{it})}
=
\sqrt{(\log R)^2+t^2}
\le
\sqrt{(\log R)^2+4\pi^2}.
$$
:::

<1>4. On $C_R$,
$$
\abs{
\frac{\Log_{C_R}z}{z^2}
}
\le
\frac{
\sqrt{(\log R)^2+4\pi^2}
}{R^2}.
$$

::: {.proof}
For $z\in C_R$,
$$
\abs z=R,
$$
so
$$
\abs{z^2}=R^2.
$$
Combine this with step <1>3.
:::

<1>5. Therefore
$$
\boxed{
\abs{
\int_{C_R}
\frac{\Log_{C_R}z}{z^2}\,dz
}
\le
\frac{2\pi}{R}
\sqrt{(\log R)^2+4\pi^2}.
}
$$

::: {.proof}
The circle $C_R$ has length
$$
2\pi R.
$$
Apply the ML estimate from step <1>2 to the bound in step <1>4:
$$
\begin{aligned}
\abs{
\int_{C_R}
\frac{\Log_{C_R}z}{z^2}\,dz
}
&\le
(2\pi R)
\frac{
\sqrt{(\log R)^2+4\pi^2}
}{R^2}\\
&=
\frac{2\pi}{R}
\sqrt{(\log R)^2+4\pi^2}.
\end{aligned}
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 gives the precise definition requested in part (a), step <1>2 proves part (b), and step <1>5 gives the requested $R$-dependent bound for part (c) after specifying the logarithm determination omitted by the source.
:::
:::
