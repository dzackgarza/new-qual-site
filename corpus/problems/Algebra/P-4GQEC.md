---
schema: qual/card@1
id: P-4GQEC
kind: problem
title: Structure theorem for PID-modules applied to a linear operator
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Rational Canonical Form
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Explain how the structure theorem for finitely-generated modules over a PID applies to a linear operator on a finite dimensional vector space.
:::


::: {.solution}
Let $V$ be a finite-dimensional vector space over a field $F$ and let $T\in\operatorname{End}_F(V)$.

<1>1. Regard $V$ as an $F[x]$-module by
\[
f(x)\cdot v=f(T)v.
\]
::: {.proof}
Polynomial evaluation respects addition and multiplication:
\[
(f+g)(T)=f(T)+g(T),
\qquad
(fg)(T)=f(T)g(T),
\qquad
1(T)=I.
\]
Thus the displayed rule satisfies the module axioms.
:::

<1>2. This $F[x]$-module is finitely generated and torsion.
::: {.proof}
Any $F$-basis of $V$ generates $V$ as an $F[x]$-module, so it is finitely generated. By Cayley--Hamilton, the characteristic polynomial satisfies
\[
\chi_T(T)=0,
\]
so every vector is annihilated by the nonzero polynomial $\chi_T(x)$. Hence the module is torsion.
:::

<1>3. Since $F[x]$ is a PID, the structure theorem gives monic polynomials
\[
a_1(x)\mid a_2(x)\mid\cdots\mid a_r(x)
\]
such that
\[
V\cong\bigoplus_{i=1}^r F[x]/(a_i(x))
\]
as $F[x]$-modules.
::: {.proof}
Apply the structure theorem for finitely generated torsion modules over the PID $F[x]$ to <1>2. The $a_i$ are the invariant factors of the module, hence of the operator $T$.
:::

<1>4. On the summand $F[x]/(a_i)$, multiplication by $x$ is represented by the companion matrix of $a_i$.
::: {.proof}
If $d=\deg a_i$, then the residue classes
\[
1,x,\ldots,x^{d-1}
\]
form an $F$-basis of $F[x]/(a_i)$. Multiplication by $x$ shifts this basis, and the relation $a_i(x)=0$ expresses $x^d$ as the corresponding linear combination of lower powers. This is exactly the companion matrix $C(a_i)$.
:::

<1>5. Therefore $T$ is similar to the rational canonical form
\[
C(a_1)\oplus\cdots\oplus C(a_r).
\]
::: {.proof}
Choose for each cyclic summand the basis from <1>4 and transport the direct-sum basis to $V$ through the module isomorphism in <1>3. Since multiplication by $x$ is exactly the action of $T$, its matrix is the displayed block diagonal matrix.
:::

<1>6. The invariant factors recover the characteristic and minimal polynomials:
\[
\chi_T(x)=\prod_{i=1}^r a_i(x),
\qquad
\mu_T(x)=a_r(x).
\]
::: {.proof}
The characteristic polynomial of a companion matrix $C(a_i)$ is $a_i$, so block diagonality gives the product formula. A polynomial annihilates the direct sum exactly when it is divisible by every $a_i$; because $a_1\mid\cdots\mid a_r$, their least common multiple is $a_r$. Hence the minimal polynomial is $a_r$.
:::

<1>7. Factoring the invariant factors into powers of irreducibles gives the elementary-divisor form; after passing to a splitting field, this refines to Jordan blocks.
::: {.proof}
The primary decomposition part of the PID-module structure theorem decomposes each cyclic module according to the prime-power factors of the $a_i$. Over a splitting field those irreducibles are linear, so the cyclic modules $F[x]/((x-\lambda)^e)$ correspond to Jordan blocks of size $e$ with eigenvalue $\lambda$.
:::
:::
