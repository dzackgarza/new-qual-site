---
schema: qual/card@1
id: P-AGXGATHSECSTALKS
kind: problem
title: When germs at points determine a section of a sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Stalks
  - Regular Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Gathmann 3.22 in the retained native problem source at revision
    7eafedfc0 and compared all three parts with the current card. The retained
    source gives the problem statement but no worked solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the proof. Checked the neighborhood argument and sheaf uniqueness
    in (a), density of nonempty opens and closed equalizers of regular
    functions in (b), and the continuous-function counterexample in (c).
---

::: {.problem}
Let $\phi, \psi \in \mcf(U)$ be two sections of some sheaf $\mcf$ on an open $U\subseteq X$ and show that

a. If $\phi, \psi$ agree on all stalks, so $\bar{(U, \phi)} = \bar{(U, \psi)} \in \mcf_a$ for all $a\in U$, then $\phi$ and $\psi$ are equal.

b. If $\mcf \da \OO_X$ is the sheaf of regular functions on some irreducible affine variety $X$, then if $\psi = \phi$ on one stalk $\mcf_a$, then $\phi = \psi$ everywhere.

c. For a general sheaf $\mcf$ on $X$, (b) is false.
:::

::: {.solution}

::: pf

::: {.pf-step #same-germs-implies-equal}
(a) If $\phi$ and $\psi$ have the same germ at every point of $U$,
then $\phi=\psi$ in $\mcf(U)$.

::: pf-proof
Fix $a\in U$. Equality of the two germs in $\mcf_a$ means that there is an
open neighborhood
$$
U_a\subseteq U
$$
of $a$ such that
$$
\ro{\phi}{U_a}=\ro{\psi}{U_a}.
$$
The sets $U_a$ cover $U$. Hence the restrictions of $\phi$ and $\psi$
agree on an open cover of $U$. By the uniqueness axiom for the sheaf
$\mcf$, the two sections are equal on $U$.
:::

:::

::: {.pf-step #irreducible-regular-functions-agree}
(b) If $X$ is irreducible, $\mcf=\OO_X$, and the germs of
$\phi,\psi\in\OO_X(U)$ agree at one point $a\in U$, then
$$
\boxed{\phi=\psi\text{ on }U}.
$$

::: pf-proof
Equality of the germs at $a$ gives a nonempty open neighborhood
$$
W\subseteq U
$$
on which $\phi=\psi$.

Because $X$ is irreducible and $U$ is a nonempty open subset of $X$, the
space $U$ is irreducible. Therefore every nonempty open subset of $U$ is
dense in $U$, so $W$ is dense in $U$.

The difference
$$
h=\phi-\psi
$$
is a regular function on $U$. Its zero locus
$$
V_U(h)=\{x\in U:h(x)=0\}
$$
is closed in $U$. Since $W\subseteq V_U(h)$ and $W$ is dense in $U$, one
has
$$
V_U(h)=U.
$$
Thus $h=0$ on $U$, so $\phi=\psi$ everywhere on $U$.
:::

:::

::: {.pf-step #counterexample-general-sheaf}
(c) Equality on one stalk does not determine sections of a general sheaf.

::: pf-proof
Let $X=\RR$ with its standard topology and let $\mcf$ be the sheaf of
continuous real-valued functions. On $U=\RR$, define
$$
\phi(x)=0
$$
and
$$
\psi(x)=
\begin{cases}
0,&x\le1,\\
x-1,&x>1.
\end{cases}
$$
Both are continuous. On a neighborhood of $a=0$ they agree identically,
so
$$
\phi_0=\psi_0\in\mcf_0.
$$
But $\psi(2)=1\ne0=\phi(2)$, so $\phi\ne\psi$ as global sections. This
gives the required counterexample.
:::

:::

::: pf-qed
Steps [](#same-germs-implies-equal){.pf-ref}, [](#irreducible-regular-functions-agree){.pf-ref} and [](#counterexample-general-sheaf){.pf-ref} prove (a)--(c), respectively.
:::

:::
:::
