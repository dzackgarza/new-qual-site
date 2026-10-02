---
schema: qual/card@1
id: P-UCLARA18F-06
kind: problem
title: Wiener's theorem on translates in $L^2(\mathbb R)$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 6. Let $f\in L^2(\mathbb R)$ and assume its Fourier transform satisfies
\[
|\widehat f(\xi)|>0
\]
for Lebesgue almost every $\xi\in\mathbb R$. Prove that the set of finite linear combinations of the translates
\[
f_y(x)=f(x-y)
\]
is norm dense in $L^2(\mathbb R)$.
:::

::: {.solution}
Let
\[
M=\operatorname{span}\{f_y:y\in\mathbb R\}\subseteq L^2(\mathbb R),
\qquad
f_y(x)=f(x-y),
\]
and use the Fourier convention
\[
\widehat h(\xi)=\int_{\mathbb R}h(x)e^{-2\pi i x\xi}\,dx
\]
whenever \(h\in L^1\).

<1>1. If \(g\in M^\perp\), then for every \(y\in\mathbb R\),
\[
\int_{\mathbb R}e^{-2\pi i y\xi}\widehat f(\xi)\overline{\widehat g(\xi)}\,d\xi=0.
\]

::: {.proof}
Since \(g\perp M\), one has \(\langle f_y,g\rangle_{L^2}=0\) for every \(y\). The \(L^2\) Plancherel theorem, i.e. the unitary extension of [[PR-JCZKL|Plancherel's identity]], gives
\[
0=\langle\widehat{f_y},\widehat g\rangle_{L^2}.
\]
Translation by \(y\) satisfies
\[
\widehat{f_y}(\xi)=e^{-2\pi i y\xi}\widehat f(\xi),
\]
which yields the displayed integral.
:::

<1>2. The function
\[
h(\xi)=\widehat f(\xi)\overline{\widehat g(\xi)}
\]
belongs to \(L^1(\mathbb R)\), and \(\widehat h(y)=0\) for every \(y\in\mathbb R\).

::: {.proof}
By Cauchy--Schwarz and Plancherel,
\[
\int_{\mathbb R}|h(\xi)|\,d\xi
\le\|\widehat f\|_{L^2}\|\widehat g\|_{L^2}
=\|f\|_{L^2}\|g\|_{L^2}<\infty.
\]
Thus \(h\in L^1\). By the chosen Fourier convention,
\[
\widehat h(y)
=\int_{\mathbb R}h(\xi)e^{-2\pi i y\xi}\,d\xi,
\]
and this is zero for every \(y\) by step <1>1.
:::

<1>3. Every \(g\in M^\perp\) is zero almost everywhere.

::: {.proof}
Step <1>2 and [[PR-47TTS|injectivity of the Fourier transform on \(L^1\)]] imply
\[
h(\xi)=\widehat f(\xi)\overline{\widehat g(\xi)}=0
\]
for almost every \(\xi\). By hypothesis, \(|\widehat f(\xi)|>0\) almost everywhere, so \(\widehat g(\xi)=0\) almost everywhere. Plancherel then gives
\[
\|g\|_{L^2}=\|\widehat g\|_{L^2}=0,
\]
hence \(g=0\) in \(L^2\).
:::

<1>4. Therefore
\[
\boxed{\overline{M}^{\|\cdot\|_{L^2}}=L^2(\mathbb R)}.
\]

::: {.proof}
For any subspace \(M\) of a Hilbert space,
\[
\overline M=(M^\perp)^\perp.
\]
Step <1>3 gives \(M^\perp=\{0\}\), so \(\overline M=L^2(\mathbb R)\).
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required density of finite linear combinations of translates of \(f\).
:::
:::
