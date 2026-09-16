---
schema: qual/card@1
id: P-MSHRB
kind: problem
title: Nonzero smooth compactly supported function with compactly supported Fourier transform
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Fall 2013 problem 4 on PDF page 16; both the function and its Fourier transform are required to have compact support."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Justified holomorphic dependence of the Fourier integral by dominated differentiation on compact parameter sets, and verified the hypotheses for pointwise Fourier inversion."
---

::: {.problem}
Determine whether there is a nonzero smooth compactly supported function on $\mathbb{R}$ whose Fourier transform is also compactly supported?
:::

::: {.solution}
<1>1. Suppose $f$ is a nonzero smooth compactly supported function with $\widehat f$ also compactly supported.
::: {.proof}
assume such a function exists.
:::

<1>2. Since $f$ is compactly supported, $\widehat f$ extends to an entire function (the Fourier transform of a compactly supported function is entire).
::: {.proof}
Choose $S>0$ with $\operatorname{supp}f\subset[-S,S]$ and define
$$
F(\zeta)=\int_{-S}^S f(x)e^{-2\pi i x\zeta}\,dx,
\qquad\zeta\in\mathbb C.
$$
For $\zeta$ in a compact subset $K$ of the plane, the
integrand and its $\zeta$ derivative are bounded in
modulus by constant multiples of $|f(x)|$: one may use
$e^{2\pi S\sup_K|\operatorname{Im}\zeta|}$ and
$2\pi S e^{2\pi S\sup_K|\operatorname{Im}\zeta|}$.
The same bounds on a slightly larger compact set dominate
the difference quotients. Since $f\in L^1$, dominated
convergence therefore permits complex differentiation under
the integral and gives
$F'(\zeta)=\int_{-S}^S(-2\pi i x)f(x)e^{-2\pi i x\zeta}\,dx$
[@Fol13]. Hence $F$ is entire and agrees with
$\widehat f$ on the real axis.
:::

<1>3. Since $\widehat f$ is compactly supported (on $\mathbb{R}$) and entire, and it vanishes on an interval (outside its support), it vanishes identically.
::: {.proof}
The entire function $F$ vanishes on a real interval
outside the compact support of $\widehat f$. Such an
interval has an accumulation point in its domain, so
the identity theorem gives $F\equiv0$ [@SS03].
:::

<1>4. Hence $\widehat f \equiv 0$, so $f \equiv 0$ (by Fourier inversion).
::: {.proof}
Since $f\in C_c^\infty(\mathbb R)$, it is a Schwartz
function: every polynomial times every derivative of $f$
is bounded, as all derivatives have compact support.
Fourier inversion for Schwartz functions applies pointwise
and gives $f(x)=\int_{\mathbb R}\widehat f(\xi)e^{2\pi i x\xi}\,d\xi=0$
[@Ste03].
:::

<1>5. This contradicts $f$ being nonzero.
::: {.proof}
<1>4.
:::

<1>6. Hence no such nonzero function exists.
::: {.proof}
<1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
