---
schema: qual/card@1
id: E-APRPU
kind: problem
title: Higher-dimensional separation theorems from the no-retraction theorem
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §62 Exercise 6, printed p. 385. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. Checked against Lemma 62.1 (printed p. 381) for the
    extension step, Lemma 62.2 (printed p. 382) for the shape of the Borsuk argument and Theorem 62.3 (printed
    p. 383) for what part (c) must prove. One gap was repaired: the ball B in part (a) must contain the compact
    set A as well as the bounded component C, otherwise the identity on the boundary of B is not available and
    r o G restricted to B is not a retraction. Nothing else needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §62 Exercise 6, printed p. 385. Searched outside the checkout for issue #144 on the orchestrator's
    machine, recorded in tmp/sources/mse-searches-144.md; no thread was saved because no question on the exercise
    was found. The queries were "Borsuk lemma S^n", "invariance of domain no retraction Munkres", "invariance of
    domain Borsuk", the title query "Borsuk lemma", "no compact contractible" and the /similar query of the
    exercise's statement; two questions were read and rejected, 3435898, which is about n = 2 and odd maps, and
    2054009, which gives no proof. Nothing is transcribed. The card's proof is its own, checked on 2026-11-11
    against Lemma 62.1, Lemma 62.2 and Theorem 62.3 as the note above records; it was not re-read in this pass.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose in three headed parts with no `pf` structure. It
    is now a `pf` with ten steps covering (a), (b) and (c), each carrying a `pf-proof`. Cited by
    numbered statement only: Munkres, Topology, §62 Exercise 6, Theorem 26.6 (a continuous injection on
    a compact space is an imbedding), §59 (stereographic projection), Lemma 62.2 and the homotopy
    extension step of the Borsuk lemma in §62, Theorem 25.3 (a component of a locally path connected
    space is open), Theorem 18.3 (the pasting lemma), and the no-retraction hypothesis the exercise
    grants. No retained published set reaches §62, and the card's preamble says so and names the search
    record. Checked: that transporting a nullhomotopy through $f^{-1}$ makes the inclusion
    nullhomotopic, that the components correspond under stereographic projection and that $0$'s
    component is the unbounded one, that $G$ is well defined and continuous on two closed pieces
    agreeing on $A$, that it avoids $0$ on $D$ because $0\in C$, that the radial projection is the
    identity on $\partial B$, that a contraction of $A$ to a point of $A$ stays inside
    $S^n-\{a,b\}$, and that $f(\operatorname{Int}B)$ is a component equal to $V$.
---

::: {.exercise}

Suppose you are given that there is no retraction of $B^n$ onto $S^{n-1}$.

(a) Show the Borsuk lemma holds for $S^n$.

(b) Show that no compact contractible subspace of $S^n$ separates $S^n$.

(c) Suppose you are given also that any subspace of $S^n$ homeomorphic to $S^{n-1}$ separates $S^n$.
Prove the invariance of domain theorem in dimension $n$.
:::

::: {.solution}

No retained published solution of Munkres, *Topology*, §62 Exercise 6 was located: the sets searched are listed in the `COMPLAINTS.md` entry for §51--§63 of `SRC-TEXT-MUN00`, and no retained set reaches §62. The proof is the card's own, checked against the numbered statements it cites, and it takes the no-retraction theorem as the exercise grants it.

::: pf

