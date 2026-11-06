---
schema: qual/card@1
id: E-AMD-CCULHKQJ
kind: problem
title: Fundamental theorem of Galois theory
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source says K/F Galois without finiteness; the solution uses the finite Galois correspondence, so the statement now says finite Galois. The bulleted parts are relabelled (a)-(c).'
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof, one top-level step per part. What was
    checked: the statement (already repaired on 2026-10-29 to say finite Galois and to
    label the parts (a)-(c); nothing further), and the existing prose against a fresh
    re-derivation: (a) K splits a separable polynomial over F, hence over E, so K/E is
    normal and separable, and every E-automorphism fixes F, so H <= G; (b) E/F is
    separable as an intermediate extension of a separable one, so Galois = normal,
    and normality is equivalent to sigma(E) = E for every sigma in G, which by
    Fix(sigma H sigma^{-1}) = sigma(E) is equivalent to H being normal in G; (c)
    restriction rho: G -> Gal(E/F) is defined, has kernel H, and is surjective because
    normality of K/F extends embeddings, so Gal(E/F) = G/H. Correct. No source
    solution is retained for this card, so no source comparison was made. What was not
    checked: any printed source; the three quoted facts (Galois correspondence, the
    degree formula, extension of embeddings) are used as standard.
---

::: {.exercise}
Let $K/E/F$ be a tower of fields with $K/F$ finite Galois, and write $g(L/M)$ for the Galois group of $L/M$.

(a) Show that $K/E$ is Galois with $g(K/E) \leq g(K/F)$.

(b) Show that $E/F$ is Galois $\iff g(K/E) \normal g(K/F)$.

(c) Show that in this case, $g(E/F) = g(K/F) / g(K/E)$.
:::

::: {.solution}
Let $F\subseteq E\subseteq K$ with $K/F$ finite Galois, and put $G=\Gal(K/F)$ and $H=\Gal(K/E)$; recall that for a finite Galois extension the fixed field of a subgroup of its Galois group is the corresponding intermediate field, and that $\abs{\Gal(K/M)}=[K:M]$ for every intermediate field $M$.

::: pf

::: {.pf-step #part-a}
(a) $K/E$ is Galois and $H\leq G$.

::: pf-proof
Since $K/F$ is Galois, it is the splitting field over $F$ of a separable polynomial $f\in F[x]$. As $F\subseteq E$, the same polynomial lies in $E[x]$, and over $K$ it splits into distinct linear factors none of which is new; so $K/E$ is normal and separable, hence Galois. Every $E$-automorphism of $K$ fixes $E$ and therefore fixes $F\subseteq E$, so it is an $F$-automorphism of $K$: $H\subseteq G$. Both are subgroups of $\Aut(K)$, so $H\leq G$.
:::

:::

::: {.pf-step #part-b}
(b) $E/F$ is Galois if and only if $H\trianglelefteq G$.

::: pf-proof
$E/F$ is separable, because separability of $K/F$ passes to intermediate extensions, so $E/F$ is Galois exactly when it is normal, that is, exactly when every $F$-embedding of $E$ into an algebraic closure carries $E$ to itself.

For $\sigma\in G$ the fixed field of $\sigma H\sigma^{-1}$ is $\sigma(E)$: an automorphism $\tau$ of $K$ fixes $\sigma(E)$ pointwise exactly when $\sigma^{-1}\tau\sigma$ fixes $E$ pointwise, that is, exactly when $\tau\in\sigma H\sigma^{-1}$. By the Galois correspondence, $H\trianglelefteq G$ means $\sigma H\sigma^{-1}=H$ for every $\sigma\in G$, which by the previous sentence is the same as $\sigma(E)=E$ for every $\sigma\in G$.

Finally, since $K/F$ is normal, every $F$-embedding of $E$ into an algebraic closure extends to an element of $G$; so the condition "$\sigma(E)=E$ for every $\sigma\in G$" is the same as "every $F$-embedding of $E$ fixes $E$", which is normality of $E/F$. Chaining the three equivalences gives $E/F$ Galois iff $H\trianglelefteq G$.
:::

:::

::: {.pf-step #part-c}
(c) If $E/F$ is Galois then $\Gal(E/F)=\Gal(K/F)/\Gal(K/E)$.

::: pf-proof
Assume $E/F$ Galois; by step [](#part-b){.pf-ref} $H\trianglelefteq G$ and $\sigma(E)=E$ for every $\sigma\in G$. Then restriction gives a group homomorphism $\rho\colon G\to\Gal(E/F)$, $\rho(\sigma)=\sigma|_E$: it is well defined because $\sigma(E)=E$, and it is a homomorphism because restriction respects composition.

Its kernel is $H$: $\sigma|_E=\mathrm{id}_E$ exactly when $\sigma$ fixes $E$ pointwise, that is, when $\sigma\in\Gal(K/E)$.

It is surjective: given $\tau\in\Gal(E/F)$, the extension $K/F$ is normal, so the embedding $\tau\colon E\to K$ extends to an $F$-embedding $K\to K$, which is an element $\sigma\in G$ with $\sigma|_E=\tau$.

The first isomorphism theorem applied to $\rho$ gives $\Gal(E/F)\cong G/\ker\rho=G/H$, which is the assertion.
:::

:::

::: {.pf-step}
The three parts hold, so $\abs{\Gal(K/E)}=[K:E]$, $E/F$ is Galois precisely when $\Gal(K/E)\trianglelefteq\Gal(K/F)$, and then the Galois group of $E/F$ is the quotient.

::: pf-proof
Parts (a), (b) and (c) are steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref} and [](#part-c){.pf-ref}. The counts quoted in the summary are the degree formula $\abs{\Gal(K/M)}=[K:M]$ for a finite Galois extension, applied to $M=E$.
:::

:::

:::
:::
