---
schema: qual/card@1
id: E-HAT-4.D-5
kind: problem
title: Gysin sequence and Hopf invariant of sphere bundles
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the Gysin computation: with
    k >= 1 and m = n + k, the terms H^k(S^m) and H^{k+1}(S^m) both vanish for n > 1, so cupping
    with the Euler class is an isomorphism Z -> H^{k+1}(S^n), which forces k + 1 = n and hence
    m = 2n - 1. The dimension step is now justified as the manifold dimension of the total space
    rather than by a homotopy-group comparison, and orientability by triviality of the monodromy
    action of pi_1(S^n) = 0. For the Hopf invariant: the disc bundle has an integral Thom class
    (Theorem 4D.10, p. 442), the Thom isomorphism (Corollary 4D.9, p. 441) applied to 1 shows the
    Thom class generates H^n of the cone, the identity at the end of section 4.D (p. 444) gives
    Phi(e) = U^2, and since e generates, U^2 generates, so the integer in alpha^2 = H(p) beta can
    be taken as +-1. The n = 1 case is separated, as the card had it, because the vanishing used
    for n > 1 fails there. Statement and hint unchanged; Adams' theorem is quoted, not used.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the Gysin computation: with
    k >= 1 and m = n + k, the terms H^k(S^m) and H^{k+1}(S^m) both vanish for n > 1, so cupping
    with the Euler class is an isomorphism Z -> H^{k+1}(S^n), which forces k + 1 = n and hence
    m = 2n - 1. The dimension step is now justified as the manifold dimension of the total space
    rather than by a homotopy-group comparison, and orientability by triviality of the monodromy
    action of pi_1(S^n) = 0. For the Hopf invariant: the disc bundle has an integral Thom class
    (Theorem 4D.10, p. 442), the Thom isomorphism (Corollary 4D.9, p. 441) applied to 1 shows the
    Thom class generates H^n of the cone, the identity at the end of section 4.D (p. 444) gives
    Phi(e) = U^2, and since e generates, U^2 generates, so the integer in alpha^2 = H(p) beta can
    be taken as +-1. The n = 1 case is separated, as the card had it, because the vanishing used
    for n > 1 fails there. Statement and hint unchanged; Adams' theorem is quoted, not used.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the Gysin computation: with
    k >= 1 and m = n + k, the terms H^k(S^m) and H^{k+1}(S^m) both vanish for n > 1, so cupping
    with the Euler class is an isomorphism Z -> H^{k+1}(S^n), which forces k + 1 = n and hence
    m = 2n - 1. The dimension step is now justified as the manifold dimension of the total space
    rather than by a homotopy-group comparison, and orientability by triviality of the monodromy
    action of pi_1(S^n) = 0. For the Hopf invariant: the disc bundle has an integral Thom class
    (Theorem 4D.10, p. 442), the Thom isomorphism (Corollary 4D.9, p. 441) applied to 1 shows the
    Thom class generates H^n of the cone, the identity at the end of section 4.D (p. 444) gives
    Phi(e) = U^2, and since e generates, U^2 generates, so the integer in alpha^2 = H(p) beta can
    be taken as +-1. The n = 1 case is separated, as the card had it, because the vanishing used
    for n > 1 fails there. Statement and hint unchanged; Adams' theorem is quoted, not used.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the page locators in the card's text are removed; the Gysin sequence of §4.D and Corollaries 4D.9 and 4D.3 are cited by
    number, and the Gysin sequence, which the book leaves unnumbered, by the section that
    states it, each read in `tmp/sources/hatcher-2002-algebraic-topology.md`. The earlier
    events keep their text (QUAL-11); these citations supersede their page locators. No step
    changes.

- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.D Exercise 5. The proof is correct, but the sentence "no retained
    solution set covers this exercise" is false: the half of the exercise that asks for the dimension
    is word for word §4.2 Exercise 32, which Sam's §4.2 Exercise 32 and Proudfoot's homework 7,
    Problem 32, both solve. The sentence now records that. The n=1 case is separated in the card and
    the general argument starts at n>1.
---

