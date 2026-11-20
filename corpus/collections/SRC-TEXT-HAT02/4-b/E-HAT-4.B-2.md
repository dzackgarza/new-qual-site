---
schema: qual/card@1
id: E-HAT-4.B-2
kind: problem
title: "Fiber bundles $S^k \\to S^m \\to S^n$ and the Hopf invariant"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.B, Exercise 2 and its hint; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.B, printed p. 427, with Corollary 4.9 (p. 349),
    Corollary 4.25 (p. 361), the homotopy sequence of a bundle (p. 376), Theorem 3.30 (p. 241)
    and Corollary 3.39 (p. 250). Correct. Dimensions give $m=n+k$; for $n>1$ the fibre is not
    $S^0$, and $\pi_n(S^m)=0\to\pi_n(S^n)=\ZZ\to\pi_{n-1}(S^k)$ forces $k\le n-1$, while
    $k<n-1$ would give the exact segment $0=\pi_{k+1}(S^n)\to\pi_k(S^k)=\ZZ\to\pi_k(S^m)=0$; so
    $k=n-1$ and $m=2n-1$, with the exceptional $S^0\to S^1\to S^1$ at $n=1$ treated by its own
    exact segment. The mapping cone $C_p$ is a closed orientable $2n$-manifold, its $H^n$ and
    $H^{2n}$ are $\ZZ$, and Poincare duality in the form of Corollary 3.39 makes the cup product
    pairing nonsingular, so $\alpha^2=H(p)\gamma$ with $\gamma$ a generator forces $H(p)=\pm1$.
    Nothing changed. Not claimed: a published solution, and no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.B Exercise 2 and its hint, with Corollary 4.9, Corollary 4.25, the
    homotopy sequence of a fibration (§4.2, Theorem 4.41), the cellular chain complex of $C_p$ and
    Poincaré duality for a closed orientable manifold (Theorem 3.30 and Corollary 3.39). The
    dimension argument is correct: $m=n+k$; for $n>1$ the fibre is not $S^0$ over a simply connected
    base, so $k>0$ and $m>n$; $\pi_n(S^m)=0\to\pi_n(S^n)=\ZZ\to\pi_{n-1}(S^k)$ forces
    $k\le n-1$, while $k<n-1$ would give the exact segment $0=\pi_{k+1}(S^n)\to\pi_k(S^k)=\ZZ
    \to\pi_k(S^m)=0$; and for $n=1$ the segment $\pi_1(S^m)\to\pi_1(S^1)\to\pi_0(S^k)$ forces
    $k=0$, the double cover $S^0\to S^1\to S^1$. The Hopf-invariant half is also correct in
    substance: $C_p$ is a closed orientable $2n$-manifold, its $H^n$ and $H^{2n}$ are $\ZZ$, and
    Poincaré duality makes the cup product pairing perfect, so $\alpha^2=H(p)\beta$ with
    $H(p)=\pm1$. Four repairs. (1) $C_p$ was identified with a cone-on-the-fibre picture without
    saying what its boundary is; it is now the Thom space $D(E)/S(E)$ of the associated rank-$n$
    disc bundle, a closed $2n$-manifold, which is what makes both the manifold statement and the
    orientability argument work. (2) The cohomology of $C_p$ was asserted; it is now derived from
    which cells exist, as on `E-HAT-4.B-1`. (3) The symbol $\beta$ was used for the generator of
    $H^{2n}$ and then for an arbitrary element of $H^n$; the second is now $\alpha'=c\alpha$.
    (4) The text cited pages for Theorem 4.41, Corollaries 4.9 and 4.25, Theorem 3.30 and
    Corollary 3.39, and by the owner's correction of this date it cites the numbered statements
    only. The prose is now a structured proof. No statement changed. No retained solution set
    covers the exercise: Sam's set stops at §4.3. Not checked: no certificate; no obstruction-theory
    input is used, so none was verified.

---

::: {.problem}
Show that if $S^k \to S^m \xrightarrow{p} S^n$ is a fiber bundle, then $m = 2n-1$, $k = n-1$, and, when $n > 1$, $H(p) = \pm 1$.
[Show that $C_p$ is a manifold and apply Poincaré duality.]
:::

::: {.solution}
No retained solution set covers this exercise — Sam's set stops at §4.3 and the other sets retained for this project have no §4.B solution — so the argument is the card's own, following the hint printed with the exercise. It uses Corollary 4.9, Corollary 4.25, the homotopy exact sequence of a fibration (Theorem 4.41), the cellular chain complex of $C_p$ (the cellular boundary formula of §2.2 with Theorem 2.35), and Poincaré duality in the form of Theorem 3.30 with Corollary 3.39.

