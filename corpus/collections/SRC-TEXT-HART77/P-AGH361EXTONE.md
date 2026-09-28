---
schema: qual/card@1
id: P-AGH361EXTONE
kind: problem
title: Extensions of sheaves of modules are classified by $\Ext^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ext Groups
  - Extensions
  - Sheaves of Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the extension equivalence and the connecting-homomorphism assignment with the retained Hartshorne III.6.1 transcription. Checked the extension construction against Stacks Project sections 12.6 and 13.27. The proof constructs an inverse using an injective embedding and identifies its class by naturality of the specified boundary map.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $(X, \mco_X)$ be a ringed space, and let $\mcf', \mcf'' \in \Mod(X)$.
An **extension** of $\mcf''$ by $\mcf'$ is a short exact sequence
$$
0 \to \mcf' \to \mcf \to \mcf'' \to 0
$$
in $\Mod(X)$.
Two extensions are isomorphic if there is an isomorphism of the short exact sequences, inducing the identity maps on $\mcf'$ and $\mcf''$.
Given an extension as above, consider the long exact sequence arising from $\Hom(\mcf'', \wait)$, in particular the map
$$
\delta: \Hom(\mcf'', \mcf'') \to \Ext^1(\mcf'', \mcf'),
$$
and let $\xi \in \Ext^1(\mcf'', \mcf')$ be $\delta(1_{\mcf''})$.
Show that this process gives a one-to-one correspondence between isomorphism classes of extensions of $\mcf''$ by $\mcf'$, and elements of the group $\Ext^1(\mcf'', \mcf')$.
:::

::: {.solution}
Put $A=\mcf'$ and $B=\mcf''$, and take all morphisms and extensions in $\Mod(X)$.
Choose an embedding $u:A\hookrightarrow J$ into an injective sheaf and put $C=J/u(A)$, with quotient map $v:J\twoheadrightarrow C$.
Such an embedding exists for modules on a ringed space [@Har10a, Proposition III.2.2].
Write $\partial:\Hom(B,C)\to\Ext^1(B,A)$ for the connecting map associated to $0\to A\xrightarrow{u}J\xrightarrow{v}C\to0$.

<1>1. The map $\partial$ induces an isomorphism
$$
\Hom(B,C)/\im\bigl(\Hom(B,J)\xrightarrow{v\circ-}\Hom(B,C)\bigr)
\xrightarrow{\cong}\Ext^1(B,A).
$$

::: {.proof}
The long exact sequence of the right derived functors of $\Hom(B,-)$ contains
$$
\Hom(B,J)\longrightarrow\Hom(B,C)\xrightarrow{\partial}
\Ext^1(B,A)\longrightarrow\Ext^1(B,J).
$$
The last group is zero because $J$ is injective [@Har10a, Chapter III, §6].
Exactness proves the assertion.
:::

<1>2. For $c:B\to C$, the pullback sheaf
$$
E_c=J\times_C B=\ker\bigl(J\oplus B\xrightarrow{(j,b)\mapsto v(j)-c(b)}C\bigr)
$$
is an extension of $B$ by $A$, whose assigned class is $\partial(c)$.

::: {.proof}
The maps are $a\mapsto(u(a),0)$ and $(j,b)\mapsto b$.
They give an exact sequence $0\to A\to E_c\to B\to0$.
Indeed, on each stalk, surjectivity of $v$ supplies a lift of $c(b)$, and the kernel of the projection is $\ker v=u(A)$.
Projection to $J$, together with the identity on $A$ and the map $c$ on the quotient, is a morphism from this sequence to $0\to A\to J\to C\to0$.
Naturality of connecting homomorphisms therefore gives
$$
\delta_{E_c}(\id_B)=\partial(c).
$$
Step <1>1 now shows that every element of $\Ext^1(B,A)$ is the assigned class of an extension.
:::

<1>3. Every extension $0\to A\xrightarrow{a}E\xrightarrow{p}B\to0$ is isomorphic, with identity maps on its endpoints, to some $E_c$.

::: {.proof}
Injectivity of $J$ extends $u:A\to J$ across $a$ to a morphism $h:E\to J$ with $ha=u$.
The composite $vh$ vanishes on $a(A)$, so it factors uniquely as $c p$ for a morphism $c:B\to C$.
Thus
$$
E\longrightarrow E_c,\qquad e\longmapsto(h(e),p(e))
$$
is a morphism of extensions inducing the identity on $A$ and $B$.
It is an isomorphism: at a stalk, an element in its kernel lies in $a(A)$ and is zero because $u$ is injective.
For $(j,b)\in(E_c)_x$, choose $e\in E_x$ with $p(e)=b$.
Then $j-h(e)\in\ker v=u(A_x)$; adding its preimage under $u$ through $a$ adjusts $e$ to a preimage of $(j,b)$.
Hence the map is bijective on every stalk.
By step <1>2 and naturality under an isomorphism of extensions, the class assigned to $E$ is $\partial(c)$.
:::

<1>4. Two extensions have the same assigned class if and only if they are isomorphic as extensions.

::: {.proof}
An isomorphism of extensions has identity endpoint maps, so naturality of the long exact sequence makes their values of $\delta(\id_B)$ equal.

Conversely, use step <1>3 to express the two extensions as $E_c$ and $E_d$.
If their assigned classes agree, then $\partial(c)=\partial(d)$ by step <1>2.
Step <1>1 supplies $t:B\to J$ with $d-c=vt$.
The map
$$
E_c\longrightarrow E_d,\qquad (j,b)\longmapsto(j+t(b),b)
$$
is defined because $v(j+t(b))=c(b)+(d-c)(b)=d(b)$.
Its inverse subtracts $t(b)$.
It fixes both endpoints and is therefore the required extension isomorphism.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>2 proves surjectivity of the specified assignment, and step <1>4 proves that its fibres are exactly the isomorphism classes of extensions.
Thus it gives the requested bijection.
The zero class corresponds to the split extension: by exactness, $\delta(\id_B)=0$ exactly when $\id_B$ lifts to a morphism $B\to E$, which is a splitting.
:::
:::
