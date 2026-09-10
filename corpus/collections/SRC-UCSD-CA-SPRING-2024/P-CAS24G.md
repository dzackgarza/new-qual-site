---
schema: qual/card@1
id: P-CAS24G
kind: problem
title: Polynomial of an isolated singularity preserves singularity type
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Holomorphic Functions
relations: []
review: draft
---

::: problem
Let $U \subset \mathbb{C}$ be an open set.
Let $f : U \setminus \{a\} \to \mathbb{C}$ be a holomorphic function with an isolated singularity at $a \in U$.

Let $P$ be a non-constant polynomial.
Let $g : U \setminus \{a\} \to \mathbb{C}$ be given by
\[
g(z) = P(f(z)).
\]

Show that:

(i) If $f$ has a removable singularity at $a$, then $g$ has a removable singularity at $a$.

(ii) If $f$ has a pole at $a$, then $g$ has a pole at $a$.

(iii) If $f$ has an essential singularity at $a$, then $g$ has an essential singularity at $a$.
:::

::: solution
Write
\[
P(w)=c_d w^d+\cdots+c_0,
\qquad c_d\ne0,
\quad d\ge1.
\]

(i) If $f$ has a removable singularity at $a$, it extends holomorphically
across $a$. Then $P\circ f$ also extends holomorphically, so $g$ is removable.

(ii) If $f$ has a pole at $a$, then $|f(z)|\to\infty$ as $z\to a$. Since a
nonconstant polynomial satisfies $|P(w)|\to\infty$ as $|w|\to\infty$, we get
\[
|g(z)|=|P(f(z))|\to\infty.
\]
Thus $g$ has a pole at $a$.

(iii) Suppose $f$ is essential at $a$. If $g=P(f)$ were removable, then $g$
would be bounded near $a$. Polynomial growth implies that the set
\[
\{w:|P(w)|\le M\}
\]
is bounded for every $M$, so $f$ would be bounded near $a$ and hence
removable, a contradiction. If $g$ had a pole, then $|P(f(z))|\to\infty$;
again polynomial growth forces $|f(z)|\to\infty$, so $f$ would have a pole,
also a contradiction. Therefore $g$ is neither removable nor a pole, and its
isolated singularity at $a$ is essential.
:::
