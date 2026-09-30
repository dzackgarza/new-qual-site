---
schema: qual/card@1
id: P-AGH323SUPPORTS
kind: problem
title: Cohomology with supports in a closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Local Cohomology
  - Flasque Sheaves
  - Excision
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all six parts with the retained Hartshorne Chapter III section 2 transcription and checked the support and flasque-resolution constructions against Stacks Project sections 20.12 and 20.21. The proof corrects arbitrary lifts to have the required support and derives excision on the same resolution, with no finiteness hypothesis on the space.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a topological space, let $Y$ be a closed subset, and let $\mcf$ be a sheaf of abelian groups.
Let $\Gamma_Y(X, \mcf)$ denote the group of sections of $\mcf$ with support in $Y$ (II, Ex. 1.20).

(a) Show that $\Gamma_Y(X, \wait)$ is a left exact functor from $\Ab(X)$ to $\Ab$.
We denote the right derived functors of $\Gamma_Y(X, \wait)$ by $H_Y^i(X, \wait)$.
They are the cohomology groups of $X$ with supports in $Y$, and coefficients in a given sheaf.

(b) If $0 \to \mcf' \to \mcf \to \mcf'' \to 0$ is an exact sequence of sheaves, with $\mcf'$ flasque, show that
$$
0 \to \Gamma_Y(X, \mcf') \to \Gamma_Y(X, \mcf) \to \Gamma_Y(X, \mcf'') \to 0
$$
is exact.

(c) Show that if $\mcf$ is flasque, then $H_Y^i(X, \mcf)=0$ for all $i>0$.

(d) If $\mcf$ is flasque, show that the sequence
$$
0 \to \Gamma_Y(X, \mcf) \to \Gamma(X, \mcf) \to \Gamma(X-Y, \mcf) \to 0
$$
is exact.

(e) Let $U=X-Y$.
Show that for any $\mcf$, there is a long exact sequence of cohomology groups
$$
\begin{aligned}
0 &\to H_Y^0(X, \mcf) \to H^0(X, \mcf) \to H^0(U, \restrictionof{\mcf}{U}) \\
&\to H_Y^1(X, \mcf) \to H^1(X, \mcf) \to H^1(U, \restrictionof{\mcf}{U}) \\
&\to H_Y^2(X, \mcf) \to \cdots
\end{aligned}
$$

(f) *Excision.* Let $V$ be an open subset of $X$ containing $Y$.
Then there are natural functorial isomorphisms, for all $i$ and $\mcf$,
$$
H_Y^i(X, \mcf) \cong H_Y^i(V, \restrictionof{\mcf}{V}).
$$
:::

::: {.solution}
Put $U=X\setminus Y$.
For a section $s$ of an abelian sheaf, its [[D-UDIVH|support]] is the set of points where its germ is nonzero.
Consequently
$$
\Gamma_Y(X,\mcf)=\ker\bigl(\Gamma(X,\mcf)\longrightarrow\Gamma(U,\mcf|_U)\bigr).
$$
We use the ordinary cohomological facts that injective abelian sheaves are flasque, flasque sheaves are acyclic for global sections on every open, and acyclic resolutions compute right derived functors [@Har10a, Chapter III, §1, Lemma III.2.4 and Proposition III.2.5].
Restriction of a flasque sheaf to an open subset is flasque by its definition.

::: pf

::: {.pf-step #s1}

Sections with support in $Y$ form an additive left exact functor, proving (a).

::: pf-proof

A morphism of sheaves sends a section with zero germ at a point to one with zero germ there.
It therefore sends sections supported in $Y$ to sections supported in $Y$, and respects sums, identities and compositions.

Consider an exact sequence $0\to A\xrightarrow{a}B\xrightarrow{b}C$ of sheaves.
Left exactness of ordinary global sections makes $\Gamma(X,A)\to\Gamma(X,B)$ injective.
If $s\in\Gamma_Y(X,B)$ maps to zero in $\Gamma_Y(X,C)$, there is a unique $t\in\Gamma(X,A)$ with $a(t)=s$.
At every point outside $Y$, the image of $t_x$ under the injective stalk map $a_x$ is zero.
Thus $t_x=0$ there, so $t$ is supported in $Y$.
This proves exactness at the middle term for sections with support, as well as injectivity at the first term.
The functor's zeroth derived functor is itself, so $H_Y^0(X,\mcf)=\Gamma_Y(X,\mcf)$.

:::

:::

::: {.pf-step #s2}

If the kernel $A$ of a short exact sequence $0\to A\to B\to C\to0$ is flasque, then $\Gamma_Y(X,B)\to\Gamma_Y(X,C)$ is surjective.

::: pf-proof

Let $c\in\Gamma_Y(X,C)$.
Ordinary global sections of the given sequence are exact on the right, because $H^1(X,A)=0$ for the flasque sheaf $A$.
Choose a global lift $b\in\Gamma(X,B)$ of $c$.
Its restriction to $U$ maps to zero in $C|_U$ and therefore comes from a section $a_U\in\Gamma(U,A|_U)$.
Flasqueness of $A$ extends $a_U$ to $a\in\Gamma(X,A)$.
Subtract its image from $b$.
The resulting section still maps to $c$ and restricts to zero on $U$, so it belongs to $\Gamma_Y(X,B)$.
Together with step [](#s1){.pf-ref}, this gives the full exact sequence in (b).

:::

:::

::: {.pf-step #s3}

Every flasque sheaf is acyclic for $\Gamma_Y(X,-)$, proving (c).

::: pf-proof

First, the quotient $Q$ in a short exact sequence $0\to A\to B\to Q\to0$ with $A$ and $B$ flasque is flasque.
For opens $W\subseteq V$, a section of $Q$ on $W$ lifts to $B(W)$, because $A|_W$ is acyclic for ordinary global sections.
Extend the lift to $B(V)$ by flasqueness and take its image in $Q(V)$.
This extends the original section, proving the assertion.

Now let $\mcf$ be flasque and construct an injective resolution through sequences
$$
0\longrightarrow Z^j\longrightarrow I^j\longrightarrow Z^{j+1}\longrightarrow0,
\qquad Z^0=\mcf.
$$
Every $I^j$ is flasque because it is injective.
The quotient assertion just proved shows inductively that every $Z^j$ is flasque.
Step [](#s2){.pf-ref} makes each of these sequences exact after applying $\Gamma_Y(X,-)$.
Splicing the resulting sequences shows that the augmented complex
$$
0\to\Gamma_Y(X,\mcf)\to\Gamma_Y(X,I^0)
\to\Gamma_Y(X,I^1)\to\cdots
$$
is exact.
Its positive-degree cohomology groups are the derived functors $H_Y^i(X,\mcf)$, so they are zero.

:::

:::

::: {.pf-step #s4}

The sequence in (d) is exact for every flasque $\mcf$.

::: pf-proof

The kernel of restriction to $U$ is exactly $\Gamma_Y(X,\mcf)$ by the support description preceding step [](#s1){.pf-ref}.
The restriction map $\Gamma(X,\mcf)\to\Gamma(U,\mcf|_U)$ is surjective by flasqueness.
This proves all terms of the short exact sequence in (d).

:::

:::

::: {.pf-step #s5}

The long exact sequence in (e) is the cohomology sequence of a short exact sequence of complexes.

::: pf-proof

Choose an injective resolution $\mcf\to I^\bullet$ on $X$.
Its terms are flasque, so step [](#s4){.pf-ref} gives a degreewise short exact sequence
$$
0\to\Gamma_Y(X,I^\bullet)\to\Gamma(X,I^\bullet)
\to\Gamma(U,I^\bullet|_U)\to0.
$$
The first two complexes compute $H_Y^i(X,\mcf)$ and $H^i(X,\mcf)$ by definition.
Restriction is exact, and $I^\bullet|_U$ has flasque terms.
It is therefore an acyclic resolution of $\mcf|_U$ for ordinary cohomology, so the third complex computes $H^i(U,\mcf|_U)$.
The long exact cohomology sequence of these complexes is exactly the sequence in (e), with the zeroth supported term identified by step [](#s1){.pf-ref}.
The maps arise from inclusion of supported sections, restriction and the connecting maps of the short exact sequence.
Comparison of resolutions gives their naturality in $\mcf$ [@Har10a, Chapter III, §1].

:::

:::

::: {.pf-step #s6}

Restriction gives the natural excision isomorphisms in (f).

::: pf-proof

For every sheaf $A$ on $X$, restriction induces an isomorphism
$$
\Gamma_Y(X,A)\xrightarrow{\cong}\Gamma_Y(V,A|_V).
$$
Indeed, a section on $V$ supported in $Y$ is zero on $V\setminus Y$.
It therefore glues with the zero section on $X\setminus Y$ to a unique section on $X$, since $V\cup(X\setminus Y)=X$.
The glued section has support in $Y$.
This construction is inverse to restriction and commutes with morphisms of sheaves.

Apply these degree-zero isomorphisms to the injective resolution $I^\bullet$ from step [](#s5){.pf-ref}.
They identify the complexes $\Gamma_Y(X,I^\bullet)$ and $\Gamma_Y(V,I^\bullet|_V)$.
The restricted complex resolves $\mcf|_V$ and consists of flasque sheaves.
By step [](#s3){.pf-ref}, these terms are acyclic for $\Gamma_Y(V,-)$, so its cohomology is $H_Y^i(V,\mcf|_V)$.
The first complex computes $H_Y^i(X,\mcf)$.
Taking cohomology of the natural isomorphism of complexes proves (f) in every degree, including degree zero.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove parts (a)--(f), respectively, without imposing a noetherian, separation or local compactness hypothesis on the topological space.

:::

:::

:::
