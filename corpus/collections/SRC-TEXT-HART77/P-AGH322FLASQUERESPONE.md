---
schema: qual/card@1
id: P-AGH322FLASQUERESPONE
kind: problem
title: Flasque resolution of the structure sheaf on the projective line
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Flasque Sheaves
  - Projective Line
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the statement with the retained Hartshorne Chapter III section 2 transcription and independently reviewed the principal-parts decomposition and rational-function construction on the existing II.1.21 card. The proof establishes flasqueness on every open subset and uses the surjectivity of the actual global principal-parts map.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X=\PP_k^1$ be the projective line over an algebraically closed field $k$.
Show that the exact sequence
$$
0 \to \mco \to \mck \to \mck/\mco \to 0
$$
of (II, Ex. 1.21d) is a flasque resolution of $\mco$.
Conclude from (II, Ex. 1.21e) that $H^i(X, \mco)=0$ for all $i>0$.
:::

::: {.solution}
Put $\OO=\OO_X$, $K=k(t)$, and let $\mathcal K$ be the constant sheaf associated to the additive group of $K$.
For a closed point $P$, write $I_P=K/\OO_{X,P}$ and let $i_P:\{P\}\hookrightarrow X$ be the inclusion.
The generic point contributes zero to these quotients, since its local ring is $K$.

<1>1. The sheaf $\mathcal K$ is flasque.

::: {.proof}
The projective line is irreducible, and every nonempty open subset is connected.
Thus $\mathcal K(V)=K$ for every nonempty open $V$, with identity restrictions between nonempty opens.
The section group on the empty open is zero.
All restriction maps are surjective, which is [[D-COHFLQ|flasqueness]].
:::

<1>2. The quotient $\mathcal K/\OO$ is flasque.

::: {.proof}
The principal-parts decomposition of [[P-AGH2121VARSHEAVES]], part (d), gives
$$
\mathcal K/\OO\cong\bigoplus_{P\text{ closed}}i_{P*}I_P.
$$
Its sections on an open $V\subseteq X$ are precisely the finite-support tuples
$$
\Gamma(V,\mathcal K/\OO)\cong\bigoplus_{P\in V\text{ closed}}I_P.
$$
The finiteness in this description holds because $V$ is quasi-compact: a quotient section is locally represented by a rational function, each such function has only finitely many poles, and a finite number of those neighborhoods cover $V$.
The isomorphism itself sends a section to its principal-part germs and is checked at each stalk, as proved on that card.

For an inclusion $W\subseteq V$, restriction simply discards the components indexed by points outside $W$.
Every finite-support tuple on $W$ extends to one on $V$ by giving all other components value zero.
Thus the restriction is surjective for every such pair of opens, proving flasqueness.
This argument does not assume that arbitrary infinite direct sums of flasque sheaves on arbitrary spaces remain flasque.
:::

<1>3. The sequence in the statement is a flasque resolution and yields
$$
\boxed{H^i(\PP_k^1,\OO)=0\qquad(i>0).}
$$

::: {.proof}
The inclusion $\OO\hookrightarrow\mathcal K$ and its quotient give the stated exact sequence, and steps <1>1--<1>2 make both resolution terms flasque.
By [@Har10a, Proposition III.2.5 and Remark III.2.5.1], its global-section complex computes $H^i(X,\OO)$.
There are terms only in degrees zero and one, so the groups in degrees $i\ge2$ vanish.
The group in degree one is the cokernel of
$$
K\longrightarrow\bigoplus_{P\text{ closed}}K/\OO_{X,P}.
$$
This map is surjective by [[P-AGH2121VARSHEAVES]], part (e).
Explicitly, the principal part at a finite point $t=a$ has a representative $\sum_{j=1}^{N_a}c_{a,j}(t-a)^{-j}$, and a principal part at infinity has a representative $\sum_{j=1}^{N_\infty}d_jt^j$.
The sum of these expressions over the finitely many prescribed points realizes all their principal parts: the finite-point terms are regular at infinity and at every other finite point, while the polynomial term is regular at every finite point.
Hence that cokernel is also zero, proving the assertion for $i=1$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 establish the flasque resolution, and step <1>3 computes all its positive-degree cohomology groups.
:::
:::
