---
schema: qual/card@1
id: E-HAT-3.1-9
kind: problem
title: Degree $d$ maps act on $H^n(S^n;G)$ by multiplication by $d$
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 9; it matches the printed text. The card makes the implicit $n>0$ of the degree explicit.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the Kronecker pairing argument: naturality gives
    $\langle f^*\alpha,[S^n]\rangle=\langle\alpha,f_*[S^n]\rangle=d\langle\alpha,[S^n]\rangle$, and
    evaluation on the fundamental class is an isomorphism $H^n(S^n;G)\cong G$, so
    $f^*\alpha=d\alpha$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 9 (p.205), with the n>0 that the degree of Exercise 9 needs made explicit. All four terse proofs replaced by the actual reasons: H^n(S^n;G) = Hom(Z,G) = G from Theorem 3.2 p.195 with Ext vanishing since H_{n-1}(S^n) is free or zero; the fundamental class as generator of H_n(S^n) = Z from p.134; naturality of the evaluation in the form (f^*phi)(sigma) = phi(f_# sigma), equivalently precomposition with f_* under the universal coefficient isomorphism by the naturality of p.196; and deg f as the multiplier of [S^n]. Not covered: n = 0, where H^0(S^0;G) = G^2 and the conclusion fails.
---

::: {.problem}
For $n>0$, show that if $f: S^n \to S^n$ has degree $d$ then $f^*: H^n(S^n; G) \to H^n(S^n; G)$ is multiplication by $d$.
:::

::: {.solution}

::: pf

::: pf-step

$H^n(S^n; G) \cong G$ and $H_n(S^n) \cong \ZZ$, with the natural pairing $H^n(S^n; G) \times H_n(S^n) \to G$ given by evaluation.

::: pf-proof

$H_n(S^n)=\ZZ$ for $n>0$ is the computation of §2.1-2.2, and $H^n(S^n;G)\cong\operatorname{Hom}(H_n(S^n),G)$ is Theorem 3.2 (p.195) because $H_{n-1}(S^n)$ is $0$ for $n\ge2$ and $\ZZ$ for $n=1$, both free and so of vanishing Ext; hence $H^n(S^n;G)\cong G$.

:::

:::

::: pf-step

Let $\alpha \in H^n(S^n; G)$ and $[S^n] \in H_n(S^n)$ the fundamental class.

::: pf-proof

For $n>0$ the group $H_n(S^n)$ is infinite cyclic and $[S^n]$ denotes its generator, the fundamental class, as on p.134; $\alpha$ is an arbitrary element of $H^n(S^n;G)$, which by the previous step is $G$.

:::

:::

::: {.pf-step #s3}

By naturality of the Kronecker pairing, $\langle f^*\alpha, [S^n] \rangle = \langle \alpha, f_*[S^n] \rangle$.

::: pf-proof

At the cochain level $(f^*\varphi)(\sigma)=\varphi(f_\#\sigma)$, so the evaluation pairing $\langle\alpha,\sigma\rangle=\alpha(\sigma)$ of a cocycle on a cycle satisfies $\langle f^*\alpha,\sigma\rangle=\langle\alpha,f_\#\sigma\rangle$ and passes to homology. Equivalently, under the isomorphism of Theorem 3.2 (p.195) the map $f^*$ corresponds to precomposition with $f_*$, which is the naturality of the universal coefficient sequence stated on p.196.

:::

:::

::: {.pf-step #s4}

$f_*[S^n] = d[S^n]$ (by definition of degree).

::: pf-proof

p.134: the degree of $f:S^n\to S^n$ is defined by $f_*[S^n]=d[S^n]$, which is legitimate because $H_n(S^n)\cong\ZZ$.

:::

:::

::: {.pf-step #s5}

Hence $\langle f^*\alpha, [S^n] \rangle = \langle \alpha, d[S^n] \rangle = d\langle \alpha, [S^n] \rangle$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Since the pairing with $[S^n]$ identifies $H^n(S^n; G)$ with $G$ (it is an isomorphism), $f^*\alpha = d\alpha$.

::: pf-proof

Step [](#s5){.pf-ref} (the pairing $\alpha \mapsto \langle \alpha, [S^n] \rangle$ is an isomorphism $H^n(S^n;G) \to G$).

:::

:::

::: {.pf-step #s7}

Hence $f^*$ is multiplication by $d$.

::: pf-proof

Step [](#s6){.pf-ref}: $f^*\alpha=d\alpha$ for every $\alpha\in H^n(S^n;G)$, which is the assertion.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
