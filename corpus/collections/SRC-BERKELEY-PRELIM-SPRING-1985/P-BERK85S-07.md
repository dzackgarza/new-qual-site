---
schema: qual/card@1
id: P-BERK85S-07
kind: problem
title: Fourier transform of the Gaussian by a cosine integral
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Established locally uniform domination for complex b, differentiated the
    full Gaussian Fourier integral, solved F'=-2bF, and used parity to recover
    the half-line cosine integral. No restriction on b is necessary.
---

::: {.problem}
Prove that
\[
\int_0^\infty e^{-x^2}\cos(2bx)\,dx
=\frac{\sqrt\pi}{2}e^{-b^2}.
\]
What restrictions, if any, must be placed on $b$?
:::

::: {.solution}
<1>1. For every $b\in\CC$, the integral in the problem converges absolutely.

::: {.proof}
For $x\geq0$,
$$
\begin{aligned}
\abs{\cos(2bx)}
&=
\frac12\abs{e^{2ibx}+e^{-2ibx}}\\
&\leq
\frac12\left(e^{-2\operatorname{Im}(b)x}
+e^{2\operatorname{Im}(b)x}\right)\\
&\leq
e^{2\abs{\operatorname{Im}(b)}x}.
\end{aligned}
$$
Therefore
$$
\abs{e^{-x^2}\cos(2bx)}
\leq
e^{-x^2+2\abs{\operatorname{Im}(b)}x}.
$$
If $c=\abs{\operatorname{Im}(b)}$, then
$$
-x^2+2cx=-(x-c)^2+c^2,
$$
so the majorant is integrable on $[0,\infty)$.
:::

<1>2. Define
$$
F(b)\coloneqq
\int_{-\infty}^{\infty}e^{-x^2}e^{2ibx}\,dx.
$$
Then $F$ is entire and
$$
F'(b)
=
2i\int_{-\infty}^{\infty}
x e^{-x^2}e^{2ibx}\,dx.
$$

::: {.proof}
Let $K\subset\CC$ be compact and choose $M>0$ such that
$\abs{\operatorname{Im}(b)}\leq M$ for every $b\in K$. Then
$$
\abs{e^{-x^2}e^{2ibx}}
\leq
e^{-x^2+2M\abs{x}},
$$
and
$$
\abs{2ix e^{-x^2}e^{2ibx}}
\leq
2\abs{x}\,e^{-x^2+2M\abs{x}}.
$$
Both majorants are integrable on $\RR$. Hence the standard holomorphic
differentiation-under-the-integral theorem applies on every compact subset
of $\CC$, proving the claim.
:::

<1>3. For every $b\in\CC$,
$$
F'(b)=-2bF(b).
$$

::: {.proof}
By step <1>2,
$$
F'(b)
=
2i\int_{-\infty}^{\infty}
x e^{-x^2}e^{2ibx}\,dx.
$$
Since
$$
x e^{-x^2}=-\frac12\frac{d}{dx}e^{-x^2},
$$
integration by parts gives
$$
\begin{aligned}
\int_{-\infty}^{\infty}
x e^{-x^2}e^{2ibx}\,dx
&=
-\frac12
\left[e^{-x^2}e^{2ibx}\right]_{-\infty}^{\infty}
+ib
\int_{-\infty}^{\infty}
e^{-x^2}e^{2ibx}\,dx\\
&=ibF(b).
\end{aligned}
$$
The boundary term vanishes because
$$
\abs{e^{-x^2}e^{2ibx}}
\leq
e^{-x^2+2\abs{\operatorname{Im}(b)}\abs{x}}
\longrightarrow0
$$
as $\abs{x}\to\infty$. Therefore
$$
F'(b)=2i(ibF(b))=-2bF(b).
$$
:::

<1>4. For every $b\in\CC$,
$$
F(b)=\sqrt\pi\,e^{-b^2}.
$$

::: {.proof}
By step <1>3,
$$
\frac{d}{db}\left(e^{b^2}F(b)\right)
=
e^{b^2}\left(2bF(b)+F'(b)\right)
=0.
$$
Thus $e^{b^2}F(b)$ is constant on $\CC$. At $b=0$, the standard Gaussian
integral gives
$$
F(0)
=
\int_{-\infty}^{\infty}e^{-x^2}\,dx
=
\sqrt\pi.
$$
Hence the constant is $\sqrt\pi$.
:::

<1>5. For every $b\in\CC$,
$$
\boxed{
\int_0^\infty e^{-x^2}\cos(2bx)\,dx
=
\frac{\sqrt\pi}{2}e^{-b^2}
\quad\text{with no restriction on }b
}.
$$

::: {.proof}
For real $x$, the function $\cos(2bx)$ is even in $x$ and
$\sin(2bx)$ is odd in $x$. Moreover the same exponential estimate used
in step <1>1 gives
$$
\abs{\sin(2bx)}
\leq
e^{2\abs{\operatorname{Im}(b)}\abs{x}},
$$
so both the sine and cosine terms are absolutely integrable on $\RR$.
Thus the full integral may be split into its sine and cosine terms.
Therefore
$$
\begin{aligned}
F(b)
&=
\int_{-\infty}^{\infty}
e^{-x^2}\bigl(\cos(2bx)+i\sin(2bx)\bigr)\,dx\\
&=
2\int_0^\infty e^{-x^2}\cos(2bx)\,dx.
\end{aligned}
$$
Apply step <1>4 and divide by $2$. Since step <1>1 holds for every
$b\in\CC$, no restriction on $b$ is required.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves both assertions.
:::
:::
