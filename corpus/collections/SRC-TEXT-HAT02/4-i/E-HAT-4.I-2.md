---
schema: qual/card@1
id: E-HAT-4.I-2
kind: problem
title: "Suspension of $K(\\ZZ_m \\times \\ZZ_n, 1)$ for coprime $m, n$"
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
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.I, printed p. 470, with Proposition 4I.1 on printed
    p. 467 (whose statement in the extracted text has $\vee$ misread as $\times$; the PDF page
    prints $\Sigma(X\times Y)\simeq\Sigma X\vee\Sigma Y\vee\Sigma(X\wedge Y)$), the homology of
    lens spaces in Example 2.43 on printed pp. 144--145, the Künneth formula of Theorem 3B.6 on
    printed p. 275 and Corollary 4.33 on printed p. 367. The mathematics was right: the reduced
    homology of $K(\ZZ_m,1)$ is $m$-torsion and that of $K(\ZZ_n,1)$ is $n$-torsion, Bézout gives
    $A\otimes B=0$ from $um+vn=1$, $\operatorname{Tor}$ is annihilated by both $m$ and $n$ and
    hence by $1$, the Künneth summands of $X\wedge Y$ all vanish, and $\Sigma(X\wedge Y)$ is a
    simply connected CW complex with vanishing reduced homology, hence contractible. Rewritten
    from a nest of `pf` blocks whose proofs were noun phrases ('homology of $K(\ZZ_n,1)$',
    'Euclidean algorithm', 'algebra of torsion abelian groups', 'suspension isomorphism in
    homology', 'Whitehead's Theorem and Hurewicz Theorem') and which ended in a 'Conclusion ...
    Q.E.D.' step proved by naming two labels. Five steps now, each carrying its argument.
    Not claimed: a certificate.
---

::: {.problem}
Using the Künneth formula, show that $\Sigma K(\ZZ_m \times \ZZ_n, 1) \simeq \Sigma K(\ZZ_m, 1) \vee \Sigma K(\ZZ_n, 1)$ if $m$ and $n$ are relatively prime.
Thus to determine stable splittings of $K(\ZZ_n, 1)$ it suffices to do the case that $n$ is a prime power, as in Proposition 4I.3.
:::

::: {.solution}
Write $X=K(\ZZ_m,1)$ and $Y=K(\ZZ_n,1)$. The exercise is Exercise 2 of §4.I, and the proof uses the Künneth formula as its hint directs.

::: pf

::: {.pf-step #s1}

$\Sigma(X\times Y)\simeq\Sigma X\vee\Sigma Y\vee\Sigma(X\wedge Y)$ for CW complexes $X$, $Y$.

::: pf-proof

This is Proposition 4I.1. It applies here because Eilenberg--MacLane spaces of discrete groups are CW complexes.

:::

:::

::: {.pf-step #s2}

$K(\ZZ_m\times\ZZ_n,1)\simeq K(\ZZ_m,1)\times K(\ZZ_n,1)$.

::: pf-proof

$\pi_1$ of a product is the product of the fundamental groups, and the universal cover of $K(\ZZ_m,1)\times K(\ZZ_n,1)$ is the product of the universal covers of the two factors, which is contractible as a product of contractible spaces. A CW complex with fundamental group $\ZZ_m\times\ZZ_n$ and contractible universal cover is a $K(\ZZ_m\times\ZZ_n,1)$.

:::

:::

::: {.pf-step #s3}

$\widetilde H_i(X)$ is annihilated by $m$ and $\widetilde H_j(Y)$ by $n$, so for $\gcd(m,n)=1$ every group $A=\widetilde H_i(X)$ and $B=\widetilde H_j(Y)$ satisfies $A\otimes B=0$ and $\operatorname{Tor}_1^\ZZ(A,B)=0$.

::: pf-proof

$K(\ZZ_m,1)$ is the infinite lens space, whose integral homology is $\ZZ_m$ in odd positive degrees and $0$ in even positive degrees by the computation for lens spaces in Example 2.43, so $m\cdot\widetilde H_i(X)=0$ for every $i$; symmetrically $n\cdot\widetilde H_j(Y)=0$. Choose $u,v$ with $um+vn=1$. Then $a\otimes b=u(ma\otimes b)+v(a\otimes nb)=0$ for $a\in A$, $b\in B$. And $\operatorname{Tor}_1^\ZZ(A,B)$ is annihilated by $m$, because multiplication by $m$ is zero on $A$ and Tor is a functor in each variable, and annihilated by $n$ for the same reason on $B$; hence it is annihilated by $um+vn=1$, so it is zero.

:::

:::

::: {.pf-step #s4}

$\widetilde H_k(X\wedge Y)=0$ for all $k$.

::: pf-proof

By the Künneth formula of Theorem 3B.6 applied to $X\times Y$, and the identification of $\widetilde H_*(X\wedge Y)$ with the quotient of $\widetilde H_*(X\times Y)$ by $\widetilde H_*(X\vee Y)=\widetilde H_*(X)\oplus\widetilde H_*(Y)$, which removes exactly the terms with $i=0$ or $j=0$ because reduced homology vanishes in degree $0$,
$$
\widetilde H_k(X\wedge Y)\cong\bigoplus_{i+j=k}\widetilde H_i(X)\otimes\widetilde H_j(Y)\ \oplus\bigoplus_{i+j=k-1}\operatorname{Tor}_1^\ZZ\bigl(\widetilde H_i(X),\widetilde H_j(Y)\bigr),
$$
and every summand vanishes by the previous step.

:::

:::

::: {.pf-step #s5}

$\Sigma(X\wedge Y)\simeq *$, and hence $\Sigma K(\ZZ_m\times\ZZ_n,1)\simeq\Sigma K(\ZZ_m,1)\vee\Sigma K(\ZZ_n,1)$ when $\gcd(m,n)=1$.

::: pf-proof

A suspension is simply connected, and the suspension isomorphism gives $\widetilde H_k(\Sigma(X\wedge Y))\cong\widetilde H_{k-1}(X\wedge Y)=0$ for all $k$. By the homology form of Whitehead's theorem, Corollary 4.33, a map from a simply connected CW complex to a point that induces isomorphisms on all homology groups is a homotopy equivalence, so $\Sigma(X\wedge Y)\simeq *$. Substituting into the splitting of the first step and applying the second gives the stated equivalence.

:::

:::

:::

:::
