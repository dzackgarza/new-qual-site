---
schema: qual/card@1
id: P-UCLAB18F-06
kind: problem
title: A parameter integral and its C1 inverse
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
For $x>0$ define
$$
F(x)=\int_0^\infty\frac{1-e^{-tx}}{t^{3/2}}\,dt.
$$
Show that $F:(0,\infty)\to(0,\infty)$ is well-defined, bijective, of class $C^1$, and has a $C^1$ inverse.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x>0$, the improper integral
$$
F(x)
=
\int_0^\infty
\frac{1-e^{-tx}}{t^{3/2}}
\,dt
$$
converges.


::: pf-proof

Split the integral at $t=1$.

For
$$
0<t\le1,
$$
the elementary inequality
$$
0\le1-e^{-u}\le u
$$
for $u\ge0$ gives
$$
0
\le
\frac{1-e^{-tx}}{t^{3/2}}
\le
\frac{tx}{t^{3/2}}
=
x\,t^{-1/2}.
$$
The majorant is integrable on $(0,1]$.

For
$$
t\ge1,
$$
one has
$$
0\le1-e^{-tx}\le1,
$$
so
$$
0
\le
\frac{1-e^{-tx}}{t^{3/2}}
\le
t^{-3/2},
$$
which is integrable on $[1,\infty)$.
Thus the integral converges absolutely.

:::

:::

::: {.pf-step #s1-2}

For $x>0$, the substitution
$$
u=tx
$$
gives
$$
F(x)
=
\sqrt{x}
\int_0^\infty
\frac{1-e^{-u}}{u^{3/2}}
\,du.
$$


::: pf-proof

With
$$
t=\frac ux,
\qquad
dt=\frac{du}{x},
$$
one has
$$
t^{-3/2}dt
=
\left(\frac ux\right)^{-3/2}\frac{du}{x}
=
x^{1/2}u^{-3/2}\,du.
$$
Substitute into the convergent improper integral from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_0^\infty
\frac{1-e^{-u}}{u^{3/2}}
\,du
=
2\sqrt{\pi}.
$$


::: pf-proof

Integrate by parts on
$$
[\varepsilon,R]
$$
with
$$
a(u)=1-e^{-u},
\qquad
db=u^{-3/2}\,du.
$$
Then
$$
da=e^{-u}\,du,
\qquad
b=-2u^{-1/2}.
$$
Hence
$$
\begin{aligned}
\int_\varepsilon^R
\frac{1-e^{-u}}{u^{3/2}}\,du
&=
\left[
-2(1-e^{-u})u^{-1/2}
\right]_\varepsilon^R\\
&\quad+
2\int_\varepsilon^R
e^{-u}u^{-1/2}\,du.
\end{aligned}
$$

As
$$
R\to\infty,
$$
the boundary term at $R$ tends to $0$.
As
$$
\varepsilon\to0^+,
$$
one has
$$
1-e^{-\varepsilon}\sim\varepsilon,
$$
so
$$
(1-e^{-\varepsilon})\varepsilon^{-1/2}\to0.
$$
Therefore
$$
\int_0^\infty
\frac{1-e^{-u}}{u^{3/2}}\,du
=
2\int_0^\infty e^{-u}u^{-1/2}\,du.
$$
Using
$$
\Gamma\!\left(\frac12\right)=\sqrt{\pi},
$$
the final integral equals
$$
2\sqrt{\pi}.
$$

:::

:::

::: {.pf-step #s1-4}

Consequently
$$
\boxed{F(x)=2\sqrt{\pi x}}
$$
for every $x>0$.


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}:
$$
F(x)
=
\sqrt{x}\cdot2\sqrt{\pi}
=
2\sqrt{\pi x}.
$$

:::

:::

::: {.pf-step #s1-5}

The map
$$
F:(0,\infty)\to(0,\infty)
$$
is bijective.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
F(x)=2\sqrt{\pi}\sqrt{x}.
$$
The square-root function is strictly increasing on $(0,\infty)$, so $F$ is injective.

Also
$$
\lim_{x\to0^+}F(x)=0
$$
and
$$
\lim_{x\to\infty}F(x)=\infty.
$$
Since $F$ is continuous and strictly increasing, its image is exactly $(0,\infty)$.
Thus it is surjective.

:::

:::

::: {.pf-step #s1-6}

The function $F$ is of class $C^1$ on $(0,\infty)$, with
$$
\boxed{
F'(x)
=
\frac{\sqrt{\pi}}{\sqrt{x}}
}.
$$


::: pf-proof

Differentiate the explicit formula from step [](#s1-4){.pf-ref}:
$$
F(x)
=
2\sqrt{\pi}\,x^{1/2}.
$$
Then
$$
F'(x)
=
2\sqrt{\pi}\cdot\frac12x^{-1/2}
=
\sqrt{\pi}\,x^{-1/2}.
$$
This derivative is continuous for $x>0$.

:::

:::

::: {.pf-step #s1-7}

The inverse of $F$ is
$$
\boxed{
F^{-1}(y)
=
\frac{y^2}{4\pi}
},
\qquad
y>0.
$$


::: pf-proof

Solve
$$
y=2\sqrt{\pi x}
$$
for $x$:
$$
y^2=4\pi x,
$$
so
$$
x=\frac{y^2}{4\pi}.
$$

:::

:::

::: {.pf-step #s1-8}

The inverse is of class $C^1$ on $(0,\infty)$.


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
(F^{-1})'(y)
=
\frac{y}{2\pi},
$$
which is continuous on $(0,\infty)$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves well-definedness, step [](#s1-5){.pf-ref} proves bijectivity, step [](#s1-6){.pf-ref} proves that $F$ is $C^1$, and steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} prove that its inverse is $C^1$.

:::

:::

:::
