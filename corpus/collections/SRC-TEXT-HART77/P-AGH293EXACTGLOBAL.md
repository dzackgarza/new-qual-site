---
schema: qual/card@1
id: P-AGH293EXACTGLOBAL
kind: problem
title: Global sections on an affine formal scheme are exact
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Coherent Sheaves
  - Inverse Limits
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both steps with the retained Hartshorne II.9.3 transcription and Propositions II.9.1, II.9.2 and II.9.6. Checked the inverse-system exactness criterion against Stacks Project section 12.31. Only the kernel is assumed coherent; the proof takes inverse limits on affine sections before asserting exactness of sheaves.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Prove the analogue of (5.6) for formal schemes, which says: if $\mathfrak{X}$ is an affine noetherian formal scheme, and if
$$
0 \to \mcf' \to \mcf \to \mcf'' \to 0
$$
is an exact sequence of $\OO_\mathfrak{X}\dash$modules, and if $\mcf'$ is coherent, then the sequence of global sections
$$
0 \to \Gamma(\mathfrak{X}, \mcf') \to \Gamma(\mathfrak{X}, \mcf) \to \Gamma(\mathfrak{X}, \mcf'') \to 0
$$
is exact.
Proceed in the following steps.

(a) Let $\mci$ be an ideal of definition for $\mathfrak{X}$, and for each $n > 0$ consider the exact sequence
$$
0 \to \mcf'/\mci^n \mcf' \to \mcf/\mci^n \mcf' \to \mcf'' \to 0
.
$$
   Use (5.6), slightly modified, to show that for every open affine subset $\mcu \subseteq \mathfrak{X}$ the sequence
$$
0 \to \Gamma(\mcu, \mcf'/\mci^n \mcf') \to \Gamma(\mcu, \mcf/\mci^n \mcf') \to \Gamma(\mcu, \mcf'') \to 0
$$
   is exact.

(b) Now pass to the limit, using (9.1), (9.2), and (9.6).
   Conclude that $\mcf \cong \inverselim_n \mcf/\mci^n \mcf'$ and that the sequence of global sections above is exact.
:::

::: {.solution}
Identify $\mcf'$ with its image in $\mcf$ and put
$$
K_n=\mcf'/\mci^n\mcf',\qquad G_n=\mcf/\mci^n\mcf',
\qquad \mathfrak X_n=(|\mathfrak X|,\OO_{\mathfrak X}/\mci^n).
$$
The schemes $\mathfrak X_n$ are the ordinary infinitesimal layers on the common underlying space of the [[D-SCHFORMAL|formal scheme]].
On an affine formal open $\mathfrak U$, their restrictions $\mathfrak U_n$ are affine schemes [@Har10a, Propositions II.9.4 and II.9.5].
The sheaf $K_n$ is coherent on $\mathfrak X_n$, and
$$
\mcf'\xrightarrow{\cong}\varprojlim_n K_n
$$
by [@Har10a, Proposition II.9.6].
Neither $\mcf$ nor $\mcf''$ is assumed coherent or annihilated by a power of $\mci$.

::: pf

::: {.pf-step #s1}

For every affine formal open $\mathfrak U$ and $n\ge1$, the sequence
$$
0\to K_n(\mathfrak U)\to G_n(\mathfrak U)
\to\mcf''(\mathfrak U)\to0
$$
is exact.

::: pf-proof

The sheaf sequence $0\to K_n\to G_n\to\mcf''\to0$ is exact by taking the indicated quotient of the original sequence.
Left exactness on sections gives exactness except possibly at the last term.

Take $s\in\mcf''(\mathfrak U)$.
Surjectivity as sheaves gives local lifts to $G_n$.
Refine their domains to a finite cover by opens which are distinguished affine opens of $\mathfrak U_n$; the topology is the same, and the affine scheme $\mathfrak U_n$ is quasi-compact.
Write the lifts as $s_i$.
On overlaps their differences $c_{ij}=s_i-s_j$ are sections of $K_n$ and satisfy $c_{ij}+c_{jk}=c_{ik}$.
The usual affine gluing argument for a quasi-coherent sheaf gives sections $b_i$ of $K_n$ with $c_{ij}=b_i-b_j$ [@Har10a, Proposition II.5.6], as in the affine Čech calculation in [[T-COHAFF]].
Thus $s_i-b_i$ agree on overlaps and glue to a section of $G_n(\mathfrak U)$ lifting $s$.

This argument only uses the quasi-coherence of $K_n$ on the affine scheme $\mathfrak U_n$.
The middle and last sheaves need only be sheaves of abelian groups for the correction and gluing, so they need not be modules over $\OO_{\mathfrak U_n}$.
This proves the required modification of Proposition II.5.6 and all of (a).

:::

:::

::: {.pf-step #s2}

The transition maps $K_{n+1}(\mathfrak U)\to K_n(\mathfrak U)$ are surjective for every affine formal open $\mathfrak U$.

::: pf-proof

On the affine scheme $\mathfrak U_{n+1}$ there is an exact sequence of coherent sheaves
$$
0\to\mci^n\mcf'/\mci^{n+1}\mcf'
\to K_{n+1}\to K_n\to0.
$$
The last sheaf is regarded as a sheaf on that scheme through its quotient structure sheaf.
Exactness of global sections for quasi-coherent sheaves on an affine scheme gives the asserted surjectivity [@Har10a, Proposition II.5.6].
Consequently the inverse system of groups $K_n(\mathfrak U)$ satisfies the Mittag--Leffler condition.

:::

:::

::: {.pf-step #s3}

For $H=\varprojlim_n G_n$, there is an exact sequence of sheaves
$$
0\longrightarrow\mcf'\longrightarrow H\longrightarrow\mcf''\longrightarrow0,
$$
and it is exact on sections over every affine formal open.

::: pf-proof

The sequences in step [](#s1){.pf-ref} form a short exact sequence of inverse systems of groups, with the constant system $\mcf''(\mathfrak U)$ on the right.
Step [](#s2){.pf-ref} and the inverse-limit exactness criterion give
$$
0\to\varprojlim_n K_n(\mathfrak U)
\to\varprojlim_n G_n(\mathfrak U)
\to\mcf''(\mathfrak U)\to0
$$
[@Har10a, Proposition II.9.1].
Explicitly, compatible lifts of a fixed section can be constructed recursively.
After choosing a lift at level $n$, choose any lift at level $n+1$ by step [](#s1){.pf-ref}.
Its discrepancy at level $n$ lies in $K_n(\mathfrak U)$; lift that discrepancy through the surjection of step [](#s2){.pf-ref} and subtract it at level $n+1$.
This produces compatible lifts at every level.

Limits of sheaves are computed on sections [@Har10a, Proposition II.9.2].
Together with $\mcf'\cong\varprojlim_n K_n$, this identifies the displayed sequence with
$$
0\to\mcf'(\mathfrak U)\to H(\mathfrak U)
\to\mcf''(\mathfrak U)\to0.
$$
These maps commute with restriction.
Since affine formal opens form a basis, the resulting sequence of sheaves is exact.
In particular, exactness has been proved on sections before passing to sheaves; it is not an application of a generally false exactness assertion for inverse limits of sheaves.

:::

:::

::: {.pf-step #s4}

The natural map $\mcf\to H$ is an isomorphism, and the desired global-section sequence is exact.

::: pf-proof

The quotient maps $\mcf\to G_n$ give a natural map $\eta:\mcf\to H$.
It takes the original short exact sequence to the short exact sequence in step [](#s3){.pf-ref}, with the identity on $\mcf'$ and on $\mcf''$.
At a stalk, an element in the kernel of $\eta$ maps to zero in $\mcf''$ and hence comes from $\mcf'$; the identity on that term forces it to be zero.
Conversely, an element of $H$ at a stalk has an image in $\mcf''$ which lifts to $\mcf$ at that stalk.
Subtracting the image of this lift leaves an element of $\mcf'$, also in the image of $\eta$.
Thus $\eta$ is an isomorphism at every stalk and therefore an isomorphism of sheaves.

We have proved the specific completion assertion
$$
\boxed{\mcf\xrightarrow{\cong}\varprojlim_n\mcf/\mci^n\mcf'.}
$$
This uses the filtration by $\mci^n\mcf'$, not the possibly different filtration by $\mci^n\mcf$.
Finally, take $\mathfrak U=\mathfrak X$ in step [](#s3){.pf-ref} and replace $H$ by $\mcf$ through $\eta$.
The result is the full short exact sequence of global sections requested in (b).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a), and steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove both the inverse-limit identification and global exactness in (b).

:::

:::

:::
