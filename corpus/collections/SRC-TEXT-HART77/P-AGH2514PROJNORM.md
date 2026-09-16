---
schema: qual/card@1
id: P-AGH2514PROJNORM
kind: problem
title: Projective normality of the d-uple embedding
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Normality
  - Normal Schemes
  - Veronese Embedding
relations: []
review: draft
---

::: problem
Let $A$ be a ring, and let $X$ be a closed subscheme of $\PP^r_A$.
Define the **homogeneous coordinate ring** $S(X)$ of $X$ for the given embedding to be $A[x_0, \ldots, x_r]/I$, where $I$ is the ideal $\Gamma_*(\mci_X)$ constructed in the proof of (5.16).
Recall that a scheme $X$ is **normal** if its local rings are integrally closed domains.
A closed subscheme $X \subseteq \PP^r_A$ is **projectively normal** for the given embedding if $S(X)$ is an integrally closed domain (cf. (I, Ex. 3.18)).

Now assume $k$ is an algebraically closed field, and $X$ is a connected, normal closed subscheme of $\PP^r_k$.
Show that for some $d > 0$ the $d\dash$uple embedding of $X$ is projectively normal, as follows.

a. Let $S$ be the homogeneous coordinate ring of $X$, and let $S' = \bigoplus_{n \geq 0} \Gamma(X, \OO_X(n))$.
Show that $S$ is a domain, and that $S'$ is its integral closure.
*Hint:* first show $X$ is integral; then regard $S'$ as the global sections of the sheaf of rings $\mcs = \bigoplus_{n \geq 0} \OO_X(n)$ on $X$, and show that $\mcs$ is a sheaf of integrally closed domains.

b. Use (Ex. 5.9) to show that $S_d = S'_d$ for all sufficiently large $d$.

c. Show that $S^{(d)}$ is integrally closed for sufficiently large $d$, and conclude that the $d\dash$uple embedding of $X$ is projectively normal.

d. As a corollary of (a), show that a closed subscheme $X \subseteq \PP^r_A$ is projectively normal if and only if it is normal and for every $n \geq 0$ the natural map $\Gamma(\PP^r, \OO_{\PP^r}(n)) \to \Gamma(X, \OO_X(n))$ is surjective.
:::
