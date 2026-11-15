---
schema: qual/card@1
id: E-26ELV
kind: problem
title: Second countable locally compact Hausdorff spaces of finite dimension imbed as closed subspaces
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source writes f(x)>n for a vector-valued map. Escape to infinity means the norm of f(x) exceeds n outside a compact set.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked line by line against Munkres, Topology (2000), §50 Exercise 6, printed pp. 315-316, with Urysohn's
    lemma (Theorem 33.1), the Tietze extension theorem (Theorem 35.1), Theorem 48.2 and Lemma 48.4 for the Baire
    arguments, Theorem 26.5 and Theorem 26.6 for the passage to one-point compactifications, and the density step
    of the proof of Theorem 50.5 for part (d). Each part is correct as written: (a) a perturbation of size less
    than 1 preserves going to infinity; (b) the extension to one-point compactifications is continuous at
    infinity by the very definition, and an injective continuous map of a compact Hausdorff space into a
    Hausdorff space is an imbedding whose image is closed; (c) the set of pairs at distance at least eps is
    compact, and simple convergence controls the distance between two images; (d) is the Tietze device of the
    exercise's hint; (e) needs a locally finite sum of the functions 1 - phi_n, which the card obtains from the
    nesting C_n inside the interior of C_{n+1}; (f) closes with Baire and the observation that two distinct
    points lie in some C_n at distance at least 1/n. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Two parts of Munkres §50 Exercise 6 (printed pp. 315--316) are
    asked on Math StackExchange, and both answers agree with the card. Part (b) is question 1626767, "Exercise
    6 in section 50 in Topology textbook of Munkres" (2016-01-25), whose answer 1627645 by Birkhoff
    (2016-01-26), kept at tmp/sources/mse-1626767-munkres-50-6a.md, extends $f$ by $\hat f(\infty)=\infty$ and
    gets closedness of the image from a sequence argument inside the compactification; the card's step
    [](#s2) instead uses that $\hat f$ is an injective continuous map of the compact Hausdorff $X^*$ into a
    Hausdorff space, hence an embedding with compact, therefore closed, image, and then
    $f(X)=\hat f(X^*)\cap\RR^N$, which needs no sequence. Part (d) is question 1650910, "Another question from
    Exercise 6d in section 50 in Munkres' textbook in Topology" (2016-02-11), whose answer 2825193 by Will
    Fisher (2018-06-19), kept at tmp/sources/mse-1650910-munkres-50-6d.md, proves the density by reducing to
    the compact metrizable case: $C$ is compact Hausdorff, second countable and of dimension at most $m$, so
    it is metrizable by the Urysohn metrization theorem and the density lemma of the imbedding theorem applies
    to $\mathcal{C}(C,\RR^{2m+1})$; the card's step [](#s4) is the same reduction followed by the Tietze device
    of the exercise's hint. Neither answer touches (a), (c), (e) or (f), which remain the card's. The AoPS
    post *Topology by Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630)
    answers §50 with its formulas lost; Murayama and dbFin have no Chapter 8. Nothing needed correction.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144 against §50 Exercise 6 as printed on pp. 315--316. Part (e) prints "Show there exists
    a map f: X -> R such that f(x) -> infinity as x -> infinity", in R and not in R^N, and the card stored R^N;
    the printed target is restored. The consequence is carried into (f), whose Baire set is about maps into
    R^N: the card now forms f_1(x) = (psi(x), 0, ..., 0) in C(X, R^N) from part (e)'s real-valued psi and runs
    (a) on f_1, which is what the printed (f) does with the C_n of (e). What was not changed: the printed
    sentence "f(x) > n" is about a vector-valued map and stays as norm(f(x)) > n, as the 2026-10-31 event
    records.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144; four arguments that the card asserted were supplied. (1) Part (e) now proves the
    exhaustion X = union C_n with C_n compact and C_n inside Int C_{n+1} that the hint asks for: the basis
    elements with compact closure form a countable basis (Theorem 29.2, printed p. 185), and the compact C_n
    are built from them by finite subcovers, a set once covered remaining covered. (2) psi = sum (1 - phi_n) is
    shown continuous rather than assumed: the Int C_k cover X, and on Int C_k every summand with n >= k
    vanishes, so psi is a finite sum there. (3) The bound psi(x) >= k-1 for x outside C_k is now derived rather
    than asserted, from Int C_{n+1} contained in C_k for n <= k-1. (4) Part (b) now says of continuity at
    points of X what it said only of infinity: X is open in X^*, and f^* agrees with f there. In part (c) the
    equivalence defining membership in U_epsilon(C) is justified through the maximum of the distance on the
    compact set {f(x) = f(y)} contained in C x C, which is where Delta(f|C), a supremum of fibre diameters
    (printed p. 311), is attained. What was not re-read: parts (a) and (d), whose arguments the earlier events
    checked, and the correctness of the density lemma of the imbedding theorem quoted in (d).
