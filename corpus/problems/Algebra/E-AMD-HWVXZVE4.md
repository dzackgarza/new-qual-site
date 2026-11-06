---
schema: qual/card@1
id: E-AMD-HWVXZVE4
kind: problem
title: The radical of an ideal is the intersection of the primes containing it
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Prime Ideals
  - Nilpotence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard theorem; no repair needed, including the degenerate case I = R,
    where the family of primes containing I is empty and the intersection is R,
    which matches sqrt(R) = R), and the existing prose solution against a fresh
    re-derivation: frozenset S = {x^k : k >= 0} is multiplicatively closed and
    contains 1; x not in sqrt(I) makes I disjoint from S; the family of ideals
    containing I and disjoint from S is nonempty and closed under unions of
    chains, so Zorn gives a maximal p; maximality forces p + (a) and p + (b) to
    meet S, and the product of the two witnesses lands in p + (ab) inside p,
    contradicting disjointness when ab is in p, so p is prime. Correct; the
    structured proof spells out the union-of-a-chain argument and the ideal
    product, which the prose compressed. No source solution is retained for this
    card (SRC-UNSORTED-ALGEBRA, a compilation with no provenance href), so no
    source comparison was made. What was not checked: any printed source.
---

::: {.exercise}
Show that for an ideal $I\trianglelefteq R$ in a commutative ring $R$, its radical $\sqrt{I}$ is the intersection of all prime ideals containing $I$.
:::

::: {.solution}
Let $R$ be a commutative ring with $1$, $I\trianglelefteq R$ an ideal, and $\sqrt I=\theset{x\in R:x^n\in I\text{ for some }n\geq1}$ its radical. Write $\bigcap_{I\subseteq\mathfrak p}\mathfrak p$ for the intersection of the prime ideals containing $I$, which is $R$ when there are none.

::: pf

::: {.pf-step #inside}
$\sqrt I\subseteq\bigcap_{I\subseteq\mathfrak p}\mathfrak p$.

::: pf-proof
Let $x\in\sqrt I$ and let $\mathfrak p\supseteq I$ be prime. Choose $n\geq1$ with $x^n\in I$, so $x^n\in\mathfrak p$. We show by induction on $k\geq1$ that $y^k\in\mathfrak p$ implies $y\in\mathfrak p$: for $k=1$ this is the hypothesis, and for $k+1$ we have $y^{k+1}=y\cdot y^k\in\mathfrak p$, so primeness gives $y\in\mathfrak p$ or $y^k\in\mathfrak p$, and the second alternative gives $y\in\mathfrak p$ by the induction hypothesis. Applying this to $y=x$ and $k=n$ gives $x\in\mathfrak p$; since $\mathfrak p$ was an arbitrary prime containing $I$, $x$ lies in the intersection.
:::

:::

::: {.pf-step #outside}
If $x\notin\sqrt I$, then some prime ideal $\mathfrak p\supseteq I$ does not contain $x$.

::: pf-proof
Let $S=\theset{x^k:k\geq0}$; it contains $1=x^0$ and is closed under multiplication, since $x^jx^k=x^{j+k}$.

::: {.pf-step #disjoint}
$I\cap S=\varnothing$.

::: pf-proof
If $x^k\in I$ with $k\geq0$ then $k\neq0$, because $x^0=1\notin I$ would force $I=R$ and then $\sqrt I=R\ni x$, contrary to hypothesis; so $k\geq1$ and $x\in\sqrt I$, again contrary to hypothesis.
:::

:::

::: {.pf-step #zorn}
Among the ideals $J$ with $I\subseteq J$ and $J\cap S=\varnothing$ there is one maximal under inclusion.

::: pf-proof
The family is nonempty because it contains $I$, which is disjoint from $S$ by step [](#disjoint){.pf-ref}. It is partially ordered by inclusion, and the union of a chain of its members is again an ideal containing $I$ and still disjoint from $S$, since an element of the union lies in some member of the chain and no member meets $S$; so every chain has an upper bound in the family. Zorn's lemma, applied to this nonempty partially ordered set in which every chain is bounded above, produces a maximal member $\mathfrak p$.
:::

:::

::: {.pf-step #prime}
$\mathfrak p$ is prime.

::: pf-proof
First $\mathfrak p\neq R$, since $1\in S$ and $\mathfrak p\cap S=\varnothing$. Now let $a,b\in R$ with $ab\in\mathfrak p$ and suppose for contradiction that $a\notin\mathfrak p$ and $b\notin\mathfrak p$. Then $\mathfrak p+(a)$ and $\mathfrak p+(b)$ strictly contain $\mathfrak p$, so by maximality of $\mathfrak p$ neither is disjoint from $S$; choose $m,n\geq0$ with $x^m\in\mathfrak p+(a)$ and $x^n\in\mathfrak p+(b)$. Multiplying, $x^{m+n}\in\bigl(\mathfrak p+(a)\bigr)\bigl(\mathfrak p+(b)\bigr)\subseteq\mathfrak p+(ab)\subseteq\mathfrak p$, where the last inclusion uses $ab\in\mathfrak p$ and $\mathfrak p$ being an ideal. That contradicts $\mathfrak p\cap S=\varnothing$, since $x^{m+n}\in S$. Hence $a\in\mathfrak p$ or $b\in\mathfrak p$.
:::

:::

By step [](#zorn){.pf-ref} and step [](#prime){.pf-ref}, $\mathfrak p$ is a prime ideal containing $I$, and $x\notin\mathfrak p$ because $x\in S$ and $\mathfrak p\cap S=\varnothing$.
:::

:::

::: {.pf-step}
$\sqrt I=\bigcap_{I\subseteq\mathfrak p}\mathfrak p$.

::: pf-proof
Step [](#inside){.pf-ref} gives one inclusion. For the other, let $x\notin\sqrt I$; step [](#outside){.pf-ref} produces a prime $\mathfrak p\supseteq I$ with $x\notin\mathfrak p$, so $x$ is not in the intersection. Hence the intersection is contained in $\sqrt I$, and the two inclusions give equality.
:::

:::

:::
:::
