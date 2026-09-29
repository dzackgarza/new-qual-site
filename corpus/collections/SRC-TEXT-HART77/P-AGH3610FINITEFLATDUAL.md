---
schema: qual/card@1
id: P-AGH3610FINITEFLATDUAL
kind: problem
title: Duality for a finite flat morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Duality
  - Finite Morphisms
  - Ext Sheaves
  - Flatness
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four parts and both hints with the retained Hartshorne III.6.10 transcription. Checked finite-morphism duality against Stacks Project section 48.11. The proof constructs the Ext map from a pushed-forward acyclic resolution, proves the vector-bundle case, and completes the suggested degree induction by proving injectivity for every coherent sheaf before surjectivity.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
(a) Let $f: X \to Y$ be a finite morphism of noetherian schemes.
For any quasi-coherent $\mco_Y$-module $\mcg$, $\sheafhom_Y(f_* \mco_X, \mcg)$ is a quasi-coherent $f_* \mco_X$-module, hence corresponds to a quasi-coherent $\mco_X$-module, which we call $f^{!} \mcg$ (II, Ex. 5.17e).

(b) Show that for any coherent $\mcf$ on $X$ and any quasi-coherent $\mcg$ on $Y$, there is a natural isomorphism
$$
f_* \sheafhom_X(\mcf, f^{!} \mcg) \iso \sheafhom_Y(f_* \mcf, \mcg).
$$

(c) For each $i \geq 0$, construct a natural map
$$
\varphi_i: \Ext_X^i(\mcf, f^{!} \mcg) \to \Ext_Y^i(f_* \mcf, \mcg).
$$

(d) Now assume that $X$ and $Y$ are separated, $\Coh(X)$ has enough locally frees, and assume that $f_* \mco_X$ is locally free on $Y$ (this is equivalent to saying $f$ is flat — see §9). Show that $\varphi_i$ is an isomorphism for all $i$, all $\mcf$ coherent on $X$, and all $\mcg$ quasi-coherent on $Y$.
:::

::: {.hint}
For (c), first construct a map $\Ext_X^i(\mcf,f^{!}\mcg)\to\Ext_Y^i(f_*\mcf,f_*f^{!}\mcg)$ and then compose with a suitable map $f_*f^{!}\mcg\to\mcg$.
For (d), first do $i=0$, then $\mcf=\mco_X$ using (Ex. 4.1), and then $\mcf$ locally free.
Do the general case by induction on $i$, writing $\mcf$ as a quotient of a locally free sheaf.
:::

::: {.solution}
Put $\mathcal B=f_*\OO_X$.
For a finite morphism, $f_*$ preserves coherence and is exact on quasi-coherent sheaves, by restriction of scalars on affine opens [@Har10a, Proposition II.5.8 and Exercise II.5.5].
All Ext groups below are computed in the categories of all module sheaves, not only the quasi-coherent subcategories.

::: pf