---

::: {.exercise}

Prove the following.

Theorem.
Let $X$ be a locally compact Hausdorff space with a countable basis, such that every compact subspace of $X$ has topological dimension at most $m$.
Then $X$ is homeomorphic to a closed subspace of $\RR^{2m+1}$.

If $f: X \to \RR^N$ is a continuous map, we say $f(x) \to \infty$ as $x \to \infty$ if given $n$, there is a compact subspace $C$ of $X$ such that $\norm{f(x)} > n$ for $x \in X - C$.

(a) Let $\bar{\rho}$ be the uniform metric on $\mathcal{C}(X, \RR^N)$.
Show that if $f(x) \to \infty$ as $x \to \infty$ and $\bar{\rho}(f, g) < 1$, then $g(x) \to \infty$ as $x \to \infty$.

(b) Show that if $f(x) \to \infty$ as $x \to \infty$, then $f$ extends to a continuous map of one-point compactifications.
Conclude that if $f$ is injective as well, then $f$ is a homeomorphism of $X$ with a closed subspace of $\RR^N$.

(c) Given $f: X \to \RR^N$ and given a compact subspace $C$ of $X$, let

$$
U_\epsilon(C) = \theset{f \mid \Delta(f \mid C) < \epsilon}.
$$

Show that $U_\epsilon(C)$ is open in $\mathcal{C}(X, \RR^N)$.

(d) Show that if $N = 2m + 1$, then $U_\epsilon(C)$ is dense in $\mathcal{C}(X, \RR^N)$.
[Hint: Given $f$ and given $\epsilon, \delta > 0$, choose $g: C \to \RR^N$ so that $d(f(x), g(x)) < \delta$ for $x \in C$, and $\Delta(g) < \epsilon$. Extend $f - g$ to $h: X \to [-\delta, \delta]^N$ using the Tietze theorem.]

(e) Show there exists a map $f: X \to \RR$ such that $f(x) \to \infty$ as $x \to \infty$.
[Hint: Write $X$ as the union of compact subspaces $C_n$ such that $C_n \subset \operatorname{Int} C_{n+1}$ for each $n$.]

(f) Let $C_n$ be as in (e). Use the fact that $\bigcap U_{1/n}(C_n)$ is dense in $\mathcal{C}(X, \RR^N)$ to complete the proof.
:::

::: {.solution}
The locally compact second-countable Hausdorff space $X$ is metrizable by the Urysohn metrization theorem. Fix a compatible metric $d$ on $X$. Use the maximum norm on $\RR^N$ and its uniform metric on the function space.

::: pf

