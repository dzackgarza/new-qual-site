---
schema: qual/card@1
id: P-JHUMAY06ANI
kind: problem
title: 'The Fourier transform of an $L^1$ function is uniformly continuous and vanishes at infinity'
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Riemann-Lebesgue Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked May 2006 problem 9 on PDF page 41, including the request for a direct proof without citing Fourier-transform properties."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Handled the zero-norm case, used a positive truncation radius, made the translation sign consistent and justified L1 translation continuity independently of Fourier theory."
---

::: {.problem}
9. Suppose that f is in $L ^ { 1 } ( \mathbb { R } )$ . Prove directly (i.e., without citing properties of the Fourier transform) that the function

$$
\widehat { f } ( t ) = \int _ { \mathbb { R } } e ^ { - i x t } f ( x ) d x
$$

is uniformly continuous and ${ \widehat { f } } ( t ) \to 0 { \mathrm { ~ a s ~ } } t \to \infty$
:::

::: {.solution}
If $\|f\|_1=0$, then $f=0$ almost everywhere and
$\widehat f=0$, so both conclusions hold. Assume henceforth
that $\|f\|_1>0$.

<1>1. For $t, s \in \mathbb{R}$,
$$|\widehat f(t) - \widehat f(s)| = \left| \int_{\mathbb{R}} (e^{-ixt} - e^{-ixs}) f(x)\,dx \right| \le \int_{\mathbb{R}} |e^{-ixt} - e^{-ixs}|\,|f(x)|\,dx.$$
::: {.proof}
definition of $\widehat f$ and the triangle inequality.
:::

<1>2. $|e^{-ixt} - e^{-ixs}| = |e^{-ixs}(e^{-ix(t-s)} - 1)| = |e^{-ix(t-s)} - 1| \le |x|\,|t - s|$.
::: {.proof}
$|e^{iu} - 1| \le |u|$ for real $u$.
:::

<1>3. The defining integral is absolutely convergent and $|\widehat f(t)|\leq\|f\|_1$ for every real $t$.
::: {.proof}
Since $|e^{-ixt}|=1$ for real $x,t$, the absolute value
of the integrand is $|f(x)|$, which is integrable. The
integral triangle inequality gives the asserted bound.
:::

<1>4. For any $\varepsilon>0$, choose $R\geq1$ with $\int_{|x|>R}|f|<\varepsilon/4$.
::: {.proof}
$f \in L^1$, so the tail integral tends to $0$.
:::

<1>5. Then
$$|\widehat f(t) - \widehat f(s)| \le \int_{|x| \le R} |x|\,|t-s|\,|f(x)|\,dx + 2\int_{|x| > R} |f(x)|\,dx \le R\,|t-s|\,\|f\|_1 + \varepsilon/2.$$
::: {.proof}
<1>2 split over $|x| \le R$ and $|x| > R$, using $|e^{-ixt} - e^{-ixs}| \le 2$.
:::

<1>6. Choose $\delta = \varepsilon/(2R\|f\|_1)$; then $|t - s| < \delta$ implies $|\widehat f(t) - \widehat f(s)| < \varepsilon$.
::: {.proof}
<1>5.
:::

<1>7. Hence $\widehat f$ is uniformly continuous.
::: {.proof}
<1>6 (the choice of $\delta$ is independent of $t, s$).
:::

<1>8. For the decay: for $t \neq 0$, substitute $u = x - \pi/t$ (so $x = u + \pi/t$):
$$\widehat f(t) = \int_{\mathbb{R}} e^{-i(u + \pi/t)t} f(u + \pi/t)\,du = -\int_{\mathbb{R}} e^{-iut} f(u + \pi/t)\,du.$$
::: {.proof}
$e^{-i\pi} = -1$.
:::

<1>9. Averaging the two expressions for $\widehat f(t)$:
$$\widehat f(t) = \frac{1}{2}\int_{\mathbb{R}} e^{-ixt}\left(f(x) - f(x + \pi/t)\right)\,dx.$$
::: {.proof}
<1>8 and the original definition.
:::

<1>10. Hence $|\widehat f(t)| \le \frac{1}{2}\int_{\mathbb{R}} |f(x) - f(x + \pi/t)|\,dx \to 0$ as $|t| \to \infty$.
::: {.proof}
To justify translation continuity without Fourier theory,
given $\eta>0$ choose $\varphi\in C_c(\mathbb R)$ with
$\|f-\varphi\|_1<\eta$, using density in $L^1$ [@Fol13].
Translation invariance of the integral gives
$$
\|f(\cdot+h)-f\|_1
\leq2\eta+\|\varphi(\cdot+h)-\varphi\|_1.
$$
For $|h|\leq1$, the two compactly supported functions
on the right vanish outside one fixed bounded interval.
Uniform continuity of $\varphi$ makes their difference
tend uniformly to zero, so its $L^1$ norm tends to zero.
Letting $h\to0$ and then $\eta\downarrow0$ proves the
required translation limit. Apply it with $h=\pi/t$
in step <1>9 to obtain the asserted decay.
:::

<1>11. Therefore $\widehat f(t) \to 0$ as $t \to \infty$.
::: {.proof}
<1>10.
:::

<1>12. Q.E.D.
::: {.proof}
<1>7 and <1>11.
:::
:::
