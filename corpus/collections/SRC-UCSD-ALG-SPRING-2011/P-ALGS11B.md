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
Let $G$ be a finite group and let $p$ be the smallest prime dividing $|G|$.
Assume that $G$ has a unique subgroup $H$ of order $p$.
Show that $H$ is contained in the center of $G$.

Hint: For each $g \in G$, prove that the permutation $\sigma_g(h) = ghg^{-1}$ of the set $H \setminus \{e\}$ is trivial by investigating its order.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The subgroup $H$ is normal in $G$.

::: pf-proof

For every $g\in G$, the conjugate $gHg^{-1}$ is again a subgroup of $G$ of order $p$.
By uniqueness of $H$, one has
\[
gHg^{-1}=H.
\]
Thus $H\trianglelefteq G$.

:::

:::

::: pf-step

Conjugation defines a homomorphism
\[
\theta:G\longrightarrow \operatorname{Aut}(H),
\qquad
\theta(g)(h)=ghg^{-1}.
\]

::: pf-proof

By step [](#s1){.pf-ref}, conjugation by every $g\in G$ preserves $H$.
Restriction of conjugation to $H$ is therefore an automorphism of $H$, and
\[
\theta(g_1g_2)=\theta(g_1)\theta(g_2)
\]
for all $g_1,g_2\in G$.

:::

:::

::: {.pf-step #s3}

For every $g\in G$, the automorphism $\theta(g)$ is trivial.

::: pf-proof

Since $|H|=p$, the group $H$ is cyclic, so
\[
|\operatorname{Aut}(H)|=p-1.
\]
Let $r=\operatorname{ord}(\theta(g))$.
Because $\theta$ is a homomorphism, $r$ divides $\operatorname{ord}(g)$, hence $r$ divides $|G|$ by Lagrange's theorem.
Also $r$ divides $p-1$ because $\theta(g)\in\operatorname{Aut}(H)$.

If a prime $q$ divided $r$, then $q\mid |G|$ and therefore $q\ge p$, since $p$ is the smallest prime dividing $|G|$.
But $q\mid p-1$ also gives $q\le p-1<p$, a contradiction.
Hence $r$ has no prime divisor, so $r=1$.
Therefore $\theta(g)=\operatorname{id}_H$.

:::

:::

::: pf-step

Hence $H\subseteq Z(G)$.

::: pf-proof

By step [](#s3){.pf-ref}, for every $g\in G$ and every $h\in H$,
\[
ghg^{-1}=h.
\]
Equivalently, $gh=hg$.
Thus every element of $H$ commutes with every element of $G$, so
\[
H\le Z(G).
\]

:::

:::

:::

:::