Let $S^k\to S^m\xrightarrow{p}S^n$ be a fibre bundle. A bundle is locally a product, so $m=n+k$.

::: pf

::: {.pf-step #dimensions}
$m=n+k$.

::: pf-proof
A point of $S^n$ has a neighbourhood $U$ with $p^{-1}(U)$ homeomorphic to $U\times S^k$, so $m=\dim S^m=n+k$.
:::

:::

::: {.pf-step #nonzero-fibre}
If $n>1$ then $k>0$, hence $m>n$.

::: pf-proof
For $n>1$ the base $S^n$ is simply connected. A bundle with fibre $S^0$ over a simply connected base is trivial, since the two possible images of a point in the fibre define a continuous local system with trivial monodromy, so its total space is $S^n\times S^0$, which is disconnected, whereas $S^m$ is connected. Hence $k\ne0$, that is $k>0$, and $m=n+k>n$.
:::

:::

::: {.pf-step #upper}
$k\le n-1$.

::: pf-proof
The fibration gives the exact segment $\pi_n(S^m)\to\pi_n(S^n)\to\pi_{n-1}(S^k)$. By step [](#nonzero-fibre){.pf-ref} $m>n$, so $\pi_n(S^m)=0$ by Corollary 4.9, while $\pi_n(S^n)\cong\ZZ$ by Corollary 4.25. Exactness makes $\ZZ\to\pi_{n-1}(S^k)$ injective, so $\pi_{n-1}(S^k)\ne0$; by Corollary 4.9 again, $\pi_i(S^k)=0$ for $i<k$, so $n-1\ge k$.
:::

:::

::: {.pf-step #lower}
$k\ge n-1$.

::: pf-proof
Suppose $k<n-1$. Then $k+1<n$, so $\pi_{k+1}(S^n)=0$ by Corollary 4.9, and $k<m$, so $\pi_k(S^m)=0$ by Corollary 4.9; also $\pi_k(S^k)\cong\ZZ$ by Corollary 4.25. The exact segment $\pi_{k+1}(S^n)\to\pi_k(S^k)\to\pi_k(S^m)$ is then $0\to\ZZ\to0$, which is impossible: exactness makes $\ZZ$ both a subgroup of $0$ and the image of $0$. Hence $k\ge n-1$.
:::

:::

::: {.pf-step #exceptional}
For $n=1$ the bundle is the double cover $S^0\to S^1\to S^1$, so $k=0$ and $m=1$.

::: pf-proof
Here $m=1+k$ and the exact segment is $\pi_1(S^m)\to\pi_1(S^1)\to\pi_0(S^k)$. If $k>0$ then $S^k$ is connected, so $\pi_0(S^k)$ is a single point and the map $\pi_1(S^1)\to\pi_0(S^k)$ is onto; exactness then makes $\pi_1(S^m)\to\pi_1(S^1)$ onto, whereas $m=1+k\ge2$ gives $\pi_1(S^m)=0$ and $\pi_1(S^1)=\ZZ$. Hence $k=0$ and $m=1$, which is the covering $S^0\to S^1\to S^1$.
:::

:::

::: {.pf-step #dimension-conclusion}
For $n>1$, $\boxed{m=2n-1,\ k=n-1}$.

::: pf-proof
Steps [](#upper){.pf-ref} and [](#lower){.pf-ref} give $k=n-1$, and step [](#dimensions){.pf-ref} gives $m=n+k=2n-1$. Step [](#exceptional){.pf-ref} treats $n=1$ separately, where the same two conclusions hold.
:::

:::

::: {.pf-step #manifold}
Let $n>1$, so the bundle is $S^{n-1}\to S^{2n-1}\xrightarrow{p}S^n$ with associated disc bundle $D^n\to D(E)\xrightarrow{\pi}S^n$ and sphere bundle $S(E)=S^{2n-1}$. Then $C_p$, the mapping cone of $p$, is the closed $2n$-manifold $D(E)/S(E)$.

::: pf-proof
The disc bundle $D(E)$ is a compact $2n$-manifold whose boundary is the sphere bundle $S(E)$, the total space of the bundle of unit vectors, which is $S^{2n-1}$ by step [](#dimension-conclusion){.pf-ref} and the hypothesis. Collapsing the boundary of a compact manifold with boundary gives a closed manifold of the same dimension, so $D(E)/S(E)$ is a closed $2n$-manifold. It is the mapping cone of $p$: the quotient of $D(E)$ by its boundary is the space obtained from $S^n$ by attaching the cone on each fibre, which is exactly $S^n\cup_p CS^{2n-1}$, and the homeomorphism is the identity on the zero section, which is a copy of $S^n$.
:::

:::

::: {.pf-step #orientable}
$C_p$ is orientable.

::: pf-proof
$D(E)$ carries the stable splitting $T D(E)\cong\pi^*(TS^n\oplus\xi)$ for the rank-$n$ vector bundle $\xi$ with $D(\xi)=E$, so $w_1(D(E))=\pi^*\bigl(w_1(S^n)+w_1(\xi)\bigr)$. Here $w_1(S^n)=0$ because $S^n$ is orientable, and $w_1(\xi)\in H^1(S^n;\ZZ_2)=0$ because $n>1$; hence $D(E)$ is orientable as a manifold with boundary, and collapsing the boundary preserves orientability.
:::

:::

::: {.pf-step #cohomology}
$H^n(C_p;\ZZ)\cong\ZZ$ and $H^{2n}(C_p;\ZZ)\cong\ZZ$, with $H^k(C_p;\ZZ)=0$ for the other $k>0$ other than $0$ and $n$.

::: pf-proof
As the mapping cone of $p$, $C_p$ has exactly one cell in each of the dimensions $0$, $n$ and $2n$, and none in any other dimension; its cellular chain complex is therefore $\ZZ$ in those three degrees and $0$ elsewhere. A boundary can be nonzero only between two of these degrees, which for $n>1$ never happens: the numbers $1$, $n+1$ and $2n+1$ are not in $\{0,n,2n\}$. So all boundaries vanish, the homology is $\ZZ$ in the three degrees, and the universal coefficient theorem, Theorem 3.2, gives the same for integral cohomology.
:::

:::

::: {.pf-step #duality}
The cup product pairing $H^n(C_p;\ZZ)\times H^n(C_p;\ZZ)\to H^{2n}(C_p;\ZZ)$ is perfect.

::: pf-proof
$C_p$ is a closed connected orientable $2n$-manifold by steps [](#manifold){.pf-ref} and [](#orientable){.pf-ref}, so Poincaré duality, Theorem 3.30, applies with any coefficients. Corollary 3.39 is its consequence for a closed orientable $n$-manifold: an element of $H^k$ is a generator of an infinite cyclic direct summand exactly when it pairs to a generator of $H^n$ with some element of $H^{n-k}$. Taking the complementary degrees to be $n$ and $2n-n=n$, this says that $\alpha\in H^n(C_p;\ZZ)$ generates the free group $H^n$ exactly when there is some $\alpha''\in H^n(C_p;\ZZ)$ with $\alpha\smile\alpha''$ a generator of $H^{2n}$.
:::

:::

::: {.pf-step #hopf}
$H(p)=\pm1$.

::: pf-proof
Let $\alpha$ generate $H^n(C_p;\ZZ)$ and $\beta$ generate $H^{2n}(C_p;\ZZ)$; then $\alpha^2=H(p)\beta$ defines the Hopf invariant of $p$, by §4.B. By step [](#cohomology){.pf-ref} $H^n=\ZZ\alpha$, so an element pairing with $\alpha$ to a generator has the form $c\alpha$ with $c\in\ZZ$, and by step [](#duality){.pf-ref} there is such a $c$ with $\alpha\smile c\alpha=c\,H(p)\beta$ a generator of $H^{2n}(C_p;\ZZ)\cong\ZZ$. A multiple $c\,H(p)\beta$ is a generator exactly when $c\,H(p)=\pm1$, which forces $H(p)=\pm1$.
:::

:::

::: {.pf-step}
Every sphere bundle $S^k\to S^m\to S^n$ satisfies $\boxed{m=2n-1,\ k=n-1}$, and when $n>1$ its projection has $\boxed{H(p)=\pm1}$.

::: pf-proof
The dimension statements are step [](#dimension-conclusion){.pf-ref}, the case $n=1$ being step [](#exceptional){.pf-ref}, and the Hopf invariant statement is step [](#hopf){.pf-ref}, which applies to every bundle with base $S^n$ for $n>1$ through the manifold $C_p$ of step [](#manifold){.pf-ref}.
:::

:::

:::
:::