::: {.pf-step #s1}
Part (a): Perturbation of proper maps.

::: pf-proof

::: pf-step
Let $n \in \ZZ_+$.
Since $f(x) \to \infty$, there exists a compact $C \subset X$ such that $\norm{f(x)} > n + 1$ for all $x \in X \setminus C$.
:::

::: pf-step
Since $\bar{\rho}(f, g) < 1$, $\norm{f(x) - g(x)} \le 1$ for all $x \in X$.
:::

::: pf-step
For any $x \in X \setminus C$: $$\norm{g(x)} \ge \norm{f(x)} - \norm{f(x) - g(x)} > (n + 1) - 1 = n.$$
:::

::: pf-step
Hence $g(x) \to \infty$ as $x \to \infty$.
:::

:::

:::

::: {.pf-step #s2}
Part (b): Continuous extension to one-point compactifications and closed embeddings.

::: pf-proof

::: pf-step
Let $X^* = X \cup \{\infty_X\}$ and $(\RR^N)^* = \RR^N \cup \{\infty\}$ be the one-point compactifications.
:::

::: pf-step
Define $f^*: X^* \to (\RR^N)^*$ by $f^*(x) = f(x)$ for $x \in X$ and $f^*(\infty_X) = \infty$.
:::

::: pf-step
$f^*$ is continuous at every point of $X$.

::: pf-proof
$X$ is open in $X^*$, and on the open neighbourhood $X$ of a point $x$ the restriction $f^*\restrict_X$ is $f$, which is continuous. Continuity is a local property, so $f^*$ is continuous at $x$.
:::

:::

::: pf-step
$f^*$ is continuous at $\infty_X$.

::: pf-proof
Every neighbourhood $V$ of $\infty$ in $(\RR^N)^*$ contains $(\RR^N \setminus \overline{B}_n) \cup \{\infty\}$ for some $n$. Since $f(x) \to \infty$, there is a compact $C \subset X$ with $f(X \setminus C) \subseteq \RR^N \setminus \overline{B}_n$, so $(f^*)^{-1}(V) \supseteq (X \setminus C) \cup \{\infty_X\}$, which is open in $X^*$. Hence $f^*$ is continuous at $\infty_X$, and with the preceding step, continuous.
:::

:::

::: pf-step
If $f$ is injective, then $f^*$ is an injective continuous map from the compact Hausdorff space $X^*$ into the Hausdorff space $(\RR^N)^*$, hence a topological embedding.
:::

::: pf-step
The image $f^*(X^*)$ is compact, hence closed in $(\RR^N)^*$.
:::

::: pf-step
Restricting to $X$, $f(X) = f^*(X^*) \cap \RR^N$ is closed in $\RR^N$, and $f: X \to f(X)$ is a homeomorphism.
:::

:::

:::

::: {.pf-step #s3}
Part (c): Openness of $U_\varepsilon(C)$.

::: pf-proof

::: pf-step
The condition $\Delta(f\restrict_C) < \varepsilon$ is equivalent to saying that if $x_1, x_2 \in C$ with $d(x_1, x_2) \ge \varepsilon$, then $f(x_1) \neq f(x_2)$.

::: pf-proof
By the definition on printed p. 311,
$$\Delta(f\restrict_C)=\sup\theset{\operatorname{diam}(f\restrict_C)^{-1}(\{z\}) \mid z\in f(C)} .$$
The set $P=\theset{(x_1,x_2)\in C\times C : f(x_1)=f(x_2)}$ is the preimage of the diagonal of $\RR^N\times\RR^N$ under the continuous map $(f\restrict_C)\times(f\restrict_C)$, so it is closed in the compact space $C\times C$ and hence compact; $d$ is continuous there, so $D=\max_{(x_1,x_2)\in P}d(x_1,x_2)$ is attained, and $D=\Delta(f\restrict_C)$: two points with the same image lie in one fibre, and two points of one fibre are such a pair. So the supremum defining $\Delta(f\restrict_C)$ is a maximum, and $\Delta(f\restrict_C)<\varepsilon$ says exactly that no point of $P$ has $d(x_1,x_2)\ge\varepsilon$, which is the stated condition.
:::

:::

::: pf-step
The set $S = \{(x_1, x_2) \in C \times C : d(x_1, x_2) \ge \varepsilon\}$ is compact.
:::

::: pf-step
If $S=\varnothing$, then $U_\varepsilon(C)$ is the whole function space. Otherwise, if $f \in U_\varepsilon(C)$, the continuous function $(x_1, x_2) \mapsto \norm{f(x_1) - f(x_2)}$ is strictly positive on compact $S$, so it achieves a minimum $\delta = \min_S \norm{f(x_1) - f(x_2)} > 0$.
:::

::: pf-step
If $\bar{\rho}(f, g) < \min\{1,\delta/3\}$, then $\norm{f(x)-g(x)}\le\bar\rho(f,g)$ for every $x$, and for all $(x_1, x_2) \in S$: $$\norm{g(x_1) - g(x_2)} \ge \norm{f(x_1) - f(x_2)} - 2\bar{\rho}(f, g) > \delta - \frac{2\delta}{3} = \frac{\delta}{3} > 0.$$
:::

::: pf-step
Thus $g \in U_\varepsilon(C)$, so $U_\varepsilon(C)$ is open.
:::

:::

:::

::: {.pf-step #s4}
Part (d): Density of $U_\varepsilon(C)$ for $N = 2m + 1$.

::: pf-proof

::: pf-step
Since $C$ is compact metrizable with $\dim C \le m$, the maps with $\Delta < \varepsilon$ are dense in $\mathcal{C}(C, \RR^{2m+1})$; this is the density lemma in the proof of the imbedding theorem for compact metrizable spaces of dimension $m$.
:::

::: pf-step
Given $f \in \mathcal{C}(X, \RR^N)$ and $\delta > 0$, choose $g_0 \in \mathcal{C}(C, \RR^N)$ such that $\norm{f\restrict_C - g_0} < \delta$ and $\Delta(g_0) < \varepsilon$.
:::

::: pf-step
The metrizable space $X$ is normal. By the Tietze extension theorem, extend the coordinate functions of $g_0 - f\restrict_C: C \to [-\delta, \delta]^N$ to a continuous map $h: X \to [-\delta, \delta]^N$.
:::

::: pf-step
Define $g = f + h \in \mathcal{C}(X, \RR^N)$.
Then $\bar{\rho}(f, g) \le \delta$ and $g\restrict_C = g_0 \in U_\varepsilon(C)$, proving density.
:::

:::

:::

::: {.pf-step #s5}
Part (e): there is a continuous map $f_0: X \to \RR$ with $f_0(x) \to \infty$ as $x \to \infty$.

::: pf-proof

::: pf-step
There is a countable basis $\theset{B_i}$ of $X$ consisting of open sets with compact closure.

::: pf-proof
Let $x\in X$ and let $O$ be an open set containing $x$. By Theorem 29.2 (printed p. 185) there is a neighbourhood $V$ of $x$ with $\overline V$ compact and $\overline V\subseteq O$, and the given countable basis has an element $B_i$ with $x\in B_i\subseteq V$; then $\overline{B_i}\subseteq\overline V$ is compact. So the basis elements with compact closure form a basis, and there are countably many of them.
:::

:::

::: pf-step
There are compact subspaces $C_1,C_2,\ldots$ with $C_n\subseteq\operatorname{Int}C_{n+1}$ for every $n$ and $X=\bigcup_n C_n$.

::: pf-proof
Put $C_1=\overline{B_1}$ and $k_1=1$. Suppose $C_n=\overline{B_1}\cup\cdots\cup\overline{B_{k_n}}$ has been chosen. The sets $B_i$ cover the compact space $C_n$, so finitely many of them, say $B_{i_1},\ldots,B_{i_r}$, cover it; put $k_{n+1}=\max\{n+1,k_n,i_1,\ldots,i_r\}$ and $C_{n+1}=\overline{B_1}\cup\cdots\cup\overline{B_{k_{n+1}}}$. Then $C_{n+1}$ is a finite union of compact sets and is compact, and $C_n\subseteq C_{n+1}$ because $k_{n+1}\ge k_n$. Moreover $C_n\subseteq B_1\cup\cdots\cup B_{k_{n+1}}$, a union of sets each contained in $C_{n+1}$, so $C_n$ lies in the open set $B_1\cup\cdots\cup B_{k_{n+1}}\subseteq C_{n+1}$ and hence in $\operatorname{Int}C_{n+1}$. Finally $B_1\cup\cdots\cup B_n\subseteq C_{n+1}$ because $k_{n+1}\ge n+1$, so $X=\bigcup_i B_i\subseteq\bigcup_n C_n$.
:::

:::

::: pf-step
There are continuous functions $\phi_n: X \to [0,1]$ with $\phi_n(C_n)=\{1\}$ and $\phi_n(X\setminus\operatorname{Int}C_{n+1})=\{0\}$.

::: pf-proof
The metrizable space $X$ is normal; $C_n$ and $X\setminus\operatorname{Int}C_{n+1}$ are closed and disjoint, since $C_n\subseteq\operatorname{Int}C_{n+1}$. Urysohn's lemma (Theorem 33.1) applies to this pair and gives $\phi_n$.
:::

:::

::: pf-step
$\psi(x)=\sum_{n=1}^\infty(1-\phi_n(x))$ defines a continuous function $\psi: X \to \RR$.

::: pf-proof
Each summand lies in $[0,1]$ and is nonnegative. Given $x$, let $m$ be least with $x\in C_m$, which exists because $X=\bigcup_n C_n$; for $n\ge m$ one has $x\in C_n$, so $\phi_n(x)=1$ and the summand $1-\phi_n(x)$ vanishes, leaving the finite sum $\psi(x)=\sum_{n<m}(1-\phi_n(x))$. For continuity, the sets $\operatorname{Int}C_k$ cover $X$, because $C_k\subseteq\operatorname{Int}C_{k+1}$; and on $\operatorname{Int}C_k$ every summand with $n\ge k$ vanishes, because $\operatorname{Int}C_k\subseteq C_k\subseteq C_n$. So on $\operatorname{Int}C_k$ the function $\psi$ agrees with the finite sum $\sum_{n<k}(1-\phi_n)$, which is continuous there; continuity is a local property and the $\operatorname{Int}C_k$ cover $X$, so $\psi$ is continuous.
:::

:::

::: {.pf-step #psi-bound}
$\psi(x)\ge k-1$ for every $x\in X\setminus C_k$.

::: pf-proof
Let $n\le k-1$. Since $\operatorname{Int}C_{n+1}\subseteq C_{n+1}\subseteq C_k$, the point $x$ lies outside $\operatorname{Int}C_{n+1}$, so $\phi_n(x)=0$ and $1-\phi_n(x)=1$. Every summand of $\psi$ is nonnegative, so $\psi(x)\ge\sum_{n=1}^{k-1}1=k-1$.
:::

:::

::: pf-step
$\psi(x)\to\infty$ as $x\to\infty$.

::: pf-proof
Given $n$, take the compact set $C=C_{n+1}$; for $x\in X\setminus C$ step [](#psi-bound){.pf-ref} gives $\psi(x)\ge n$, which is the definition of $\psi(x)\to\infty$. So $f_0=\psi$ is the map that (e) asks for.
:::

:::

:::

:::

::: pf-step
Part (f): an injective map $f$ with $f(x) \to \infty$ exists.

::: pf-proof

::: pf-step
Since $\RR^N$ is complete, $(\mathcal{C}(X, \RR^N), \bar{\rho})$ is a complete metric space (Theorem 43.5), hence a Baire space.
:::

::: pf-step
The map $f_1(x)=(\psi(x),0,\ldots,0)$ lies in $\mathcal{C}(X,\RR^N)$ and $f_1(x)\to\infty$ as $x\to\infty$.

::: pf-proof
Its first coordinate $\psi$ is continuous by step [](#s5){.pf-ref} and $\norm{f_1(x)}=\psi(x)\ge0$ because $\phi_n\le1$, so for $x$ outside $C_{n+1}$ one has $\norm{f_1(x)}=\psi(x)\ge n$.
:::

:::

::: pf-step
Let $B = \{g \in \mathcal{C}(X, \RR^N) : \bar{\rho}(f_1, g) < 1\}$.
$B$ is a non-empty open subspace, hence a Baire space.
:::

::: pf-step
For each $n \in \ZZ_+$, $U_{1/n}(C_n) \cap B$ is open and dense in $B$ by step [](#s3){.pf-ref} and step [](#s4){.pf-ref}.
:::

::: pf-step
By the Baire category theorem, the intersection $G = \bigcap_{n=1}^\infty U_{1/n}(C_n) \cap B$ is dense in $B$, hence non-empty.
:::

::: pf-step
Choose $f \in G$.
Since $f \in B$, $\bar\rho(f_1,f)<1$ and $f_1(x)\to\infty$, so $f(x) \to \infty$ as $x \to \infty$ by step [](#s1){.pf-ref}.
:::

::: pf-step
For any distinct $x_1, x_2 \in X$, there exists $n$ such that $x_1, x_2 \in C_n$ and $d(x_1, x_2) \ge \frac{1}{n}$.
Since $f \in U_{1/n}(C_n)$, $f(x_1) \neq f(x_2)$.
Thus $f$ is injective.
:::

::: pf-step
By step [](#s2){.pf-ref}, $f$ is a homeomorphism of $X$ onto a closed subspace of $\RR^{2m+1}$.
:::

:::

:::

:::

:::
