---
schema: qual/card@1
id: P-25QBA
kind: problem
title: Translation-invariant subspaces of $L^1$ as convolution algebras relative to
  $L^2$
classification:
  areas:
  - algebra
  topics:
  - Convolution
  - Function Spaces
  - Algebras
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $M \subseteq L^1(\mathbb{R})$ be a closed, translation-invariant subspace. (1) Prove
that $M$ is a closed ideal in the convolution Banach algebra $(L^1(\mathbb{R}), *)$. (2)
Explain the connection with Wiener's Tauberian Theorem and the Fourier transform. (3)
Discuss its relation to $L^2(\mathbb{R})$ as a convolution module / algebra and the
Plancherel transform.
:::

::: {.solution}
<1>1. Let \(\tau_y f(x)=f(x-y)\). If \(f\in M\) and \(g\in L^1(\mathbb R)\), then
\[
g*f=\int_{\mathbb R} g(y)\,\tau_y f\,dy
\]
as a Bochner integral in \(L^1(\mathbb R)\).
::: {.proof}
The map \(y\mapsto \tau_y f\) is continuous from \(\mathbb R\) to \(L^1(\mathbb R)\),
hence strongly measurable. Moreover
\[
\|g(y)\tau_yf\|_1=|g(y)|\,\|f\|_1,
\]
which is integrable in \(y\). Thus the Bochner integral exists. Its value is the usual
convolution by Fubini--Tonelli.
:::

<1>2. Since \(M\) is translation invariant and closed, \(g*f\in M\). Hence \(M\) is a
closed ideal of the commutative Banach algebra \((L^1(\mathbb R),*)\).
::: {.proof}
For every \(y\), \(\tau_yf\in M\), so the integrand in <1>1 is \(M\)-valued. A
Bochner-integrable map with values in a closed linear subspace has its integral in that
subspace: approximate it in \(L^1(\mathbb R;L^1(\mathbb R))\) by simple \(M\)-valued
functions. Thus \(g*f\in M\). Closedness is part of the hypothesis, and convolution on
\(L^1(\mathbb R)\) is commutative.
:::

<1>3. Fourier transform converts the ideal structure into multiplication:
\[
\widehat{g*f}(\xi)=\widehat g(\xi)\widehat f(\xi).
\]
For a single \(f\in L^1(\mathbb R)\), Wiener's Tauberian theorem says that the closed
linear span of its translates is all of \(L^1(\mathbb R)\) if and only if \(\widehat f\)
is nowhere zero.
::: {.proof}
The convolution identity is the standard Fubini calculation for \(L^1\) functions.
Wiener's theorem is precisely the cyclicity criterion for the translation representation
on \(L^1(\mathbb R)\).
:::

<1>4. Consequently, if \(M\) contains an \(f\) with nowhere-vanishing Fourier transform,
then \(M=L^1(\mathbb R)\). More generally, if
\[
Z(M)=\{\xi\in\mathbb R:\widehat f(\xi)=0\text{ for every }f\in M\},
\]
then \(M\) is proper only if \(Z(M)\neq\varnothing\).
::: {.proof}
The first statement follows from <1>3 because \(M\) is closed and contains every
translate of \(f\). For the second, a proper closed ideal in a commutative Banach
algebra is contained in a maximal ideal. The characters of \(L^1(\mathbb R)\) are the
Fourier evaluations \(f\mapsto\widehat f(\xi)\), so containment in a maximal ideal gives
a common zero \(\xi\).
:::

<1>5. The zero set \(Z(M)\) is therefore an important spectral invariant, but it should
not be presented as a complete classification of closed ideals of \(L^1(\mathbb R)\).
::: {.proof}
Complete recovery of closed ideals from their hulls is the spectral-synthesis problem.
For non-discrete locally compact abelian groups, spectral synthesis fails in general, so
distinct closed ideals can have the same hull.
:::

<1>6. The correct \(L^2\) relation is module-theoretic rather than algebraic. If
\(a\in L^1(\mathbb R)\) and \(h\in L^2(\mathbb R)\), then
\[
\|a*h\|_2\le \|a\|_1\|h\|_2,
\]
so \(L^2(\mathbb R)\) is a Banach module over \(L^1(\mathbb R)\).
::: {.proof}
This is Young's convolution inequality in the \(L^1*L^2\to L^2\) case.
:::

<1>7. In contrast, \(L^2(\mathbb R)\) is not a convolution algebra in general.
::: {.proof}
Let \(u(x)=(1+|x|)^{-2/3}\). Then \(u\in L^2(\mathbb R)\). For \(x\ge 3\), restricting
the convolution integral to \(y\in[x/3,2x/3]\) gives
\[
(u*u)(x)\ge Cx\cdot x^{-2/3}x^{-2/3}=Cx^{-1/3}.
\]
Hence \(u*u\notin L^2(\mathbb R)\). Thus convolution does not make all of \(L^2\) into
an algebra.
:::

<1>8. Under the unitary Fourier--Plancherel transform
\(\mathcal F:L^2(\mathbb R)\to L^2(\mathbb R)\), the \(L^1\)-module action becomes
multiplication:
\[
\mathcal F(a*h)=\widehat a\,\mathcal Fh.
\]
::: {.proof}
First prove the identity for \(h\in L^1\cap L^2\). Since \(\widehat a\in L^\infty\) and
convolution by \(a\) is bounded on \(L^2\) by <1>6, density of \(L^1\cap L^2\) in
\(L^2\) extends the identity to every \(h\in L^2\).
:::

<1>9. Closed translation-invariant subspaces of \(L^2(\mathbb R)\) are exactly the
inverse Fourier transforms of spaces \(L^2(E)\) for measurable sets
\(E\subseteq\mathbb R\).
::: {.proof}
Translations become multiplication by the characters \(e^{-iy\xi}\). If
\(V\subseteq L^2\) is closed and invariant under every translation, it is also invariant
under every inverse translation, so its orthogonal projection commutes with all
character multipliers. The von Neumann algebra generated by those multipliers is the
algebra of multiplication operators by \(L^\infty\)-functions. Hence the projection is
multiplication by an idempotent \(L^\infty\)-function, necessarily \(1_E\) for a
measurable set \(E\). Therefore \(\mathcal F(V)=L^2(E)\).
:::

<1>10. Thus the three viewpoints fit together as follows: translation invariance in
\(L^1\) is the same as closed-ideal behavior under convolution; Wiener detects cyclicity
through Fourier zeros; and on \(L^2\), convolution by \(L^1\)-functions becomes bounded
multiplication under Plancherel, with translation-invariant closed subspaces classified
by measurable spectral support.
::: {.proof}
Combine <1>2--<1>9.
:::
:::
