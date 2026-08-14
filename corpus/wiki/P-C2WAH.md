---
schema: qual/card@1
id: P-C2WAH
kind: problem
title: "Nilradical is intersection of primes"
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - prime-ideals
  - ideals
relations: []
review: draft
---

::: {.problem title="Nilradical is intersection of primes"}
The nilradical is the intersection of all prime ideals, i.e.
\[
\nilrad{R} = \Intersect_{\mathfrak{p} \in \spec(R)} \mathfrak{p}
\]
:::

::: {.solution}
\envlist

- $\nilrad{R} \subseteq \intersect \mathfrak{p}$:

- $x \in \nilrad{R} \implies x^n = 0 \in \mathfrak p$, and induction on $n$ using that $\mfp$ is prime gives $x\in \mathfrak{p}$.

- $R\sm \nilrad{R} \subseteq \union_{\mfp} (R\sm \mathfrak{p})$:

- Fix $a$ non-nilpotent and define $S = \theset{I\normal R \suchthat a^n\not\in I \text{ for any } n\geq 1}$.

- Then $\gens{0}\in S$, and the union of a chain in $S$ is again in $S$, so Zorn's lemma gives an ideal $\mfp$ maximal *within $S$*.

- Such a $\mfp$ is prime: if $a', b'\not\in \mfp$ then $\mfp + \gens{a'}$ and $\mfp + \gens{b'}$ strictly contain $\mfp$, hence leave $S$, so some $a^m \in \mfp + \gens{a'}$ and $a^n \in \mfp + \gens{b'}$; then $a^{m+n} \in \mfp + \gens{a'b'}$, which forces $a'b'\not\in\mfp$.

- Note $\mfp$ need not be a maximal ideal, only maximal among the ideals avoiding all powers of $a$.
  Since $\mfp\in S$ we have $a\not\in \mfp$, so $a$ escapes the intersection.
:::
