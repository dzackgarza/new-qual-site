---
schema: qual/card@1
id: P-TOPF09G
kind: problem
title: "Suspension of a homology 3-sphere is homotopy equivalent to S^4"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Suspensions
  - Homotopy Type
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subclaims suffice, and the 17
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: the suspension split into the two open cones with contractible total space
    and intersection homotopy equivalent to $M$, van Kampen giving a trivial fundamental group, the
    Mayer--Vietoris suspension isomorphism shifting the only non-zero reduced group from degree $3$ to
    degree $4$, Hurewicz giving $\pi_4\cong\ZZ$ and vanishing of $\pi_2,\pi_3$, and Whitehead's
    homological theorem applied to finite CW models supplied by Moise. The card's two imported theorems,
    Moise's triangulability and the homological Whitehead theorem, are named where they are used; neither
    is proved here. Checked against the statement on the card, from the UCSD Fall 2009 topology qualifying
    exam. Nothing in the statement was changed.

---

::: {.problem}
Let $M^3$ be a homology sphere: a connected closed compact $3$-manifold with the same homology groups as $S^3$.
Calculate the fundamental group and homology of the suspension $\Sigma M$.
Use this to show that the suspension is homotopy-equivalent to $S^4$.
:::

::: {.solution}
::: pf

::: pf-step
Fundamental group of $\Sigma M$:

::: pf-proof

::: pf-step
The suspension $\Sigma M$ is the quotient of $M \times [-1, 1]$ identifying $M \times \{1\}$ to a north cone point $N$ and $M \times \{-1\}$ to a south cone point $S$.

::: pf-proof
This is the definition of the suspension of $M$.
:::

:::

::: pf-step
Decompose $\Sigma M = U \cup V$ with open sets $U = \Sigma M \setminus \{S\}$ and $V = \Sigma M \setminus \{N\}$.

::: pf-proof
Removing a cone point leaves an open set, and the two complements meet in $M\times(-1,1)$.
:::

:::

::: pf-step
The open cone $U$ deformation retracts to the point $N$, and $V$ deformation retracts to $S$, so both $U$ and $V$ are contractible ($\pi_1(U) = \pi_1(V) = \{e\}$).

::: pf-proof
Pushing along the cone lines retracts $U$ onto $N$ through a homotopy that fixes $N$, and a space admitting such a deformation retraction to a point is contractible.
:::

:::

::: pf-step
The intersection $U \cap V = M \times (-1, 1)$ deformation retracts to $M$, which is path-connected by hypothesis.

::: pf-proof
The projection $M\times(-1,1)\to M$ and the inclusion $M\cong M\times\{0\}\hookrightarrow M\times(-1,1)$ are homotopy inverses.
:::

:::

::: pf-step
By the Seifert–van Kampen Theorem:
$$\pi_1(\Sigma M) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V) \cong \{e\} *_{\pi_1(M)} \{e\} \cong \{e\}.$$

::: pf-proof
van Kampen applies to the open cover by $U$ and $V$, whose intersection is path connected because $M$ is; the amalgamated product of two trivial groups over any group is trivial.
:::

:::

::: pf-step
Thus $\Sigma M$ is simply connected: $\pi_1(\Sigma M) = 0$.

::: pf-proof
A trivial fundamental group is the definition of simply connected.
:::

:::

:::

:::

::: pf-step
Homology groups of $\Sigma M$:

::: pf-proof

::: pf-step
Apply the Mayer–Vietoris sequence to the open cover $\{U, V\}$ of $\Sigma M$:
$$\cdots \to \widetilde{H}_k(U) \oplus \widetilde{H}_k(V) \to \widetilde{H}_k(\Sigma M) \xrightarrow{\partial_*} \widetilde{H}_{k-1}(U \cap V) \to \widetilde{H}_{k-1}(U) \oplus \widetilde{H}_{k-1}(V) \to \cdots$$

::: pf-proof
Mayer–Vietoris applies to an open cover with non-empty intersection and gives the displayed exact sequence in reduced homology.
:::

:::

::: pf-step
Since $U$ and $V$ are contractible, $\widetilde{H}_k(U) = \widetilde{H}_k(V) = 0$ for all $k$, yielding the suspension isomorphism:
$$\widetilde{H}_k(\Sigma M) \cong \widetilde{H}_{k-1}(U \cap V) \cong \widetilde{H}_{k-1}(M) \quad \text{for all } k \ge 1.$$

