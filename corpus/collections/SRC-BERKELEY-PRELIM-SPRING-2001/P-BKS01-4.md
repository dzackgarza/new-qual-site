---
schema: qual/card@1
id: P-BKS01-4
kind: problem
title: Evaluate $\int_0^\infty(1+x^5)^{-1}\,dx$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Integrated 1/(1+z^5) over the sector of angle 2 pi/5. The sector
    contains only the pole exp(i pi/5); the two radial integrals differ
    by exp(2 pi i/5), and the circular arc vanishes.
---

::: {.problem}
Evaluate
\[
\int_0^\infty\frac{dx}{1+x^5}.
\]
:::

::: {.solution}
Set
$$
f(z)=\frac{1}{1+z^5},
\qquad
\zeta=e^{i\pi/5}.
$$

<1>1. Let $C_R$ be the positively oriented boundary of the sector
$$
0\leq\arg z\leq\frac{2\pi}{5},
\qquad
\abs{z}\leq R,
$$
where $R>1$. The only pole of $f$ inside $C_R$ is
$$
\zeta=e^{i\pi/5},
$$
and
$$
\operatorname{Res}_{z=\zeta}f(z)
=
\frac{1}{5\zeta^4}.
$$

::: {.proof}
The poles are the five roots of
$$
z^5=-1,
$$
whose arguments are
$$
\frac{(2k+1)\pi}{5},
\qquad
k=0,1,2,3,4.
$$
Only the root with argument $\pi/5$ lies in the open sector. Since
the pole is simple,
$$
\operatorname{Res}_{z=\zeta}f(z)
=
\frac{1}{(z^5+1)'|_{z=\zeta}}
=
\frac{1}{5\zeta^4}.
$$
:::

<1>2. If
$$
I_R=\int_0^R\frac{dx}{1+x^5},
$$
then the two radial pieces of $C_R$ contribute
$$
I_R
\qquad\text{and}\qquad
-e^{2\pi i/5}I_R.
$$

::: {.proof}
The lower ray is the positive real axis, so its contribution is $I_R$.
On the upper ray write
$$
z=xe^{2\pi i/5},
$$
with $x$ decreasing from $R$ to $0$. Then
$$
z^5=x^5,
\qquad
dz=e^{2\pi i/5}\,dx.
$$
Hence the upper-ray integral is
$$
\int_R^0
\frac{e^{2\pi i/5}}{1+x^5}\,dx
=
-e^{2\pi i/5}I_R.
$$
:::

<1>3. The integral over the circular arc of $C_R$ tends to zero as
$R\to\infty$.

::: {.proof}
On the arc,
$$
\abs{1+z^5}
\geq
R^5-1.
$$
Its length is $2\pi R/5$, so the estimation lemma gives
$$
\left|
\int_{\text{arc}}f(z)\,dz
\right|
\leq
\frac{2\pi R/5}{R^5-1}
\longrightarrow0.
$$
:::

<1>4. If
$$
I=\int_0^\infty\frac{dx}{1+x^5},
$$
then
$$
\left(1-e^{2\pi i/5}\right)I
=
\frac{2\pi i}{5\zeta^4}.
$$

::: {.proof}
By the residue theorem and steps <1>1--<1>2,
$$
\left(1-e^{2\pi i/5}\right)I_R
+
\int_{\text{arc}}f(z)\,dz
=
2\pi i\frac{1}{5\zeta^4}.
$$
Now let $R\to\infty$ and use step <1>3.
:::

<1>5. The value of the integral is
$$
\boxed{
\frac{\pi}{5\sin(\pi/5)}
}.
$$

::: {.proof}
Put
$$
\theta=\frac{\pi}{5},
\qquad
\zeta=e^{i\theta}.
$$
Then
$$
1-e^{2i\theta}
=
-2ie^{i\theta}\sin\theta.
$$
Using step <1>4,
$$
\begin{aligned}
I
&=
\frac{2\pi i e^{-4i\theta}}
{5(1-e^{2i\theta})}\\
&=
-\frac{\pi e^{-5i\theta}}{5\sin\theta}\\
&=
\frac{\pi}{5\sin(\pi/5)},
\end{aligned}
$$
because $e^{-5i\theta}=e^{-i\pi}=-1$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested value.
:::
:::
