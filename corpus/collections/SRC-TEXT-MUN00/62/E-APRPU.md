---
schema: qual/card@1
id: E-APRPU
kind: problem
title: Higher-dimensional separation theorems from the no-retraction theorem
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Suppose you are given that there is no retraction of $B^n$ onto $S^{n-1}$.

(a) Show the Borsuk lemma holds for $S^n$.

(b) Show that no compact contractible subspace of $S^n$ separates $S^n$.

(c) Suppose you are given also that any subspace of $S^n$ homeomorphic to $S^{n-1}$ separates $S^n$.
Prove the invariance of domain theorem in dimension $n$.
:::

::: {.solution}
Assume throughout that there is no retraction \(B^n\to S^{n-1}\).

**(a) The Borsuk lemma for \(S^n\).** Let \(a,b\in S^n\), let \(A\) be compact, and let
\[
f:A\longrightarrow S^n-\{a,b\}
\]
be continuous and injective. Assume that \(f\) is nullhomotopic. We prove that \(a\) and \(b\) lie in the same component of \(S^n-f(A)\).

Because \(A\) is compact and \(S^n\) is Hausdorff, \(f:A\to f(A)\) is a homeomorphism. Thus the inclusion
\[
j:f(A)\hookrightarrow S^n-\{a,b\}
\]
is nullhomotopic: transport a nullhomotopy of \(f\) through \(f^{-1}\). Hence it suffices to treat the special case in which the compact space itself is a compact subset of \(S^n-\{a,b\}\) and \(f=j\) is inclusion.

Identify
\[
S^n-\{b\}\cong\mathbb R^n
\]
so that \(a\) corresponds to \(0\). The assertion becomes:

> If \(A\subset\mathbb R^n-\{0\}\) is compact and the inclusion
> \(j:A\hookrightarrow\mathbb R^n-\{0\}\) is nullhomotopic, then \(0\) lies in the unbounded component of \(\mathbb R^n-A\).

Suppose instead that the component \(C\) of \(\mathbb R^n-A\) containing \(0\) is bounded. Since \(A\) is compact, \(C\cup A\) is a metrizable space. The homotopy-extension lemma used in Munkres's proof of the Borsuk lemma applies to the closed subset \(A\subset C\cup A\): because \(j\) is nullhomotopic, there is a continuous extension
\[
g:C\cup A\longrightarrow\mathbb R^n-\{0\}
\]
with \(g|_A=j\).

Let
\[
D=\mathbb R^n-C.
\]
Because \(A\) is closed, \(\mathbb R^n-A\) is locally path connected. Hence its components are open as well as closed in \(\mathbb R^n-A\). Thus \(C\) is open in \(\mathbb R^n\), so \(D\) is closed; and the union of all components of \(\mathbb R^n-A\) other than \(C\) is open in \(\mathbb R^n\), so its complement \(C\cup A\) is closed. Since \(C\cap A=\varnothing\), we have
\[
(C\cup A)\cap D=A.
\]
On this intersection \(g=j\) agrees with the identity. Hence
\[
G(x)=
\begin{cases}
g(x),&x\in C\cup A,\\
x,&x\in D
\end{cases}
\]
is a continuous map \(G:\mathbb R^n\to\mathbb R^n-\{0\}\). Since \(C\) is bounded, choose a closed ball \(B\) centered at \(0\) containing \(C\) in its interior. On \(\partial B\) we have \(G=\operatorname{id}\). Composing \(G|_B\) with radial projection
\[
r:\mathbb R^n-\{0\}\longrightarrow\partial B
\]
gives a retraction
\[
r\circ G|_B:B\longrightarrow\partial B\cong S^{n-1},
\]
contrary to the assumed no-retraction theorem. Therefore \(0\) lies in the unbounded component, which is exactly the Borsuk lemma for \(S^n\).

**(b)** Let \(A\subset S^n\) be compact and contractible. Suppose \(A\) separates \(S^n\), and choose \(a,b\) in two distinct components of \(S^n-A\). The inclusion
\[
i:A\hookrightarrow S^n-\{a,b\}
\]
is nullhomotopic: contract \(A\) to any point of \(A\), and this contraction remains inside \(A\subset S^n-\{a,b\}\). The map \(i\) is injective, so part (a) says that \(a\) and \(b\) must lie in the same component of \(S^n-A\), a contradiction. Thus no compact contractible subspace of \(S^n\) separates \(S^n\).

**(c) Invariance of domain.** Assume additionally that every embedded copy of \(S^{n-1}\) in \(S^n\) separates \(S^n\). Let \(U\subset\mathbb R^n\) be open and let
\[
f:U\to S^n
\]
be continuous and injective. Fix \(x\in U\) and choose a closed \(n\)-ball \(B\) with
\[
x\in\operatorname{Int}B\subset B\subset U.
\]
The compact set \(f(B)\) is homeomorphic to \(B\), hence contractible, so by part (b) it does not separate \(S^n\). On the other hand,
\[
f(\partial B)\cong S^{n-1}
\]
separates \(S^n\) by hypothesis. Since \(f(\operatorname{Int}B)\) is connected and disjoint from \(f(\partial B)\), it lies in one component \(V\) of \(S^n-f(\partial B)\).

We claim
\[
f(\operatorname{Int}B)=V.
\]
If \(y\in V-f(\operatorname{Int}B)\), choose \(z\) in another component of \(S^n-f(\partial B)\), which exists because \(f(\partial B)\) separates. Neither \(y\) nor \(z\) lies in \(f(B)\): the image \(f(B)\) is the disjoint union of \(f(\operatorname{Int}B)\) and \(f(\partial B)\), and the former lies entirely in \(V\). But \(S^n-f(B)\) is connected by part (b), so as a connected subset of \(S^n-f(\partial B)\) it must lie in a single component. It contains both \(y\in V\) and \(z\notin V\), contradiction. Thus the claim holds.

Hence \(f(\operatorname{Int}B)=V\) is open. Every \(x\in U\) has such a ball, so \(f\) is an open map. A continuous injective open map is a homeomorphism onto its image. Therefore \(f(U)\) is open in \(S^n\), proving invariance of domain in dimension \(n\).
:::
