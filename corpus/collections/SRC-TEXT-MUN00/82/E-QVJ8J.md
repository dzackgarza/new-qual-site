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
  date: 2026-11-15
  note: >-
    Munkres §82 Supplementary Exercise 2, printed pp. 499--500. Searched outside the checkout for issue #146;
    the record is tmp/sources/mse-searches-146.md. No source was saved. The queries were the Stack Exchange
    advanced search "regular countable basis semilocally simply connected fundamental group countable" (no
    hits) and the similar-question search from "Fundamental group of second countable semilocally simply
    connected space is countable" (15 items). The thread 1169500, whose answer 1186182 proves the compact
    finite-generation theorem, was read and rejected for this card: its hypothesis is compactness, not a
    countable basis with regularity, and it concludes finite generation. Thread 4813468 treats the manifold
    case and proves nothing. The card keeps its own proof, which is the printed outline with a countable
    cover from the regular second-countable hypothesis.
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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose; the argument and its citations are
    unchanged. Added as its own step the passage from the pairwise-union property of the refinement
    to the same property for the members of B, which the prose asserted in a clause: two path
    components of members of A' that meet force those members to meet, so both lie in one member
    of A. Checked in (a) that n is chosen below both the Lebesgue number and the continuity
    threshold, so the last interval lies in B_0 by construction rather than by refining a
    subdivision, and that consecutive members meet at f(t_{i-1}) for i >= 2 and at x_0 for i = 1.
    Checked in (c) that the product telescopes through the classes of the alpha_i and that
    [alpha_0] and [alpha_n] are the class of the constant path, and that [f] is the product of the
    [f_i] by additivity of path homotopy (Theorem 51.2). The countability of the set of finite
    words is now cited through the section's own theorems, a finite product of countable sets
    (Theorem 7.6, printed p. 49) and a countable union (Theorem 7.5, printed p. 48), rather than by
    a single number. What was not verified: the search record for published solutions, which the
    events above carry.
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
The proof is the card's own, following the printed outline: no complete published solution of Munkres §82 Supplementary Exercise 2  was located, and the searches are recorded in the audit above. The numbered results cited are the Urysohn metrization theorem (Theorem 34.1), the Lebesgue number lemma (Lemma 27.5), the algebra of path-homotopy classes (Theorem 51.2), and the countability theorems of §7 (Theorem 7.5, and Theorem 7.6); the definition of semilocal simple connectedness is on printed p. 494.

