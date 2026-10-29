---
schema: qual/card@1
id: P-TIE-S15-14
kind: problem
title: 'Residue computations: $\frac{\sin x}{x}$, Mellin-type, and logarithmic integrals'
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 14.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rebuilt the integral list, whose labels restart at (i) across the page break, with consecutive labels against Spring 2015, question 14, pages 12-13 of Questions_from_Tie.pdf (read from the page image).
---

::: {.problem}
Compute the following integrals.

(i) $\displaystyle\int_0^\infty \frac{\sin x}{x}\,dx$

(ii) $\displaystyle\int_0^\infty \left(\frac{\sin x}{x}\right)^2 dx$

(iii) $\displaystyle\int_0^\infty \frac{x^{a-1}}{(1+x)^2}\,dx$, $0 < a < 2$

(iv) $\displaystyle\int_0^\infty \frac{\cos ax - \cos bx}{x^2}\,dx$, $a, b > 0$

(v) $\displaystyle\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx$, $0 < a < n$

(vi) $\displaystyle\int_0^\infty \frac{\log x}{1+x^n}\,dx$, $n \ge 2$

(vii) $\displaystyle\int_0^\infty \frac{\log x}{(1+x^2)^2}\,dx$

(viii) $\displaystyle\int_0^\pi \log\abs{1 - a\sin\theta}\,d\theta$, $a \in \CC$
:::

::: {.remark}
The source labels the first three integrals (i)–(iii) and then, at the top of the next page, restarts the labels at (i) for the remaining five, (i)–(v); here they are numbered consecutively (i)–(viii).
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The Dirichlet integral is
$$
\boxed{
\int_0^\infty\frac{\sin x}{x}\,dx
=
\frac\pi2.
}
$$


::: pf-proof

For $\varepsilon>0$ and $b\ge0$, define
$$
F_\varepsilon(b)
\coloneqq
\int_0^\infty
e^{-\varepsilon x}
\frac{\sin(bx)}{x}\,dx.
$$
Differentiation under the integral sign is justified by the integrable majorant $e^{-\varepsilon x}$, and gives
$$
F_\varepsilon'(b)
=
\int_0^\infty
e^{-\varepsilon x}\cos(bx)\,dx
=
\frac{\varepsilon}{\varepsilon^2+b^2}.
$$
Since $F_\varepsilon(0)=0$,
$$
F_\varepsilon(1)
=
\int_0^1
\frac{\varepsilon}{\varepsilon^2+b^2}\,db
=
\arctan\frac1\varepsilon.
$$

As $\varepsilon\downarrow0$,
$$
F_\varepsilon(1)\longrightarrow\frac\pi2.
$$
It remains to identify this with the ordinary improper integral. For $R>0$, the function
$$
h_\varepsilon(x)
\coloneqq
\frac{e^{-\varepsilon x}}{x}
$$
is positive and decreasing, so Dirichlet's estimate gives
$$
\abs{
\int_R^\infty
h_\varepsilon(x)\sin x\,dx
}
\le
\frac{2}{R}
$$
uniformly in $\varepsilon\ge0$. On $[0,R]$, dominated convergence applies as $\varepsilon\downarrow0$. Thus the Abel-regularized integrals converge to the ordinary improper integral, proving the value $\pi/2$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{
\int_0^\infty
\left(\frac{\sin x}{x}\right)^2dx
=
\frac\pi2.
}
$$


::: pf-proof

