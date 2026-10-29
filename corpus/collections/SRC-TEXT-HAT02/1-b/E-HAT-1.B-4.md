---
schema: qual/card@1
id: E-HAT-1.B-4
kind: problem
title: "The HNN extension $A *_C$ as a quotient of $A * \\ZZ$ via van Kampen"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Use van Kampen's theorem to compute $A *_C$ as a quotient of $A * \ZZ$, as stated in the text.
:::

::: {.solution}

In the text, $A *_C$ is the fundamental group of the graph of groups with one vertex group $A$, one edge group $C$, and one loop edge, with injective homomorphisms $\varphi, \psi: C \to A$.
Its graph of spaces is
$$Z = \big(X_A \sqcup (X_C \times [0, 1])\big) \big/ \big((x, 0) \sim f(x),\ (x, 1) \sim g(x)\big),$$
where $X_A$ and $X_C$ are $K(A, 1)$ and $K(C, 1)$ CW complexes and $f, g: X_C \to X_A$ are cellular maps inducing $\varphi$ and $\psi$.
Fix a $0$-cell $c_0 \in X_C$.
The claim to prove is
$$\pi_1(Z) \cong (A * \langle t \rangle) \big/ \big\langle\!\big\langle\, t\, \varphi(c)\, t^{-1} \psi(c)^{-1} : c \in C \,\big\rangle\!\big\rangle.$$

::: pf

::: {.pf-step #same-basepoint}

We may assume $f(c_0) = g(c_0) = a_0$.

::: pf-proof

$X_A$ is path-connected, so there is a path from $g(c_0)$ to $f(c_0)$.
By homotopy extension for the CW pair $(X_C, c_0)$, $g$ is homotopic to a map $g'$ with $g'(c_0) = f(c_0)$.
Homotopic attaching maps give homotopy-equivalent spaces, so $Z$ changes only up to homotopy equivalence.
The homomorphism $\psi$ changes only by composition with an inner automorphism of $A$, namely conjugation by the class of the path, and that conjugation is absorbed by replacing $t$ with $t$ times this class.
So the presentation to be proved is unchanged.

:::

:::

::: {.pf-step #cover}

Let $U = Z \setminus (X_C \times \{1/2\})$, and let $V$ be the union of $X_C \times (0, 1)$ with $N \times [0, 1]$ and a contractible open neighborhood $N_A$ of $a_0$ in $X_A$, where $N \subset X_C$ is a contractible open neighborhood of $c_0$ with $f(N), g(N) \subset N_A$.
Then $U$, $V$ and $U \cap V$ are open and path-connected, and
$$\pi_1(U) \cong A, \qquad \pi_1(V) \cong C * \langle t \rangle, \qquad \pi_1(U \cap V) \cong C_0 * C_1,$$
where $t$ is the loop $\{c_0\} \times [0, 1]$, whose ends both lie at $a_0$, and $C_0, C_1$ are two copies of $C$.

::: pf-proof

CW complexes are locally contractible, so $N_A$ and $N$ exist; continuity of $f$ and $g$ lets $N$ be shrunk until $f(N), g(N) \subset N_A$.
Each half-cylinder $X_C \times [0, 1/2)$ and $X_C \times (1/2, 1]$ deformation retracts onto its end, so $U$ deformation retracts onto $X_A$, and $\pi_1(U) \cong A$.
In $V$, shrink $N_A$ to $a_0$ and $N$ to $c_0$: $V$ deformation retracts onto $X_C \times (0, 1)$ with the arc $\{c_0\} \times [0, 1]$ whose two ends are joined at $a_0$.
This space is homotopy equivalent to $X_C \vee S^1$, so $\pi_1(V) \cong C * \langle t \rangle$.
In the same way, $U \cap V$ deformation retracts onto the two pieces $X_C \times \{1/4\}$ and $X_C \times \{3/4\}$ joined through $N_A$ by the arcs $\{c_0\} \times [0, 1/4]$ and $\{c_0\} \times [3/4, 1]$.
This space is homotopy equivalent to $X_C \vee X_C$, so $\pi_1(U \cap V) \cong C_0 * C_1$.

:::

:::

::: {.pf-step #inclusions}

With base point $a_0$, the inclusion of $U \cap V$ into $U$ sends $c \in C_0$ to $\varphi(c)$ and $c \in C_1$ to $\psi(c)$.
The inclusion into $V$ sends $c \in C_0$ to $c$ and $c \in C_1$ to $t^{-1} c\, t$.

::: pf-proof

In $U$, the deformation onto $X_A$ moves $X_C \times \{1/4\}$ to its image under $f$ and $X_C \times \{3/4\}$ to its image under $g$, along the arcs from $a_0$; so the two copies of $C$ map by $f_* = \varphi$ and $g_* = \psi$.
In $V$, a loop $c$ in $X_C \times \{1/4\}$ is the generator $c$ of the factor $C$.
A loop $c$ in $X_C \times \{3/4\}$, read at $a_0$, leaves $a_0$ through the end of the arc at height $1$, runs down the arc to height $3/4$, goes around $c$, and returns.
Sliding the loop $c$ down the cylinder to height $1/4$ turns this into: the whole arc from height $1$ to height $0$, which is $t^{-1}$, then $c$, then $t$; so it equals $t^{-1} c\, t$ in $\pi_1(V)$.

:::

:::

::: pf-step

$\pi_1(Z) \cong (A * \langle t \rangle) / \langle\!\langle t\, \varphi(c)\, t^{-1} \psi(c)^{-1} : c \in C \rangle\!\rangle$, which is $A *_C$.

::: pf-proof

By van Kampen's theorem and steps [](#cover){.pf-ref} and [](#inclusions){.pf-ref},
$$\pi_1(Z) \cong (A * C * \langle t \rangle) \big/ \big\langle\!\big\langle\, \varphi(c)\, c^{-1},\ \psi(c)\, t^{-1} c^{-1} t : c \in C \,\big\rangle\!\big\rangle.$$
The first family of relations sets $c = \varphi(c)$, so the factor $C$ is eliminated.
The second family then reads $\psi(c) = t^{-1} \varphi(c)\, t$.
Replacing the generator $t$ by $t^{-1}$ turns this into $t\, \varphi(c)\, t^{-1} = \psi(c)$, which is the presentation of $A *_C$ as a quotient of $A * \ZZ$ stated in the text.
By step [](#same-basepoint){.pf-ref}, this holds without the assumption $f(c_0) = g(c_0)$.

:::

:::

:::

:::
