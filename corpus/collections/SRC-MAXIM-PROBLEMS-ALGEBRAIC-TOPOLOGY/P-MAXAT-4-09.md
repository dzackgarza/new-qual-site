---
schema: qual/card@1
id: P-MAXAT-4-09
kind: problem
title: The first $p$-torsion in $\pi_*(S^3)$ is $\ZZ_p$ in degree $2p$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 4, problem 9 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that the p-torsion in $\pi _ { i } ( S ^ { 3 } )$ appears first for $i = 2 p$ and it is $\ZZ _ { p } .$
:::

::: {.solution}

Fix a prime $p$. Let
$$
u:S^3\longrightarrow K(\ZZ,3)
$$
represent the fundamental class in
$$
H^3(S^3;\ZZ)\cong\ZZ,
$$
and let $F$ be its homotopy fiber.

The calculation below is the standard proof of Serre's first-$p$-torsion
theorem; see, for example, D. Ravenel, *Complex Cobordism and Stable
Homotopy Groups of Spheres*, Lemma 1.2.3 and Corollary 1.2.4.

::: pf

::: {.pf-step #s1-1}

There is a fibration
$$
K(\ZZ,2)
\longrightarrow
F
\longrightarrow
S^3.
$$


::: pf-proof

By definition, $F$ is the homotopy fiber of
$$
u:S^3\to K(\ZZ,3).
$$
The fiber of the path-space fibration over $K(\ZZ,3)$ is
$$
\Omega K(\ZZ,3)
\simeq
K(\ZZ,2).
$$
Pulling that path-space fibration back along $u$ gives the displayed
fibration.

:::

:::

::: {.pf-step #s1-2}

The map $u$ induces an isomorphism on $\pi_3$, and therefore
$$
\pi_i(F)
=
0
\quad(i\le3),
$$
while
$$
\pi_i(F)
\cong
\pi_i(S^3)
\quad(i>3).
$$


::: pf-proof

Since $S^3$ is $2$-connected, the Hurewicz theorem gives
$$
\pi_3(S^3)
\xrightarrow{\cong}
H_3(S^3;\ZZ)
\cong
\ZZ.
$$
The map $u$ represents the generator of
$$
H^3(S^3;\ZZ),
$$
so on $\pi_3$ it induces multiplication by $\pm1$, hence an isomorphism
$$
\pi_3(S^3)
\xrightarrow{\cong}
\pi_3(K(\ZZ,3)).
$$

The long exact homotopy sequence of
$$
F\to S^3\xrightarrow{u}K(\ZZ,3)
$$
now gives
$$
\pi_i(F)=0
\quad(i\le3).
$$
For $i>3$,
$$
\pi_i(K(\ZZ,3))=0,
$$
so the same exact sequence gives
$$
\pi_i(F)\cong\pi_i(S^3).
$$

:::

:::

::: {.pf-step #s1-3}

The cohomology Serre spectral sequence of the fibration in step
[](#s1-1){.pf-ref} has
$$
E_2^{s,t}
\cong
H^s(S^3;\ZZ)
\otimes
H^t(K(\ZZ,2);\ZZ)
\cong
\Lambda(u_3)\otimes\ZZ[c_2],
$$
where
$$
|u_3|=3,
\qquad
|c_2|=2.
$$


::: pf-proof

The base $S^3$ is simply connected, so there is no nontrivial local
coefficient action. Moreover,
$$
K(\ZZ,2)
\simeq
\CP^{\infty}
$$
and hence
$$
H^*(K(\ZZ,2);\ZZ)
\cong
\ZZ[c_2],
\qquad |c_2|=2.
$$
Finally,
$$
H^*(S^3;\ZZ)
\cong
\Lambda(u_3).
$$
Substitution into the Serre $E_2$-page gives the claim.

:::

:::

::: {.pf-step #s1-4}

The transgression satisfies
$$
d_3(c_2)=u_3.
$$


::: pf-proof

The fibration
$$
K(\ZZ,2)\to F\to S^3
$$
is obtained by pulling back the path-loop fibration of
$$
K(\ZZ,3)
$$
along the classifying map $u$.

In the path-loop fibration, the fundamental class
$$
c_2\in H^2(K(\ZZ,2);\ZZ)
$$
transgresses to the fundamental class in
$$
H^3(K(\ZZ,3);\ZZ).
$$
Naturality of transgression under pullback therefore gives
$$
d_3(c_2)=u_3.
$$

:::

:::

::: {.pf-step #s1-5}

For every $m\ge1$,
$$
d_3(c_2^m)
=
m u_3c_2^{m-1}.
$$


::: pf-proof

The Serre differential is a graded derivation. Since $|c_2|$ is even,
$$
\begin{aligned}
d_3(c_2^m)
&=
\sum_{j=0}^{m-1}
c_2^j d_3(c_2)c_2^{m-1-j}\\
&=
m u_3c_2^{m-1}
\end{aligned}
$$
by step [](#s1-4){.pf-ref}.

:::

:::

::: pf-step

The spectral sequence has no nonzero differential after $d_3$, and
for $m>1$ it yields
$$
H^{2m+1}(F;\ZZ)
\cong
\ZZ/m,
$$
while the other positive-degree cohomology groups vanish.


::: pf-proof

The $E_2$-page is supported only in base columns
$$
s=0
\quad\text{and}\quad
s=3.
$$
Therefore the only possible nonzero differential is
$$
d_3:E_3^{0,t}\to E_3^{3,t-2}.
$$

By step [](#s1-5){.pf-ref}, in fiber degree $2m$ this map is multiplication by $m$:
$$
\ZZ\langle c_2^m\rangle
\xrightarrow{\times m}
\ZZ\langle u_3c_2^{m-1}\rangle.
$$
For $m\ge1$ this map is injective. Its cokernel is
$$
\ZZ/m.
$$
The target class has total degree
$$
3+2(m-1)
=
2m+1.
$$
For $m=1$ the cokernel is zero; for $m>1$ it is $\ZZ/m$.

No later differential can occur because there are no further nonzero base
columns. Hence
$$
E_4=E_\infty,
$$
giving the stated cohomology groups.

:::

:::

::: {.pf-step #s1-7}

The homology of $F$ is
$$
H_i(F;\ZZ)
\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ/m,&i=2m, m>1,\\
0,&\text{otherwise}.
\end{cases}
$$


::: pf-proof

The universal coefficient theorem for cohomology gives short exact
sequences
$$
0
\to
\operatorname{Ext}(H_{n-1}(F),\ZZ)
\to
H^n(F;\ZZ)
\to
\operatorname{Hom}(H_n(F),\ZZ)
\to
0.
$$

The Serre spectral sequence in step [](#s1-3){.pf-ref} has finitely generated entries in
every total degree, so $H_n(F;\ZZ)$ is finitely generated for every
$n$. Also $F$ is $3$-connected by step [](#s1-2){.pf-ref}.

Apply the universal coefficient sequences successively in increasing
degree. If
$$
H^{2m}(F)=0,
$$
then the sequence gives
$$
\operatorname{Ext}(H_{2m-1}(F),\ZZ)=0
$$
and
$$
\operatorname{Hom}(H_{2m}(F),\ZZ)=0.
$$
For finitely generated groups, the first equality says that
$H_{2m-1}(F)$ is torsion-free, while the second says that $H_{2m}(F)$ is
torsion. The neighboring odd-degree sequence
$$
H^{2m+1}(F)\cong\ZZ/m
$$
then forces the free group
$$
\operatorname{Hom}(H_{2m+1}(F),\ZZ)
$$
to vanish and identifies
$$
\operatorname{Ext}(H_{2m}(F),\ZZ)
\cong
\ZZ/m.
$$
Thus $H_{2m+1}(F)$ is both torsion-free from the next even-degree sequence
and torsion from this one, so it is zero. Since a finitely generated
torsion group $A$ satisfies
$$
\operatorname{Ext}(A,\ZZ)\cong A,
$$
one obtains
$$
H_{2m}(F)\cong\ZZ/m.
$$
Starting with $H_i(F)=0$ for $i\le3$, this induction gives the displayed
homology groups in every degree.

In particular, the elementary identity
$$
\operatorname{Ext}(\ZZ/m,\ZZ)
\cong
\ZZ/m,
$$
is the torsion calculation at each induction step. This is also exactly
the homology calculation in Ravenel, Lemma 1.2.3.

:::

:::

::: {.pf-step #s1-8}

Let $\mathcal C_p$ be the Serre class of finite abelian groups whose
orders are prime to $p$. Then
$$
H_i(F)\in\mathcal C_p
\quad(0<i<2p),
$$
while the $p$-primary part of
$$
H_{2p}(F)
$$
is
$$
\ZZ/p.
$$


::: pf-proof

By step [](#s1-7){.pf-ref}, the only nonzero positive homology groups below degree $2p$
are
$$
H_{2m}(F)\cong\ZZ/m
\qquad
(1<m<p).
$$
Since $m<p$, the prime $p$ does not divide $m$. Hence each such group lies
in $\mathcal C_p$.

At degree $2p$, step [](#s1-7){.pf-ref} gives
$$
H_{2p}(F)\cong\ZZ/p.
$$

:::

:::

::: {.pf-step #s1-9}

Serre's Hurewicz theorem modulo the Serre class $\mathcal C_p$
implies
$$
\pi_i(F)
$$
has no $p$-torsion for
$$
0<i<2p,
$$
and the $p$-primary subgroup of
$$
\pi_{2p}(F)
$$
is
$$
\ZZ/p.
$$


::: pf-proof

The space $F$ is simply connected, indeed $3$-connected by step [](#s1-2){.pf-ref}.
Step [](#s1-8){.pf-ref} says that, modulo the Serre class $\mathcal C_p$, its reduced
homology vanishes below degree $2p$ and is $\ZZ/p$ in degree
$2p$.

The Hurewicz theorem modulo a Serre class therefore gives the same
statement for homotopy: below the first degree not belonging to
$\mathcal C_p$, the homotopy groups lie in $\mathcal C_p$, and in that
first degree the Hurewicz map is an isomorphism modulo
$\mathcal C_p$.

Consequently the $p$-primary subgroup vanishes below degree $2p$ and is
$$
\ZZ/p
$$
in degree $2p$. This is precisely Serre's argument, recorded as Ravenel,
Corollary 1.2.4.

:::

:::

::: {.pf-step #s1-10}

For every prime $p$,
$$
\pi_i(S^3)
$$
has no $p$-torsion for
$$
3<i<2p,
$$
whereas
$$
\boxed{
\pi_{2p}(S^3)_{(p),\mathrm{tors}}
\cong
\ZZ/p.
}
$$


::: pf-proof

For every $i>3$, step [](#s1-2){.pf-ref} gives
$$
\pi_i(F)
\cong
\pi_i(S^3).
$$
Transport the conclusion of step [](#s1-9){.pf-ref} through these isomorphisms.

For $p=2$, the first relevant degree is
$$
2p=4,
$$
and the conclusion gives
$$
\pi_4(S^3)\cong\ZZ/2.
$$
For odd $p$, it gives the first $p$-primary torsion in degree $2p$.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is exactly the assertion that the first $p$-torsion in the
homotopy groups of $S^3$ occurs in $\pi_{2p}(S^3)$ and is
$$
\ZZ/p.
$$

:::

:::

:::
