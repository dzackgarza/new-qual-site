---
schema: qual/card@1
id: P-TIE-S15-13
kind: problem
title: 'Residue computations: rational, trigonometric, and Fourier-type integrals'
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 13.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rebuilt the run-together integral list with consecutive labels (the source repeats (v)) and added an erratum for a = 0 in (ii), against Spring 2015, question 13, page 12 of Questions_from_Tie.pdf (read from the page image).
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source labels the integrals (i)-(v), (v), (vi); the statement now numbers them (i)-(vii), so the source's second (v) is (vi) and its (vi) is (vii).
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source allows every real a in (ii), but the integral diverges at a = 0. Integral (ii) now assumes a is nonzero.
---

::: {.problem}
Compute the following integrals.

(i) $\displaystyle\int_0^\infty \frac{1}{(1+x^n)^2}\,dx$, $n \ge 1$

(ii) $\displaystyle\int_0^\infty \frac{\cos x}{(x^2+a^2)^2}\,dx$, $a \in \RR$, $a \neq 0$

(iii) $\displaystyle\int_0^\pi \frac{1}{a + \sin\theta}\,d\theta$, $a > 1$

(iv) $\displaystyle\int_0^{\frac{\pi}{2}} \frac{d\theta}{a + \sin^2\theta}$, $a > 0$.

(v) $\displaystyle\int_{\abs{z}=2} \frac{1}{(z^5-1)(z-3)}\,dz$

(vi) $\displaystyle\int_{-\infty}^\infty \frac{\sin \pi a}{\cosh \pi x + \cos \pi a}\,e^{-ix\xi}\,dx$, $0 < a < 1$, $\xi \in \RR$

(vii) $\displaystyle\int_{\abs{z}=1} \cot^2 z\,dz$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $n=1$,
$$
\int_0^\infty\frac{dx}{(1+x)^2}
=
\boxed{1}.
$$


::: pf-proof

An antiderivative is
$$
-\frac1{1+x},
$$
so
$$
\int_0^\infty\frac{dx}{(1+x)^2}
=
\left[-\frac1{1+x}\right]_{0}^{\infty}
=1.
$$

:::

:::

