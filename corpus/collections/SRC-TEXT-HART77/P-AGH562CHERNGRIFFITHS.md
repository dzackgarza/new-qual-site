---
schema: qual/card@1
id: P-AGH562CHERNGRIFFITHS
kind: problem
title: Chern-Griffiths theorem bounding the geometric genus by the degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Canonical Divisor
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Hartshorne V.6.2 transcription and collection context,
    and the retained Hartshorne V migration ledger, which records that the
    V.6.2 statement and its Clifford/Riemann--Roch/Kodaira hint were compared
    with the source. The retained Hartshorne solution attachment ends in
    Chapter IV, so there is no V.6.2 source solution to incorporate. The
    proof below is an independent argument using a general hyperplane
    section, Clifford's theorem, adjunction, surface Riemann--Roch, and
    Kodaira vanishing.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the complete argument. Checked the hyperplane restriction bound
    h^0(C,O_C(1))>=n+1, the iterative restriction argument that nonspeciality
    forces p_g=0, and the Clifford equality case at d=2n. In the hyperelliptic
    equality case, deg L=2n and h^0(L)=n+1 make all sections pullbacks of
    H^0(P^1,O(n)), contradicting very ampleness. In the canonical equality
    case, K_X.H=0 and a nonzero canonical section force K_X~0; surface
    Riemann--Roch plus Kodaira vanishing then gives
    h^0(O_X(1))=n+2-q, while nondegeneracy gives at least n+2 sections, so
    q=0 and X is K3.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Read for issue #121 and cited the published proof of the strict-inequality
    half on the card: J. Harris, A bound on the geometric genus of projective
    varieties, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 8 (1981), §2, printed
    pp. 42--44, read in
    tmp/sources/harris-1981-bound-geometric-genus.md, whose page markers place
    §2 in its first twenty pages. Step harris-bound transcribes Harris's
    displays: M and epsilon at printed p. 42, the curve bound and the Poincaré
    residue sequence at printed p. 43, the surface bound and the corollary
    p_g = 0 for d <= k(N-k)+1 at printed p. 44; it replaces the step
    nonspecial-below-2n of the 2026-09-20 solution, whose conditional
    derivation of H^1(C,L) = 0 is subsumed. Checked against the exercise and
    its hint at Hartshorne V.6.2, printed p. 423 (PDF p. 438, printed = PDF
    minus 15), and against the book pages the other steps now name: Proposition
    8.20 printed p. 182, Theorem 5.4 printed p. 343, Theorem 1.6 printed
    p. 362 and Remark 7.15 printed p. 248. Read for the equality case: Yang
    Pi-Yeh, solution 5.6.2, printed p. 115 of
    tmp/sources/lfwin-hartshorne-solutions.pdf, read in
    tmp/sources/lfwin-hartshorne-solutions.md, both halves present and two
    steps unproved, namely H.K >= 0 in his chain 2n+2 <= 2-2g+2d <= d and the
    passage from p_a = 1 to p_g = 1. The card keeps its own steps for those
    two, and the gap is recorded in COMPLAINTS.md today. Not checked: Harris's
    §1 and §§3--5, which the card does not use, and no other published proof
    of the equality case was sought.

---

::: {.problem}
Prove the following theorem of Chern and Griffiths.
Let $X$ be a nonsingular surface of degree $d$ in $\PP_{\CC}^{n+1}$, which is not contained in any hyperplane.
If $d<2 n$, then $p_g(X)=0$.
If $d=2 n$, then either $p_g(X)=0$, or $p_g(X)=1$ and $X$ is a K3 surface.

Hint: Cut $X$ with a hyperplane and use Clifford's theorem (IV, 5.4). For the last statement, use the Riemann-Roch theorem on $X$ and the Kodaira vanishing theorem (III, 7.15).
:::