Since
$$
\sin^2x
=
\frac{1-\cos2x}{2},
$$
we have
$$
\int_0^\infty
\left(\frac{\sin x}{x}\right)^2dx
=
\frac12
\int_0^\infty
\frac{1-\cos2x}{x^2}\,dx.
$$
Integrating by parts,
$$
\int_0^\infty
\frac{1-\cos2x}{x^2}\,dx
=
2
\int_0^\infty
\frac{\sin2x}{x}\,dx.
$$
The boundary term vanishes at both $0$ and $\infty$. With $u=2x$ and step [](#s1-1){.pf-ref},
$$
\int_0^\infty
\frac{\sin2x}{x}\,dx
=
\int_0^\infty
\frac{\sin u}{u}\,du
=
\frac\pi2.
$$
Hence the integral in the first display equals
$$
\frac12\cdot2\cdot\frac\pi2
=
\frac\pi2.
$$

:::

:::

::: {.pf-step #s1-3}

For $0<a<2$,
$$
\boxed{
\int_0^\infty
\frac{x^{a-1}}{(1+x)^2}\,dx
=
\frac{\pi(1-a)}{\sin\pi a},
}
$$
with the removable value
$$
\boxed{1}
$$
at $a=1$.


::: pf-proof

Euler's beta integral gives
$$
\int_0^\infty
\frac{x^{a-1}}{(1+x)^2}\,dx
=
B(a,2-a)
=
\Gamma(a)\Gamma(2-a).
$$
Using
$$
\Gamma(2-a)
=(1-a)\Gamma(1-a)
$$
and the reflection formula
$$
\Gamma(a)\Gamma(1-a)
=
\frac{\pi}{\sin\pi a},
$$
we obtain
$$
\frac{\pi(1-a)}{\sin\pi a}
$$
for $a\ne1$. At $a=1$, the original integral is
$$
\int_0^\infty\frac{dx}{(1+x)^2}=1,
$$
which is also the limit of the displayed formula as $a\to1$.

:::

:::

::: {.pf-step #s1-4}

For $a,b>0$,
$$
\boxed{
\int_0^\infty
\frac{\cos ax-\cos bx}{x^2}\,dx
=
\frac\pi2(b-a).
}
$$


::: pf-proof

Integrate by parts with
$$
u=\cos ax-\cos bx,
\qquad
dv=\frac{dx}{x^2}.
$$
The boundary term
$$
-\frac{\cos ax-\cos bx}{x}
$$
vanishes at both endpoints: near $0$ the numerator is $O(x^2)$, and at infinity it is bounded. Thus
$$
\begin{aligned}
\int_0^\infty
\frac{\cos ax-\cos bx}{x^2}\,dx
&=
-a
\int_0^\infty
\frac{\sin ax}{x}\,dx
+
b
\int_0^\infty
\frac{\sin bx}{x}\,dx.
\end{aligned}
$$
For any $c>0$, the substitution $u=cx$ and step [](#s1-1){.pf-ref} give
$$
\int_0^\infty
\frac{\sin cx}{x}\,dx
=
\frac\pi2.
$$
Hence the result is
$$
-a\frac\pi2+b\frac\pi2
=
\frac\pi2(b-a).
$$

:::

:::

::: {.pf-step #s1-5}

For $0<a<n$,
$$
\boxed{
\int_0^\infty
\frac{x^{a-1}}{1+x^n}\,dx
=
\frac{\pi}{n}
\csc\frac{\pi a}{n}.
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
\frac1n t^{1/n-1}\,dt
$$
and
$$
x^{a-1}dx
=
\frac1n t^{a/n-1}\,dt.
$$
Therefore
$$
\int_0^\infty
\frac{x^{a-1}}{1+x^n}\,dx
=
\frac1n
\int_0^\infty
\frac{t^{a/n-1}}{1+t}\,dt.
$$
Since $0<a/n<1$, Euler's beta integral and the reflection formula give
$$
\int_0^\infty
\frac{t^{a/n-1}}{1+t}\,dt
=
\Gamma\left(\frac an\right)
\Gamma\left(1-\frac an\right)
=
\frac{\pi}{\sin(\pi a/n)}.
$$
Multiplying by $1/n$ gives the formula.

:::

:::

::: {.pf-step #s1-6}

For $n\ge2$,
$$
\boxed{
\int_0^\infty
\frac{\log x}{1+x^n}\,dx
=
-\frac{\pi^2}{n^2}
\csc\frac{\pi}{n}
\cot\frac{\pi}{n}.
}
$$


::: pf-proof

For $0<a<n$, define
$$
I_n(a)
\coloneqq
\int_0^\infty
\frac{x^{a-1}}{1+x^n}\,dx.
$$
On a small closed interval around $a=1$ contained in $(0,n)$, differentiation under the integral sign is justified by integrable bounds at both $0$ and $\infty$. Hence
$$
I_n'(1)
=
\int_0^\infty
\frac{\log x}{1+x^n}\,dx.
$$
By step [](#s1-5){.pf-ref},
$$
I_n(a)
=
\frac{\pi}{n}
\csc\frac{\pi a}{n}.
$$
Differentiating,
$$
I_n'(a)
=
-\frac{\pi^2}{n^2}
\csc\frac{\pi a}{n}
\cot\frac{\pi a}{n}.
$$
Setting $a=1$ gives the stated value.

:::

:::

::: {.pf-step #s1-7}

One has
$$
\boxed{
\int_0^\infty
\frac{\log x}{(1+x^2)^2}\,dx
=
-\frac\pi4.
}
$$


::: pf-proof

For $0<a<4$, set
$$
J(a)
\coloneqq
\int_0^\infty
\frac{x^{a-1}}{(1+x^2)^2}\,dx.
$$
With $t=x^2$,
$$
J(a)
=
\frac12
B\left(\frac a2,2-\frac a2\right).
$$
Using the beta-gamma identity, the recurrence for $\Gamma$, and the reflection formula,
$$
\begin{aligned}
J(a)
&=
\frac12
\Gamma\left(\frac a2\right)
\Gamma\left(2-\frac a2\right)\\
&=
\frac{\pi(2-a)}
{4\sin(\pi a/2)}.
\end{aligned}
$$
Differentiation under the integral sign is valid near $a=1$, so
$$
J'(1)
=
\int_0^\infty
\frac{\log x}{(1+x^2)^2}\,dx.
$$
Differentiating the closed form at $a=1$, where
$$
\cot\frac\pi2=0,
$$
gives
$$
J'(1)
=
-\frac\pi4.
$$

:::

:::

::: {.pf-step #s1-8}

For $a\in\CC$, choose a root $q$ of
$$
a q^2-2q+a=0
$$
with $\abs{q}\le1$; for $a=0$, take $q=0$. Define
$$
T(q)
\coloneqq
\sum_{k=0}^{\infty}
\frac{(-1)^kq^{2k+1}}{(2k+1)^2}.
$$
Then
$$
\boxed{
\int_0^\pi
\log\abs{1-a\sin\theta}\,d\theta
=
-\pi\log\abs{1+q^2}
-
4\operatorname{Re}T(q).
}
$$


::: pf-proof

If $a=0$, take $q=0$, for which the displayed formula is immediate. Assume now that $a\ne0$. The two roots of
$$
a q^2-2q+a=0
$$
have product $1$, so at least one has modulus at most $1$. For such a root,
$$
a
=
\frac{2q}{1+q^2}.
$$

Set
$$
\phi
\coloneqq
\theta-\frac\pi2.
$$
Then
$$
\sin\theta=\cos\phi
$$
and
$$
1-a\cos\phi
=
\frac{
(1-qe^{i\phi})(1-qe^{-i\phi})
}{1+q^2}.
$$
Hence
$$
\begin{aligned}
\int_0^\pi
\log\abs{1-a\sin\theta}\,d\theta
&=
-\pi\log\abs{1+q^2}\\
&\quad+
2
\int_{-\pi/2}^{\pi/2}
\log\abs{1-qe^{i\phi}}\,d\phi.
\end{aligned}
$$

If $\abs{q}<1$, then
$$
\log(1-qe^{i\phi})
=
-\sum_{n=1}^{\infty}
\frac{q^ne^{in\phi}}{n}
$$
uniformly on the integration interval. Taking real parts and integrating term by term,
$$
\begin{aligned}
\int_{-\pi/2}^{\pi/2}
\log\abs{1-qe^{i\phi}}\,d\phi
&=
-2\operatorname{Re}
\sum_{n=1}^{\infty}
\frac{q^n\sin(n\pi/2)}{n^2}\\
&=
-2\operatorname{Re}T(q).
\end{aligned}
$$
Substitution gives the formula.

If $\abs{q}=1$, apply the preceding formula for the half-circle logarithmic integral to $\rho q$ and let $\rho\uparrow1$. The series defining $T(q)$ converges absolutely, and
$$
\log\abs{1-\rho q e^{i\phi}}
$$
converges in $L^1$ to
$$
\log\abs{1-qe^{i\phi}};
$$
any singularity is logarithmic and integrable. Thus the same identity holds on the boundary by radial passage to the limit.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-8){.pf-ref} evaluate parts (i)--(viii), respectively.

:::

:::

:::