::: {.problem}
Use the Gysin sequence to show that for a fiber bundle $S^k \to S^m \xrightarrow{p} S^n$ we must have $k = n-1$ and $m = 2n-1$.
Then use the Thom isomorphism to show that the Hopf invariant of $p$ must be $\pm 1$.
[Hence $n = 1, 2, 4, 8$ by Adams' theorem.]
:::

::: {.solution}
The Gysin sequence of the sphere bundle forces $k+1=n$: the flanking groups vanish, so cupping with the Euler class is an isomorphism $\ZZ\to H^{k+1}(S^n)$, which is possible only when $k+1=n$. Coning the fibers gives a disc bundle whose Thom class generates the middle cohomology of the mapping cone and whose square is the image of the Euler class, so the Hopf invariant is $\pm1$. The argument is this card's own, and a retained solution covers the half of the exercise that asks for the dimension: that half is word for word §4.2 Exercise 32, solved in **Sam, §4.2 Exercise 32** (`tmp/sources/hatcher-solutions-sam-2008.md`) and in **Proudfoot, homework 7, Problem 32** (`tmp/sources/uoregon-proudfoot-634-hw7.md`); the sentence claiming that no retained set covers the exercise was false.

::: pf

::: {.pf-step #setup}
For a fiber bundle $S^k\to S^m\xrightarrow{p}S^n$ with $n>1$ one has $k\ge1$, $m=n+k$, and the bundle is orientable.

::: pf-proof
If $k=0$ the bundle is a two-sheeted covering of the simply connected $S^n$, so its total space is disconnected, while $S^m$ is connected; hence $k\ge1$. A fiber bundle with base a manifold of dimension $n$ and fiber a manifold of dimension $k$ is a manifold of dimension $n+k$, the local trivializations giving charts, so $m=n+k$. And a sphere bundle is orientable when $\pi_1$ of the base acts trivially on $H_k$ of the fiber; here $\pi_1(S^n)=0$ for $n>1$, so the action is trivial.
:::

:::


::: {.pf-step #gysin}
Cup product with the Euler class $e\in H^{k+1}(S^n;\ZZ)$ is an isomorphism $H^0(S^n)\to H^{k+1}(S^n)$, and $H^{k+1}(S^n)\cong\ZZ$.

::: pf-proof
The Gysin sequence of the oriented sphere bundle (§4.D) reads
$$
\cdots\to H^k(S^m)\xrightarrow{p_!}H^0(S^n)\xrightarrow{\smile e}H^{k+1}(S^n)\xrightarrow{p^*}H^{k+1}(S^m)\to\cdots
$$
The two outer groups vanish: $H^k(S^m)=0$ since $m=n+k>k$, and $H^{k+1}(S^m)=0$ since $m=n+k>k+1$ because $n>1$. Hence $\smile e$ is an isomorphism. Since $H^0(S^n)=\ZZ$ and the reduced cohomology of $S^n$ is $\ZZ$ only in degree $n$, $H^{k+1}(S^n)\cong\ZZ$ forces $k+1=n$, and then $e$ is a generator up to sign.
:::

:::


::: {.pf-step #dims}
$k=n-1$ and $m=2n-1$.

::: pf-proof
$k=n-1$ is step [](#gysin){.pf-ref}, and $m=n+k$ is step [](#setup){.pf-ref}; substituting gives $m=2n-1$.
:::

:::


::: {.pf-step #thom}
There is an oriented disc bundle $V\to S^n$ with $\partial V$ the given sphere bundle, an integral Thom class $U\in H^n(V,S(V);\ZZ)$, and $V/S(V)\simeq C_p$.

::: pf-proof
Coning off each fiber of the sphere bundle gives a disc bundle: over each trivializing chart the fiber $S^k$ is replaced by $D^{k+1}=D^n$ with boundary $S^k$, and the transition functions act on the disc by coning the homeomorphisms of the sphere, which glues the pieces to an oriented $D^n$-bundle $V$ over $S^n$ with $\partial V$ the sphere bundle. By Theorem 4D.10 (printed p.~442) an oriented bundle has an integral Thom class, in the direction orientable implies Thom class, which is the one used. The quotient $V/S(V)$ is homotopy equivalent to the mapping cone $C_p$: both are obtained by coning off the sphere bundle along the fibers and collapsing the zero section, $C_p$ being the cone on $E$ with the copy of $B$ collapsed to a point, and the disc bundle is exactly the result of coning each fiber; so collapsing the boundary of the disc bundle and collapsing the base in the cone give the same space up to homotopy.
:::

:::


::: {.pf-step #generates}
The Thom class $U$, regarded as a class in $H^n(C_p;\ZZ)$, generates.

::: pf-proof
The Thom isomorphism of Corollary 4D.9 is $\Phi\colon H^i(S^n)\to H^{i+n}(V,S(V))$, $\Phi(b)=p^*(b)\smile U$. At $i=0$ with $b=1$ this gives $\Phi(1)=U$, so $U$ is the image under an isomorphism of a generator of $H^0(S^n)=\ZZ$, hence generates $H^n(V,S(V))\cong H^n(C_p)\cong\ZZ$. A generator of the middle cohomology of the cone is what the definition of the Hopf invariant requires.
:::

:::


::: {.pf-step #square}
$\Phi(e)=U\smile U$ in $H^{2n}(V,S(V);\ZZ)$, and $H(p)=\pm1$.

::: pf-proof
The identity at the end of §4.D says that under the Thom isomorphism the Euler class corresponds to the square of the Thom class, $\Phi(e)=U\smile U$. Since $\Phi$ is an isomorphism and $e$ generates $H^n(S^n)$ by step [](#gysin){.pf-ref}, $U^2$ generates $H^{2n}(C_p;\ZZ)\cong\ZZ$. The Hopf invariant of $p$ is defined (printed p.~427) by writing $\alpha^2=H(p)\beta$ for a generator $\alpha$ of $H^n(C_p)$ and a generator $\beta$ of $H^{2n}(C_p)$; taking $\alpha=U$ makes $\alpha^2=U^2$ a generator, so the integer $H(p)$ is $\pm1$.
:::

:::


::: {.pf-step #n1}
For $n=1$ the only possibility is $k=0$ and $m=1$.

::: pf-proof
If $n=1$ and $k\ge1$ then $m=1+k\ge2$ so $\pi_1(S^m)=0$, while a fibration with connected fiber gives a surjection $\pi_1(S^m)\to\pi_1(S^1)=\ZZ$, which is impossible. Hence $k=0$ and $m=1$; the Hopf-invariant argument above used $n>1$ and does not apply.
:::

:::


::: {.pf-step #conclusion}
A fiber bundle $S^k\to S^m\to S^n$ forces $k=n-1$ and $m=2n-1$, and for $n>1$ the Hopf invariant of $p$ is $\pm1$.

::: pf-proof
Steps [](#gysin){.pf-ref} and [](#dims){.pf-ref} give the dimensions for $n>1$, step [](#n1){.pf-ref} settles $n=1$, and steps [](#thom){.pf-ref}, [](#generates){.pf-ref} and [](#square){.pf-ref} give the Hopf invariant. Adams' theorem, restricting $n$ to $1,2,4,8$, is quoted in the statement and is not used.
:::

:::

:::
:::
