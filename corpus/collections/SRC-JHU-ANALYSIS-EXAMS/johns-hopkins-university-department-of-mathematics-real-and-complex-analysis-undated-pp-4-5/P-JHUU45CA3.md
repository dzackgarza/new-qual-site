---
schema: qual/card@1
id: P-JHUU45CA3
kind: problem
title: Maximum modulus property forces holomorphic functions to be constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the attained maximum of the sum of two moduli with Problem 6 of the undated JHU exam on pages 4–5; no boundedness of the domain is assumed."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the zero-maximum case, choice of phases when either initial value is zero, the scalar maximum principle, and the equality argument forcing both holomorphic summands to be real-valued."
---

Let $f$ and $g$ be functions holomorphic defined on a domain $U \subseteq \mathbb{C}$.
Set $\varphi(z) = |f(z)| + |g(z)|$ for $z \in U$.
If $\varphi$ assumes a maximum value on $U$, show that both $f$ and $g$ are constants on $U$.

::: solution
Choose $z_0\in U$ where the maximum is attained and set
$M=|f(z_0)|+|g(z_0)|$. If $M=0$, the inequality
$0\leq|f(z)|+|g(z)|\leq M$ makes both functions zero.
Assume henceforth that $M>0$.

<1>1. A suitable holomorphic linear combination is constant.

::: proof
Choose complex numbers $\alpha,\beta$ of modulus one with
$\alpha f(z_0)=|f(z_0)|$ and $\beta g(z_0)=|g(z_0)|$.
For a nonzero value, take its conjugate divided by its
modulus; for a zero value, any unit complex number works.
The holomorphic function $H=\alpha f+\beta g$ satisfies
$$
|H(z)|\leq|f(z)|+|g(z)|\leq M,
\qquad H(z_0)=M.
$$
The maximum modulus principle on the connected domain
$U$ therefore gives $H\equiv M$ [@SS03].
:::

<1>2. Each summand must be constant separately.

::: proof
For every $z\in U$,
$$
\bigl(|\alpha f(z)|-\operatorname{Re}(\alpha f(z))\bigr)
+\bigl(|\beta g(z)|-\operatorname{Re}(\beta g(z))\bigr)
=\varphi(z)-M\leq0.
$$
Each term on the left is nonnegative, so both vanish.
A complex number whose real part equals its modulus
is real and nonnegative. Thus $\alpha f$ and $\beta g$
take values in $[0,\infty)$. A nonconstant holomorphic
function on a domain has open image [@SS03], which
cannot be contained in this real half-line. Hence both
$\alpha f$ and $\beta g$ are constant. Since the phases
are nonzero, $f$ and $g$ are constant as well.
:::
:::
