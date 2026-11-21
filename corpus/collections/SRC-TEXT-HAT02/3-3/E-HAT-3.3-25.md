---
schema: qual/card@1
id: E-HAT-3.3-25
kind: problem
title: Torsionfree $H_{k-1}$ implies torsionfree $H_k$
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 25; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 25; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: torsion-freeness of the finitely generated $H_{k-1}$ kills the Ext term, so
    $H^k\cong\operatorname{Hom}(H_k,\ZZ)$ is free, and Poincaré duality identifies it with $H_k$.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Published argument located at Guanyu Li, Hatcher.pdf, Exercise 3.3.9 (Hatcher 3.3 #25), printed
    p.59, with its symbol defect corrected: the universal coefficient sequence goes from
    Ext(H_{k-1}) to H^k to Hom(H_k), so the object after its vanishing Ext term is Hom(H_k(M),Z),
    not Ext(H_k(M),Z). Poincare duality then gives H_k(M), and Hom of a finitely generated group
    into Z is free (in particular torsionfree).

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §3.3. Read against Hatcher, Exercise 25 of §3.3, printed p. 259, and
    against the transcription's source, Guanyu Li, Exercise 3.3.9 (Hatcher 3.3 #25), printed p. 59 of
    `tmp/sources/hatcher-solutions-guanyu-li.pdf`. The printed page is added, the card having had
    none. Checked: $H_{k-1}(M)$ finitely generated and torsionfree is free, so
    $\operatorname{Ext}(H_{k-1}(M),\ZZ)=0$; the universal coefficient sequence then gives
    $H^k(M;\ZZ)\cong\operatorname{Hom}(H_k(M),\ZZ)$, free because $H_k(M)$ is finitely generated;
    and Poincaré duality on the closed orientable $2k$-manifold gives $H^k(M)\cong H_k(M)$, so $H_k$
    is free and in particular torsionfree. The source's slip — writing $\operatorname{Ext}(H_k(M),\ZZ)$
    for the surviving term after its Ext vanishes — is recorded on the card and not reproduced. No
    defect.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Citation rewritten: the retained set is named by its exercise number, Guanyu Li, *Solution of
    Allen Hatcher*, Exercise 3.3.9, which is Hatcher §3.3 Exercise 25, and the locator into the local
    file and the external URL are given without a page. The source's own slip is recorded there and
    not repaired in silence: it writes $H^k(M;\ZZ)\cong\operatorname{Ext}(H_k(M),\ZZ)$ where the
    universal coefficient sequence gives $\operatorname{Hom}(H_k(M),\ZZ)$.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted to numbered steps under #2, transcribing the retained set's argument into the Lamport
    structure and checking each step against Hatcher. One step the source leaves implicit is added:
    finite generation of $H_*(M;\ZZ)$, which is what makes "torsionfree" imply "free" and so what
    makes the $\operatorname{Ext}$ term vanish, and which is also what turns $H_k\cong\operatorname{Hom}(H_k,\ZZ)$
    into the vanishing of the torsion. The torsion argument is the source's, made exact: writing
    $H_k=\ZZ^r\oplus T$, the isomorphism forces $T=0$. Checked against Hatcher, §3.3: the universal
    coefficient theorem for cohomology, Theorem 3.2 of §3.1; Poincaré duality, Theorem 3.30 of §3.3;
    and Corollary A.8 for a closed manifold having the homotopy type of a finite complex. Not
    checked: no certificate, and no case $k=0$ is discussed, where the statement is trivial.

---
::: {.solution}
The argument is that of the retained solution set, **Guanyu Li, *Solution of Allen Hatcher*, Exercise 3.3.9**, which is Hatcher §3.3 Exercise 25, checked against the book and read in the local file `tmp/sources/hatcher-solutions-guanyu-li.pdf`. The source writes the second group of the universal coefficient sequence as $\Ext(H_k(M),\ZZ)$ where the sequence gives $\Hom(H_k(M),\ZZ)$; the corrected form is used below, and the source's remaining step, that a finitely generated group isomorphic to its own dual is free, is written out rather than assumed. Let $M$ be a closed orientable manifold of dimension $2k$.

::: pf

::: {.pf-step #finite}
$H_i(M;\ZZ)$ is finitely generated for every $i$.

::: pf-proof
$M$ is a closed manifold, hence compact, and a compact manifold has the homotopy type of a finite CW complex, so its homology is that of a chain complex of finitely generated free abelian groups and is finitely generated (Hatcher, Corollary A.8).
:::

:::

::: {.pf-step #ext}
If $H_{k-1}(M;\ZZ)$ is torsionfree then $\Ext(H_{k-1}(M;\ZZ),\ZZ)=0$.

::: pf-proof
By step [](#finite){.pf-ref} the group $H_{k-1}(M;\ZZ)$ is finitely generated, and a finitely generated torsionfree abelian group is free. For a free abelian group $A$ the group $\Ext(A,\ZZ)$ vanishes, since $A$ has the free resolution $0\to A\to A\to0$.
:::

:::

::: {.pf-step #uct}
The universal coefficient theorem in degree $k$ gives a short exact sequence $0\to\Ext(H_{k-1}(M),\ZZ)\to H^k(M;\ZZ)\to\Hom(H_k(M),\ZZ)\to0$, which by step [](#ext){.pf-ref} is an isomorphism $H^k(M;\ZZ)\cong\Hom(H_k(M),\ZZ)$.

::: pf-proof
The split exact sequence is the universal coefficient theorem for cohomology (Hatcher, Theorem 3.2), applied to the singular chain complex of $M$, which is free in each degree; the first term vanishes by step [](#ext){.pf-ref}, and an exact sequence whose first term is zero is an isomorphism between the other two.
:::

:::

::: {.pf-step #poincare}
$H_k(M;\ZZ)\cong H^k(M;\ZZ)$.

::: pf-proof
Poincaré duality for a closed orientable $n$-manifold gives $H^k(M;\ZZ)\cong H_{n-k}(M;\ZZ)$ (Hatcher, Theorem 3.30), and here $n-k=2k-k=k$.
:::

:::

::: {.pf-step #dual}
Hence $H_k(M;\ZZ)\cong\Hom(H_k(M;\ZZ),\ZZ)$.

::: pf-proof
Steps [](#uct){.pf-ref} and [](#poincare){.pf-ref} exhibit both $H_k(M;\ZZ)$ and $\Hom(H_k(M;\ZZ),\ZZ)$ as isomorphic to $H^k(M;\ZZ)$, so they are isomorphic to each other.
:::

:::

::: {.pf-step #torsion}
A finitely generated abelian group isomorphic to its own dual $\Hom(-,\ZZ)$ is free.

::: pf-proof
Write $A=\ZZ^r\oplus T$ with $T$ finite, by the classification of finitely generated abelian groups (step [](#finite){.pf-ref}). Then $\Hom(A,\ZZ)=\Hom(\ZZ^r,\ZZ)\cong\ZZ^r$, because a homomorphism from the finite group $T$ to the torsionfree group $\ZZ$ is zero: its image is a finite subgroup of $\ZZ$, hence trivial. An isomorphism $A\cong\Hom(A,\ZZ)$ therefore identifies $\ZZ^r\oplus T$ with $\ZZ^r$, and comparing ranks, the free parts agree and $T$ is trivial.
:::

:::

::: {.pf-step}
If $H_{k-1}(M;\ZZ)$ is torsionfree then $H_k(M;\ZZ)$ is torsionfree.

::: pf-proof
Steps [](#dual){.pf-ref} and [](#torsion){.pf-ref} give that $H_k(M;\ZZ)$ is free, hence torsionfree.
:::

:::

:::

:::
