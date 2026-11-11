---
schema: qual/card@1
id: E-QVJ8J
kind: problem
title: Countability of the fundamental group under countable basis and regularity
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 82 Supplementary Exercise 2, printed pp. 499-500. Countability of pi_1 for a regular space with a countable basis, path connected, locally path connected and semilocally simply connected, by the cover-by-open-sets argument of the printed proof. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: part (a) said "refine the subdivision near 1 so that the last interval maps into B_0", which is a deformation of a subdivision already chosen and is not what the argument needs; the proof now chooses the mesh of the subdivision smaller than both a Lebesgue number (Lemma 27.5, printed p. 175) and a number eta witnessing continuity of f at 1 with values in the open set B_0, so the last interval lies in B_0 by construction. Corrected: the construction of the countable cover B was described as taking "a countable subcover" of the path components of a cover, which is not immediate because those components need not be pairwise disjoint; the proof now selects, for each element of the countable basis lying in one of the components, that component, and obtains a countable subfamily directly. Corrected: the conclusion that consecutive B_{i-1} and B_i intersect was asserted "after the evident index shift"; the intersection is now exhibited, at the common point f(t_{i-1}) for i >= 2 and at x_0 for i = 1. Citations added: the Urysohn metrization theorem Theorem 34.1 (printed p. 215), the Definition of semilocal simple connectness (printed p. 494), and Theorem 51.2 (printed p. 326) for the algebra of path-homotopy classes used in parts (b) and (c). What the certificate does not cover: the printed hypothesis of regularity with a countable basis is used only to make X metrizable; nothing else in the proof needs it.
---

::: {.exercise}

Prove the following.

Theorem.
Let $X$ be a space that is path connected, locally path connected, and semilocally simply connected.
If $X$ is regular with a countable basis, then $\pi_1(X, x_0)$ is countable.

