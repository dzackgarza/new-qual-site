---
schema: qual/card@1
id: E-I9R8B
kind: problem
title: The cone on the infinite earring
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 82 Exercise 2, printed p. 499. The cone on the infinite earring is simply connected but not locally simply connected at the origin. Checked against Example 1 of Section 80 and Theorem 59.3. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: the proof began by writing C(X) as the quotient (X x [0,1])/(X x {1}) with no justification; the two are now identified through the map q, which is a continuous bijection from the compact space X x [0,1] onto the Hausdorff subspace C(X) and so a homeomorphism of the quotient by Theorem 26.6 (printed p. 167), compactness being Theorem 26.7 (printed p. 167) together with the compactness of the earring. Corrected: the conclusion was drawn for "no neighbourhood has all its loops nullhomotopic in U" without stating the definition it negates; the proof now negates the definition of local simple connectedness quoted on printed p. 494, using that a nullhomotopy inside a smaller neighbourhood V would be one inside U. Citations added: Example 1 of §80 (printed p. 487) for the earring, Lemma 55.1 (printed p. 348) for injectivity of the map induced by a retraction, and Theorem 54.5 (printed p. 345) for pi_1 of the circle. What the certificate does not cover: the deformation retraction of the punctured cone and the retraction of the earring onto one of its circles are written out here, not taken from the book.
---

::: {.exercise}

Let $X$ be the infinite earring in $\RR^2$.
(See Example 1 of §80.) Let $C(X)$ be the subspace of $\RR^3$ that is the union of all line segments joining points of $X \times 0$ to the point $p = (0, 0, 1)$.
It is called the cone on $X$.
Show that $C(X)$ is simply connected, but is not locally simply connected at the origin.

:::

::: {.solution}

Let $X=\bigcup_{n\ge1}C_n$ be the earring of Example 1 of §80 (printed p. 487), the union of the circles $C_n$ of radius $1/n$ through the origin $o$. Let $q:X\times[0,1]\to\RR^3$ be the map $q(x,t)=(1-t)x+t\,p$; its image is $C(X)$ and $q(x,1)=p$ for every $x$.

::: pf

::: {.pf-step #cone}

$q$ induces a homeomorphism of the quotient space $(X\times[0,1])/(X\times\{1\})$ onto $C(X)$.

::: pf-proof

Distinct points $(x,t)$ and $(x',t')$ of $X\times[0,1)$ have distinct images under $q$: two such points lie on the line segments joining $p$ to $x$ and to $x'$, which meet only in $p$ because $p\notin\RR^2\times 0$, and on one such segment $q$ is injective. So $q$ is constant exactly on the fibres of the projection to $(X\times[0,1])/(X\times\{1\})$, and therefore induces a continuous bijection $Q$ of that quotient onto $C(X)$. That quotient is compact, being the image of the compact space $X\times[0,1]$ under a continuous map (Theorem 26.5, printed p. 166); here $X$ is compact, being closed and bounded in $\RR^2$, and a product of two compact spaces is compact (Theorem 26.7, printed p. 167). The space $C(X)$ is Hausdorff, being a subspace of $\RR^3$. A continuous bijection of a compact space onto a Hausdorff space is a homeomorphism (Theorem 26.6, printed p. 167), so $Q$ is one.

:::

:::

::: {.pf-step #contractible}

$C(X)$ is contractible, hence simply connected.

::: pf-proof

Under the identification of step [](#cone){.pf-ref} the formula $H([x,t],s)=[x,(1-s)t+s]$ defines a continuous map $C(X)\times[0,1]\to C(X)$: it is well defined on the quotient because $(1-s)t+s=1$ whenever $t=1$. It satisfies $H(\cdot,0)=\id$ and $H(\cdot,1)\equiv p$. A path homotopy of a loop $f$ to the constant loop at $f(0)$ is given by $(s,u)\mapsto H(f(s),u)$, so every loop in $C(X)$ is nullhomotopic and $C(X)$ is simply connected in the sense of the Definition (printed p. 333).

:::

:::

::: {.pf-step #retract}

$U=C(X)\setminus\{p\}$ is an open neighbourhood of $o$ of which $X$ is a deformation retract, and for every neighbourhood $V\subseteq U$ of $o$ there is $n$ with $C_n\subseteq V$.

::: pf-proof

$\{p\}$ is closed in the metric space $C(X)$, so $U$ is open, and $o=q(o,0)\in U$. The map $r:U\to X$, $r([x,t])=[x,0]=x$, is continuous, and $H([x,t],s)=[x,(1-s)t]$ is a homotopy in $U$ from the identity of $U$ to the inclusion $X\to U$; so $X$ is a deformation retract of $U$. Since $C_n$ has diameter $2/n$ and passes through $o$, a neighbourhood $V$ of $o$ in $C(X)$ contains $C_n$ as soon as it contains a ball about $o$ of radius greater than $2/n$.

:::

:::

::: {.pf-step #notnull}

For each $n$ the loop $\gamma_n$ that traverses $C_n$ once is not nullhomotopic in $U$.

::: pf-proof

The retraction $r_n:X\to C_n$ that maps $C_i$ to $o$ for $i\ne n$ and fixes $C_n$ is continuous, and $(r_n)_*:\pi_1(X,o)\to\pi_1(C_n,o)$ is injective by Lemma 55.1 (printed p. 348). The class $(r_n)_*[\gamma_n]$ generates $\pi_1(C_n,o)\cong\ZZ$ (Theorem 54.5, printed p. 345) and is therefore nonzero, so $[\gamma_n]\ne 0$ in $\pi_1(X,o)$. If $\gamma_n$ were nullhomotopic in $U$, applying the retraction $r:U\to X$ of step [](#retract){.pf-ref} would give a nullhomotopy of $\gamma_n$ in $X$, and then $(r_n)_*[\gamma_n]=(r_n\circ r)_*[\gamma_n]=0$, a contradiction.

:::

:::

::: {.pf-step #notlocally}

$C(X)$ is not locally simply connected at $o$.

::: pf-proof

Local simple connectedness at $o$ would mean that within each neighbourhood of $o$ there is a neighbourhood that is itself simply connected (printed p. 494). But $U=C(X)\setminus\{p\}$ is a neighbourhood of $o$, and for every neighbourhood $V\subseteq U$ of $o$ step [](#retract){.pf-ref} provides an $n$ with $\gamma_n$ a loop in $V$ based at $o$; by step [](#notnull){.pf-ref} that loop is not nullhomotopic in $U$, hence not in the smaller space $V$. So no neighbourhood of $o$ contained in $U$ is simply connected, and $C(X)$ is not locally simply connected at $o$.

:::

:::

:::

:::
