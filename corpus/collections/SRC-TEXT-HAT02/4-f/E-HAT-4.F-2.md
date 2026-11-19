---
schema: qual/card@1
id: E-HAT-4.F-2
kind: problem
title: "Suspension sequences of CW complexes"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.F, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.F, printed p. 455, with the Freudenthal suspension
    theorem (Corollary 4.24, p. 360) and the Puppe sequence of p. 398. Correct. For $X=S^q$ the
    suspension map is $\pi_{q+r}(\Sigma^rY)\to\pi_{q+r+1}(\Sigma^{r+1}Y)$, and $\Sigma^rY$ is
    $(r-1)$-connected, so $q+r<2(r-1)-1$ holds for large $r$ and Freudenthal makes it an
    isomorphism; a finite wedge follows by the same argument applied to its summands. For the
    inductive step, $X=A\cup_\varphi e^q$ gives the cofibration $S^{q-1}\to A\to X\to S^q$, and the
    Puppe sequence of the suspended cofibration mapped into $\Sigma^rY$ is exact, with the two
    consecutive sequences connected by the suspension maps; the terms are groups once $r$ is large
    because the target is then highly connected, so the five lemma applies and gives the
    isomorphism for $X$. Finitely many cells end the induction. Nothing changed. Not claimed: a
    published solution, and no certificate.
---

::: {.problem}
For CW complexes $X$ and $Y$ consider the suspension sequence

$$\langle X, Y \rangle \stackrel{\Sigma}{\longrightarrow} \langle \Sigma X, \Sigma Y \rangle \stackrel{\Sigma}{\longrightarrow} \langle \Sigma^2 X, \Sigma^2 Y \rangle \longrightarrow \cdots$$

Show that if $X$ is a finite complex, these maps eventually become isomorphisms.
[Use induction on the number of cells of $X$ and the five-lemma.]
:::

::: {.solution}
We prove stabilization by induction on the number of cells of the finite CW complex $X$.

For $X=S^q$, the suspension map is
$$
\pi_{q+r}(\Sigma^rY)
\longrightarrow
\pi_{q+r+1}(\Sigma^{r+1}Y).
$$
For large $r$, the space $\Sigma^rY$ is highly connected: after suspending sufficiently often, its connectivity grows by one at each suspension. The Freudenthal suspension theorem (Corollary 4.24, p. 360: for an $(n-1)$-connected CW complex $W$ the suspension $\pi_i(W)\to\pi_{i+1}(\Sigma W)$ is an isomorphism for $i<2n-1$) therefore implies that the displayed map is an isomorphism for all sufficiently large $r$. The same is true for a finite wedge of spheres.

Now suppose $X$ is obtained from a finite subcomplex $A$ by attaching one $q$-cell. There is a cofibration
$$
S^{q-1}\xrightarrow{\varphi}A\longrightarrow X\longrightarrow S^q
$$
and hence, after suspending $r$ times and mapping into $\Sigma^rY$, the associated Puppe sequence (p. 398) gives an exact sequence of homotopy classes. Suspending once more gives a second such exact sequence, and the suspension maps form a commutative diagram between them.

By the induction hypothesis, the suspension maps involving $A$ are isomorphisms for all sufficiently large $r$. By the sphere case, the maps involving $S^{q-1}$ and $S^q$ are also isomorphisms for sufficiently large $r$. After increasing $r$ if necessary, the relevant terms are groups, and the five-lemma (p. 130) applied to the two Puppe sequences shows that
$$
\langle\Sigma^rX,\Sigma^rY\rangle
\longrightarrow
\langle\Sigma^{r+1}X,\Sigma^{r+1}Y\rangle
$$
is an isomorphism.

Since $X$ has only finitely many cells, the induction terminates. Therefore
$$
\boxed{\text{the suspension maps are isomorphisms for all sufficiently large }r.}
$$
:::
