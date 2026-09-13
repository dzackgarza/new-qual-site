---
schema: qual/card@1
id: P-ALGCOMP03-01
kind: problem
title: Coprime subgroup indices and conjugates of a proper subgroup
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the finite-index divisibility argument in part (a) and the strict conjugate-union counting bound in part (b).
---

::: {.problem}
(a) If $A$ and $B$ are subgroups of finite index in a group $G$, and $[G:A]$ and $[G:B]$ are relatively prime, prove that $G=AB$.

(b) If $H$ is a proper subgroup of a finite group $G$, prove that
\[
\bigcup_{x\in G}x^{-1}Hx\ne G.
\]
:::


::: {.solution}
<1>1. If \([G:A]\) and \([G:B]\) are coprime, then \(G=AB\).
::: {.proof}
Set
\[
m=[G:A],
\qquad
n=[G:B].
\]
Both are finite and \(\gcd(m,n)=1\). By multiplicativity of finite index,
\[
[G:A\cap B]
=[G:A][A:A\cap B]
=m[A:A\cap B],
\]
and also
\[
[G:A\cap B]
=[G:B][B:A\cap B]
=n[B:A\cap B].
\]
Hence
\[
m[A:A\cap B]=n[B:A\cap B].
\]
Since \(\gcd(m,n)=1\), it follows that
\[
n\mid[A:A\cap B].
\]

On the other hand, the map
\[
A/(A\cap B)\longrightarrow G/B,
\qquad
a(A\cap B)\longmapsto aB
\]
is injective. Therefore
\[
[A:A\cap B]\le [G:B]=n.
\]
Combining the divisibility with this inequality gives
\[
[A:A\cap B]=n.
\]
Thus the \(A\)-orbit of the coset \(B\) in \(G/B\) has size \(n\), which is the total number of cosets. Hence that orbit is all of \(G/B\). Therefore every \(g\in G\) satisfies
\[
gB=aB
\]
for some \(a\in A\), so \(g\in aB\subseteq AB\). Hence
\[
\boxed{G=AB}.
\]
:::

<1>2. A finite group is not the union of the conjugates of a proper subgroup.
::: {.proof}
Let
\[
N=N_G(H)=\{g\in G:g^{-1}Hg=H\}.
\]
The number of distinct conjugates of \(H\) is
\[
r=[G:N].
\]
Every conjugate has \(|H|\) elements, and all conjugates contain the identity. Therefore, even if we ignore every other possible overlap,
\[
\left|\bigcup_{x\in G}x^{-1}Hx\right|
\le 1+r(|H|-1).
\]
Since \(H\le N\), we have \(|N|\ge|H|\), hence
\[
r=[G:N]\le [G:H]=\frac{|G|}{|H|}.
\]
Thus
\[
\left|\bigcup_{x\in G}x^{-1}Hx\right|
\le
1+\frac{|G|}{|H|}(|H|-1)
=1+|G|-\frac{|G|}{|H|}.
\]
Because \(H\) is proper,
\[
[G:H]=\frac{|G|}{|H|}\ge2.
\]
Therefore
\[
1+|G|-\frac{|G|}{|H|}\le |G|-1<|G|.
\]
Consequently
\[
\boxed{\bigcup_{x\in G}x^{-1}Hx\ne G}.
\]
:::
:::