Throughout, $\mathcal{A}$ is the cover of $X$ by path-connected open sets with $\pi_{1}(A,a)\to\pi_{1}(X,a)$ trivial, $\mathcal{B}$ is the countable cover of the statement satisfying the conditions of [[E-8Q9TN]], $p(B)\in B$ is the chosen point, $g(B,B')$ is the select path in $B\cup B'$, $B_{0}\in\mathcal{B}$ is fixed and $x_{0}=p(B_{0})$.

::: pf

::: {.pf-step #covera}
A cover $\mathcal{A}$ of $X$ by path-connected open sets with $\pi_{1}(A,a)\to\pi_{1}(X,a)$ trivial for every $a\in A$ exists.

::: pf-proof
For $x\in X$ let $N$ be a neighbourhood of $x$ such that every loop in $N$ at $x$ is nullhomotopic in $X$, which semilocal simple connectedness supplies (printed p. 494). Local path connectedness gives a path-connected open neighbourhood $U$ of $x$ with $U\subset N$, and then any loop in $U$ at any of its points is a loop in $N$ at that point, hence nullhomotopic in $X$; so $\pi_{1}(U,a)\to\pi_{1}(X,a)$ is trivial for every $a\in U$. The sets $U$ so obtained cover $X$.
:::
:::

::: {.pf-step #coverb}
There is a countable open cover $\mathcal{B}$ of $X$ by nonempty path-connected sets such that $B,B'\in\mathcal{B}$ with $B\cap B'\neq\varnothing$ implies $B\cup B'\subset A$ for some $A\in\mathcal{A}$.

::: pf-proof
$X$ is regular with a countable basis, so it is metrizable by the Urysohn metrization theorem (Theorem 34.1). By [[E-8Q9TN]] (a) the cover $\mathcal{A}$ of the metrizable space $X$ has an open refinement $\mathcal{A}'$ with the pairwise-union property. The path components of members of $\mathcal{A}'$ are open, because $X$ is locally path connected, and path connected; they refine $\mathcal{A}$, so they have the trivial-$\pi_{1}$ property, and they inherit the pairwise-union property. Select, for each element $M$ of the fixed countable basis of $X$ that is contained in one of these components, one such component $C_{M}$. Every point $x$ lies in some member of $\mathcal{A}'$, hence in one of its path components $C$, and $C$ is open, so the basis contains $M$ with $x\in M\subset C$; thus the selected components cover $X$, and there are countably many of them. They are the members of $\mathcal{B}$.
:::
:::

::: {.pf-step #pairwise}
If $B,B'\in\mathcal{B}$ meet, then $B\cup B'\subset A$ for some $A\in\mathcal{A}$.

::: pf-proof
Both are path components of members of $\mathcal{A}'$, and $\mathcal{A}'$ has the pairwise-union property, so two of its members that meet have their union inside a member $\bar A$ of $\mathcal{A}$; a component of one of them meeting a component of the other forces the two members to meet, so both components lie in the same member $A$ of $\mathcal{A}$.
:::
:::

::: {.pf-step #subdivision}
(a) There is a subdivision $0=t_{0}<\cdots<t_{n}=1$ of $[0,1]$ with $f([t_{n-1},t_{n}])\subset B_{0}$ and $f([t_{i-1},t_{i}])\subset B_{i}$ for $i=1,\ldots,n-1$, with $B_{n}=B_{0}$.

::: pf-proof
The sets $f^{-1}(B)$ for $B\in\mathcal{B}$ are open and cover the compact metric space $[0,1]$, so the Lebesgue number lemma (Lemma 27.5) gives $\delta>0$ such that every subset of diameter less than $\delta$ lies in one of them. Continuity of $f$ at $1$ and $f(1)=x_{0}\in B_{0}$ with $B_{0}$ open give $\eta>0$ with $f([1-\eta,1])\subset B_{0}$. Choose $n$ with $1/n<\min(\delta,\eta)$ and $t_{i}=i/n$. Each $[t_{i-1},t_{i}]$ has diameter $1/n<\delta$, so $f([t_{i-1},t_{i}])$ has diameter less than $\delta$ and lies in some $B_{i}\in\mathcal{B}$; the last interval satisfies $[t_{n-1},t_{n}]\subset[1-\eta,1]$, so $B_{n}=B_{0}$ serves. Consecutive members meet: for $i\geq2$ both $B_{i-1}$ and $B_{i}$ contain $f(t_{i-1})$, and $B_{0}$ and $B_{1}$ both contain $f(0)=x_{0}=f(1)$.
:::
:::

::: {.pf-step #homotopy}
(b) $[f_{i}]*[\alpha_{i}]=[\alpha_{i-1}]*[g_{i}]$ for $i=1,\ldots,n$.

::: pf-proof
The paths $f_{i}*\alpha_{i}$ and $\alpha_{i-1}*g_{i}$ have the same initial point $f(t_{i-1})$ and the same terminal point $p(B_{i})$. Their concatenation with one of them reversed is a loop lying in $B_{i-1}\cup B_{i}$, since $f_{i}$ takes values in $B_{i-1}$, $\alpha_{i-1}$ in $B_{i-1}$, $\alpha_{i}$ in $B_{i}$ and $g_{i}$ in $B_{i-1}\cup B_{i}$. By step [](#pairwise){.pf-ref} that union lies in some $A\in\mathcal{A}$, so the loop is nullhomotopic in $X$ because the inclusion-induced map $\pi_{1}(A)\to\pi_{1}(X)$ is trivial. Theorem 51.2  now gives $[f_{i}]*[\alpha_{i}]=[\alpha_{i-1}]*[g_{i}]$.
:::
:::

::: {.pf-step #countable}
(c) $[f]=[g_{1}]*\cdots*[g_{n}]$, so $\pi_{1}(X,x_{0})$ is countable.

::: pf-proof
Rearranging part (b) gives $[f_{i}]=[\alpha_{i-1}]*[g_{i}]*[\alpha_{i}]^{-1}$; multiplying these for $i=1,\ldots,n$ cancels the intermediate $[\alpha_{i}]$, and $[\alpha_{0}]$ and $[\alpha_{n}]$ are the class of the constant path at $x_{0}$, so $[f_{1}]*\cdots*[f_{n}]=[g_{1}]*\cdots*[g_{n}]$. By part (a), $[f]=[f_{1}]*\cdots*[f_{n}]$ (Theorem 51.2 again). Since $\mathcal{B}$ is countable, there are countably many select paths, and the set of finite words in a countable alphabet is countable, the words of each length forming a finite product of countable sets and the lengths a countable family (Theorem 7.6, and Theorem 7.5); every element of $\pi_{1}(X,x_{0})$ is $[f]$ for a loop $f$ and so is one of these countably many products.
:::
:::
:::

:::
