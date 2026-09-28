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
Write $\norm f_1=\int_\RR\abs f$. The integral defining $\widehat f(t)$ converges absolutely, since its integrand has modulus $\abs{f(x)}$.

<1>1. $\widehat f$ is uniformly continuous.

::: {.proof}
Let $\eps>0$; we may assume $\norm f_1>0$, since otherwise $\widehat f=0$. Choose $R\ge1$ with $\int_{\abs x>R}\abs f<\eps/4$. Since $\abs{e^{iu}-1}\le\abs u$ for real $u$, and $\abs{e^{-ixt}-e^{-ixs}}\le2$,
$$\abs{\widehat f(t)-\widehat f(s)}\le\int_{\abs x\le R}\abs x\abs{t-s}\abs{f(x)}\,dx+2\int_{\abs x>R}\abs f\le R\abs{t-s}\norm f_1+\frac\eps2.$$
So $\abs{t-s}<\eps/(2R\norm f_1)$ implies $\abs{\widehat f(t)-\widehat f(s)}<\eps$, with a bound independent of $t$ and $s$.
:::

<1>2. $\norm{f(\cdot+h)-f}_1\to0$ as $h\to0$.

::: {.proof}
Given $\eta>0$, choose $\varphi\in C_c(\RR)$ with $\norm{f-\varphi}_1<\eta$ [@Fol13]. Translation invariance of the integral gives $\norm{f(\cdot+h)-f}_1\le2\eta+\norm{\varphi(\cdot+h)-\varphi}_1$. For $\abs h\le1$ both functions on the right vanish outside one bounded interval, and uniform continuity of $\varphi$ makes their difference tend uniformly to $0$, so its integral tends to $0$. Letting $h\to0$ and then $\eta\to0$ proves the claim.
:::

<1>3. $\widehat f(t)\to0$ as $\abs t\to\infty$.

::: {.proof}
For $t\ne0$, the substitution $x=u+\pi/t$ and $e^{-i\pi}=-1$ give $\widehat f(t)=-\int e^{-iut}f(u+\pi/t)\,du$. Averaging with the definition,
$$\abs{\widehat f(t)}=\frac12\abs{\int e^{-ixt}\bigl(f(x)-f(x+\pi/t)\bigr)\,dx}\le\frac12\norm{f(\cdot+\pi/t)-f}_1,$$
which tends to $0$ by step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>3 are the two claims.
:::
:::
