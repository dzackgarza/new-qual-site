---
schema: qual/card@1
id: P-AZOFF-D08
kind: problem
title: Cauchy-type integrals are analytic off the curve
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Integrals and Cauchy’s theorem, Problem 8, of Azoff Problems by Topic.pdf; the source leaves g undefined, so a remark records the missing continuity hypothesis on g.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    Page 4 of the retained PDF uses g in the Cauchy-type integral without
    defining it. The problem now states the standard missing hypothesis that
    g is continuous on the range of gamma; the existing erratum remark
    records the source omission.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Parametrized the curve on [0,1], used compactness to obtain positive
    distance from an arbitrary exterior point and boundedness of g, and
    estimated the difference quotient uniformly to justify passage through
    the line integral. This gives f'(z) as the integral with kernel
    (w-z)^(-2) at every point off the curve.
---

::: {.problem}
Let $\gamma$ be a smooth curve joining two distinct points $a, b \in \mathbb{C}$, and let $g$ be continuous on the range of $\gamma$. Prove that the function defined by the formula
$$
f(z) = \int_\gamma \frac{g(w)\,dw}{w - z}
$$
is analytic off the range of $\gamma$. Justify every step.
:::

::: {.solution}
Choose a smooth parametrization
$$
\gamma:[0,1]\longrightarrow\CC
$$
and write
$$
\Gamma=\gamma([0,1]).
$$

<1>1. The set $\Gamma$ is compact, and for every $z\in\CC\sm\Gamma$ the
integral
$$
f(z)=\int_\gamma\frac{g(w)}{w-z}\,dw
$$
is well defined.

::: {.proof}
The interval $[0,1]$ is compact and $\gamma$ is continuous, so $\Gamma$ is
compact. Fix $z\notin\Gamma$. Then $w-z$ never vanishes on $\Gamma$, so
$$
w\longmapsto\frac{g(w)}{w-z}
$$
is continuous on $\Gamma$. Hence its line integral along the smooth curve
$\gamma$ exists.
:::

<1>2. Fix $z_0\in\CC\sm\Gamma$ and set
$$
\delta=\operatorname{dist}(z_0,\Gamma)>0.
$$
If $\abs{\eta}<\delta/2$, then $z_0+\eta\notin\Gamma$ and
$$
\abs{w-z_0-\eta}\geq\delta/2
$$
for every $w\in\Gamma$.

::: {.proof}
Since $\Gamma$ is compact and $z_0\notin\Gamma$, the continuous function
$w\mapsto\abs{w-z_0}$ attains a strictly positive minimum $\delta$ on
$\Gamma$. For $w\in\Gamma$ and $\abs{\eta}<\delta/2$, the reverse
triangle inequality gives
$$
\abs{w-z_0-\eta}
\geq
\abs{w-z_0}-\abs{\eta}
>
\delta/2.
$$
In particular, $z_0+\eta$ does not lie in $\Gamma$.
:::

<1>3. For $0<\abs{\eta}<\delta/2$,
$$
\frac{f(z_0+\eta)-f(z_0)}{\eta}
=
\int_\gamma
\frac{g(w)}
{(w-z_0-\eta)(w-z_0)}
\,dw.
$$

::: {.proof}
By step <1>2, both integrals are defined. Linearity of the line integral and
the identity
$$
\frac1\eta
\left(
\frac1{w-z_0-\eta}
-
\frac1{w-z_0}
\right)
=
\frac1{(w-z_0-\eta)(w-z_0)}
$$
give the formula.
:::

<1>4. As $\eta\to0$, the integrands in step <1>3 converge uniformly along
$\Gamma$ to
$$
\frac{g(w)}{(w-z_0)^2}.
$$

::: {.proof}
Because $g$ is continuous on the compact set $\Gamma$, there is
$$
M=\max_{w\in\Gamma}\abs{g(w)}<\infty.
$$
For $0<\abs{\eta}<\delta/2$, step <1>2 gives
$$
\begin{aligned}
&\abs{
\frac{g(w)}
{(w-z_0-\eta)(w-z_0)}
-
\frac{g(w)}{(w-z_0)^2}
}\\
&\qquad=
\frac{\abs{g(w)}\abs{\eta}}
{\abs{w-z_0-\eta}\abs{w-z_0}^2}\\
&\qquad\leq
\frac{2M\abs{\eta}}{\delta^3}
\end{aligned}
$$
for every $w\in\Gamma$. The right-hand side is independent of $w$ and
tends to zero with $\eta$, proving uniform convergence.
:::

<1>5. The complex derivative of $f$ exists at $z_0$ and satisfies
$$
f'(z_0)
=
\int_\gamma\frac{g(w)}{(w-z_0)^2}\,dw.
$$

::: {.proof}
Let
$$
L=\int_0^1\abs{\gamma'(t)}\,dt,
$$
the finite length of the smooth curve. By step <1>4, the difference between
the line integral in step <1>3 and the proposed derivative is bounded by
$$
L\,
\sup_{w\in\Gamma}
\abs{
\frac{g(w)}
{(w-z_0-\eta)(w-z_0)}
-
\frac{g(w)}{(w-z_0)^2}
},
$$
which tends to zero as $\eta\to0$. Therefore the difference quotient in
step <1>3 converges to the displayed line integral.
:::

<1>6. The function $f$ is analytic on $\CC\sm\Gamma$.

::: {.proof}
The point $z_0\in\CC\sm\Gamma$ was arbitrary. Step <1>5 shows that $f$
has a complex derivative at every point of $\CC\sm\Gamma$. Since $\Gamma$
is compact, its complement is open. Hence $f$ is analytic off the range of
$\gamma$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::

::: {.remark}
Erratum: the source does not say what $g$ is. The corrected statement above
adds the standard hypothesis that $g$ is continuous on the range of
$\gamma$; under this hypothesis the Cauchy-type integral is defined for
every $z$ off that range.
:::
