---
schema: qual/card@1
id: E-HAT-2.B-1
kind: problem
title: "Homology of complements of wedges and disjoint unions in spheres"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the Alexander-duality and Mayer--Vietoris calculations and all degree shifts.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 1, printed page
    176; the statement matches word for word. Checked: Alexander duality
    H̃_i(S^n − X) ≅ H̃^{n−i−1}(X) (Theorem 3.44, p. 253) applies to these compact
    locally contractible X; H̃^j(S^k ∨ S^ℓ) is Z in degrees k and ℓ (Z^2 when
    k = ℓ) and H̃^0 = 0, giving Z in degrees n−k−1 and n−ℓ−1; for the disjoint union
    there is also H̃^0 = Z, giving one more Z in degree n−1. Degree shifts and the
    ordinary H_0 statement checked. No defect.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Source coverage and degree accounting verified against DeMason, M382C Full Credit HW Problems
    (2021), Hatcher 2.B.1, pp.68-70. The wedge's reduced cohomology is the direct sum of the two
    sphere contributions; the disjoint case has one further H~^0=Z, and terms at the coinciding
    indices n-k-1, n-l-1, n-1 must be summed. Explicitly, at n=1 and k=l=0, X has four points and
    the complement has H~_0=Z^3, so H_0=Z^4. This refines the existing correct formula without
    invoking an inappropriate connectedness assumption for S^0.

- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Replaced the unconditional H~^0(X)=Z in the disjoint case by the actual cases: Z for k,l >= 1,
    Z^2 when exactly one index is 0, and Z^3 for k=l=0. S^0 itself has two points, so k=l=0 gives
    four points and unreduced H_0=Z^4 when n=1. The proof now starts from DeMason's cover A,B of
    S^n with intersection equivalent to S^n-X, and uses Proposition 2B.1(b) with relative
    Mayer-Vietoris and explicitly summed coincident indices, rather than claiming the published
    proof is merely equivalent to a different Alexander-duality argument. Also relocated the
    inserted source-checked note inside audit, before the YAML separator, and separated the source
    text from the closing display as required by the source renderer.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 1 of §2.B, printed p. 176, in
    `tmp/sources/hatcher-2002-algebraic-topology.md`, and the transcription checked against
    DeMason, *M382C Full Credit HW Problems*, Hatcher 2.B.1, printed pp. 68--70 of
    `tmp/sources/demason-m382c-hatcher-20210404.pdf`, whose section begins on p. 68 and whose next
    exercise begins on p. 70. Two points checked. (1) Theorem 3.44 is on printed p. 254, not
    p. 253 as the event of 2026-11-06 has it (PDF page 263 of the book, whose folio is 254); the
    statement itself is quoted correctly. (2) The source's displayed answer for the disjoint union
    lists an entry at $i=0$ separately from those at $i=n-k-1$ and $i=n-\ell-1$; the card keeps
    the entries at $n-k-1$, $n-\ell-1$ and the $\widetilde H^{n-1}(X)$ term and merges coincident
    indices, which is the correct reading: for the wedge the complement of $S^n-X$ is connected
    unless $n-k-1=0$ or $n-\ell-1=0$, and in those cases the entry coincides with one already
    present. Checked in the card: the wedge's reduced cohomology as a direct sum, Alexander duality
    in the form $\widetilde H_i(S^n-X)\cong\widetilde H^{n-i-1}(X)$, and the component counts
    $\widetilde H^0(X)=\ZZ,\ZZ^2,\ZZ^3$ for a disjoint union with $k,\ell\geq1$, exactly one zero,
    and $k=\ell=0$ respectively, the last being four points and $H_0(S^1-X)=\ZZ^4$. Not claimed: a
    different published solution of the exercise.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 185 carries the running head 176,
    so the printed page is the one the card's earlier event claimed. The durable part of the locator
    is that printed page; the file path names this machine's copy and `tmp/sources` does not survive a
    VM reset. No mathematics changed.
---

