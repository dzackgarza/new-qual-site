---
schema: qual/card@1
id: P-BERK85SU-06
kind: problem
title: The integral $\int_0^\infty x^{a-1}/(1+x)\,dx$ and its domain of convergence
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The improper integral converges exactly for 0<Re(a)<1. A keyhole contour
    for z^{a-1}/(1+z), using 0<arg z<2pi, gives
    (1-e^{2pi i a})I(a)=-2pi i e^{pi i a}; simplifying yields
    I(a)=pi/sin(pi a).
---

::: {.problem}
Evaluate
\[
\int_0^\infty \frac{x^{a-1}}{1+x}\,dx,
\]
where $a$ is a complex number. What restrictions must be imposed on $a$?
:::

::: {.solution}
Set
$$
I(a)=\int_0^\infty\frac{x^{a-1}}{1+x}\,dx,
\qquad
\sigma=\operatorname{Re}a.
$$

<1>1. The improper integral $I(a)$ converges exactly when
$$
0<\sigma<1.
$$

::: {.proof}
Near $0$,
$$
\frac{\abs{x^{a-1}}}{1+x}
=
\frac{x^{\sigma-1}}{1+x},
$$
so absolute convergence there holds when $\sigma>0$. Near infinity,
$$
\frac{\abs{x^{a-1}}}{1+x}
=
\frac{x^{\sigma-1}}{1+x},
$$
which is comparable to $x^{\sigma-2}$, so absolute convergence
there holds when $\sigma<1$.

These conditions are also necessary for ordinary improper
convergence. As $x\to0^+$,
$$
\frac1{1+x}=1+O(x).
$$
If $\sigma<0$, then for fixed sufficiently small $\delta>0$,
$$
\int_\varepsilon^\delta
\frac{x^{a-1}}{1+x}\,dx
=
\frac{\delta^a-\varepsilon^a}{a}
+o(\abs{\varepsilon^a})
\qquad
(\varepsilon\to0^+).
$$
Since $\abs{\varepsilon^a}=\varepsilon^\sigma\to\infty$, the
partial integrals cannot converge. If $\sigma=0$ and $a\neq0$, the
error term has a finite limit while
$\varepsilon^a=e^{a\log\varepsilon}$ has no limit; for $a=0$ the
leading integral is logarithmic. Thus convergence at $0$ requires
$\sigma>0$.

Likewise,
$$
\frac1{1+x}
=
x^{-1}(1+O(x^{-1}))
\qquad
(x\to\infty).
$$
If $\sigma>1$, then
$$
\int_\delta^R
\frac{x^{a-1}}{1+x}\,dx
=
\frac{R^{a-1}-\delta^{a-1}}{a-1}
+o(\abs{R^{a-1}})
\qquad
(R\to\infty),
$$
so the partial integrals cannot converge. If $\sigma=1$ and
$a\neq1$, the error term converges while $R^{a-1}$ has no limit; for
$a=1$ the leading integral is logarithmic. Thus convergence at
infinity requires $\sigma<1$.
:::

<1>2. Assume henceforth that $0<\sigma<1$, and define
$$
F(z)=\frac{z^{a-1}}{1+z}
$$
using the branch
$$
z^{a-1}
=
\exp\bigl((a-1)(\log\abs{z}+i\arg z)\bigr),
\qquad
0<\arg z<2\pi.
$$
On a keyhole contour about the positive real axis, the circular arc
integrals tend to $0$ as the outer radius tends to infinity and the
inner radius tends to $0$.

::: {.proof}
On the outer circle $\abs{z}=R$, the factor coming from
$e^{-\operatorname{Im}(a)\arg z}$ is bounded uniformly for
$0\le\arg z\le2\pi$. Thus, for a constant $C_a$ independent of
$R$,
$$
\abs{F(z)}
\le
C_a\frac{R^{\sigma-1}}{R-1}.
$$
Multiplying by the arc length $2\pi R$ gives a bound of order
$R^{\sigma-1}$, which tends to $0$ because $\sigma<1$.

On the inner circle $\abs{z}=r$,
$$
\abs{F(z)}
\le
C_a\frac{r^{\sigma-1}}{1-r}.
$$
Multiplication by the arc length $2\pi r$ gives a bound of order
$r^\sigma$, which tends to $0$ because $\sigma>0$.
:::

<1>3. The limiting contour integral satisfies
$$
(1-e^{2\pi ia})I(a)
=
-2\pi i e^{\pi ia}.
$$

::: {.proof}
On the upper side of the positive real axis, $\arg z=0$, so the
contribution tends to $I(a)$. On the lower side,
$\arg z=2\pi$ and the contour runs from infinity back to $0$, so
the contribution tends to
$$
-e^{2\pi i(a-1)}I(a)
=
-e^{2\pi ia}I(a).
$$
By step <1>2, the circular contributions vanish in the limit.

The only pole inside the keyhole contour is $z=-1$. Since
$\arg(-1)=\pi$ on the chosen branch,
$$
\Res_{z=-1}F(z)
=
(-1)^{a-1}
=
e^{\pi i(a-1)}
=
-e^{\pi ia}.
$$
The residue theorem therefore gives the displayed identity.
:::

<1>4. For $0<\operatorname{Re}a<1$,
$$
\boxed{
I(a)
=
\frac{\pi}{\sin(\pi a)}
}.
$$

::: {.proof}
Using
$$
1-e^{2\pi ia}
=
-2i e^{\pi ia}\sin(\pi a),
$$
step <1>3 gives
$$
I(a)
=
\frac{-2\pi i e^{\pi ia}}
{-2i e^{\pi ia}\sin(\pi a)}
=
\frac{\pi}{\sin(\pi a)}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 gives the exact restriction on $a$, and step <1>4 evaluates
the integral throughout that domain.
:::
:::
