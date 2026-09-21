---
schema: qual/card@1
id: P-AZOFF-I07
kind: problem
title: Schwarz reflection across the circle and functions real on the unit circle
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Schwarz lemma and reflection principle, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The source uses H in part (b) without defining it. The requested
    conjugation identity and the real-axis Schwarz reflection principle force
    H to be a half-plane bounded by the real axis; the standard convention
    used here is the upper half-plane. The card also removes a stray
    OCR-derived subscript colon after the closed disk in part (c).
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Stated the real-axis reflection principle, used T(z)=i(1+z)/(1-z) to
    conjugate real-axis reflection to circle reflection. For part (c), the
    imaginary part of f is harmonic, continuous on the closed disk, and zero
    on the boundary; the harmonic maximum principle makes it identically
    zero, and the open mapping theorem then forces f to be constant.
---

::: {.problem}
[August 2007, Problem $\# 4]$

a) State the standard Schwarz reflection principle involving reflection across the real axis.

b) Let $H=\{z\in\mathbb C:\operatorname{Im}z>0\}$. Give, with justification, a linear fractional transformation T mapping D to H. Let $g ( z ) = { \overline { { z } } } ;$ show that $\begin{array} { r } { T ^ { - 1 } \circ g \circ T ( z ) = \frac { 1 } { \overline { { z } } } } \end{array}$

c) Suppose f is holomorphic on D, continuous on ${ \overline { { \mathbb { D } } } }$ , and real on the unit circle.
Prove that f must be constant.
:::

::: {.solution}
<1>1. Part (a): the Schwarz reflection principle across the real axis says
the following.

::: {.proof}
Let $U\subseteq\CC$ be a domain symmetric under conjugation, and write
$$
U_+=\{z\in U:\operatorname{Im}z>0\}.
$$
If $F$ is holomorphic on $U_+$, continuous on
$$
U_+\cup(U\cap\RR),
$$
and real-valued on $U\cap\RR$, then
$$
\widetilde F(z)
=
\begin{cases}
F(z),&\operatorname{Im}z\geq0,\\
\overline{F(\bar z)},&\operatorname{Im}z<0
\end{cases}
$$
defines a holomorphic function on all of $U$.
:::

<1>2. Part (b): the linear fractional transformation
$$
\boxed{
T(z)=i\frac{1+z}{1-z}
}
$$
maps $\DD$ biholomorphically onto the upper half-plane $H$.

::: {.proof}
For $z\in\DD$,
$$
\begin{aligned}
\operatorname{Im}T(z)
&=
\operatorname{Re}\frac{1+z}{1-z}\\
&=
\frac{1-\abs{z}^2}{\abs{1-z}^2}\\
&>
0.
\end{aligned}
$$
Thus $T(\DD)\subseteq H$. Solving
$$
w=i\frac{1+z}{1-z}
$$
for $z$ gives
$$
T^{-1}(w)=\frac{w-i}{w+i},
$$
which maps $H$ back into $\DD$. Hence $T$ is a biholomorphism from $\DD$
onto $H$.
:::

<1>3. With $g(w)=\bar w$, one has on the Riemann sphere
$$
\boxed{
T^{-1}\circ g\circ T(z)=\frac1{\bar z}.
}
$$

::: {.proof}
For finite $z\neq0,1$,
$$
\overline{T(z)}
=
-i\frac{1+\bar z}{1-\bar z}.
$$
Therefore
$$
\begin{aligned}
T^{-1}(\overline{T(z)})
&=
\frac{-i\frac{1+\bar z}{1-\bar z}-i}
{-i\frac{1+\bar z}{1-\bar z}+i}\\
&=
\frac{-2i/(1-\bar z)}
{-2i\bar z/(1-\bar z)}\\
&=
\frac1{\bar z}.
\end{aligned}
$$
Both sides are the same anti-Möbius transformation of the Riemann sphere,
so the identity extends to the exceptional points as well, with
$0$ and $\infty$ interchanged.
:::

<1>4. Part (c): the function $f$ is constant.

::: {.proof}
Write
$$
f=u+iv
$$
with real-valued functions $u$ and $v$. Since $f$ is holomorphic on $\DD$,
the function $v=\operatorname{Im}f$ is harmonic there. Since $f$ is
continuous on $\overline{\DD}$ and real-valued on the unit circle, $v$ is
continuous on $\overline{\DD}$ and
$$
v=0
$$
on $\partial\DD$.

The maximum principle for harmonic functions applied to $v$ gives
$$
v\leq0
$$
on $\DD$, while applying it to $-v$ gives
$$
v\geq0.
$$
Hence $v\equiv0$ on $\DD$, so
$$
f(\DD)\subseteq\RR.
$$
If $f$ were nonconstant, the open mapping theorem would make $f(\DD)$ open
in $\CC$, which is impossible for a subset of $\RR$. Therefore $f$ is
constant.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 answers part (a), steps <1>2--<1>3 answer part (b), and step <1>4
proves part (c).
:::
:::
