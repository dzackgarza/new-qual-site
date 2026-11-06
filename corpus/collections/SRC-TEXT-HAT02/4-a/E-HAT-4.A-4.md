---
schema: qual/card@1
id: E-HAT-4.A-4
kind: problem
title: "Automorphisms of wedge sums of spheres"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-written
  by: claude
  date: 2026-11-04
  note: >-
    Repair of the Whitehead step in the third block, which claimed that an isomorphism on pi_k(X)
    alone, for X k-dimensional, detects a homotopy equivalence. Whitehead's theorem needs the
    isomorphism on every homotopy group, and pi_i of a wedge of k-spheres can be nonzero for i > k
    (Hilton-Milnor), so the step as written did not cover i > k. The replacement runs the hint in the
    printed exercise itself: naturality of Hurewicz turns the pi_k isomorphism into one on
    H_k(X;Z) = Z^n, X has no other reduced homology, and simply-connected CW homology isomorphisms
    are homotopy equivalences by the homology form of Whitehead's theorem (Corollary 4.33). The
    equality criterion M(f) in GL_n(Z) is unchanged. Checked: every substep of the monoid
    characterization [X,X]_* = M_n(Z), its multiplicativity, and the based/free identification at the
    end. Not checked: re-verification of the printed hint's parenthetical beyond its restatement here.

---

::: {.problem}
With the notation of the preceding problem, show that $\operatorname{Aut}(\bigvee_n S^k) \approx \operatorname{GL}_n(\ZZ)$ for $k > 1$, where $\bigvee_n S^k$ denotes the wedge sum of $n$ copies of $S^k$ and $\operatorname{GL}_n(\ZZ)$ is the group of $n \times n$ matrices with entries in $\ZZ$ having an inverse matrix of the same form.
[$\operatorname{GL}_n(\ZZ)$ is the automorphism group of $\ZZ^n \approx \pi_k(\bigvee_n S^k) \approx H_k(\bigvee_n S^k)$.]
:::

::: {.solution}
::: pf

::: pf-step
Compute $\pi_k(X)$ for $X = \bigvee_{j=1}^n S^k$ ($k > 1$):

::: pf-proof

::: pf-step
Since $k > 1$, the space $X$ is $(k-1)$-connected: $\pi_1(X) = \cdots = \pi_{k-1}(X) = 0$.

