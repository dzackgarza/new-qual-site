---
schema: qual/card@1
id: P-SJ47O
kind: problem
title: Center, linear characters, and irreducible representations of a nonabelian
  group of order $p^3$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a non-abelian group of order $p^3$ with $p$ a prime.

- Determine the order of the center $Z$ of $G$.

- Determine the number of inequivalent complex 1-dimensional representations of $G$.

- Compute the dimensions of all the inequivalent irreducible representations of $G$ and verify that the number of such representations equals the number of conjugacy classes of $G$.
:::


::: {.solution}
<1>1. The center \(Z=Z(G)\) has order \(p\).
::: {.proof}
Every nontrivial finite \(p\)-group has nontrivial center, so \(|Z|\ge p\). Since \(G\) is nonabelian, \(Z\ne G\). If \(|Z|=p^2\), then \(G/Z\) has order \(p\), hence is cyclic; but if \(G/Z(G)\) is cyclic, then \(G\) is abelian, a contradiction. Therefore
\[
|Z|=p.
\]
:::

<1>2. We have
\[
G/Z\cong C_p\times C_p
\quad\text{and}\quad
[G,G]=Z.
\]
::: {.proof}
The quotient \(G/Z\) has order \(p^2\). It cannot be cyclic, since that would force \(G\) abelian. Hence
\[
G/Z\cong C_p\times C_p.
\]
In particular \(G/Z\) is abelian, so
\[
[G,G]\subseteq Z.
\]
Because \(G\) is nonabelian, \([G,G]\ne1\). Since \(|Z|=p\), it follows that
\[
[G,G]=Z.
\]
:::

<1>3. The number of inequivalent one-dimensional complex representations of \(G\) is \(p^2\).
::: {.proof}
One-dimensional complex representations factor through the abelianization
\[
G^{\mathrm{ab}}=G/[G,G].
\]
By <1>2,
\[
|G^{\mathrm{ab}}|=|G/Z|=p^2.
\]
A finite abelian group \(A\) has exactly \(|A|\) complex linear characters. Therefore \(G\) has exactly
\[
p^2
\]
inequivalent one-dimensional representations.
:::

<1>4. Every noncentral element of \(G\) has centralizer of order \(p^2\), and hence conjugacy class of size \(p\).
::: {.proof}
Let \(x\notin Z\). Its centralizer \(C_G(x)\) contains both \(x\) and \(Z\), so it contains the subgroup \(\langle x,Z\rangle\). Since \(x\notin Z\), this subgroup has order at least \(p^2\). On the other hand \(C_G(x)\ne G\), because \(x\) is not central. Thus
\[
|C_G(x)|=p^2.
\]
By the orbit-stabilizer formula for conjugation,
\[
|x^G|=[G:C_G(x)]=p.
\]
:::

<1>5. The number of conjugacy classes of \(G\) is
\[
p^2+p-1.
\]
::: {.proof}
The \(p\) elements of \(Z\) each form a singleton conjugacy class. The remaining
\[
p^3-p
\]
elements are partitioned, by <1>4, into conjugacy classes of size \(p\). Hence the number of noncentral conjugacy classes is
\[
\frac{p^3-p}{p}=p^2-1.
\]
Thus the total number is
\[
p+(p^2-1)=p^2+p-1.
\]
:::

<1>6. Therefore \(G\) has exactly \(p-1\) nonlinear irreducible complex representations.
::: {.proof}
For a finite group, the number of inequivalent irreducible complex representations equals the number of conjugacy classes. By <1>5 there are \(p^2+p-1\) irreducibles in total, and by <1>3 exactly \(p^2\) are one-dimensional. Hence the number of nonlinear irreducibles is
\[
(p^2+p-1)-p^2=p-1.
\]
:::

<1>7. Every irreducible complex representation of \(G\) has dimension at most \(p\).
::: {.proof}
Let \(\chi\) be an irreducible character of degree \(d=\chi(1)\). By Schur's lemma, every \(z\in Z\) acts by a scalar of absolute value \(1\), so
\[
|\chi(z)|=d
\qquad(z\in Z).
\]
Character orthogonality gives
\[
\sum_{g\in G}|\chi(g)|^2=|G|=p^3.
\]
Restricting the sum to the \(p\) central elements yields
\[
pd^2\le p^3,
\]
so
\[
d\le p.
\]
:::

<1>8. Every nonlinear irreducible representation has dimension exactly \(p\).
::: {.proof}
Let the nonlinear irreducible degrees be
\[
d_1,\dots,d_{p-1}.
\]
The sum-of-squares formula gives
\[
|G|=\sum_{\rho\in\operatorname{Irr}(G)}(\dim\rho)^2.
\]
The \(p^2\) linear representations contribute \(p^2\), so
\[
\sum_{j=1}^{p-1}d_j^2=p^3-p^2=p^2(p-1).
\]
By <1>7, each \(d_j^2\le p^2\). Since there are exactly \(p-1\) terms and their sum is exactly \(p^2(p-1)\), equality must hold term-by-term:
\[
d_j=p
\qquad(1\le j\le p-1).
\]
:::

<1>9. Thus the irreducible representation degrees are
\[
\boxed{\underbrace{1,\dots,1}_{p^2\text{ times}},
\underbrace{p,\dots,p}_{p-1\text{ times}}},
\]
and their number is
\[
p^2+p-1,
\]
which agrees with the number of conjugacy classes computed in <1>5.
:::
