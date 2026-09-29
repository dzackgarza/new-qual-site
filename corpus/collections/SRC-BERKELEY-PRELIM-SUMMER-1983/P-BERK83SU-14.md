---
schema: qual/card@1
id: P-BERK83SU-14
kind: problem
title: Invariant equivalence relations for a transitive simple permutation group
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The relation defines a transitive action of G on its equivalence classes.
    The kernel is normal, hence is either G or trivial. In the first case the
    relation is universal; in the second the induced action on the classes is
    faithful. A regular A_5 action with classes given by cosets of a subgroup
    of order 2 shows that nontrivial proper invariant relations can occur.
---

::: {.problem}
Let $G$ be a transitive subgroup of $S_n$ acting on $\{1,\ldots,n\}$. Assume that $G$ is simple and that $\sim$ is an equivalence relation on $\{1,\ldots,n\}$ such that
\[
i\sim j\quad\Longrightarrow\quad \sigma(i)\sim\sigma(j)
\]
for every $\sigma\in G$.
What can one conclude about the equivalence relation $\sim$?
:::

::: {.solution}
Let
$$
X=\{1,\ldots,n\},
\qquad
\mathcal B=X/{\sim}
$$
be the set of equivalence classes.

::: pf

::: pf-step

The rule
$$
\sigma\cdot[i]=[\sigma(i)]
$$
defines a transitive action of $G$ on $\mathcal B$.

::: pf-proof

The stated hypothesis gives
$$
i\sim j
\quad\Longrightarrow\quad
\sigma(i)\sim\sigma(j).
$$
Applying the same implication to $\sigma^{-1}$ shows the converse, so
$$
i\sim j
\quad\Longleftrightarrow\quad
\sigma(i)\sim\sigma(j).
$$
Hence the displayed rule is well defined on equivalence classes.

For classes $[i]$ and $[j]$, transitivity of the action of $G$ on $X$
gives some $\sigma\in G$ with $\sigma(i)=j$. Then
$\sigma\cdot[i]=[j]$, so the induced action on $\mathcal B$ is
transitive.

:::

:::

::: {.pf-step #s2}

If
$$
K=\ker\bigl(G\to\operatorname{Sym}(\mathcal B)\bigr),
$$
then either $K=G$ or $K=\{1\}$.

::: pf-proof

The kernel $K$ is a normal subgroup of $G$. Since $G$ is simple, it
has no normal subgroups other than $\{1\}$ and $G$.

:::

:::

::: {.pf-step #s3}

If $K=G$, then $\sim$ is the universal equivalence relation.

::: pf-proof

If $K=G$, every element of $G$ fixes every class in $\mathcal B$.
Fix $i\in X$. For any $j\in X$, transitivity gives
$\sigma\in G$ with $\sigma(i)=j$. Since $\sigma$ fixes the class
$[i]$, one has
$$
[j]
=[\sigma(i)]
=
[i].
$$
Thus every two elements of $X$ are equivalent.

:::

:::

::: {.pf-step #s4}

If $K=\{1\}$, then the induced action of $G$ on the set of
equivalence classes is faithful.

::: pf-proof

This is exactly the assertion that the kernel of
$$
G\longrightarrow\operatorname{Sym}(\mathcal B)
$$
is trivial.

:::

:::

::: {.pf-step #s5}

No stronger conclusion, such as saying that $\sim$ must be
either equality or the universal relation, follows from the stated
hypotheses.

::: pf-proof

Let $G=A_5$ act on the set $X=G$ by left multiplication. This action
is transitive, and $A_5$ is simple. Let $H\le A_5$ be a subgroup of
order $2$, and define
$$
x\sim y
\quad\Longleftrightarrow\quad
x^{-1}y\in H.
$$
The equivalence classes are the right cosets $xH$, so each class has
two elements and there is more than one class.

For $g,x,y\in G$,
$$
(gx)^{-1}(gy)=x^{-1}y,
$$
so left multiplication preserves the relation. Thus this is a
nontrivial proper $G$-invariant equivalence relation satisfying all
the hypotheses.

:::

:::

::: {.pf-step #s6}

Consequently,
$$
\boxed{
\text{$\sim$ is universal, or $G$ acts faithfully on $X/{\sim}$.}
}
$$

::: pf-proof

By step [](#s2){.pf-ref}, the kernel of the induced action is either $G$ or
trivial. Step [](#s3){.pf-ref} identifies the first case with the universal
relation, and step [](#s4){.pf-ref} identifies the second with a faithful action.
Step [](#s5){.pf-ref} shows that the second case need not be the equality
relation.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} gives the complete conclusion forced by the hypotheses.

:::

:::

:::