::: pf-proof
Every map $S^i\to X$ with $i<k$ is homotopic to a cellular map by the cellular approximation theorem (Theorem 4.8, p. 349), and a cellular map $S^i\to X$ has image in the $i$-skeleton of $X$, which is the single $0$-cell when $i<k$; so $\pi_i(X)=0$ for $0<i<k$. (For $i=1$ the same conclusion follows from van Kampen's theorem, Theorem 1.20, p. 43, since $k>1$ makes each summand $S^k$ simply connected and a wedge of simply connected spaces is simply connected.)
:::

:::

::: pf-step
By the Hurewicz Theorem:
$$
\pi_k(X) \cong H_k(X; \ZZ) \cong \bigoplus_{j=1}^n H_k(S^k; \ZZ) \cong \ZZ^n.
$$

::: pf-proof
Theorem 4.32 (p. 366), the Hurewicz theorem, applies because $X$ is $(k-1)$-connected with $k\ge2$ and gives $\pi_k(X)\cong H_k(X;\ZZ)$; and $H_k(\bigvee_j S^k)\cong\bigoplus_j H_k(S^k)\cong\ZZ^n$ since the $k$-spheres are the $k$-cells of $X$ and cellular homology is computed by the cellular chain complex (Theorem 2.35, p. 139).
:::

:::

::: pf-step
Let $\iota_j: S^k \hookrightarrow X$ denote the inclusion of the $j$-th sphere summand; their homotopy classes $\{[\iota_1], \dots, [\iota_n]\}$ form a standard $\ZZ$-basis for $\pi_k(X)$.

::: pf-proof
Each $\iota_j$ is a cellular cycle generating the $j$-th summand $H_k(S^k)\cong\ZZ$ of $H_k(X)$, and the Hurewicz isomorphism of Theorem 4.32 (p. 366) is natural, so their classes form a $\ZZ$-basis of $\pi_k(X)$.
:::

:::

:::

:::

::: {.pf-step #s2}
Characterize the monoid of based homotopy classes $[X, X]_*$:

::: pf-proof

::: pf-step
By the universal property of the wedge sum, a based map $f: X \to X$ is determined up to based homotopy by its restrictions $f \circ \iota_j: S^k \to X$ for $j = 1, \dots, n$.

::: pf-proof
A based map out of a wedge is determined by the restrictions to the summands, bijectively, because a map on the quotient $\bigvee_j S^k=(S^k\sqcup\cdots\sqcup S^k)/{\sim}$ is exactly a compatible family of maps on the summands (the universal property of the quotient, the basepoints being identified).
:::

:::

::: pf-step
Each restriction $[f \circ \iota_j] \in \pi_k(X) \cong \ZZ^n$.

::: pf-proof
The composite $f\circ\iota_j:S^k\to X$ is a based map, so its class lies in $\pi_k(X)=[S^k,X]_*$ by definition of the $k$-th homotopy group, and it is computed through the identification of $\pi_k(X)$ with $\operatorname{Hom}(\ZZ^n,\ZZ^n)$ above.
:::

:::

::: pf-step
Thus $[X, X]_* \cong \prod_{j=1}^n \pi_k(X) \cong M_n(\ZZ)$, where $f$ corresponds to the matrix $M(f) \in M_n(\ZZ)$ whose $j$-th column is the coordinate vector of $f_*([\iota_j])$ in the basis $\{[\iota_1], \dots, [\iota_n]\}$.

::: pf-proof
$\prod_{j=1}^n\pi_k(X)=\operatorname{Hom}(\ZZ^n,\ZZ^n)$: a homomorphism out of the free group $\ZZ^n$ is determined by the images of the $n$ basis elements, which are the columns of $M(f)$.
:::

:::

::: pf-step
The assignment $f \mapsto M(f)$ preserves composition: $M(g \circ f) = M(g) M(f)$.

::: pf-proof
functoriality of induced maps on homotopy groups $(g \circ f)_* = g_* \circ f_*$.
:::

:::

:::

:::

::: {.pf-step #s3}
Characterize homotopy equivalences via Whitehead’s Theorem:

::: pf-proof

::: pf-step
$X$ is a finite CW complex of dimension $k$ with cells only in dimensions $0$ and $k$.

::: pf-proof
cellular structure of a wedge of spheres.
:::

:::

::: pf-step
If $f_*: \pi_k(X) \to \pi_k(X)$ is an isomorphism, then $f$ is a homotopy equivalence, and the converse holds as well.

::: pf-proof
Naturality of the Hurewicz homomorphism turns $f_*$ on $\pi_k(X)$ into $f_*$ on $H_k(X;\ZZ)$, and by the Hurewicz isomorphism established above these two are the same map $\ZZ^n \to \ZZ^n$. Since $X$ has cells only in dimensions $0$ and $k$, every other reduced homology group of $X$ vanishes, so $f$ induces isomorphisms on all homology groups. Both $X$ and $Y=X$ are simply connected CW complexes, so by the homology form of Whitehead's theorem (Corollary 4.33) $f$ is a homotopy equivalence. The converse needs no theorem: a homotopy equivalence induces isomorphisms on every homotopy group, in particular on $\pi_k$. The hypothesis that $\pi_k(X)$ alone is an isomorphism is used exactly here and not claimed to detect equivalences in general; the homology form carries the argument because $X$ has only one nonzero reduced homology group.
:::

:::

::: pf-step
The group homomorphism $f_*: \ZZ^n \to \ZZ^n$ is an isomorphism if and only if its representation matrix $M(f)$ is invertible over $\ZZ$, which means $M(f) \in \operatorname{GL}_n(\ZZ)$ (i.e. $\det M(f) = \pm 1$).

::: pf-proof
A $\ZZ$-linear endomorphism of $\ZZ^n$ is an isomorphism exactly when its matrix has a two-sided inverse over $\ZZ$; such a matrix has $\det=\pm1$ by multiplicativity of the determinant and conversely an integer matrix with $\det=\pm1$ has the integer inverse $(\det M)^{-1}\operatorname{adj}(M)$. This is $\operatorname{GL}_n(\ZZ)$ as in Hatcher's hint, the automorphism group of $\pi_k(X)$.
:::

:::

:::

:::

::: pf-step
Conclusion: The map $[f] \mapsto M(f)$ induces an isomorphism of groups:
$$
\operatorname{Aut}\left(\bigvee_{j=1}^n S^k\right) \cong \operatorname{GL}_n(\ZZ).
$$

::: pf-proof
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}. Since $X$ is simply connected, the action of $\pi_1(X)$ on based homotopy classes is trivial, so based and free homotopy classes agree here.
:::

:::

:::

:::
