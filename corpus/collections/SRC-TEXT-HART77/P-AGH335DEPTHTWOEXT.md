---
schema: qual/card@1
id: P-AGH335DEPTHTWOEXT
kind: problem
title: Depth two and unique extension of sections across a point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Cohomology
  - Depth
  - Noetherian Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both conditions and the cross-reference with the retained Hartshorne Chapter III section 3 transcription. The proof identifies the ringed local space with the spectrum of the local ring, compares supported cohomology in every neighborhood, and uses affine vanishing in the converse.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme, and let $P$ be a closed point of $X$.
Show that the following conditions are equivalent:

(i) $\depth \mco_P \geq 2$;

(ii) if $U$ is any open neighborhood of $P$, then every section of $\mco_X$ over $U-P$ extends uniquely to a section of $\mco_X$ over $U$.

This generalizes (I, Ex. 3.20), in view of (II, 8.22A).
:::

::: {.solution}
Put $R=\OO_{X,P}$, let $\mathfrak m$ be its maximal ideal, and let $S=X_P$ be the local space of [[P-AGH325LOCALSPACE]].
Write $H_P^i$ for cohomology with supports in the closed singleton $\{P\}$.

<1>1. The space $S$, equipped with the inverse image of $\OO_X$, is the scheme $\Spec R$.

::: {.proof}
Choose an affine neighborhood $V=\Spec A$ of $P$ and let $\mathfrak p\subseteq A$ correspond to $P$.
Every generization of $P$ lies in every open neighborhood of $P$, hence lies in $V$.
Inside $V$, these generizations are exactly the prime ideals $\mathfrak q\subseteq\mathfrak p$.
They are the image of the localization map $\Spec A_{\mathfrak p}\to\Spec A$.
This map is a homeomorphism onto that subspace: its distinguished opens are the intersections of the subspace with the opens $D(a)$ for $a\in A$.
At the point associated to $\mathfrak q$, the map on local rings is
$$
A_{\mathfrak q}\xrightarrow{\cong}(A_{\mathfrak p})_{\mathfrak qA_{\mathfrak p}}.
$$
Thus the natural map from the inverse-image structure sheaf to the structure sheaf of $\Spec A_{\mathfrak p}$ is an isomorphism on every stalk and hence an isomorphism.
Since $A_{\mathfrak p}=R$, this proves the assertion.
The point $P$ corresponds to $\mathfrak m$.
:::

<1>2. For every open neighborhood $U$ of $P$ and every $i\ge0$, there is a natural isomorphism
$$
H_P^i(U,\OO_U)\cong H_{\mathfrak m}^i(R).
$$

::: {.proof}
The scheme $U$ is noetherian, so its underlying space is a Zariski space by [[P-AGH2317ZARISKISPACE]], part (a).
Its local space at $P$ is the same $S$, since all the generizations of $P$ lie in $U$.
Apply [[P-AGH325LOCALSPACE]] to $U$ and its structure sheaf.
By step <1>1, the result is
$$
H_P^i(U,\OO_U)\cong H_{\{\mathfrak m\}}^i(\Spec R,\OO_{\Spec R}).
$$
The comparison in [[P-AGH333LOCALCOH]], part (b), identifies the right side with $H_{\mathfrak m}^i(R)$, since $V(\mathfrak m)=\{\mathfrak m\}$.
This proves the stated comparison for arbitrary $U$, not only for affine neighborhoods.
:::

<1>3. Condition (i) implies condition (ii).

::: {.proof}
The ring $R$ is a nonzero noetherian local ring and a finite module over itself.
By [[P-AGH334DEPTHCOH]], part (b), the inequality $\depth R\ge2$ gives
$$
H_{\mathfrak m}^0(R)=H_{\mathfrak m}^1(R)=0.
$$
For any neighborhood $U$ of $P$, step <1>2 therefore makes both $H_P^0(U,\OO_U)$ and $H_P^1(U,\OO_U)$ zero.
The supported-cohomology long exact sequence from [[P-AGH323SUPPORTS]], part (e), begins
$$
0\to H_P^0(U,\OO_U)\to\Gamma(U,\OO_U)
\to\Gamma(U\setminus\{P\},\OO_U)
\to H_P^1(U,\OO_U).
$$
The two outer groups vanish, so the restriction map is an isomorphism.
Surjectivity gives existence of every extension and injectivity gives its uniqueness, as required in (ii).
:::

<1>4. Condition (ii) implies condition (i).

::: {.proof}
Take an affine neighborhood $V$ of $P$.
Condition (ii) makes $\Gamma(V,\OO_V)\to\Gamma(V\setminus\{P\},\OO_V)$ an isomorphism.
The exact sequence used in step <1>3 first gives $H_P^0(V,\OO_V)=0$.
Its continuation has the exact segment
$$
\Gamma(V,\OO_V)\to\Gamma(V\setminus\{P\},\OO_V)
\to H_P^1(V,\OO_V)\to H^1(V,\OO_V).
$$
The first arrow is surjective, and the last term is zero by [[T-COHAFF|affine vanishing]] [@Har10a, Theorem III.3.5].
Hence $H_P^1(V,\OO_V)=0$ as well.
Step <1>2 gives $H_{\mathfrak m}^0(R)=H_{\mathfrak m}^1(R)=0$.
The converse in [[P-AGH334DEPTHCOH]], part (b), now yields $\depth R\ge2$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>3 and <1>4 prove the two implications, using the local-ring comparison in steps <1>1--<1>2.
:::
:::