::: {.problem}
This is Exercise 1 of Section 2.B of Hatcher, *Algebraic Topology* (2002), read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf`; the statement below is its wording.

Compute $H_i(S^n - X)$ when $X$ is a subspace of $S^n$ homeomorphic to $S^k \vee S^\ell$ or to $S^k \amalg S^\ell$.
:::

::: {.solution}
Use DeMason's reduced Mayer--Vietoris decompositions for both cases, printed pp. 68--70. Proposition 2B.1(b) supplies the homology of the complement of an individual sphere, and the cover and the reduced sequence are compared term by term.

::: pf

::: {.pf-step #s1}

If $X=S^k\vee S^\ell$, then
$$
\widetilde H^j(X)\cong
\begin{cases}
\ZZ,&j=k\ne\ell,\\
\ZZ,&j=\ell\ne k,\\
\ZZ^2,&j=k=\ell,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Reduced cohomology takes a finite wedge to the direct sum of the reduced cohomologies of the two spheres. Each sphere has one copy of $\ZZ$ in its dimension and zero reduced cohomology elsewhere.

:::

:::

::: pf-step

Consequently, for $X=S^k\vee S^\ell$,
$$
\widetilde H_i(S^n-X)\cong
\begin{cases}
\ZZ,&i=n-k-1\ne n-\ell-1,\\
\ZZ,&i=n-\ell-1\ne n-k-1,\\
\ZZ^2,&i=n-k-1=n-\ell-1,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Use DeMason's cover $A$ and $B$ adapted to the two sphere factors $X_k$ and $X_\ell$. Their union is $S^n-p$, where $p$ is the wedge point, hence is contractible; their intersection is $S^n-(X_k\cup X_\ell)$, with $X_k\cap X_\ell=\{p\}$. Relative reduced Mayer--Vietoris gives the direct sum of the two individual sphere-complement contributions, with the degree shift. This is the published proof, not an assertion of equivalence with a different one.

:::

:::

::: pf-step

If $X=S^k\amalg S^\ell$, DeMason's construction uses $A$, an open set having the homology of $S^n-X_k$, and $B$, an open set having the homology of $S^n-X_\ell$. The sphere factors are disjoint, so these sets cover $S^n$, and their intersection deforms to $S^n-X$. Reduced Mayer--Vietoris then compares the individual sphere complements in Proposition 2B.1(b) with $S^n-X$ and $S^n$.

For $k,\ell\ge1$ this gives copies of $\ZZ$ in the two dimensions $n-k-1$ and $n-\ell-1$, together with one additional copy in degree $n-1$. If two of these dimensions coincide, the corresponding contributions add rather than being counted as one group; in particular $k=\ell$ gives $\ZZ^2$ there.

The zero-dimensional cases must be stated separately:
$$
\widetilde H^0(X)\cong
\begin{cases}
\ZZ,&k,\ell\ge1,\\
\ZZ^2,&\text{exactly one of }k,\ell\text{ is }0,\\
\ZZ^3,&k=\ell=0.
\end{cases}
$$
This is a statement about $\widetilde H^0$, not a blanket $\ZZ$ for every disjoint union. In particular, $S^0$ has two points, so the case $k=\ell=0$ has four points in $X$, not one or two. As DeMason explains there, at $n=1$ and $k=\ell=0$ this gives $\widetilde H_0(S^1-X)=\ZZ^3$ and hence $H_0(S^1-X)=\ZZ^4$. Otherwise the reduced component group is handled by the usual reduced-to-unreduced step, not counted twice among coinciding indices.

::: pf-proof

These are exactly the sphere/complement computations on pp. 68--70, with the component-count correction for S^0 applied to the disjoint case.
:::

:::

:::

The unreduced group $H_0$ is obtained, as usual, by adjoining one copy of $\ZZ$ to $\widetilde H_0$.

The source is **Kenneth DeMason, *M382C Full Credit HW Problems* (4 April 2021)**, Hatcher 2.B.1, printed pp. 68--70, also held locally at `tmp/sources/demason-m382c-hatcher-20210404.pdf`. The wedge and the disjoint-union arguments above follow its sphere-factor covers and reduced Mayer--Vietoris sequences. Their degree-zero component counts are kept separate in the disjoint case, and the unreduced $H_0$ is obtained afterward.


:::