::: {.pf-step #s1-2}

For every integer $n>1$,
$$
\boxed{
\int_0^\infty\frac{dx}{(1+x^n)^2}
=
\frac{\pi(n-1)}
{n^2\sin(\pi/n)}.
}
$$


::: pf-proof

Set
$$
t=x^n.
$$
Then
$$
dx
=
\frac1n t^{1/n-1}\,dt,
$$
and therefore
$$
\int_0^\infty\frac{dx}{(1+x^n)^2}
=
\frac1n
\int_0^\infty
\frac{t^{1/n-1}}{(1+t)^2}\,dt.
$$
With
$$
u=\frac{t}{1+t},
$$
this becomes
$$
\frac1n
\int_0^1
u^{1/n-1}(1-u)^{1-1/n}\,du
=
\frac1n
B\left(\frac1n,2-\frac1n\right).
$$
Euler's beta-gamma identity gives
$$
B\left(\frac1n,2-\frac1n\right)
=
\Gamma\left(\frac1n\right)
\Gamma\left(2-\frac1n\right).
$$
Since
$$
\Gamma\left(2-\frac1n\right)
=
\left(1-\frac1n\right)
\Gamma\left(1-\frac1n\right),
$$
the reflection formula yields
$$
\Gamma\left(\frac1n\right)
\Gamma\left(1-\frac1n\right)
=
\frac{\pi}{\sin(\pi/n)}.
$$
Combining these identities gives
$$
\frac1n
\left(1-\frac1n\right)
\frac{\pi}{\sin(\pi/n)}
=
\frac{\pi(n-1)}
{n^2\sin(\pi/n)}.
$$

:::

:::

::: {.pf-step #s1-3}

For $a>0$,
$$
\boxed{
\int_0^\infty
\frac{\cos x}{(x^2+a^2)^2}\,dx
=
\frac{\pi e^{-a}(a+1)}{4a^3}.
}
$$


::: pf-proof

Consider
$$
F(z)
\coloneqq
\frac{e^{iz}}{(z^2+a^2)^2}
$$
and integrate over the upper semicircle of radius $R>a$. The arc integral tends to $0$ because on the arc
$$
\abs{e^{iz}}\le1
$$
and the denominator has size of order $R^4$, while the arc length is $\pi R$.

The only pole in the upper half-plane is the double pole at $z=ia$. Its residue is
$$
\begin{aligned}
\operatorname{Res}_{z=ia}F
&=
\left.
\frac{d}{dz}
\left(
\frac{e^{iz}}{(z+ia)^2}
\right)
\right|_{z=ia}\\
&=
\left.
\left(
\frac{i e^{iz}}{(z+ia)^2}
-
\frac{2e^{iz}}{(z+ia)^3}
\right)
\right|_{z=ia}\\
&=
-\frac{i e^{-a}(a+1)}{4a^3}.
\end{aligned}
$$
Hence
$$
\int_{-\infty}^{\infty}
\frac{e^{ix}}{(x^2+a^2)^2}\,dx
=
2\pi i
\operatorname{Res}_{z=ia}F
=
\frac{\pi e^{-a}(a+1)}{2a^3}.
$$
The sine part is odd, so the integral is real and equals the full-line cosine integral. Since the cosine integrand is even,
$$
2
\int_0^\infty
\frac{\cos x}{(x^2+a^2)^2}\,dx
=
\frac{\pi e^{-a}(a+1)}{2a^3},
$$
which gives the result.

:::

:::

::: {.pf-step #s1-4}

For every real $a\ne0$,
$$
\boxed{
\int_0^\infty
\frac{\cos x}{(x^2+a^2)^2}\,dx
=
\frac{\pi e^{-\abs{a}}(\abs{a}+1)}
{4\abs{a}^3}.
}
$$


::: pf-proof

The integrand depends on $a$ only through $a^2$. Thus replacing $a$ by $\abs{a}>0$ in step [](#s1-3){.pf-ref} gives the formula for every nonzero real $a$.

:::

:::

::: {.pf-step #s1-5}

For $a>1$,
$$
\boxed{
\int_0^\pi
\frac{d\theta}{a+\sin\theta}
=
\frac{2}{\sqrt{a^2-1}}
\arctan\sqrt{a^2-1}.
}
$$


::: pf-proof

Use the tangent half-angle substitution
$$
t=\tan\frac{\theta}{2},
\qquad
\sin\theta=\frac{2t}{1+t^2},
\qquad
d\theta=\frac{2\,dt}{1+t^2}.
$$
As $\theta$ runs from $0$ to $\pi$, $t$ runs from $0$ to $\infty$. Hence
$$
\begin{aligned}
\int_0^\pi
\frac{d\theta}{a+\sin\theta}
&=
\int_0^\infty
\frac{2\,dt}
{a(1+t^2)+2t}\\
&=
\frac2a
\int_0^\infty
\frac{dt}
{\left(t+\frac1a\right)^2
+\frac{a^2-1}{a^2}}.
\end{aligned}
$$
Since $a>1$,
$$
\begin{aligned}
\int_0^\pi
\frac{d\theta}{a+\sin\theta}
&=
\frac{2}{\sqrt{a^2-1}}
\left[
\arctan
\frac{at+1}{\sqrt{a^2-1}}
\right]_{0}^{\infty}\\
&=
\frac{2}{\sqrt{a^2-1}}
\left(
\frac\pi2
-
\arctan\frac1{\sqrt{a^2-1}}
\right)\\
&=
\frac{2}{\sqrt{a^2-1}}
\arctan\sqrt{a^2-1}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

For $a>0$,
$$
\boxed{
\int_0^{\pi/2}
\frac{d\theta}{a+\sin^2\theta}
=
\frac{\pi}{2\sqrt{a(a+1)}}.
}
$$


::: pf-proof

Set
$$
t=\tan\theta.
$$
Then
$$
\sin^2\theta
=
\frac{t^2}{1+t^2},
\qquad
d\theta
=
\frac{dt}{1+t^2},
$$
and $t$ runs from $0$ to $\infty$. Therefore
$$
\begin{aligned}
\int_0^{\pi/2}
\frac{d\theta}{a+\sin^2\theta}
&=
\int_0^\infty
\frac{dt}{a+(a+1)t^2}\\
&=
\frac1{\sqrt{a(a+1)}}
\left[
\arctan
\left(
t\sqrt{\frac{a+1}{a}}
\right)
\right]_{0}^{\infty}\\
&=
\frac{\pi}{2\sqrt{a(a+1)}}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

One has
$$
\boxed{
\int_{\abs{z}=2}
\frac{dz}{(z^5-1)(z-3)}
=
-\frac{\pi i}{121}.
}
$$


::: pf-proof

The poles inside $\abs{z}=2$ are the five fifth roots of unity. The only other finite pole is at $z=3$. The rational function
$$
R(z)
\coloneqq
\frac1{(z^5-1)(z-3)}
$$
is $O(z^{-6})$ at infinity, so its residue at infinity is $0$. Hence the sum of all finite residues is $0$.

At $z=3$,
$$
\operatorname{Res}_{z=3}R
=
\frac1{3^5-1}
=
\frac1{242}.
$$
Therefore the sum of the residues at the five roots of unity is
$$
-\frac1{242}.
$$
The residue theorem on $\abs{z}=2$ gives
$$
\int_{\abs{z}=2}R(z)\,dz
=
2\pi i
\left(-\frac1{242}\right)
=
-\frac{\pi i}{121}.
$$

:::

:::

::: {.pf-step #s1-8}

For $0<a<1$ and $\xi\ne0$,
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{\sin\pi a}
{\cosh\pi x+\cos\pi a}
e^{-ix\xi}\,dx
=
\frac{2\sinh(a\xi)}{\sinh\xi}.
}
$$


::: pf-proof

Set
$$
F(z)
\coloneqq
\frac{\sin\pi a}
{\cosh\pi z+\cos\pi a}
e^{-iz\xi}.
$$
Integrate $F$ around the rectangle with vertices
$$
-R,\quad R,\quad R+2i,\quad -R+2i.
$$
For fixed $\xi$, the vertical integrals tend to $0$ as $R\to\infty$, because the denominator grows like $e^{\pi R}$ while the numerator is bounded by a constant depending only on $a$ and $\xi$ on the strip $0\le\operatorname{Im}z\le2$.

Since
$$
\cosh\pi(z+2i)
=
\cosh\pi z
$$
and
$$
e^{-i\xi(z+2i)}
=
e^{2\xi}e^{-i\xi z},
$$
the top edge contributes
$$
-e^{2\xi}
\int_{-R}^{R}F(x)\,dx.
$$
Thus, after $R\to\infty$,
$$
\left(1-e^{2\xi}\right)I(\xi)
=
2\pi i
\sum \operatorname{Res}F
$$
where
$$
I(\xi)
\coloneqq
\int_{-\infty}^{\infty}
\frac{\sin\pi a}
{\cosh\pi x+\cos\pi a}
e^{-ix\xi}\,dx.
$$

The poles in the strip are
$$
z_1=i(1-a),
\qquad
z_2=i(1+a).
$$
Since
$$
\frac{d}{dz}
\left(\cosh\pi z+\cos\pi a\right)
=
\pi\sinh\pi z,
$$
their residues are
$$
\operatorname{Res}_{z=z_1}F
=
\frac{e^{\xi(1-a)}}{\pi i}
$$
and
$$
\operatorname{Res}_{z=z_2}F
=
-\frac{e^{\xi(1+a)}}{\pi i}.
$$
Hence
$$
2\pi i
\sum\operatorname{Res}F
=
-4e^\xi\sinh(a\xi).
$$
Also,
$$
1-e^{2\xi}
=
-2e^\xi\sinh\xi.
$$
Dividing gives
$$
I(\xi)
=
\frac{2\sinh(a\xi)}{\sinh\xi}.
$$

:::

:::

::: {.pf-step #s1-9}

At $\xi=0$,
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{\sin\pi a}
{\cosh\pi x+\cos\pi a}\,dx
=
2a.
}
$$


::: pf-proof

The kernel
$$
\frac{\sin\pi a}
{\cosh\pi x+\cos\pi a}
$$
is integrable on $\RR$, because it decays exponentially as $\abs{x}\to\infty$. Hence the Fourier integral in step [](#s1-8){.pf-ref} is continuous at $\xi=0$ by dominated convergence. Therefore
$$
I(0)
=
\lim_{\xi\to0}
\frac{2\sinh(a\xi)}{\sinh\xi}
=
2a.
$$

:::

:::

::: {.pf-step #s1-10}

Finally,
$$
\boxed{
\int_{\abs{z}=1}\cot^2z\,dz
=0.
}
$$


::: pf-proof

The poles of $\cot z$ occur at the integer multiples of $\pi$. Inside $\abs{z}=1$, the only pole is at $z=0$. The Laurent expansion
$$
\cot z
=
\frac1z-\frac z3+O(z^3)
$$
gives
$$
\cot^2z
=
\frac1{z^2}
-\frac23
+O(z^2).
$$
There is no $z^{-1}$ term, so
$$
\operatorname{Res}_{z=0}\cot^2z=0.
$$
The residue theorem therefore gives the stated contour integral.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} evaluate part (i), steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} evaluate part (ii) with the corrected hypothesis $a\ne0$, and steps [](#s1-5){.pf-ref} through [](#s1-10){.pf-ref} evaluate parts (iii)--(vii).

:::

:::

:::
