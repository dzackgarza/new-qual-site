---
schema: qual/card@1
id: P-WESTOP09-I5
kind: problem
title: A Hausdorff continuous image of the unit interval is metrizable
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Suppose $X$ is Hausdorff and there is a continuous surjection
$$
f:I=[0,1]\to X.
$$
This problem proves the metrizability part of the Hahn--Mazurkiewicz theorem.

1. Show that $f$ is a closed map.
2. Show that $X$ is second countable. The source suggests choosing a countable basis $B$ for $I$, taking the set $C$ of finite unions of elements of $B$, and proving that
   $$
   \{X\setminus f(I\setminus U):U\in C\}
   $$
   is a basis for $X$.
3. Prove that $X$ is metrizable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The map $f:I\to X$ is closed.


::: pf-proof

Let $F\subseteq I$ be closed. Since $I$ is compact, $F$ is compact. Its
continuous image $f(F)$ is compact, and compact subsets of the Hausdorff space
$X$ are closed. Hence $f$ sends closed sets to closed sets.

:::

:::

::: {.pf-step #s1-2}

Let $\mathcal B$ be a countable basis for $I$, and let $\mathcal C$ be
the collection of all finite unions of elements of $\mathcal B$. Then
$\mathcal C$ is countable.


::: pf-proof

For each $n\ge1$, the set of unions of exactly $n$ members of the countable
set $\mathcal B$ is countable. The collection $\mathcal C$ is the countable
union of these countable sets, together with the empty union, so it is
countable.

:::

:::

::: {.pf-step #s1-3}

For $U\in\mathcal C$, define
$$
V_U=X\setminus f(I\setminus U).
$$
Then $V_U$ is open in $X$, and
$$
y\in V_U
\quad\Longleftrightarrow\quad
f^{-1}(y)\subseteq U.
$$


::: pf-proof

Since $U$ is open in $I$, the set $I\setminus U$ is closed. Step [](#s1-1){.pf-ref} implies
that $f(I\setminus U)$ is closed, so $V_U$ is open.

Moreover,
$$
y\notin f(I\setminus U)
$$
means precisely that no point of the fiber $f^{-1}(y)$ lies outside $U$,
which is equivalent to $f^{-1}(y)\subseteq U$.

:::

:::

::: {.pf-step #s1-4}

The countable family
$$
\mathcal V=\{V_U:U\in\mathcal C\}
$$
is a basis for $X$.


::: pf-proof

Let $O\subseteq X$ be open and let $x\in O$. The fiber
$$
K=f^{-1}(x)
$$
is closed in the compact space $I$, hence compact. Since
$$
K\subseteq f^{-1}(O)
$$
and $f^{-1}(O)$ is open, for every $t\in K$ choose
$B_t\in\mathcal B$ with
$$
t\in B_t\subseteq f^{-1}(O).
$$
Compactness of $K$ gives finitely many
$$
B_{t_1},\dots,B_{t_n}
$$
covering $K$. Set
$$
U=B_{t_1}\cup\cdots\cup B_{t_n}\in\mathcal C.
$$
Then
$$
f^{-1}(x)\subseteq U\subseteq f^{-1}(O).
$$
By step [](#s1-3){.pf-ref}, $x\in V_U$. If $y\in V_U$, then
$f^{-1}(y)\subseteq U\subseteq f^{-1}(O)$. Since $f$ is surjective,
$f^{-1}(y)$ is nonempty, so choosing $t\in f^{-1}(y)$ gives
$t\in f^{-1}(O)$ and therefore $y=f(t)\in O$. Thus
$$
x\in V_U\subseteq O.
$$
Hence $\mathcal V$ is a basis. It is countable by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The space $X$ is metrizable.


::: pf-proof

The space $I$ is compact, so its continuous image
$$
X=f(I)
$$
is compact. By hypothesis $X$ is Hausdorff. Every compact Hausdorff space is
regular, and step [](#s1-4){.pf-ref} shows that $X$ is second countable. The Urysohn
metrization theorem therefore implies that
$$
\boxed{X\text{ is metrizable}}.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part 1, step [](#s1-4){.pf-ref} proves part 2, and step [](#s1-5){.pf-ref} proves part 3.

:::

:::

:::
