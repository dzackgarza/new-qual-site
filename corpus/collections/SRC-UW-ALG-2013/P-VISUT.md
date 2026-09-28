---
schema: qual/card@1
id: P-VISUT
kind: problem
title: Unique Galois quartic $\QQ(\sqrt{d_1},\sqrt{d_2})$ in a nonabelian Galois octic
  $K/\QQ$; $d_1,d_2>0$ when $G=Q_8$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
This question concerns an extension $K$ of $\mathbb Q$ such that $[K:\mathbb Q]=8$.
Assume that $K/\mathbb Q$ is Galois and let $G=\Gal(K/\mathbb Q)$.
Furthermore, assume that $G$ is non-abelian.

- Prove that $K$ has a unique subfield $F$ such that $F/\mathbb Q$ is Galois and $[F:\mathbb Q]=4$.

- Prove that $F$ has the form $F=\mathbb Q(\sqrt{d_1},\sqrt{d_2})$ where $d_1,d_2$ are non-zero integers.

- Suppose that $G$ is the quaternionic group.
  Prove that $d_1$ and $d_2$ are positive integers.
:::


::: {.solution}
<1>1. Since \(G\) is a nonabelian group of order \(8\), we have
\[
G\cong D_8\quad\text{or}\quad G\cong Q_8.
\]
In either case \(G\) has a unique normal subgroup \(H\) of order \(2\), namely \(Z(G)\).
::: {.proof}
The classification of groups of order \(8\) gives the three abelian groups together with \(D_8\) and \(Q_8\). Since \(G\) is nonabelian, only the latter two occur.

For \(D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), the unique normal subgroup of order \(2\) is \(\langle r^2\rangle=Z(D_8)\); the reflection subgroups of order \(2\) are conjugate and hence not normal. For \(Q_8\), the unique element of order \(2\) is \(-1\), so \(\{\pm1\}=Z(Q_8)\) is the unique subgroup of order \(2\).
:::

<1>2. There is a unique subfield \(F\subset K\) with
\[
[F:\mathbb Q]=4
\]
and \(F/\mathbb Q\) Galois.
::: {.proof}
By the Galois correspondence, subfields \(F\) with \([F:\mathbb Q]=4\) correspond to subgroups \(H\le G\) of order \(2\). Such an \(F/\mathbb Q\) is Galois exactly when \(H\trianglelefteq G\). By <1>1 there is exactly one such normal subgroup, namely \(H=Z(G)\). Thus
\[
F=K^{Z(G)}
\]
is the unique quartic Galois subfield.
:::

<1>3. The Galois group of \(F/\mathbb Q\) is
\[
\operatorname{Gal}(F/\mathbb Q)\cong C_2\times C_2.
\]
::: {.proof}
Since \(F=K^{Z(G)}\), Galois theory gives
\[
\operatorname{Gal}(F/\mathbb Q)\cong G/Z(G).
\]
For both \(D_8\) and \(Q_8\), the quotient by the center is the Klein four group.
:::

<1>4. There exist nonzero integers \(d_1,d_2\) such that
\[
F=\mathbb Q(\sqrt{d_1},\sqrt{d_2}).
\]
::: {.proof}
By <1>3, the group \(\operatorname{Gal}(F/\mathbb Q)\cong C_2^2\) has three distinct subgroups of order \(2\). Their fixed fields are three distinct quadratic extensions of \(\mathbb Q\). Choose two of them, say
\[
E_1=\mathbb Q(\sqrt{d_1}),
\qquad
E_2=\mathbb Q(\sqrt{d_2}),
\]
where \(d_1,d_2\in\mathbb Z\setminus\{0\}\) may be taken squarefree. Since \(E_1\ne E_2\), their compositum has degree
\[
[E_1E_2:\mathbb Q]=4.
\]
As \(E_1E_2\subseteq F\) and \([F:\mathbb Q]=4\), we get
\[
F=E_1E_2=\mathbb Q(\sqrt{d_1},\sqrt{d_2}).
\]
:::

<1>5. Suppose now that \(G\cong Q_8\). Then \(F\) is contained in \(\mathbb R\).
::: {.proof}
Fix the given embedding \(K\subseteq\mathbb C\). Complex conjugation restricts to an element
\[
c\in\operatorname{Gal}(K/\mathbb Q)=Q_8
\]
of order at most \(2\). If \(c=1\), then every element of \(K\), hence every element of \(F\), is real.

If \(c\ne1\), then \(c\) must be the unique element of order \(2\) in \(Q_8\), namely the central involution \(-1\). Hence
\[
\langle c\rangle=Z(Q_8),
\]
and therefore
\[
F=K^{Z(Q_8)}=K^{\langle c\rangle}.
\]
But the fixed field of complex conjugation consists precisely of the real elements of \(K\). Thus again \(F\subseteq\mathbb R\).
:::

<1>6. In the quaternionic case, \(d_1\) and \(d_2\) may be chosen positive.
::: {.proof}
By <1>5, each quadratic subfield \(E_i=\mathbb Q(\sqrt{d_i})\subseteq F\) is contained in \(\mathbb R\). A quadratic field \(\mathbb Q(\sqrt d)\) with squarefree integer \(d\) is real exactly when \(d>0\). Hence the squarefree representatives \(d_1,d_2\) in <1>4 can be chosen positive.
:::
:::