::: {.pf-step #borsuk-reduce}
(a) It is enough to prove the Borsuk lemma for a compact $A\subseteq S^n-\{a,b\}$ and the inclusion $j:A\hookrightarrow S^n-\{a,b\}$.

::: pf-proof
Let $f:A\to S^n-\{a,b\}$ be continuous and injective with $A$ compact. $A$ is compact and $S^n$ is Hausdorff, so $f$ is a closed map onto its image and hence a homeomorphism onto $f(A)$ (Munkres, Theorem 26.6). Transporting a nullhomotopy of $f$ through the inverse homeomorphism $f(A)\to A$ makes the inclusion $j:f(A)\hookrightarrow S^n-\{a,b\}$ nullhomotopic, and $S^n-f(A)=S^n-f(A)$ does not change, so the two statements are the same.
:::

:::

::: {.pf-step #euclidean-form}
(a) In the coordinates where $S^n-\{b\}$ is $\RR^n$ and $a$ is $0$, the assertion is: if $A\subseteq\RR^n-\{0\}$ is compact and the inclusion $j:A\hookrightarrow\RR^n-\{0\}$ is nullhomotopic, then $0$ lies in the unbounded component of $\RR^n-A$.

::: pf-proof
The stereographic projection $S^n-\{b\}\to\RR^n$ is a homeomorphism (Munkres, §59), and a component of $S^n-A$ corresponds under it to a component of $\RR^n-A$, with the component containing $a$ corresponding to the one containing $0$. The unbounded component of $\RR^n-A$ is the image of the component of $a$, since a component of the complement of a compact set other than the unbounded one is bounded.
:::

:::

::: {.pf-step #extension}
(a) If the component $C$ of $\RR^n-A$ containing $0$ is bounded, then there is a continuous $g:C\cup A\to\RR^n-\{0\}$ with $g\restrict_A=j$.

::: pf-proof
$A$ is compact and $C$ is bounded, so $C\cup A$ lies in a closed ball and is metrizable; $A$ is closed in it. A nullhomotopy of $j$ is a map $A\times[0,1]\to\RR^n-\{0\}$ constant on $A\times\{1\}$, and the homotopy extension property for the closed subset $A$ of the metrizable space $C\cup A$ (Munkres, Lemma 62.2 and the argument of the Borsuk lemma in §62) extends it to $C\cup A\times[0,1]$, giving $g$ as the value at $t=0$.
:::

:::

::: {.pf-step #components-open}
(a) $\RR^n-A$ is locally path connected, so its components are open and closed in $\RR^n-A$ and hence open in $\RR^n$.

::: pf-proof
$\RR^n-A$ is open in $\RR^n$ and $\RR^n$ is locally path connected, so every open subset of it is locally path connected (Munkres, Theorem 25.3 and its remark on open subspaces). The components of a locally path connected space are open, and each is closed as the complement of the union of the others.
:::

:::

::: {.pf-step #patch}
(a) With $D=\RR^n-C$ the formula $G(x)=g(x)$ on $C\cup A$ and $G(x)=x$ on $D$ defines a continuous $G:\RR^n\to\RR^n-\{0\}$ that is the identity on the boundary of a large ball.

::: pf-proof
$C$ is open in $\RR^n$ by step [#components-open]{.pf-ref}, so $D$ is closed and $C\cup A$ is closed, being the complement of the union of the other components, which is open. On the intersection $(C\cup A)\cap D=A$ the two formulas agree, because $g\restrict_A=j$ is the inclusion; so $G$ is well defined, and it is continuous on the two closed pieces (Munkres, Theorem 18.3, the pasting lemma). Its values lie in $\RR^n-\{0\}$ because $g$ takes them there and $D\supseteq\partial B$ for a ball $B$ containing the bounded set $C\cup A$, which does not contain $0$ since $0\in C$. On $\partial B\subseteq D$ the map $G$ is the identity.
:::

:::

::: {.pf-step #retraction}
(a) A retraction $B\to\partial B$ exists, contradicting the hypothesis, so $C$ is unbounded and part (a) holds.

::: pf-proof
Composing $G\restrict_B:B\to\RR^n-\{0\}$ with the radial projection $r:\RR^n-\{0\}\to S^{n-1}$, $r(y)=y/\norm{y}$, gives a continuous map $B\to\partial B$ that is the identity on $\partial B$, since $G$ is the identity there and $r$ fixes unit vectors. That is a retraction of $B$ onto $S^{n-1}$, which the exercise grants does not exist. So $C$ cannot be bounded, and the Euclidean form of step [#euclidean-form]{.pf-ref} gives the Borsuk lemma for $S^n$.
:::

:::

::: {.pf-step #contractible}
(b) No compact contractible subspace of $S^n$ separates $S^n$.

::: pf-proof
Let $A\subseteq S^n$ be compact and contractible and suppose $S^n-A=U\cup V$ is a separation; choose $a\in U$ and $b\in V$. The inclusion $i:A\hookrightarrow S^n-\{a,b\}$ is nullhomotopic, because $A$ is contractible and a contraction of $A$ to a point of $A$ has image in $A\subseteq S^n-\{a,b\}$. The map $i$ is injective and $A$ is compact, so part (a) says $a$ and $b$ lie in the same component of $S^n-A$, contradicting that they lie in different members of a separation. Hence $S^n-A$ is connected.
:::

:::

::: {.pf-step #invariance-setup}
(c) Let $U\subseteq\RR^n$ be open, $f:U\to S^n$ continuous and injective, and $x\in U$; choose a closed ball $B$ with $x\in\operatorname{Int}B\subseteq B\subseteq U$. Then $f(B)$ is compact and contractible and does not separate $S^n$, while $f(\partial B)$ separates $S^n$.

::: pf-proof
Such a ball exists because $U$ is open. $f$ is injective and continuous on the compact $B$, so $f\restrict_B$ is a homeomorphism onto $f(B)$ (Munkres, Theorem 26.6); $B$ is convex, hence contractible, so $f(B)$ is contractible, and it is compact. By part (b) it does not separate $S^n$. The boundary $\partial B$ is homeomorphic to $S^{n-1}$, so $f(\partial B)$ is a subspace of $S^n$ homeomorphic to $S^{n-1}$, and the exercise's additional hypothesis makes it separate $S^n$.
:::

:::

::: {.pf-step #component-equality}
(c) $f(\operatorname{Int}B)$ is a component of $S^n-f(\partial B)$ and equals it.

::: pf-proof
$f(\operatorname{Int}B)$ is connected and disjoint from $f(\partial B)$, since $f$ is injective and $\operatorname{Int}B\cap\partial B=\varnothing$, so it lies in one component $V$ of $S^n-f(\partial B)$. If $y\in V-f(\operatorname{Int}B)$, choose $z$ in another component, which exists because $f(\partial B)$ separates $S^n$. Neither $y$ nor $z$ lies in $f(B)=f(\operatorname{Int}B)\cup f(\partial B)$, because the first term lies in $V$ and the second is removed. But $S^n-f(B)$ is connected, and as a subset of $S^n-f(\partial B)$ it lies in a single component; it contains $y\in V$ and $z\notin V$, a contradiction. Hence $V=f(\operatorname{Int}B)$.
:::

:::

::: {.pf-step #invariance}
(c) $f$ is an open map, hence a homeomorphism onto its image, which is invariance of domain in dimension $n$.

::: pf-proof
Step [#component-equality]{.pf-ref} shows that the image under $f$ of $\operatorname{Int}B$ is open in $S^n$ for the ball $B$ about $x$ of step [#invariance-setup]{.pf-ref}, and $\operatorname{Int}B$ is a neighbourhood of $x$ inside $U$; so $f(U)$ is open in $S^n$ around $f(x)$, for every $x\in U$. A continuous injective open map is a homeomorphism onto its image, so $f:U\to f(U)$ is a homeomorphism and $f(U)$ is open. That is the invariance of domain theorem in dimension $n$ as the exercise states it.
:::

:::

:::

:::
