---
schema: qual/card@1
id: P-RZ2JV
kind: problem
title: Maximal submodules are those with simple quotient, and the roots of unity have
  no maximal submodule
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Maximal Ideals
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card was a stack of label-steps with no proofs and 23 nested
    steps that carried the mathematics in one-sentence claims with nothing behind them, closed
    by a pf-qed reading 'Steps [#s1], [#s2] and [#s3] prove parts (a), (b), and (c),
    respectively'. Every part now has a proof: the lattice isomorphism theorem written as the
    pair of mutually inverse maps, the cyclic-and-prime-order characterisation of a simple
    abelian group with both cases (infinite order and composite order) handled, and the
    divisibility argument for mu_infinity including the existence of p-th roots in C and the
    conclusion pM = M. The answers are unchanged. Not claimed: a retained solution set; the
    collection's provenance is the examination paper only.
---
::: {.problem}
Let $R$ be a ring, and let $M$ be an $R$-module. An $R$-submodule $N \subset M$ is called **maximal** if $N \ne M$ and there is no $R$-submodule $P$ satisfying $N \subsetneq P \subsetneq M$.

(a) Show that an $R$-submodule $N$ of $M$ is maximal if and only if the quotient module $M/N$ is a **simple** $R$-module (that is, $M/N \ne \{0\}$ and $M/N$ has no submodules other than $\{0\}$ and $M/N$).

(b) Let $M$ be a $\ZZ$-module (an abelian group). Show that a submodule $N \subseteq M$ is maximal if and only if the quotient $\cardinality{M/N} = p$ for some prime number $p$.

(c) Let $M = \mu_\infty = \{z \in \CC^\times : z^n = 1 \text{ for some } n \in \ZZ^+\}$ be the multiplicative group of all complex roots of unity, viewed as a $\ZZ$-module. Show that $M$ has no maximal $\ZZ$-submodules.
:::

::: {.solution}
Throughout $R$ is a ring, $M$ an $R$-module, $N \subseteq M$ a submodule, and $M/N$ the quotient module; a module is simple when it is nonzero and has no submodules other than $0$ and itself. Part (c) takes $M = \mu_{\infty} \subseteq \CC^{\times}$, the group of all roots of unity, as a $\ZZ$-module under multiplication. The collection's `provenance` is the Fall 2018 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #a}
(a) $N$ is maximal in $M$ if and only if $M/N$ is simple.

::: pf-proof
The quotient map $\pi\colon M \to M/N$ induces an inclusion-preserving bijection between the submodules of $M$ containing $N$ and the submodules of $M/N$, sending $P$ to $P/N = \pi(P)$ and $Q$ to $\pi^{-1}(Q)$; this is the lattice isomorphism theorem for modules, and the two maps are mutually inverse because $\pi$ is surjective with kernel $N$. Under it, $N$ corresponds to $0$ and $M$ to $M/N$, so the proper intermediate submodules $N \subsetneq P \subsetneq M$ correspond exactly to the nonzero proper submodules $0 \subsetneq P/N \subsetneq M/N$. Hence $N$ is maximal — that is, $N \ne M$ with no such $P$ — exactly when $M/N \ne 0$ with no such $P/N$, which is simplicity of $M/N$.

:::

:::

::: {.pf-step #b}
(b) For a $\ZZ$-module $M$ the submodule $N$ is maximal if and only if $M/N$ has exactly $p$ elements for some prime $p$.

::: pf-proof
$\ZZ$-submodules of $M$ are exactly the subgroups, so a submodule is maximal exactly when the subgroup is maximal, that is when $M/N$ is a simple $\ZZ$-module by step [](#a){.pf-ref}, which is the same as $M/N$ being a simple abelian group. A simple abelian group $A$ is cyclic: for $0 \ne a \in A$ the subgroup $\ZZ a$ is nonzero, hence equals $A$. Its order is prime: if $A$ is infinite then $\ZZ a \cong \ZZ$ has the proper nonzero subgroup $2\ZZ a$, and if $\abs{A} = mn$ with $m, n > 1$ then $A$ has a subgroup of order $m$ by Cauchy's theorem (or by the structure of cyclic groups), proper and nonzero. Conversely a group of prime order $p$ has, by Lagrange, no subgroup other than $0$ and itself, so it is simple. Composing with step [](#a){.pf-ref} gives the equivalence.

:::

:::

::: {.pf-step #c}
(c) $M = \mu_{\infty}$ has no maximal $\ZZ$-submodule.

::: pf-proof
First, $M$ is divisible by every prime: given $x \in M$ there is $m \ge 1$ with $x^{m} = 1$, and choosing $y \in \CC^{\times}$ with $y^{p} = x$ — which exists because $\CC$ is algebraically closed — one has $y^{pm} = (y^{p})^{m} = x^{m} = 1$, so $y \in \mu_{\infty} = M$ and $x = y^{p}$. Hence $pM = M$ for every prime $p$. Now suppose $N \subsetneq M$ is maximal. By step [](#b){.pf-ref} the quotient $M/N$ has $p$ elements for some prime $p$, so $p(M/N) = 0$, that is $pM \subseteq N$. But $pM = M$, so $M \subseteq N$, contradicting $N \subsetneq M$. Therefore no maximal submodule exists.

:::

:::

::: {.pf-step #c-concl}
All three parts hold: the maximal submodules are the kernels of surjections onto simple modules, over $\ZZ$ these are the subgroups with quotient of prime order, and $\mu_{\infty}$ has none.

::: pf-proof
Part (a) is step [](#a){.pf-ref}, part (b) step [](#b){.pf-ref}, and part (c) step [](#c){.pf-ref}, whose argument uses the primality conclusion of (b) together with divisibility of $\mu_{\infty}$.

:::

:::

:::
:::
