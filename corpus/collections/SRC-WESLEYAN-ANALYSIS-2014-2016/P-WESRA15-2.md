---
schema: qual/card@1
id: P-WESRA15-2
kind: problem
title: 'Uniqueness of finite measures agreeing on a generating algebra'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $(X,\mathcal A)$ be a measurable space and let $\mathcal C\subset\mathcal A$ be an algebra with $\mathcal A=\sigma(\mathcal C)$.
Let $\mu,\nu$ be finite measures such that
$$
\mu(C)=\nu(C)\qquad(C\in\mathcal C).
$$
Prove that $\mu(A)=\nu(A)$ for every $A\in\mathcal A$.

Hint: show that the collection of all sets on which $\mu$ and $\nu$ agree is a $\sigma$-algebra.
:::

::: {.solution}

Let
$$
\mathcal D=\{A\in\mathcal A:\mu(A)=\nu(A)\}.
$$
The useful closure property here is that $\mathcal D$ is a Dynkin system; it need not be a $\sigma$-algebra merely from its definition.

::: pf

::: {.pf-step #s1-1}

One has $X\in\mathcal D$.


::: pf-proof

Because $\mathcal C$ is an algebra, $X\in\mathcal C$. The hypothesis therefore gives
$$
\mu(X)=\nu(X),
$$
so $X\in\mathcal D$.

:::

:::

::: {.pf-step #s1-2}

If $A,B\in\mathcal D$ and $A\subseteq B$, then
$$
B\setminus A\in\mathcal D.
$$


::: pf-proof

The measures are finite, so
$$
\mu(B\setminus A)=\mu(B)-\mu(A)
$$
and similarly for $\nu$. Since $A,B\in\mathcal D$,
$$
\mu(B)-\mu(A)=\nu(B)-\nu(A).
$$
Hence $B\setminus A\in\mathcal D$.

:::

:::

::: {.pf-step #s1-3}

If $A_1,A_2,\ldots\in\mathcal D$ are pairwise disjoint, then
$$
\bigcup_{n=1}^{\infty}A_n\in\mathcal D.
$$


::: pf-proof

Countable additivity gives
$$
\mu\left(\bigcup_{n=1}^{\infty}A_n\right)
=\sum_{n=1}^{\infty}\mu(A_n)
=\sum_{n=1}^{\infty}\nu(A_n)
=\nu\left(\bigcup_{n=1}^{\infty}A_n\right).
$$

:::

:::

::: {.pf-step #s1-4}

Thus $\mathcal D$ is a Dynkin system containing $\mathcal C$.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} are the Dynkin-system axioms. The inclusion $\mathcal C\subseteq\mathcal D$ is exactly the hypothesis that $\mu$ and $\nu$ agree on every member of $\mathcal C$.

:::

:::

::: {.pf-step #s1-5}

If a Dynkin system $\mathcal L$ contains an algebra $\mathcal C$, then $\mathcal L$ contains $\sigma(\mathcal C)$.


::: pf-proof

It suffices to prove this for the smallest Dynkin system $\lambda(\mathcal C)$ containing $\mathcal C$.

First fix $C\in\mathcal C$ and define
$$
\mathcal L_C
=\{B\in\lambda(\mathcal C):C\cap B\in\lambda(\mathcal C)\}.
$$
Because $\mathcal C$ is an algebra, it is closed under finite intersections, so $\mathcal C\subseteq\mathcal L_C$. The Dynkin-system axioms show that $\mathcal L_C$ is itself a Dynkin system: it contains $X$ because $C\cap X=C$; it is closed under relative differences of nested sets; and it is closed under countable disjoint unions. By minimality of $\lambda(\mathcal C)$,
$$
\mathcal L_C=\lambda(\mathcal C).
$$
Thus
$$
C\cap B\in\lambda(\mathcal C)
$$
for every $C\in\mathcal C$ and $B\in\lambda(\mathcal C)$.

Now fix $B\in\lambda(\mathcal C)$ and define
$$
\mathcal M_B
=\{A\in\lambda(\mathcal C):A\cap B\in\lambda(\mathcal C)\}.
$$
By the preceding paragraph, $\mathcal C\subseteq\mathcal M_B$. The same Dynkin-system verification shows that $\mathcal M_B$ is a Dynkin system, so again minimality gives
$$
\mathcal M_B=\lambda(\mathcal C).
$$
Hence $\lambda(\mathcal C)$ is closed under finite intersections.

A Dynkin system closed under finite intersections is a $\sigma$-algebra: complements follow from
$$
A^c=X\setminus A,
$$
and an arbitrary countable union can be disjointified using finite intersections and complements, after which the Dynkin disjoint-union axiom applies. Therefore $\lambda(\mathcal C)$ is a $\sigma$-algebra containing $\mathcal C$, so
$$
\sigma(\mathcal C)\subseteq\lambda(\mathcal C).
$$
The reverse inclusion holds because every $\sigma$-algebra is a Dynkin system. Thus
$$
\lambda(\mathcal C)=\sigma(\mathcal C).
$$
Consequently every Dynkin system containing $\mathcal C$ contains $\sigma(\mathcal C)$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\mathcal A\subseteq\mathcal D.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, $\mathcal D$ is a Dynkin system containing the algebra $\mathcal C$. Step [](#s1-5){.pf-ref} therefore gives
$$
\sigma(\mathcal C)\subseteq\mathcal D.
$$
Since $\mathcal A=\sigma(\mathcal C)$, the claim follows.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{\mu(A)=\nu(A)\quad\text{for every }A\in\mathcal A}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, every $A\in\mathcal A$ belongs to $\mathcal D$, whose defining property is equality of the two measures.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
