---
schema: qual/card@1
id: P-AGH522DECOMPSECT
kind: problem
title: Decomposability of a rank two bundle via disjoint sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.2 together with Proposition V.2.6, which identifies
    sections of P(E) with quotient line bundles of E and shows that the
    corresponding kernels are invertible sheaves.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.2, printed page 383. Checked the card's use of Proposition 2.6
    (printed page 371), which is the one-to-one correspondence between sections
    and surjections to invertible sheaves with invertible kernel, and of the
    convention of II.7 that a point of P(E) is a one-dimensional quotient of
    E_c. Searched outside the twelve retained sets and read two further
    published treatments: Algebraic Geometry II, National Taiwan University,
    2020 Spring, Chapter V homework, Exercise 2 of section 2, PDF pp. 5-6
    (tmp/sources/ntu-ag2-chapter5.pdf), which proves both directions by the
    card's argument, and Yang Pi-Yeh, Hartshorne Solutions, exercise 5.2.2,
    printed p. 102 (tmp/sources/lfwin-hartshorne-solutions.pdf), which asserts
    both directions. The card's determinant argument in step s3 is not in
    either. Not checked: nothing in the exercise depends on the characteristic.
---

::: {.problem}
Let $X$ be the ruled surface $\PP(\mathcal{E})$ over a curve $C$.
Show that $\mathcal{E}$ is decomposable if and only if there exist two sections $C^{\prime}, C^{\prime \prime}$ of $X$ such that $C^{\prime} \cap C^{\prime \prime}=\varnothing$.
:::

::: {.solution}
For a section
$$
\sigma:C\longrightarrow \PP(\mathcal E),
$$
write
$$
q_\sigma:\mathcal E\twoheadrightarrow\mathcal L_\sigma
$$
for the corresponding quotient line bundle from Proposition V.2.6, and put
$$
\mathcal N_\sigma=\ker q_\sigma.
$$
Proposition V.2.6 also shows that $\mathcal N_\sigma$ is an invertible sheaf.

::: pf

::: {.pf-step #s1}

For two sections $\sigma',\sigma''$, their images are disjoint if and
only if
$$
(\mathcal N_{\sigma'})_c\ne(\mathcal N_{\sigma''})_c
\quad\text{inside }\mathcal E_c
$$
for every $c\in C$.

::: pf-proof

Both sections lie over the identity of $C$.  Hence their images meet if and
only if there is a point $c\in C$ for which
$$
\sigma'(c)=\sigma''(c)
$$
in the fibre $\PP(\mathcal E_c)$.

Under Hartshorne's quotient convention for $\PP(\mathcal E)$, a point of
$\PP(\mathcal E_c)$ is a one-dimensional quotient of the two-dimensional
vector space $\mathcal E_c$.  Two such quotient maps determine the same point
exactly when they have the same one-dimensional kernel.  Since the quotient
sequences of Proposition V.2.6 remain exact on fibres, those kernels are
$(\mathcal N_{\sigma'})_c$ and $(\mathcal N_{\sigma''})_c$.  This proves the
claim.

:::

:::

::: {.pf-step #s2}

If $\mathcal E$ is decomposable, then $\PP(\mathcal E)$ has two
disjoint sections.

::: pf-proof

Write
$$
\mathcal E\cong\mathcal L'\oplus\mathcal L''
$$
with $\mathcal L'$ and $\mathcal L''$ invertible.  The two projections
$$
\mathcal E\twoheadrightarrow\mathcal L',
\qquad
\mathcal E\twoheadrightarrow\mathcal L''
$$
give sections $\sigma'$ and $\sigma''$ by Proposition V.2.6.  Their kernels
are respectively $\mathcal L''$ and $\mathcal L'$.  In every fibre these are
the two distinct direct-summand lines of
$$
\mathcal E_c=\mathcal L'_c\oplus\mathcal L''_c.
$$
Step [](#s1){.pf-ref} therefore shows that the two sections are disjoint.

:::

:::

::: {.pf-step #s3}

If $\PP(\mathcal E)$ has two disjoint sections, then
$$
\boxed{
\mathcal E\cong
\mathcal N_{\sigma'}\oplus\mathcal N_{\sigma''}.
}
$$

::: pf-proof

Let $\sigma',\sigma''$ be disjoint sections and consider the natural map of
rank-two locally free sheaves
$$
\theta:
\mathcal N_{\sigma'}\oplus\mathcal N_{\sigma''}
\longrightarrow
\mathcal E
$$
induced by the two kernel inclusions.

For each $c\in C$, step [](#s1){.pf-ref} says that the one-dimensional subspaces
$$
(\mathcal N_{\sigma'})_c,
\qquad
(\mathcal N_{\sigma''})_c
$$
of the two-dimensional vector space $\mathcal E_c$ are distinct.  They
therefore span $\mathcal E_c$, so
$$
\theta_c:
(\mathcal N_{\sigma'})_c\oplus(\mathcal N_{\sigma''})_c
\longrightarrow\mathcal E_c
$$
is an isomorphism for every $c$.

The determinant $\det\theta$ is consequently a nowhere-vanishing morphism
between line bundles.  Hence $\det\theta$ is an isomorphism, and therefore
$\theta$ itself is an isomorphism.  Thus $\mathcal E$ is a direct sum of two
invertible sheaves.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the forward implication, and step [](#s3){.pf-ref} proves the converse.

:::

:::

:::

::: {.remark title="Published solution"}
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 2 of §2 (solution by Yu-Chi Hou), PDF pp. 5--6, proves both directions. For $\Rightarrow$, the two direct summands give surjections $\mathcal E\twoheadrightarrow\mathcal L_i$, hence sections $C_1,C_2$; twisting $\pi^*\sigma_i^*\OO_X(1)=\pi^*\mathcal L_i$ by $\OO_X(-C_j)$ and restricting to $C_i$ gives $\deg_{C_i}(\OO_X(C_j)|_{C_i})=C_i\cdot C_j=0$, and distinct irreducible curves with intersection number zero are disjoint. For $\Leftarrow$, the kernel inclusions give $\mathcal N_1\oplus\mathcal N_2\to\mathcal E$, and the check is made pointwise: at a point of $C_1$ the local equation $f_1$ generates $\OO_X(-C_1)$ while $\OO_X(-C_2)=\OO_X$ there, because $C_1\cap C_2=\varnothing$, so a pair $(0,a)$ maps to $a$. That is step [](#s1){.pf-ref} and step [](#s3){.pf-ref}, with the determinant replacing the pointwise accounting of the quotient.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.2, printed p. 102, asserts both directions: "clearly the sections corresponding to $L$ and $L'$ have no intersection", and in the converse "since $C\cap C'=\emptyset$, we have $K\oplus K'\to E$ is injective".

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.2, PDF p. 261: the whole entry is the citation "Marumaye, Remark 1.20"; Maruyama's paper is not in `tmp/sources`, so there is no argument to read.
:::
