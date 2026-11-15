---
schema: qual/card@1
id: E-OWZBO
kind: problem
title: Uniqueness of free products
classification:
  areas:
  - topology
  topics:
  - Free Products
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §68 Exercise 4, printed p. 421, whose statement is Theorem 68.4 on printed p. 418. The card had
    paraphrased the theorem's hypothesis as "the families are free products with the extension property", and
    now reproduces the printed hypothesis: the families {i_alpha(G_alpha)} and {i'_alpha(G_alpha)} generate G
    and G' respectively, and both G and G' satisfy the extension property of Lemma 68.3 (printed p. 418), the
    book having already proved in Lemma 68.5 that the extension property forces freeness, so the theorem does
    not assume it. No complete published solution located; the searches are listed in the COMPLAINTS.md entry
    for §61--§73. Proof checked line by line against Lemma 68.3 and Theorem 68.4 as printed, and it is the same
    two-homomorphism argument the book uses for Theorem 67.6 (printed p. 410), which was read for comparison.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144) for §68 Exercise 4 (printed p. 418); queries and sets are in the
    COMPLAINTS.md entry for §66--§73 of SRC-TEXT-MUN00. Query used: "Munkres Theorem 68.4 uniqueness of free
    products exercise solution extension property proof". Nothing usable located. Math StackExchange 4884788,
    "Munkres lemma 68.5", does contain an answer proving Theorem 68.4 in the generalized form, as its search
    excerpt shows, but the body could not be read (the API answered "too many requests from this IP, more
    requests available in 75550 seconds", the page a Cloudflare human check, and no Wayback snapshot exists),
    so nothing is transcribed from it and no claim is made that its argument agrees with this card's. dbFin has
    no §68 page, the Riverside Part 9 sheet answers §68 Exercises 2 and 3, the fourteen repositories stop at
    Chapter 3. The card's own proof was re-read: it is the two-homomorphism argument, checked against Lemma
    68.3 and Theorem 68.4 as printed on p. 418 and against Theorem 67.6 (printed p. 410). Nothing changed.
---

::: {.exercise}

Prove Theorem 68.4 (uniqueness of free products): let $\theset{G_\alpha}_{\alpha \in J}$ be a family of groups.
Suppose $G$ and $G'$ are groups and $i_\alpha: G_\alpha \to G$ and $i_\alpha': G_\alpha \to G'$ are families of monomorphisms, such that the families $\theset{i_\alpha(G_\alpha)}$ and $\theset{i_\alpha'(G_\alpha)}$ generate $G$ and $G'$, respectively.
If both $G$ and $G'$ have the extension property stated in Lemma 68.3, then there is a unique isomorphism $\phi: G \to G'$ such that $\phi \circ i_\alpha = i_\alpha'$ for each $\alpha$.
:::

::: {.solution}

The extension property of Lemma 68.3 (printed p. 418) reads: given any group $H$ and any family of homomorphisms $h_\alpha:G_\alpha\to H$, there is a unique homomorphism $h:G\to H$ with $h\circ i_\alpha=h_\alpha$ for all $\alpha$.

::: pf

::: pf-step

There are homomorphisms $\phi:G\to G'$ and $\psi:G'\to G$ with $\phi\circ i_\alpha=i_\alpha'$ and $\psi\circ i_\alpha'=i_\alpha$.

::: pf-proof

Apply the extension property of $G$ to the family $i_\alpha':G_\alpha\to G'$, which gives a unique $\phi$ with $\phi\circ i_\alpha=i_\alpha'$; apply the extension property of $G'$ to the family $i_\alpha:G_\alpha\to G$, which gives a unique $\psi$ with $\psi\circ i_\alpha'=i_\alpha$.

:::

:::

::: pf-step

$\psi\circ\phi=\mathrm{id}_G$ and $\phi\circ\psi=\mathrm{id}_{G'}$.

::: pf-proof

For every $\alpha$, $(\psi\circ\phi)\circ i_\alpha=\psi\circ i_\alpha'=i_\alpha=\mathrm{id}_G\circ i_\alpha$. Both $\psi\circ\phi$ and $\mathrm{id}_G$ are homomorphisms $G\to G$ whose restrictions to every $i_\alpha(G_\alpha)$ agree, and the uniqueness clause of the extension property of $G$ applied to the family $h_\alpha=i_\alpha$ gives $\psi\circ\phi=\mathrm{id}_G$. Interchanging the roles of $G$ and $G'$ gives $\phi\circ\psi=\mathrm{id}_{G'}$.

:::

:::

::: pf-step

$\phi$ is an isomorphism, and it is the only one with $\phi\circ i_\alpha=i_\alpha'$.

::: pf-proof

By step 2, $\phi$ has the two-sided inverse $\psi$, so $\phi$ is a bijective homomorphism. If $\phi'$ is any homomorphism $G\to G'$ with $\phi'\circ i_\alpha=i_\alpha'$ for all $\alpha$, then $\phi'$ and $\phi$ agree on every $i_\alpha(G_\alpha)$, and these sets generate $G$; two homomorphisms agreeing on a generating set agree everywhere, so $\phi'=\phi$. This is also the uniqueness clause of the extension property.

:::

:::

::: pf-qed

Steps 1--3 prove Theorem 68.4 as printed.

:::

:::
:::
