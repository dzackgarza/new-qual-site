---
schema: qual/card@1
id: P-PRELIM82S-02
kind: problem
title: The integral $\int_0^\infty x^{50}/(x^{100}+1)\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Substituted t=x^100, reducing the integral to
    (1/100) integral_0^infinity t^{51/100-1}/(1+t) dt. A keyhole-contour
    computation gives the standard identity
    integral_0^infinity t^{a-1}/(1+t) dt=pi/sin(pi a) for 0<a<1.
    Substituting a=51/100 and using
    sin(51pi/100)=cos(pi/100) gives the value.
---

::: {.problem}
Compute
\[
\int_0^\infty \frac{x^{50}}{x^{100}+1}\,dx.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

With
$$
t=x^{100},
$$
the integral becomes
$$
\frac1{100}
\int_0^\infty
\frac{t^{51/100-1}}{1+t}
\,dt.
$$

::: pf-proof

The substitution gives
$$
x=t^{1/100}
$$
and
$$
dx
=
\frac1{100}
t^{1/100-1}
\,dt.
$$
Therefore
$$
\begin{aligned}
\frac{x^{50}}{x^{100}+1}\,dx
&=
\frac{t^{1/2}}{1+t}
\frac1{100}
t^{1/100-1}
\,dt\\
&=
\frac1{100}
\frac{t^{51/100-1}}{1+t}
\,dt.
\end{aligned}
$$

:::

:::

::: pf-step

For
$$
0<a<1,
$$
set
$$
J(a)
=
\int_0^\infty
\frac{t^{a-1}}{1+t}
\,dt.
$$
This improper integral converges.

::: pf-proof

Near $0$, the integrand is bounded in absolute value by
$$
t^{a-1},
$$
whose integral converges because $a>0$. For $t\geq1$,
$$
\frac{t^{a-1}}{1+t}
\leq
t^{a-2},
$$
whose integral over $[1,\infty)$ converges because $a-2<-1$.

:::

:::

::: pf-step

On
$$
\CC\sm[0,\infty),
$$
choose the branch
$$
\Log z
=
\log\abs{z}
+
i\arg z,
\qquad
0<\arg z<2\pi,
$$
and define
$$
z^{a-1}
=
\exp\bigl((a-1)\Log z\bigr).
$$

::: pf-proof

The slit plane is a domain on which the displayed argument is continuous.
Thus $\Log z$ and hence $z^{a-1}$ are holomorphic there.

:::

:::

::: {.pf-step #s4}

Let $\Gamma_{\varepsilon,R}$ be the positively oriented keyhole
contour about the positive real axis, with inner radius $\varepsilon$ and
outer radius $R$, where
$$
0<\varepsilon<1<R.
$$
Then
$$
\int_{\Gamma_{\varepsilon,R}}
\frac{z^{a-1}}{1+z}
\,dz
=
2\pi i\,e^{i\pi(a-1)}.
$$

::: pf-proof

Inside the keyhole contour, the function
$$
\frac{z^{a-1}}{1+z}
$$
has one pole, at $z=-1$. On the chosen branch,
$$
\arg(-1)=\pi,
$$
so
$$
(-1)^{a-1}
=
e^{i\pi(a-1)}.
$$
Hence
$$
\operatorname{Res}_{z=-1}
\frac{z^{a-1}}{1+z}
=
e^{i\pi(a-1)}.
$$
The residue theorem gives the displayed contour integral.

:::

:::

::: {.pf-step #s5}

The contributions from the inner and outer circular arcs of
$\Gamma_{\varepsilon,R}$ tend to $0$ as
$$
\varepsilon\to0^+
\qquad\text{and}\qquad
R\to\infty.
$$

::: pf-proof

On the inner circle $\abs{z}=\varepsilon$,
$$
\abs{
\frac{z^{a-1}}{1+z}
}
\leq
\frac{\varepsilon^{a-1}}{1-\varepsilon}.
$$
Its length is $2\pi\varepsilon$, so the absolute value of its contribution
is at most
$$
\frac{2\pi\varepsilon^a}{1-\varepsilon}
\longrightarrow
0.
$$

On the outer circle $\abs{z}=R$,
$$
\abs{
\frac{z^{a-1}}{1+z}
}
\leq
\frac{R^{a-1}}{R-1}.
$$
Its length is $2\pi R$, so the contribution is at most
$$
\frac{2\pi R^a}{R-1}.
$$
Since $a<1$, this tends to $0$ as $R\to\infty$.

:::

:::

::: {.pf-step #s6}

In the limit
$$
\varepsilon\to0^+,
\qquad
R\to\infty,
$$
the two straight portions of the keyhole contour contribute
$$
\bigl(
1-e^{2\pi ia}
\bigr)J(a).
$$

::: pf-proof

On the upper side of the positive axis,
$$
\arg z=0,
$$
so the contribution tends to
$$
J(a).
$$

On the lower side,
$$
\arg z=2\pi,
$$
so
$$
z^{a-1}
=
e^{2\pi i(a-1)}t^{a-1}
=
e^{2\pi ia}t^{a-1}.
$$
This side is traversed from $R$ back to $\varepsilon$, so its limiting
contribution is
$$
-e^{2\pi ia}J(a).
$$
Adding the two gives the claim.

:::

:::

::: {.pf-step #s7}

For $0<a<1$,
$$
\boxed{
J(a)
=
\frac{\pi}{\sin(\pi a)}.
}
$$

::: pf-proof

Letting the two radii tend to their limits in step [](#s4){.pf-ref} and using steps
[](#s5){.pf-ref} and [](#s6){.pf-ref} gives
$$
\bigl(
1-e^{2\pi ia}
\bigr)J(a)
=
2\pi i\,e^{i\pi(a-1)}.
$$
Now
$$
1-e^{2\pi ia}
=
-2i\,e^{i\pi a}\sin(\pi a),
$$
while
$$
e^{i\pi(a-1)}
=
-e^{i\pi a}.
$$
Substitution and cancellation yield
$$
J(a)
=
\frac{\pi}{\sin(\pi a)}.
$$

:::

:::

::: {.pf-step #s8}

The requested integral equals
$$
\boxed{
\frac{\pi}
{100\cos(\pi/100)}.
}
$$

::: pf-proof

Apply step [](#s7){.pf-ref} with
$$
a=\frac{51}{100}.
$$
Step [](#s1){.pf-ref} gives
$$
\begin{aligned}
\int_0^\infty
\frac{x^{50}}{x^{100}+1}
\,dx
&=
\frac1{100}
\frac{\pi}
{\sin(51\pi/100)}\\
&=
\frac{\pi}
{100\cos(\pi/100)},
\end{aligned}
$$
because
$$
\sin\left(
\frac\pi2+\frac{\pi}{100}
\right)
=
\cos\left(
\frac{\pi}{100}
\right).
$$

:::

:::

::: pf-qed

Step [](#s8){.pf-ref} is the requested value.

:::

:::

:::
