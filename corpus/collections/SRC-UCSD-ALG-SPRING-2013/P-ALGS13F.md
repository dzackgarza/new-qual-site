---
schema: qual/card@1
id: P-ALGS13F
kind: problem
title: Splitting field of $x^p-2$ over $\QQ$ and the Galois action
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card was two label-steps with empty proofs over eight
    unproved claims, and its (b) asserted that 'all p(p-1) pairs must be realized' without the
    count being available: the degree p(p-1) was quoted, not proved. It is now five proved
    steps: the root list and the two inclusions giving E = Q(zeta_p, alpha); the degree, with
    Eisenstein for [Q(alpha):Q] = p, the cyclotomic degree p-1, and the intersection Q(alpha) ∩
    Q(zeta_p) = Q by the tower law inside each field; the Galois count |Gal| = [E:Q]; the
    constraint on the pair (sigma(zeta_p), sigma(alpha)) together with injectivity; and the
    bijection given by the two counts. The answers are unchanged, including the p = 2 remark.
    Not claimed: a retained solution set; the collection's provenance is the examination paper
    only.
---

::: {.problem}
Let $E$ be the splitting field of $x^p - 2$ over $\QQ$, where $p$ is an odd prime.

(a) Prove that $E = \QQ[\zeta_p, \sqrt[p]{2}]$ and find $[E:\QQ]$.
(Here $\zeta_p$ is a primitive $p$th root of unity.)

(b) Find $\{(\sigma(\zeta_p), \sigma(\sqrt[p]{2})) \mid \sigma \in \mathrm{Gal}(E/\QQ)\}$.
Justify your answer.
:::

::: {.solution}
Throughout $p$ is an odd prime, $\alpha \coloneqq \sqrt[p]{2}$ is the positive real $p$-th root of $2$, $\zeta_{p} \coloneqq e^{2\pi i/p}$, and $E$ is the splitting field of $x^{p}-2$ over $\QQ$ inside $\CC$. The collection's `provenance` is the Spring 2013 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #roots}
(a) The roots of $x^{p}-2$ are $\zeta_{p}^{k}\alpha$, $0 \le k \le p-1$, and $E = \QQ(\zeta_{p},\alpha)$.

::: pf-proof
$(\zeta_{p}^{k}\alpha)^{p} = \zeta_{p}^{kp}\alpha^{p} = 2$, so each is a root, and they are $p$ distinct numbers; since $x^{p}-2$ has degree $p$, these are all its roots. The splitting field is generated over $\QQ$ by the roots, so $E = \QQ(\alpha, \zeta_{p}\alpha, \ldots, \zeta_{p}^{p-1}\alpha)$. The inclusion $\subseteq \QQ(\zeta_{p},\alpha)$ is clear, and conversely $\zeta_{p} = (\zeta_{p}\alpha)/\alpha$ and $\alpha$ are both in $E$, so $\QQ(\zeta_{p},\alpha) \subseteq E$; hence $E = \QQ(\zeta_{p},\alpha)$.

:::

:::

::: {.pf-step #degree}
(a) $[E:\QQ] = p(p-1)$.

::: pf-proof
$x^{p}-2$ is Eisenstein at the prime $2$, so it is irreducible over $\QQ$ and $[\QQ(\alpha):\QQ] = p$; the cyclotomic polynomial $\Phi_{p}$ has degree $p-1$ and is irreducible, so $[\QQ(\zeta_{p}):\QQ] = p-1$. For the compositum, $[E:\QQ] = [\QQ(\zeta_{p}):\QQ]\cdot[E:\QQ(\zeta_{p})]$ also $\QQ(\alpha) \cap \QQ(\zeta_{p})$ has degree over $\QQ$ dividing both $p$ and $p-1$ — by the tower law applied inside $\QQ(\alpha)$ and inside $\QQ(\zeta_{p})$ respectively — hence equals $\QQ$, and then $[\QQ(\zeta_{p},\alpha):\QQ(\zeta_{p})] = [\QQ(\alpha):\QQ] = p$, giving $[E:\QQ] = p(p-1)$.

:::

:::

::: {.pf-step #galois}
(b) $E/\QQ$ is Galois of degree $p(p-1)$, so $\cardinality{\Gal(E/\QQ)} = p(p-1)$, and each $\sigma$ is determined by the pair $\bigl(\sigma(\zeta_{p}), \sigma(\alpha)\bigr)$.

::: pf-proof
$E$ is the splitting field over $\QQ$ of the separable polynomial $x^{p}-2$ — separable because $\QQ$ has characteristic $0$ — so $E/\QQ$ is Galois, and a finite Galois extension has as many automorphisms as its degree: $\cardinality{\Gal(E/\QQ)} = [E:\QQ] = p(p-1)$ by step [](#degree){.pf-ref}. Since $E$ is generated over $\QQ$ by $\zeta_{p}$ and $\alpha$, a $\QQ$-automorphism is determined by the images of these two elements.

:::

:::

::: {.pf-step #pairs}
(b) $\bigl(\sigma(\zeta_{p}), \sigma(\alpha)\bigr) = \bigl(\zeta_{p}^{a}, \zeta_{p}^{b}\alpha\bigr)$ with $1 \le a \le p-1$ and $0 \le b \le p-1$, and every such pair occurs exactly once.

::: pf-proof
A $\QQ$-automorphism carries a root of $x^{p}-2$ to a root of $x^{p}-2$, so $\sigma(\alpha) = \zeta_{p}^{b}\alpha$ for a unique $b \in \theset{0,\ldots,p-1}$; it carries the primitive $p$-th root $\zeta_{p}$ to another primitive $p$-th root of unity, that is to $\zeta_{p}^{a}$ with $a$ coprime to $p$, which for prime $p$ means $1 \le a \le p-1$. This gives an injective map $\sigma \mapsto (a,b)$ into a set of $p(p-1)$ pairs, and by step [](#galois){.pf-ref} the domain has $p(p-1)$ elements, so the map is a bijection: every pair $(a,b)$ with those constraints is realized by exactly one automorphism.

:::

:::

::: pf-step
(b) The required set is $\boxed{\theset{\bigl(\zeta_{p}^{a}, \zeta_{p}^{b}\alpha\bigr) \mid 1 \le a \le p-1,\ 0 \le b \le p-1}}$, a set of $p(p-1)$ pairs.

::: pf-proof
Steps [](#pairs){.pf-ref} show both inclusions: each automorphism gives a pair of that form, and the counting argument in the same step shows every such pair arises. The number of pairs is $(p-1)\cdot p = p(p-1) = \cardinality{\Gal(E/\QQ)}$, consistent with the bijection.

:::

:::

:::
:::

::: {.remark title="Variations"}
For $p=2$ the same description holds: the splitting field of $x^2-2$ is $\QQ(\sqrt2)$, of degree $p(p-1)=2$, and its Galois group is $\ZZ/2\ZZ\rtimes(\ZZ/2\ZZ)^\times\cong\ZZ/2\ZZ$, generated by $\sqrt2\mapsto-\sqrt2$.
For odd $p$, the automorphisms are $\sigma_{a,b}\colon\sqrt[p]2\mapsto\zeta_p^a\sqrt[p]2$, $\zeta_p\mapsto\zeta_p^b$ with $a\in\ZZ/p\ZZ$, $b\in(\ZZ/p\ZZ)^\times$, and $\sigma_{a,b}\mapsto\begin{pmatrix}b&a\\0&1\end{pmatrix}$ identifies the group with $\ZZ/p\ZZ\rtimes(\ZZ/p\ZZ)^\times$.
:::
