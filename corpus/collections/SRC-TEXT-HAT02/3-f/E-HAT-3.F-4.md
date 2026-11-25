---
schema: qual/card@1
id: E-HAT-3.F-4
kind: problem
title: "Divisible groups and vanishing Ext"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 4; repaired the local statement to restore the source's “if and only if”.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.F Exercise 4, printed page
    320; the statement matches word for word. Checked: a direct sum of copies of Q is
    divisible coordinatewise and divisibility passes to quotients, giving one
    direction; conversely a divisible G is a quotient of ⊕_I Q by choosing a
    generating set and dividing repeatedly to build Q-linear combinations mapping
    onto G. The deduction uses Exercise 3 (Ext(A,Q) = 0) with the long exact Ext
    sequence, so Ext(A,G) = 0 for divisible G. No defect.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two directions and the deduction, which is what Queue D asks for on this card. The converse is split into the construction of the maps Q -> G from the divisibility of G and the surjectivity of their direct sum; the additivity and well-definedness of phi, which the prose compressed into "inductively this defines a homomorphism", are now checked at a common denominator, and the vanishing of Ext for the direct sum is derived from Exercise 3 by the behaviour of Ext on direct sums in the second variable rather than being asserted. No retained set covers this exercise; the card now says so, and the exercise and its previous problem are both located on printed p. 320. No statement repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read again against Hatcher, §3.F Exercise 4, and its "if and only if": the text version of the
    book drops the "f" and prints one direction, and the card states both, which is the printed
    reading. The proof is correct as it stands — quotients of direct sums of $\QQ$ are divisible; the
    elements $g_n$ with $n!g_n=g_{(n-1)!}$ satisfy $m!g_m=g$ by induction, which makes
    $\phi(m/k!)=mg_k$ well defined and additive on a common denominator; a generating set and one
    such $\phi$ per generator make $G$ a quotient of $\bigoplus_I\QQ$; and
    $\operatorname{Ext}(A,\QQ)=0$ with $\operatorname{Ext}$ turning $\bigoplus$ in the second
    variable into $\prod$ gives $\operatorname{Ext}(A,G)=0$ from the sequence ending
    $\operatorname{Ext}(A,D)\to\operatorname{Ext}(A,G)\to0$. One correction to the provenance: the
    paragraph said the retained sets stop inside §3.3, which is false — Sam's set reaches §4.3 and
    Koukpari's carries a §3.F heading — so it now records what the retained sets contain and that
    none of them has a solution of this exercise.
---

::: {.problem}
An abelian group $G$ is defined to be divisible if the map $G \xrightarrow{n} G$, $g \mapsto ng$, is surjective for all $n > 1$.
Show that a group is divisible if and only if it is a quotient of a direct sum of $\QQ$'s. Deduce from the previous problem that if $G$ is divisible then $\operatorname{Ext}(A, G) = 0$ for all $A$.
:::

::: {.solution}
The argument is the card's own: no retained solution set contains a solution of any exercise of §3.F. Koukpari's set carries the §3.F heading *Limits and Ext* with nothing under it, Sam's begins at §4.1, and the other retained sets stop earlier; there is therefore no published proof of this exercise to transcribe. It is checked against Hatcher, §3.F Exercise 4, whose "previous problem" is §3.F Exercise 3, $\operatorname{Ext}(A,\QQ)=0$ for all $A$.

::: pf

::: {.pf-step #quotients}
A quotient of a direct sum of copies of $\QQ$ is divisible.

::: pf-proof
A direct sum of copies of $\QQ$ is divisible coordinatewise: an element has only finitely many nonzero coordinates, and each of those is divisible in $\QQ$. If $D$ is divisible, $K\le D$ and $G=D/K$, then for $\overline g=g+K$ and $n>0$ divisibility of $D$ gives $h\in D$ with $nh=g$, so $n\overline h=\overline g$. Hence $G$ is divisible.
:::

:::

::: {.pf-step #roots}
For every $g\in G$ there is a homomorphism $\phi:\QQ\to G$ with $\phi(1)=g$.

::: pf-proof
Divisibility lets one choose elements $g_n$ with $n!\,g_n=g_{(n-1)!}$ for $n\ge2$, starting from $g_1=g$: an element $g_{(n-1)!}$ has an $n$-th root because the map $x\mapsto nx$ is onto. By induction $m!\,g_m=g$ for every $m$. Now set $\phi(m/k!)=m\,g_k$ for $m\in\ZZ$, $k\ge1$. This is well defined: if $m/k!=m'/k'$ and $N\ge k,k'$, then $mN!/k!=m'N!/k'$ in $\ZZ$, and
$$
m\,g_k=m\cdot\tfrac{N!}{k!}g_N=\tfrac{mN!}{k!}g_N=\tfrac{m'N!}{k'}g_N=m'\cdot\tfrac{N!}{k'}g_{k'}=m'\,g_{k'},
$$
using $k!\,g_k=N!\,g_N$, which is the identity $m!g_m=g$ read at $m=N$ and $m=k$. It is additive on a common denominator, because $(m+m')/k!=m/k!+m'/k!$ gives $(m+m')g_k=mg_k+m'g_k$, so $\phi$ is a homomorphism $\QQ\to G$ with $\phi(1)=g$.
:::

:::

::: {.pf-step #surjective}
$G$ is a quotient of a direct sum of copies of $\QQ$.

::: pf-proof
Choose a generating set $(g_i)_{i\in I}$ of $G$ as an abelian group and, for each $i$, a homomorphism $\phi_i:\QQ\to G$ with $\phi_i(1)=g_i$, which step [](#roots){.pf-ref} provides. The direct sum over $I$ of copies of $\QQ$ maps by $\Phi$ to $G$, and its image contains every $g_i$, hence is all of $G$ since the $g_i$ generate. So $G\cong\bigl(\bigoplus_I\QQ\bigr)/\ker\Phi$ is a quotient of a direct sum of copies of $\QQ$.
:::

:::

::: {.pf-step #ext-divisible}
If $G$ is divisible then $\operatorname{Ext}(A,G)=0$ for every abelian group $A$.

::: pf-proof
By steps [](#quotients){.pf-ref} and [](#surjective){.pf-ref} write $G=D/K$ with $D=\bigoplus_I\QQ$. Exercise 3 of the section gives $\operatorname{Ext}(A,\QQ)=0$ for all $A$; since $\operatorname{Ext}$ converts direct sums in its second variable into products, $\operatorname{Ext}(A,D)=\prod_I\operatorname{Ext}(A,\QQ)=0$. The short exact sequence $0\to K\to D\to G\to0$ gives the six-term exact sequence of $\operatorname{Hom}(A,-)$ and $\operatorname{Ext}(A,-)$, which ends
$$
\operatorname{Ext}(A,D)\longrightarrow\operatorname{Ext}(A,G)\longrightarrow0 .
$$
The left group vanishes, so $\operatorname{Ext}(A,G)=0$; that is $\boxed{\operatorname{Ext}(A,G)=0}$ for every divisible $G$ and every $A$, which is the deduction the exercise asks for.
:::

:::

:::
:::
