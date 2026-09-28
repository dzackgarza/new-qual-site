---
schema: qual/card@1
id: P-AZKKJ
kind: problem
title: Units of $R[x]$ for reduced $R$, and units of $\mathbb{Z}_4[x]$
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Nilpotence
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}

- Let $R$ be a commutative ring with no nonzero nilpotent elements.
  Show that the only units in the polynomial ring $R[x]$ are the units of $R$, regarded as constant polynomials.

- Find all units in the polynomial ring $\mathbb Z_4[x]$.
:::


::: {.solution}
<1>1. Let
\[
f(x)=a_0+a_1x+\cdots+a_nx^n\in R[x]
\]
be a unit, with inverse \(g(x)\). Then every coefficient \(a_i\) for \(i>0\) is nilpotent.
::: {.proof}
Let \(\mathfrak p\) be any prime ideal of \(R\). Reducing the identity \(fg=1\) modulo \(\mathfrak p\) gives a unit
\[
\overline f\in (R/\mathfrak p)[x].
\]
Since \(R/\mathfrak p\) is an integral domain, degrees add for nonzero polynomials. Hence the only units in \((R/\mathfrak p)[x]\) are nonzero constants. Therefore
\[
a_i\in\mathfrak p
\qquad(i>0)
\]
for every prime ideal \(\mathfrak p\). Thus each \(a_i\) belongs to the intersection of all prime ideals, which is the nilradical of \(R\); equivalently, each \(a_i\) is nilpotent.
:::

<1>2. If \(R\) has no nonzero nilpotent elements, then every unit of \(R[x]\) is a constant unit of \(R\).
::: {.proof}
By <1>1, all coefficients of positive degree vanish. Hence \(f=a_0\in R\). From \(fg=1\), comparison of constant terms gives \(a_0b_0=1\), so \(a_0\in R^\times\). Conversely every unit of \(R\) is plainly a unit in \(R[x]\).
:::

<1>3. A polynomial
\[
f(x)=a_0+a_1x+\cdots+a_nx^n\in\mathbb Z_4[x]
\]
is a unit only if \(a_0\) is odd and every \(a_i\) for \(i>0\) is even.
::: {.proof}
Reduce modulo \(2\). The image of a unit of \(\mathbb Z_4[x]\) is a unit of \(\mathbb F_2[x]\), hence must equal the nonzero constant \(1\). Therefore
\[
a_0\equiv1\pmod2,
\qquad
a_i\equiv0\pmod2\quad(i>0).
\]
:::

<1>4. Conversely, every polynomial with odd constant coefficient and even positive-degree coefficients is a unit in \(\mathbb Z_4[x]\).
::: {.proof}
Write
\[
f(x)=u+n(x),
\]
where \(u=a_0\in\{1,3\}\) is a unit and every coefficient of \(n(x)\) is divisible by \(2\), with zero constant term. Then
\[
n(x)^2=0
\]
because every coefficient of the square is divisible by \(4\). Hence
\[
f=u\bigl(1+u^{-1}n(x)\bigr)
\]
has inverse
\[
f^{-1}=u^{-1}\bigl(1-u^{-1}n(x)\bigr),
\]
since \((u^{-1}n(x))^2=0\).
:::

<1>5. Therefore the units of \(\mathbb Z_4[x]\) are exactly
\[
\boxed{
\left\{a_0+a_1x+\cdots+a_nx^n:
 a_0\in\{1,3\},\ a_i\in\{0,2\}\ (i>0)
\right\}.
}
\]
:::
