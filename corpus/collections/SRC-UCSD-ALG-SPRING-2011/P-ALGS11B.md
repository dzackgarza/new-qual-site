---
schema: qual/card@1
id: P-ALGS11B
kind: problem
title: Unique subgroup of order the smallest prime divides is central
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Group Actions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 2 of the UCSD Algebra Qualifying Exam, Spring 2011, p. 1 of the
    two-page paper retained at assets/attachments/SP11_200_Algebra_Qual.pdf, is the statement the
    card answers, and the paragraph at the head of the solution records that the paper prints the
    questions and no solutions, so the argument is the card's own. Checked: the statement and the
    printed hint against the paper's text layer at the page named; that the card's route through
    the conjugation map into the automorphism group, rather than through the hint's permutation of
    H minus e, reaches the same conclusion and is recorded as a different route;
    `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering and the QED. Not
    checked: no retained solution exists to compare the argument with, and no other card of the
    collection in this pass.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 2 of the official UCSD Spring 2011 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Verified the hint argument via the conjugation homomorphism into Aut(H), using that every prime divisor of |G| is at least p whereas every prime divisor of |Aut(H)|=p-1 is smaller than p.
---

::: {.problem}
Let $G$ be a finite group and let $p$ be the smallest prime dividing $\cardinality{G}$.
Assume that $G$ has a unique subgroup $H$ of order $p$.
Show that $H$ is contained in the center of $G$.

Hint: For each $g \in G$, prove that the permutation $\sigma_g(h) = ghg^{-1}$ of the set $H \setminus \{e\}$ is trivial by investigating its order.
:::

::: {.solution}

The problem is Problem 2 of the UCSD Algebra Qualifying Exam, Spring 2011, printed on p. 1 of the two-page paper retained at `assets/attachments/SP11_200_Algebra_Qual.pdf`, with its hint. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and it takes a route different from the printed hint — instead of the order of the permutation $\sigma_g$ of $H\setminus\{e\}$, it uses the conjugation map into $\operatorname{Aut}(H)$ and the fact that the order of $\theta(g)$ divides both $\cardinality{G}$ and $p-1$, which rests on the same observation that no prime smaller than $p$ divides $\cardinality{G}$.

::: pf

::: {.pf-step #s1}

The subgroup $H$ is normal in $G$.

::: pf-proof

For every $g\in G$, the conjugate $gHg^{-1}$ is again a subgroup of $G$ of order $p$.
By uniqueness of $H$, one has
$$
gHg^{-1}=H.
$$
Thus $H\trianglelefteq G$.

:::

:::

::: pf-step

Conjugation defines a homomorphism
$$
\theta:G\longrightarrow \operatorname{Aut}(H),
\qquad
\theta(g)(h)=ghg^{-1}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, conjugation by every $g\in G$ preserves $H$.
Restriction of conjugation to $H$ is therefore an automorphism of $H$, and
$$
\theta(g_1g_2)=\theta(g_1)\theta(g_2)
$$
for all $g_1,g_2\in G$.

:::

:::

::: {.pf-step #s3}

For every $g\in G$, the automorphism $\theta(g)$ is trivial.

::: pf-proof

Since $\cardinality{H}=p$, the group $H$ is cyclic, so
$$
\cardinality{\operatorname{Aut}(H)}=p-1.
$$
Let $r=\operatorname{ord}(\theta(g))$.
Because $\theta$ is a homomorphism, $r$ divides $\operatorname{ord}(g)$, hence $r$ divides $\cardinality{G}$ by Lagrange's theorem.
Also $r$ divides $p-1$ because $\theta(g)\in\operatorname{Aut}(H)$.

If a prime $q$ divided $r$, then $q\mid \cardinality{G}$ and therefore $q\ge p$, since $p$ is the smallest prime dividing $\cardinality{G}$.
But $q\mid p-1$ also gives $q\le p-1<p$, a contradiction.
Hence $r$ has no prime divisor, so $r=1$.
Therefore $\theta(g)=\operatorname{id}_H$.

:::

:::

::: pf-step

Hence $H\subseteq Z(G)$.

::: pf-proof

By step [](#s3){.pf-ref}, for every $g\in G$ and every $h\in H$,
$$
ghg^{-1}=h.
$$
Equivalently, $gh=hg$.
Thus every element of $H$ commutes with every element of $G$, so
$$
H\le Z(G).
$$

:::

:::

:::

:::
