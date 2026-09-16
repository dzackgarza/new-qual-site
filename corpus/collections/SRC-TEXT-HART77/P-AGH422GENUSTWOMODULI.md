---
schema: qual/card@1
id: P-AGH422GENUSTWOMODULI
kind: problem
title: Curves of genus $2$ correspond to six branch points on $\PP^1$ modulo $\Sigma_6$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Riemann-Hurwitz
  - Hyperelliptic Curves
  - Canonical Divisor
relations: []
review: draft
---

::: {.problem}
Fix an algebraically closed field $k$ of characteristic $\neq 2$.

a. If $X$ is a curve of genus 2 over $k$, the canonical linear system $\abs{K}$ determines a finite morphism $f: X \to \PP^1$ of degree 2 (Ex.
1.7). Show that it is ramified at exactly 6 points, with ramification index 2 at each one.
Note that $f$ is uniquely determined, up to an automorphism of $\PP^1$, so $X$ determines an (unordered) set of 6 points of $\PP^1$, up to an automorphism of $\PP^1$.

b. Conversely, given six distinct elements $\alpha_1, \ldots, \alpha_6 \in k$, let $K$ be the extension of $k(x)$ determined by the equation $z^2=(x-\alpha_1) \cdots (x-\alpha_6)$.
Let $f: X \to \PP^1$ be the corresponding morphism of curves.
Show that $g(X)=2$, the map $f$ is the same as the one determined by the canonical linear system, and $f$ is ramified over the six points $x=\alpha_i$ of $\PP^1$, and nowhere else.
(Cf.
(II, Ex.
6.4).)

c. Using (I, Ex.
6.6), show that if $P_1, P_2, P_3$ are three distinct points of $\PP^1$, then there exists a unique $\varphi \in \Aut \PP^1$ such that $\varphi(P_1)=0, \varphi(P_2)=1, \varphi(P_3)=\infty$.
Thus in (a), if we order the six points of $\PP^1$, and then normalize by sending the first three to $0,1,\infty$ respectively, we may assume that $X$ is ramified over $0,1,\infty, \beta_1, \beta_2, \beta_3$, where $\beta_1, \beta_2, \beta_3$ are three distinct elements of $k$, $\neq 0,1$.

d. Let $\Sigma_6$ be the symmetric group on 6 letters.
Define an action of $\Sigma_6$ on sets of three distinct elements $\beta_1, \beta_2, \beta_3$ of $k$, $\neq 0,1$, as follows: reorder the set $0,1,\infty, \beta_1, \beta_2, \beta_3$ according to a given element $\sigma \in \Sigma_6$, then renormalise as in (c) so that the first three become $0,1,\infty$ again.
Then the last three are the new $\beta_1', \beta_2', \beta_3'$.

e. Summing up, conclude that there is a one-to-one correspondence between the set of isomorphism classes of curves of genus 2 over $k$, and triples of distinct elements $\beta_1, \beta_2, \beta_3$ of $k$, $\neq 0,1$, modulo the action of $\Sigma_6$ described in (d). In particular, there are many non-isomorphic curves of genus 2. We say that curves of genus 2 depend on three parameters, since they correspond to the points of an open subset of $\AA_k^3$ modulo a finite group.
:::
