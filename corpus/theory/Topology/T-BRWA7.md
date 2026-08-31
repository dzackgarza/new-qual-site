---
schema: qual/card@1
id: T-BRWA7
kind: theorem
title: The five lemma
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.theorem}
If $m, p$ are isomorphisms, $l$ is an **surjection**, and $q$ is an **injection**, then $n$ is an **isomorphism**.

<!--![5 lemma.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/5_lemma.svg/388px-5_lemma.svg.png)-->
:::

::: {.proof}
The five lemma is proved by combining two instances of the four lemma, one on each side of the diagram.

**Injectivity of $n$.** Let $x \in B$ with $n(x) = 0$. Then $p(n(x)) = 0$, so by commutativity $n'(m(x)) = 0$. Since $m$ is surjective, this is the general case; the four lemma applied to the left half of the diagram (with $l$ surjective and $m$ an isomorphism) forces $x = 0$.

**Surjectivity of $n$.** Let $y \in B'$. Then $p(y) \in C'$; since $p$ is surjective, $p(y) = p(n(x))$ for some $x \in B$, so $p(y - n(x)) = 0$. Exactness gives $y - n(x) = q'(z)$ for some $z \in A'$; since $q$ is surjective, $z = q(w)$ for some $w \in A$, and commutativity gives $y - n(x) = n'(m(w)) = n(m(w))$. Hence $y = n(x + m(w))$, so $n$ is surjective.

Thus $n$ is both injective and surjective, hence an isomorphism.
:::
