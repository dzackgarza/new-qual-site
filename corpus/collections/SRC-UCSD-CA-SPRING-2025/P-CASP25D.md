---
schema: qual/card@1
id: P-CASP25D
kind: problem
title: Automorphisms of the punctured disk $\DD\setminus\{a\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Automorphisms
  - Conformal Maps
  - Punctured Disk
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: a bounded holomorphic function on the
    punctured disk has a removable singularity at the puncture, and the extension is bounded by $1$
    and nonconstant, so the maximum principle puts it strictly inside $\DD$; the inverse extends
    too, and the two composite identities, known on $G$, extend by the identity theorem; a bijection
    of $\DD$ carrying $G$ onto $G$ carries the complement $\{a\}$ onto itself; restrictions of disk
    automorphisms fixing $a$ are automorphisms of $G$; and the automorphisms of $\DD$ fixing $a$ are
    $\varphi_a^{-1}R_\theta\varphi_a$, since the stabilizer of $0$ is the rotations by Schwarz's
    lemma. Added: the reason the extension is nonconstant and the Schwarz-lemma identification of the
    stabilizer, which the prose asserted. Repaired: `\operatorname{id}` is written `\id`, the
    vocabulary macro, and the automorphism $\phi_a$ is named $\varphi_a$ so as not to clash with the
    radical-symmetry notation elsewhere. The collection's provenance is the Spring 2025 examination
    paper, so no retained solution set covers the problem.
---

::: {.problem}
Let $a \in \DD$ and set $G = \DD \setminus \{a\}$.
Find all analytic automorphisms of $G$, i.e., find all one-to-one and onto analytic functions from $G$ to $G$.
Write down the expressions for such functions (can be unsimplified).
Prove your answer.
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem and the argument is the card's own. Write $G=\DD\setminus\{a\}$ and $\varphi_a(z)=(z-a)/(1-\overline a z)$ for the disk automorphism sending $a$ to $0$.

::: pf

::: {.pf-step #extension}
Every automorphism $F\colon G\to G$ extends to a holomorphic $\widetilde F\colon\DD\to\DD$.

::: pf-proof
$F$ maps into $\DD$, so it is bounded near $a$ and the isolated singularity at $a$ is removable; the extension $\widetilde F$ is holomorphic on $\DD$ and bounded by $1$. It is nonconstant, since $F$ is injective on the nonempty set $G$; a nonconstant holomorphic function on $\DD$ cannot attain the value $1$ in modulus at an interior point by the maximum modulus principle, so $\abs{\widetilde F}<1$ on $\DD$.
:::

:::

::: {.pf-step #automorphism}
$\widetilde F$ is an automorphism of $\DD$, and $\widetilde F(a)=a$.

::: pf-proof
The inverse $F^{-1}$ is an automorphism of $G$ as well, so it extends to a holomorphic $\widetilde H\colon\DD\to\DD$ by the same argument with $F^{-1}$ in place of $F$. On the punctured disk, where both extensions agree with the original maps, $\widetilde H\circ\widetilde F=\id$ and $\widetilde F\circ\widetilde H=\id$; two holomorphic functions agreeing on $G$, which has accumulation points in $\DD$, agree on $\DD$ by the identity theorem. So $\widetilde F$ is biholomorphic with inverse $\widetilde H$. Since $\widetilde F$ is a bijection of $\DD$ carrying $G$ onto $F(G)=G$, it carries the complement $\{a\}$ onto the complement $\{a\}$, that is $\widetilde F(a)=a$.
:::

:::

::: {.pf-step #converse}
Every automorphism of $\DD$ fixing $a$ restricts to an automorphism of $G$.

::: pf-proof
Let $\Phi$ be an automorphism of $\DD$ with $\Phi(a)=a$. Then $\Phi$ maps $G=\DD\setminus\{a\}$ bijectively onto $\DD\setminus\{\Phi(a)\}=G$, and its restriction is holomorphic, injective and onto, with holomorphic inverse the restriction of $\Phi^{-1}$.
:::

:::

::: {.pf-step}
$\boxed{F(z)=\varphi_a^{-1}\bigl(e^{i\theta}\varphi_a(z)\bigr)\text{ for some }\theta\in\RR}$ are all the automorphisms of $G$.

::: pf-proof
By steps [](#extension){.pf-ref} and [](#automorphism){.pf-ref} every automorphism of $G$ is the restriction of a disk automorphism fixing $a$, and by step [](#converse){.pf-ref} every such restriction is an automorphism of $G$. The disk automorphisms fixing $a$ are exactly $\varphi_a^{-1}\circ R_\theta\circ\varphi_a$ with $R_\theta(w)=e^{i\theta}w$: conjugation by $\varphi_a$ identifies the automorphisms of $\DD$ fixing $a$ with those fixing $0$, and an automorphism of $\DD$ fixing $0$ is a rotation, by Schwarz's lemma applied to it and to its inverse. Hence the automorphisms of $G$ are the functions displayed, with $\theta$ ranging over $\RR$ modulo $2\pi$.
:::

:::

:::
:::
