---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-06
kind: problem
title: Closed-map and open-map criteria for identification maps
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part One, question 6 of the Topology Ph.D. Qualifying Exam
    dated January 17, 2009 in assets/attachments/F08phdtop.pdf. The source has
    a harmless punctuation artifact immediately before the map arrow.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Replaced the older prose-outline solution with a structured proof. For the
    closed-map criterion, use F=pi(pi^{-1}(F)) by surjectivity; the open-map
    criterion is identical with open sets.
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.problem}
Define the term identification map in the category of topological spaces.
Let $\pi:X\to Y$ be a surjective, continuous map of topological spaces.
Suppose that $\pi$ maps closed sets to closed sets.
Show that $\pi$ is an identification map.
What happens if we replace closed sets by open sets?
Justify your answers.
:::

::: {.solution}
A surjection $q:X\to Y$ is an identification (quotient) map if
\[
U\subseteq Y\text{ is open}
\quad\Longleftrightarrow\quad
q^{-1}(U)\text{ is open in }X.
\]
Equivalently, by complements,
\[
F\subseteq Y\text{ is closed}
\quad\Longleftrightarrow\quad
q^{-1}(F)\text{ is closed in }X.
\]

Now let $\pi:X\to Y$ be surjective, continuous, and closed. If $F\subseteq Y$ is closed, then $\pi^{-1}(F)$ is closed by continuity. Conversely, if $\pi^{-1}(F)$ is closed, then
\[
F=\pi(\pi^{-1}(F))
\]
by surjectivity, and the right-hand side is closed because $\pi$ is a closed map. Hence $\pi$ satisfies the quotient criterion.

The same argument works with open sets. If $\pi$ is surjective, continuous, and open, then for any $U\subseteq Y$,
\[
U\text{ open}\implies \pi^{-1}(U)\text{ open}
\]
by continuity, while
\[
\pi^{-1}(U)\text{ open}\implies
U=\pi(\pi^{-1}(U))\text{ open}
\]
by surjectivity and openness. Thus every surjective continuous open map is also an identification map.
::: {.proof}
This is the definition.
Equivalently, by taking complements, a surjective map $q$ is an identification map exactly when
\[
F\text{ is closed in }Y
\quad\Longleftrightarrow\quad
q^{-1}(F)\text{ is closed in }X
\]
for every $F\subseteq Y$.
:::

<1>2. If $\pi:X\to Y$ is surjective, continuous, and closed, then $\pi$ is an identification map.
::: {.proof}
By <1>1 it suffices to characterize closed subsets of $Y$ by their inverse images.

Let $F\subseteq Y$.
If $F$ is closed in $Y$, continuity of $\pi$ gives
\[
\pi^{-1}(F)\text{ closed in }X.
\]

Conversely, suppose $\pi^{-1}(F)$ is closed in $X$.
Because $\pi$ is a closed map,
\[
\pi(\pi^{-1}(F))
\]
is closed in $Y$.
Surjectivity gives
\[
\pi(\pi^{-1}(F))=F.
\]
Therefore $F$ is closed in $Y$.

Hence
\[
F\text{ closed in }Y
\quad\Longleftrightarrow\quad
\pi^{-1}(F)\text{ closed in }X,
\]
so $\pi$ is an identification map.
:::

<1>3. Replacing “closed” by “open” gives the same conclusion: every surjective, continuous, open map is an identification map.
::: {.proof}
Let $U\subseteq Y$.
If $U$ is open in $Y$, continuity gives
\[
\pi^{-1}(U)\text{ open in }X.
\]

Conversely, suppose $\pi^{-1}(U)$ is open in $X$.
Because $\pi$ is an open map,
\[
\pi(\pi^{-1}(U))
\]
is open in $Y$.
Surjectivity gives
\[
\pi(\pi^{-1}(U))=U.
\]
Hence $U$ is open in $Y$.

Thus
\[
U\text{ open in }Y
\quad\Longleftrightarrow\quad
\pi^{-1}(U)\text{ open in }X,
\]
which is the criterion in <1>1.
:::
:::