::: pf-proof
The terms of $U$ and $V$ vanish, so the connecting map is an isomorphism in each degree; and $U\cap V$ deformation retracts to $M$, so its reduced homology is that of $M$ shifted by one.
:::

:::

::: pf-step
Since $M$ is a homology 3-sphere, its reduced homology is $\widetilde{H}_3(M) \cong \ZZ$ and $\widetilde{H}_j(M) = 0$ for all $j \neq 3$.

::: pf-proof
This is the definition of a homology $3$-sphere: the reduced homology agrees with that of $S^3$.
:::

:::

::: pf-step
Therefore, the reduced homology groups of $\Sigma M$ are:
$$\widetilde{H}_k(\Sigma M) \cong \begin{cases} \ZZ & k = 4, \\ 0 & k \neq 4. \end{cases}$$

::: pf-proof
The suspension isomorphism shifts the only non-vanishing reduced group, in degree $3$, up to degree $4$.
:::

:::

:::

:::

::: pf-step
Homotopy equivalence $\Sigma M \simeq S^4$ via Hurewicz and Whitehead:

::: pf-proof

::: pf-step
Since $\Sigma M$ is simply connected ($\pi_1(\Sigma M) = 0$) and $\widetilde{H}_k(\Sigma M) = 0$ for $1 \le k \le 3$, the Hurewicz Theorem implies that:
$$\pi_2(\Sigma M) = 0, \qquad \pi_3(\Sigma M) = 0,$$
and the Hurewicz homomorphism $h: \pi_4(\Sigma M) \to H_4(\Sigma M) \cong \ZZ$ is an isomorphism.

::: pf-proof
$\Sigma M$ is simply connected and its homology vanishes in degrees $1$ to $3$, so the Hurewicz theorem gives $\pi_k=0$ for $k\le3$ and an isomorphism $\pi_4\to H_4$.
:::

:::

::: pf-step
Choose a continuous map $f: S^4 \to \Sigma M$ representing a generator of $\pi_4(\Sigma M) \cong \ZZ$.

::: pf-proof
Every element of $\pi_4$ is represented by a map of the $4$-sphere.
:::

:::

::: pf-step
By construction, $f_*: H_4(S^4; \ZZ) \to H_4(\Sigma M; \ZZ)$ is an isomorphism.

::: pf-proof
Under the Hurewicz isomorphism the chosen class corresponds to a generator of $H_4\cong\ZZ$, so $f$ induces an isomorphism in degree $4$.
:::

:::

::: pf-step
In all other degrees $k \neq 4$, $H_k(S^4) \cong H_k(\Sigma M)$ are either $\ZZ$ (for $k = 0$) or $0$ (for $k \neq 0, 4$), so $f_*: H_k(S^4; \ZZ) \to H_k(\Sigma M; \ZZ)$ is an isomorphism for every $k \ge 0$.

::: pf-proof
$H_0$ of both spaces is $\ZZ$ and the spaces are connected, so the induced map is an isomorphism there; in every other degree both groups vanish.
:::

:::

::: pf-step
By Moise's Theorem, every compact 3-manifold is triangulable as a finite simplicial complex, so the suspension $\Sigma M$ is a finite 4-dimensional CW complex.

::: pf-proof
Moise's theorem triangulates the compact $3$-manifold, and the suspension of a finite complex is a finite complex one dimension higher.
:::

:::

::: pf-step
By Whitehead's Theorem (homological version for simply connected CW complexes), a homology isomorphism between simply connected CW complexes is a homotopy equivalence.

::: pf-proof
This is the homological Whitehead theorem: both spaces are CW complexes and both are simply connected.
:::

:::

::: pf-step
Therefore $f: S^4 \to \Sigma M$ is a homotopy equivalence, so $\Sigma M \simeq S^4$.

::: pf-proof
The two preceding steps supply a homology isomorphism between simply connected CW complexes, which is a homotopy equivalence.
:::

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$\pi_1(\Sigma M) = 0$, $\widetilde{H}_*(\Sigma M) \cong \widetilde{H}_*(S^4)$, and $\Sigma M \simeq S^4$.
:::

:::

:::
:::
