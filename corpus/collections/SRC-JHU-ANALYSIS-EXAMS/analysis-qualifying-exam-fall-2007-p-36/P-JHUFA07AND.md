---
schema: qual/card@1
id: P-JHUFA07AND
kind: problem
title: The integral of $1/(1+x^n)$ by residue calculus
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Fall 2007 problem 4 on PDF page 36; the source gives no exponent range. The solution covers every real n and in particular all positive integers, and removes the trailing parenthesis."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked divergence for n at most one, the branch on the annular sector for nonintegral n, its unique pole, both arc estimates and the phase cancellation giving the real value."
---

::: problem
For real $n$, determine when $\int_0^\infty (1+x^n)^{-1}\,dx$
converges, and use residue calculus to evaluate it when finite.
:::

::: solution
The integral diverges to $+\infty$ for $n\leq1$. For $n>1$,
$$
\boxed{\int_0^\infty\frac{dx}{1+x^n}
=\frac{\pi}{n\sin(\pi/n)}}.
$$

<1>1. The exact convergence range is $n>1$.

::: proof
For $n>1$, the integrand is at most one on $(0,1)$
and at most $x^{-n}$ on $[1,\infty)$, so both ends
are integrable. If $n\leq0$, it is at least $1/2$ for
$x\geq1$. If $0<n\leq1$, it is at least $1/(2x)$
there because $1+x^n\leq2x$. These comparisons prove
divergence in all the remaining real cases.
:::

<1>2. An annular sector contains exactly one simple pole.

::: proof
Fix $n>1$ and set $\theta=2\pi/n<2\pi$. Choose a
logarithm branch on an open sector slightly wider than
$0\leq\arg z\leq\theta$, and define
$z^n=\exp(n\operatorname{Log}z)$ there. This is possible
since the sector can have angular width less than $2\pi$.
For $0<\varepsilon<1<R$, integrate $F(z)=(1+z^n)^{-1}$
over the positive boundary of
$\{\varepsilon<|z|<R,\ 0<\arg z<\theta\}$.

In this sector, $z^n=-1$ requires $|z|=1$ and
$n\arg z=\pi$, so the only pole is
$\zeta=e^{i\pi/n}$. It is simple, with residue
$$
\operatorname{Res}_{\zeta}F
=\frac1{n\zeta^{n-1}}=-\frac\zeta n,
$$
because $\zeta^n=-1$. On the second radial edge,
writing $z=xe^{i\theta}$ gives $z^n=x^n$ and
$dz=e^{i\theta}dx$, with $x$ traversed from $R$ to
$\varepsilon$. Thus the two radial integrals sum to
$$
(1-e^{i\theta})\int_\varepsilon^R\frac{dx}{1+x^n}.
$$
The residue theorem gives the total contour integral
$-2\pi i\zeta/n$ [@SS03].
:::

<1>3. The arcs vanish and the phase factors simplify.

::: proof
The outer and inner arc integrals have moduli bounded by
$$
\frac{\theta R}{R^n-1}\longrightarrow0,
\qquad
\frac{\theta\varepsilon}{1-\varepsilon^n}\longrightarrow0,
$$
respectively, using the arc lengths and $|z^n|=|z|^n$.
Letting $R\to\infty$ and $\varepsilon\downarrow0$,
step <1>1 and the residue identity therefore give
$$
(1-e^{2\pi i/n})I=-\frac{2\pi i e^{i\pi/n}}n.
$$
Finally
$1-e^{2\pi i/n}=-2i e^{i\pi/n}\sin(\pi/n)$, whose
sine factor is positive for $n>1$. Dividing gives
$I=\pi/(n\sin(\pi/n))$ as claimed.
:::
:::
