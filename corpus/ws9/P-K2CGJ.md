---
schema: qual/card@1
id: P-K2CGJ
kind: problem
title: Conjugacy class size equals the index of the centralizer; restriction to a subgroup of index $2$
classification:
  areas:
  - algebra
  topics:
  - conjugacy
  - centralizers-and-normalizers
  - class-equation
relations: []
review: draft
solved: false
---

::: problem
Let $G$ be a finite group. For any $x \in G$
$$Z_G(x) = \{g \in G : gxg^{-1} = x\}$$
is the centralizer of $x$ in $G$ and
$$x^G = \{gxg^{-1} : g \in G\}$$
is the conjugacy class of $x$ in $G$.

a. Show that $|x^G| = [G : Z_G(x)]$.

b. If $H \le G$ and $x \in H$, prove that $Z_H(x) = H \cap Z_G(x)$.

c. If $H$ is a subgroup of index 2 in $G$ and $x \in H$, prove that either $|x^H| = |x^G|$ or $|x^H| = \frac{1}{2}|x^G|$.
:::