::: {.pf-step #s1}

The construction in (a) defines $f^!\mcg$, and it carries a natural evaluation morphism
$$
\varepsilon_\mcg:f_*f^!\mcg=\sheafhom_Y(\mathcal B,\mcg)\longrightarrow\mcg,
\qquad \lambda\longmapsto\lambda(1).
$$

::: pf-proof

For local sections $b,b'$ of $\mathcal B$, give sheaf Hom the action $(b\lambda)(b')=\lambda(bb')$.
This is a unital associative $\mathcal B$-module action compatible with restriction.
The sheaf $\mathcal B$ is coherent, so [[P-AGH363EXTCOHERENT]], in degree zero, makes $\sheafhom_Y(\mathcal B,\mcg)$ quasi-coherent.
The affine-morphism equivalence in [[P-AGH2517AFFMOR]], part (e), therefore gives a corresponding quasi-coherent sheaf $f^!\mcg$ on $X$.
On $V=\Spec A\subseteq Y$, write $f^{-1}(V)=\Spec B$ and $\mcg|_V=\widetilde N$.
The corresponding $B$-module is $\Hom_A(B,N)$ with the displayed action.
These descriptions commute with localization because $B$ is finite over the noetherian ring $A$ and hence finitely presented.
Evaluation at $1$ is $\OO_Y$-linear and commutes with restrictions and morphisms of $\mcg$, giving $\varepsilon_\mcg$.

:::

:::

::: {.pf-step #s2}

Evaluation at $1$ gives the natural isomorphism in (b); on global sections it is $\varphi_0$.

::: pf-proof

On the affine opens of step [](#s1){.pf-ref}, write $\mcf|_{f^{-1}(V)}=\widetilde M$ for a finite $B$-module $M$.
The relevant module isomorphism is
$$
\Hom_B(M,\Hom_A(B,N))\longrightarrow\Hom_A(M,N),
\qquad h\longmapsto\bigl(m\mapsto h(m)(1)\bigr).
$$
Its inverse sends $a:M\to N$ to the map
$$
m\longmapsto\bigl(b\mapsto a(bm)\bigr).
$$
The latter is $B$-linear since replacing $m$ by $b'm$ has the same effect as replacing the argument $b$ by $bb'$.
The first composite is the identity by setting $b=1$.
For the other composite, $B$-linearity of $h$ gives $h(bm)(1)=(b h(m))(1)=h(m)(b)$.
Thus both composites are identities.
The formulas commute with localizations and with maps of $M,N$, so they identify the sheaves and prove (b).
On global Hom, the isomorphism takes $a:\mcf\to f^!\mcg$ to $\varepsilon_\mcg\circ f_*a$.

:::

:::

::: {.pf-step #s3}

The natural maps in (c) exist and commute with the long exact Ext sequences in the coherent first variable.

::: pf-proof

For any quasi-coherent sheaf $H$ on $X$, take an injective resolution $H\to I^\bullet$ in $\Mod(X)$.
One has $R^qf_*H=0$ for $q>0$: over an affine open $V\subseteq Y$, the inverse image is affine, and affine vanishing applies to $H|_{f^{-1}(V)}$ [@Har10a, Theorem III.3.5].
Consequently $f_*I^\bullet$ is a resolution of $f_*H$, although its terms need not be injective.

Choose an injective resolution $f_*H\to J^\bullet$ on $Y$.
The comparison theorem for injective resolutions gives a chain map $f_*I^\bullet\to J^\bullet$ extending the identity, unique up to homotopy.
Compose it with pushforward on Hom to get
$$
\Hom_X(\mcf,I^\bullet)\longrightarrow
\Hom_Y(f_*\mcf,f_*I^\bullet)\longrightarrow
\Hom_Y(f_*\mcf,J^\bullet).
$$
Taking cohomology defines the first map in the hint,
$$
\Ext_X^i(\mcf,H)\longrightarrow\Ext_Y^i(f_*\mcf,f_*H).
$$
Comparison maps and homotopies show that it is independent of resolutions and natural in both arguments [@Har10a, Chapter III, §1].
Now take $H=f^!\mcg$ and follow this map by the map on Ext induced by $\varepsilon_\mcg$.
The result is $\varphi_i$.
Equivalently, use a chain map $f_*I^\bullet\to J_\mcg^\bullet$ extending $\varepsilon_\mcg$, with $J_\mcg^\bullet$ an injective resolution of $\mcg$.

For a short exact sequence of coherent first arguments, pushforward is exact.
Applying Hom into the injective terms $I^q$ on $X$ and $J_\mcg^q$ on $Y$ gives short exact sequences of complexes and a morphism between them.
Their connecting maps therefore commute with $\varphi_i$.
No exactness of $f_*$ on arbitrary module sheaves is assumed.

:::

:::

::: {.pf-step #s4}

Under the hypotheses of (d), $\varphi_i$ is an isomorphism for every $i$ when the first argument $E$ is locally free of finite rank.

::: pf-proof

The sheaf $f_*E$ is locally free of finite rank on $Y$.
Indeed, over $V=\Spec A$ as in step [](#s1){.pf-ref}, $B$ is finite projective over $A$, and the module of $E$ on $\Spec B$ is finite projective over $B$.
It is a direct summand of some $B^{\oplus r}$, hence finite projective over $A$.

For a finite-rank locally free first argument, global Ext is the cohomology of its sheaf Hom [@Har10a, Propositions III.6.3 and III.6.7].
The affine cohomology comparison [[P-AGH341AFFINEMORPH]] and step [](#s2){.pf-ref} give
$$
\begin{aligned}
\Ext_X^i(E,f^!\mcg)
&\cong H^i(X,\sheafhom_X(E,f^!\mcg))\\
&\cong H^i(Y,f_*\sheafhom_X(E,f^!\mcg))\\
&\cong H^i(Y,\sheafhom_Y(f_*E,\mcg))
\cong\Ext_Y^i(f_*E,\mcg).
\end{aligned}
$$
In particular this proves the $E=\OO_X$ case suggested by the hint.

These isomorphisms give the actual map $\varphi_i$ of step [](#s3){.pf-ref}.
To check this, use there a chain map $f_*I^\bullet\to J_\mcg^\bullet$ extending evaluation.
It induces a map
$$
f_*\sheafhom_X(E,I^\bullet)
\longrightarrow\sheafhom_Y(f_*E,J_\mcg^\bullet).
$$
Both complexes are flasque resolutions of their degree-zero sheaves: tensoring an injective by a finite-rank locally free sheaf preserves injectivity [@Har10a, Lemma III.6.6], direct image preserves flasqueness, and the quasi-coherent sheaf $\sheafhom_X(E,f^!\mcg)$ has vanishing positive direct images under $f$.
The map on degree-zero sheaves is the isomorphism of step [](#s2){.pf-ref}.
Its global-section map is precisely the complex map defining $\varphi_i$, so it induces the displayed cohomology isomorphisms.

:::

:::

::: {.pf-step #s5}

For $i\ge1$, if $\varphi_j$ is an isomorphism for all coherent first arguments and all $0\le j<i$, then $\varphi_i$ is injective for all coherent first arguments.

::: pf-proof

Fix $\mcg$, and abbreviate $T^j(F)=\Ext_X^j(F,f^!\mcg)$ and $S^j(F)=\Ext_Y^j(f_*F,\mcg)$.
Choose $0\to K\to E\to F\to0$ with $E$ locally free of finite rank and $K$ coherent.
The long exact sequences have corresponding segments
$$
T^{i-1}(E)\to T^{i-1}(K)\xrightarrow{\partial_T}T^i(F)
\to T^i(E)\to T^i(K),
$$
and the same sequence with $S$ in place of $T$; step [](#s3){.pf-ref} makes the comparison commute.

Let $a\in T^i(F)$ with $\varphi_i(a)=0$.
Its image in $T^i(E)$ vanishes because $\varphi_i$ on $E$ is injective by step [](#s4){.pf-ref}.
Thus $a=\partial_T b$ for some $b\in T^{i-1}(K)$.
The image of $b$ in $S^{i-1}(K)$ has zero boundary and comes from $S^{i-1}(E)$.
Lift that element to $T^{i-1}(E)$, using step [](#s4){.pf-ref}, and subtract its image from $b$.
The adjusted element still has boundary $a$ and maps to zero in $S^{i-1}(K)$.
It is zero by the induction hypothesis, so $a=0$.
This proves injectivity for every coherent $F$ at once.

:::

:::

::: {.pf-step #s6}

Under the same induction hypothesis, $\varphi_i$ is also surjective for every coherent first argument.

::: pf-proof

Use the notation and exact sequence of step [](#s5){.pf-ref}, and take $b\in S^i(F)$.
Its image in $S^i(E)$ has a preimage $a_E\in T^i(E)$ by step [](#s4){.pf-ref}.
The image of $a_E$ in $T^i(K)$ maps to zero in $S^i(K)$ by exactness.
Step [](#s5){.pf-ref} already proved injectivity in degree $i$ for every coherent sheaf, including $K$, so this image is zero.
Hence $a_E$ lifts to some $a\in T^i(F)$.

The difference $b-\varphi_i(a)$ has zero image in $S^i(E)$ and is the boundary of an element of $S^{i-1}(K)$.
Lift this element to $T^{i-1}(K)$ by the induction hypothesis and add its boundary to $a$.
The resulting element maps to $b$, proving surjectivity.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove (a)--(c).
Step [](#s2){.pf-ref} gives the degree-zero isomorphism for every coherent first argument.
Starting with that base case, steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove by induction that every $\varphi_i$ is an isomorphism under the hypotheses of (d).
This completes all four parts and identifies the isomorphism with the map constructed in (c).

:::

:::

:::
