---
schema: qual/card@1
id: P-T4KHN
kind: problem
title: The nilradical is $\sqrt{(0)}$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Show that the nilradical is $\sqrt{(0)}$." and names no ring; the statement declares a commutative ring $R$.'
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired. The card's single step asserted 'by definition sqrt((0)) is the set of nilpotent
    elements, that is the nilradical', which is an unpacking only if the nilradical is defined
    as the set of nilpotents; the corpus's own definition card [[P-C2WAH]] defines it as the
    intersection of the prime ideals, and then the assertion is exactly what has to be proved.
    The card now proves both inclusions — nilpotents lie in every prime by induction from
    primality, and a non-nilpotent survives in some prime obtained by contracting a maximal
    ideal of the localisation at the multiplicative set of its powers — and closes by checking
    that sqrt((0)) is an ideal. The statement is unchanged. Not claimed: a retained solution
    set.
---

::: {.problem}
Let $R$ be a commutative ring. Show that the nilradical of $R$ is $\sqrt{(0)}$.
:::

::: {.solution}
Throughout $R$ is a commutative ring, $\sqrt{(0)} = \theset{x \in R \mid x^{n} = 0 \text{ for some } n \ge 1}$ is the set of nilpotent elements, and the nilradical is the ideal of nilpotent elements, equivalently the intersection of all prime ideals of $R$. The two descriptions are what this card reconciles: with the nilradical defined as $\sqrt{(0)}$ the statement is definitional, and the content is the identification with the intersection of the prime ideals, which is [[P-C2WAH]]; with the nilradical defined as that intersection, the content is the two inclusions proved below.

::: pf

::: {.pf-step #in-primes}
Every element of $\sqrt{(0)}$ lies in every prime ideal of $R$.

::: pf-proof
Let $x^{n} = 0$ with $n \ge 1$ and let $\mathfrak{p}$ be prime. Since $0 \in \mathfrak{p}$ and $\mathfrak{p}$ is an ideal, $x^{n} \in \mathfrak{p}$; by induction on $n$, $x^{n} \in \mathfrak{p}$ together with primality — which says that $yz \in \mathfrak{p}$ implies $y \in \mathfrak{p}$ or $z \in \mathfrak{p}$ — gives $x \in \mathfrak{p}$.

:::

:::

::: {.pf-step #localise}
If $a \in R$ is not nilpotent then there is a prime ideal $\mathfrak{p}$ with $a \notin \mathfrak{p}$.

::: pf-proof
Let $S \coloneqq \theset{a^{n} \mid n \ge 0}$, a multiplicative set containing $1$. The localisation $S^{-1}R$ is not the zero ring: $1/1 = 0$ in $S^{-1}R$ would mean $a^{m} \cdot 1 = 0$ for some $m$, that is $a^{m} = 0$, contrary to hypothesis. So $S^{-1}R$ has a maximal ideal $\mathfrak{m}$, and $\mathfrak{p} \coloneqq \pi^{-1}(\mathfrak{m})$ under the localisation map $\pi$ is a prime ideal of $R$, being the contraction of a prime ideal. If $a \in \mathfrak{p}$ then $a/1 \in \mathfrak{m}$, but $a/1$ is a unit of $S^{-1}R$ because $1/a = a^{0}/a$ is invertible in the localisation; a unit lies in no proper ideal, so $a \notin \mathfrak{p}$.

:::

:::

::: {.pf-step #equality}
$\sqrt{(0)} = \bigcap_{\mathfrak{p} \text{ prime}}\mathfrak{p}$.

::: pf-proof
Step [](#in-primes){.pf-ref} gives the inclusion $\subseteq$. For the reverse, if $a$ is not nilpotent, step [](#localise){.pf-ref} produces a prime ideal missing it, so $a$ lies outside the intersection; hence the intersection is contained in the nilpotents.

:::

:::

::: pf-step
The nilradical of $R$ is $\sqrt{(0)}$, the ideal of nilpotent elements.

::: pf-proof
By step [](#equality){.pf-ref} the intersection of the prime ideals — the nilradical in the sense of [[P-C2WAH]] — is exactly $\sqrt{(0)}$, and $\sqrt{(0)}$ is closed under addition and multiplication by elements of $R$: if $x^{m} = y^{n} = 0$ then every term of $(x+y)^{m+n}$ contains $x^{m}$ or $y^{n}$ and vanishes, and $(rx)^{m} = r^{m}x^{m} = 0$. So it is an ideal, and it is the nilradical in either sense.

:::

:::

:::
:::