Let $\mathcal{A}$ be a covering of $X$ by path-connected open sets such that for each $A \in \mathcal{A}$ and each $a \in A$, the homomorphism $\pi_1(A, a) \to \pi_1(X, a)$ induced by inclusion is trivial.
Let $\mathcal{B}$ be a countable open covering of $X$ by nonempty path-connected sets that satisfies the conditions of [[E-8Q9TN]]. Choose a point $p(B) \in B$ for each $B \in \mathcal{B}$.
For each pair $B$, $B'$ of elements of $\mathcal{B}$ for which $B \cap B' \neq \varnothing$, choose a path $g(B, B')$ in $B \cup B'$ from $p(B)$ to $p(B')$.
We call the path $g(B, B')$ a select path.

Let $B_0$ be a fixed element of $\mathcal{B}$; let $x_0 = p(B_0)$.
Show that if $f$ is a loop in $X$ based at $x_0$, then $f$ is path homotopic to a product of select paths, as follows:

(a) Show that there is a subdivision

$$
0 = t_0 < \dots < t_n = 1
$$

of $[0, 1]$ such that $f$ maps $[t_{n-1}, t_n]$ into $B_0$, and for each $i = 1, \ldots, n-1$, $f$ maps $[t_{i-1}, t_i]$ into an element $B_i$ of $\mathcal{B}$.
Set $B_n = B_0$.

(b) Let $f_i$ be the positive linear map of $[0, 1]$ onto $[t_{i-1}, t_i]$ followed by $f$.
Let $g_i = g(B_{i-1}, B_i)$.
Choose a path $\alpha_i$ in $B_i$ from $f(t_i)$ to $p(B_i)$; if $i = 0$ or $n$, let $\alpha_i$ be the constant path at $x_0$.
Show that

$$
[f_i] * [\alpha_i] = [\alpha_{i-1}] * [g_i].
$$

(c) Show that $[f] = [g_1] * \dots * [g_n]$.

:::

::: {.solution}

First, $\mathcal{A}$ exists: for each $x \in X$ choose a path-connected open neighbourhood $U$ of $x$ such that $\pi_1(U,x)\to\pi_1(X,x)$ is trivial, which is the definition of semilocal simple connectedness (printed p. 494) together with local path connectedness.

Second, $\mathcal{B}$ exists. Since $X$ is regular with a countable basis, it is metrizable by the Urysohn metrization theorem (Theorem 34.1, printed p. 215), so by [[E-8Q9TN]] (a) the cover $\mathcal{A}$ has an open refinement $\mathcal{A}'$ with the pairwise-union property. The path components of the members of $\mathcal{A}'$ are open, because $X$ is locally path connected; they are path connected, they refine $\mathcal{A}$ and they inherit the pairwise-union property. Take one such component for each element of the countable basis that is contained in a component, and note that every point $x$ has a basis element $M$ with $x\in M\subseteq C$, where $C$ is the component containing $x$ of a member of $\mathcal{A}'$; these components are then a countable subfamily still covering $X$, and they form $\mathcal{B}$.

Thus whenever $B,B'\in\mathcal B$ intersect, there is $A\in\mathcal A$ with
$$
B\cup B'\subset A,
$$
and every loop in $A$ maps trivially in $\pi_1(X)$.

(a) The sets $f^{-1}(B)$, $B\in\mathcal B$, form an open cover of the compact interval $[0,1]$, which is a metric space in the euclidean metric; let $\delta>0$ be a Lebesgue number for this cover (Lemma 27.5, printed p. 175). Since $f$ is continuous at $1$ and $f(1)=x_0\in B_0$ with $B_0$ open, there is $\eta>0$ with $f([1-\eta,1])\subseteq B_0$. Choose $n$ with $1/n<\min(\delta,\eta)$ and set $t_i=i/n$. Then each $f([t_{i-1},t_i])$ has diameter less than $\delta$ and so lies in some $B_i\in\mathcal B$; the last interval lies in $B_0$, so we set $B_n=B_0$. Consecutive sets meet: $B_{i-1}\cap B_i\ne\varnothing$ because both contain $f(t_{i-1})$ when $i\ge 2$, and $B_0\cap B_1\ne\varnothing$ because both contain $f(0)=x_0=f(1)$.

(b) The paths
$$
f_i*\alpha_i
\qquad\text{and}\qquad
\alpha_{i-1}*g_i
$$
have the same initial point $f(t_{i-1})$ and the same terminal point $p(B_i)$. Their concatenation with one reversed is a loop contained in
$$
B_{i-1}\cup B_i,
$$
because $f_i$ and $\alpha_{i-1}$ lie in $B_{i-1}$, and $\alpha_i$ and $g_i$ lie in $B_i$. Since $B_{i-1}\cap B_i\ne\varnothing$, this union lies in some $A\in\mathcal A$. The inclusion-induced map $\pi_1(A)\to\pi_1(X)$ is trivial, so the loop is nullhomotopic in $X$. Hence the two paths are homotopic rel endpoints:
$$
[f_i]*[\alpha_i]=[\alpha_{i-1}]*[g_i],
$$
by Theorem 51.2 (printed p. 326), which gives cancellation of path-homotopy classes.

(c) Rearranging the equality from (b),
$$
[f_i]=[\alpha_{i-1}]*[g_i]*[\alpha_i]^{-1}.
$$
Multiplying these identities for $i=1,\dots,n$, all intermediate $\alpha_i$'s cancel. Since $\alpha_0$ and $\alpha_n$ are constant at $x_0$,
$$
[f]=[f_1]*\cdots*[f_n]
=[g_1]*\cdots*[g_n].
$$
There are only countably many select paths because $\mathcal B$ is countable, and the set of all finite words in a countable alphabet is countable. Every element of $\pi_1(X,x_0)$ is represented by such a finite product. Therefore
$$
\boxed{\pi_1(X,x_0)\text{ is countable}.}
$$

:::
