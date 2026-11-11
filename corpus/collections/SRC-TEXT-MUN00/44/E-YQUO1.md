---
schema: qual/card@1
id: E-YQUO1
kind: problem
title: Peano spaces and the Hahn-Mazurkiewicz theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §44 Exercise 4 was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book, part
    (a) following the exercise's hint. Compactness and connectedness of X = f(I) are Theorem 26.5 and
    Theorem 23.5. The hint is discharged: a closed subset of the compact space I has compact image, closed
    in the Hausdorff space X, so f is a closed map, and its fibers are closed subsets of I hence compact
    (Theorem 26.2 and Theorem 17.5), which is the definition of a perfect map in Exercise 31.7.
    Weak local connectedness is proved on the card in the form of §25: for x in U take the compact fiber F
    inside the open set f^{-1}(U), cover F by finitely many connected basis intervals inside f^{-1}(U),
    and use closedness of f to obtain a neighbourhood of x whose image lies in the union of the images of
    those intervals, a connected set inside U. Metrizability follows because second countability is
    transferred by the perfect map (the already sourced Exercise 31.7(d), card E-Y4MFU) and a second
    countable compact Hausdorff space is metrizable by the Urysohn metrization theorem (Theorem 34.1,
    with Theorem 32.3 giving normality and Theorem 30.2 hereditary second countability). Part (b) is the
    exercise's own instruction to assume the Hahn-Mazurkiewicz theorem and verify its hypotheses for
    I^omega: compactness by the Tychonoff theorem (Theorem 37.3), metrizability by Theorem 20.5,
    connectedness because a product of connected spaces is connected (Theorem 23.6 for the finite pieces,
    Theorem 23.3 for their union over a common point and Theorem 23.4 for the closure, an argument the
    card now writes out in place of the bare appeal it made before), and weak local connectedness from the
    basis of products of connected intervals, connected for the same reason.
---

::: {.exercise}

(a) Let $X$ be a Hausdorff space.
Show that if there is a continuous surjective map $f: I \to X$, then $X$ is compact, connected, weakly locally connected, and metrizable.
[Hint: Show $f$ is a perfect map.]

(b) The converse of the result in (a) is a famous theorem of point-set topology called the Hahn-Mazurkiewicz theorem (see [H-Y], p. 129). Assuming this theorem, show there is a continuous surjective map $f: I \to I^\omega$.

A Hausdorff space that is the continuous image of the closed unit interval is often called a Peano space.
:::

::: {.solution}
(a) Let $f:I\to X$ be continuous and surjective, with $X$ Hausdorff. Since $I$ is compact, $X=f(I)$ is compact. Since $I$ is connected, $X$ is connected.

The map $f$ is closed: a closed subset of $I$ is compact, and its image is compact, hence closed in the Hausdorff space $X$. Its fibers are closed subsets of $I$, hence compact. Thus $f$ is a perfect quotient map.

Let $x\in X$ and let $U$ be an open neighborhood of $x$. The compact fiber $F=f^{-1}(x)$ lies in the open set $f^{-1}(U)$. Cover $F$ by finitely many connected open intervals $V_1,\ldots,V_m$ contained in $f^{-1}(U)$. Each $f(V_i)$ is connected and contains $x$, so $C=\bigcup_i f(V_i)$ is connected and lies in $U$. Since $f$ is closed and $\bigcup_i V_i$ is an open neighborhood of $F$, the set $X\setminus f(I\setminus\bigcup_i V_i)$ is an open neighborhood of $x$ contained in $C$. Thus $C$ is a connected neighborhood of $x$ inside $U$, and $X$ is weakly locally connected.

Finally, $I$ is second countable, and perfect maps preserve second countability by [[E-Y4MFU]](d). Thus $X$ is second countable. A compact Hausdorff space is regular, so the Urysohn metrization theorem implies that $X$ is metrizable.

Therefore every Hausdorff continuous image of $I$ is compact, connected, weakly locally connected, and metrizable.

(b) The Hilbert cube
$$
I^\omega=\prod_{n\ge1}I
$$
is compact by the Tychonoff theorem (Theorem 37.3) and metrizable because it is a countable product of metrizable spaces (Theorem 20.5). It is connected because a product of connected spaces is: fix a point $a$ of the product; for each finite set $F$ of indices the subspace $X_F=\{x \mid x_i=a_i \text{ for } i\notin F\}$ is a finite product of connected spaces, hence connected (Theorem 23.6), and all the $X_F$ contain $a$, so their union is connected (Theorem 23.3) and dense in the product; therefore the product is connected (Theorem 23.4). This applies to $I^\omega$.

It is also weakly locally connected. A basic neighbourhood of a point of $I^\omega$ is $\prod_{i\le N}J_i\times\prod_{i>N}I$ with open intervals $J_i$ containing the coordinates; being a product of connected spaces, it is connected by the argument above. The basic sets form a neighbourhood basis, so each point has a neighbourhood basis of connected sets.

Hence $I^\omega$ satisfies the hypotheses of the Hahn--Mazurkiewicz theorem quoted in the exercise. Therefore there exists a continuous surjection
$$
I\twoheadrightarrow I^\omega.
$$
:::
