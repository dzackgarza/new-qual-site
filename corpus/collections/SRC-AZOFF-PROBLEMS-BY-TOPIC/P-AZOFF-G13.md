---
schema: qual/card@1
id: P-AZOFF-G13
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{(a+b\cos\theta)^2}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 13, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    First evaluated the auxiliary integral of 1/(a+b cos theta) by the unit
    circle substitution and the residue at the unique root inside the disk,
    obtaining 2pi/sqrt(a^2-b^2). Differentiating this identity with respect
    to a, justified uniformly away from the zero denominator because a>b,
    gives 2pi a/(a^2-b^2)^(3/2).
---

::: {.problem}
Suppose $a > b > 0$ . Evaluate $\begin{array} { r } { \int _ { 0 } ^ { 2 \pi } \frac { d \theta } { ( a + b \cos \theta ) ^ { 2 } } } \end{array}$
:::

::: {.solution}
Put
$$
d=\sqrt{a^2-b^2}>0.
$$
First consider the auxiliary integral
$$
J(a)
=
\int_0^{2\pi}
\frac{d\theta}{a+b\cos\theta}.
$$

<1>1. Under the substitution $z=e^{i\theta}$,
$$
J(a)
=
\frac2i
\int_{\abs{z}=1}
\frac{dz}{bz^2+2az+b}.
$$

::: {.proof}
On the unit circle,
$$
d\theta=\frac{dz}{iz}
$$
and
$$
\cos\theta=\frac12\left(z+z^{-1}\right).
$$
Therefore
$$
\begin{aligned}
\frac{d\theta}{a+b\cos\theta}
&=
\frac{1}{a+\frac b2(z+z^{-1})}
\frac{dz}{iz}\\
&=
\frac{2\,dz}
{i(bz^2+2az+b)}.
\end{aligned}
$$
Integrating once counterclockwise around the unit circle gives the claim.
:::

<1>2. The roots of
$$
bz^2+2az+b
$$
are
$$
\alpha=\frac{-a+d}{b},
\qquad
\beta=\frac{-a-d}{b},
$$
with
$$
\abs{\alpha}<1<\abs{\beta}.
$$

::: {.proof}
The quadratic formula gives the two roots. Their product is
$$
\alpha\beta=1.
$$
Moreover,
$$
\abs{\alpha}
=
\frac{a-d}{b}
=
\frac{b}{a+d}
<1,
$$
because $a+d>b$. Therefore
$$
\abs{\beta}=\frac1{\abs{\alpha}}>1.
$$
:::

<1>3. The auxiliary integral is
$$
J(a)
=
\frac{2\pi}{\sqrt{a^2-b^2}}.
$$

::: {.proof}
By step <1>2, only the simple pole $z=\alpha$ lies inside the unit circle.
For
$$
G(z)
=
\frac2{i(bz^2+2az+b)},
$$
the residue at $\alpha$ is
$$
\begin{aligned}
\Res(G;\alpha)
&=
\frac2{i(2b\alpha+2a)}\\
&=
\frac1{i(b\alpha+a)}.
\end{aligned}
$$
Since
$$
b\alpha+a=d,
$$
one has
$$
\Res(G;\alpha)
=
\frac1{id}
=
-\frac{i}{d}.
$$
The residue theorem and step <1>1 therefore give
$$
J(a)
=
2\pi i
\left(-\frac{i}{d}\right)
=
\frac{2\pi}{d}.
$$
Substitute $d=\sqrt{a^2-b^2}$.
:::

<1>4. Differentiation with respect to $a$ may be passed through the
integral defining $J(a)$, and
$$
J'(a)
=
-\int_0^{2\pi}
\frac{d\theta}{(a+b\cos\theta)^2}.
$$

::: {.proof}
Since $a>b$, choose
$$
0<\delta<a-b.
$$
For $s$ with $\abs{s-a}<\delta$ and every real $\theta$,
$$
s+b\cos\theta
\geq
s-b
>
a-b-\delta
>
0.
$$
Thus the function
$$
(s,\theta)
\longmapsto
\frac1{s+b\cos\theta}
$$
and its $s$-derivative are continuous on a compact parameter rectangle
around $a$ and $[0,2\pi]$. The standard differentiation-under-the-integral
theorem applies, giving
$$
\begin{aligned}
J'(a)
&=
\int_0^{2\pi}
\frac{\partial}{\partial a}
\left(
\frac1{a+b\cos\theta}
\right)
d\theta\\
&=
-\int_0^{2\pi}
\frac{d\theta}{(a+b\cos\theta)^2}.
\end{aligned}
$$
:::

<1>5. The requested integral is
$$
\boxed{
\int_0^{2\pi}
\frac{d\theta}{(a+b\cos\theta)^2}
=
\frac{2\pi a}{(a^2-b^2)^{3/2}}.
}
$$

::: {.proof}
Differentiate the formula in step <1>3:
$$
J'(a)
=
-\frac{2\pi a}{(a^2-b^2)^{3/2}}.
$$
Combine this with step <1>4 and multiply by $-1$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested evaluation.
:::
:::