::: {.solution}
Put
$$
A=\OO_X(1).
$$
Choose a general hyperplane section
$$
C\in\linearsystem{A}.
$$
By [[T-BERTINI|Bertini's theorem]], $C$ is a smooth irreducible curve.
Write
$$
L=A\restrict_C=\OO_C(1).
$$
Then
$$
\deg L=C^2=A^2=d.
$$

::: pf

::: {.pf-step #hyperplane-restriction-sections}
The hyperplane line bundle satisfies
$$
\boxed{h^0(C,L)\ge n+1.}
$$

::: pf-proof
Since $X$ is not contained in any hyperplane, restriction of ambient
linear forms gives an injection
$$
H^0(\PP^{n+1},\OO(1))
\hookrightarrow
H^0(X,A).
$$
Thus
$$
h^0(X,A)\ge n+2.
$$

The section defining $C$ gives the exact sequence
$$
0\longrightarrow\OO_X
\longrightarrow A
\longrightarrow L
\longrightarrow0.
$$
Since $X$ is an irreducible projective variety,
$$
h^0(X,\OO_X)=1.
$$
The image of $H^0(X,A)$ in $H^0(C,L)$ therefore has dimension
$$
h^0(X,A)-1\ge n+1.
$$
Hence $h^0(C,L)\ge n+1$.

This is the opening move of the book's hint for V.6.2, printed p. 423: cut
$X$ with a hyperplane and count sections of $\OO_C(1)$.
:::

:::

::: {.pf-step #harris-bound}
If $d<2n$, then
$$
\boxed{p_g(X)=0.}
$$

::: pf-proof
This is Harris's bound on the geometric genus. J. Harris, *A bound on the
geometric genus of projective varieties*, Ann. Scuola Norm. Sup. Pisa Cl.
Sci. (4) 8 (1981), text version
`tmp/sources/harris-1981-bound-geometric-genus.md`, §2, printed pp. 42--44.
Written for a surface in $\PP^{n+1}$, with $N=n+1$, the argument is as
follows.

Put
$$
M=\left[\frac{d-1}{N-2}\right],
\qquad
\varepsilon=d-1-M(N-2).
$$
The generic hyperplane section is a nondegenerate curve $C$ of degree $d$ in
$\PP^{N-1}$ (Harris, printed p. 42), and Riemann--Roch with the count
$h^0(C,\OO_C(l))-h^0(C,\OO_C(l-1))\ge l(N-2)+1$ for $l\le M$ gives
$$
h^0(C,\omega_C(-M+l))
\le
l\varepsilon+\binom{l}{2}(N-2)
$$
(Harris, printed p. 43).

The Poincaré residue sequence of the pair $C\subset X$,
$$
0\longrightarrow\Omega^2_X(-l)
\longrightarrow\Omega^2_X(-l+1)
\longrightarrow\omega_C(-l)
\longrightarrow0,
$$
gives $h^0(X,\Omega^2_X(-M+1))=0$ and then, summing the resulting
inequalities,
$$
h^0(X,\Omega^2_X(-M+l))
\le
\sum_{i=1}^{l-1}h^0(C,\omega_C(-M+i))
$$
(Harris, printed p. 43). At $l=M$ this reads
$$
p_g(X)
=
h^0(X,\Omega^2_X)
\le
\binom{M}{3}(N-2)+\binom{M}{2}\varepsilon,
$$
which is Harris's bound at printed p. 44 for dimension two.

Now $d<2n$ means $d\le2N-3$, so
$$
M=\left[\frac{d-1}{N-2}\right]\le2.
$$
If $M\le1$, both binomial coefficients vanish and the bound is $0$. If
$M=2$, then
$$
\varepsilon=d-1-2(N-2)\le 2N-3-1-2N+4=0,
$$
while $\varepsilon\ge0$ by its definition, so $\varepsilon=0$ and the bound
is $0$ again. Hence
$$
p_g(X)=0.
$$
:::

:::

::: {.pf-step #nonspecial-implies-pg-zero}
Whenever $H^1(C,L)=0$, one has
$$
\boxed{p_g(X)=0.}
$$

::: pf-proof
Adjunction (Hartshorne, Proposition 8.20, printed p. 182) gives
$$
\omega_C
\cong
(\omega_X\otimes A)\restrict_C,
$$
and therefore
$$
\omega_X\restrict_C
\cong
\omega_C\otimes L^{-1}.
$$
Serre duality on $C$ gives
$$
H^0(C,\omega_C\otimes L^{-1})
\cong
H^1(C,L)^\vee
=0.
$$

For every $m\ge0$, tensor the hyperplane-section sequence by
$\omega_X\otimes A^{-m}$:
$$
0
\longrightarrow
\omega_X\otimes A^{-(m+1)}
\longrightarrow
\omega_X\otimes A^{-m}
\longrightarrow
\omega_C\otimes L^{-(m+1)}
\longrightarrow0.
$$
The right-hand sheaf has no nonzero global section. Indeed, if it had a
section, multiplying by any nonzero section of $L^m$ would give a nonzero
section of
$$
\omega_C\otimes L^{-1},
$$
which has none. Hence for every $m\ge0$,
$$
H^0(X,\omega_X\otimes A^{-(m+1)})
\xrightarrow{\sim}
H^0(X,\omega_X\otimes A^{-m}).
$$
Iterating,
$$
h^0(X,\omega_X)
=
h^0(X,\omega_X\otimes A^{-m})
$$
for every $m$.

For $m\gg0$, the latter space is zero. Otherwise an effective divisor
$D_m$ would satisfy
$$
D_m\sim K_X-mA,
$$
so ampleness of $A$ would give
$$
0\le A\cdot D_m
=
A\cdot K_X-mA^2,
$$
which is impossible for sufficiently large $m$ because $A^2=d>0$.
Therefore
$$
p_g(X)=h^0(X,\omega_X)=0.
$$
:::

:::

::: {.pf-step #clifford-equality-canonical}
If $d=2n$ and $L$ is special, then
$$
\boxed{L\cong\omega_C.}
$$

::: pf-proof
Clifford's theorem (Hartshorne, Theorem 5.4, printed p. 343) and step [](#hyperplane-restriction-sections){.pf-ref} give
$$
n+1
\le
h^0(C,L)
\le
\frac d2+1
=
n+1.
$$
Thus equality holds in Clifford's theorem.

The divisor class $L$ is nonzero.
If equality came from the hyperelliptic case, then $L$ would be a
multiple of the unique $g^1_2$:
$$
L\cong f^*\OO_{\PP^1}(n)
$$
for the hyperelliptic double cover
$$
f:C\to\PP^1.
$$
Pullback gives an injective map
$$
H^0(\PP^1,\OO_{\PP^1}(n))
\hookrightarrow
H^0(C,L).
$$
Both spaces have dimension $n+1$: the source has that dimension, and
equality in the preceding Clifford estimate gives
$$
h^0(C,L)=n+1.
$$
Thus every section of $L$ is pulled back from $\PP^1$ and takes the same
value on the two points of each fiber of $f$. Hence $L$ could not be very
ample.
But $L=\OO_C(1)$ is very ample because it is the restriction of the
projective embedding.

The only remaining equality case in Clifford's theorem is therefore
$$
L\cong\omega_C.
$$
:::

:::

::: {.pf-step #canonical-meets-hyperplane-zero}
In the special case of step [](#clifford-equality-canonical){.pf-ref},
$$
\boxed{K_X\cdot A=0.}
$$

::: pf-proof
Adjunction gives
$$
\omega_X\restrict_C
\cong
\omega_C\otimes L^{-1}.
$$
Step [](#clifford-equality-canonical){.pf-ref} identifies the right-hand side with $\OO_C$. Consequently
$$
\deg(\omega_X\restrict_C)=0.
$$
Since $C\sim A$, this degree is
$$
K_X\cdot A.
$$
:::

:::

::: {.pf-step #trivial-canonical-pg-one}
If $d=2n$, $L$ is special, and $p_g(X)>0$, then
$$
\boxed{\omega_X\cong\OO_X}
$$
and
$$
\boxed{p_g(X)=1.}
$$

::: pf-proof
Choose a nonzero canonical section.
Its zero divisor $D$ is effective and satisfies
$$
D\sim K_X.
$$
By step [](#canonical-meets-hyperplane-zero){.pf-ref},
$$
A\cdot D
=
A\cdot K_X
=0.
$$
Since $A$ is ample, every nonzero effective curve has positive
intersection with $A$. Hence $D=0$.

A nowhere-vanishing section of $\omega_X$ trivializes it, so
$$
\omega_X\cong\OO_X.
$$
Because $X$ is an irreducible projective variety over $\CC$,
$$
h^0(X,\OO_X)=1.
$$
Thus
$$
p_g(X)
=
h^0(X,\omega_X)
=1.
$$
:::

:::

::: {.pf-step #irregularity-zero}
Under the hypotheses of step [](#trivial-canonical-pg-one){.pf-ref},
$$
\boxed{q(X)=h^1(X,\OO_X)=0.}
$$

::: pf-proof
Put
$$
q=h^1(X,\OO_X).
$$
Step [](#trivial-canonical-pg-one){.pf-ref} gives $p_g=1$, so
$$
\chi(\OO_X)
=
1-q+p_g
=
2-q.
$$

Apply surface Riemann--Roch (Hartshorne, Theorem 1.6, printed p. 362)
[[T-SRFRR]] to $A$.
Since $K_X\sim0$ and
$$
A^2=\deg X=d=2n,
$$
one obtains
$$
\chi(A)
=
\chi(\OO_X)+\frac12A\cdot(A-K_X)
=
(2-q)+n
=
n+2-q.
$$

By Kodaira vanishing (Hartshorne, Remark 7.15, printed p. 248)
[[T-KODVAN]], using
$$
A\cong\omega_X\otimes A
$$
and the ampleness of $A$,
$$
H^i(X,A)=0
\qquad
(i>0).
$$
Hence
$$
h^0(X,A)
=
\chi(A)
=
n+2-q.
$$

The given nondegenerate embedding
$$
X\hookrightarrow\PP^{n+1}
$$
supplies $n+2$ linearly independent global sections of $A$. Therefore
$$
n+2
\le
h^0(X,A)
=
n+2-q.
$$
Thus $q\le0$, and hence
$$
q=0.
$$
:::

:::

::: {.pf-step #main-dichotomy}
If $d<2n$, then $p_g(X)=0$. If $d=2n$, then either
$p_g(X)=0$, or $p_g(X)=1$ and $X$ is a K3 surface.

::: pf-proof
For $d<2n$, step [](#harris-bound){.pf-ref} gives
$$
p_g(X)=0.
$$

Now assume $d=2n$.
If $L$ is nonspecial, step [](#nonspecial-implies-pg-zero){.pf-ref} again gives $p_g(X)=0$.
If $L$ is special, step [](#clifford-equality-canonical){.pf-ref} gives $L\cong\omega_C$.
If in addition $p_g(X)=0$, this is the first alternative in the theorem.
Otherwise steps [](#trivial-canonical-pg-one){.pf-ref} and [](#irregularity-zero){.pf-ref} give
$$
\omega_X\cong\OO_X,
\qquad
p_g(X)=1,
\qquad
q(X)=0.
$$
A smooth projective surface over $\CC$ with trivial canonical bundle and
$H^1(X,\OO_X)=0$ is a K3 surface. Hence the second alternative is exactly
that $X$ is K3.
:::

:::

::: pf-qed
Step [](#harris-bound){.pf-ref}, Harris's bound, proves the strict inequality case. Steps [](#clifford-equality-canonical){.pf-ref}, [](#canonical-meets-hyperplane-zero){.pf-ref}, [](#trivial-canonical-pg-one){.pf-ref}, [](#irregularity-zero){.pf-ref} and [](#main-dichotomy){.pf-ref}
analyze the equality case and give precisely the two alternatives stated
in the theorem.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.6, exercise 6.2, printed p. 423, text version `tmp/sources/hartshorne-1977-algebraic-geometry.md` (printed page = its marker minus 15), with the hint printed there: cut $X$ with a hyperplane and use Clifford's theorem (IV, 5.4, printed p. 343), and for the last statement use Riemann--Roch on $X$ (Theorem 1.6, printed p. 362) and Kodaira vanishing (Remark 7.15, printed p. 248).

The strict inequality is Harris's theorem. J. Harris, *A bound on the geometric genus of projective varieties*, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 8 (1981), text version `tmp/sources/harris-1981-bound-geometric-genus.md`, §2, printed pp. 42--44, bounds the geometric genus of a nondegenerate variety of dimension $k$ and degree $d$ in $\PP^N$ by
$$p_g\le\binom{M}{k+1}(N-k)+\binom{M}{k}\varepsilon,\qquad M=\left[\frac{d-1}{N-k}\right],\quad \varepsilon=d-1-M(N-k),$$
and records, immediately after it, that the geometric genus vanishes whenever $d\le k(N-k)+1$ (printed p. 44). For a surface, $k=2$ and $N=n+1$, so $d\le2n-1$, that is $d<2n$, gives $p_g(X)=0$; step [](#harris-bound){.pf-ref} transcribes the two displays this uses, at printed pp. 42--44.

The equality case $d=2n$ has no complete published proof in the sets read. Yang Pi-Yeh, *Hartshorne Solutions*, solution 5.6.2, printed p. 115 of that set (`tmp/sources/lfwin-hartshorne-solutions.pdf`; read in `tmp/sources/lfwin-hartshorne-solutions.md`), states both halves and argues the second through Clifford, adjunction, Theorems 6.1--6.3 of the book and Kodaira vanishing, but two of its steps are not proved: the chain $2n+2\le2-2g+2d\le d$ uses $H\cdot K_X\ge0$, which is what the card's step [](#clifford-equality-canonical){.pf-ref} derives from Clifford's equality case instead, and its conclusion $p_a(X)=1$ is the arithmetic genus, whereas the theorem asks for $p_g(X)=1$, which the card's steps [](#trivial-canonical-pg-one){.pf-ref} and [](#irregularity-zero){.pf-ref} give together with $q(X)=0$. Its citation of "theorem 6.2" for $\linearsystem{12K}\ne\emptyset$ is to Theorem 6.1, printed p. 421, which identifies $\kappa=-1$ with $\linearsystem{12K}=\emptyset$ and with $X$ rational or ruled, and it uses $12K=0$ without saying that $H\cdot K_X=0$ with $H$ ample forces the effective divisor in $\linearsystem{12K}$ to be zero.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.6.2, printed p. 303 of that set, text version `tmp/sources/hartshorne-solutions-egbert.md`, is a garbled sketch and is not used here.
:::
