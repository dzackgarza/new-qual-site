---
schema: qual/card@1
id: P-QVPRB
kind: problem
title: Cayley-Hamilton theorem for finite free modules
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Determinants
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hungerford VII.5.2 in an independent exercise reproduction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

:::{.problem}
Show that if $\phi$ is an endomorphism of a free $k$-module $E$ of finite rank, then
$p_\phi(\phi) = 0$.

*Hint: If $A$ is the matrix of $\phi$ and $B = x I_n - A$ then*
\[
B^a B = |B| I_n = p_\phi I_n \in M_n(k[x])
.\]
*If $E$ is a $k[x]$-module with structure induced by $\phi$, and $\psi$ is the $k[x]$-module endomorphism $E\to E$ with matrix given by $B$, then*
\[ 
\psi(u) = x u -\phi(u) = \phi(u) - \phi(u) = 0 && \forall u\in E
.\]

:::



::: solution
Let \(E\) be free of rank \(n\), choose a basis, and let \(A\in M_n(k)\) be the
matrix of \(\phi\). Write
\[
p_\phi(x)=\det(xI_n-A).
\]
We prove that \(p_\phi(A)=0\), which is equivalent to
\(p_\phi(\phi)=0\).

<1>1. In \(M_n(k[x])\), the adjugate identity gives
\[
\operatorname{adj}(xI_n-A)(xI_n-A)=p_\phi(x)I_n.
\]
::: proof
For every square matrix \(M\) over a commutative ring,
\[
\operatorname{adj}(M)M=\det(M)I_n.
\]
Apply this to \(M=xI_n-A\) over the polynomial ring \(k[x]\).
:::

<1>2. Give \(E\) the structure of a \(k[x]\)-module by letting \(x\) act as
\(\phi\). Then the \(k[x]\)-linear endomorphism represented by \(xI_n-A\) is the
zero map.
::: proof
For \(u\in E\), multiplication by \(x\) in this module is defined to be
\(\phi\). Hence
\[
(xI_n-A)u=xu-\phi(u)=\phi(u)-\phi(u)=0.
\]
:::

<1>3. Multiplication by \(p_\phi(x)\) on this \(k[x]\)-module is the zero map.
::: proof
The matrix identity in <1>1 represents an identity of \(k[x]\)-linear
endomorphisms of \(E\). By <1>2 its left-hand side is
\[
\operatorname{adj}(xI_n-A)\circ0=0.
\]
Therefore the right-hand side \(p_\phi(x)I_n\) also represents the zero
endomorphism. Thus
\[
p_\phi(x)u=0
\]
for every \(u\in E\).
:::

<1>4. Therefore \(p_\phi(\phi)=0\).
::: proof
By definition of the \(k[x]\)-module structure, multiplication by a polynomial
\[
a_0+a_1x+\cdots+a_mx^m
\]
acts as
\[
a_0I+a_1\phi+\cdots+a_m\phi^m.
\]
Hence the zero action of \(p_\phi(x)\) from <1>3 is exactly the identity
\[
p_\phi(\phi)=0.
\]
:::
:::
